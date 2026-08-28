<!-- Reality Block
last_update: 2026-06-02
status: draft
scope:
  summary: "Kleines GUI, um Spark-Modelle zu sehen und per SSH zu switchen."
  in_scope:
    - list models/actions
    - show live status (/health, /v1/models)
    - run switch scripts via ssh
  out_of_scope:
    - remote installation on Spark
    - secrets (Bearer Token etc.)
notes:
  - "Dieses Tool läuft lokal (z. B. auf VM105/Windows)."
-->

# Spark Model Switcher (GUI)

Ziel: **visuell Modelle auswählen** und im Hintergrund **Start/Stop/Switch** via SSH ausführen, plus Live‑Checks (`/health`, `/v1/models`).

## Voraussetzungen

- Auf deinem Windows/VM105: **OpenSSH** (`ssh`) im PATH
- Python 3.x lokal
- SSH Zugriff auf Spark (Port `2222`, User `sparkuser`)

## Setup

Im Ordner `infrastructure/spark/tools/spark_model_switcher/`:

```bash
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
```

Alternativ (Windows, empfohlen):

```powershell
.\setup.ps1
```

Konfig kopieren und anpassen:

- Kopiere `config.example.json` nach `config.json`
- Trage `spark.host` ein (z. B. `100.x`, MagicDNS, oder `spark-56d0...ts.net`)
- Optional: `ssh_identity_file` setzen (Pfad zu privatem Key)
- Optional: `actions[].remote_path` für Modelle ergänzen
- Für Qwen3.6 FP8: `remote_path` auf `/home/sparkuser/ai/scripts/serve/sglang_switch_to_qwen36_27b_fp8.sh` setzen

## Actions Schema (Model Picker)

Die GUI sortiert Buttons wie ein “Model Picker” über optionale Felder:

- **`category`**: `"Allround" | "Coding" | "Long-context" | "Uncensored-ish" | "Other"`
- **`order`**: Zahl (kleiner = weiter oben)
- **`slot`**: `"primary"` (typisch Port `30001`) oder `"secondary"` (typisch Port `30000`) – nur als Hinweis in der UI
- **`description`**: Kurzbeschreibung (wird unter dem Label angezeigt)

## Start

```bash
.\.venv\Scripts\python -m streamlit run app.py
```

## Was es kann / was nicht

- **Kann**: Buttons → remote Switch‑Scripts starten; Status anzeigen; Command‑Output anzeigen.
- **Kann nicht**: “magisch” neue Modelle bauen/abliterate/quantizen. Dafür bleiben `~/ai/scripts/` und separate Workflows zuständig.

## Troubleshooting: Exit Code 126

Wenn der Switcher `Exit Code: 126` meldet, ist das Skript auf Spark meist nicht ausführbar oder hat Windows-Zeilenenden (`CRLF`) nach `scp`.

Auf Spark (SSH):

```bash
sed -i 's/\r$//' /home/sparkuser/ai/scripts/serve/sglang_switch_to_qwen36_27b_fp8.sh
chmod +x /home/sparkuser/ai/scripts/serve/sglang_switch_to_qwen36_27b_fp8.sh
bash /home/sparkuser/ai/scripts/serve/sglang_switch_to_qwen36_27b_fp8.sh
```

Der Switcher ruft Scripts seit dem Fix per `bash <remote_path>` auf (nicht mehr als direktes Executable).

## Qwen3.6-27B-FP8: `qwen3_5` / Transformers zu alt

Symptom im Container-Log:

`model type qwen3_5 but Transformers does not recognize this architecture`

Ursache: `lmsysorg/sglang:spark` ist älter als Qwen3.6. Auf Spark:

```bash
docker pull scitrera/dgx-spark-sglang:0.5.11
export SGLANG_IMAGE=scitrera/dgx-spark-sglang:0.5.11
bash /home/sparkuser/ai/scripts/serve/sglang_switch_to_qwen36_27b_fp8.sh
```

Bis das klappt: im Switcher **Qwen3 32B (NVFP4)** starten (`sglang_switch_to_qwen.sh`).

## Ports / Slots (praktisch)

- **Primary**: typischerweise SGLang auf Port `30001` (hier laufen Allround/Coding/Reasoning-Modelle als “Default”).
- **Secondary**: optionaler zweiter Slot auf Port `30000` (oft Scout/Long‑Context), wenn Memory es zulässt.
- **Stop**:
  - “Stop Secondary (30000)” stoppt nur den Secondary‑Container (typisch `sglang-scout`).
  - “Stop ALL SGLang” stoppt beide Slots (Primary + Secondary).

