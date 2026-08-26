#!/usr/bin/env python3
"""
Layer-2: 4C VPI Vessel Contracts → imc_vessel_contracts (light subset).

Default: CountryName = Germany (not full ~17k). Keep curated pilot:* rows.

Voraussetzung: ingest_raw.py --profile vpi, transform_4c_vessels.py, imc_wind_farms.

  python transform_4c_vessel_contracts.py --latest --country Germany
  python transform_4c_vessel_contracts.py --latest --all
"""

from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation

import psycopg
from dotenv import load_dotenv

from config import SOURCE_4C_VPI, get_database_url
from transform_4c_events import blank_to_none, load_farm_index
from transform_4c_windfarm import parse_4c_date

load_dotenv()

SHEET = "Vessel Contracts"


def normalize_ext_id(value) -> str | None:
    value = blank_to_none(value)
    if value is None:
        return None
    text = str(value).strip()
    if text.endswith(".0"):
        try:
            text = str(int(Decimal(text)))
        except (InvalidOperation, ValueError):
            text = text[:-2]
    return text or None


def resolve_contract_farm(
    payload: dict,
    by_ext: dict[str, str],
    by_name_country: dict[tuple[str, str], str],
) -> str | None:
    for key in ("ProjectId", "WindfarmId"):
        ext = normalize_ext_id(payload.get(key))
        if ext and ext in by_ext:
            return by_ext[ext]

    name = blank_to_none(payload.get("ProjectName") or payload.get("Name"))
    country = blank_to_none(payload.get("CountryName") or payload.get("Country"))
    if name and country:
        return by_name_country.get(
            (str(name).strip().lower(), str(country).strip().lower())
        )
    return None


def load_vessel_index(cur: psycopg.Cursor) -> dict[str, str]:
    cur.execute(
        """
        SELECT vessel_id::text, ext_vessel_key
        FROM public.imc_vessels
        WHERE ext_vessel_key IS NOT NULL
          AND is_type_catalog = false
        """
    )
    out: dict[str, str] = {}
    for vessel_id, ext_key in cur.fetchall():
        if ext_key:
            out[str(ext_key).strip()] = vessel_id
    return out


