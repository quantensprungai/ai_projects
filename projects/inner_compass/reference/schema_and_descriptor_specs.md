# Inner Compass — Schema-Blueprints & System-Descriptor-Spec

> Konsolidiert aus hd_saas: layer_model_and_schemas, system_descriptor_spec, layers_overview.
> cursor/contracts.md hat den Interpretations-Payload. cursor/architecture.md hat das 10-Tabellen-Schema.
> Dieses Dokument enthält: Alle Layer-JSON-Blueprints (L1-L11) + die vollständige System-Descriptor-Spec.

## 1. Flow ↔ Layer Mapping

| Layer | Name | Flow | Status |
|-------|------|------|--------|
| L1 | Ingestion | A | ✅ |
| L2 | Cleaning/Chunking | B | ✅ |
| L3 | Domain Classification | C | ✅ |
| L4 | Knowledge Graph (Nodes/Edges) | C | ✅ Nodes, ⚠️ Edges |
| L5 | Interpretation Repository | C | ✅ |
| L6 | Dynamics Engine | C | ❌ geplant |
| L7 | Context (User-Kontext) | E | ❌ geplant |
| L8 | Temporal (Zyklen/Transite) | E | ❌ geplant |
| L9 | Guidance/Reflection | E | ❌ geplant |
| L10 | Synthesis | D | ✅ |
| L11 | State Detection | E | ❌ geplant |

## 2. JSON-Schema-Blueprints (L1-L11)

### L1 Ingestion
```json
{ "ingest_id": "uuid", "source_type": "upload|url|raw_text",
  "file_type": "pdf|image|audio|text", "storage_path": "string|null",
  "language_detected": "string|null", "status": "pending|processed|failed" }
```

### L2 Cleaning/Chunking
```json
{ "chunk_id": "uuid", "ingest_id": "uuid", "text_clean": "string",
  "token_count": 1234, "metadata": { "page": 12 } }
```

### L3 Domain Classification
```json
{ "chunk_id": "uuid", "system": "hd|bazi|astro|mixed",
  "probability": 0.95, "subdomain": "Gate|Stem|House|...", "element_id": "string|null" }
```

### L4 Knowledge Graph
**Node:**
```json
{ "node_key": "hd.type.generator", "type": "Gate|Type|Stem|...",
  "canonical_description": "string|null",
  "metadata": { "interpretation_ids": ["uuid"], "dimensions": { "...": null },
                 "interactions": { "with_centers": [], "with_profile": [] } } }
```
**Edge:**
```json
{ "from_node": "node_id", "to_node": "node_id",
  "relation_type": "part_of|amplifies|depends_on|maps_to",
  "strength": "low|medium|strong|dominant" }
```

### L5 Interpretation Repository
→ Siehe `cursor/contracts.md` Abschnitt 3 (Interpretations-Payload). Autoritative Quelle.

### L6 Dynamics Engine
```json
{ "dynamic_id": "uuid", "name": "string", "system": "hd|bazi|multi",
  "references": ["node_id"],
  "phases": [{ "phase": 1, "name": "string", "symptoms": ["string"],
               "triggers": ["string"], "risks": ["string"], "opportunities": ["string"] }],
  "growth_path": ["string"] }
```

### L7 Context (User-Kontext)
```json
{ "user_id": "uuid",
  "conditioning": { "open_centers": ["string"], "family_patterns": ["string"] },
  "life_factors": { "relationship_status": "string|null", "career_stage": "string|null" } }
```

### L8 Temporal (Zyklen/Transite)
```json
{ "user_id": "uuid",
  "cycles": { "saturn_return": { "active": false, "start": "date|null" },
              "luck_pillars": { "current": "string|null" } },
  "current_influences": [{ "element_id": "string", "score": 0.0 }] }
```

### L9 Guidance/Reflection
```json
{ "linked_to": "dynamic_id|node_id", "type": "reflection|coaching|integration",
  "questions": ["string"], "actions": ["string"], "integration_prompts": ["string"] }
```

