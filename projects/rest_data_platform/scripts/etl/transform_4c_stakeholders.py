#!/usr/bin/env python3
"""
Layer-2: 4C Windfarm Supply Chain → imc_orgs + imc_farm_stakeholders.

Voraussetzung: ingest_raw.py --profile windfarm, imc_wind_farms befüllt.

  python transform_4c_stakeholders.py --latest --country Germany
  python transform_4c_stakeholders.py --latest --all
"""

from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation

import psycopg
from dotenv import load_dotenv

from config import SOURCE_4C_WINDFARM, get_database_url
from transform_4c_events import blank_to_none, load_farm_index, resolve_farm

load_dotenv()

SHEET = "Windfarm Supply Chain"


def parse_decimal(value) -> Decimal | None:
    if value in (None, ""):
        return None
    try:
        return Decimal(str(value).replace(",", "").strip())
    except (InvalidOperation, ValueError):
        return None


def parse_bool(value) -> bool | None:
    if value in (None, ""):
        return None
    text = str(value).strip().lower()
    if text in ("1", "true", "yes", "y", "t"):
        return True
    if text in ("0", "false", "no", "n", "f"):
        return False
    return None


def upsert_org(
    cur: psycopg.Cursor,
    *,
    org_name: str,
    country: str | None,
    website: str | None,
    source_id: str,
) -> str:
    cur.execute(
        """
        INSERT INTO public.imc_orgs (org_name, country, website, source_id)
        VALUES (%s, %s, %s, %s::uuid)
        ON CONFLICT (org_name, country) DO UPDATE SET
          website = COALESCE(EXCLUDED.website, public.imc_orgs.website),
          source_id = COALESCE(EXCLUDED.source_id, public.imc_orgs.source_id)
        RETURNING org_id::text
        """,
        (org_name, country, website, source_id),
    )
    row = cur.fetchone()
    if row:
        return str(row[0])

    # ON CONFLICT with NULL country does not match in Postgres — fall back.
    cur.execute(
        """
        SELECT org_id::text FROM public.imc_orgs
        WHERE org_name = %s AND country IS NOT DISTINCT FROM %s
        LIMIT 1
        """,
        (org_name, country),
    )
    existing = cur.fetchone()
    if existing:
        return str(existing[0])
    raise RuntimeError(f"org upsert failed for {org_name!r} / {country!r}")


