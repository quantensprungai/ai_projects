#!/usr/bin/env python3
"""
Layer-2a: MaStR raw units → park aggregates + DE farm match candidates.

Keine automatische Übernahme in 4C-Felder. Review → apply_mastr_matches.py.

Beispiel:
  python match_mastr_de.py --latest
  python match_mastr_de.py --snapshot-id <uuid> --min-score 0.75
"""

from __future__ import annotations

import argparse
import hashlib
import math
import re
import sys
from collections import defaultdict
from datetime import date, datetime
from difflib import SequenceMatcher
from typing import Any

import psycopg
from dotenv import load_dotenv
from psycopg.types.json import Jsonb

from config import SOURCE_MASTR, get_database_url

load_dotenv()

# Rough DE North Sea / Baltic offshore window (WGS84)
OFFSHORE_BBOX = (3.0, 53.0, 15.0, 56.8)

# MaStR catalog: WindAnLandOderAufSee 889 = Windkraft auf See
OFFSHORE_LAND_SEE_IDS = {"889"}

FIELD_ALIASES: dict[str, tuple[str, ...]] = {
    "unit_id": (
        "EinheitMastrNummer",
        "MaStR-Nr. der Einheit",
        "MaStR-Nr der Einheit",
    ),
    "name_windpark": ("NameWindpark", "Name des Windparks"),
    "anzeige_name": (
        "AnzeigeNameDerEinheit",
        "Anzeige-Name der Einheit",
        "Name der Einheit",
        "NameStromerzeugungseinheit",
    ),
    "capacity_kw": ("Bruttoleistung", "Bruttoleistung der Einheit"),
    "commissioning": (
        "Inbetriebnahmedatum",
        "Inbetriebnahmedatum der Einheit",
    ),
    "lat": ("Breitengrad",),
    "lon": ("Laengengrad", "Längengrad"),
    "energietraeger": ("Energietraeger", "Energieträger"),
    "land_or_sea": ("WindAnLandOderAufSee", "Lage", "WindSeeLage"),
    "land_or_sea_label": ("WindAnLandOderAufSee_label",),
}


def pick(payload: dict[str, Any], key: str) -> Any:
    for alias in FIELD_ALIASES[key]:
        if alias in payload and payload[alias] not in (None, ""):
            return payload[alias]
    return None


def normalize_name(value: str | None) -> str | None:
    if not value:
        return None
    text = value.casefold().strip()
    text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    drop = {
        "windpark",
        "wind",
        "park",
        "offshore",
        "owf",
        "owp",
        "gmbh",
        "ag",
        "the",
        "of",
    }
    tokens = [t for t in text.split() if t and t not in drop]
    return " ".join(tokens) or None


