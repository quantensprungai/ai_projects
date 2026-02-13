<!-- Reality Block
last_update: 2026-02-12
status: stable
scope:
  summary: "Aktueller Stand: Makerkit lokal (Supabase) + HD ingestion slice (assets.jsonl) end-to-end bis hd_assets."
  in_scope:
    - what is working locally
    - where the code lives
    - how to reproduce quickly
  out_of_scope:
    - production deployment
    - Spark/DGX worker (cloud)
    - secrets
notes: []
-->

# Aktueller Stand (Local Dev) – HD-SaaS / Makerkit

## TL;DR

Wir können lokal:

- einloggen
- im HD-Ingestion Screen `assets.jsonl` hochladen (Storage + DB Rows)
- queued `import_assets_jsonl` Jobs verarbeiten (dev runner) → `hd_assets` wird gefüllt

Zusätzlich (neu):
- PDFs hochladen → `extract_text` Job wird angelegt
- Worker-MVP Script kann `extract_text` + `extract_interpretations` (LLM oder Stub) verarbeiten → `hd_asset_chunks` + `hd_interpretations`

## Wo ist der Code?

- Code-Repo: `code/hd_saas_app/` (**eigenes Git-Repo**, nicht Teil des Root-Repos)
- Doku (dieses Repo): `projects/hd_saas/`

## Repro in 3 Minuten

1. In `code/hd_saas_app/apps/web` Supabase lokal starten: `pnpm supabase:start`
2. Next dev starten mit **expliziten** Supabase-ENV Overrides (URL + beide Keys)
3. In `/home/hd/ingestion` (oder `/home/<account>/hd/ingestion`) `assets.jsonl` hochladen
4. Button **„Queued Import-Job verarbeiten (dev)”** klicken → `hd_assets` wird gefüllt

## Implementierte Kette (MVP-Sicht)

Upload → `hd_documents` + `hd_document_files` + `hd_ingestion_jobs(job_type=import_assets_jsonl)` → dev runner → `hd_assets`

Zusätzlich (Worker-MVP):

PDF Upload → `hd_documents` + `hd_document_files` + `hd_ingestion_jobs(job_type=extract_text)` → Worker → `hd_asset_chunks`
→ queued `extract_interpretations` → Worker → `hd_interpretations.payload` (Contract-Shape; bei HD_LLM_EXTRACTION_URL echte LLM-Extraktion, sonst Stub)

Details sind im Code-Repo dokumentiert:

- `code/hd_saas_app/docs/hd_ingestion_local_dev.md`

## Hinweis: Cloud vs Local

Wenn du „in der Cloud nicht die gleichen Tabellen“ siehst: Cloud hat vermutlich eure Migrationen noch nicht bekommen.
Cloud muss per `supabase db push` mit den Migrationen aus `code/hd_saas_app/apps/web/supabase/migrations/` vorbereitet werden.

**Verbindliche Guardrails (bitte lesen, spart Zeit):**
- `projects/hd_saas/00_overview/local_vs_cloud_guardrails.md`

## Status Snapshot (Cloud E2E MVP)

Stand: **2026-02-10**

- **Cloud Schema vorhanden** (HD Tabellen + RLS + Worker service_role policies).
- **App (Cloud):** PDF-Direkt-Upload in Storage, Server Action legt nur Metadaten + `extract_text`-Job an (kein Body-Limit). classify_domain + system-aware `extract_interpretations` (LLM bei HD_LLM_EXTRACTION_URL, sonst Stub).
- **Worker auf Spark (spark-56d0):** systemd-Service in `~/srv/hd-worker`, MinerU + LLM-Extraktion (SGLang/Qwen 32B auf Port 30001). Verarbeitet extract_text, extract_text_ocr, classify_domain, extract_term_mapping, extract_interpretations, **text2kg**. Worker-Signatur (`worker_host`, `worker_pid`) wird im Job-`debug` geschrieben.

