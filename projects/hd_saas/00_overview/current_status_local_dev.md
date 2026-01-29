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

Details sind im Code-Repo dokumentiert:

- `code/hd_saas_app/docs/hd_ingestion_local_dev.md`

