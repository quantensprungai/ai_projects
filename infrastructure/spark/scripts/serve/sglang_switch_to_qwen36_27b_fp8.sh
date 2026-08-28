#!/bin/bash
# Switch Primary Slot (30001) to Qwen3.6 27B FP8
# Deploy: scp ... sparkuser@<spark>:~/ai/scripts/serve/
#
# Qwen3.6 needs SGLang >= 0.5.10 and Transformers >= 5.3 (model_type qwen3_5).
# Default image for Qwen3.6 on DGX Spark:
#   scitrera/dgx-spark-sglang:0.5.12
#
# Short-term fallback (stock lmsysorg/sglang:spark):
#   bash /home/sparkuser/ai/scripts/serve/sglang_switch_to_qwen.sh

set -euo pipefail
SGLANG_IMAGE="${SGLANG_IMAGE:-scitrera/dgx-spark-sglang:0.5.12}"
MODEL_PATH="/home/sparkuser/ai/models/qwen36/qwen3.6-27b-fp8"
SERVED_NAME="qwen3.6-27b-fp8"
CONTAINER_NAME="sglang-qwen36-27b-fp8"
PORT=30001
LOG_DIR="/home/sparkuser/ai/logs/sglang"
mkdir -p "$LOG_DIR"

if [ ! -f "$MODEL_PATH/config.json" ]; then
  echo "ERROR: Model not found at $MODEL_PATH (missing config.json). Finish hf download first."
  exit 1
fi

# Stop current primary / all SGLang
if [ -x /home/sparkuser/ai/scripts/serve/sglang_stop_all.sh ]; then
  /home/sparkuser/ai/scripts/serve/sglang_stop_all.sh || true
else
  docker stop sglang-qwen-uncensored sglang-qwen36-27b-fp8 sglang-llama31-8b sglang-llama32-11b sglang-scout 2>/dev/null || true
fi

docker rm -f "$CONTAINER_NAME" 2>/dev/null || true

echo "Using SGLang image: $SGLANG_IMAGE"

# No --rm: if the server crashes, "docker logs sglang-qwen36-27b-fp8" still works.
docker run -d --gpus all --name "$CONTAINER_NAME" \
  --shm-size=32g \
  -p "${PORT}:${PORT}" \
  -v "$MODEL_PATH:/model" \
  -v /home/sparkuser/ai/cache/sglang:/root/.cache \
  "$SGLANG_IMAGE" \
  python3 -m sglang.launch_server \
    --model-path /model \
    --served-model-name "$SERVED_NAME" \
    --host 0.0.0.0 \
    --port "$PORT" \
    --trust-remote-code \
    --tp 1 \
    --mem-fraction-static 0.75 \
    --context-length 65536 \
    --reasoning-parser qwen3

sleep 5
if docker ps --format '{{.Names}}' | grep -qx "$CONTAINER_NAME"; then
  echo "Started $SERVED_NAME on port $PORT (container running; model may still be loading)."
  echo "Check: curl -s http://127.0.0.1:$PORT/v1/models"
  echo "Logs: docker logs -f $CONTAINER_NAME"
  exit 0
fi

echo "ERROR: Container exited during startup. Last log lines:"
docker logs "$CONTAINER_NAME" 2>&1 | tail -n 80 | tee "$LOG_DIR/qwen36-last-start.log"
echo "Full log saved to $LOG_DIR/qwen36-last-start.log"
echo "Fallback: bash /home/sparkuser/ai/scripts/serve/sglang_switch_to_qwen.sh"
exit 1