### payload.source vs. System (2026-02-10)

- **payload.source** = Herkunft der Extraktion: `llm_extraction` (vom LLM) oder `mvp_stub` (Stub). Wird vom Worker gesetzt; bei LLM-Aufruf immer `llm_extraction`, damit erkennbar ist, ob die Extraktion „echt“ war.
- **System** (hd, bazi, …) steht in der Spalte `hd_interpretations.system`, nicht in payload.source. Doku: `02_system_design/interpretations_contract.md`, `02_system_design/worker_contract_extract_interpretations.md`.

### LLM-Extraktion und text2kg (2026-02-09 / 2026-02-10)

- **extract_interpretations** mit **HD_LLM_EXTRACTION_URL** (SGLang auf Spark) erfolgreich getestet. Payload enthält essence, mechanics, dimensions, interactions, evidence; `source: "llm_extraction"` (seit 2026-02-10 fest vom Worker gesetzt).
- **text2kg** auf Spark durchgespielt (24 Nodes für ein BaZi-Asset). text2kg nutzt **Term-Mapping-Lookup** für node_key (canonical_id bei Treffer, sonst Fallback system.element_type.element_id).

### Nächste Schritte (Reihenfolge)

1. ~~**Worker als systemd-Service**~~ (erledigt)
2. ~~**OCR (extract_text_ocr)**~~ (erledigt)
3. ~~**Worker auf Spark / MinerU**~~ (erledigt)
4. ~~**LLM-Extraktion**~~ (erledigt; Env: `HD_LLM_EXTRACTION_URL`, `HD_LLM_EXTRACTION_LANG`, optional MODEL/API_KEY)
5. ~~**text2kg**~~ (erledigt): Im Worker implementiert, Term-Mapping-Lookup für node_key, auf Spark getestet. Spec/Test: `02_system_design/text2kg_spec.md`, `text2kg_test_procedure.md`. Optionaler Export: `export_supabase_to_arangodb.md`.

### Worker-Laufort und schrittweiser Prozess (Spark)

- **Laufzeit:** Spark (`spark-56d0`), systemd-Service `hd-worker.service`, WorkingDir `~/srv/hd-worker`. Gleiche Umgebung wie für Produktion; MinerU + LLM laufen dort stabil.
- **Ressourcen:** MinerU und LLM werden aus Lastgründen ggf. getrennt betrieben (z. B. nacheinander); der Ablauf ist ohnehin schrittweise (extract_text → extract_interpretations → text2kg → …), sodass das gut handhabbar ist.
- **Entwicklung:** Worker-Code liegt in `code/hd_saas_app/apps/web/scripts/hd_worker_mvp.py`; Änderungen lokal vornehmen, dann z. B. per SCP nach Spark deployen.

**Stand pushen:** Nach größeren Schritten (z. B. text2kg, source-Fix, Term-Mapping) empfiehlt sich Commit + Push des Repos (ai_projects und ggf. code/hd_saas_app), damit Spark und andere den gleichen Stand ziehen können.

### Zwei-Phasen-Betrieb (Phase 1 ohne LLM, 2026-02-12)

- **Phase 1 (VM102, kein LLM):** `HD_WORKER_JOB_TYPES=extract_text,extract_text_ocr` in hd-worker.service → Worker verarbeitet nur Textextraktion, keine Stub-Interpretations. MinerU auf VM102: nicht (PyMuPDF); MinerU auf Spark.
- **Phase 2 (mit LLM):** `HD_WORKER_JOB_TYPES` entfernen → Worker verarbeitet alle Jobs inkl. extract_interpretations (LLM-Extraktion).
- **Stub-Cleanup:** `docs/sql_hd_delete_stub_interpretations.sql` – löscht Interpretationen mit `payload.source = 'mvp_stub'`.

### Datenstand (2026-02-12)

