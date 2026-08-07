#!/usr/bin/env python3
"""
Layer-1: MaStR → imc_source_snapshots + imc_source_raw_rows (bnetza_mastr).

Unterstützt:
  - XML-Ordner (Gesamtdatenexport-Ausschnitt, UTF-16)
  - CSV (Browser-Export / Fixture)

XML-Default-Objekte:
  EinheitenWind, AnlagenEegWind, Katalogwerte, Katalogkategorien

Beispiel:
  python ingest_mastr.py --xml-dir "C:/Users/he5013/academiccloudsync/.../Extraction/MaStR"
  python ingest_mastr.py --xml-dir ... --scope offshore
  python ingest_mastr.py --file fixtures/mastr_units_offshore_sample.csv
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any, Iterable, Iterator

import psycopg
from dotenv import load_dotenv

from config import SOURCE_MASTR, get_database_url

load_dotenv()

DEFAULT_XML_OBJECTS = (
    "EinheitenWind",
    "AnlagenEegWind",
    "Katalogwerte",
    "Katalogkategorien",
)

XML_OBJECT_SPECS: dict[str, dict[str, str]] = {
    "EinheitenWind": {
        "file": "EinheitenWind.xml",
        "record_tag": "EinheitWind",
        "sheet_name": "EinheitenWind",
        "key_field": "EinheitMastrNummer",
    },
    "AnlagenEegWind": {
        "file": "AnlagenEegWind.xml",
        "record_tag": "AnlageEegWind",
        "sheet_name": "AnlagenEegWind",
        "key_field": "EegMaStRNummer",
    },
    "Katalogwerte": {
        "file": "Katalogwerte.xml",
        "record_tag": "Katalogwert",
        "sheet_name": "Katalogwerte",
        "key_field": "Id",
    },
    "Katalogkategorien": {
        "file": "Katalogkategorien.xml",
        "record_tag": "Katalogkategorie",
        "sheet_name": "Katalogkategorien",
        "key_field": "Id",
    },
}

# Catalog field enrichments on EinheitenWind payloads
UNIT_CATALOG_FIELDS = (
    "WindAnLandOderAufSee",
    "EinheitBetriebsstatus",
    "EinheitSystemstatus",
    "Energietraeger",
    "Land",
    "Bundesland",
)

OFFSHORE_CATALOG_ID = "889"
BATCH_SIZE = 2000
TAG_VALUE_RE = re.compile(r"<([A-Za-z0-9_]+)>([^<]*)</\1>")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_manifest(paths: list[Path]) -> str:
    h = hashlib.sha256()
    for path in sorted(paths, key=lambda p: p.name.lower()):
        h.update(path.name.encode("utf-8"))
        h.update(b"\0")
        h.update(sha256_file(path).encode("ascii"))
        h.update(b"\0")
    return h.hexdigest()


def blank_to_none(value: object) -> object:
    if value is None:
        return None
    if isinstance(value, str) and not value.strip():
        return None
    return value


def parse_flat_record(block: str) -> dict[str, Any]:
    payload: dict[str, Any] = {}
    for tag, value in TAG_VALUE_RE.findall(block):
        cleaned = blank_to_none(value)
        if cleaned is None:
            continue
        # Keep first value; nested/repeated tags are rare in these objects
        if tag not in payload:
            payload[tag] = cleaned
    return payload


def iter_xml_records(path: Path, record_tag: str) -> Iterator[tuple[int, dict[str, Any]]]:
    open_tag = f"<{record_tag}>"
    close_tag = f"</{record_tag}>"
    buffer = ""
    row_num = 0
    with path.open("r", encoding="utf-16") as handle:
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            buffer += chunk
            while True:
                start = buffer.find(open_tag)
                if start < 0:
                    # retain possible partial open tag
                    keep = max(len(open_tag) - 1, 0)
                    buffer = buffer[-keep:] if keep else ""
                    break
                end = buffer.find(close_tag, start)
                if end < 0:
                    buffer = buffer[start:]
                    break
                end += len(close_tag)
                block = buffer[start:end]
                buffer = buffer[end:]
                row_num += 1
                payload = parse_flat_record(block)
                if payload:
                    yield row_num, payload


def load_csv_rows(path: Path) -> list[tuple[str, int, str | None, dict]]:
    rows_out: list[tuple[str, int, str | None, dict]] = []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV ohne Header")
        for idx, row in enumerate(reader, start=2):
            payload = {
                str(k).strip(): blank_to_none(v)
                for k, v in row.items()
                if k is not None and str(k).strip()
            }
            if not any(v is not None for v in payload.values()):
                continue
            ext_key = (
                payload.get("EinheitMastrNummer")
                or payload.get("MaStR-Nr. der Einheit")
                or payload.get("MaStR-Nr der Einheit")
            )
            rows_out.append(
                ("EinheitenWind", idx, str(ext_key) if ext_key is not None else None, payload)
            )
    return rows_out


def build_catalog_lookup(katalogwerte_path: Path) -> dict[str, str]:
    lookup: dict[str, str] = {}
    for _, payload in iter_xml_records(katalogwerte_path, "Katalogwert"):
        cid = payload.get("Id")
        wert = payload.get("Wert")
        if cid is not None and wert is not None:
            lookup[str(cid)] = str(wert)
    return lookup


def enrich_unit_payload(payload: dict[str, Any], catalog: dict[str, str]) -> dict[str, Any]:
    out = dict(payload)
    for field in UNIT_CATALOG_FIELDS:
        raw = out.get(field)
        if raw is None:
            continue
        label = catalog.get(str(raw))
        if label:
            out[f"{field}_label"] = label
    return out


def is_offshore_unit(payload: dict[str, Any]) -> bool:
    code = str(payload.get("WindAnLandOderAufSee") or "")
    if code == OFFSHORE_CATALOG_ID:
        return True
    label = str(payload.get("WindAnLandOderAufSee_label") or "").casefold()
    return "auf see" in label


def load_xml_dir_rows(
    xml_dir: Path,
    objects: Iterable[str],
    scope: str,
) -> tuple[list[Path], list[tuple[str, int, str | None, dict]]]:
    paths: list[Path] = []
    rows: list[tuple[str, int, str | None, dict]] = []

    catalog: dict[str, str] = {}
    katalogwerte_spec = XML_OBJECT_SPECS["Katalogwerte"]
    katalogwerte_path = xml_dir / katalogwerte_spec["file"]
    if katalogwerte_path.exists() and "Katalogwerte" in set(objects):
        print(f"Katalog-Lookup laden: {katalogwerte_path.name} ...")
        catalog = build_catalog_lookup(katalogwerte_path)
        print(f"  {len(catalog)} Katalogwerte")

    for object_name in objects:
        spec = XML_OBJECT_SPECS[object_name]
        path = xml_dir / spec["file"]
        if not path.exists():
            raise FileNotFoundError(f"Fehlt: {path}")
        paths.append(path)

        sheet = spec["sheet_name"]
        record_tag = spec["record_tag"]
        key_field = spec["key_field"]
        kept = 0
        seen = 0
        print(f"Parse {path.name} ({record_tag}) ...")
        for row_num, payload in iter_xml_records(path, record_tag):
            seen += 1
            if object_name == "EinheitenWind":
                payload = enrich_unit_payload(payload, catalog)
                if scope == "offshore" and not is_offshore_unit(payload):
                    continue
            ext_key = payload.get(key_field)
            rows.append(
                (
                    sheet,
                    row_num,
                    str(ext_key) if ext_key is not None else None,
                    payload,
                )
            )
            kept += 1
            if seen % 10000 == 0:
                print(f"  ... {seen} gelesen, {kept} behalten")
        print(f"  fertig: {seen} gelesen, {kept} behalten → sheet={sheet}")

    return paths, rows


def upsert_snapshot(
    conn: psycopg.Connection,
    source_id: str,
    source_file: str,
    file_hash: str,
    row_count: int,
    notes: str,
) -> str:
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE public.imc_data_sources
            SET snapshot_date = %s, file_hash = %s, source_type = 'bnetza_mastr'
            WHERE source_id = %s
            """,
            (date.today(), file_hash, source_id),
        )
        cur.execute(
            """
            INSERT INTO public.imc_source_snapshots
                (source_id, source_file, file_hash, row_count, notes)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (source_id, file_hash) DO UPDATE SET
                row_count = EXCLUDED.row_count,
                notes = EXCLUDED.notes,
                ingested_at = now()
            RETURNING snapshot_id
            """,
            (source_id, source_file, file_hash, row_count, notes),
        )
        snapshot_id = cur.fetchone()[0]
    conn.commit()
    return str(snapshot_id)


