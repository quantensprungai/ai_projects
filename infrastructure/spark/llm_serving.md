<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "Serving-Übersicht: welche Engine wofür, Start/Stop, Basis-Checks, Logs (Spark)."
  in_scope:
    - serving overview
    - operational checklist (documentation)
    - ports summary
  out_of_scope:
    - model downloads
    - container image pinning strategy
    - deep performance tuning
notes: []
-->

# LLM Serving (Spark)

## Übersicht

Auf Spark laufen die Inferenzserver als Container. In diesem Repo wird **nur dokumentiert**, nicht ausgeführt.

## Empfohlene Spark-Ordnerstruktur (Runtime auf Spark)

```text
~/ai/
  models/
    llama4/
    qwen3/
    deepseek/
    phi4/
    embeddings/
  servers/
    sglang/
    vllm/
    tensorrt/
  configs/
    sglang/
    vllm/
    huggingface/
    docker/
  scripts/
    download/
    serve/
    update/
    system/
  logs/
    sglang/
    vllm/
    models/
  projects/
    rag/
    agents/
    pipelines/
  cache/
    huggingface/
    sglang/
    vllm/
```

## Engines

- **SGLang**: interaktiv/low-latency, Agents, ggf. multimodal
- **vLLM**: OpenAI‑kompatibles API, Throughput, Batch/RAG, große Kontexte (**Achtung: auf GB10 aktuell je nach Image/Toolchain broken**)
- **TensorRT-LLM**: maximale Performance (insb. NVFP4/FP8), aber weniger flexibel (Build/Compile/Cache-Zyklen; eher “production” als “experiment”)
- **Ollama (Fallback)**: schnell “wieder online”, aber nicht der langfristige Standard auf Spark

## Reality Check: Quantisierung (GB10 / SM121)

- **NVFP4/MXFP4 (FP4)** ist das “native” Blackwell‑Ziel, aber in der Praxis hängt die Performance stark vom Engine‑Build und den verwendeten Kernels ab.
  - In vLLM können FP4‑Weights (je nach Build/Detection) auf **Marlin/weight-only FP4 Fallback** laufen → dann ist der Performance‑Gewinn gegenüber FP8/BF16 kleiner oder negativ.
  - Einige FP4‑Pfade (FlashInfer/CUTLASS) sind historisch stark auf **SM100a** fokussiert; auf GB10 (SM121) kann es daher zu **Fallbacks** oder Build‑Footguns kommen.
- **FP8** ist im Alltag oft der **stabile Sweet Spot**: deutlich schneller/kleiner als BF16, und in SGLang/vLLM breit unterstützt.
- **`compressed-tensors` vermeiden (Stand heute)**:
  - Viele Community‑“FP8/NVFP4” Repos sind `compressed-tensors` (float‑quantized). Unser aktuelles SGLang‑Setup hat damit bekannte Scheme/Loader‑Probleme.
  - Wenn ein Modell nicht startet: zuerst `config.json` prüfen (`quantization_config.quant_method`). Bei `compressed-tensors` ist ein Engine/Image‑Upgrade oder ein anderer Checkpoint meistens der schnellste Fix.

## Embeddings (aktueller Stand)

- **BGE statt Voyage**: Wenn du BGE-Embeddings nutzt, ist **`BAAI/bge-m3`** ein guter multilingual Default.
- Ablage (Beispiel): `~/ai/models/embeddings/bge-m3`

## Standard-Ports (Default)

- **SGLang**: `30000`
- **vLLM**: `8000`
- **Ollama**: `11434` (Fallback)
- **Open WebUI**: `8080`
- **OpenSSH (sshd, Admin-Fallback)**: `2222`

## Ist‑Stand (Spark‑56d0, GB10) – Reality Check

- **Open WebUI** läuft als Docker Container auf `:8080`.
- **Open WebUI Storage** liegt in einem Docker Volume:
  - `/var/lib/docker/volumes/open-webui/_data`
- **vLLM** kann auf GB10 je nach Container/Toolchain scheitern (PTXAS/Triton `sm_121a`).
  → In dem Fall ist **SGLang** die bevorzugte Engine.
- **Open WebUI** kann (und sollte) als OpenAI‑compatible Backend direkt auf SGLang zeigen (Ports `30000/30001`),
  statt über Ollama zu gehen.
- **SGLang Slot `:30001`** läuft stabil (OpenAI‑kompatibel: `/v1/models`, `/v1/chat/completions`) – welches Modell dort “default” ist,
  hängt vom Switch‑Script ab (z. B. Qwen ↔ R1‑8B BF16).
