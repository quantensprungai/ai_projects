#!/usr/bin/env python3
"""
Layer-2: 4C Windfarm Sample → imc_wind_farms + imc_farm_design (+ milestones/events).

Voraussetzung: ingest_raw.py + Schema v1 + Raw-Mirror + Seed + IMC_ETL_ACCOUNT_ID.

Beispiel:
  python transform_4c_windfarm.py --snapshot-id <uuid>
  python transform_4c_windfarm.py --latest
"""

from __future__ import annotations

import argparse
import re
import sys
from decimal import Decimal, InvalidOperation

import psycopg
from dotenv import load_dotenv

from config import (
    FOURC_STATUS_TO_LIFECYCLE,
    SOURCE_4C_WINDFARM,
    get_database_url,
    get_etl_account_id,
)

load_dotenv()

FOUNDATION_MAP = {
    "monopile": "monopile",
    "jacket": "jacket",
    "gravity-base": "gravity_based",
    "gravity base": "gravity_based",
    "tripod": "tripod",
    "tripile": "tripile",
    "suction bucket": "suction_bucket",
    "semi-submersible": "semi_submersible",
    "semi submersible": "semi_submersible",
    "spar": "spar",
    "tension leg": "tension_leg",
    "floating": "semi_submersible",
}


def map_lifecycle(status: str | None) -> str:
    if not status:
        return "planning"
    key = status.strip().lower()
    return FOURC_STATUS_TO_LIFECYCLE.get(key, "planning")


def map_foundation(raw: str | None) -> tuple[str | None, str | None]:
    if not raw:
        return None, None
    detail = raw.strip()
    lower = detail.lower()
    fixed_or_floating = "floating" if "floating" in lower else "fixed"
    for token, enum_val in FOUNDATION_MAP.items():
        if token in lower:
            return enum_val, detail
    if "not specified" in lower or "not decided" in lower:
        return "unknown", detail
    return "other", detail


def parse_aliases(other_names: str | None, windfarm_id: str | None) -> list[str] | None:
    parts: list[str] = []
    if windfarm_id:
        parts.append(f"4C:{windfarm_id}")
    if other_names:
        parts.extend([p.strip() for p in re.split(r"[,;]", other_names) if p.strip()])
    return parts or None


def blank_to_none(value):
    if isinstance(value, str) and not value.strip():
        return None
    return value


def numeric_or_none(value, max_abs: str | None = None):
    if value is None:
        return None
    try:
        number = Decimal(str(value))
    except (InvalidOperation, ValueError):
        return None
    if max_abs is not None and abs(number) > Decimal(max_abs):
        return None
    return number


