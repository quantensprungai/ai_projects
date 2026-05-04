<!-- Reality Block
last_update: 2026-04-20
status: stable
scope:
  summary: "Spark-Worker, MinerU, VM102-PDF-Vorprozess; inkl. Inner-Compass-sys_*-Hinweis."
  in_scope:
    - worker ops and mineru workaround
    - vm102 annas archive upload bridge
    - ic vs legacy naming note
  out_of_scope:
    - ic app ui
notes:
  - "Abschnitte mit hd_*-Tabellennamen sind HD-SaaS-Historie; IC nutzt sys_* (s5_runbook, aa_ic_toolkit_alignment)."
-->

# HD Worker – Übergabe (Spark)

## Kontext / Zweck
Ziel ist eine robuste PDF-Pipeline für RAG/LLM: Upload → Extraktion → Chunking → Interpretation.  
Der Worker läuft auf Spark (GPU), Supabase ist Control Plane.

### Inner Compass (`sys_*`) — gleiche Pipeline, andere Tabellen
Für **Inner Compass** sind die Schritte dieselben (MinerU, Worker-Loop), die **Postgres-Objekte** heißen aber **`sys_*`** (z. B. `sys_source_chunks`, `sys_interpretations`, `sys_ingestion_jobs`). PDF-Upload von VM102: `hd_saas_uploader.py` mit **`--sys-mode`** → `sys_uploads_raw` / `sys_sources` / `sys_ingestion_jobs`. Worker-Code: **`code/inner_compass_app/apps/web/scripts/ic_worker.py`**. Runbook: **`projects/inner_compass/reference/s5_runbook.md`**, Alignment: **`projects/inner_compass/reference/aa_ic_toolkit_alignment.md`**. Deploy Uploader 105→102: **`infrastructure/spark/sync_aa_uploader_to_vm102.ps1`**. — Abschnitte unten mit **`hd_*`**-Namen beschreiben die **ältere HD-SaaS**-Benennung; für IC jeweils das **`sys_*`**-Äquivalent verwenden.

## Aktueller Stand (Feb 2026)
- Worker ist auf Spark eingerichtet (systemd, venv, `.env`).  
- MinerU ist integriert und optional aktivierbar (`HD_USE_MINERU=true`).  
- **Workaround aktiv:** `draw_layout_bbox` in MinerU auf Spark deaktiviert (pypdf „negative seek“); MinerU erzeugt wieder .md. CLI-Test bestätigt (BaZi-PDF 81).  
- Bei Scan-PDFs erfolgt Fallback zu OCR (`extract_text_ocr` / EasyOCR).  
- Debug enthält bei „no .md“ Laufzeit `mineru_duration_sec`.

**Status 2026-02-09:** Ein konkreter `extract_text`-Job (ein PDF) wird weiterhin mit `routed_to: extract_text_ocr`, `extracted_text_len: 0` und **ohne** `mineru_fallback` im Job-Debug abgeschlossen (Attempts 27–29). Worker-Code enthält `**debug`/`_debug_out` und Truncation; Env unter systemd ist korrekt. Ursache (Logging/DB oder MinerU-Pfad) noch offen. Details: **`infrastructure/spark/hd_worker_ops.md`** → Abschnitt „Status (Stand 2026-02-09)“.

## Pipeline (App → Worker → LLM)
1. **App-Upload**  
   PDF → Supabase Storage. Server Action legt Asset/Document/Document_File an und erstellt **`extract_text`**-Job.
2. **Worker: `extract_text`**  
   - Mit `HD_USE_MINERU=true`: MinerU (hybrid-auto-engine) → Markdown  
   - Sonst: PyMuPDF → falls Scan/zu wenig Text → **`extract_text_ocr`**
3. **Chunking**  
   - MinerU-Markdown → **heading-aware** Chunking  
   - Fallback → Paragraph-Chunking  
   → `hd_asset_chunks`
4. **classify_domain**  
   Klassifiziert System/Domain (z. B. hd/bazi) und schreibt in Asset-Metadata.
5. **extract_interpretations**  
   LLM verarbeitet Chunks → strukturierte JSON-Interpretationen in `hd_interpretations`.

## Bisheriges Problem (durch Workaround behoben)
MinerU erzeugte JPGs (Predict 100 %), stürzte aber in `draw_layout_bbox` (pypdf) ab und schrieb keine .md → Fallback zu PyMuPDF/OCR. Durch Deaktivieren von `draw_layout_bbox` im MinerU-venv auf Spark ist MinerU wieder nutzbar (siehe Workaround).

## Ergebnis CLI-Test (Feb 2026, BaZi-PDF 81)

Direkter MinerU-CLI-Lauf auf Spark (gleiches PDF wie im Worker) hat die **Ursache** geliefert:

