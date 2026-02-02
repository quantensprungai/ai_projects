<!-- Reality Block
last_update: 2026-01-30
status: stable
scope:
  summary: "Täglicher Workflow für Fast-Downloads: Limit-Checks, Downloads starten, Retries, Monitoring."
  in_scope:
    - daily download workflow
    - limit management
    - retry procedures
    - monitoring and maintenance
  out_of_scope:
    - technical setup (siehe code/docs/FAST_DOWNLOAD_SETUP.md)
    - complete end-to-end workflow (siehe complete_workflow.md)
notes: []
-->

# Täglicher Workflow - Fast-Downloads

## Aktueller Stand

### Was wir haben:
- ✅ **Fast-Download-System** mit Member-API
- ✅ **Relevanz-Filterung** basierend auf `topics.txt` (107 Topics)
- ✅ **Tägliches Limit-Tracking** (50 Downloads/Tag)
- ✅ **Rate-Limiting-Behandlung** (429-Fehler)
- ✅ **Retry-System** für fehlgeschlagene Downloads
- ✅ **Queue-Management** (Reset, Status-Tracking)

## Täglicher Workflow

### 1. Limit prüfen (jeden Tag)

**Auf VM102 (Linux):**
```bash
# SSH zu VM102
ssh user@100.83.17.106

# Wechsle ins Projekt-Verzeichnis
cd ~/annas-archive-toolkit

# Secret laden
set -a; source /etc/annas-archive-toolkit/member.env; set +a

# Config setzen
export AAT_CONFIG=projects/hd_content/config.json

# Limit prüfen
python3 src/check_daily_limit.py
```

**Output-Beispiele:**
```
✅ Kann downloaden: 50 Downloads verfügbar
❌ Limit erreicht: 50/50 Downloads heute verwendet
```

### 2. Downloads starten (falls Limit verfügbar)

```bash
# Option A: Alle verfügbaren Downloads nutzen
python3 src/fast_download_acquire.py --max-items $(python3 src/check_daily_limit.py --json | jq -r '.remaining')

# Option B: Feste Anzahl (z.B. 20 für Tests)
python3 src/fast_download_acquire.py --max-items 20

# Option C: Nur sehr relevante Items (Score >= 0.5)
python3 src/fast_download_acquire.py --min-relevance-score 0.5
```

### 3. Fehlgeschlagene Downloads retry (täglich)

**Nach Limit-Reset (00:00 UTC) oder bei verfügbarem Limit:**
```bash
# Retry alle fehlgeschlagenen Downloads
python3 src/retry_failed_downloads.py

# Oder: Nur erste 10 retry
python3 src/retry_failed_downloads.py --max-items 10
```

### 4. Status prüfen

```bash
# Zeige Statistik
cat output/hd_content/acquire_queue.json | jq '.queue | group_by(.status) | map({status: .[0].status, count: length})'

# Zeige completed Items von heute
cat output/hd_content/acquire_queue.json | jq '.queue[] | select(.status == "completed" and (.completed_at | startswith("'$(date -u +%Y-%m-%d)'")))'

# Zeige failed Items
cat output/hd_content/acquire_queue.json | jq '.queue[] | select(.status == "failed") | {title: .title, error: .last_error}'
```

## Workflow bei Limit-Erreichung

### Wenn tägliches Limit erreicht (50/50):

1. **Warte bis morgen (00:00 UTC)**
   - Limit wird automatisch zurückgesetzt
   - Nutze `check_daily_limit.py` um zu prüfen

2. **Retry fehlgeschlagene Downloads**
   ```bash
   python3 src/retry_failed_downloads.py
   ```

3. **Priorisiere wichtige Items**
   - Nutze `--min-relevance-score` um nur sehr relevante Items zu laden
   - Nutze `--max-items` um gezielt zu limitieren

## Erweiterung für weitere Inhalte (BaZi, etc.)

### 1. Topics-Liste erweitern

**Auf VM105 (Windows):**
```powershell
# Öffne topics.txt
code code\annas-archive-toolkit\projects\hd_content\topics.txt

# Füge neue Topics hinzu:
# BaZi / Four Pillars
bazi
four pillars
八字
四柱
```

**Übertragen:**
```powershell
cd code\annas-archive-toolkit
powershell -ExecutionPolicy Bypass -File .\transfer_to_vm102.ps1
```

### 2. Queue neu erstellen (optional)

**Auf VM102 (Linux):**
```bash
# Falls neue Metadaten gesammelt wurden
python3 src/libgen_metadata_collector.py  # Mit erweiterten Topics
python3 src/export_assets.py
python3 src/build_acquire_queue.py
```

### 3. Downloads starten

```bash
# Gleicher Workflow wie oben
python3 src/check_daily_limit.py
python3 src/fast_download_acquire.py --max-items 50
```

## Code-Updates von VM105 nach VM102

### Workflow:

**Auf VM105 (Windows):**
```powershell
# 1. Vergleich (optional)
cd C:\Users\Admin105\ai_projects\code\annas-archive-toolkit
powershell -ExecutionPolicy Bypass -File .\compare_files.ps1

# 2. Transfer
powershell -ExecutionPolicy Bypass -File .\transfer_to_vm102.ps1
```

**Auf VM102 (Linux):**
```bash
# 3. Config aktivieren (falls geändert)
cp projects/hd_content/config_vm102.json projects/hd_content/config.json

# 4. Scripts sind jetzt aktualisiert
```

## Monitoring & Wartung

### Wöchentliche Checks:

1. **Queue-Status prüfen:**
   ```bash
   python3 src/check_daily_limit.py
   cat output/hd_content/acquire_queue.json | jq '.queue | group_by(.status) | map({status: .[0].status, count: length})'
   ```

2. **Failed Items analysieren:**
   ```bash
   cat output/hd_content/acquire_queue.json | jq '.queue[] | select(.status == "failed") | {title: .title, error: .last_error, attempts: .download_attempts}'
   ```

3. **Topics-Liste erweitern** (falls neue relevante Begriffe gefunden)

4. **Code-Updates** (falls neue Features hinzugefügt)

## Troubleshooting

### "Limit erreicht, aber Downloads fehlgeschlagen"
- Nutze `retry_failed_downloads.py` morgen
- Prüfe `last_error` in Queue für Details

### "Zu viele I-Ching Items (nicht HD-relevant)"
- Erhöhe `--min-relevance-score` auf 0.5 oder 0.7
- Oder: Erweitere Topics-Liste mit spezifischeren Begriffen

### "Rate Limiting trotz erhöhter Delay"
- Prüfe ob Config aktualisiert wurde (`delay_between_requests: 12.0`)
- Nutze `retry_failed_downloads.py` später

### "Scripts funktionieren nicht"
- Prüfe: Wurde `transfer_to_vm102.ps1` ausgeführt?
- Prüfe: Ist Config aktiviert? (`cp config_vm102.json config.json`)
- Prüfe: Ist Secret geladen? (`source /etc/annas-archive-toolkit/member.env`)

## Links

- **Technische Setup-Anleitung:** `../../code/annas-archive-toolkit/docs/FAST_DOWNLOAD_SETUP.md`
- **Kompletter Workflow:** `complete_workflow.md`
- **High-Level Workflow:** `workflow.md`
- **Execution Guide:** `../../code/annas-archive-toolkit/docs/EXECUTION_GUIDE.md`
