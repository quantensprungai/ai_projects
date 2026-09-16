#!/usr/bin/env python3
"""
Export PDF documents from a Telegram chat (e.g. Secret Library) using the same
Telethon session as telegram-mcp on VM102.

Run on docker-apps:
  /home/user/telegram-research/telegram-mcp/.venv/bin/python \
    telegram_pdf_export.py --query Prepping --limit 30

Optional push to bigdata (Calibre staging on pve):
  RSYNC_TARGET='root@192.168.0.50:/mnt/bigdata/archive/incoming/telegram-pdf/' \
    telegram_pdf_export.py --query BBK --push
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import DocumentAttributeFilename

DEFAULT_CHAT_ID = -1001344875575
DEFAULT_OUT = Path("/home/user/telegram-research/downloads/telegram-pdf")
DEFAULT_ENV = Path("/home/user/telegram-research/.env")
DEFAULT_MANIFEST = DEFAULT_OUT / "manifest.json"

INVALID_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')

# Thematic discovery (Secret Library and similar channels).
DISCOVER_TOPICS: dict[str, list[str]] = {
    "krise_notfall": [
        "Blackout",
        "Stromausfall",
        "EMP",
        "Krisenvorsorge",
        "Notfall",
        "BBK",
        "Bevölkerungsschutz",
        "Evakuierung",
        "Erste Hilfe",
        "Sanitäter",
    ],
    "prep_survival": [
        "Prepping",
        "Survival",
        "Bunker",
        "Selbstversorgung",
        "Vorrat",
        "Ham Radio",
        "CB-Funk",
    ],
    "prophezeiung_endzeit": [
        "Prophezeiung",
        "Apokalypse",
        "Endzeit",
        "Revelation",
        "Bibel",
    ],
    "essen_landwirtschaft": [
        "Meal Prep",
        "Ernährung",
        "Kochen",
        "Permakultur",
        "Garten",
        "Landwirtschaft",
        "Samentausch",
        "Ferment",
    ],
    "technik_energie": [
        "Solar",
        "Photovoltaik",
        "Elektronik",
        "Radio",
        "Handwerk",
        "Werkstatt",
        "Mechanik",
        "Ingenieur",
        "3D Druck",
    ],
    "wiederaufbau_resilienz": [
        "Wiederaufbau",
        "Resilienz",
        "Infrastruktur",
        "Community",
        "Kooperation",
        "Souveränität",
        "Autark",
        "Nachbarschaft",
        "Organisation",
    ],
    "sicherheit_recht": [
        "Waffe",
        "Schießen",
        "Sicherheit",
        "Verteidigung",
        "Recht",
        "Grundgesetz",
    ],
    "bildung_wissen": [
        "Handbuch",
        "Lehrbuch",
        "Skript",
        "Enzyklopädie",
        "Lexikon",
        "OER",
    ],
}


def _load_session_and_api(env_path: Path) -> tuple[str, int, str]:
    if not env_path.is_file():
        raise SystemExit(f"Missing env file: {env_path}")
    load_dotenv(env_path)
    api_id = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")
    session = os.getenv("TELEGRAM_SESSION_STRING")
    if not api_id or not api_hash or not session:
        raise SystemExit(
            "TELEGRAM_API_ID, TELEGRAM_API_HASH, and TELEGRAM_SESSION_STRING required in .env"
        )
    return session, int(api_id), api_hash


def _safe_name(raw: str, max_len: int = 180) -> str:
    cleaned = INVALID_CHARS.sub("_", raw.strip())
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" .")
    if not cleaned:
        cleaned = "document"
    if len(cleaned) > max_len:
        cleaned = cleaned[:max_len].rstrip(" .")
    return cleaned


def _pdf_title(msg) -> str | None:
    if not msg or not msg.media or not getattr(msg, "document", None):
        return None
    doc = msg.document
    mime = getattr(doc, "mime_type", "") or ""
    name = None
    for attr in doc.attributes or []:
        if isinstance(attr, DocumentAttributeFilename):
            name = attr.file_name
            break
    if name and not name.lower().endswith(".pdf"):
        if "pdf" not in mime.lower():
            return None
    elif "pdf" not in mime.lower():
        return None
    base = name or (msg.message or "").split("\n", 1)[0]
    return base.strip() or None


def _pdf_filename(msg) -> str | None:
    if not msg or not msg.media or not getattr(msg, "document", None):
        return None
    doc = msg.document
    mime = getattr(doc, "mime_type", "") or ""
    name = None
    for attr in doc.attributes or []:
        if isinstance(attr, DocumentAttributeFilename):
            name = attr.file_name
            break
    if name and not name.lower().endswith(".pdf"):
        if "pdf" not in mime.lower():
            return None
    elif "pdf" not in mime.lower():
        return None
    base = name or (msg.message or "").split("\n", 1)[0]
    base = _safe_name(base)
    if not base.lower().endswith(".pdf"):
        base = f"{base}.pdf"
    return f"{msg.id}_{base}"


def _load_manifest(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {"messages": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"messages": {}}
    if "messages" not in data:
        data["messages"] = {}
    return data


def _save_manifest(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(path)


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


async def _collect_message_ids(
    client: TelegramClient,
    chat_id: int,
    queries: Iterable[str],
    limit: int,
    scan_limit: int,
    message_ids: Iterable[int] | None = None,
) -> list[Any]:
    entity = await client.get_entity(chat_id)
    seen: set[int] = set()
    ordered: list[Any] = []

    ids = list(message_ids or [])
    if ids:
        fetched = await client.get_messages(entity, ids=ids)
        if not isinstance(fetched, list):
            fetched = [fetched]
        for msg in fetched:
            if msg and msg.id not in seen:
                seen.add(msg.id)
                ordered.append(msg)

    for q in queries:
        async for msg in client.iter_messages(entity, search=q, limit=limit):
            if msg.id in seen:
                continue
            seen.add(msg.id)
            ordered.append(msg)

    if scan_limit > 0:
        async for msg in client.iter_messages(entity, limit=scan_limit):
            if msg.id in seen:
                continue
            seen.add(msg.id)
            ordered.append(msg)

    return ordered


def _msg_record(msg, topics: list[str], matched_queries: list[str]) -> dict[str, Any]:
    doc = msg.document
    size = getattr(doc, "size", None)
    title = _pdf_title(msg) or f"msg-{msg.id}"
    caption = (msg.message or "").strip()
    if len(caption) > 240:
        caption = caption[:237] + "..."
    return {
        "id": msg.id,
        "date": msg.date.isoformat() if msg.date else None,
        "title": title,
        "size_bytes": size,
        "caption": caption,
        "topics": topics,
        "matched_queries": matched_queries,
    }


async def run_discover(args: argparse.Namespace) -> int:
    session, api_id, api_hash = _load_session_and_api(args.env)
    limit = args.limit
    topics_map = DISCOVER_TOPICS
    if args.query:
        topics_map = {"custom": args.query}

    # msg_id -> {record fields, topics set, queries set}
    index: dict[int, dict[str, Any]] = {}

    async with TelegramClient(StringSession(session), api_id, api_hash) as client:
        entity = await client.get_entity(args.chat_id)

        for topic_key, queries in topics_map.items():
            for q in queries:
                async for msg in client.iter_messages(entity, search=q, limit=limit):
                    if not _pdf_title(msg):
                        continue
                    mid = msg.id
                    if mid not in index:
                        index[mid] = {
                            "record": _msg_record(msg, [], []),
                            "topics": set(),
                            "queries": set(),
                        }
                    index[mid]["topics"].add(topic_key)
                    index[mid]["queries"].add(q)

        if args.scan_documents > 0:
            async for msg in client.iter_messages(entity, limit=args.scan_documents):
                if not _pdf_title(msg):
                    continue
                mid = msg.id
                if mid not in index:
                    index[mid] = {
                        "record": _msg_record(msg, [], []),
                        "topics": set(["recent_feed"]),
                        "queries": set(),
                    }

    rows: list[dict[str, Any]] = []
    for mid, entry in sorted(index.items(), key=lambda x: x[0], reverse=True):
        rec = entry["record"]
        rec["topics"] = sorted(entry["topics"])
        rec["matched_queries"] = sorted(entry["queries"])
        rows.append(rec)

    by_topic: dict[str, int] = {}
    for r in rows:
        for t in r["topics"]:
            by_topic[t] = by_topic.get(t, 0) + 1

    report = {
        "chat_id": args.chat_id,
        "generated": datetime.now(timezone.utc).isoformat(),
        "pdf_hits": len(rows),
        "by_topic": dict(sorted(by_topic.items(), key=lambda kv: (-kv[1], kv[0]))),
        "items": rows,
    }

    out_path = args.discover_out or (args.out / "discover_report.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"# Telegram PDF Discovery ({len(rows)} Treffer)")
    print(f"Report: {out_path}\n")
    print("## Treffer pro Themenblock")
    for topic, count in report["by_topic"].items():
        print(f"- {topic}: {count}")
    print("\n## Highlights (neueste zuerst, max 40)")
    for r in rows[:40]:
        size_mb = (r["size_bytes"] or 0) / (1024 * 1024)
        tags = ",".join(r["topics"])
        print(f"- [{r['id']}] ({size_mb:.1f} MB) [{tags}] {r['title'][:120]}")
    return 0


async def run(args: argparse.Namespace) -> int:
    session, api_id, api_hash = _load_session_and_api(args.env)
    out_dir: Path = args.out
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = args.manifest or (out_dir / "manifest.json")
    manifest = _load_manifest(manifest_path)

    queries = args.query or []
    async with TelegramClient(StringSession(session), api_id, api_hash) as client:
        messages = await _collect_message_ids(
            client,
            args.chat_id,
            queries,
            args.limit,
            args.scan_documents,
            message_ids=args.message_id,
        )

        downloaded = 0
        skipped = 0
        for msg in messages:
            fname = _pdf_filename(msg)
            if not fname:
                continue
            key = str(msg.id)
            if key in manifest["messages"] and not args.force:
                skipped += 1
                continue
            dest = out_dir / fname
            if dest.is_file() and not args.force:
                manifest["messages"][key] = {
                    "path": str(dest),
                    "sha256": _sha256(dest),
                    "date": msg.date.isoformat() if msg.date else None,
                    "query_note": "already_on_disk",
                }
                skipped += 1
                continue
            if args.dry_run:
                print(f"DRY-RUN would download msg {msg.id} -> {dest.name}")
                continue
            path = await client.download_media(msg, file=str(dest.with_suffix("")))
            if not path:
                print(f"FAIL msg {msg.id}", file=sys.stderr)
                continue
            final = Path(path).resolve()
            manifest["messages"][key] = {
                "path": str(final),
                "sha256": _sha256(final),
                "date": msg.date.isoformat() if msg.date else None,
            }
            downloaded += 1
            print(f"OK {msg.id} -> {final.name}")

    if not args.dry_run:
        manifest["updated"] = datetime.now(timezone.utc).isoformat()
        _save_manifest(manifest_path, manifest)

    if args.push and not args.dry_run:
        target = os.getenv("RSYNC_TARGET", "").strip()
        if not target:
            print("RSYNC_TARGET not set; skip push", file=sys.stderr)
        else:
            import shutil
            import subprocess

            if shutil.which("rsync"):
                cmd = ["rsync", "-av", f"{out_dir}/", target]
                print("PUSH:", " ".join(cmd))
                subprocess.check_call(cmd)
            else:
                host_part, _, remote_path = target.partition(":")
                if not remote_path:
                    raise SystemExit(f"Invalid RSYNC_TARGET: {target}")
                remote_path = remote_path.rstrip("/")
                pdfs = sorted(out_dir.glob("*.pdf"))
                if not pdfs:
                    print("PUSH: no PDFs to upload", file=sys.stderr)
                else:
                    cmd = [
                        "scp",
                        "-o",
                        "BatchMode=yes",
                        *[str(p) for p in pdfs],
                        f"{host_part}:{remote_path}/",
                    ]
                    print("PUSH:", " ".join(cmd))
                    subprocess.check_call(cmd)

    print(
        f"Done: downloaded={downloaded} skipped={skipped} "
        f"manifest={manifest_path}"
    )
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Export PDFs from a Telegram chat.")
    parser.add_argument(
        "--chat-id",
        type=int,
        default=int(os.getenv("TELEGRAM_PDF_CHAT_ID", DEFAULT_CHAT_ID)),
    )
    parser.add_argument(
        "--query",
        action="append",
        help="Search term (repeatable). Default queries if none given.",
    )
    parser.add_argument("--limit", type=int, default=40, help="Per-query message limit.")
    parser.add_argument(
        "--scan-documents",
        type=int,
        default=0,
        help="Additionally scan the last N channel messages for PDFs.",
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--env", type=Path, default=DEFAULT_ENV)
    parser.add_argument("--manifest", type=Path, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true", help="Re-download even if in manifest.")
    parser.add_argument(
        "--push",
        action="store_true",
        help="rsync out/ to RSYNC_TARGET after download.",
    )
    parser.add_argument(
        "--discover",
        action="store_true",
        help="Thematic PDF scan only (no download); writes discover_report.json.",
    )
    parser.add_argument(
        "--discover-out",
        type=Path,
        default=None,
        help="JSON path for --discover (default: <out>/discover_report.json).",
    )
    parser.add_argument(
        "--message-id",
        type=int,
        action="append",
        dest="message_id",
        help="Download specific message ID (repeatable).",
    )
    args = parser.parse_args()
    if args.discover:
        raise SystemExit(asyncio.run(run_discover(args)))
    if not args.query and not args.message_id:
        args.query = [
            "Prepping",
            "BBK",
            "Krisenvorsorge",
            "Survival",
            "Notfall",
            "Bevölkerungsschutz",
        ]
    elif not args.query:
        args.query = []
    raise SystemExit(asyncio.run(run(args)))


if __name__ == "__main__":
    main()
