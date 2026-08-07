#!/usr/bin/env python3
"""
Layer-2b: Übernimmt *accepted* MaStR-Matches als Anreicherung.

Schreibt nur:
  - aliases: MaStRPark:<Name> (+ optional 1× MaStR:<SEE…>)
  - milestones.full_commissioning, falls noch leer

Nicht: 4C-Kapazität/Foundation überschreiben.
"""

from __future__ import annotations

import argparse
import sys

import psycopg
from dotenv import load_dotenv

from config import SOURCE_MASTR, get_database_url

load_dotenv()


def clean_aliases(aliases: list[str] | None, park_name: str, sample_ids: list[str] | None) -> list[str]:
    """Keep non-MaStR aliases; replace MaStR* clutter with park + one unit id."""
    kept: list[str] = []
    for alias in aliases or []:
        text = str(alias)
        if text.startswith("MaStRPark:") or text.startswith("MaStR:"):
            continue
        if text not in kept:
            kept.append(text)
    kept.append(f"MaStRPark:{park_name}")
    if sample_ids:
        unit_tag = f"MaStR:{sample_ids[0]}"
        if unit_tag not in kept:
            kept.append(unit_tag)
    return kept


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply accepted MaStR matches")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--source-id", default=SOURCE_MASTR)
    parser.add_argument(
        "--reapply-aliases",
        action="store_true",
        help="MaStR-Aliases auch bei bereits angereicherten Farms neu setzen (aufräumen)",
    )
    args = parser.parse_args()

    with psycopg.connect(get_database_url()) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT
                  m.match_id,
                  m.farm_id,
                  wf.name,
                  wf.aliases,
                  p.name_windpark,
                  p.sample_mastr_unit_ids,
                  p.commissioning_max,
                  ms.full_commissioning
                FROM public.imc_mastr_farm_matches m
                JOIN public.imc_mastr_park_agg p ON p.park_key = m.park_key
                JOIN public.imc_wind_farms wf ON wf.farm_id = m.farm_id
                LEFT JOIN public.imc_farm_milestones ms ON ms.farm_id = m.farm_id
                WHERE m.status = 'accepted'
                ORDER BY wf.name
                """
            )
            rows = cur.fetchall()
            if not rows:
                print("Keine accepted Matches — nichts anzuwenden.")
                return 0

            applied = 0
            for (
                match_id,
                farm_id,
                name,
                aliases,
                park_name,
                sample_ids,
                commissioning_max,
                full_commissioning,
            ) in rows:
                new_aliases = clean_aliases(aliases, park_name, sample_ids)
                alias_changed = list(aliases or []) != new_aliases
                will_set_commissioning = bool(commissioning_max and not full_commissioning)

                if not alias_changed and not will_set_commissioning and not args.reapply_aliases:
                    print(f"{name}: bereits aktuell")
                    continue

                print(
                    f"{'[dry-run] ' if args.dry_run else ''}"
                    f"{name}: aliases={len(new_aliases)}"
                    f"{', commissioning=' + str(commissioning_max) if will_set_commissioning else ''}"
                )

                if args.dry_run:
                    continue

                if alias_changed or args.reapply_aliases:
                    cur.execute(
                        """
                        UPDATE public.imc_wind_farms
                        SET aliases = %s, updated_at = now()
                        WHERE farm_id = %s
                        """,
                        (new_aliases, farm_id),
                    )

                if will_set_commissioning:
                    cur.execute(
                        """
                        INSERT INTO public.imc_farm_milestones (farm_id, full_commissioning, source_id)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (farm_id) DO UPDATE SET
                          full_commissioning = COALESCE(
                            imc_farm_milestones.full_commissioning,
                            EXCLUDED.full_commissioning
                          ),
                          source_id = COALESCE(
                            imc_farm_milestones.source_id,
                            EXCLUDED.source_id
                          ),
                          updated_at = now()
                        """,
                        (farm_id, commissioning_max, args.source_id),
                    )

                cur.execute(
                    """
                    UPDATE public.imc_mastr_farm_matches
                    SET evidence = evidence || jsonb_build_object('applied_at', now()::text),
                        updated_at = now()
                    WHERE match_id = %s
                    """,
                    (match_id,),
                )
                applied += 1

        if not args.dry_run:
            conn.commit()

    print(f"Apply OK: {0 if args.dry_run else applied} farms updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