def transform_row(cur: psycopg.Cursor, account_id: str, source_id: str, payload: dict) -> None:
    payload = {key: blank_to_none(value) for key, value in payload.items()}

    if payload.get("Name") is None:
        return

    windfarm_id = payload.get("WindfarmId")
    lifecycle = map_lifecycle(payload.get("WindfarmStatus"))
    foundation_type, foundation_detail = map_foundation(payload.get("Foundation"))
    lat, lon = payload.get("Lat"), payload.get("Lon")

    country = payload.get("CountryName") or "Unknown"
    aliases = parse_aliases(payload.get("OtherNames"), str(windfarm_id) if windfarm_id else None)

    cur.execute(
        """
        SELECT farm_id FROM public.imc_wind_farms
        WHERE name = %s AND country = %s
        LIMIT 1
        """,
        (payload.get("Name"), country),
    )
    row = cur.fetchone()
    if row:
        farm_id = row[0]
        cur.execute(
            """
            UPDATE public.imc_wind_farms SET
                aliases = COALESCE(%s, aliases),
                region = COALESCE(%s, region),
                georegion = COALESCE(%s, georegion),
                sea_basin = COALESCE(%s, sea_basin),
                lifecycle_phase = %s::public.imc_lifecycle_phase,
                project_url = COALESCE(%s, project_url),
                location = CASE WHEN %s IS NOT NULL AND %s IS NOT NULL
                    THEN ST_SetSRID(ST_MakePoint(%s::float8, %s::float8), 4326)
                    ELSE location END,
                source_id = %s,
                updated_at = now()
            WHERE farm_id = %s
            """,
            (
                aliases,
                payload.get("Region"),
                payload.get("Georegion"),
                payload.get("SeaName"),
                lifecycle,
                payload.get("Website"),
                lat,
                lon,
                lon,
                lat,
                source_id,
                farm_id,
            ),
        )
    else:
        cur.execute(
            """
            INSERT INTO public.imc_wind_farms (
                account_id, name, aliases, country, region, georegion, sea_basin,
                lifecycle_phase, project_url, location, source_id
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, %s,
                %s::public.imc_lifecycle_phase, %s,
                CASE WHEN %s IS NOT NULL AND %s IS NOT NULL
                     THEN ST_SetSRID(ST_MakePoint(%s::float8, %s::float8), 4326)
                     ELSE NULL END,
                %s
            )
            RETURNING farm_id
            """,
            (
                account_id,
                payload.get("Name"),
                aliases,
                country,
                payload.get("Region"),
                payload.get("Georegion"),
                payload.get("SeaName"),
                lifecycle,
                payload.get("Website"),
                lat,
                lon,
                lon,
                lat,
                source_id,
            ),
        )
        farm_id = cur.fetchone()[0]

    cur.execute(
        """
        INSERT INTO public.imc_farm_design (
            farm_id, rated_capacity_mw_min, rated_capacity_mw_max,
            is_estimated_turbine, turbine_mw_min, turbine_mw_max,
            num_turbines_min, num_turbines_max, foundation_type, foundation_detail,
            foundation_comments, fixed_or_floating,
            water_depth_min_m, water_depth_max_m, distance_from_shore_km,
            dist_shore_auto_km, site_area_km2, power_density_mw_km2,
            mean_wind_speed_100m, mean_wind_speed_150m, design_lifetime_years,
            mod_capacity_mw, source_id
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s::public.imc_foundation_type, %s, %s,
            CASE WHEN %s = 'floating' THEN 'floating'::public.imc_fixed_or_floating
                 ELSE 'fixed'::public.imc_fixed_or_floating END,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
        ON CONFLICT (farm_id) DO UPDATE SET
            rated_capacity_mw_min = EXCLUDED.rated_capacity_mw_min,
            rated_capacity_mw_max = EXCLUDED.rated_capacity_mw_max,
            foundation_type = EXCLUDED.foundation_type,
            updated_at = now()
        """,
        (
            farm_id,
                numeric_or_none(payload.get("CapacityMWMin"), "999999.99"),
                numeric_or_none(payload.get("CapacityMWMax"), "999999.99"),
            str(payload.get("IsEstimatedTurbine") or "").lower() in ("yes", "true", "1"),
                numeric_or_none(payload.get("TurbineMWMin"), "9999.99"),
                numeric_or_none(payload.get("TurbineMWMax"), "9999.99"),
            payload.get("NoTurbinesMin"),
            payload.get("NoTurbinesMax"),
            foundation_type,
            foundation_detail,
            payload.get("FoundationComments"),
            "floating" if foundation_type in ("semi_submersible", "spar", "tension_leg") else "fixed",
                numeric_or_none(payload.get("WaterDepthMinM"), "99999.9"),
                numeric_or_none(payload.get("WaterDepthMaxM"), "99999.9"),
                numeric_or_none(payload.get("DistanceFromShoreQuoted"), "99999.99"),
                numeric_or_none(payload.get("DistanceFromShoreAuto"), "99999.99"),
                numeric_or_none(payload.get("AreaSqKm"), "999999.99"),
                numeric_or_none(payload.get("MWkm2"), "9999.99"),
                numeric_or_none(payload.get("WindSpeed100m"), "999.99"),
                numeric_or_none(payload.get("WindSpeed150m"), "999.99"),
            payload.get("ExpectedLifeYears"),
                numeric_or_none(payload.get("ModelledCapacityMW"), "999999.99"),
            source_id,
        ),
    )


def resolve_snapshot_id(conn: psycopg.Connection, snapshot_id: str | None, latest: bool) -> str:
    with conn.cursor() as cur:
        if latest:
            cur.execute(
                """
                SELECT snapshot_id FROM public.imc_source_snapshots
                WHERE source_id = %s
                ORDER BY ingested_at DESC
                LIMIT 1
                """,
                (SOURCE_4C_WINDFARM,),
            )
        else:
            cur.execute(
                "SELECT snapshot_id FROM public.imc_source_snapshots WHERE snapshot_id = %s",
                (snapshot_id,),
            )
        row = cur.fetchone()
    if not row:
        raise RuntimeError("Kein Snapshot gefunden — zuerst ingest_raw.py ausführen")
    return str(row[0])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot-id")
    parser.add_argument("--latest", action="store_true")
    args = parser.parse_args()
    if not args.latest and not args.snapshot_id:
        parser.error("--snapshot-id oder --latest erforderlich")

    account_id = get_etl_account_id()

    with psycopg.connect(get_database_url()) as conn:
        snapshot_id = resolve_snapshot_id(conn, args.snapshot_id, args.latest)
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT payload FROM public.imc_source_raw_rows
                WHERE snapshot_id = %s AND sheet_name = 'Windfarm Project Details'
                ORDER BY source_row_num
                """,
                (snapshot_id,),
            )
            rows = cur.fetchall()
            if not rows:
                cur.execute(
                    """
                    SELECT payload FROM public.imc_source_raw_rows
                    WHERE snapshot_id = %s
                    ORDER BY source_row_num
                    """,
                    (snapshot_id,),
                )
                rows = cur.fetchall()

            count = 0
            for (payload,) in rows:
                transform_row(cur, account_id, SOURCE_4C_WINDFARM, payload)
                count += 1
        conn.commit()

    print(f"Transform OK: {count} Zeilen verarbeitet (snapshot={snapshot_id})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
