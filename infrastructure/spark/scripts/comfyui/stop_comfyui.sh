#!/bin/bash
set -euo pipefail
PID_FILE="${HOME}/ai/logs/comfyui/comfyui.pid"
if [ -f "$PID_FILE" ]; then
  pid="$(cat "$PID_FILE")"
  if kill -0 "$pid" 2>/dev/null; then
    kill "$pid"
    echo "Stopped ComfyUI PID $pid"
  else
    echo "Stale PID file ($pid)"
  fi
  rm -f "$PID_FILE"
else
  pkill -f "ComfyUI/main.py" && echo "Stopped via pkill" || echo "ComfyUI not running"
fi
