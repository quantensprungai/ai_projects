# text2kg – Implementierungsskizze (Worker)

<!--
last_update: 2026-02-10
status: draft
scope:
  summary: "Pseudo-Code, DB-Queries und Einbindung in hd_worker_mvp.py für den Job text2kg."
  in_scope:
    - Ablauf im Worker
    - Supabase-Queries (Interpretations, Term-Mapping, Upsert Nodes/Edges)
    - Idempotenz, Scope (asset/document)
  out_of_scope:
    - Konkrete Python-Syntax (nur Skizze)
notes:
  - "Spec: text2kg_spec.md. Worker-Code: code/hd_saas_app/apps/web/scripts/hd_worker_mvp.py"
-->

Diese Skizze beschreibt, **wo** und **wie** der Job `text2kg` im Worker eingebaut wird. Vollständige Spec: `text2kg_spec.md`.

**Wichtig:** text2kg ist **kein** eigener Worker-Prozess. Er wird **im bestehenden HD-Worker** (`hd_worker_mvp.py`) als weiterer Job-Typ implementiert – derselbe Prozess verarbeitet extract_text, extract_interpretations, text2kg usw. nacheinander. Es gibt keine separaten „anderen Worker“ für KG; alles läuft in einem Worker.

## 1) Einbindung in den Worker

- **Datei:** `code/hd_saas_app/apps/web/scripts/hd_worker_mvp.py` (derselbe HD-Worker wie für alle anderen Jobs).
- **Job-Typ:** `text2kg` in `_pick_next_job()` zur Liste der abgefragten `job_type` hinzufügen (neben extract_text, extract_text_ocr, classify_domain, extract_term_mapping, extract_interpretations).
- **Ablauf:** Wie bei anderen Jobs: `process_one_job()` → `job_type == "text2kg"` → eigener Block mit Input-Lesen, Node/Edge-Upserts, Job-Update auf completed/failed.

## 2) Job-Input (debug / Scope)

Aus `hd_ingestion_jobs.debug`:

- `account_id` (immer aus Job-Row)
- `asset_id` (optional): nur Interpretations zu diesem Asset
- `document_id` (optional): nur Interpretations zu Chunks dieses Dokuments
- Kein asset_id/document_id → Scope = alle Interpretationen des Accounts (mit Limit, z. B. 5000)

Interpretations filtern:

- Entweder über Join: Chunks haben `asset_id` → Interpretationen haben `chunk_id` → Chunks.asset_id = debug.asset_id.
- Oder: Interpretations laden und über zugehörige Chunk-Rows filtern (chunk_id IN (SELECT id FROM hd_asset_chunks WHERE asset_id = ?)).

## 3) DB-Queries (Skizze)

### 3.1 Interpretationen laden (pro Scope)

```text
Wenn asset_id gesetzt:
  1) Chunk-IDs holen: GET hd_asset_chunks?account_id=eq.X&asset_id=eq.Y&select=id
  2) Interpretationen: GET hd_interpretations?account_id=eq.X&chunk_id=in.(id1,id2,...)&select=*
Wenn document_id gesetzt:
  1) Asset-IDs zum Dokument (über hd_document_files / hd_assets) oder Chunks direkt per document_id (falls in metadata)
  2) Wie oben, Interpretationen zu diesen Chunks
Wenn weder asset_id noch document_id:
  GET hd_interpretations?account_id=eq.X&order=created_at.asc&limit=5000
```

### 3.2 Term-Mapping laden (canonical_id Lookup)

```text
GET hd_term_mapping?account_id=eq.X&select=canonical_id,system,term,language,school
Optional: In-Memory-Map (account_id, system, element_type, element_id) -> canonical_id
  element_id kann term oder normalisierte Form sein; Matching über term/synonyms.
Fallback node_key: "{system}.{element_type}.{element_id}"
```

### 3.3 Node Upsert

```text
Unique-Key: (account_id, node_key)
1) SELECT id FROM hd_kg_nodes WHERE account_id = ? AND node_key = ?
2) Wenn Row existiert:
   PATCH hd_kg_nodes?id=eq.{id}
     metadata = merge(existing.metadata, new_metadata)  # interpretation_ids append, dimensions/interactions overwrite
     canonical_description NICHT setzen (leer lassen)
3) Wenn nicht existiert:
   POST hd_kg_nodes
     account_id, node_key, node_type, canonical_description=NULL, metadata={...}
```

