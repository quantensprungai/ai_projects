<!-- Reality Block
last_update: 2026-02-06
status: draft
scope:
  summary: "Ops-Notizen für den HD Worker auf Spark: Debug/Retry, typische Fehler, Supabase Checks."
  in_scope:
    - job debugging
    - retry/requeue procedure
    - failure patterns
  out_of_scope:
    - worker code implementation (liegt auf Spark / separates Repo)
notes: []
-->

# HD Worker – Ops (Spark)

## Zweck

Kurze, praxisnahe Referenz: **Warum hängen Jobs? Wie debuggen wir das? Wie requeue’n wir sauber?**

**→ Schritt-für-Schritt „Was du selbst machen musst“:** **`infrastructure/spark/HD_WORKER_SPARK_SELBST_CHECKLISTE.md`** (Pfad, SCP, venv, .env, systemd, Neustart).

## Spark als einziger Worker-Host (OCR + LLM dort)

Da die nächsten Schritte **OCR** und **LLM** ohnehin auf Spark laufen sollen, kann der Worker **jetzt** auf Spark laufen statt auf VM102. Dann: **eine** Laufumgebung für Data Plane (extract_text, extract_text_ocr, classify_domain, extract_interpretations); OCR auf Spark: **GPU-OCR (EasyOCR)** – nutzt CUDA automatisch; LLM-Extraktion ruft direkt vLLM/SGLang auf Spark auf. **Kopplung:** Unverändert – Supabase = Control Plane, Spark pollt Jobs; welcher Host den Worker ausführt, ist der Queue egal.

**Checkliste „Wechsel von VM102 auf Spark“:** (1) Auf Spark: `mkdir -p ~/srv/hd-worker`, Worker-Dateien per SCP von `code/hd_saas_app/apps/web/scripts/` (inkl. `requirements-hd-worker-spark.txt`) bzw. `infrastructure/spark/hd-worker-spark.service` (als `hd-worker.service`). (2) venv: `cd ~/srv/hd-worker && python3 -m venv .venv && .venv/bin/pip install -r requirements-hd-worker-spark.txt` – enthält MVP + **MinerU**; OCR = **GPU-OCR (EasyOCR)**, kein Tesseract nötig; EasyOCR nutzt CUDA automatisch. (3) `.env` mit SUPABASE_URL + SUPABASE_SERVICE_ROLE_KEY (Cloud); für MinerU: `HD_USE_MINERU=true`, ggf. `HD_MINERU_BACKEND=hybrid`, `HD_MINERU_DEVICE=cuda`. (4) systemd (einmalig auf Spark, sudo): `sudo cp ~/srv/hd-worker/hd-worker.service /etc/systemd/system/`, `sudo systemctl daemon-reload`, `sudo systemctl enable --now hd-worker.service`. (5) Auf VM102: `sudo systemctl stop hd-worker.service`, damit nur Spark die Queue bedient.

**Dateien auf Spark kopieren (von Windows aus, Repo-Root = `ai_projects`):**

```powershell
cd code\hd_saas_app\apps\web\scripts
scp -P 2222 hd_worker_mvp.py requirements-hd-worker-mvp.txt requirements-hd-worker-spark.txt sparkuser@<spark-ts-ip>:~/srv/hd-worker/
scp -P 2222 c:\Users\Admin105\ai_projects\infrastructure\spark\hd-worker-spark.service sparkuser@<spark-ts-ip>:~/srv/hd-worker/hd-worker.service
```

(Oder von Linux/WSL: `scp -P 2222 hd_worker_mvp.py requirements-hd-worker-mvp.txt requirements-hd-worker-spark.txt hd-worker-spark.service sparkuser@<spark-ip>:~/srv/hd-worker/` und auf Spark `hd-worker-spark.service` als `hd-worker.service` umbenennen.)

**Einmalig auf Spark (interaktive SSH-Session, sudo braucht Passwort):**

```bash
# Verzeichnis + venv (MVP + MinerU)
mkdir -p ~/srv/hd-worker
cd ~/srv/hd-worker
python3 -m venv .venv
.venv/bin/pip install -r requirements-hd-worker-spark.txt

# systemd Service aktivieren (Worker läuft dauerhaft; OCR = EasyOCR/GPU, MinerU optional via HD_USE_MINERU)
sudo cp ~/srv/hd-worker/hd-worker.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now hd-worker.service
sudo systemctl status hd-worker.service --no-pager
```

## Grundannahmen (Architecture)

- **Supabase Cloud** = Control Plane (Auth, Storage, Tabellen, Jobs)
- **Spark Worker** = Data Plane (polling, processing, write-back)

Wichtig: Wenn die App lokal gegen `http://127.0.0.1:54321` schreibt, sieht Spark **keine** Jobs.

