<!-- Reality Block
last_update: 2026-02-15
status: draft
scope:
  summary: "Setup für Llama 3.1 8B und Llama 3.2 11B auf Spark (SGLang, Model Switcher)."
  in_scope:
    - Download
    - Serve-Scripts
    - Model Switcher Integration
  out_of_scope:
    - Quantization (BF16/FP16 reicht für 8B/11B)
notes:
  - "OpenClaw Reality Check: Community empfiehlt 14B+ für Agent/Tool-Calling; 8B/11B sind 'lightweight'."
-->

# Llama 3.1 8B & Llama 3.2 11B – Setup auf Spark

## Reality Check: OpenClaw

Die OpenClaw-Community empfiehlt für Agent-/Tool-Calling **mindestens 14B**, idealerweise **32B+** (Qwen3-Coder 32B, GLM-4.7). Modelle unter 14B neigen zu Loops, Halluzinationen und instabilem Tool-Calling.

**Llama 3.1 8B und 3.2 11B** sind damit eher für:
- Leichte Chat-Aufgaben
- Schnelle Antworten (wenig VRAM)
- Experimente / Vergleich

Für **stabile OpenClaw-Agents** weiterhin Qwen3 32B oder DeepSeek R1 8B (abliterated) bevorzugen.

---

## 1) Modelle herunterladen (auf Spark)

**Voraussetzung:** Hugging Face Account, Llama-Lizenz akzeptiert (meta-llama/Llama-3.1-8B-Instruct, meta-llama/Llama-3.2-11B-Instruct).

```bash
# Auf Spark einloggen
ssh -p 2222 sparkuser@<spark-ip>

# Verzeichnisse anlegen
mkdir -p ~/ai/models/llama

# Llama 3.1 8B Instruct (~16 GB)
huggingface-cli download meta-llama/Llama-3.1-8B-Instruct \
  --local-dir ~/ai/models/llama/llama-3.1-8b-instruct

# Llama 3.2 11B Instruct (~22 GB)
huggingface-cli download meta-llama/Llama-3.2-11B-Instruct \
  --local-dir ~/ai/models/llama/llama-3.2-11b-instruct
```

Falls `huggingface-cli` fehlt: `pip install huggingface_hub[cli]` oder im SGLang-Container nutzen.

---

## 2) Serve-Scripts auf Spark deployen

Die Scripts liegen im Repo unter `infrastructure/spark/scripts/serve/`. Nach Spark kopieren:

```powershell
# Von Windows (Repo-Root: c:\Users\Admin105\ai_projects)
scp -P 2222 -o StrictHostKeyChecking=accept-new `
  c:\Users\Admin105\ai_projects\infrastructure\spark\scripts\serve\sglang_switch_to_llama31_8b.sh `
  c:\Users\Admin105\ai_projects\infrastructure\spark\scripts\serve\sglang_switch_to_llama32_11b.sh `
  sparkuser@100.96.115.1:~/ai/scripts/serve/
```

Auf Spark ausführbar machen:

```bash
chmod +x ~/ai/scripts/serve/sglang_switch_to_llama31_8b.sh
chmod +x ~/ai/scripts/serve/sglang_switch_to_llama32_11b.sh
```

---

## 3) Model Switcher konfigurieren

Die `config.json` im Model Switcher enthält bereits die neuen Actions (Llama 3.1 8B, Llama 3.2 11B). Falls du `config.example.json` nutzt, kopiere sie nach `config.json` und prüfe `spark.host`.

Start des Model Switchers:

```powershell
cd c:\Users\Admin105\ai_projects\infrastructure\spark\tools\spark_model_switcher
.\.venv\Scripts\python -m streamlit run app.py
```

Dann im UI auf **Llama 3.1 8B** oder **Llama 3.2 11B** → **Start/Switch** klicken.

---

## 4) Served Model Names (für Cursor/OpenWebUI)

Nach dem Switch liefert `GET /v1/models`:

| Modell | Served ID |
|--------|-----------|
| Llama 3.1 8B | `llama-3.1-8b-instruct` |
| Llama 3.2 11B | `llama-3.2-11b-instruct` |

In Cursor oder OpenWebUI als **Model Name** exakt diese ID eintragen.

---

## 5) Ports

Beide Modelle laufen auf dem **Primary Slot (Port 30001)** – wie Qwen und DeepSeek R1. Beim Switch wird der vorherige Primary gestoppt.

---

## Referenzen

- `inference_endpoints.md` – Ports, Health, Cursor-Setup
- `model_inventory.md` – Ist-Stand der Modelle
- `tools/spark_model_switcher/README.md` – GUI-Nutzung
