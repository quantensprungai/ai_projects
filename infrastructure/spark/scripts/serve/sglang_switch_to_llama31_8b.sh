#!/bin/bash
# Switch Primary Slot (30001) to Llama 3.1 8B Instruct
# Deploy: scp ... sparkuser@<spark>:~/ai/scripts/serve/

set -e
MODEL_PATH="/home/sparkuser/ai/models/llama/llama-3.1-8b-instruct"
SERVED_NAME="llama-3.1-8b-instruct"
CONTAINER_NAME="sglang-llama31-8b"
PORT=30001

# Stop current primary / all SGLang
if [ -x /home/sparkuser/ai/scripts/serve/sglang_stop_all.sh ]; then
  /home/sparkuser/ai/scripts/serve/sglang_stop_all.sh || true
else
  docker stop sglang-qwen-uncensored sglang-llama31-8b sglang-llama32-11b sglang-scout 2>/dev/null || true
fi

# Start Llama 3.1 8B on Primary
docker run -d --rm --gpus all --name "$CONTAINER_NAME" \
  -p ${PORT}:${PORT} \
  -v "$MODEL_PATH:/model" \
  -v /home/sparkuser/ai/cache/sglang:/root/.cache \
  lmsysorg/sglang:spark \
  python3 -m sglang.launch_server \
    --model-path /model \
    --served-model-name "$SERVED_NAME" \
    --host 0.0.0.0 \
    --port $PORT \
    --trust-remote-code \
    --tp 1

echo "Started $SERVED_NAME on port $PORT. Check: curl -s http://127.0.0.1:$PORT/v1/models"
