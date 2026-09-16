#!/usr/bin/env bash
# VM102 (docker-apps): PDF-Export aus Telegram → Calibre-Staging auf pve.
set -euo pipefail

ROOT="${TELEGRAM_RESEARCH_ROOT:-/home/user/telegram-research}"
PY="${ROOT}/telegram-mcp/.venv/bin/python"
SCRIPT="${ROOT}/scripts/telegram_pdf_export.py"

if [[ ! -x "$PY" ]]; then
  echo "Missing venv python: $PY" >&2
  exit 1
fi
if [[ ! -f "$SCRIPT" ]]; then
  echo "Missing script: $SCRIPT (copy from ai_projects infrastructure/docker/scripts/)" >&2
  exit 1
fi

export RSYNC_TARGET="${RSYNC_TARGET:-root@192.168.0.50:/mnt/bigdata/archive/incoming/telegram-pdf/}"

exec "$PY" "$SCRIPT" "$@"
