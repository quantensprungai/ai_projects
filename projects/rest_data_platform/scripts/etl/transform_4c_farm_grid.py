#!/usr/bin/env python3
"""
Layer-2: 4C Windfarm Project Details → imc_farm_grid.

Voraussetzung: ingest_raw (windfarm) + imc_wind_farms.

  python transform_4c_farm_grid.py --latest
"""

from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation

import psycopg
from dotenv import load_dotenv

from config import SOURCE_4C_WINDFARM, get_database_url
from transform_4c_events import load_farm_index
from transform_4c_windfarm import numeric_or_none

load_dotenv()


def blank_to_none(value):
    if isinstance(value, str) and not value.strip():
        return None
    return value


def int_or_none(value) -> int | None:
    if value is None or value == "":
        return None
    try:
        return int(Decimal(str(value)))
    except (InvalidOperation, ValueError, TypeError):
        return None


def resolve_farm_id(
    payload: dict,
    by_ext: dict[str, str],
    by_name_country: dict[tuple[str, str], str],
) -> str | None:
    # Project Details uses WindfarmId; other sheets may use WindfarmID.
    windfarm_id = blank_to_none(
        payload.get("WindfarmId") or payload.get("WindfarmID")
    )
    if windfarm_id is not None:
        farm_id = by_ext.get(str(windfarm_id).strip())
        if farm_id:
            return farm_id

    name = blank_to_none(
        payload.get("Name")
        or payload.get("Windfarm Name")
        or payload.get("WindfarmName")
    )
    country = blank_to_none(payload.get("Country Name") or payload.get("CountryName"))
    if name and country:
        return by_name_country.get((str(name).strip().lower(), str(country).strip().lower()))
    return None


