<!-- Reality Block
last_update: 2026-01-30
status: stable
scope:
  summary: "Weiterverarbeitung in HD-SaaS: Was passiert nach dem Upload von assets.jsonl? Worker-Pipeline, Status-Management, nächste Schritte."
  in_scope:
    - HD-SaaS ingestion workflow
    - worker pipeline (geplant vs. implementiert)
    - status management (queued/processed/failed)
    - topic/profile filtering for processing
  out_of_scope:
    - technical implementation details (siehe code/hd_saas_app/)
    - setup instructions (siehe projects/hd_saas/)
notes: []
-->

# Weiterverarbeitung in HD-SaaS

## Übersicht: Was passiert nach dem Upload?

Nach dem Upload von `assets.jsonl` zu HD-SaaS gibt es **zwei Phasen**:

1. **Phase 1: Ingestion (✅ implementiert)** - `assets.jsonl` → `hd_assets` Tabelle
2. **Phase 2: Processing (🚧 teilweise implementiert als MVP)** - PDF → Text → Chunks → Interpretations (Stub) → (später KG)

## Phase 1: Ingestion (assets.jsonl → hd_assets)

### Was passiert beim Upload?

**Upload-Prozess:**
1. **Upload** `assets.jsonl` via HD-SaaS UI (`/home/hd/ingestion`)
2. **Storage:** Datei wird in `hd_uploads_raw` Bucket gespeichert
3. **DB-Einträge:**
   - `hd_documents` (status: `pending`)
   - `hd_document_files` (kind: `assets_jsonl`)
   - `hd_ingestion_jobs` (job_type: `import_assets_jsonl`, status: `queued`)

**Job-Verarbeitung:**
- Dev Runner verarbeitet `import_assets_jsonl` Job
- Liest `assets.jsonl` aus Storage
- Schreibt jede Zeile als Asset in `hd_assets` Tabelle
- **Duplikat-Prävention:** Upsert basierend auf `(account_id, source_ref)`

**Ergebnis:**
- `hd_assets` Tabelle enthält alle Assets (metadata-only)
- Status: `queued` (bereit für Weiterverarbeitung)

### Code-Referenz

- **Upload Action:** `code/hd_saas_app/apps/web/app/home/_lib/hd-ingestion/actions.ts` → `uploadAssetsJsonlAndCreateImportJob`
- **Job Processing:** `code/hd_saas_app/apps/web/app/home/_lib/hd-ingestion/actions.ts` → `processNextQueuedAssetsJsonlImportJob`
- **Doku:** `code/hd_saas_app/docs/hd_ingestion_local_dev.md`

## Phase 2: Processing (PDF → Text → Chunks → KG)

### Geplante Worker-Pipeline

**Job-Typen (geplant, noch nicht implementiert):**

1. **`extract_text`** - PDF → Text
   - Input: PDF aus Storage (`hd_document_files`)
   - Output: `hd_asset_chunks` oder `hd_document_texts`
   - Steps: PDF Parsing, OCR (falls Scan), Cleaning

2. **`extract_interpretations`** - Text → Interpretations
   - Input: Chunks (`hd_asset_chunks`)
   - Output: `hd_interpretations` (statements/rules/relations candidates)
   - Steps: LLM-basierte Extraction

3. **`text2kg`** - Interpretations → Knowledge Graph
   - Input: Interpretations/Chunks
   - Output: `hd_kg_nodes`, `hd_kg_edges`
   - Steps: Entity/Relation Extraction, KG Upsert

4. **`classify_domain`** - Domain Classification
   - Input: Chunks
   - Output: Classification (`HD|BaZi|Astro|GeneKeys|Mixed|Other`)
   - Steps: LLM-basierte Classification
   - Speicherung: `hd_classifications` oder `metadata.classification`

5. **`synthesize_node`** - KG → Canonical Descriptions
   - Input: Node + zugehörige Interpretations/Dynamics
   - Output: `hd_syntheses`, `hd_kg_nodes.canonical_description`
   - Steps: LLM-basierte Canonicalization

### Status-Management