- **Predict-Phase läuft durch** (125 + 621 Seiten, GPU).
- **Absturz danach** in `_process_output` → `draw_layout_bbox(...)`: MinerU zeichnet ein Layout-Debug-PDF und liest dazu die Original-PDF mit **pypdf** (`PdfReader`). pypdf wirft **`ValueError: negative seek value -999999576`** (kaputter xref-Eintrag in der PDF oder pypdf-Inkompatibilität).
- **Folge:** MinerU kommt nie zum Schreiben der .md – der Prozess bricht vorher ab (nicht Exit 0 im CLI, sondern Exception; im Worker evtl. trotzdem als „keine .md“ sichtbar wenn der Subprocess die Exception nicht sauber nach außen reicht).

**Fazit:** Ursache ist **nicht** GPU/Backend generell, sondern der Schritt **Layout-BBox zeichnen** (pypdf + diese PDF).

## Hypothese (aktualisiert)
Der Markdown-Schreibschritt wird nie erreicht, weil davor **draw_layout_bbox** mit pypdf auf die PDF zugreift und bei (einigen) PDFs mit ungültigem xref abstürzt.

**Backend `pipeline` getestet:** Derselbe Fehler – auch `pipeline` ruft in `_process_output` **draw_layout_bbox** auf (Zeile 117 in `mineru/cli/common.py`). Beide Backends teilen diesen Schritt; Workaround muss dort ansetzen.

## Eigentlicher Prozess (Betrieb)

Der **Worker** nutzt dasselbe venv wie der CLI-Test (`~/srv/hd-worker/.venv`). Der Patch wurde in genau diesem venv angewendet – **für den laufenden Betrieb ist nichts weiter nötig.** Neue `extract_text`-Jobs (mit `HD_USE_MINERU=true`) werden von MinerU verarbeitet und liefern .md → heading-aware Chunking → wie vorgesehen.

**Nur in diesen Fällen den Patch erneut ausführen:**
- **MinerU-Upgrade:** Nach `pip install -U mineru` (oder Reinstall des venv) auf Spark: einmalig `python infrastructure\spark\run_patch_on_spark.py` von Windows aus.
- **Neues Spark-Setup:** Beim Einrichten eines neuen Worker-Venv (neue Maschine / frisches venv) den Workaround einmal anwenden (run_patch_on_spark.py oder Option B/C im Abschnitt Workaround).

**Optional (Follow-up):** MinerU-Issue/PR für optionale Deaktivierung von `draw_layout_bbox` (CLI-Flag/Env), damit wir langfristig ohne manuellen Patch auskommen.

## Workaround: draw_layout_bbox auf Spark deaktivieren

Damit MinerU die .md schreibt, den Layout-Debug-Schritt in MinerU abschalten. **Einmalig auf Spark** (nach jedem `pip install -U mineru` ggf. erneut anwenden).

**Option A – Patch per Python ausführen (empfohlen, kein CRLF-Problem):** Im Repo-Root `ai_projects`:

```powershell
python infrastructure\spark\run_patch_on_spark.py
```

(Optional: `python infrastructure\spark\run_patch_on_spark.py sparkuser@spark-56d0` für anderen Host.) Das Skript verbindet per SSH mit Spark und führt den Patch dort aus – keine .sh-Datei, keine Zeilenenden-Probleme.

**Option B – Shell-Skript (LF nötig):** Repo enthält `infrastructure/spark/patch_mineru_draw_bbox.sh`. Mit LF-Pipe:  
`(Get-Content -Raw infrastructure\spark\patch_mineru_draw_bbox.sh) -replace "`r`n", "`n" | ssh -p 2222 sparkuser@100.96.115.1 "bash -s"`.  
Oder SCP + auf Spark ausführen (dort ggf. zuerst `sed -i 's/\r$//' patch_mineru_draw_bbox.sh`).

(Spark-Host ggf. ersetzen.) Das Skript fügt in MinerU `common.py` die Zeile `f_draw_layout_bbox = False` vor `if f_draw_layout_bbox:` ein. Danach MinerU-CLI oder Worker erneut ausführen.

**Option C – Manuell in nano:** Datei `~/srv/hd-worker/.venv/lib/python3.12/site-packages/mineru/cli/common.py` öffnen, in der Funktion `_process_output` direkt vor `if f_draw_layout_bbox:` die Zeile `f_draw_layout_bbox = False  # Workaround: …` einfügen. Speichern, dann MinerU/Worker neu starten.

Optional CLI-Test:

```bash
cd ~/srv/hd-worker && source .venv/bin/activate
mineru -p 81970458e683c785171eb93326a97dfc.pdf -o /tmp/mineru_test_fixed -b hybrid-auto-engine --device cuda
find /tmp/mineru_test_fixed -name "*.md"
```