def insert_raw_rows(
    conn: psycopg.Connection,
    snapshot_id: str,
    source_id: str,
    rows: list[tuple[str, int, str | None, dict]],
) -> int:
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM public.imc_source_raw_rows WHERE snapshot_id = %s",
            (snapshot_id,),
        )
        for i in range(0, len(rows), BATCH_SIZE):
            batch = rows[i : i + BATCH_SIZE]
            cur.executemany(
                """
                INSERT INTO public.imc_source_raw_rows
                    (snapshot_id, source_id, sheet_name, source_row_num, ext_record_key, payload)
                VALUES (%s, %s, %s, %s, %s, %s::jsonb)
                """,
                [
                    (
                        snapshot_id,
                        source_id,
                        sheet,
                        row_num,
                        ext_key,
                        json.dumps(payload, ensure_ascii=False),
                    )
                    for sheet, row_num, ext_key, payload in batch
                ],
            )
            print(f"  insert {min(i + BATCH_SIZE, len(rows))}/{len(rows)}")
    conn.commit()
    return len(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="MaStR XML/CSV → raw mirror")
    parser.add_argument("--file", type=Path, help="CSV-Datei (Fixture/Browser-Export)")
    parser.add_argument(
        "--xml-dir",
        type=Path,
        help="Ordner mit EinheitenWind.xml / AnlagenEegWind.xml / Katalog*.xml",
    )
    parser.add_argument("--source-id", default=SOURCE_MASTR)
    parser.add_argument(
        "--scope",
        choices=("offshore", "all-wind"),
        default="offshore",
        help="EinheitenWind: nur See (889) oder alle Wind-Einheiten",
    )
    parser.add_argument(
        "--objects",
        default=",".join(DEFAULT_XML_OBJECTS),
        help="Kommagetrennte XML-Objekte",
    )
    args = parser.parse_args()

    if bool(args.file) == bool(args.xml_dir):
        print("Bitte genau eines von --file oder --xml-dir angeben", file=sys.stderr)
        return 1

    if args.file:
        path = args.file.resolve()
        if not path.exists():
            print(f"Datei nicht gefunden: {path}", file=sys.stderr)
            return 1
        file_hash = sha256_file(path)
        rows = load_csv_rows(path)
        source_file = str(path)
        notes = "ingest_mastr.py csv"
        print(
            f"Gelesen: {len(rows)} CSV-Zeilen aus {path.name} "
            f"(sha256={file_hash[:12]}...)"
        )
    else:
        xml_dir = args.xml_dir.resolve()
        if not xml_dir.is_dir():
            print(f"Ordner nicht gefunden: {xml_dir}", file=sys.stderr)
            return 1
        objects = [o.strip() for o in args.objects.split(",") if o.strip()]
        unknown = [o for o in objects if o not in XML_OBJECT_SPECS]
        if unknown:
            print(f"Unbekannte Objekte: {unknown}", file=sys.stderr)
            return 1
        paths, rows = load_xml_dir_rows(xml_dir, objects, args.scope)
        file_hash = sha256_manifest(paths)
        source_file = str(xml_dir)
        notes = f"ingest_mastr.py xml scope={args.scope} objects={','.join(objects)}"
        print(
            f"Gelesen: {len(rows)} XML-Records aus {xml_dir} "
            f"(scope={args.scope}, sha256={file_hash[:12]}...)"
        )

    with psycopg.connect(get_database_url()) as conn:
        snapshot_id = upsert_snapshot(
            conn, args.source_id, source_file, file_hash, len(rows), notes
        )
        print(f"Snapshot {snapshot_id} — schreibe raw rows ...")
        n = insert_raw_rows(conn, snapshot_id, args.source_id, rows)

    by_sheet: dict[str, int] = {}
    for sheet, *_rest in rows:
        by_sheet[sheet] = by_sheet.get(sheet, 0) + 1
    print(f"Import OK: snapshot_id={snapshot_id}, rows={n}")
    for sheet, count in sorted(by_sheet.items()):
        print(f"  {sheet}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