## Zugriff (robust)

- SSH Admin: `ssh -p 2222 sparkuser@<spark-ts-ip>`
- Worker Runtime Path (Spark): `~/srv/hd-worker/`

## Secrets / ENV (nicht verhandelbar)

- **Kein Secret in Terminal tippen** (History/Scrollback/Logs).
- Worker bekommt Secrets ausschließlich über ein **env‑file** (z.B. `~/srv/hd-worker/.env`) oder systemd `EnvironmentFile=`.
- Wenn ein Service Role Key sichtbar war: **rotieren**.

Minimal‑ENV:
- `SUPABASE_URL` (Cloud)
- `SUPABASE_SERVICE_ROLE_KEY` (Service Role; server‑only)

**MinerU (strukturiertes Markdown für RAG):** Auf Spark mit **`requirements-hd-worker-spark.txt`** ist MinerU bereits im venv installiert. In `.env`: `HD_USE_MINERU=true`, ggf. `HD_MINERU_BACKEND=hybrid`, `HD_MINERU_DEVICE=cuda`, `HD_MINERU_LANG=latin` (oder `en`, `ch`). **Automatische Spracherkennung (z. B. Chinesisch):** `HD_MINERU_AUTO_LANG=true` (und `HD_MINERU_LANG` leer) – Worker erkennt Sprache aus ersten Seiten (fast_langdetect) und übergibt sie an MinerU; Ergebnis in **asset.metadata.detected_language**. Dann nutzt `extract_text` (PDF) MinerU statt PyMuPDF; Chunking ist **heading-aware** (##/###-Abschnitte), optimal für LLM-Extraktion. Kein separater `extract_text_ocr`-Pfad für Hybrid-PDFs nötig. Gesamtprozess (PDF → Chunks → classify_domain → extract_interpretations): `infrastructure/spark/pdf_extraction_options.md`.

**MinerU mit CUDA (optional):** Wenn im Job-Debug `Torch not compiled with CUDA enabled` steht, nutzt das venv PyTorch ohne CUDA – MinerU (hybrid-auto-engine) schreibt dann keine .md, der Worker leitet Scans auf **extract_text_ocr** (EasyOCR) um. Das reicht für den Betrieb. Falls ihr MinerU auch für Scans mit strukturiertem Markdown nutzen wollt: im Worker-venv PyTorch mit CUDA nachinstallieren (siehe unten).

**CUDA-Version auf dem DGX prüfen und PyTorch-Wheel wählen:**

Auf Spark per SSH ausführen:

```bash
# Max. vom Treiber unterstützte CUDA-Version (reicht als Orientierung)
nvidia-smi

# Falls CUDA Toolkit installiert ist (z. B. auf DGX Station)
nvcc --version
# oder
cat /usr/local/cuda/version.txt 2>/dev/null || true
```

PyTorch-Wheel anhand der **unterstützten** CUDA-Version wählen (der Treiber muss mindestens diese Version unterstützen; nvidia-smi zeigt z. B. "CUDA Version: 12.4"):

| nvidia-smi / Umgebung | PyTorch install (im venv) |
|----------------------|---------------------------|
| CUDA 11.x (11.8)      | `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118` |
| CUDA 12.1            | `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121` |
| CUDA 12.4            | `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124` |
| CUDA 13.0 (z. B. DGX) | `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu130` |

Konkret auf dem Worker-venv (einmalig nach dem Check):

```bash
cd ~/srv/hd-worker
# z. B. bei CUDA 12.1:
.venv/bin/pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
# MinerU nutzt das venv-PyTorch; danach hybrid-auto-engine mit GPU testen
```

**VRAM:** MinerU (hybrid-auto-engine/VLM) braucht **16 GB+ VRAM** (laut MinerU-Maintainer). Läuft auf derselben GPU noch **SGLang** (oft ~10 GB+), reicht der Speicher nicht → **CUDA out of memory**. Dann entweder SGLang stoppen, wenn MinerU für Scans laufen soll, oder beim Worker den Fallback zu **extract_text_ocr** (EasyOCR) nutzen – der läuft auch bei geteilter GPU.

**Workflow bei geteilter GPU (SGLang + MinerU):** (1) SGLang stoppen → extract_text/extract_text_ocr laufen durch (Chunking für alle PDFs, MinerU hat ggf. mehr VRAM). (2) Wenn Chunking durch ist: SGLang wieder starten, alle fehlgeschlagenen **extract_interpretations**-Jobs auf `status=queued` und `error=null` setzen (Requeue). Dann laufen die LLM-Jobs, ohne dass MinerU gleichzeitig VRAM braucht.

Quick check:

```bash
cd ~/srv/hd-worker
set -a; source .env; set +a
python3 - <<'PY'
import os
print("SUPABASE_URL =", os.environ.get("SUPABASE_URL"))
print("HAS_SERVICE_ROLE_KEY =", bool(os.environ.get("SUPABASE_SERVICE_ROLE_KEY")))
PY
```

## Betrieb als Service (systemd)

Ziel: Worker läuft stabil weiter, Restart‑Policy, Logs über journalctl, keine „hängenden“ Sessions.

### 1) Unit File

Datei: `/etc/systemd/system/hd-worker.service`

```ini
[Unit]
Description=HD Worker (Supabase Job Processor)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=sparkuser
WorkingDirectory=/home/sparkuser/srv/hd-worker
EnvironmentFile=/home/sparkuser/srv/hd-worker/.env
ExecStart=/home/sparkuser/srv/hd-worker/.venv/bin/python3 /home/sparkuser/srv/hd-worker/hd_worker_mvp.py --loop --sleep 5
Restart=always
RestartSec=3

# Hardening (lightweight)
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=full
ProtectHome=false

[Install]
WantedBy=multi-user.target
```

Hinweis: `ProtectHome=false`, weil wir typischerweise unter `/home/sparkuser/srv/...` arbeiten. Kann später strenger werden.

### 2) Enable/Start/Logs

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now hd-worker.service

sudo systemctl status hd-worker.service --no-pager
journalctl -u hd-worker.service -n 200 --no-pager
journalctl -u hd-worker.service -f
```

## Job Debug (schnell)

### 1) Letzte Jobs ansehen (Service Role)

Auf Spark (mit `.env` geladen):

```bash
cd ~/srv/hd-worker
set -a; source .env; set +a

python3 - <<'PY'
import os,requests
url=os.environ['SUPABASE_URL']
key=os.environ['SUPABASE_SERVICE_ROLE_KEY']
h={'apikey':key,'Authorization':f'Bearer {key}'}
params={'select':'id,account_id,job_type,status,attempts,error,debug,created_at,started_at,finished_at','order':'created_at.desc','limit':'10'}
r=requests.get(f"{url}/rest/v1/hd_ingestion_jobs", params=params, headers=h, timeout=30)
print(r.status_code)
print(r.text)
PY
```

### 1b) OCR‑Jobs (`extract_text_ocr`) gezielt ansehen

```bash
cd ~/srv/hd-worker
set -a; source .env; set +a

python3 - <<'PY'
import os,requests
url=os.environ['SUPABASE_URL']
key=os.environ['SUPABASE_SERVICE_ROLE_KEY']
h={'apikey':key,'Authorization':f'Bearer {key}'}
params={
  'select':'id,account_id,job_type,status,attempts,error,debug,created_at,started_at,finished_at',
  'job_type':'eq.extract_text_ocr',
  'order':'created_at.desc',
  'limit':'20'
}
r=requests.get(f"{url}/rest/v1/hd_ingestion_jobs", params=params, headers=h, timeout=30)
print(r.status_code)
print(r.text)
PY
```

### 2) Logs

```bash
tail -n 200 ~/srv/hd-worker/logs/worker.log
```

### 3) Ergebnisse prüfen (Chunks, Interpretationen)

- **Chunks:** Tabelle **`hd_asset_chunks`** – pro Asset (PDF) viele Zeilen mit `chunk_index`, `text_clean`, `metadata` (source: mineru / pymupdf / easyocr). Filter z. B. `asset_id=eq.<asset_id>`.
- **Interpretationen:** Tabelle **`hd_interpretations`** – pro Chunk eine Zeile mit `payload` (essence, mechanics, expression, …). Filter `asset_id=eq.<asset_id>` und ggf. `system_id=eq.bazi` (oder hd/astro). In der App: wo die Inhalte/Interpretationen pro Dokument angezeigt werden.

Pipeline-Reihenfolge: extract_text (oder extract_text_ocr) → Chunks in `hd_asset_chunks` → classify_domain → extract_interpretations → Einträge in `hd_interpretations`.

## Worker-Code neu laden (ohne sudo)

Nach jedem **scp** von `hd_worker_mvp.py` (oder anderen Skripten) den Worker-Prozess neu starten, damit der **neue Code** geladen wird – der laufende Prozess nutzt sonst weiter die alte Version aus dem Speicher.

```bash
pkill -f "hd_worker_mvp.py"
# systemd startet den Worker automatisch neu (Restart=always)
pgrep -af hd_worker_mvp   # prüfen, ob neuer Prozess läuft
```

Erst danach liefern z. B. verbesserte Fehlermeldungen (z. B. „Raw content (first 500 chars)“ bei extract_interpretations/LLM-JSON) die neuen Infos.

## Requeue / Retry (wenn Fix deployed ist)

```bash
cd ~/srv/hd-worker
set -a; source .env; set +a

python3 - <<'PY'
import os,requests
url=os.environ['SUPABASE_URL']
key=os.environ['SUPABASE_SERVICE_ROLE_KEY']
job_id="__JOB_ID__"
headers={'apikey':key,'Authorization':f'Bearer {key}','Content-Type':'application/json'}

patch={'status':'queued','error':None}
r=requests.patch(f"{url}/rest/v1/hd_ingestion_jobs?id=eq.{job_id}", headers=headers, json=patch, timeout=30)
print("patch", r.status_code)
PY
```

### Requeue: OCR‑Jobs schnell zurück auf `queued`

```bash
cd ~/srv/hd-worker
set -a; source .env; set +a

python3 - <<'PY'
import os,requests
url=os.environ['SUPABASE_URL']
key=os.environ['SUPABASE_SERVICE_ROLE_KEY']
headers={'apikey':key,'Authorization':f'Bearer {key}','Content-Type':'application/json'}
job_id="__JOB_ID__"
patch={'status':'queued','error':None}
r=requests.patch(f"{url}/rest/v1/hd_ingestion_jobs?id=eq.{job_id}", headers=headers, json=patch, timeout=30)
print("patch", r.status_code)
PY
```

## Typische Fehlerbilder

### A) Jobs bleiben “queued/pending”, Worker zeigt keine Aktivität

- Ursache: App schreibt gegen **lokales Supabase**, Worker pollt **Cloud Supabase**.
- Fix: App‑Env auf Cloud stellen (URL + anon/public key) und Dev Server neu starten.

### B) `Circular reference detected` (import_assets_jsonl)

- Ursache: Worker schreibt zu große / nicht JSON‑serialisierbare Strukturen nach `metadata` (z. B. komplettes Objekt als `source_line`).
- Fix: `source_line` nur als **kleines Subset** speichern (flach, ohne Self‑Refs / ohne ganze Payloads).

### C) Jobs hängen auf `running`

- Ursache: Worker Prozess ist weg/abgestürzt, Job wurde nie auf `failed/completed` gesetzt.
- Quick Fix: Job requeue’n (siehe „Requeue / Retry“) und Worker‑Logs prüfen.

---

## MinerU Debugging (leere Ordner, Exit 0)

Wenn MinerU mit **Exit 0** endet, aber **keine .md-Datei** schreibt (nur leere Unterordner wie `tmp.../hybrid_auto/images`), hilft Ursachenforschung:

### 1) Was der Worker jetzt liefert

- Bei „MinerU produced no .md file“ enthält die **Fehlermeldung** (und bei Fallback das Job‑Debug) jetzt:
  - Verzeichnislisting des Ausgabeverzeichnisses
  - **MinerU stdout** (erste 2000 Zeichen)
  - **MinerU stderr** (erste 2000 Zeichen)
- **Fallback deaktivieren**, damit der Job fehlschlägt und der volle Error in der DB steht: in `.env` setzen: **`HD_MINERU_NO_FALLBACK=true`**, Worker neu starten, Job requeuen. Dann steht die komplette Diagnose in `hd_ingestion_jobs.error`.

### 2) PDF-Eigenschaften prüfen (auf Spark)

PDF lokal ablegen (z.B. aus Supabase Storage heruntergeladen) und prüfen:

```bash
cd ~/srv/hd-worker
.venv/bin/python3 -c "
import fitz
path = '/pfad/zur/datei.pdf'  # anpassen
doc = fitz.open(path)
print('Seiten:', len(doc))
print('Verschlüsselt:', doc.is_encrypted)
if len(doc) > 0:
    print('Erste Seite Text (500 Zeichen):', doc[0].get_text()[:500])
else:
    print('Keine Seiten')
doc.close()
"
```

### 3) MinerU manuell testen (auf Spark)

```bash
cd ~/srv/hd-worker
mkdir -p /tmp/mineru_debug
.venv/bin/mineru -p /pfad/zur/datei.pdf -o /tmp/mineru_debug -b hybrid-auto-engine --device cuda

echo "Exit code: $?"
find /tmp/mineru_debug -type f
ls -laR /tmp/mineru_debug
```

So siehst du direkt, was MinerU ausgibt und ob Dateien woanders landen. Bei Bedarf `--lang latin` (oder `en`, `ch`) ergänzen.

### 4) Typische Ursachen (Checkliste)

| Möglichkeit | Check |
|------------|--------|
| PDF leer (0 Seiten) | `len(doc)` in Schritt 2 |
| PDF verschlüsselt | `doc.is_encrypted` in Schritt 2 |
| Reiner Scan, OCR schlägt fehl (Modell/CUDA) | MinerU **stderr** in Job‑Error/Debug (Schritt 1) |
| MinerU schreibt woanders hin | `find /tmp/mineru_debug` in Schritt 3 |

