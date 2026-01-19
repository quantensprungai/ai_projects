<!-- Reality Block
last_update: 2026-01-19
status: draft
scope:
  summary: "Contract zwischen Makerkit/Supabase (Control Plane) und Spark/DGX (Worker/Data Plane)."
  in_scope:
    - job types
    - input/output payloads
    - storage path conventions
  out_of_scope:
    - konkrete Spark Implementierung
notes: []
-->

# Worker Contract – Spark/DGX ↔ Supabase (HD‑SaaS)

## Zielbild

- **Supabase** ist die **Control Plane**: Auth/RLS, Storage, Tabellen, Job-Queue.
- **Spark/DGX Worker** ist die **Data Plane**: OCR/Whisper/LLM-Extraction/Text2KG/Synthesis im Batch.

Der Worker verarbeitet **Jobs** aus `public.hd_ingestion_jobs` und schreibt Ergebnisse in:
- `public.hd_assets`
- `public.hd_asset_chunks`
- `public.hd_interpretations`
- `public.hd_kg_nodes`, `public.hd_kg_edges`
- `public.hd_dynamics`
- `public.hd_syntheses`

## Storage Konvention (tenant-safe)

- Alle Objekte liegen unter:
  - `accounts/{account_id}/...`
- Bucket (aktuell):
  - `hd_uploads_raw` (Input/Contracts, PDFs, JSONL, etc.)

## Job-Tabelle (Source of Truth)

- **Tabelle**: `public.hd_ingestion_jobs`
- **Wichtige Felder**:
  - `account_id`: Tenant
  - `document_id`: Referenz auf `public.hd_documents`
  - `job_type`: Typ
  - `status`: `queued | running | completed | failed`
  - `attempts`, `error`
  - `debug` (jsonb): Payload / Pointer zu Storage + Parametern

## Job Types (MVP)

### 1) `import_assets_jsonl`

- **Input**:
  - `hd_ingestion_jobs.debug` enthält:
    - `bucket`: `hd_uploads_raw`
    - `path`: `accounts/{account_id}/assets-jsonl/{timestamp}-assets.jsonl`
    - `format`: `assets.jsonl`
- **Worker-Output**:
  - pro Asset eine Zeile in `public.hd_assets`
  - optional: Status/Statistik zurück in `hd_ingestion_jobs.debug`
- **Erwartetes `assets.jsonl`**:
  - 1 JSON-Objekt pro Zeile
  - minimale Felder (MVP): `title`, `source_type`, `source_ref`, `metadata`
  - Alles weitere kann in `metadata` landen (jsonb)

### 2) (später) `extract_text`

- **Input**:
  - `hd_document_files.bucket` + `storage_path` (PDF/Text)
- **Output**:
  - `public.hd_asset_chunks` (oder zunächst `public.hd_document_texts`)

### 3) (später) `extract_interpretations`

- **Input**:
  - Chunks (`hd_asset_chunks`)
- **Output**:
  - `public.hd_interpretations.payload` (jsonb: statements/rules/relations candidates)

### 4) (später) `text2kg`

- **Input**:
  - Interpretations/Chunks
- **Output**:
  - Upsert `public.hd_kg_nodes` + `public.hd_kg_edges`

### 5) (später) `synthesize_node`

- **Input**:
  - Node + zugehörige Interpretationen/Dynamics
- **Output**:
  - `public.hd_syntheses` + optional `hd_kg_nodes.canonical_description`

## Wichtige Regeln für den Worker

- **Immer tenant‑safe schreiben**:
  - Jede Row bekommt `account_id` aus dem Job/Path.
- **Idempotenz**:
  - Jobs dürfen wiederholbar sein (Retries): Upserts/Unique Constraints nutzen.
- **Statuspflege**:
  - `status` und `error` in `hd_ingestion_jobs` sauber setzen.
- **Service Role**:
  - Worker nutzt Service Role Key, damit er schreiben kann; trotzdem `account_id` strikt setzen.

