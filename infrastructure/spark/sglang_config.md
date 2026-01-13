<!-- Reality Block
last_update: 2026-01-12
status: stable
scope:
  summary: "Configuration and serving details for SGLang on DGX Spark (GB10)."
  in_scope:
    - container config
    - ports
    - runtime settings
    - model paths
  out_of_scope:
    - TensorRT-LLM engines
    - hardware tuning
notes:
  - "Optimized for multimodal Llama-4-Scout-17B NVFP4."
-->

# SGLang Configuration (DGX Spark)

## Overview
SGLang is the high‑speed inference engine used for interactive chat,
agent systems, and multimodal (vision+text) processing.

It is the primary engine for:
- Llama‑4‑Scout‑17B‑NVFP4
- Phi‑4‑Reasoning (optional)
- Multimodal tasks
- Agent pipelines

---

## Serve Script Location

`~/ai/scripts/serve/sglang.sh`

Typical content:

```bash
docker run --rm --gpus all \
  -p 30000:30000 \
  -v /home/sparkuser/ai/models/<model>:/model \
  lmsysorg/sglang:spark \
  python3 -m sglang.launch_server \
    --model-path /model \
    --trust-remote-code \
    --host 0.0.0.0 \
    --port 30000
```

### Modern (recommended)

```bash
#!/bin/bash
MODEL_PATH="$1"

docker run --rm --gpus all \
  -p 30000:30000 \
  -v $MODEL_PATH:/model \
  -v /home/sparkuser/ai/cache/sglang:/root/.cache \
  lmsysorg/sglang:spark \
  python3 -m sglang.launch_server \
    --model-path /model \
    --host 0.0.0.0 \
    --port 30000 \
    --trust-remote-code \
    --tp 1 \
    --max-total-tokens 2000000
```

---

## Default Model (recommended)

`~/ai/models/llama4/llama4-scout-17b-nvfp4`

---

## Ports
- SGLang HTTP REST API → **30000**

Health Check:

```bash
curl http://localhost:30000/health
```

---

## Start via systemd

```bash
sudo systemctl start sglang
sudo systemctl stop sglang
sudo systemctl restart sglang
```

---

## Logs

```bash
docker logs $(docker ps -qf "ancestor=lmsysorg/sglang:spark")
```


