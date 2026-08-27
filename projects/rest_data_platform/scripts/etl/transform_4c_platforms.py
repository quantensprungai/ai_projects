#!/usr/bin/env python3
"""
Layer-2: 4C Platform Type → imc_offshore_platforms (light).

Voraussetzung: ingest_raw (windfarm, sheet Platform Type) + imc_wind_farms.

Farm-Link: WindfarmID, sonst Codes in ConnectingWindfarms wie \"Name (DE2X)\".
Shared platforms without resolvable farm are skipped (farm_id NOT NULL).

  python transform_4c_platforms.py --latest
"""

from __future__ import annotations

import argparse
import re

import psycopg
from dotenv import load_dotenv

from config import SOURCE_4C_WINDFARM, get_database_url
from transform_4c_events import load_farm_index

load_dotenv()

CONNECTING_CODE_RE = re.compile(r"\(([A-Za-z0-9]+)\)")


def blank_to_none(value):
    if isinstance(value, str) and not value.strip():
        return None
    return value


def resolve_farm_ids(
    payload: dict,
    by_ext: dict[str, str],
) -> list[str]:
    farm_ids: list[str] = []
    seen: set[str] = set()

    windfarm_id = blank_to_none(
        payload.get("WindfarmId") or payload.get("WindfarmID")
    )
    if windfarm_id is not None:
        farm_id = by_ext.get(str(windfarm_id).strip())
        if farm_id and farm_id not in seen:
            farm_ids.append(farm_id)
            seen.add(farm_id)

    connecting = blank_to_none(payload.get("ConnectingWindfarms"))
    if connecting:
        for code in CONNECTING_CODE_RE.findall(str(connecting)):
            farm_id = by_ext.get(code.strip())
            if farm_id and farm_id not in seen:
                farm_ids.append(farm_id)
                seen.add(farm_id)

    return farm_ids


def upsert_platform(
    cur: psycopg.Cursor,
    *,
    farm_id: str,
    source_id: str,
    payload: dict,
) -> bool:
    ext_platform_id = blank_to_none(payload.get("PlatformID"))
    if ext_platform_id is None:
        return False
    ext_platform_id = str(ext_platform_id).strip()
    if ext_platform_id.endswith(".0"):
        ext_platform_id = ext_platform_id[:-2]

    platform_name = blank_to_none(payload.get("PlatformName") or payload.get("NameConverter"))
    platform_group_type = blank_to_none(payload.get("PlatformGroupType"))
    platform_type = blank_to_none(payload.get("PlatformType"))
    platform_owner = blank_to_none(payload.get("PlatformOwner"))
    connecting_farms = blank_to_none(payload.get("ConnectingWindfarms"))

    cur.execute(
        """
        SELECT platform_id
        FROM public.imc_offshore_platforms
        WHERE farm_id = %s AND ext_platform_id = %s
        LIMIT 1
        """,
        (farm_id, ext_platform_id),
    )
    existing = cur.fetchone()
    if existing:
        cur.execute(
            """
            UPDATE public.imc_offshore_platforms SET
                platform_name = COALESCE(%s, platform_name),
                platform_group_type = COALESCE(%s, platform_group_type),
                platform_type = COALESCE(%s, platform_type),
                platform_owner = COALESCE(%s, platform_owner),
                connecting_farms = COALESCE(%s, connecting_farms),
                source_id = COALESCE(source_id, %s)
            WHERE platform_id = %s
            """,
            (
                platform_name,
                platform_group_type,
                platform_type,
                platform_owner,
                connecting_farms,
                source_id,
                existing[0],
            ),
        )
    else:
        cur.execute(
            """
            INSERT INTO public.imc_offshore_platforms (
                ext_platform_id,
                farm_id,
                platform_name,
                platform_group_type,
                platform_type,
                platform_owner,
                connecting_farms,
                source_id
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                ext_platform_id,
                farm_id,
                platform_name,
                platform_group_type,
                platform_type,
                platform_owner,
                connecting_farms,
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
            by_ext, _by_name = load_farm_index(cur)
            cur.execute(
                """
                SELECT payload FROM public.imc_source_raw_rows
                WHERE snapshot_id = %s AND sheet_name = 'Platform Type'
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
                farm_ids = resolve_farm_ids(payload, by_ext)
                if not farm_ids:
                    skipped += 1
                    continue
                for farm_id in farm_ids:
                    if upsert_platform(
                        cur,
                        farm_id=farm_id,
                        source_id=SOURCE_4C_WINDFARM,
                        payload=payload,
                    ):
                        upserted += 1
                    else:
                        skipped += 1

        conn.commit()
        print(f"imc_offshore_platforms upserted={upserted} skipped={skipped} snapshot={snapshot_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
