<!-- Reality Block
last_update: 2026-01-18
status: draft
scope:
  summary: "Konkrete Definition des HD-Ingestion Slice (MVP): Buckets + Tabellen + Statusmodell + minimaler Ablauf."
  in_scope:
    - buckets
    - tables (logical schema)
    - job lifecycle
  out_of_scope:
    - full SQL migrations
    - UI implementation details
notes: []
-->

# HD‑Ingestion Slice – Spec (MVP)

## Ziel

Ein minimaler, operabler Pfad:

- Upload (PDF/Transkript) **pro Makerkit Account (`public.accounts`)**
- Persistenz in Supabase Storage + DB
- Erstellung eines Jobs (Extraction)
- Speichern des extrahierten Textes (als Grundlage für Chunking/Extraction/KG)

**Actor (wichtig):** In v0 ist das ein **interner Curator/Admin‑Workflow** zum Aufbau des HD‑Korpus (Schulen/Quellen).  
End‑User laden in v0 keine eigenen PDFs hoch – sie nutzen später das abgeleitete System (Readings/Chat).

## Storage Buckets (Vorschlag)

- **`hd_uploads_raw`**: Original‑PDFs
- **`hd_transcripts_raw`**: Original‑Transkripte (z.B. `.txt`, `.md`, `.json`)

**Key‑Schema (Pfadkonvention, tenant‑fähig)**:

- `accounts/{account_id}/documents/{document_id}/original.pdf`
- `accounts/{account_id}/documents/{document_id}/transcript.txt`
- optional: `accounts/{account_id}/documents/{document_id}/derived/extracted.txt`

## Tabellen (logisches Modell)

### `hd_documents`

- `id uuid pk`
- `account_id uuid not null` → FK `public.accounts(id)`
- `title text not null`
- `source_type text` (z.B. `upload|import|manual`)
- `status text` (z.B. `pending|processing|ready|failed`)
- `created_by uuid` → FK `auth.users(id)`
- `created_at timestamptz`
- `updated_at timestamptz`
- `metadata jsonb` (frei: z.B. Sprache, Tags, Herkunft, Lizenznotiz)

### `hd_document_files`

- `id uuid pk`
- `document_id uuid not null` → FK `hd_documents(id)`
- `account_id uuid not null` (denormalisiert für RLS‑Policy‑Einfachheit)
- `kind text` (`pdf|transcript|audio|other`)
- `bucket text not null`
- `storage_path text not null`
- `mime_type text null`
- `bytes bigint null`
- `content_hash text null` (z.B. sha256)
- `created_at timestamptz`

### `hd_ingestion_jobs`

- `id uuid pk`
- `account_id uuid not null`
- `document_id uuid not null`
- `job_type text not null` (`extract_text|ocr|whisper|chunk`)
- `status text not null` (`queued|running|succeeded|failed|cancelled`)
- `attempts int not null default 0`
- `error text null`
- `created_at timestamptz`
- `started_at timestamptz null`
- `finished_at timestamptz null`
- `debug jsonb` (frei: runtime infos, versions, checkpoints)

### optional `hd_document_texts` (MVP‑freundlich)

- `id uuid pk`
- `account_id uuid not null`
- `document_id uuid not null`
- `source_job_id uuid null` → FK `hd_ingestion_jobs(id)`
- `text text not null`
- `created_at timestamptz`
- `metadata jsonb` (z.B. Sprache, Parser, page_map)

## RLS (Prinzip)

Alle Tabellen sind **account‑scoped**:

- `account_id` muss via Makerkit Membership/Owner‑Checks zum User passen (**personal‑first, team‑ready**):
  - Personal Account: `public.accounts.primary_owner_user_id = auth.uid()`
  - Team Account: `public.has_role_on_account(account_id)` (Membership)
- Keine Queries ohne `account_id`‑Kontext (UI ist ohnehin in `(user)` oder `[account]` Kontext).

## Minimaler Ablauf (Happy Path)

1. User ist im Team‑Workspace (`[account]`) oder Personal Workspace.
2. Upload → `hd_documents` + `hd_document_files` werden erstellt.
3. Ein `hd_ingestion_jobs` (`job_type=extract_text`, `status=queued`) wird erzeugt.
4. Worker arbeitet Job ab und schreibt `hd_document_texts.text`.
5. `hd_documents.status` wird auf `ready` gesetzt.

Hinweis: “User” = der authentifizierte Actor in Makerkit (für v0 typischerweise du/Curator).

## Nicht‑Ziele (MVP)

- Noch kein KG/Nodes/Edges, keine Embeddings.
- Chunking kann als “Job‑Type” vorgesehen sein, aber muss nicht in MVP.

