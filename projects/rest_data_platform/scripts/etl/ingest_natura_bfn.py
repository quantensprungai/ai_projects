#!/usr/bin/env python3
"""
Ingest BfN marine Schutzgebiete into imc_protected_areas.

Quelle: https://geodienste.bfn.de/ogc/wfs/schutzgebiet_marin (GEOJSON)
Layer: FFH, SPA, NSG, LSG, Nationalparke, Naturparke, Biosphärenreservate.
Kein Planungsprodukt — Kontext-Layer für Assets-Karte + Farm-Nähe.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

import psycopg
from dotenv import load_dotenv

from config import SOURCE_NATURA2000, get_database_url

load_dotenv(Path(__file__).resolve().parent / ".env")
load_dotenv()

WFS_BASE = "https://geodienste.bfn.de/ogc/wfs/schutzgebiet_marin"

LAYERS = (
    ("bfn_sch_Schutzgebiet_marin:Fauna_Flora_Habitat_Gebiete", "FFH"),
    ("bfn_sch_Schutzgebiet_marin:Vogelschutzgebiete", "SPA"),
    ("bfn_sch_Schutzgebiet_marin:Naturschutzgebiete", "NSG"),
    ("bfn_sch_Schutzgebiet_marin:Landschaftsschutzgebiete", "LSG"),
    ("bfn_sch_Schutzgebiet_marin:Nationalparke", "NLP"),
    ("bfn_sch_Schutzgebiet_marin:Naturparke", "NRP"),
    ("bfn_sch_Schutzgebiet_marin:Biosphaerenreservate", "BR"),
)

# ~200 m at mid-latitudes — enough for map overlay, not cadastral precision
SIMPLIFY_TOLERANCE_DEG = 0.002


def fetch_layer(type_name: str) -> dict:
    params = {
        "SERVICE": "WFS",
        "VERSION": "2.0.0",
        "REQUEST": "GetFeature",
        "TYPENAMES": type_name,
        "OUTPUTFORMAT": "GEOJSON",
    }
    url = f"{WFS_BASE}?{urllib.parse.urlencode(params)}"
    print(f"GET {type_name} …")
    with urllib.request.urlopen(url, timeout=180) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    features = payload.get("features") or []
    print(f"  -> {len(features)} features")
    return payload


def feature_props(feature: dict, designation: str) -> dict:
    props = feature.get("properties") or {}
    site_code = (
        props.get("SITECODE")
        or props.get("sitecode")
        or props.get("ID")
        or props.get("GmlID")
    )
    name = props.get("NAME") or props.get("sitename") or site_code
    if not site_code or not name:
        raise ValueError(f"missing site_code/name in {props}")
    marin = props.get("MARIN_AREA")
    flaeche = props.get("FLAECHE")
    return {
        "site_code": str(site_code),
        "name": str(name),
        "designation": designation,
        "marin_area_pct": float(marin) if marin is not None else None,
        "area_ha": float(flaeche) if flaeche is not None else None,
        "link": props.get("LINK") or props.get("link"),
        "attrs": props,
    }


def upsert_feature(
    cur: psycopg.Cursor,
    *,
    feature: dict,
    designation: str,
    source_id: str,
    dry_run: bool,
) -> None:
    meta = feature_props(feature, designation)
    geometry = feature.get("geometry")
    if not geometry:
        print(f"  skip {meta['site_code']}: no geometry")
        return

    geom_json = json.dumps(geometry)
    if dry_run:
        print(f"  [dry-run] {meta['designation']} {meta['site_code']} {meta['name']}")
        return

    cur.execute(
        """
        INSERT INTO public.imc_protected_areas (
          site_code, name, designation, country, marin_area_pct, area_ha,
          link, geom, geom_simple, source_id, attrs, updated_at
        )
        VALUES (
          %(site_code)s,
          %(name)s,
          %(designation)s,
          'Germany',
          %(marin_area_pct)s,
          %(area_ha)s,
          %(link)s,
          ST_Multi(ST_SetSRID(ST_GeomFromGeoJSON(%(geom_json)s), 4326)),
          ST_Multi(
            ST_SimplifyPreserveTopology(
              ST_SetSRID(ST_GeomFromGeoJSON(%(geom_json)s), 4326),
              %(tol)s
            )
          ),
          %(source_id)s::uuid,
          %(attrs)s::jsonb,
          now()
        )
        ON CONFLICT (site_code, designation) DO UPDATE SET
          name = EXCLUDED.name,
          marin_area_pct = EXCLUDED.marin_area_pct,
          area_ha = EXCLUDED.area_ha,
          link = EXCLUDED.link,
          geom = EXCLUDED.geom,
          geom_simple = EXCLUDED.geom_simple,
          source_id = EXCLUDED.source_id,
          attrs = EXCLUDED.attrs,
          updated_at = now()
        """,
        {
            **meta,
            "geom_json": geom_json,
            "tol": SIMPLIFY_TOLERANCE_DEG,
            "source_id": source_id,
            "attrs": json.dumps(meta["attrs"], ensure_ascii=False),
        },
    )


def ensure_source_row(cur: psycopg.Cursor, source_id: str) -> None:
    cur.execute(
        """
        INSERT INTO public.imc_data_sources (
          source_id, source_type, source_name, source_version,
          license_info, snapshot_date, notes
        )
        VALUES (
          %(source_id)s::uuid,
          'natura2000',
          'BfN marine Schutzgebiete (FFH/SPA)',
          'WFS schutzgebiet_marin',
          'GeoNutzV — BfN Open Data (nicht für Planungszwecke)',
          %(today)s,
          'Thin Stage-A context layer for Assets map + farm proximity.'
        )
        ON CONFLICT (source_id) DO UPDATE SET
          snapshot_date = EXCLUDED.snapshot_date,
          notes = EXCLUDED.notes
        """,
        {"source_id": source_id, "today": date.today().isoformat()},
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest BfN marine Natura areas")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--source-id", default=SOURCE_NATURA2000)
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Delete existing Natura rows for this source before insert",
    )
    args = parser.parse_args()

    collections = [(fetch_layer(name), designation) for name, designation in LAYERS]

    with psycopg.connect(get_database_url()) as conn:
        with conn.cursor() as cur:
            if not args.dry_run:
                ensure_source_row(cur, args.source_id)
                if args.replace:
                    cur.execute(
                        "DELETE FROM public.imc_protected_areas WHERE source_id = %s::uuid",
                        (args.source_id,),
                    )
                    print(f"Deleted existing rows for source {args.source_id}")

            total = 0
            for payload, designation in collections:
                for feature in payload.get("features") or []:
                    upsert_feature(
                        cur,
                        feature=feature,
                        designation=designation,
                        source_id=args.source_id,
                        dry_run=args.dry_run,
                    )
                    total += 1

            if not args.dry_run:
                conn.commit()
                cur.execute("SELECT count(*) FROM public.imc_protected_areas")
                (count,) = cur.fetchone()
                print(f"Done. upserted≈{total}, table count={count}")
            else:
                print(f"[dry-run] would upsert {total} features")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001 — CLI surface
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
