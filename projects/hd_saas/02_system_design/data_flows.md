<!-- Reality Block
last_update: 2026-01-16
status: draft
scope:
  summary: "Datenflüsse für HD-SaaS inkl. Upstream (Anna Toolkit) und Content-Pipeline."
  in_scope:
    - data flow descriptions
    - sources/sinks
  out_of_scope:
    - implementation details
notes: []
-->

# Data Flows – HD‑SaaS

## Flow A: Metadaten (Katalog) – Anna Toolkit → HD‑SaaS

- **Source**: `code/annas-archive-toolkit`
  - `projects/<profile>/…`
  - `output/<profile>/metadata.json`
  - optional Export: `output/<profile>/assets.jsonl`
- **Sink**: Supabase DB (`assets` o. ä.)
- **Purpose**: Suche/Selektion/Priorisierung – **metadata‑only**.

## Flow B: Content Ingest – Dokumente → Textbasis

- **Source**: beschaffte Inhalte (Uploads/own library/licensed/free content)
- **Steps**:
  - PDF/Text → Parsing
  - Scan → OCR
  - Audio/Video → Whisper Transcript
  - Cleaning/Chunking
- **Sink**: Supabase (`documents`, `chunks`, `interpretations`)

## Flow C: Extraction – Textbasis → KG + Dynamics

- **Source**: Chunks/Interpretations
- **Steps**:
  - Domain Classification (HD/BaZi/Astro/…)
  - Entity/Relation Extraction
  - KG upsert (Nodes/Edges)
  - Dynamics Objects (Phasen/Traps/Growth Paths)
- **Sink**: Supabase (`kg_nodes`, `kg_edges`, `dynamics`)

## Flow D: Synthesis – KG/Interpretations → Canonical

- **Source**: Interpretations + KG + Dynamics
- **Step**: Canonicalization (LLM) → versioned canonical texts
- **Sink**: `kg_nodes.canonical_description` (+ optional separate `synthesis_versions`)

## Flow E: Query/Chat – User Frage → Antwort

- **Source**: App (Makerkit UI / API)
- **Steps**:
  - fetch: relevante KG‑Nodes/Edges + Dynamics + Kontext/Temporal
  - LLM Antwort (mit Quellenreferenzen)
- **Sink**: UI + optional Conversation Log


