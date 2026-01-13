<!-- Reality Block
last_update: 2026-01-12
status: stable
scope:
  summary: "Configuration for vLLM (OpenAI-compatible server) on DGX Spark."
  in_scope:
    - serve parameters
    - ports
    - model settings
    - examples
  out_of_scope:
    - TensorRT engines
    - hardware optimizations
notes:
  - "vLLM used for large-context tasks and RAG pipelines."
-->

# vLLM Configuration (DGX Spark)

## Overview
vLLM provides an OpenAI‑compatible API with high throughput and large
context window support.  
It is ideal for:
- RAG Systems
- Backend pipelines
- API usage
- Batch inference
- Document processing

---

## Serve Script

`~/ai/scripts/serve/vllm.sh`

Command template:

```bash
docker run --rm --gpus all \
  -p 8000:8000 \
  -v /home/sparkuser/ai/models/<model>:/model \
  vllm/vllm-openai:latest \
  --model /model \
  --dtype auto \
  --tensor-parallel-size 1 \
  --max-model-len 2000000
```

### Modern (recommended)

```bash
#!/bin/bash
MODEL_PATH="$1"

docker run --rm --gpus all \
  -p 8000:8000 \
  -v $MODEL_PATH:/model \
  -v /home/sparkuser/ai/cache/vllm:/root/.cache \
  vllm/vllm-openai:latest \
    --model /model \
    --tensor-parallel-size 1 \
    --dtype auto \
    --max-model-len 2000000 \
    --gpu-memory-utilization 0.92 \
    --port 8000
```

---

## Recommended Model

`~/ai/models/llama4/llama4-scout-17b-nvfp4`

Optional:
- DeepSeek‑V3  
- Qwen3‑32B‑NVFP4  

---

## Port
- vLLM OpenAI API → **8000**

---

## Test

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"local","messages":[{"role":"user","content":"Hallo"}]}'
```

---

## Start via systemd

```bash
sudo systemctl start vllm
```

---

## Logs

```bash
docker logs $(docker ps -qf "ancestor=vllm/vllm-openai:latest")
```


