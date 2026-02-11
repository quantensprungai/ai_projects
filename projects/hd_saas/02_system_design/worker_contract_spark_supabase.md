<!-- Reality Block
last_update: 2026-02-10
status: draft
scope:
  summary: "Contract zwischen Makerkit/Supabase (Control Plane) und Spark/DGX (Worker/Data Plane)."
  in_scope:
    - job types
    - input/output payloads
    - storage path conventions
    - Worker-Laufort, schrittweiser Ablauf
  out_of_scope:
    - konkrete Spark Implementierung
notes:
  - "text2kg: Spec text2kg_spec.md, Implementierungsskizze text2kg_implementation_sketch.md, Export-Entwurf export_supabase_to_arangodb.md"
-->

# Worker Contract – Spark/DGX ↔ Supabase (HD‑SaaS)

## Zielbild

- **Supabase** ist die **Control Plane**: Auth/RLS, Storage, Tabellen, Job-Queue.
- **Ein einziger HD-Worker** (Spark/DGX) ist die **Data Plane**: ein Prozess (`hd_worker_mvp.py`), der alle Job-Typen nacheinander verarbeitet – extract_text, extract_interpretations, text2kg, synthesize_node usw. Es gibt **keine** separaten Worker-Prozesse pro Job-Typ.

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

**Wichtig (Reality Check):**
- `metadata` muss **JSON-serialisierbar** bleiben. Keine “ganzen Objekte” (z. B. komplette Parsed-Payload) in `metadata` ablegen.
- Praktisch: wenn du “Originalzeile” speichern willst, dann nur als **kleines Subset** (`id`, `title`, `source_type`, `source_ref`, …), sonst drohen Fehler wie `Circular reference detected`.

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

### 4) `text2kg` (Spec + Skizze vorhanden, Job noch nicht im Worker)

- **Input**: Interpretations (`hd_interpretations`) + Term-Mapping (`hd_term_mapping`); Scope optional per `debug.asset_id` / `debug.document_id`.
- **Output**: Upsert `public.hd_kg_nodes` + `public.hd_kg_edges` (nur strukturelle Edges; dimensions/interactions in node.metadata).
- **Doku**: Spec `text2kg_spec.md`; Implementierungsskizze (Pseudo-Code, DB-Queries, Einbindung in `hd_worker_mvp.py`) `text2kg_implementation_sketch.md`; optionaler Export Supabase → ArangoDB `export_supabase_to_arangodb.md`.

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

## Worker-Laufort und Ablauf (Spark)

- **Laufzeit:** Spark (`spark-56d0`), systemd `hd-worker.service`, WorkingDir `~/srv/hd-worker`. Code-Basis: `code/hd_saas_app/apps/web/scripts/hd_worker_mvp.py` (lokal bearbeiten, Deployment z. B. per SCP).
- **Schrittweiser Prozess:** MinerU und LLM können aus Ressourcengründen getrennt laufen; die Pipeline ist ohnehin sequentiell (extract_text → … → extract_interpretations → text2kg → …), sodass ein stückweiser Ablauf vorgesehen ist.

## Ops/Debug (Pragmatik)

Siehe auch: `infrastructure/spark/hd_worker_ops.md`