def parse_float(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().replace(" ", "").replace(",", ".")
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def parse_date(value: Any) -> date | None:
    if value is None:
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    text = str(value).strip()
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(text[:10], fmt).date()
        except ValueError:
            continue
    return None


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlmb = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlmb / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def park_key_for(name: str) -> str:
    norm = normalize_name(name) or name.casefold()
    digest = hashlib.sha1(norm.encode("utf-8")).hexdigest()[:12]
    return f"mastr:{digest}"


def looks_offshore(payload: dict[str, Any], lat: float | None, lon: float | None) -> bool:
    code = str(pick(payload, "land_or_sea") or "")
    if code in OFFSHORE_LAND_SEE_IDS:
        return True
    label = str(pick(payload, "land_or_sea_label") or "").casefold()
    if "auf see" in label or label == "offshore":
        return True
    # Legacy CSV fixtures without WindAnLandOderAufSee
    lage = label or code.casefold()
    if "see" in lage or "offshore" in lage:
        return True
    name = str(pick(payload, "name_windpark") or pick(payload, "anzeige_name") or "")
    if "offshore" in name.casefold():
        return True
    if lat is not None and lon is not None:
        west, south, east, north = OFFSHORE_BBOX
        if west <= lon <= east and south <= lat <= north:
            # Only accept bbox fallback when NameWindpark present (avoid random coastal onshore)
            return pick(payload, "name_windpark") is not None
    return False


def load_latest_snapshot_id(cur: psycopg.Cursor, source_id: str) -> str | None:
    cur.execute(
        """
        SELECT snapshot_id
        FROM public.imc_source_snapshots
        WHERE source_id = %s
        ORDER BY ingested_at DESC
        LIMIT 1
        """,
        (source_id,),
    )
    row = cur.fetchone()
    return str(row[0]) if row else None


def build_park_aggs(
    raw_rows: list[tuple[dict[str, Any]]],
) -> dict[str, dict[str, Any]]:
    buckets: dict[str, dict[str, Any]] = {}
    for (payload,) in raw_rows:
        lat = parse_float(pick(payload, "lat"))
        lon = parse_float(pick(payload, "lon"))
        if not looks_offshore(payload, lat, lon):
            continue
        name = pick(payload, "name_windpark") or pick(payload, "anzeige_name")
        if not name:
            continue
        name = str(name).strip()
        key = park_key_for(name)
        bucket = buckets.get(key)
        if bucket is None:
            bucket = {
                "park_key": key,
                "name_windpark": name,
                "unit_count": 0,
                "capacity_kw_sum": 0.0,
                "commissioning_min": None,
                "commissioning_max": None,
                "lat_sum": 0.0,
                "lon_sum": 0.0,
                "coord_n": 0,
                "sample_ids": [],
            }
            buckets[key] = bucket

        bucket["unit_count"] += 1
        kw = parse_float(pick(payload, "capacity_kw"))
        if kw is not None:
            bucket["capacity_kw_sum"] += kw
        commissioned = parse_date(pick(payload, "commissioning"))
        if commissioned is not None:
            cmin = bucket["commissioning_min"]
            cmax = bucket["commissioning_max"]
            bucket["commissioning_min"] = commissioned if cmin is None else min(cmin, commissioned)
            bucket["commissioning_max"] = commissioned if cmax is None else max(cmax, commissioned)
        if lat is not None and lon is not None:
            bucket["lat_sum"] += lat
            bucket["lon_sum"] += lon
            bucket["coord_n"] += 1
        unit_id = pick(payload, "unit_id")
        if unit_id is not None and len(bucket["sample_ids"]) < 8:
            bucket["sample_ids"].append(str(unit_id))
    return buckets


def upsert_park_aggs(
    cur: psycopg.Cursor,
    snapshot_id: str,
    source_id: str,
    parks: dict[str, dict[str, Any]],
) -> int:
    cur.execute(
        "DELETE FROM public.imc_mastr_park_agg WHERE snapshot_id = %s",
        (snapshot_id,),
    )
    # Also drop orphans from older snapshots for this source when rebuilding latest
    cur.execute(
        """
        DELETE FROM public.imc_mastr_park_agg a
        USING public.imc_source_snapshots s
        WHERE a.snapshot_id = s.snapshot_id
          AND s.source_id = %s
          AND a.snapshot_id <> %s
        """,
        (source_id, snapshot_id),
    )
    for park in parks.values():
        lat_avg = park["lat_sum"] / park["coord_n"] if park["coord_n"] else None
        lon_avg = park["lon_sum"] / park["coord_n"] if park["coord_n"] else None
        cur.execute(
            """
            INSERT INTO public.imc_mastr_park_agg (
              park_key, snapshot_id, name_windpark, unit_count, capacity_kw_sum,
              commissioning_min, commissioning_max, lat_avg, lon_avg,
              sample_mastr_unit_ids, source_id, evidence, updated_at
            ) VALUES (
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb, now()
            )
            ON CONFLICT (park_key) DO UPDATE SET
              snapshot_id = EXCLUDED.snapshot_id,
              name_windpark = EXCLUDED.name_windpark,
              unit_count = EXCLUDED.unit_count,
              capacity_kw_sum = EXCLUDED.capacity_kw_sum,
              commissioning_min = EXCLUDED.commissioning_min,
              commissioning_max = EXCLUDED.commissioning_max,
              lat_avg = EXCLUDED.lat_avg,
              lon_avg = EXCLUDED.lon_avg,
              sample_mastr_unit_ids = EXCLUDED.sample_mastr_unit_ids,
              source_id = EXCLUDED.source_id,
              evidence = EXCLUDED.evidence,
              updated_at = now()
            """,
            (
                park["park_key"],
                snapshot_id,
                park["name_windpark"],
                park["unit_count"],
                park["capacity_kw_sum"] or None,
                park["commissioning_min"],
                park["commissioning_max"],
                lat_avg,
                lon_avg,
                park["sample_ids"] or None,
                source_id,
                Jsonb({"normalized_name": normalize_name(park["name_windpark"])}),
            ),
        )
    return len(parks)


def load_de_farms(cur: psycopg.Cursor) -> list[dict[str, Any]]:
    cur.execute(
        """
        SELECT
          wf.farm_id,
          wf.name,
          wf.aliases,
          wf.ext_windfarm_id,
          ST_Y(wf.location) AS lat,
          ST_X(wf.location) AS lon,
          fd.rated_capacity_mw_max
        FROM public.imc_wind_farms wf
        LEFT JOIN public.imc_farm_design fd ON fd.farm_id = wf.farm_id
        WHERE wf.country = 'Germany'
          AND wf.lifecycle_phase <> 'cancelled'
        """
    )
    cols = [d.name for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def alias_norms(farm: dict[str, Any]) -> set[str]:
    norms: set[str] = set()
    name_n = normalize_name(farm["name"])
    if name_n:
        norms.add(name_n)
    for alias in farm.get("aliases") or []:
        # skip technical 4C:DE01 markers
        if str(alias).startswith("4C:") or str(alias).startswith("MaStR:"):
            continue
        n = normalize_name(str(alias))
        if n:
            norms.add(n)
    return norms


def trailing_number(norm: str | None) -> str | None:
    if not norm:
        return None
    match = re.search(r"(?:^| )(\d+)$", norm)
    return match.group(1) if match else None


def capacity_score(farm_mw: float | None, park_mw: float | None) -> float | None:
    if farm_mw is None or park_mw is None or farm_mw <= 0 or park_mw <= 0:
        return None
    ratio = min(farm_mw, park_mw) / max(farm_mw, park_mw)
    return float(ratio)


def dedupe_proposals(proposals: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Keep strong name hits; suppress geo/fuzzy noise when a farm already has exact/alias."""
    by_farm: dict[Any, list[dict[str, Any]]] = defaultdict(list)
    for proposal in proposals:
        by_farm[proposal["farm_id"]].append(proposal)

    method_rank = {
        "exact_name": 0,
        "alias": 1,
        "fuzzy_name": 2,
        "geo": 3,
        "capacity": 4,
        "manual": 5,
    }
    kept: list[dict[str, Any]] = []
    for farm_proposals in by_farm.values():
        strong = [
            p
            for p in farm_proposals
            if p["method"] in ("exact_name", "alias") and p["score"] >= 0.9
        ]
        if strong:
            # one best strong match + no geo neighbors
            strong.sort(key=lambda p: (-p["score"], method_rank[p["method"]]))
            best = strong[0]
            kept.append(best)
            continue

        # no strong name hit: keep top candidate only
        farm_proposals.sort(key=lambda p: (-p["score"], method_rank[p["method"]]))
        kept.append(farm_proposals[0])
    return kept


def propose_matches(
    farms: list[dict[str, Any]],
    parks: dict[str, dict[str, Any]],
    min_score: float,
) -> list[dict[str, Any]]:
    proposals: list[dict[str, Any]] = []
    park_list = list(parks.values())

    for farm in farms:
        farm_norms = alias_norms(farm)
        farm_name_norm = normalize_name(farm["name"])
        farm_lat = farm.get("lat")
        farm_lon = farm.get("lon")
        farm_mw = float(farm["rated_capacity_mw_max"]) if farm["rated_capacity_mw_max"] is not None else None

        for park in park_list:
            park_name = park["name_windpark"]
            park_norm = normalize_name(park_name)
            park_mw = (park["capacity_kw_sum"] / 1000.0) if park["capacity_kw_sum"] else None
            park_lat = (
                park["lat_sum"] / park["coord_n"] if park["coord_n"] else None
            )
            park_lon = (
                park["lon_sum"] / park["coord_n"] if park["coord_n"] else None
            )

            method = None
            score = 0.0
            evidence: dict[str, Any] = {
                "farm_name": farm["name"],
                "park_name": park_name,
                "farm_mw": farm_mw,
                "park_mw": park_mw,
            }

            if park_norm and park_norm in farm_norms:
                method = "exact_name" if park_norm == farm_name_norm else "alias"
                score = 0.98 if method == "exact_name" else 0.95
            elif park_norm and farm_norms:
                best = max(SequenceMatcher(None, park_norm, n).ratio() for n in farm_norms)
                farm_num = trailing_number(farm_name_norm)
                park_num = trailing_number(park_norm)
                number_clash = (
                    farm_num is not None
                    and park_num is not None
                    and farm_num != park_num
                )
                # Borkum Riffgrund 1 vs 2 etc.
                if number_clash:
                    continue
                if best >= 0.90:
                    method = "fuzzy_name"
                    score = round(0.72 + 0.22 * best, 3)
                    evidence["fuzzy_ratio"] = round(best, 3)

            geo_bonus = 0.0
            dist = None
            if (
                farm_lat is not None
                and farm_lon is not None
                and park_lat is not None
                and park_lon is not None
            ):
                dist = haversine_km(float(farm_lat), float(farm_lon), park_lat, park_lon)
                evidence["dist_km"] = round(dist, 2)
                if dist <= 8:
                    geo_bonus = max(0.0, 0.1 * (1 - dist / 8))

            cap = capacity_score(farm_mw, park_mw)
            if cap is not None:
                evidence["capacity_ratio"] = round(cap, 3)

            # Pure geo: tight distance + strong capacity agreement
            if (
                method is None
                and dist is not None
                and dist <= 2.5
                and cap is not None
                and cap >= 0.85
            ):
                method = "geo"
                score = round(0.72 + geo_bonus + 0.12 * cap, 3)

            if method is None and cap is not None and cap >= 0.97 and dist is not None and dist <= 5:
                method = "capacity"
                score = round(0.68 + 0.2 * cap, 3)
            elif method is not None and cap is not None:
                score = min(1.0, score + 0.05 * cap)
                if cap < 0.5 and method in ("fuzzy_name", "geo"):
                    continue

            if method is None:
                continue

            score = min(1.0, score + geo_bonus)
            status = "candidate"
            if (
                score >= 0.93
                and method in ("exact_name", "alias")
                and (cap is None or cap >= 0.5)
            ):
                status = "needs_review"
            elif score >= 0.93 and method == "fuzzy_name" and cap is not None and cap >= 0.9:
                status = "needs_review"
            if score < min_score:
                continue

            proposals.append(
                {
                    "farm_id": farm["farm_id"],
                    "park_key": park["park_key"],
                    "method": method,
                    "score": round(score, 3),
                    "status": status,
                    "evidence": evidence,
                }
            )
    return dedupe_proposals(proposals)


def upsert_matches(cur: psycopg.Cursor, proposals: list[dict[str, Any]]) -> int:
    # Keep accepted/rejected human decisions; refresh only open candidates
    cur.execute(
        """
        DELETE FROM public.imc_mastr_farm_matches
        WHERE status IN ('candidate', 'needs_review')
        """
    )
    for p in proposals:
        cur.execute(
            """
            INSERT INTO public.imc_mastr_farm_matches (
              farm_id, park_key, method, score, status, evidence, updated_at
            ) VALUES (%s, %s, %s::public.imc_mastr_match_method, %s,
                      %s::public.imc_mastr_match_status, %s::jsonb, now())
            ON CONFLICT (farm_id, park_key, method) DO UPDATE SET
              score = EXCLUDED.score,
              status = CASE
                WHEN imc_mastr_farm_matches.status IN ('accepted', 'rejected')
                  THEN imc_mastr_farm_matches.status
                ELSE EXCLUDED.status
              END,
              evidence = EXCLUDED.evidence,
              updated_at = now()
            """,
            (
                p["farm_id"],
                p["park_key"],
                p["method"],
                p["score"],
                p["status"],
                Jsonb(p["evidence"]),
            ),
        )
    return len(proposals)


def main() -> int:
    parser = argparse.ArgumentParser(description="MaStR DE farm matching skeleton")
    parser.add_argument("--snapshot-id")
    parser.add_argument("--latest", action="store_true")
    parser.add_argument("--source-id", default=SOURCE_MASTR)
    parser.add_argument("--min-score", type=float, default=0.72)
    args = parser.parse_args()

    if not args.snapshot_id and not args.latest:
        print("Bitte --latest oder --snapshot-id angeben", file=sys.stderr)
        return 1

    with psycopg.connect(get_database_url()) as conn:
        with conn.cursor() as cur:
            snapshot_id = args.snapshot_id
            if args.latest or not snapshot_id:
                snapshot_id = load_latest_snapshot_id(cur, args.source_id)
            if not snapshot_id:
                print("Kein MaStR-Snapshot gefunden — zuerst ingest_mastr.py", file=sys.stderr)
                return 1

            cur.execute(
                """
                SELECT payload
                FROM public.imc_source_raw_rows
                WHERE snapshot_id = %s
                  AND sheet_name = 'EinheitenWind'
                """,
                (snapshot_id,),
            )
            raw_rows = cur.fetchall()
            parks = build_park_aggs(raw_rows)
            n_parks = upsert_park_aggs(cur, snapshot_id, args.source_id, parks)
            farms = load_de_farms(cur)
            proposals = propose_matches(farms, parks, args.min_score)
            n_matches = upsert_matches(cur, proposals)
        conn.commit()

    print(
        f"Match OK: snapshot={snapshot_id}, parks={n_parks}, "
        f"de_farms={len(farms)}, proposals={n_matches}"
    )
    top = sorted(proposals, key=lambda p: p["score"], reverse=True)[:8]
    for p in top:
        ev = p["evidence"]
        print(
            f"  {p['score']:.3f} {p['method']:12} {p['status']:12} "
            f"{ev.get('farm_name')} <-> {ev.get('park_name')}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