- **681** hd_assets (Metadaten aus assets.jsonl)
- **111** PDFs hochgeladen (VM102 fast_download)
- **Interpretations:** system = hd/bazi/…/mixed/other (classify_domain); viele mixed/other wegen Keyword-Heuristik oder mehrsprachigen Texten
- **Titel-Backfill:** `backfill_asset_titles.py` nutzt assets.jsonl; MD5-Dateinamen sind kompatibel (source_ref = Content-MD5)

### Hinweis: Windows vs Linux Worker

- Windows hatte PyMuPDF `import fitz` Probleme (DLL load failed). Daher für Cloud-Worker aktuell: **VM102/Linux** bevorzugt.
- VM102 benötigt wegen PEP 668 ein **venv** für `pip`-Deps.

## Cloud-Status: aktuelles Problem (2026-02-09)

**Symptom:** Cloud-`extract_text` endet mit `routed_to: "extract_text_ocr"` und `extracted_text_len: 0`, aber im `debug` fehlen `mineru_fallback` und `mineru_fallback_detail`, obwohl der Code diese Keys beim OCR-Route-Update mitschicken sollte.

**Beobachtet:**
- Run 28 abgeschlossen (Cloud), `debug` enthält nur Basisschlüssel + `routed_to`, kein `mineru_fallback`.
- Spark-Worker ist aktuell deployt, läuft unter systemd.
- `--once`-Lauf via `systemd-run` zeigte zuletzt "no queued jobs" (Race mit Loop-Worker möglich).

**Hypothesen:**
- Der Loop-Worker verarbeitet den Job schneller als `--once` (Race), deshalb fehlen Logzeilen im `systemd-run`-Output.
- MinerU liefert keinen `.md`-Output, OCR-Fallback läuft – aber Log-Ausgaben fehlen, was ein Logging-/Payload-Problem nahelegt.

**Nächster Schritt (sauberer Single-Run-Test):**
1. Loop-Worker stoppen: `sudo systemctl stop hd-worker.service`
2. Job auf `queued` setzen (error kann bleiben)
3. Einmallauf: `sudo systemd-run --pipe --wait -p User=sparkuser -p WorkingDirectory=/home/sparkuser/srv/hd-worker -p EnvironmentFile=/home/sparkuser/srv/hd-worker/.env /home/sparkuser/srv/hd-worker/.venv/bin/python3 /home/sparkuser/srv/hd-worker/hd_worker_mvp.py --once`
4. Loop-Worker starten: `sudo systemctl start hd-worker.service`

**Ziel:** Im Einmallauf muss mindestens eine der Zeilen erscheinen:
- `[extract_text] routing to OCR: ...`
- `[extract_text] update payload has mineru_fallback=...`

**Interpretation:**
- Wenn die Zeilen erscheinen, aber `mineru_fallback` fehlt in der DB → DB/Truncation/Update-Payload prüfen.
- Wenn die Zeilen nicht erscheinen, obwohl der Job verarbeitet wurde → falscher Codepfad/Logging oder nicht derselbe Prozess.

### Ergebnis & Fix (2026-02-09)

- Root Cause: Jobs liefen korrekt (Chunks geschrieben), aber `debug` blieb aus früheren OCR-Runs „verschmutzt“ (`routed_to`, `scan_detected`, `extracted_text_len: 0`).
- Fix im Worker: Beim erfolgreichen `extract_text`-Lauf werden OCR-Marker aus `debug` entfernt und `extracted_text_len` neu gesetzt. Zusätzlich wird `worker_host`/`worker_pid` geschrieben, um den ausführenden Host eindeutig zu erkennen.

### Empfohlene Flag-Policy (Cloud/Spark)

- **Normalbetrieb (stabil):**
  - `HD_USE_MINERU=true`
  - **kein** `HD_DISABLE_OCR_FALLBACK`
  - **kein** `HD_MINERU_NO_FALLBACK`
