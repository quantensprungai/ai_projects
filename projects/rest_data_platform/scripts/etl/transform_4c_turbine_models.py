#!/usr/bin/env python3
"""
Layer-2: 4C Turbine DB → imc_turbine_models + Farm-Design-Link.

- Upsert Specs (Offshore Wind Turbine Specs)
- Link primary model via Turbine on Windfarms → imc_farm_design.turbine_model_id
- Multi-model parks: aliases Turbine:<oem> · <model>

Ersetzt den DE01-only Pilot (transform_4c_turbine_alpha_ventus.py) für den Katalog.

  python transform_4c_turbine_models.py
  python transform_4c_turbine_models.py --windfarm-id DE01
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from decimal import Decimal, InvalidOperation

import psycopg
from dotenv import load_dotenv

from config import SOURCE_4C_TURBINE, get_database_url
from transform_4c_events import load_farm_index

load_dotenv()

SOURCE_ID = SOURCE_4C_TURBINE


def num(value, max_abs: str | None = None):
    if value is None or value == "":
        return None
    try:
        number = Decimal(str(value))
    except (InvalidOperation, ValueError):
        return None
    if max_abs is not None and abs(number) > Decimal(max_abs):
        return None
    return number


def blank(value) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def upsert_model(
    cur: psycopg.Cursor,
    *,
    tid: str,
    oem: str,
    model: str,
    rated,
    rotor,
    hub,
) -> str:
    cur.execute(
        """
        INSERT INTO public.imc_turbine_models (
          oem, model, rated_power_mw, rotor_diameter_m, hub_height_m,
          source_id, ext_turbine_model_key
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (oem, model) DO UPDATE SET
          rated_power_mw = COALESCE(EXCLUDED.rated_power_mw, imc_turbine_models.rated_power_mw),
          rotor_diameter_m = COALESCE(EXCLUDED.rotor_diameter_m, imc_turbine_models.rotor_diameter_m),
          hub_height_m = COALESCE(EXCLUDED.hub_height_m, imc_turbine_models.hub_height_m),
          source_id = COALESCE(imc_turbine_models.source_id, EXCLUDED.source_id),
          ext_turbine_model_key = COALESCE(
            imc_turbine_models.ext_turbine_model_key, EXCLUDED.ext_turbine_model_key
          )
        RETURNING turbine_model_id::text
        """,
        (oem, model, rated, rotor, hub, SOURCE_ID, tid),
    )
    return str(cur.fetchone()[0])


def load_specs(cur: psycopg.Cursor) -> dict[str, dict]:
    cur.execute(
        """
        SELECT payload
        FROM public.imc_source_raw_rows
        WHERE source_id = %s
          AND sheet_name = 'Offshore Wind Turbine Specs'
        """,
        (SOURCE_ID,),
    )
    out: dict[str, dict] = {}
    for (payload,) in cur.fetchall():
        if not isinstance(payload, dict):
            continue
        tid = blank(payload.get("TurbineId"))
        if tid:
            out[tid] = payload
    return out


def load_links(cur: psycopg.Cursor, windfarm_id: str | None) -> list[dict]:
    if windfarm_id:
        cur.execute(
            """
            SELECT payload
            FROM public.imc_source_raw_rows
            WHERE source_id = %s
              AND sheet_name = 'Turbine on Windfarms'
              AND payload->>'WindfarmId' = %s
            ORDER BY payload->>'WindfarmId', payload->>'TurbineId'
            """,
            (SOURCE_ID, windfarm_id),
        )
    else:
        cur.execute(
            """
            SELECT payload
            FROM public.imc_source_raw_rows
            WHERE source_id = %s
              AND sheet_name = 'Turbine on Windfarms'
            ORDER BY payload->>'WindfarmId', payload->>'TurbineId'
            """,
            (SOURCE_ID,),
        )
    return [p for (p,) in cur.fetchall() if isinstance(p, dict)]


def model_from_link_and_spec(link: dict, spec: dict | None) -> tuple[str, str, object, object, object, str]:
    tid = blank(link.get("TurbineId")) or "unknown"
    spec = spec or {}
    oem = blank(spec.get("Manufacturer")) or blank(link.get("TurbineManufacturer")) or "Unknown"
    model = blank(spec.get("TurbineName")) or blank(link.get("TurbineModel")) or f"tid-{tid}"
    rated = num(spec.get("RatedPowerMW") or link.get("TurbineMWMax") or link.get("TurbineMWMin"), "9999.99")
    rotor = num(spec.get("RotorDiameterm"), "9999.9")
    hub = num(spec.get("TowerHeightm"), "9999.9")
    return oem, model, rated, rotor, hub, tid


def pick_primary(entries: list[tuple[str, object]]) -> str:
    """entries: (model_id, rated_mw). Prefer highest rated, else first."""
    best_id = entries[0][0]
    best_mw = None
    for model_id, rated in entries:
        if rated is None:
            continue
        mw = float(rated)
        if best_mw is None or mw > best_mw:
            best_mw = mw
            best_id = model_id
    return best_id


def main() -> int:
    parser = argparse.ArgumentParser(description="4C turbine models → imc_turbine_models")
    parser.add_argument(
        "--windfarm-id",
        default=None,
        help="Nur ein Park (ext_windfarm_id); default = alle Links",
    )
    args = parser.parse_args()

    with psycopg.connect(get_database_url()) as conn:
        with conn.cursor() as cur:
            by_ext, _by_name = load_farm_index(cur)
            specs = load_specs(cur)
            links = load_links(cur, args.windfarm_id)
            if not links:
                print("Keine Turbine-on-Windfarms-Zeilen", file=sys.stderr)
                return 1

            # 1) Katalog: alle Specs + alle in Links referenzierten IDs
            tid_set = set(specs.keys())
            for link in links:
                tid = blank(link.get("TurbineId"))
                if tid:
                    tid_set.add(tid)

            models_upserted = 0
            tid_to_model: dict[str, str] = {}
            for tid in sorted(tid_set, key=lambda x: (len(x), x)):
                spec = specs.get(tid, {})
                # Synthetic link fields if only in specs
                link_stub = {
                    "TurbineId": tid,
                    "TurbineManufacturer": spec.get("Manufacturer"),
                    "TurbineModel": spec.get("TurbineName"),
                    "TurbineMWMax": spec.get("RatedPowerMW"),
                }
                oem, model, rated, rotor, hub, tid_n = model_from_link_and_spec(
                    link_stub, spec
                )
                if oem == "Unknown" and model.startswith("tid-") and not spec:
                    continue
                model_id = upsert_model(
                    cur,
                    tid=tid_n,
                    oem=oem,
                    model=model,
                    rated=rated,
                    rotor=rotor,
                    hub=hub,
                )
                tid_to_model[tid_n] = model_id
                models_upserted += 1

            # 2) Farm-Links
            by_farm_ext: dict[str, list[dict]] = defaultdict(list)
            for link in links:
                wid = blank(link.get("WindfarmId"))
                if wid:
                    by_farm_ext[wid].append(link)

            farms_linked = 0
            farms_skipped = 0
            for wid, farm_links in sorted(by_farm_ext.items()):
                farm_id = by_ext.get(wid)
                if not farm_id:
                    farms_skipped += 1
                    continue

                entries: list[tuple[str, object]] = []
                notes: list[str] = []
                seen_notes: set[str] = set()
                for link in farm_links:
                    tid = blank(link.get("TurbineId"))
                    if not tid:
                        continue
                    spec = specs.get(tid)
                    oem, model, rated, rotor, hub, tid_n = model_from_link_and_spec(
                        link, spec
                    )
                    model_id = tid_to_model.get(tid_n)
                    if not model_id:
                        model_id = upsert_model(
                            cur,
                            tid=tid_n,
                            oem=oem,
                            model=model,
                            rated=rated,
                            rotor=rotor,
                            hub=hub,
                        )
                        tid_to_model[tid_n] = model_id
                    entries.append((model_id, rated))
                    note = f"Turbine:{oem} · {model}"
                    if note not in seen_notes:
                        seen_notes.add(note)
                        notes.append(note)

                if not entries:
                    farms_skipped += 1
                    continue

                primary = pick_primary(entries)
                cur.execute(
                    """
                    UPDATE public.imc_farm_design
                    SET turbine_model_id = %s,
                        updated_at = now()
                    WHERE farm_id = %s
                    """,
                    (primary, farm_id),
                )
                if cur.rowcount == 0:
                    farms_skipped += 1
                    continue

                cur.execute(
                    "SELECT aliases FROM public.imc_wind_farms WHERE farm_id = %s",
                    (farm_id,),
                )
                row = cur.fetchone()
                aliases = [a for a in list(row[0] or []) if not str(a).startswith("Turbine:")]
                aliases.extend(notes)
                cur.execute(
                    """
                    UPDATE public.imc_wind_farms
                    SET aliases = %s, updated_at = now()
                    WHERE farm_id = %s
                    """,
                    (aliases, farm_id),
                )
                farms_linked += 1

        conn.commit()

    print(
        f"OK: models_upserted≈{models_upserted} farms_linked={farms_linked} "
        f"farms_unresolved_or_empty={farms_skipped}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