## Nutzen mit MinerU-.md (jetzt aktiv)
- Heading-aware Chunks → bessere RAG-Qualität  
- `extract_interpretations` liefert hochwertigere Struktur  
- Weniger OCR-Overhead; Fallback zu PyMuPDF/OCR nur noch bei echten Scan-PDFs (wenig Text)

## Woher kommen die PDFs? (Vorprozess VM102)

PDFs können **vor** dem Worker in einem **Vorprozess auf VM102** runtergeladen werden (Anna's Archive Toolkit, teils in Docker):

- **Fast-Download** (Member-API / Einzel-Downloads):  
  PDFs liegen unter **`./output/hd_content/downloads/fast_download/<md5_prefix>/<md5>.pdf`** (relativ zum Toolkit-Repo-Root auf VM102, z. B. `~/libgen-survival-project` oder `~/annas-archive-toolkit`).
- **qBittorrent/Torrent-Bulk:**  
  PDFs landen in **`/downloads_hd/_UNSORTED`**, nach Sortierung in **`/downloads_hd/_SORTED`**.

Das Script **`hd_saas_uploader.py`** (im Anna's-Archive-Toolkit-Repo) lädt diese PDFs + Metadaten nach **Supabase Storage** hoch und legt die `extract_text`-Jobs an. Der **Worker** (Spark) holt die PDFs dann per Job aus Supabase – er speichert sie nicht dauerhaft auf VM102.

**Für den MinerU-CLI-Test („no .md“-Diagnose):**
- **Option A:** Eine PDF von VM102 nach Spark kopieren (z. B. aus `output/hd_content/downloads/fast_download/...` oder `/downloads_hd/_SORTED`), dann auf Spark: `mineru -p <datei>.pdf -o /tmp/mineru_test -b hybrid-auto-engine --device cuda`.
- **Option B:** Auf Spark die gleiche PDF aus Supabase laden (bucket/path aus dem Job-Debug, z. B. **`sys_ingestion_jobs.debug`** unter Inner Compass; Legacy HD-SaaS: `hd_ingestion_jobs.debug`), dann MinerU wie oben. Siehe `hd_worker_ops.md` (Job Debug) für das Download-Snippet.
- **Option C:** PDF von Windows (z. B. `C:\Users\Admin105\Downloads\bazi_pdfs\81\...`) per SCP auf Spark kopieren, dann MinerU-CLI – siehe Runbook unten.

### MinerU CLI-Test Runbook (PDF von Windows → Spark)

**1) Von Windows (PowerShell): PDF auf Spark kopieren**

Spark-Host ggf. anpassen (z. B. Tailscale-Name statt IP).

```powershell
scp -P 2222 -o StrictHostKeyChecking=accept-new "C:\Users\Admin105\Downloads\bazi_pdfs\81\81970458e683c785171eb93326a97dfc.pdf" sparkuser@100.96.115.1:~/srv/hd-worker/
```

**2) Auf Spark: SSH + MinerU ausführen**

```bash
ssh -p 2222 sparkuser@100.96.115.1
cd ~/srv/hd-worker
source .venv/bin/activate
mineru -p 81970458e683c785171eb93326a97dfc.pdf -o /tmp/mineru_test -b hybrid-auto-engine --device cuda
```

**3) Prüfen: Wurde eine .md erzeugt?**

```bash
find /tmp/mineru_test -name "*.md"
ls -laR /tmp/mineru_test
```

- Wenn **.md vorhanden** → MinerU funktioniert im CLI; Problem liegt ggf. an Worker-Umgebung (Temp-Pfad, cwd, etc.).
- Wenn **keine .md** → stdout/stderr von MinerU lesen; ggf. mit `--device cpu` oder `-b pipeline` erneut testen.

**Optional (CPU-Test):**

```bash
mineru -p 81970458e683c785171eb93326a97dfc.pdf -o /tmp/mineru_test_cpu -b hybrid-auto-engine --device cpu
find /tmp/mineru_test_cpu -name "*.md"
```

Doku Vorprozess: `code/annas-archive-toolkit/docs/HD_SAAS_UPLOAD.md`, `code/annas-archive-toolkit/docs/setup/HD_DOWNLOAD_PIPELINE.md`.

## Wichtige Dateien
- Worker **Inner Compass:** `code/inner_compass_app/apps/web/scripts/ic_worker.py`  
- Worker **Legacy HD-SaaS:** `code/hd_saas_app/apps/web/scripts/hd_worker_mvp.py` (nur noch falls alter Stack)  
- Ops: `infrastructure/spark/hd_worker_ops.md`  
- Pipeline-Plan: `infrastructure/spark/pdf_extraction_options.md`

