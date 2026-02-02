<!-- Reality Block
last_update: 2026-01-31
status: draft
scope:
  summary: "Verbindlicher Contract für `public.hd_interpretations.payload` inkl. Dimensions (Keys mandatory, values nullable), Interactions, Evidence und Canonical IDs."
  in_scope:
    - payload contract (required vs optional)
    - id strategy (system/element_type/element_id/canonical_id)
    - how this feeds term-mapping, KG, dynamics, synthesis
  out_of_scope:
    - prompt implementations
    - full ontology for all HD element types
notes: []
-->

# Interpretations Contract (HD‑SaaS)

Diese Spec ist die **wichtigste Schnittstelle** zwischen:

- Layer B (Textbasis/Chunks) und
- Layer C (Extraction) und
- Layer D (Synthesis/UX).

Ziel: Interpretations sind **LLM‑freundlich**, aber **deterministisch strukturierbar**, damit keine Semantik „im Modell“ verschwindet.

## 1) Scope: Was ist eine Interpretation?

Eine Interpretation ist eine **strukturierte, zitier-/evidenzfähige Aussage** zu einem Element (z.B. Type/Strategy/Authority, später Gates/Lines/Centers/Channels).

- Speicherung: `public.hd_interpretations.payload` (jsonb)
- Identifikation: `system` + `element_type` + `element_id` (plus optional `canonical_id` via Term‑Mapping)

## 2) Required Fields (payload)

### 2.1 Core Narrative (required keys)

- `essence`: string
- `mechanics`: string
- `expression`: string
- `challenges`: string[]  (leer erlaubt)
- `growth`: string[]      (leer erlaubt)
- `source`: string        (z.B. `HD_classic`, `GeneKeys`, `64keys`, `modern_hd`)

### 2.2 Dimensions (required object, nullable values)

**Regel:** `dimensions` muss **immer** vorhanden sein (stabiler Contract), aber jeder Slot darf `null` sein.

```json
{
  "dimensions": {
    "mechanical": null,
    "psychological": null,
    "somatic": null,
    "social": null,
    "shadow": null,
    "gift": null,
    "role": null,
    "archetype": null
  }
}
```

Optional, aber empfohlen (kann später verpflichtend werden):
- `practice`: string|null
- `context`: string|null
- `language`: string|null
- `examples`: string[]|null

### 2.3 Interactions (required object, arrays may be empty)

```json
{
  "interactions": {
    "with_centers": [],
    "with_profile": [],
    "with_authority": []
  }
}
```

Optional später:
- `with_type`, `with_circuit`, `with_definition`, `with_conditioning`

## 3) Evidence / Provenance (recommended)

Ziel: Nichts „Wichtiges“ geht verloren. Synthesis/KG sollen immer auf Evidenz zurückgreifen können.

Empfohlen im payload:
- `evidence`: object|null
  - `chunk_id`: string|null (oder separate Relation via `hd_interpretations.chunk_id`)
  - `quotes`: string[]|null (kurze Zitate; optional)
  - `source_ref`: string|null (z.B. Buch/Doc ID)

## 4) IDs & Normalisierung

### 4.1 Element Address

Pflicht im DB‑Row (nicht payload):
- `hd_interpretations.system`: z.B. `hd`
- `hd_interpretations.element_type`: `type|strategy|authority|...`
- `hd_interpretations.element_id`: z.B. `generator`, `wait_to_respond`, `sacral`

### 4.2 Canonical IDs (Term‑Mapping)

Optional im payload (bis Term‑Mapping Tabelle existiert):
- `canonical_id`: string|null (z.B. `hd.type.generator`)

Später: `canonical_id` wird **aus `hd_term_mapping`** abgeleitet (oder dort nachgeschlagen), nicht „frei erfunden“.

## 5) Downstream Consumption (Wer nutzt was?)

- **Term‑Mapping (`extract_term_mapping`)** nutzt: `element_*`, `payload.source`, Textfelder + ggf. synonyms in Chunks
- **KG (`text2kg`)** nutzt: `canonical_id`/`element_*` + Dimensions (mechanical/shadow/gift als Relation-Kandidaten)
- **Dynamics (`extract_dynamics`)** nutzt: Dimensions (shadow/gift/practice) + challenges/growth als Prozesskandidaten
- **Interactions (`extract_interactions`)** nutzt: `payload.interactions` + social/role Dimensions
- **Synthesis (`synthesize_node`)** nutzt: alle Slots + Term‑Mapping, um `canonical_wording` + Styles zu erzeugen

## 6) Minimal Examples (sanity)

Beispiel (Type: Generator):

```json
{
  "essence": "Lebensenergie + Antwortmechanik.",
  "mechanics": "Sakrale Energie arbeitet korrekt auf Reaktion, nicht auf Initiation.",
  "expression": "Im Flow wenn beschäftigt; Frustration bei Fehlentscheidungen.",
  "challenges": ["zu früh initiieren", "Ja sagen ohne sakrale Antwort"],
  "growth": ["Warten auf Reize", "sakrale Vokale hören (Uh-huh / Un-uh)"],
  "interactions": {
    "with_centers": ["offenes Solarplexus erhöht Reaktivität"],
    "with_profile": ["3/5 verstärkt Trial & Error"],
    "with_authority": ["emotionale Autorität → Warten auf Klarheit"]
  },
  "dimensions": {
    "mechanical": "Antwortmechanik via Sakral.",
    "psychological": null,
    "somatic": null,
    "social": null,
    "shadow": "Frustration durch falsche Commitments.",
    "gift": "Zufriedenheit durch korrektes Ja/Nein.",
    "role": null,
    "archetype": null
  },
  "source": "HD_classic"
}
```

