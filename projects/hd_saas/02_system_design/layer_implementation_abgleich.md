# Abgleich: Layer-Modell & JSON-Blueprints ↔ Implementierung

<!--
last_update: 2026-02-10
status: draft
scope:
  summary: "Prüfliste: Ist alles, was in layer_model_and_schemas.md und layers_overview.md vorgesehen ist, in DB/Worker/Contracts berücksichtigt?"
  in_scope:
    - L1–L5 + L4 Edges: Vorgabe vs. Tabelle/Job/Contract
    - L6–L11: nur Stichwort (geplant/nicht implementiert)
  out_of_scope:
    - L12+ optionale Erweiterungen
notes:
  - "Autoritativ für Schemas: layer_model_and_schemas.md. Für Flows/Jobs: layers_overview.md. Für Payload: interpretations_contract.md. Für KG: text2kg_spec.md."
-->

Dieses Dokument bestätigt, dass die **Layer- und JSON-Vorgaben** aus `layer_model_and_schemas.md` und `layers_overview.md` in der **Implementierung und in den Contracts** berücksichtigt sind. Abweichungen sind explizit genannt.

---

## L1 Ingestion (File/Source Registry)

| Vorgabe (Blueprint) | Umgesetzt in | Status |
|---------------------|--------------|--------|
| ingest_id, source_type, file_type, storage_path, status, metadata | `public.hd_assets` (id, source_type, source_ref, status, metadata); `hd_document_files` (bucket, storage_path) | ✅ Tabellen und Konvention wie vorgesehen; Feldnamen teilweise anders (z. B. source_ref statt source_url), Semantik gleich. |
| tenant-safe paths | Bucket `hd_uploads_raw`, Paths `accounts/{account_id}/...` | ✅ Siehe worker_contract_spark_supabase.md, layers_overview Flow A. |

---

## L2 Cleaning/Chunking

| Vorgabe (Blueprint) | Umgesetzt in | Status |
|---------------------|--------------|--------|
| chunks[].chunk_id, text_clean, token_count, metadata | `public.hd_asset_chunks` (id, text_clean, token_count, metadata, chunk_index, asset_id) | ✅ Job `extract_text` (inkl. MinerU/OCR) füllt Chunks; Struktur entspricht Blueprint. |
| clean_id / ingest_id | Verknüpfung über `hd_asset_chunks.asset_id` → `hd_assets.id` | ✅ |

---

## L3 Domain Classification

| Vorgabe (Blueprint) | Umgesetzt in | Status |
|---------------------|--------------|--------|
| system, probability, subdomain, element_id, tags | Job `classify_domain`; Ergebnis in **asset.metadata** (system_id, ggf. confidence) und **job.debug** (system_id); kein separates „classification“-Table | ✅ Klassifikation läuft; Speicherort bewusst in Asset-Metadaten + Pipeline (nächste Jobs nutzen system_id). Blueprint „classification_id“ = logisch durch (asset_id, job) abgebildet. |

---

## L5 Interpretation Repository (Quellen‑Aussagen)

| Vorgabe (Blueprint) | Umgesetzt in | Status |
|---------------------|--------------|--------|
| system, element_type, element_id | Spalten `hd_interpretations.system`, `.element_type`, `.element_id` | ✅ |
| payload (essence, mechanics, expression, challenges, growth, dimensions, interactions, source, evidence) | `hd_interpretations.payload` (jsonb); Contract: **interpretations_contract.md** | ✅ |
| payload.source | **Herkunft der Extraktion:** `llm_extraction` \| `mvp_stub` (Worker setzt fest). System (hd, bazi, …) in Zeile `system`. | ✅ Wie in Layer-Docs und interpretations_contract festgelegt. |
| payload.dimensions | Objekt mit Keys mechanical, psychological, somatic, social, shadow, gift, role, archetype (Werte string\|null) | ✅ Contract + LLM-Prompt + Worker liefern dieses Shape. |
| payload.interactions | with_centers, with_profile, with_authority (Arrays) | ✅ |
| evidence (chunk_id, quotes) | Im Contract und Worker: **payload.evidence** (chunk_id, quotes); Zeile hat zusätzlich `chunk_id` als Spalte | ✅ |

**Referenz:** `interpretations_contract.md`, `worker_contract_extract_interpretations.md`.

---

## L4 Knowledge Graph (Nodes + Edges)

### Nodes

| Vorgabe (Blueprint) | Umgesetzt in | Status |
|---------------------|--------------|--------|
| node_id / node_key, type, canonical_description, metadata | `public.hd_kg_nodes` (id, node_key, node_type, canonical_description, metadata) | ✅ |
| metadata: interpretation_ids, chunk_ids, source, dimensions, interactions | text2kg schreibt genau diese Keys in node.metadata (dimensions/interactions aus payload) | ✅ Siehe text2kg_spec.md, Worker. |
| canonical_description leer bis Synthesis | text2kg setzt **canonical_description = NULL**; Synthesis-Job füllt später | ✅ Wie in layers_overview und text2kg_spec vorgesehen. |
| node_key stabil / normalisiert | Term-Mapping-Lookup (canonical_id) + Fallback system.element_type.element_id | ✅ Implementiert. |