- **SGLang Llama4‑Scout‑17B NVFP4** ist installiert, aber der Start benötigt korrekte Flags/Quant‑Handling (siehe `sglang_config.md`).

## Zugriff (VM105 → Spark) – Reality Check

- **Tailscale SSH** kann je nach Installationsart (snap confinement) “operation not permitted” auslösen.
- Daher nutzen wir zusätzlich klassisches **OpenSSH (`sshd`)** als robusten Admin‑Pfad:
  - Port: **`2222`**
  - Nutzung: `ssh -p 2222 sparkuser@<spark-ts-ip> ...`

## Wie “Modelle starten” wirklich funktioniert (Mental Model)

- **Modelldateien** liegen auf Disk (`~/ai/models/...`).
- Ein Modell “läuft”, wenn ein **Server-Prozess** (SGLang oder vLLM) es in **RAM/Unified Memory/VRAM** geladen hat.
- **Ein großer Server = ein großes Modell** ist der Normalfall. Mehrere große Modelle parallel gehen nur, wenn genug Memory frei ist.

Praktisch heißt das:
- Wenn `sglang.service` läuft, ist **SGLang dauerhaft an** (und hält sein Modell geladen).
- Wenn du ein anderes Modell willst, **stopst du den Service**, änderst den Model‑Pfad, und startest wieder.

## Betriebsmodi (empfohlen)

### Modus 1: “Always-on” (1 Default‑Modell)

- **Ein** Modell läuft 24/7 (z. B. Scout‑17B oder DeepSeek‑V3).
- Vorteil: immer sofort verfügbar (API für alle Projekte).
- Nachteil: bindet Memory → weniger Platz für “On-demand” Modelle.

### Modus 2: “On-demand” (Modelle nur bei Bedarf)

- Du startest SGLang/vLLM nur, wenn du das Modell brauchst (z. B. “uncensored UI” oder ein spezielles Reasoning‑Modell).
- Vorteil: maximale Flexibilität.
- Nachteil: Start dauert (Load‑Zeit).

### Modus 3: “Hybrid” (empfohlen)

- **SGLang always-on** für “Default Chat/Agent/Multimodal”
- **SGLang on-demand** auf separatem Port für “uncensored / private” Workflows
- **vLLM** nur dann als always-on, wenn ein GB10-kompatibles Image bestätigt ist
- **Ollama** nur als kurzfristiger Fallback

## Minimaler Operations-Flow

1. Engine wählen (SGLang vs vLLM)
2. Model Path prüfen (`~/ai/models/...`)
3. Service starten (systemd oder docker run)
4. Health/Test Call
5. Logs prüfen

## Quick Cheat Sheet (kurz & praktisch)

### Start/Stop/Health

```bash
# SGLang (Port 30000)
curl -sf http://localhost:30000/health

# Ollama (Fallback)
curl -sf http://localhost:11434/api/tags

# Open WebUI
curl -sf http://localhost:8080 | head
```

## SGLang – OpenAI-kompatible Calls (praktisch)

Wenn Tools eine OpenAI‑API erwarten, sind diese Checks hilfreich:

```bash
curl -sf http://localhost:30000/v1/models | head

curl http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"local","messages":[{"role":"user","content":"Hallo"}]}'
```

## Cursor – wichtiges Setup-Prinzip

Wenn du in Cursor global “OpenAI API Key aktivierst” und die “Base URL overridest”, kann Cursor damit
auch seine **Cursor‑gehosteten Modelle** (z. B. GPT‑5.2) auf deine Base URL routen → dann kommt `Unauthorized`.

Empfehlung: Spark als separater Provider/Custom Model (OpenAI‑compatible) anbinden – oder den Override nur temporär nutzen.

### Monitoring (minimal)

```bash
docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
nvidia-smi
```

## Open WebUI – Privacy / Delete

Open WebUI speichert Chats/Settings im Docker-Volume `open-webui`.

**Alles löschen:**

```bash
docker rm -f open-webui
docker volume rm open-webui
```

## Autostart (systemd) – “D” aus der anderen KI

Note: Das Repo enthält hier **nur die Vorlagen**. Auf Spark legst du die Dateien unter `/etc/systemd/system/` an.

## On-demand Serving (empfohlen – passt zu unserem Setup)

Wir nutzen auf Spark kleine Helper-Skripte unter:
- `/home/sparkuser/ai/scripts/serve/`

Praktisch (von VM105 aus):
- Qwen starten:
  - `ssh -p 2222 sparkuser@<spark-ip> "/home/sparkuser/ai/scripts/serve/sglang_qwen_uncensored.sh"`
- Health:
  - `ssh -p 2222 sparkuser@<spark-ip> "/home/sparkuser/ai/scripts/serve/sglang_health.sh 30001"`
