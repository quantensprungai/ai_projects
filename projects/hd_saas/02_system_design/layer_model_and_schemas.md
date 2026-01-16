<!-- Reality Block
last_update: 2026-01-16
status: draft
scope:
  summary: "Layer-Modell + JSON-Schema-Blueprints (aus hd_system_raw.md konsolidiert)."
  in_scope:
    - layer overview
    - schema blueprints (JSONB-friendly)
    - how layers relate
  out_of_scope:
    - full implementation
    - exhaustive domain ontology for all systems
notes:
  - "Quelle: hd_system_raw.md (Konsolidierung; nicht 1:1 Kopie)."
-->

# Layer Model & Schemas – HD‑SaaS

Ziel: Das Wissen ist nicht “im LLM”, sondern **explizit gespeichert**. Supabase/Postgres kann das als **JSONB‑first** abbilden.

## Layer Überblick (12+)

Minimaler Kern (MVP):
- **L1 Ingestion** (Files/Links/Uploads)
- **L2 Cleaning/Chunking**
- **L3 Domain Classification**
- **L4 Knowledge Graph** (Nodes/Edges)
- **L5 Interpretation Repository** (Quellen‑Aussagen)
- **L6 Dynamics Engine** (Prozesslogik)
- **L7 Context** (User‑Kontext/Konditionierung)
- **L8 Temporal** (Zyklen/Transite)
- **L9 Guidance/Reflection** (Fragen/Übungen/Handlungsableitungen)
- **L10 Synthesis** (canonical texts/versions)
- **L11 State Detection** (welche Phase/Dynamik gerade aktiv)

Optionale Erweiterungen (wenn benötigt):
- **Body‑Mechanics** (somatische/“körperliche” Aspekte aus Quellen)
- **Hidden Expectations** (soziale Erwartungsfelder)
- **Relationship Dynamics**
- **Environment/Fate** (Ort/Umgebung als relevanter Faktor)

## Schema Blueprints (JSON, JSONB‑friendly)

### L1 Ingestion (File/Source Registry)

```json
{
  "ingest_id": "uuid",
  "source_type": "upload|url|youtube|raw_text",
  "file_type": "pdf|image|audio|video|text|url",
  "source_url": "string|null",
  "storage_path": "string|null",
  "language_detected": "string|null",
  "status": "pending|processed|failed",
  "metadata": { "created_at": "timestamp", "uploaded_by": "uuid|null" }
}
```

### L2 Cleaning/Chunking

```json
{
  "clean_id": "uuid",
  "ingest_id": "uuid",
  "chunks": [
    {
      "chunk_id": "uuid",
      "text_clean": "string",
      "token_count": 1234,
      "metadata": { "page": 12, "timestamp_range": "00:10:11-00:12:03" }
    }
  ]
}
```

### L3 Domain Classification

```json
{
  "classification_id": "uuid",
  "chunk_id": "uuid",
  "system": "HD|BaZi|Astro|GeneKeys|Numerology|Mixed|Other",
  "probability": 0.0,
  "subdomain": "Gate|Line|Center|Profile|Stem|Branch|House|Archetype|...",
  "element_id": "string|null",
  "tags": ["string"]
}
```

### L4 Knowledge Graph (Nodes + Edges)

Node:

```json
{
  "node_id": "string",
  "type": "Gate|Line|Center|Channel|Profile|Authority|Type|Stem|Branch|House|Archetype",
  "canonical_description": "string|null",
  "metadata": { "system_origin": "HD|BaZi|Astro|...", "created_at": "timestamp" }
}
```

Edge:

```json
{
  "edge_id": "uuid",
  "from_node": "node_id",
  "to_node": "node_id",
  "relation_type": "belongs_to|part_of|amplifies|weakens|overrides|modulates|depends_on|context_specific|emerges_to",
  "strength": "low|medium|strong|dominant|overriding",
  "metadata": { "source": "string", "extracted_from": "chunk_id" }
}
```

### L5 Interpretation Repository (Quellen‑Aussagen)

```json
{
  "interpretation_id": "uuid",
  "system": "HD|BaZi|Astro|GeneKeys|...",
  "source": "book|lecture|transcript|website",
  "element_type": "Gate|Line|Profile|Stem|Branch|...",
  "element_id": "string",
  "text_raw": "string",
  "text_clean": "string",
  "highlighted_statements": ["string"],
  "metadata": { "ingest_id": "uuid", "chunk_id": "uuid", "created_at": "timestamp" }
}
```

### L6 Dynamics Engine (Prozesslogik)

```json
{
  "dynamic_id": "uuid",
  "name": "string",
  "system": "HD|BaZi|Astro|Multi",
  "references": ["node_id"],
  "description": "string",
  "phases": [
    {
      "phase": 1,
      "name": "string",
      "description": "string",
      "symptoms": ["string"],
      "triggers": ["string"],
      "risks": ["string"],
      "opportunities": ["string"]
    }
  ],
  "growth_path": ["string"],
  "metadata": { "source": "string|null" }
}
```

### L7 Context (User‑Kontext/Konditionierung)

```json
{
  "context_id": "uuid",
  "user_id": "uuid",
  "static": { "age": 0, "gender": "string|null", "culture": "string|null" },
  "conditioning": { "open_centers": ["string"], "family_patterns": ["string"] },
  "life_factors": { "relationship_status": "string|null", "career_stage": "string|null" }
}
```

### L8 Temporal (Zyklen/Transite)

```json
{
  "temporal_id": "uuid",
  "user_id": "uuid",
  "cycles": {
    "saturn_return": { "active": false, "start": "date|null", "end": "date|null" },
    "uranus_opposition": { "active": false },
    "chiron_return": { "active": false }
  },
  "current_influences": [{ "element_id": "string", "score": 0.0 }]
}
```

### L9 Guidance/Reflection

```json
{
  "guidance_id": "uuid",
  "linked_to": "dynamic_id|node_id",
  "type": "reflection|coaching|integration",
  "questions": ["string"],
  "actions": ["string"],
  "integration_prompts": ["string"]
}
```

### L10 Synthesis (Canonicalization)

```json
{
  "synthesis_id": "uuid",
  "element_type": "Gate|Line|Profile|...",
  "element_id": "string",
  "generated_description": "string",
  "version": 1,
  "sources_used": ["interpretation_id"],
  "metadata": { "model": "string", "created_at": "timestamp" }
}
```

### L11 State Detection (Phase Matching)

```json
{
  "state_id": "uuid",
  "user_id": "uuid",
  "dynamic_id": "uuid",
  "current_phase": 2,
  "confidence": 0.78,
  "evidence": [{ "text": "string", "score": 0.33 }],
  "context_modifiers": { "authority": 0.0, "temporal": 0.0 },
  "timestamp": "timestamp"
}
```

## Was ist noch nicht “eingepflegt” aus `hd_system_raw.md`?

- Die ausführlichen Ausformulierungen/Beispiele pro Layer (z. B. komplette 3/5‑Dynamics) sind noch nicht als konkrete Datensätze modelliert.
- Die operativen Implementierungsdetails (Supabase SQL, konkrete Pipeline‑Jobs) sind noch nicht gebaut – nur Architektur/Flows/Schemas.