def upsert_stakeholder(
    cur: psycopg.Cursor,
    *,
    farm_id: str,
    org_id: str | None,
    source_id: str,
    payload: dict,
) -> bool:
    ext_id = payload.get("WindfarmStakeholderId")
    if ext_id in (None, ""):
        return False
    ext_key = str(ext_id).strip()
    if ext_key.endswith(".0"):
        try:
            ext_key = str(int(Decimal(ext_key)))
        except (InvalidOperation, ValueError):
            pass

    stake_type = payload.get("StakeholderType") or "Unknown"
    cur.execute(
        """
        INSERT INTO public.imc_farm_stakeholders (
          ext_id, farm_id, org_id, stakeholder_type, sub_type_category, sub_type,
          client, stake_description, stake_value, stake_currency, cost_description,
          is_expired, source_id
        )
        VALUES (
          %s, %s::uuid, %s::uuid, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s::uuid
        )
        ON CONFLICT (ext_id) WHERE ext_id IS NOT NULL DO UPDATE SET
          farm_id = EXCLUDED.farm_id,
          org_id = COALESCE(EXCLUDED.org_id, public.imc_farm_stakeholders.org_id),
          stakeholder_type = EXCLUDED.stakeholder_type,
          sub_type_category = EXCLUDED.sub_type_category,
          sub_type = EXCLUDED.sub_type,
          client = EXCLUDED.client,
          stake_description = EXCLUDED.stake_description,
          stake_value = EXCLUDED.stake_value,
          stake_currency = EXCLUDED.stake_currency,
          cost_description = EXCLUDED.cost_description,
          is_expired = COALESCE(EXCLUDED.is_expired, public.imc_farm_stakeholders.is_expired),
          source_id = COALESCE(EXCLUDED.source_id, public.imc_farm_stakeholders.source_id)
        """,
        (
            ext_key,
            farm_id,
            org_id,
            str(stake_type).strip(),
            payload.get("StakeholderSubTypeCategory"),
            payload.get("StakeholderSubType"),
            payload.get("Client") or payload.get("AnalysisName"),
            payload.get("StakeDescription"),
            parse_decimal(payload.get("ValueOfStake") or payload.get("Stake")),
            payload.get("CurrencyOfStake"),
            payload.get("CostDescription"),
            parse_bool(payload.get("IsExpired")) or False,
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
        raise RuntimeError("Kein Windfarm-Snapshot — zuerst ingest_raw.py --profile windfarm")
    return str(row[0])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot-id")
    parser.add_argument("--latest", action="store_true")
    parser.add_argument(
        "--country",
        default="Germany",
        help="Nur Zeilen mit diesem Country-Feld (Default: Germany). Ignoriert mit --all.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Alle Supply-Chain-Zeilen (kein Country-Filter)",
    )
    args = parser.parse_args()
    if not args.latest and not args.snapshot_id:
        parser.error("--snapshot-id oder --latest erforderlich")

    country_filter = None if args.all else (args.country or "").strip()

    with psycopg.connect(get_database_url()) as conn:
        snapshot_id = resolve_snapshot_id(conn, args.snapshot_id, args.latest)
        with conn.cursor() as cur:
            by_ext, by_name_country = load_farm_index(cur)
            if not by_ext and not by_name_country:
                raise RuntimeError("Keine Farmen — zuerst transform_4c_windfarm.py")

            scanned = ok = miss_farm = miss_org = 0
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
                payload = {k: blank_to_none(v) for k, v in payload.items()}
                if country_filter:
                    row_country = str(
                        payload.get("Country") or payload.get("OrganisationCountry") or ""
                    ).strip()
                    if row_country.lower() != country_filter.lower():
                        continue

                farm_id = resolve_farm(payload, by_ext, by_name_country)
                if not farm_id:
                    miss_farm += 1
                    continue

                org_name = payload.get("OrganisationName")
                org_id = None
                if org_name:
                    org_country = payload.get("OrganisationCountry") or payload.get("Country")
                    if isinstance(org_country, str):
                        org_country = org_country.strip() or None
                    website = payload.get("Website")
                    if isinstance(website, str):
                        website = website.strip() or None
                    try:
                        org_id = upsert_org(
                            cur,
                            org_name=str(org_name).strip(),
                            country=org_country,
                            website=website,
                            source_id=SOURCE_4C_WINDFARM,
                        )
                    except Exception:  # noqa: BLE001
                        miss_org += 1
                        org_id = None

                if upsert_stakeholder(
                    cur,
                    farm_id=farm_id,
                    org_id=org_id,
                    source_id=SOURCE_4C_WINDFARM,
                    payload=payload,
                ):
                    ok += 1

            cur.execute("SELECT count(*) FROM public.imc_farm_stakeholders")
            total_sh = cur.fetchone()[0]
            cur.execute("SELECT count(*) FROM public.imc_orgs")
            total_org = cur.fetchone()[0]
            cur.execute(
                """
                SELECT count(*) FROM public.imc_farm_stakeholders sh
                JOIN public.imc_wind_farms f ON f.farm_id = sh.farm_id
                WHERE f.name ILIKE 'Alpha Ventus'
                """
            )
            av = cur.fetchone()[0]

        conn.commit()
        scope = "all countries" if args.all else f"country={country_filter}"
        print(
            f"OK stakeholders snapshot={snapshot_id} scope={scope} "
            f"scanned={scanned} upserted={ok} miss_farm={miss_farm} miss_org={miss_org} "
            f"total_stakeholders={total_sh} total_orgs={total_org} alpha_ventus={av}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
