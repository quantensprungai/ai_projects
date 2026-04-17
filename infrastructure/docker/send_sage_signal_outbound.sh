#!/usr/bin/env bash
# Einmalig: Nachricht aus Datei als Bot an Flora (Signal) — Ziel = letzte E.164 flora/signal in clawdbot.json
set -eu
MSG_FILE="${1:-/tmp/sage_morning_trigger.txt}"
CFG="${CLAWDBOT_CONFIG:-/home/user/.clawdbot-personal/clawdbot.json}"
BOT="/home/user/.clawdbot/bin/clawdbot"
export CLAWDBOT_PROFILE="${CLAWDBOT_PROFILE:-personal}"

TARGET="$(python3 << 'PY'
import json
import sys
path = "/home/user/.clawdbot-personal/clawdbot.json"
with open(path) as f:
    c = json.load(f)
found = []
for b in c.get("bindings", []):
    if b.get("agentId") != "flora":
        continue
    if b.get("match", {}).get("channel") != "signal":
        continue
    pid = b.get("match", {}).get("peer", {}).get("id", "")
    if isinstance(pid, str) and pid.startswith("+") and pid[1:].isdigit():
        found.append(pid)
if not found:
    print("Keine Flora-Signal-E.164 in bindings.", file=sys.stderr)
    sys.exit(1)
# letzte Eintragung in der Liste = oft aktuellere Nummer
print(found[-1])
PY
)"

test -f "$MSG_FILE" || { echo "Fehlt: $MSG_FILE" >&2; exit 1; }
MSG="$(cat "$MSG_FILE")"
exec "$BOT" --profile "$CLAWDBOT_PROFILE" message send \
  --channel signal \
  --target "$TARGET" \
  --message "$MSG" \
  --json