**Status-Felder in `hd_assets`:**
- `status`: `queued` | `processed` | `failed`
- Assets mit `status: 'queued'` werden vom Worker verarbeitet
- Nach erfolgreicher Verarbeitung: `status: 'processed'`

**Manuelle Steuerung:**

```sql
-- Alle Assets für Verarbeitung markieren
UPDATE hd_assets 
SET status = 'queued'
WHERE status != 'queued';

-- Nur bestimmte Topics verarbeiten
UPDATE hd_assets 
SET status = 'queued'
WHERE metadata->>'topic' = 'human design'
  AND status != 'queued';

-- Nur bestimmte Profile-IDs verarbeiten
UPDATE hd_assets 
SET status = 'queued'
WHERE metadata->>'profile_id' = 'hd_content'
  AND status != 'queued';
```

## Aktueller Stand

### ✅ Implementiert

- **Upload:** `assets.jsonl` hochladen
- **Ingestion:** `assets.jsonl` → `hd_assets` (metadata-only)
- **Duplikat-Prävention:** Unique Constraint auf `(account_id, source_ref)`

### ✅ Implementiert (MVP, lokal / Script)

- **PDF Upload → Job:** `extract_text` Jobs werden angelegt (UI/Action in `code/hd_saas_app`)
- **Worker MVP:** verarbeitet `extract_text` → `hd_asset_chunks`
- **Folgeschritt:** queued `extract_interpretations` → schreibt `hd_interpretations.payload` (Contract-Shape, aktuell Stub)

Siehe:
- `code/hd_saas_app/docs/hd_ingestion_local_dev.md`
- **Status-Management:** `status` Feld in `hd_assets`

### 🚧 Geplant (noch nicht implementiert)

- **PDF Processing:** PDF → Text (OCR/Extraction)
- **Chunking:** Text → Chunks
- **Classification:** Domain Classification (HD/BaZi/etc.)
- **Extraction:** Chunks → Interpretations
- **Knowledge Graph:** Interpretations → KG Nodes/Edges
- **Synthesis:** KG → Canonical Descriptions

### 📋 Worker Contract

**Dokumentation:**
- `projects/hd_saas/02_system_design/worker_contract_spark_supabase.md` - Worker Contract (Spark/DGX ↔ Supabase)
- `projects/hd_saas/02_system_design/data_flows.md` - Data Flows (Flow B, C, D)

**Job-Queue:**
- Tabelle: `hd_ingestion_jobs`
- Felder: `job_type`, `status`, `account_id`, `document_id`, `debug` (jsonb)

## Workflow: Assets für Weiterverarbeitung vorbereiten

### Schritt 1: assets.jsonl hochladen

**Via HD-SaaS UI:**
- Navigiere zu `/home/hd/ingestion` (Personal) oder `/home/<account>/hd/ingestion` (Team)
- Upload `assets.jsonl`
- Warte bis Job verarbeitet ist (`hd_ingestion_jobs.status: 'completed'`)

**Prüfen:**
```sql
-- Zeige Assets
SELECT id, title, source_ref, status, metadata->>'topic' as topic
FROM hd_assets
ORDER BY created_at DESC
LIMIT 10;
```

### Schritt 2: Assets für Verarbeitung markieren

**Option A: Alle Assets**
```sql
UPDATE hd_assets 
SET status = 'queued'
WHERE status != 'queued';
```

**Option B: Nur bestimmte Topics**
```sql
-- Nur Human Design Assets
UPDATE hd_assets 
SET status = 'queued'
WHERE metadata->>'topic' = 'human design'
  AND status != 'queued';

-- Oder: Nur BaZi Assets
UPDATE hd_assets 
SET status = 'queued'
WHERE metadata->>'topic' = 'bazi'
  AND status != 'queued';
```

**Option C: Nur bestimmte Profile-IDs**
```sql
UPDATE hd_assets 
SET status = 'queued'
WHERE metadata->>'profile_id' = 'hd_content'
  AND status != 'queued';
```

### Schritt 3: Worker verarbeitet (wenn implementiert)