**metadata (Pflicht):**

- `interpretation_ids`: [uuid, ...]
- `chunk_ids`: [uuid, ...]
- `source`: aus payload.source
- `dimensions`: payload.dimensions (vollständig)
- `interactions`: payload.interactions (vollständig)

### 3.4 Edges (nur aus payload.relations; im ersten MVP optional)

Die **Kern-Pipeline** ist vollständig spezifiziert: Nodes immer, Edges aus expliziten Relationen sobald `payload.relations` genutzt wird.

- **Im ersten MVP** können wir **nur Nodes** anlegen und Edges aus `payload.relations` weglassen („MVP optional“ = Edges in Release 1 optional). Sobald das LLM oder ein späterer Schritt `payload.relations` liefert, gleiche Logik wie unten.
- **Playbook/ArangoDB-Export** ist ein **separater, optionaler** Weg (nur Visualisierung/GraphRAG); die Source of Truth bleibt Supabase.

```text
Falls payload.relations vorhanden (später oder ab Release):
  Für jede relation: type, target_canonical_id
    from_node_id = aktueller Node (gerade upserted)
    to_node_id = Lookup node per (account_id, target_canonical_id als node_key)
    relation_type = type (nur part_of, depends_on, amplifies, maps_to erlauben)
  INSERT hd_kg_edges nur wenn to_node existiert; Idempotenz: vorher prüfen ob (from, to, relation_type) schon existiert
Erster MVP ohne payload.relations: keine Edges anlegen (nur Nodes) – Pipeline bleibt vollständig spezifiziert.
```

## 4) Pseudo-Code (pro Job-Lauf)

```text
1. job = _pick_next_job()  # inkl. job_type "text2kg"
2. Wenn job_type != "text2kg": bestehende Branches
3. Wenn job_type == "text2kg":
   a. account_id = job["account_id"]
   b. debug = job.get("debug") or {}
   c. asset_id = debug.get("asset_id")
   d. document_id = debug.get("document_id")
   e. Interpretationen laden (siehe 3.1)
   f. Term-Mapping laden (optional: pro account; oder nur bei Bedarf pro Interpretation)
   g. Für jede Interpretation:
        node_key = lookup_canonical_id(interpretation) oder fallback(interpretation.system, element_type, element_id)
        node_type = normalize(interpretation.element_type)
        metadata = {
          interpretation_ids: [interpretation.id],
          chunk_ids: [interpretation.chunk_id],
          source: payload.source,
          dimensions: payload.dimensions,
          interactions: payload.interactions
        }
        upsert_node(account_id, node_key, node_type, canonical_description=None, metadata)
        # Optional: payload.relations -> upsert_edges (MVP: skip)
   h. _update_job(..., status="completed", finished_at=..., error=None, debug={...})
   i. return True, "job {id} completed: text2kg N nodes"
4. Fehlerbehandlung: try/except, _update_job(status="failed", error=...)
```

## 5) Idempotenz

- **Nodes:** Upsert per (account_id, node_key). Bei Update: metadata mergen (interpretation_ids anhängen, dimensions/interactions ersetzen), canonical_description unverändert.
- **Edges:** Nur einfügen wenn (from_node_id, to_node_id, relation_type) noch nicht existiert (SELECT vor INSERT oder ON CONFLICT falls Unique-Constraint ergänzt wird).

## 6) Wo der Worker läuft (Doku)

- **Entwicklung/Code:** `code/hd_saas_app/apps/web/scripts/hd_worker_mvp.py` (lokal bearbeiten, dann per SCP nach Spark).
- **Laufzeit:** Spark (`spark-56d0`), systemd-Service `hd-worker.service`, WorkingDir `~/srv/hd-worker`. MinerU und LLM laufen aus Ressourcengründen ggf. getrennt (schrittweiser Prozess); text2kg ist CPU/DB-lastig und kann in derselben Worker-Unit laufen, sobald Interpretations und Term-Mapping vorliegen.

**Testablauf und erwartete DB-Inhalte:** `text2kg_test_procedure.md` (Schritte lokal/Spark, Prüf-SQL, Option Term-Mapping für node_key).

Referenz: `projects/hd_saas/00_overview/current_status_local_dev.md`, `worker_contract_spark_supabase.md`.
