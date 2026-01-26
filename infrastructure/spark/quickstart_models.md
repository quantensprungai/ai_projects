<!-- Reality Block
last_update: 2026-01-26
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

- **SGLang** (Port `30000`): Primary für Spark/GB10, Chat/Agents, auch große Contexts (z. B. Llama4‑Scout‑17B).
- **vLLM** (Port `8000`): OpenAI‑kompatibel/Throughput – auf GB10 nur verwenden, wenn das Image/Toolchain bestätigt funktioniert.
- **Ollama** (Port `11434`): Fallback, wenn du Open WebUI schnell wieder nutzbar machen willst.

## Welche Modelle wofür? (Default Empfehlung)

- **Repo-/Doku‑Synthese, “alles einlesen”**: `llama4-scout-17b-nvfp4` (on‑demand; großes Kontextfenster, aber Memory/KV‑Cache beachten)
- **Allround + Multilingual**: `qwen3-32b-nvfp4`
- **Coding (schnell, aber nicht “uncensored” per se)**: `qwen3-coder-30b-nvfp4`
- **Reasoning**: `phi4-reasoning`
- **Embeddings/RAG**: `bge-m3`

## On-demand Workflow (Start → Nutzen → Stop)

### SGLang starten (Beispiel)

```bash
docker rm -f sglang >/dev/null 2>&1 || true
docker run --rm --name sglang --gpus all \
  -p 30000:30000 \
  -v /home/sparkuser/ai/models/llama4/llama4-scout-17b-nvfp4:/model \
  -v /home/sparkuser/ai/cache/sglang:/root/.cache \
  lmsysorg/sglang:spark \
  python3 -m sglang.launch_server \
    --model-path /model \
    --served-model-name llama4-scout-17b-nvfp4 \
    --host 0.0.0.0 \
    --port 30000 \
    --trust-remote-code \
    --tp 1
```

Health:

```bash
curl -sf http://localhost:30000/health
```

Model-ID Check (wichtig für Cursor/OpenWebUI):

```bash
curl -sf http://localhost:30000/v1/models
```

> Reality Check: Der `id` Wert aus `/v1/models` ist genau der Modellname, den Cursor später “sieht”.
> Wenn dort z. B. `gpt-4o-mini` steht, dann wurde der Server mit `--served-model-name gpt-4o-mini` gestartet – unabhängig davon, welches Modell tatsächlich gemountet ist.

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

## Reality Check: “uncensored” fürs Coding

- Ein NVFP4 “Coder” ist **nicht automatisch uncensored** – das ist eine Frage von Training/Alignment, nicht vom Format.
- In unserem aktuellen Inventory ist das einzig sicher “abliterated” Modell **`deepseek-r1-8b-abliterated-bf16`** (läuft stabil, aber ist nur 8B).
- Wenn du **hohe Qualität + uncensored** willst, ist der realistischste nächste Schritt meist ein **größeres BF16/FP16 abliterated Instruct/Coder** (z. B. 32B‑Klasse). Das ist langsamer als NVFP4, aber qualitativ ein großer Sprung.

## Reality Check: Llama4‑Scout‑17B “großes Kontextfenster”

- Das theoretische Kontextfenster ist sehr groß, aber praktisch limitiert dich auf GB10 vor allem **KV‑Cache / Unified Memory**.
- “Sauber nutzbar” heißt: ja, es läuft; aber für **extrem** lange Kontexte musst du mit deutlich höherem RAM‑Verbrauch und ggf. langsamerer Performance rechnen (und ggf. die Server‑Konfiguration so setzen, dass nicht unnötig KV‑Cache für Max‑Len vorallokiert wird).

## Optional: GUI zum Umschalten (visuell)

Wenn du Modelle **visuell auswählen** willst (und im Hintergrund per SSH automatisch Start/Stop/Switch passiert), nutze:

- `tools/spark_model_switcher/` (lokales Streamlit‑Dashboard)
- Es zeigt `/health` + `/v1/models` live und kann deine Switch‑Scripts ausführen.
