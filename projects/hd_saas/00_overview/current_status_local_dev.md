<!-- Reality Block
last_update: 2026-01-29
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
- Worker-MVP Script kann `extract_text` + `extract_interpretations` (Stub) verarbeiten → `hd_asset_chunks` + `hd_interpretations`

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
→ queued `extract_interpretations` → Worker → `hd_interpretations.payload` (Contract-Shape, aktuell Stub)

Details sind im Code-Repo dokumentiert:

- `code/hd_saas_app/docs/hd_ingestion_local_dev.md`

## Hinweis: Cloud vs Local

Wenn du „in der Cloud nicht die gleichen Tabellen“ siehst: Cloud hat vermutlich eure Migrationen noch nicht bekommen.
Cloud muss per `supabase db push` mit den Migrationen aus `code/hd_saas_app/apps/web/supabase/migrations/` vorbereitet werden.

## Status Snapshot (Cloud E2E MVP)

Stand: **2026-02-02**

- **Cloud Schema vorhanden** (HD Tabellen + RLS + Worker service_role policies).
- **VM102 → Cloud Upload** funktioniert:
  - `src/hd_saas_uploader.py` erzeugt `assets.jsonl` (aus `metadata.json`) und lädt PDFs aus `output/hd_content/downloads/fast_download/...` hoch.
  - Legt `hd_assets`, `hd_documents`, `hd_document_files`, `hd_ingestion_jobs` an.
- **Worker MVP läuft auf VM102 (Linux)** und verarbeitet Cloud Jobs end-to-end:
  - `extract_text` → `hd_asset_chunks`
  - anschließend automatisch `extract_interpretations` → `hd_interpretations` (Stub Payload, contract-shaped)

### Hinweis: Windows vs Linux Worker

- Windows hatte PyMuPDF `import fitz` Probleme (DLL load failed). Daher für Cloud-Worker aktuell: **VM102/Linux** bevorzugt.
- VM102 benötigt wegen PEP 668 ein **venv** für `pip`-Deps.

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