def upsert_grid(cur: psycopg.Cursor, farm_id: str, source_id: str, payload: dict) -> bool:
    values = {
        "num_export_cables": int_or_none(payload.get("NumExportCables")),
        "export_cable_length_km": numeric_or_none(payload.get("CableLengthExportKm"), "99999.99"),
        "export_voltage_kv": numeric_or_none(payload.get("ExportNominalVoltageKV"), "9999.9"),
        "num_dc_cables": int_or_none(payload.get("DCNumCables")),
        "dc_cable_length_km": numeric_or_none(payload.get("DCCableLengthKm"), "99999.99"),
        "dc_voltage_kv": numeric_or_none(payload.get("DCNominalVoltageKV"), "9999.9"),
        "infield_cable_length_km": numeric_or_none(payload.get("CableLengthInfieldKm"), "99999.99"),
        "infield_voltage_kv": numeric_or_none(payload.get("InfieldNominalVoltageKV"), "9999.9"),
        "mod_array_cable_km": numeric_or_none(
            payload.get("ArrayCableKm_Mod") or payload.get("ArrayCableLengthKm_Mod"),
            "99999.99",
        ),
        "mod_export_cable_km": numeric_or_none(
            payload.get("ACExportCableKm_Mod") or payload.get("ExportCableKm_Mod"),
            "99999.99",
        ),
        "num_offshore_substations": int_or_none(payload.get("NumOffshoreSubstations")),
        "mod_num_substations": int_or_none(payload.get("NumSubstations_Mod")),
        "grid_connection_point": blank_to_none(payload.get("GridConnectionPoint")),
        "landing_point": blank_to_none(payload.get("LandingPoint")),
        "export_cable_comments": blank_to_none(payload.get("ExportCableComments")),
        "infield_cable_comments": blank_to_none(payload.get("InfieldCableComments")),
    }

    if not any(v is not None for v in values.values()):
        return False

    cur.execute(
        """
        INSERT INTO public.imc_farm_grid (
            farm_id,
            num_export_cables,
            export_cable_length_km,
            export_voltage_kv,
            num_dc_cables,
            dc_cable_length_km,
            dc_voltage_kv,
            infield_cable_length_km,
            infield_voltage_kv,
            mod_array_cable_km,
            mod_export_cable_km,
            num_offshore_substations,
            mod_num_substations,
            grid_connection_point,
            landing_point,
            export_cable_comments,
            infield_cable_comments,
            source_id,
            updated_at
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now()
        )
        ON CONFLICT (farm_id) DO UPDATE SET
            num_export_cables = COALESCE(EXCLUDED.num_export_cables, imc_farm_grid.num_export_cables),
            export_cable_length_km = COALESCE(EXCLUDED.export_cable_length_km, imc_farm_grid.export_cable_length_km),
            export_voltage_kv = COALESCE(EXCLUDED.export_voltage_kv, imc_farm_grid.export_voltage_kv),
            num_dc_cables = COALESCE(EXCLUDED.num_dc_cables, imc_farm_grid.num_dc_cables),
            dc_cable_length_km = COALESCE(EXCLUDED.dc_cable_length_km, imc_farm_grid.dc_cable_length_km),
            dc_voltage_kv = COALESCE(EXCLUDED.dc_voltage_kv, imc_farm_grid.dc_voltage_kv),
            infield_cable_length_km = COALESCE(EXCLUDED.infield_cable_length_km, imc_farm_grid.infield_cable_length_km),
            infield_voltage_kv = COALESCE(EXCLUDED.infield_voltage_kv, imc_farm_grid.infield_voltage_kv),
            mod_array_cable_km = COALESCE(EXCLUDED.mod_array_cable_km, imc_farm_grid.mod_array_cable_km),
            mod_export_cable_km = COALESCE(EXCLUDED.mod_export_cable_km, imc_farm_grid.mod_export_cable_km),
            num_offshore_substations = COALESCE(EXCLUDED.num_offshore_substations, imc_farm_grid.num_offshore_substations),
            mod_num_substations = COALESCE(EXCLUDED.mod_num_substations, imc_farm_grid.mod_num_substations),
            grid_connection_point = COALESCE(EXCLUDED.grid_connection_point, imc_farm_grid.grid_connection_point),
            landing_point = COALESCE(EXCLUDED.landing_point, imc_farm_grid.landing_point),
            export_cable_comments = COALESCE(EXCLUDED.export_cable_comments, imc_farm_grid.export_cable_comments),
            infield_cable_comments = COALESCE(EXCLUDED.infield_cable_comments, imc_farm_grid.infield_cable_comments),
            source_id = COALESCE(imc_farm_grid.source_id, EXCLUDED.source_id),
            updated_at = now()
        """,
        (
            farm_id,
            values["num_export_cables"],
            values["export_cable_length_km"],
            values["export_voltage_kv"],
            values["num_dc_cables"],
            values["dc_cable_length_km"],
            values["dc_voltage_kv"],
            values["infield_cable_length_km"],
            values["infield_voltage_kv"],
            values["mod_array_cable_km"],
            values["mod_export_cable_km"],
            values["num_offshore_substations"],
            values["mod_num_substations"],
            values["grid_connection_point"],
            values["landing_point"],
            values["export_cable_comments"],
            values["infield_cable_comments"],
            source_id,
        ),
    )
    return True


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

    with psycopg.connect(get_database_url()) as conn:
        snapshot_id = resolve_snapshot_id(conn, args.snapshot_id, args.latest)
        with conn.cursor() as cur:
            by_ext, by_name_country = load_farm_index(cur)
            cur.execute(
                """
                SELECT payload FROM public.imc_source_raw_rows
                WHERE snapshot_id = %s AND sheet_name = 'Windfarm Project Details'
                ORDER BY source_row_num
                """,
                (snapshot_id,),
            )
            rows = cur.fetchall()

            upserted = 0
            skipped = 0
            for (payload,) in rows:
                if not isinstance(payload, dict):
                    skipped += 1
                    continue
                farm_id = resolve_farm_id(payload, by_ext, by_name_country)
                if not farm_id:
                    skipped += 1
                    continue
                if upsert_grid(cur, farm_id, SOURCE_4C_WINDFARM, payload):
                    upserted += 1
                else:
                    skipped += 1

        conn.commit()
        print(f"imc_farm_grid upserted={upserted} skipped={skipped} snapshot={snapshot_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
