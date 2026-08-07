#!/usr/bin/env python3
"""
Minimal Turbine transform for Alpha Ventus (4C Turbine DB → imc_turbine_models).

- Upsert Specs for TurbineIds linked on Windfarm DE01
- Link primary model on imc_farm_design
- Alias notes Turbine:<oem> <model> for mixed parks (detail UI)

Beispiel:
  python transform_4c_turbine_alpha_ventus.py
"""

from __future__ import annotations

import argparse
import sys
from decimal import Decimal, InvalidOperation

import psycopg
from dotenv import load_dotenv

from config import SOURCE_4C_TURBINE, get_database_url

load_dotenv()

WINDFARM_EXT_ID = "DE01"
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


def main() -> int:
    parser = argparse.ArgumentParser(description="Alpha Ventus turbine minimal transform")
    parser.add_argument("--windfarm-id", default=WINDFARM_EXT_ID)
    args = parser.parse_args()

    with psycopg.connect(get_database_url()) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT payload
                FROM public.imc_source_raw_rows
                WHERE source_id = %s
                  AND sheet_name = 'Turbine on Windfarms'
                  AND payload->>'WindfarmId' = %s
                ORDER BY payload->>'TurbineId'
                """,
                (SOURCE_ID, args.windfarm_id),
            )
            links = [row[0] for row in cur.fetchall()]
            if not links:
                print(f"Keine Turbine-on-Windfarms-Zeilen für {args.windfarm_id}", file=sys.stderr)
                return 1

            turbine_ids = []
            for payload in links:
                tid = payload.get("TurbineId")
                if tid is None:
                    continue
                turbine_ids.append(str(tid))

            # Specs
            cur.execute(
                """
                SELECT payload
                FROM public.imc_source_raw_rows
                WHERE source_id = %s
                  AND sheet_name = 'Offshore Wind Turbine Specs'
                  AND payload->>'TurbineId' = ANY(%s)
                """,
                (SOURCE_ID, turbine_ids),
            )
            specs = {str(p.get("TurbineId")): p for (p,) in cur.fetchall()}

            model_ids: list[str] = []
            link_notes: list[str] = []
            for tid in turbine_ids:
                spec = specs.get(tid, {})
                link = next(p for p in links if str(p.get("TurbineId")) == tid)
                oem = (spec.get("Manufacturer") or link.get("TurbineManufacturer") or "Unknown").strip()
                model = (spec.get("TurbineName") or link.get("TurbineModel") or f"tid-{tid}").strip()
                rated = num(spec.get("RatedPowerMW") or link.get("TurbineMWMax"), "9999.99")
                rotor = num(spec.get("RotorDiameterm"), "9999.9")
                hub = num(spec.get("TowerHeightm"), "9999.9")
                link_notes.append(f"Turbine:{oem} · {model}")

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
                      source_id = EXCLUDED.source_id,
                      ext_turbine_model_key = EXCLUDED.ext_turbine_model_key
                    RETURNING turbine_model_id
                    """,
                    (oem, model, rated, rotor, hub, SOURCE_ID, tid),
                )
                model_id = str(cur.fetchone()[0])
                model_ids.append(model_id)
                print(f"  model {oem} / {model} (tid={tid}) → {model_id}")

            cur.execute(
                """
                SELECT farm_id, aliases
                FROM public.imc_wind_farms
                WHERE ext_windfarm_id = %s
                LIMIT 1
                """,
                (args.windfarm_id,),
            )
            farm = cur.fetchone()
            if not farm:
                print(f"Farm {args.windfarm_id} nicht in imc_wind_farms", file=sys.stderr)
                return 1
            farm_id, aliases = farm
            # Drop old Turbine: notes then re-add
            aliases = [a for a in list(aliases or []) if not str(a).startswith("Turbine:")]
            for note in link_notes:
                aliases.append(note)

            primary_model_id = model_ids[0]
            cur.execute(
                """
                UPDATE public.imc_farm_design
                SET turbine_model_id = %s,
                    is_estimated_turbine = false,
                    source_id = COALESCE(source_id, %s),
                    updated_at = now()
                WHERE farm_id = %s
                """,
                (primary_model_id, SOURCE_ID, farm_id),
            )
            cur.execute(
                """
                UPDATE public.imc_wind_farms
                SET aliases = %s, updated_at = now()
                WHERE farm_id = %s
                """,
                (aliases, farm_id),
            )

        conn.commit()

    print(
        f"OK: {args.windfarm_id} → {len(model_ids)} turbine models, "
        f"primary={primary_model_id}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
