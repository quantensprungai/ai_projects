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
- **vLLM**: OpenAI‑kompatibles API, Throughput, Batch/RAG, große Kontexte

## Embeddings (aktueller Stand)

- **BGE statt Voyage**: Wenn du BGE-Embeddings nutzt, ist **`BAAI/bge-m3`** ein guter multilingual Default.
- Ablage (Beispiel): `~/ai/models/embeddings/bge-m3`

## Standard-Ports (Default)

- **SGLang**: `30000`
- **vLLM**: `8000`

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

- **vLLM always-on** für API/Projekte (Tools/RAG/Trading/Services)
- **SGLang on-demand** für interaktives Chat/Vision/Agent‑Dev (oder umgekehrt)

## Minimaler Operations-Flow

1. Engine wählen (SGLang vs vLLM)
2. Model Path prüfen (`~/ai/models/...`)
3. Service starten (systemd oder docker run)
4. Health/Test Call
5. Logs prüfen

## Autostart (systemd) – “D” aus der anderen KI

Note: Das Repo enthält hier **nur die Vorlagen**. Auf Spark legst du die Dateien unter `/etc/systemd/system/` an.

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

> Hinweis: Dieser Abschnitt ist eine **Dokumentation** (kein Source-of-Truth für den tatsächlichen Inhalt auf Spark).

Stand: 2026-01-12 (bitte bei Änderungen aktualisieren)

### Llama 4 (NVFP4)
- `llama4-scout-17b-nvfp4` – ✔ installiert

### DeepSeek
- `deepseek-v3` – ✔ installiert

### Phi‑4
- `phi4-reasoning` – ✔ installiert

### Qwen3
- `qwen3-32b-nvfp4` – ✔ installiert

### Embeddings
- `bge-3` – ✔ (du nutzt BGE; Details nachtragen, z. B. `bge-m3`)


## Links

- `sglang_config.md`
- `vllm_config.md`
- `inference_endpoints.md`
- `optimizations.md`
- `quantizations.md`


