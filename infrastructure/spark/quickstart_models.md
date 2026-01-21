<!-- Reality Block
last_update: 2026-01-20
status: draft
scope:
  summary: "Kurz-Anleitung: welches Modell wofür + on-demand Start/Stop auf Spark."
  in_scope:
    - model/engine selection
    - on-demand workflow
    - minimal monitoring
  out_of_scope:
    - deep tuning
    - secrets
notes: []
-->

# Spark Quickstart – Modelle & Engines (kurz)

## Mental Model (1 Satz)

**Modelle “sind da” auf Disk, aber sie “blockieren Ressourcen” erst, wenn ein Server (SGLang/vLLM/Ollama) sie lädt.**

## Welche Engine wann?

- **SGLang** (Port `30000`): Primary für Spark/GB10, Chat/Agents, auch große Contexts (z. B. Scout‑10m).
- **vLLM** (Port `8000`): OpenAI‑kompatibel/Throughput – auf GB10 nur verwenden, wenn das Image/Toolchain bestätigt funktioniert.
- **Ollama** (Port `11434`): Fallback, wenn du Open WebUI schnell wieder nutzbar machen willst.

## Welche Modelle wofür? (Default Empfehlung)

- **Repo-/Doku‑Synthese, “alles einlesen”**: `llama4-scout-10m` (on‑demand)
- **Allround + Multilingual**: `qwen3-32b-nvfp4`
- **Reasoning**: `phi4-reasoning`
- **Embeddings/RAG**: `bge-m3`

## On-demand Workflow (Start → Nutzen → Stop)

### SGLang starten (Beispiel)

```bash
docker rm -f sglang >/dev/null 2>&1 || true
docker run --rm --name sglang --gpus all \
  -p 30000:30000 \
  -v /home/sparkuser/ai/models/llama4/llama4-scout-10m:/model \
  -v /home/sparkuser/ai/cache/sglang:/root/.cache \
  lmsysorg/sglang:spark \
  python3 -m sglang.launch_server \
    --model-path /model \
    --host 0.0.0.0 \
    --port 30000 \
    --trust-remote-code \
    --tp 1
```

Health:

```bash
curl -sf http://localhost:30000/health
```

Stop:

```bash
docker rm -f sglang
```

### Open WebUI: Chats löschen

```bash
docker rm -f open-webui
docker volume rm open-webui
```

## Monitoring (minimal)

```bash
docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
nvidia-smi
```

## Open WebUI ↔ Spark verbinden (kurz)

Open WebUI ist nur ein Frontend – du musst ein Backend eintragen.

- **SGLang (empfohlen auf GB10)**:
  - **Default (Qwen)**: `http://<spark-host>:30001`
  - **Optional (zweites Modell, z. B. Scout on-demand)**: `http://<spark-host>:30000`
  - Health: `GET /health`
  - OpenAI‑API: `POST /v1/chat/completions`

- **Ollama (Fallback)**:
  - URL: `http://<spark-host>:11434`

Reality Check:
- vLLM kann auf GB10 je nach Image/Toolchain scheitern (`ptxas ... sm_121a`) → dann ist SGLang der Standardweg.
