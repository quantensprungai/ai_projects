#!/usr/bin/env python3
"""
MaStR Einheit → imc_turbines for accepted farm matches.

Uses EinheitenWind rows whose NameWindpark normalizes to the same park_key
as the matched park (hyphen/space variants like Amrumbank West / Amrumbank-West).

Beispiel:
  python transform_mastr_turbines_farm.py --ext-windfarm-id DE01
  python transform_mastr_turbines_farm.py --all-accepted
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, InvalidOperation

import psycopg
from dotenv import load_dotenv

from config import SOURCE_MASTR, get_database_url
from match_mastr_de import park_key_for
from oem_lineage import FarmModel, match_farm_model

load_dotenv()


def parse_float(value):
    if value is None or value == "":
        return None
    try:
        return float(str(value).replace(",", "."))
    except ValueError:
        return None


def parse_date(value):
    if not value:
        return None
    text = str(value).strip()[:10]
    for fmt in ("%Y-%m-%d", "%d.%m.%Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    return None


def mw_from_kw(value):
    kw = parse_float(value)
    if kw is None:
        return None
    try:
        return Decimal(str(kw)) / Decimal("1000")
    except (InvalidOperation, ValueError):
        return None


def load_targets(cur: psycopg.Cursor, *, ext_id: str | None, all_accepted: bool):
    if all_accepted:
        cur.execute(
            """
            SELECT DISTINCT ON (wf.farm_id)
              wf.farm_id, wf.name, wf.ext_windfarm_id, p.name_windpark, p.snapshot_id
            FROM public.imc_wind_farms wf
            JOIN public.imc_mastr_farm_matches m ON m.farm_id = wf.farm_id
            JOIN public.imc_mastr_park_agg p ON p.park_key = m.park_key
            WHERE m.status = 'accepted'
              AND wf.country = 'Germany'
            ORDER BY wf.farm_id, m.score DESC
            """
        )
    else:
        cur.execute(
            """
            SELECT wf.farm_id, wf.name, wf.ext_windfarm_id, p.name_windpark, p.snapshot_id
            FROM public.imc_wind_farms wf
            JOIN public.imc_mastr_farm_matches m ON m.farm_id = wf.farm_id
            JOIN public.imc_mastr_park_agg p ON p.park_key = m.park_key
            WHERE wf.ext_windfarm_id = %s
              AND m.status = 'accepted'
            ORDER BY m.score DESC
            LIMIT 1
            """,
            (ext_id,),
        )
    return cur.fetchall()


def load_units_by_park_key(
    cur: psycopg.Cursor, snapshot_id
) -> dict[str, list[dict]]:
    cur.execute(
        """
        SELECT payload
        FROM public.imc_source_raw_rows
        WHERE snapshot_id = %s
          AND sheet_name = 'EinheitenWind'
          AND nullif(trim(payload->>'NameWindpark'), '') IS NOT NULL
        """,
        (snapshot_id,),
    )
    by_key: dict[str, list[dict]] = defaultdict(list)
    for (payload,) in cur.fetchall():
        if not isinstance(payload, dict):
            continue
        name = payload.get("NameWindpark")
        if not name:
            continue
        by_key[park_key_for(str(name))].append(payload)
    return by_key


def load_catalog(cur: psycopg.Cursor, source_id: str) -> dict[str, str]:
    cur.execute(
        """
        SELECT payload->>'Id', payload->>'Wert'
        FROM public.imc_source_raw_rows
        WHERE source_id = %s
          AND sheet_name = 'Katalogwerte'
          AND payload->>'Id' IS NOT NULL
        """,
        (source_id,),
    )
    out: dict[str, str] = {}
    for cid, wert in cur.fetchall():
        if cid and wert and str(cid) not in out:
            out[str(cid)] = str(wert)
    return out


def catalog_label(payload: dict, field: str, catalog: dict[str, str]) -> str | None:
    labelled = payload.get(f"{field}_label")
    if labelled:
        text = str(labelled).strip()
        return text or None
    raw = payload.get(field)
    if raw is None or str(raw).strip() == "":
        return None
    return catalog.get(str(raw))


def load_farm_models(cur: psycopg.Cursor, farm_id) -> list[FarmModel]:
    cur.execute(
        """
        SELECT DISTINCT tm.turbine_model_id::text, tm.oem, tm.model,
               tm.rotor_diameter_m::float, tm.oem_group
        FROM public.imc_turbine_models tm
        JOIN public.imc_farm_design fd
          ON fd.turbine_model_id = tm.turbine_model_id
        WHERE fd.farm_id = %s
        UNION
        SELECT DISTINCT tm.turbine_model_id::text, tm.oem, tm.model,
               tm.rotor_diameter_m::float, tm.oem_group
        FROM public.imc_wind_farms wf
        JOIN public.imc_turbine_models tm
          ON EXISTS (
            SELECT 1
            FROM unnest(coalesce(wf.aliases, ARRAY[]::text[])) AS a
            WHERE a = ('Turbine:' || tm.oem || ' · ' || tm.model)
          )
        WHERE wf.farm_id = %s
        """,
        (farm_id, farm_id),
    )
    models: list[FarmModel] = []
    for model_id, oem, model, rotor, group in cur.fetchall():
        models.append(
            FarmModel(
                turbine_model_id=str(model_id),
                oem=oem or "",
                model=model or "",
                rotor_diameter_m=float(rotor) if rotor is not None else None,
                oem_group=group,
            )
        )
    return models


def insert_units(
    cur: psycopg.Cursor,
    *,
    farm_id,
    payloads: list[dict],
    source_id: str,
    catalog: dict[str, str],
    models: list[FarmModel],
) -> int:
    cur.execute(
        """
        DELETE FROM public.imc_turbines
        WHERE farm_id = %s AND source_id = %s
        """,
        (farm_id, source_id),
    )

    inserted = 0
    for payload in payloads:
        see = payload.get("EinheitMastrNummer")
        if not see:
            continue
        name = payload.get("NameStromerzeugungseinheit") or None
        status = catalog_label(payload, "EinheitBetriebsstatus", catalog)
        rated_mw = mw_from_kw(payload.get("Bruttoleistung"))
        commissioned = parse_date(payload.get("Inbetriebnahmedatum"))
        lat = parse_float(payload.get("Breitengrad"))
        lon = parse_float(payload.get("Laengengrad"))
        manufacturer = catalog_label(payload, "Hersteller", catalog)
        type_name = (str(payload.get("Typenbezeichnung")).strip()
                     if payload.get("Typenbezeichnung") else None)
        hub = parse_float(payload.get("Nabenhoehe"))
        rotor = parse_float(payload.get("Rotordurchmesser"))
        depth = parse_float(payload.get("Wassertiefe"))
        shore = parse_float(payload.get("Kuestenentfernung"))
        sea = catalog_label(payload, "Seelage", catalog)
        eeg = payload.get("EegMaStRNummer") or None
        model_id = match_farm_model(
            manufacturer=manufacturer,
            type_designation=type_name,
            rotor_diameter_m=rotor,
            models=models,
        )

        cur.execute(
            """
            INSERT INTO public.imc_turbines (
              farm_id, ext_unit_key, name, rated_power_mw,
              commissioning_date, status_label, location, source_id,
              turbine_model_id, manufacturer_label, type_designation,
              hub_height_m, rotor_diameter_m, water_depth_m,
              distance_shore_km, sea_area_label, eeg_mastr_nr
            ) VALUES (
              %s, %s, %s, %s, %s, %s,
              CASE
                WHEN %s IS NOT NULL AND %s IS NOT NULL
                THEN ST_SetSRID(ST_MakePoint(%s, %s), 4326)
                ELSE NULL
              END,
              %s,
              %s, %s, %s,
              %s, %s, %s,
              %s, %s, %s
            )
            ON CONFLICT (farm_id, ext_unit_key) DO UPDATE SET
              name = EXCLUDED.name,
              rated_power_mw = EXCLUDED.rated_power_mw,
              commissioning_date = EXCLUDED.commissioning_date,
              status_label = EXCLUDED.status_label,
              location = EXCLUDED.location,
              source_id = EXCLUDED.source_id,
              turbine_model_id = EXCLUDED.turbine_model_id,
              manufacturer_label = EXCLUDED.manufacturer_label,
              type_designation = EXCLUDED.type_designation,
              hub_height_m = EXCLUDED.hub_height_m,
              rotor_diameter_m = EXCLUDED.rotor_diameter_m,
              water_depth_m = EXCLUDED.water_depth_m,
              distance_shore_km = EXCLUDED.distance_shore_km,
              sea_area_label = EXCLUDED.sea_area_label,
              eeg_mastr_nr = EXCLUDED.eeg_mastr_nr,
              updated_at = now()
            """,
            (
                farm_id,
                str(see),
                name,
                rated_mw,
                commissioned,
                status,
                lon,
                lat,
                lon,
                lat,
                source_id,
                model_id,
                manufacturer,
                type_name,
                hub,
                rotor,
                depth,
                shore,
                sea,
                str(eeg) if eeg else None,
            ),
        )
        inserted += 1
    return inserted


def transform_farm(
    cur: psycopg.Cursor,
    *,
    farm_id,
    farm_name: str,
    ext_id: str | None,
    park_name: str,
    payloads: list[dict],
    source_id: str,
) -> int:
    if not payloads:
        print(f"SKIP: {farm_name} — keine Einheiten für Park '{park_name}'")
        return 0

    models = load_farm_models(cur, farm_id)
    catalog = load_catalog(cur, source_id)

    inserted = insert_units(
        cur,
        farm_id=farm_id,
        payloads=payloads,
        source_id=source_id,
        catalog=catalog,
        models=models,
    )

    cur.execute(
        """
        UPDATE public.imc_wind_farms
        SET aliases = ARRAY(
              SELECT a FROM unnest(coalesce(aliases, ARRAY[]::text[])) AS a
              WHERE a NOT LIKE 'MaStR:%%'
            ),
            updated_at = now()
        WHERE farm_id = %s
        """,
        (farm_id,),
    )

    label = ext_id or "—"
    print(f"OK: {farm_name} ({label}) <- {inserted} units from '{park_name}'")
    return inserted


def main() -> int:
    parser = argparse.ArgumentParser(description="MaStR units → imc_turbines")
    parser.add_argument("--ext-windfarm-id", default=None)
    parser.add_argument(
        "--all-accepted",
        action="store_true",
        help="Alle accepted DE-Matches (nicht nur ein Park)",
    )
    parser.add_argument("--source-id", default=SOURCE_MASTR)
    args = parser.parse_args()

    if not args.all_accepted and not args.ext_windfarm_id:
        args.ext_windfarm_id = "DE01"

    with psycopg.connect(get_database_url()) as conn:
        with conn.cursor() as cur:
            targets = load_targets(
                cur,
                ext_id=args.ext_windfarm_id,
                all_accepted=args.all_accepted,
            )
            if not targets:
                print("Keine Ziele gefunden", file=sys.stderr)
                return 1

            units_cache: dict[str, dict[str, list[dict]]] = {}
            total_units = 0
            farms_ok = 0
            for farm_id, farm_name, ext_id, park_name, snapshot_id in targets:
                snap = str(snapshot_id)
                if snap not in units_cache:
                    units_cache[snap] = load_units_by_park_key(cur, snapshot_id)
                payloads = units_cache[snap].get(park_key_for(park_name), [])
                # Stable order for diffs / UI
                payloads = sorted(
                    payloads,
                    key=lambda p: (
                        str(p.get("NameStromerzeugungseinheit") or ""),
                        str(p.get("EinheitMastrNummer") or ""),
                    ),
                )
                n = transform_farm(
                    cur,
                    farm_id=farm_id,
                    farm_name=farm_name,
                    ext_id=ext_id,
                    park_name=park_name,
                    payloads=payloads,
                    source_id=args.source_id,
                )
                if n:
                    farms_ok += 1
                    total_units += n
        conn.commit()

    print(f"Fertig: {farms_ok}/{len(targets)} Parks, {total_units} Einheiten")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