- **Fehleranalyse (kurzzeitig):**
  - `HD_DISABLE_OCR_FALLBACK=true` → OCR-Route blockiert, Job muss fehlschlagen (Signal „MinerU/Scan-Route“).
  - `HD_MINERU_NO_FALLBACK=true` → PyMuPDF-Fallback aus, MinerU-Fehler wird sichtbar.
  - Danach Flags wieder entfernen, um Pipeline robust zu halten.

**Warum Fallback behalten?** Für große PDF-Batches ist ein sauberer Durchlauf wichtiger als harte Abbrüche. Fallbacks verhindern, dass einzelne PDFs den Batch blockieren. Für Ursachenanalyse nutzt man die Debug-Flags gezielt für kurze Zeitfenster.

### OCR & Spark/Blackwell (Plan vs. MVP)

- **Plan (Docs):** Worker Contract und `layers_overview.md` sehen die **Data Plane (OCR/Whisper/LLM)** auf **Spark/DGX**. OCR ist dort explizit vorgesehen; für Scan-PDFs: „Marker oder OCRmyPDF/Tesseract“, Gate „text vs. scan“.
- **Blackwell:** AI-GPU-Mikroarchitektur (Tensor Cores, LLM-optimiert). **OCR auf Spark:** direkt **GPU-OCR (EasyOCR)** – kein Tesseract-Umweg; EasyOCR nutzt CUDA automatisch. LLM-Extraktion (extract_interpretations) bleibt Hauptkandidat für Blackwell.
- **MinerU integriert:** Bei `HD_USE_MINERU=true` nutzt der Worker für `extract_text` (PDF) **MinerU** (strukturiertes Markdown, Hybrid Text+OCR). Auf Spark: MinerU im venv installieren (`pip install "mineru[core]"` oder `mineru[all]`), `HD_USE_MINERU=true` in `.env`. Details: `infrastructure/spark/pdf_extraction_options.md`.

### Security Reminder

- Service Role Keys wurden zwischendurch in Terminal-Ausgaben sichtbar. Bitte Keys rotieren und künftig aus einem lokalen env-file laden (nicht in Logs tippen).

## Cloud Setup Snippet (Minimal)

Ziel: Cloud so vorbereiten, dass VM102 Uploads/JOBS anlegen kann und Spark/DGX Worker sie sieht.

### 1) Cloud DB Schema deployen (Supabase CLI)

In `code/hd_saas_app/apps/web`:

```bash
# 1) Projekt ref setzen (Beispiel: wyyeepxcmwmjzxdsknve)
export SUPABASE_PROJECT_REF="wyyeepxcmwmjzxdsknve"

# 2) Link + Push
supabase link --project-ref "$SUPABASE_PROJECT_REF"
supabase db push
```

Danach sollten die Tabellen wie lokal existieren (u.a. `hd_assets`, `hd_ingestion_jobs`, `hd_asset_chunks`, `hd_interpretations`, ...).

### 2) „Einmal gegen Cloud einloggen/Signup“ – wie?

Du musst die Web-App einmal gegen Cloud konfigurieren (statt local `127.0.0.1:54321`):
- setze `NEXT_PUBLIC_SUPABASE_URL` auf deine Cloud Supabase URL
- setze `NEXT_PUBLIC_SUPABASE_PUBLIC_KEY` (und zur Sicherheit auch `NEXT_PUBLIC_SUPABASE_ANON_KEY`) auf den Cloud Publishable/Anon Key
- starte dann `pnpm dev` und gehe durch den normalen Signup/Login

Ergebnis: Makerkit legt (je nach Flow) eine Row in `public.accounts` an.

### 3) `HD_ACCOUNT_ID` finden (wichtig)

`HD_ACCOUNT_ID` ist **public.accounts.id** (UUID), nicht der Project Ref.

Du findest ihn:
- in Supabase Studio (Cloud) → Table Editor → `public.accounts`
- oder (Personal Account) oft identisch mit `auth.users.id` des Users

