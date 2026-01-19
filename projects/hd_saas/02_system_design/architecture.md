<!-- Reality Block
last_update: 2026-01-16
status: draft
scope:
  summary: "Systemarchitektur für HD-SaaS (KG + Dynamics + Context/Temporal + Pipeline)."
  in_scope:
    - components
    - boundaries
    - interfaces
  out_of_scope:
    - low-level implementation
notes: []
-->

# Architecture – HD‑SaaS

## Überblick

HD‑SaaS besteht aus drei Ebenen:
- **Data Layer (Supabase/Postgres)**: Assets, Chunks, Interpretationen, KG (Nodes/Edges), Dynamics, Context/Temporal.
- **Pipeline Layer (Batch/Jobs)**: OCR/Whisper → Cleaning → Classification → Extraction → KG Update → Synthesis.
- **App Layer (Makerkit/Next.js)**: UI + Auth + Admin/Curate + Chat/Query.

Siehe auch: `projects/hd_saas/02_system_design/worker_contract_spark_supabase.md` (konkreter Contract Spark/DGX ↔ Supabase).

## Kernkomponenten

### 1) Storage & DB (Supabase)

- **Storage**: Uploads (PDF/Audio/Video/Transkripte).
- **DB** (Postgres/JSONB):
  - Assets (Ingest‑Contract z. B. `assets.jsonl`)
  - Chunks (cleaned text chunks)
  - Interpretations (Quelle → Aussagen/Statements)
  - KG Nodes/Edges (qualitative Relationen)
  - Dynamics Objects (Phasen/Fallen/Wege)
  - Context/Temporal (User‑Kontext + Zyklen)

### 2) Ingest Contracts

- **Metadata‑Contract**: `assets.jsonl` (aus Anna’s Archive Toolkit).  
  Zweck: **Katalog/Selektionsbasis** (metadata‑only möglich).
- **Content‑Contract**: “Dokument + Quelle + Rechte” (PDF/Text/Transcript) für OCR/Whisper/Parsing.

### 3) Extraction / Graph Builder

Pipeline‑Steps (LLM‑gestützt):
- Cleaning & Chunking
- Domain Classification (HD/BaZi/Astro …)
- Extraction (Entities/Relations/Rules/Dynamics‑Kandidaten)
- KG Updater (upsert Nodes/Edges)
- Dynamics Builder (Dynamic Objects)

### 4) Synthesis Engine

Ziel: **kanonische** Texte/Regeln aus vielen Quellen erzeugen (versioniert):
- canonical_description pro Node
- ggf. “canonical dynamics” pro Dynamic Object

### 5) Query / Chat Layer

LLM ist **Interface**:
- holt relevante KG‑Daten + Interpretationen + Dynamics + Kontext/Temporal
- antwortet **mit Referenzen** (Asset/Chunk IDs)

## Abgrenzung zu Anna’s Archive Toolkit

`annas-archive-toolkit` ist **Upstream** und liefert:
- Topics/Profiles
- Metadaten‑Collection (`metadata.json/csv`)
- optionaler Export `assets.jsonl`

HD‑SaaS verarbeitet:
- `assets.jsonl` (Katalog)
- plus Inhalte (Text/PDF/Audio/Transkripte) für die eigentliche KG/Dynamics Extraktion