### Edges

| Vorgabe (Blueprint) | Umgesetzt in | Status |
|---------------------|--------------|--------|
| from_node, to_node, relation_type, strength, metadata | `public.hd_kg_edges` (from_node_id, to_node_id, relation_type, strength, metadata) | ✅ Schema vorhanden. |
| relation_type: part_of, depends_on, amplifies, maps_to, … | **text2kg** aktuell: nur Nodes (MVP); Edges aus payload.relations geplant, erlaubte Typen: part_of, depends_on, amplifies, maps_to (Blueprint listet mehr auf; wir nutzen bewusst Teilmenge, siehe text2kg_spec) | ⚠️ Edges aus Relations noch nicht implementiert; Spec und Schema sind vorbereitet. |
| strength: low \| medium \| strong \| dominant | DB default `medium`; Migration erlaubt Werte wie im Blueprint | ✅ |

**Referenz:** `text2kg_spec.md`, `text2kg_implementation_sketch.md`, Migration `20260119165000_hd_knowledge_core.sql`.

---

## Term-Mapping (Layer C, kritische Ergänzung)

| Vorgabe (layers_overview) | Umgesetzt in | Status |
|---------------------------|--------------|--------|
| canonical_id, system, term, synonyms, school, language | `public.hd_term_mapping` (canonical_id, system, term, language, school, synonyms, …) | ✅ |
| Job extract_term_mapping | Worker: Seed-Befüllung + Pipeline vor extract_interpretations; text2kg nutzt Lookup für node_key | ✅ |

---

## Abgrenzung KG vs. Dynamics vs. Interactions (layers_overview)

| Vorgabe | Umgesetzt | Status |
|---------|-----------|--------|
| KG-Edges nur strukturell (part_of, depends_on, amplifies, maps_to) | text2kg_spec + Worker: dimensions/interactions **nicht** als Edges, nur in node.metadata | ✅ |
| Dynamics = hd_dynamics (Phasen/Traps/Growth), nicht als Kanten | extract_dynamics geplant; keine Kanten aus Dynamics | ✅ Konzept eingehalten. |
| Interactions = hd_interactions (Pattern/Regelsets), **niemals** als KG-Kanten | payload.interactions **nur** in node.metadata.interactions; **dürfen nie** KG-Edges erzeugen. extract_interactions geplant → hd_interactions. | ✅ |

---

## Noch nicht implementiert (bewusst offen)

- **L4 Edges** aus payload.relations (Schema und Spec vorbereitet, MVP nur Nodes).
- **L6** hd_dynamics: Job extract_dynamics.
- **L6/Layer C** hd_interactions: Job extract_interactions.
- **L10** Synthesis: Job **synthesize_node** implementiert (hd_synthesis_wordings + hd_kg_nodes.canonical_description); hd_syntheses.payload optional später.
- **L7, L8, L9, L11**: Context, Temporal, Guidance, State Detection – Tabellen/Jobs nicht im aktuellen MVP.
- **System Descriptor:** Vollständig spezifiziert: `system_descriptor_spec.md`, JSON-Deskriptoren (hd, bazi, astro, genekeys) in `system_descriptors/*.json`, DB-Tabelle `public.hd_systems` (Migration `20260210120000_hd_systems.sql`), Worker-Contract `worker_contract_system_descriptor.md`. Integration in Worker-Jobs (classify_domain, text2kg, …) folgt schrittweise.

Diese Punkte sind in den Layer-Docs als „geplant“ bzw. „optional“ geführt und brechen die Vorgaben nicht.

---

## Kurzfassung

- **L1–L3, L5, L4 Nodes, Term-Mapping, payload.source/dimensions/interactions:** wie in Layer-Modell und JSON-Blueprints vorgesehen umgesetzt bzw. in verbindlichen Contracts (interpretations_contract, text2kg_spec) abgebildet.
- **L4 Edges:** Schema und erlaubte relation_types definiert; Erzeugung aus payload.relations im MVP ausstehend, in Spec skizziert.
- **L10 (Synthesis):** synthesize_node im Worker umgesetzt (Stub + optional LLM); Pipeline text2kg → synthesize_node. **L6 (Dynamics/Interactions), L7–L9, L11:** wie in den Layer-Docs als nächste Schritte/geplant dokumentiert.

**Referenzen:** `layer_model_and_schemas.md`, `layers_overview.md`, `interpretations_contract.md`, `text2kg_spec.md`, `worker_contract_spark_supabase.md`, `current_status_local_dev.md`, `system_descriptor_spec.md`.
