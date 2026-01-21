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
- Qwen3‑32B NVFP4 (current default, stable)
- Llama‑4‑Scout‑17B‑NVFP4 (target; needs correct flags/config)
- Phi‑4‑Reasoning (optional; only when memory allows)
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

## Default Model (recommended, current reality)

`~/ai/models/qwen3/qwen3-32b-nvfp4`

Reality Check:
- Auf Spark/GB10 läuft aktuell stabil ein SGLang Server für Qwen auf Port `30001`.
- Llama4‑Scout‑17B NVFP4 ist installiert, benötigt aber **korrekte Quant/Attention Flags**; sonst crasht der Start.

---

## Ports
- SGLang HTTP REST API → **30000**

Health Check:

```bash
curl http://localhost:30000/health
```

---

## Llama4‑Scout‑17B NVFP4 (Kontext & Flags)

### Kontextfenster (aus `config.json`)

Llama4‑Scout‑17B hat in der Model‑Config ein extrem großes `max_position_embeddings`:
- `max_position_embeddings = 10485760` (≈ 10.5M Tokens, theoretisch)

Reality Check:
- Das ist ein **theoretisches** Limit aus der Config. Praktisch limitieren RAM/VRAM/UMA, KV‑Cache, und die Server‑Flags.
- Trotzdem: es ist **sehr wahrscheinlich größer** als typische Cloud‑Modelleinstellungen (und für “Doku komplett einlesen” interessant).

### Benötigte Flags (GB10, SGLang)

Wir haben gesehen, dass Llama4 Start ohne spezifische Settings scheitern kann, z. B.:
- `AssertionError: ... attention_backend ... required for Llama4`
- ModelOpt Quant Config Mismatch (FP8/FP4)

Deshalb als Startpunkt:

```bash
python3 -m sglang.launch_server \
  --model-path /model \
  --trust-remote-code \
  --host 0.0.0.0 \
  --port 30000 \
  --tp 1 \
  --attention-backend triton \
  --quantization modelopt_fp4 \
  --modelopt-quant nvfp4
```

> Hinweis: falls das Modell bereits quantized ist, kann `--quantization ...` trotzdem nötig sein, damit SGLang die richtige Quant‑Config interpretiert.

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


