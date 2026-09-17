#!/bin/bash
# Start ComfyUI on :8188 (all interfaces). Stops a previous instance first.
set -euo pipefail

ROOT="${HOME}/ai/comfyui"
LOG_DIR="${HOME}/ai/logs/comfyui"
PID_FILE="${LOG_DIR}/comfyui.pid"
mkdir -p "$LOG_DIR"

if [ -f "$PID_FILE" ] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
  echo "Already running PID $(cat "$PID_FILE")"
  exit 0
fi

# shellcheck disable=SC1091
source "${ROOT}/comfyui-env/bin/activate"
cd "${ROOT}/ComfyUI"

nohup python main.py --listen 0.0.0.0 --port 8188 \
  >> "${LOG_DIR}/comfyui.log" 2>&1 &
echo $! > "$PID_FILE"
echo "ComfyUI PID $(cat "$PID_FILE")  http://spark-56d0:8188  log: ${LOG_DIR}/comfyui.log"
