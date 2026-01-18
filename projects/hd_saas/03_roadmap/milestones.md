<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "Meilensteine für HD-SaaS."
  in_scope:
    - milestones
    - deliverables
  out_of_scope:
    - detailed task breakdown
notes: []
-->

# Milestones – HD‑SaaS

## M0 – Bootstrap & Verständnis (done)

- Makerkit Repo geklont, `origin` + `upstream` gesetzt
- Dependencies installiert
- Interne Orientierung dokumentiert (`makerkit_bootstrap_and_orientation.md`)

## M1 – HD‑Ingestion Slice: Datenmodell + Storage (MVP‑Grundlage)

- Storage Buckets angelegt:
  - `hd_uploads_raw`
  - `hd_transcripts_raw`
- Tabellen + RLS (MVP):
  - `hd_documents`
  - `hd_document_files`
  - `hd_ingestion_jobs`
  - optional `hd_document_texts`

## M2 – Minimal UI: Upload + Status + Anzeige

- Upload pro Account (Team/Personal)
- Dokumentliste mit Status
- Anzeige “Extracted Text” (read‑only)

## M3 – Job Runner (MVP)

- Worker/Script, der `queued` Jobs verarbeitet und Status/Errors schreibt
- Minimal: PDF→Text (ohne OCR) + Transcript‑Copy

## M4 – Erweiterungen (nach MVP)

- Chunking‑Job + `chunks` Tabelle
- Extraction (Entities/Relations) → KG
- Synthesis (canonical texts)
- RAG/Embeddings