**Automatisch:**
- Worker liest Assets mit `status: 'queued'`
- Verarbeitet PDF → Text → Chunks → Classification → KG
- Aktualisiert `status: 'processed'`

**Manuell (aktuell):**
- Worker-Pipeline ist noch nicht implementiert
- Assets bleiben in `status: 'queued'` bis Worker verfügbar ist

## Monitoring & Prüfung

### Assets-Status prüfen

```sql
-- Status-Verteilung
SELECT 
  status,
  COUNT(*) as count
FROM hd_assets
GROUP BY status;

-- Topic-Verteilung
SELECT 
  metadata->>'topic' as topic,
  COUNT(*) as count,
  COUNT(*) FILTER (WHERE status = 'queued') as queued,
  COUNT(*) FILTER (WHERE status = 'processed') as processed
FROM hd_assets
GROUP BY metadata->>'topic';

-- Profile-ID-Verteilung
SELECT 
  metadata->>'profile_id' as profile_id,
  COUNT(*) as count,
  COUNT(*) FILTER (WHERE status = 'queued') as queued
FROM hd_assets
GROUP BY metadata->>'profile_id';
```

### Jobs prüfen

```sql
-- Aktuelle Jobs
SELECT 
  job_type,
  status,
  COUNT(*) as count
FROM hd_ingestion_jobs
GROUP BY job_type, status;

-- Fehlgeschlagene Jobs
SELECT 
  id,
  job_type,
  status,
  error,
  attempts
FROM hd_ingestion_jobs
WHERE status = 'failed'
ORDER BY created_at DESC;
```

## Nächste Schritte (für Entwicklung)

### 1. Worker-Pipeline implementieren

**Priorität:**
1. **`extract_text`** - PDF → Text (Grundlage für alles weitere)
2. **`classify_domain`** - Domain Classification (für Topic-Filterung)
3. **`extract_interpretations`** - Text → Interpretations
4. **`text2kg`** - Interpretations → KG

**Referenz:**
- `projects/hd_saas/02_system_design/worker_contract_spark_supabase.md`
- `projects/hd_saas/02_system_design/data_flows.md`

### 2. PDF-Upload ermöglichen

**Aktuell:** Nur `assets.jsonl` (metadata-only)
**Geplant:** PDF-Upload für Assets mit `source_ref` (MD5)

**Workflow:**
- Upload PDF zu Storage
- Verknüpfe mit Asset via `source_ref` (MD5)
- Erstelle `extract_text` Job

### 3. Topic/Profile-Filterung im Worker

**Worker sollte:**
- Assets nach `metadata->>'topic'` filtern können
- Assets nach `metadata->>'profile_id'` filtern können
- Nur bestimmte Topics verarbeiten (konfigurierbar)

## Zusammenfassung

### ✅ Was funktioniert jetzt:

- **Upload:** `assets.jsonl` hochladen
- **Ingestion:** `assets.jsonl` → `hd_assets` (metadata-only)
- **Duplikat-Prävention:** Automatisch via Unique Constraint
- **Status-Management:** Assets können auf `queued` gesetzt werden

### 🚧 Was noch kommt:

- **PDF Processing:** PDF → Text (OCR/Extraction)
- **Chunking:** Text → Chunks
- **Classification:** Domain Classification
- **Extraction:** Chunks → Interpretations
- **Knowledge Graph:** Interpretations → KG Nodes/Edges
- **Synthesis:** KG → Canonical Descriptions

### 📝 Aktueller Workflow:

1. **Upload** `assets.jsonl` → `hd_assets` (status: `queued`)
2. **Manuell:** Assets für Verarbeitung markieren (SQL)
3. **Warten:** Auf Worker-Implementierung
4. **Zukünftig:** Worker verarbeitet automatisch

## Links

- **HD-SaaS Doku:** `projects/hd_saas/`
- **Worker Contract:** `projects/hd_saas/02_system_design/worker_contract_spark_supabase.md`
- **Data Flows:** `projects/hd_saas/02_system_design/data_flows.md`
- **Local Dev:** `code/hd_saas_app/docs/hd_ingestion_local_dev.md`
- **Kompletter Workflow:** `complete_workflow.md`
