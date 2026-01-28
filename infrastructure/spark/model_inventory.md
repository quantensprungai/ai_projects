<!-- Reality Block
last_update: 2026-01-22
status: draft
scope:
  summary: "Ist-Stand der Model-Assets auf Spark (Disk) + Serve-Namen/Ports + Hinweise zu Quant/Alignment."
  in_scope:
    - models present on disk (Spark)
    - served model names + ports
    - quantization / format notes
    - operational notes (what is actually usable)
  out_of_scope:
    - download instructions (see per-model docs/scripts)
    - sensitive secrets/tokens
notes:
  - "Quelle für 'on disk': ls/du auf /home/sparkuser/ai/models (Spark-56d0)."
  - "Quelle für 'served-model-name': /home/sparkuser/ai/scripts/serve/*."
-->

# Spark Model Inventory (Spark‑56d0 / GB10) — Ist‑Stand

## Begriffsklärung (wichtig)

- **On disk**: Ordner liegt unter `~/ai/models/...` auf Spark (heißt nur: Files vorhanden).
- **Served**: ein Inferenz‑Server (SGLang) läuft und liefert das Modell via `/v1/models`.
- **“Uncensored”**: ist **kein** Garant. Das ist i. d. R. ein Trainings-/Prompting‑Artefakt (und oft nur “weniger aligned”).
  Hardware (DGX Spark) “zensiert” nichts extra.

## Aktuell “served” (Cursor nutzbar)

| Served model name (Cursor) | Engine | Interner Port | Proxy Port | Status | Notes |
|---|---:|---:|---:|---|---|
| `deepseek-r1-8b-abliterated-bf16` | SGLang | `30001` | `31001` | ✅ läuft (aktuell) | Abliterated (BF16/FP16). Läuft stabil; nicht NVFP4/FP8‑optimiert. |
| `llama4-scout-17b-nvfp4` | SGLang | `30000` | `31000` | ✅ läuft (wenn gestartet) | Sehr großes theoretisches Kontextfenster; praktisch KV‑Cache‑/RAM‑Limits beachten. |
| `qwen3-32b-nvfp4` | SGLang | `30001` | `31001` | ✅ läuft (per Switch) | NVFP4 ModelOpt; “known good”. |

> Ports/Proxies/Token-Auth: siehe `infrastructure/spark/inference_endpoints.md`.

## On disk (bestätigt auf Spark)

## Reality Check: Quantisierung auf DGX Spark (GB10 / SM121)

- **NVFP4/MXFP4 ist das Ziel-Format** (Blackwell Tensor Cores), aber: je nach Engine/Build können FP4‑Kernels auf GB10 aktuell in **Fallbacks** laufen (Performance variiert).
- **FP8 ist oft der “sichere Default”**: breit unterstützt, stabil, meistens deutlich schneller/kleiner als BF16.
- **`compressed-tensors` ist aktuell unser größter Stolperstein**: mehrere Community‑FP8/NVFP4 Repos sind als `compressed-tensors` gepackt; unser aktuelles SGLang‑Image hat damit bekannte Probleme (Start scheitert / Scheme fehlt).
- **Pragmatische Regel für “läuft garantiert”**:
  - **NVIDIA‑Playbook/ModelOpt Checkpoints (NVFP4/FP8)** bevorzugen, oder
  - **plain BF16/FP16 safetensors** nutzen (auch für Abliteration), ggf. später requantizen.

### Core LLMs (SGLang/vLLM‑tauglich)

| Model folder (Spark) | Vermutetes Format | Größe (du) | On disk | Alignment/“uncensored” | Notes |
|---|---|---:|---:|---|---|
| `~/ai/models/qwen3/qwen3-32b-nvfp4` | NVFP4 | ~20G | ✅ | unbekannt | Aktuell “known good” für Cursor. |
| `~/ai/models/llama4/llama4-scout-17b-nvfp4` | NVFP4 | ~61G | ✅ | unbekannt | Served‑Name steht im Script. |
| `~/ai/models/phi4/phi4-reasoning` | (vermutl. FP8/BF16) | ~28G | ✅ | eher “safe” | Gute Reasoning‑Baseline; nicht “uncensored”. |
| `~/ai/models/qwen/qwen3-coder-30b-nvfp4` | NVFP4 | ~17G | ✅ | unbekannt | Coding‑Candidate. Serve/Switch‑Script vorhanden (served‑name: `qwen3-coder-30b-nvfp4`). |
| `~/ai/models/nvidia/nemotron-3-nano-fp8` | FP8 | ~31G | ✅ | unbekannt | Candidate für Agents/Tool‑Calling; evtl. extra Flags nötig. |
| `~/ai/models/nvidia/gpt-oss-20b` | (MXFP4 o.ä.) | ~39G | ✅ | unbekannt | Sehr groß; vLLM/SGLang‑Kompatibilität prüfen. |
| `~/ai/models/nvidia/gpt-oss-120b` | (MXFP4 o.ä.) | ~183G | ✅ | unbekannt | Sehr groß; “experimentell” (Unified Memory / OOM‑Risiko). |

### DeepSeek (Abliterated / R1)