### L10 Synthesis
```json
{ "element_id": "string", "canonical_description": "string",
  "canonical_wording": "string|null",
  "styles": { "natural": "...", "coaching": "...", "poetic": "...", "technical": "..." },
  "language": "de|en", "version": 1, "sources_used": ["interpretation_id"] }
```

### L11 State Detection
```json
{ "user_id": "uuid", "dynamic_id": "uuid", "current_phase": 2,
  "confidence": 0.78, "evidence": [{ "text": "string", "score": 0.33 }] }
```

## 3. System Descriptor Spec

### 3.1 Zweck
Jedes integrierte System wird durch einen JSON-Deskriptor beschrieben. Alle Pipeline-Jobs (classify_domain → extract_interpretations → text2kg → synthesis) nutzen den Deskriptor zur Validierung und Steuerung.

### 3.2 Speicherorte

| Ort | Pfad |
|-----|------|
| Autoritative Quelle (JSON) | `projects/inner_compass/system_descriptors/{system_id}.json` |
| DB (Laufzeit) | `sys_systems` (system_id, system_name, canonical_prefix, descriptor jsonb) |
| Seed-Skript | `code/hd_saas_app/apps/web/scripts/seed_hd_systems.py` |

### 3.3 Descriptor-Format

```json
{
  "system_id": "string",
  "system_name": "string",
  "canonical_prefix": "string (z.B. 'hd.')",
  "input_format": "datetime | datetime+location | name | date",
  "calendar_basis": "gregorian | lunar | sidereal | solar",
  "element_types": ["type", "gate", "stem", "branch", "..."],
  "identifier_rules": { "gate": "1-64", "line": "1-6" },
  "canonical_id_rules": { "format": "{prefix}{element_type}.{element_id}" },
  "term_mapping_rules": { "schools": ["HD_classic", "64keys"], "normalization": "lowercase_underscore" },
  "kg_rules": { "allowed_relation_types": ["part_of", "depends_on", "amplifies", "maps_to"] },
  "dynamics_rules": { "has_dynamics": true, "dynamic_types": ["phase_cycle", "trap", "growth_path"] },
  "synthesis_rules": { "default_style": "natural", "language_defaults": ["de", "en"] },
  "interaction_rules": { "supports_interactions": true, "interaction_entities": ["type", "profile"] },
  "body_mechanics_support": true,
  "relationship_dynamics_support": true,
  "environment_fate_support": true
}
```

### 3.4 Required vs. Optional Felder

| Feld | Required | Beschreibung |
|------|----------|-------------|
| system_id | ✅ | Eindeutige ID (hd, bazi, astro...) |
| system_name | ✅ | Anzeigename |
| canonical_prefix | ✅ | Präfix für canonical_id |
| element_types | ✅ | Erlaubte Element-Typen |
| Alle anderen | ❌ | Fehlt → Worker nutzt Defaults |

### 3.5 Verwendung in Pipeline

| Job | Descriptor-Nutzung |
|-----|---------------------|
| classify_domain | system_id-Liste |
| extract_interpretations | element_types → Validierung |
| extract_term_mapping | term_mapping_rules (schools, normalization) |
| text2kg | canonical_prefix + allowed_relation_types |
| extract_dynamics | dynamics_rules.has_dynamics |
| synthesize_node | synthesis_rules (style, tone, language) |

### 3.6 Vorhandene Deskriptoren (10)

hd, bazi, astro, genekeys, enneagram, jyotish, numerology, nine_star_ki, mayan_tzolkin, akan

## 4. Abgrenzung: KG vs. Dynamics vs. Interactions

Diese Trennung ist verbindlich:

| Konzept | Tabelle | Inhalt | NICHT als |
|---------|---------|--------|-----------|
| Strukturelle Relationen | sys_kg_edges | part_of, depends_on, amplifies, maps_to | Dynamics/Interactions |
| Dynamische Prozesse | sys_dynamics | Zyklen, Traps, Growth Paths, Spektren | KG-Edges |
| Soziale/Kontextuelle Muster | sys_interactions | Interaktionslogik, Pattern, Regelsets | KG-Edges |