def upsert_contract(
    cur: psycopg.Cursor,
    *,
    farm_id: str | None,
    vessel_id: str | None,
    source_id: str,
    payload: dict,
) -> bool:
    ext = normalize_ext_id(payload.get("WindfarmStakeholderId"))
    if not ext:
        return False
    ext_key = f"vpi:{ext}"

    period_start = parse_4c_date(payload.get("VesselStartDate"))
    period_end = parse_4c_date(payload.get("VesselEndDate"))

    stakeholder_type = blank_to_none(payload.get("StakeholderType"))
    stake_desc = blank_to_none(
        payload.get("StakeDescription") or payload.get("Stake")
    )
    note_parts = [p for p in (stakeholder_type, stake_desc) if p]
    scope_note = " — ".join(str(p) for p in note_parts)[:2000] if note_parts else None

    project_name = blank_to_none(payload.get("ProjectName"))
    client_name = blank_to_none(payload.get("Client") or payload.get("AnalysisAlias"))
    contract_type = blank_to_none(
        payload.get("TypeOfContract") or payload.get("StakeholderType")
    )
    market = blank_to_none(payload.get("Market"))
    country_name = blank_to_none(payload.get("CountryName"))

    cur.execute(
        """
        INSERT INTO public.imc_vessel_contracts (
          vessel_id,
          farm_id,
          project_name,
          client_name,
          contract_type,
          market,
          country_name,
          period_start,
          period_end,
          day_rate_eur,
          scope_note,
          ext_contract_key,
          source_id
        ) VALUES (
          %s::uuid, %s::uuid, %s, %s, %s, %s, %s, %s, %s, NULL, %s, %s, %s::uuid
        )
        ON CONFLICT (ext_contract_key) WHERE (ext_contract_key IS NOT NULL)
        DO UPDATE SET
          vessel_id = COALESCE(EXCLUDED.vessel_id, public.imc_vessel_contracts.vessel_id),
          farm_id = COALESCE(EXCLUDED.farm_id, public.imc_vessel_contracts.farm_id),
          project_name = EXCLUDED.project_name,
          client_name = EXCLUDED.client_name,
          contract_type = EXCLUDED.contract_type,
          market = EXCLUDED.market,
          country_name = EXCLUDED.country_name,
          period_start = EXCLUDED.period_start,
          period_end = EXCLUDED.period_end,
          scope_note = EXCLUDED.scope_note,
          source_id = EXCLUDED.source_id,
          updated_at = now()
        """,
        (
            vessel_id,
            farm_id,
            str(project_name)[:500] if project_name else None,
            str(client_name)[:500] if client_name else None,
            str(contract_type)[:200] if contract_type else None,
            str(market)[:200] if market else None,
            str(country_name)[:200] if country_name else None,
            period_start,
            period_end,
            scope_note,
            ext_key,
            source_id,
        ),
    )
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="VPI Vessel Contracts → imc_vessel_contracts (light)"
    )
    parser.add_argument("--snapshot-id")
    parser.add_argument("--latest", action="store_true")
    parser.add_argument(
        "--country",
        default="Germany",
        help="Filter CountryName (default Germany). Ignored with --all.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Import full Vessel Contracts sheet (not recommended yet).",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.latest and not args.snapshot_id:
        parser.error("--snapshot-id oder --latest erforderlich")

    country_filter = None if args.all else str(args.country).strip().lower()

    with psycopg.connect(get_database_url()) as conn:
        with conn.cursor() as cur:
            if args.latest:
                cur.execute(
                    """
                    SELECT snapshot_id FROM public.imc_source_snapshots
                    WHERE source_id = %s
                    ORDER BY ingested_at DESC
                    LIMIT 1
                    """,
                    (SOURCE_4C_VPI,),
                )
                row = cur.fetchone()
                if not row:
                    raise RuntimeError("Kein VPI-Snapshot — zuerst ingest_raw.py --profile vpi")
                snapshot_id = str(row[0])
            else:
                snapshot_id = str(args.snapshot_id)

            by_ext, by_name_country = load_farm_index(cur)
            vessels_by_ext = load_vessel_index(cur)
            if not by_ext and not by_name_country:
                raise RuntimeError("Keine Farmen — zuerst transform_4c_windfarm.py")

            scanned = ok = miss_farm = miss_key = skipped_country = 0
            cur.execute(
                """
                SELECT payload FROM public.imc_source_raw_rows
                WHERE snapshot_id = %s AND sheet_name = %s
                ORDER BY source_row_num
                """,
                (snapshot_id, SHEET),
            )
            for (payload,) in cur.fetchall():
                scanned += 1
                payload = {k: blank_to_none(v) for k, v in dict(payload).items()}

                country = blank_to_none(payload.get("CountryName") or payload.get("Country"))
                if country_filter and (
                    not country or str(country).strip().lower() != country_filter
                ):
                    skipped_country += 1
                    continue

                if not normalize_ext_id(payload.get("WindfarmStakeholderId")):
                    miss_key += 1
                    continue

                farm_id = resolve_contract_farm(payload, by_ext, by_name_country)
                if not farm_id:
                    miss_farm += 1
                    # Still import with farm_id null if vessel known? Prefer skip without farm for light.
                    continue

                vessel_ext = normalize_ext_id(payload.get("VesselId"))
                vessel_id = vessels_by_ext.get(vessel_ext) if vessel_ext else None

                if args.dry_run:
                    ok += 1
                    continue

                if upsert_contract(
                    cur,
                    farm_id=farm_id,
                    vessel_id=vessel_id,
                    source_id=SOURCE_4C_VPI,
                    payload=payload,
                ):
                    ok += 1

            cur.execute("SELECT count(*) FROM public.imc_vessel_contracts")
            total = cur.fetchone()[0]
            cur.execute(
                """
                SELECT count(*) FROM public.imc_vessel_contracts
                WHERE farm_id = 'b3920ba9-f33f-4d3e-94c8-d2bfc0d28634'::uuid
                """
            )
            alpha = cur.fetchone()[0]

        if not args.dry_run:
            conn.commit()

    print(
        f"Transform OK: scanned={scanned} upserted={ok} miss_farm={miss_farm} "
        f"miss_key={miss_key} skipped_country={skipped_country} "
        f"total_contracts={total} alpha_ventus={alpha} snapshot={snapshot_id}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