| Model folder (Spark) | Vermutetes Format | Größe (du) | On disk | Läuft mit SGLang? | Notes |
|---|---|---:|---:|---:|---|
| `~/ai/models/deepseek/josiefied-r1-0528-qwen3-8b-abliterated-v1` | BF16/FP16 (safetensors) | ~16G | ✅ | ✅ | **Served name**: `deepseek-r1-8b-abliterated-bf16` |
| `~/ai/models/deepseek/deepseek-r1-70b-fp8-abliterated` | FP8 (**compressed-tensors / float-quantized**) | ~68G | ✅ | ❌ (aktuell) | `config.json` zeigt `quantization_config.quant_method=compressed-tensors`. Unser aktuelles SGLang‑Image hat damit bekannte Probleme → Modell kommt nicht “ready”. Kandidat für Engine/Image‑Upgrade oder anderer 70B‑Checkpoint (FP8 ohne compressed-tensors). |
| `~/ai/models/deepseek/deepseek-r1-0528-qwen3-8b-abliterated-nvfp4` | NVFP4 (`compressed-tensors`) | ~6.0G | ✅ | ❌ (aktuell) | Unser SGLang‑Image findet keine kompatible `compressed-tensors` Scheme → startet nicht. Kandidat für später (Image/Engine‑Upgrade). |

### Embeddings

| Model folder (Spark) | Größe (du) | On disk | Notes |
|---|---:|---:|---|
| `~/ai/models/embeddings/bge-m3` | ~2.2G | ✅ | multilingual Default |
| `~/ai/models/embeddings/bge-multilingual-gemma2` | ~28K | ✅ (Stub?) | Größe deutet auf Stub/partial hin → prüfen (Download vollständig?). |

### GGUF (kleinere Geräte / Laptop)

| Folder | Zweck | Notes |
|---|---|---|
| `~/ai/models/small/llama-3.2-3b-gguf` | Pi/Handy | vorhanden |
| `~/ai/models/small/phi4-mini-reasoning-gguf` | Pi/Handy | vorhanden |
| `~/ai/models/small/granite-4.0-micro-gguf` | Pi/Handy | vorhanden |
| `~/ai/models/laptop/mistral-small-3.2-gguf` | Laptop | vorhanden |
| `~/ai/models/laptop/qwen3-8b-gguf` | Laptop | vorhanden |


## “Uncensored” Modelle — realistische Erwartung

- **Am sichersten**: Behaupte “uncensored” nicht aus Namen/Blogposts, sondern teste es.
- Viele Community‑“uncensored” Modelle sind **nicht** NVFP4/FP8‑optimiert; sie laufen trotzdem (BF16/FP16), aber nicht “Spark‑maximal”.
- Wenn du Funnel dauerhaft nutzt: Auth ist Pflicht (siehe `inference_endpoints.md`).

## Nächste sinnvolle Pflegeaufgaben

- Optional: pro “Candidate” (phi4/nemotron/qwen3-coder) ein Serve‑Script + ein 3‑Zeilen Test (`/health`, `/v1/models`, `/v1/chat/completions`).


## Warum “Serve‑Script Pattern standardisieren”?

Damit neue Modelle **ohne Fußangeln** in Cursor/WebUI “wählbar” sind:
- **stabile Namen**: `--served-model-name ...` → `/v1/models` liefert eine saubere ID
- **stabile Ports/Proxies**: klare Zuordnung Model ↔ Port ↔ Proxy (`30000/30001` ↔ `31000/31001`)
- **exklusive Starts**: große Modelle werden zuverlässig gegenseitig gestoppt (Memory/KV‑Cache)
- **einheitliche Flags**: Quant/Attention/TP sind pro Modell sauber dokumentiert und reproduzierbar

## Downloads vorbereiten (Plan) – “in unserem Setting”

### Grundsatz: “wählbar” heißt bei großen Modellen meistens “umschaltbar”
Auf 128GB UMA ist es realistisch, **1 großes Modell gleichzeitig** sauber zu serven.
Heißt: du legst mehrere Model‑Ordner “on disk” ab, aber “served” ist immer nur eins — Umschalten per Script.

### Kandidaten (nicht installiert) — als TODO‑Liste
Diese Liste ist **keine** Aussage, dass die Modelle NVFP4/FP8 sind; das ist pro Repo/Release zu prüfen:
- Qwen2.5‑32B Instruct “abliterated” (BF16, Kandidat)
- DeepSeek‑R1 Distill Llama‑70B “abliterated” (groß, Kandidat)
- GPT‑OSS‑20B “abliterated” (falls verfügbar; Kandidat)

### Minimaler Ablauf pro neuem Modell
1. **Download** nach `~/ai/models/<vendor>/<model>/`
2. **Serve‑Script** anlegen/duplizieren (Port + `--served-model-name`)
3. **Proxy**: entweder bestehenden Port nutzen (Switch‑Workflow) oder neuen Proxy-Port definieren
4. **Test**: `/health`, `/v1/models`, `/v1/chat/completions`
5. **Cursor/WebUI**: Model‑ID eintragen (genau wie in `/v1/models`)