- Generate (ohne JSON-Quoting-Stress in PowerShell):
  - `ssh -p 2222 sparkuser@<spark-ip> "/home/sparkuser/ai/scripts/serve/sglang_generate.sh 30001 \"Hallo\""`

### `sglang.service` (Beispiel)

```ini
[Unit]
Description=SGLang LLM Server
After=network.target docker.service
Requires=docker.service

[Service]
Restart=always
RestartSec=5
ExecStartPre=/usr/bin/docker pull lmsysorg/sglang:spark
ExecStart=/usr/bin/docker run --rm --name sglang --gpus all -p 30000:30000 -v /home/sparkuser/ai/models/llama4/llama4-scout-17b-nvfp4:/model -v /home/sparkuser/ai/cache/sglang:/root/.cache lmsysorg/sglang:spark python3 -m sglang.launch_server --model-path /model --trust-remote-code --host 0.0.0.0 --port 30000 --tp 1
ExecStop=/usr/bin/docker stop -t 10 sglang

[Install]
WantedBy=multi-user.target
```

### `vllm.service` (Beispiel)

> Reality Check: vLLM ist auf unserem Spark/GB10 aktuell **nicht stabil** (Toolchain/`ptxas`/SM-Arch).  
> Dieses Beispiel ist eine Vorlage – wir pinnen später ein GB10‑kompatibles Image (nicht `latest`).

```ini
[Unit]
Description=vLLM OpenAI-Compatible Server
After=network.target docker.service
Requires=docker.service

[Service]
Restart=always
RestartSec=5
ExecStartPre=/usr/bin/docker pull vllm/vllm-openai:latest
ExecStart=/usr/bin/docker run --rm --name vllm --gpus all -p 8000:8000 -v /home/sparkuser/ai/models/llama4/llama4-scout-17b-nvfp4:/model -v /home/sparkuser/ai/cache/vllm:/root/.cache vllm/vllm-openai:latest --model /model --dtype auto --tensor-parallel-size 1 --max-model-len 2000000 --gpu-memory-utilization 0.92 --port 8000
ExecStop=/usr/bin/docker stop -t 10 vllm

[Install]
WantedBy=multi-user.target
```

### Enable/Start (auf Spark)

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now sglang
sudo systemctl enable --now vllm
systemctl status sglang
systemctl status vllm
```

## “Uncensored / ohne System Prompt” – was ist realistisch?

- **Ohne System Prompt**: Du kannst bei OpenAI‑kompatiblen APIs den System‑Teil weglassen (nur `user` Messages senden).  
  Das bedeutet aber **nicht**, dass ein Modell “ungefiltert” ist.
- **Uncensored**: Viele “uncensored” Modelle sind in Wahrheit nur **weniger aligned**. Fast jedes moderne Instruct‑Modell hat trotzdem eingebaute Safety/Policy‑Tendenzen.
- **Spark‑optimiert (NVFP4/FP8)** und **frei (ungated)** ist selten gleichzeitig. Viele NVFP4/FP8 Builds sind gated.

Wenn du “möglichst frei” willst:
- **DeepSeek‑V3** (gut, oft relativ wenig over‑filtering)
- **Qwen‑Instruct/Variants** (je nach Variante)
- Viele “uncensored” Community‑Derivate sind **nicht** NVFP4/FP8‑optimiert, laufen aber trotzdem via vLLM/SGLang (dann eben weniger “Blackwell‑spezifisch”).

## Was kommt als Nächstes, wenn alle Modelle da sind?

1. **Sanity Tests**: SGLang Health + vLLM Chat Completion + ein kurzer Embedding-Test (wenn Embedding-Service existiert)
2. **Start-Profile festlegen**: welches Modell läuft “default” (z. B. Scout‑17B), welches on-demand
3. **Stabilität/Observability**: Logs (journalctl), Crash-Recovery (systemd), Dashboard als Primär-Monitoring
4. **Projekt-Integration**: deine Projekte nutzen `inference_endpoints.md` als Source-of-Truth für URLs/Ports

## Model Inventory (Doku-Abschnitt)

Dieser Abschnitt ist bewusst kurz gehalten. Die **Source of Truth** (Doku) liegt hier:

- `infrastructure/spark/model_inventory.md`

Dort unterscheiden wir sauber:
- **on disk** (liegt unter `~/ai/models/...` auf Spark)
- **served** (läuft aktuell über SGLang/Proxy und ist in Cursor nutzbar)


## Links

- `sglang_config.md`
- `vllm_config.md`
- `inference_endpoints.md`
- `optimizations.md`
- `quantizations.md`


