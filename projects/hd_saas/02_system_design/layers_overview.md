<!-- Reality Block
last_update: 2026-01-31
status: draft
scope:
  summary: "1-Doc Übersicht der Processing-Layer (Flow B/C/D) für HD-SaaS inkl. Tabellen/Jobs/Artefakte und Einordnung des Interpretations-Schemas."
  in_scope:
    - Processing layer map (Flow B/C/D)
    - responsibilities (Supabase control plane vs worker data plane)
    - where Interpretations schema fits
  out_of_scope:
    - full infra topology (VM105/VM102) (kommt später in einer End-to-End Übersicht)
    - implementation code details
notes: []
-->

# Processing Layer Overview (Flow B/C/D)

Diese Seite ist die **kompakte 1‑Doc‑Übersicht** über die Processing‑Schichten nach der Ingestion.

## Leitprinzip (Control Plane vs Data Plane)

- **Supabase (DB + Storage + RLS + Job Queue)** = **Control Plane** (Source of Truth)
- **Worker (Spark/DGX)** = **Data Plane** (OCR/Whisper/LLM‑Processing im Batch)

Wichtig: Ein Worker kann nur Jobs sehen, wenn er gegen **dieselbe Supabase‑Instanz** läuft (typisch: **Cloud**). Lokal (`127.0.0.1:54321`) ist primär für UI/Ingestion/Dev.

Referenzen:
- Worker Contract: `projects/hd_saas/02_system_design/worker_contract_spark_supabase.md`
- Ops: `infrastructure/spark/hd_worker_ops.md`
- Flows: `projects/hd_saas/02_system_design/data_flows.md`
- Layer‑Blueprints: `projects/hd_saas/02_system_design/layer_model_and_schemas.md`

---

## Flow A — Upload + Binding (Asset Registry ↔ Files ↔ Job Creation)

Dieser Flow ist **pre‑processing** und entscheidet, ob der Rest deterministisch/robust läuft.

**Zweck:**
- Uploads tenant‑safe speichern
- Dateien an `hd_assets` binden (Idempotenz!)
- daraus **deterministische Jobs** erzeugen (z. B. `extract_text`)

### Inputs
- `assets.jsonl` (metadata‑only; bereits implementiert)
- Content Files: PDF/Text/Audio/Video (Upload; noch zu implementieren)

### Storage Konvention (tenant‑safe)
- Bucket: `hd_uploads_raw`
- Paths unter: `accounts/{account_id}/...` (keine „freien“ Pfade)

### DB‑Artefakte (Source of Truth)
- `public.hd_assets` (Registry; `source_ref` als stabiler Identifier, typ. MD5)
- `public.hd_documents` (Dokument‑Metadaten)
- `public.hd_document_files` (Bucket + storage_path, Unique auf bucket+path)
- `public.hd_ingestion_jobs` (Job Queue)

### Guardrails (damit nichts chaotisch wird)
- **Idempotenz**:
  - `hd_assets` upsert by `(account_id, source_ref)`
  - `hd_document_files` unique `(bucket, storage_path)`
- **Binding‑Regel**:
  - Asset ↔ File wird über `source_ref` (z. B. MD5) oder explizite Link‑Metadaten hergestellt.
- **Status‑Sets sind entitätsspezifisch**:
  - Jobs: `queued|running|completed|failed`
  - Assets: `queued|processed|failed`
  - Documents: `pending|processed|failed` (aktuell; muss final dokumentiert werden)
- **JSONB Hygiene**:
  - keine riesigen/circular payloads in `metadata` (sonst `Circular reference detected` Risiko)

---

## Mapping: Flows (A–E) ↔ Layer Modell (L1–L14)

Wir nutzen **Flows** als Prozess‑Sicht und **L‑Layer** als inhaltliche System‑Sicht. Das Mapping verhindert, dass Wissen/Verantwortung „zwischen Docs“ verloren geht.

| Layer (L) | Name | Primärer Flow |
|---|---|---|
| L1 | Ingestion (Files/Links/Uploads) | Flow A |
| L2 | Cleaning/Chunking | Flow B |
| L3 | Domain Classification | Flow C |
| L4 | Knowledge Graph (Nodes/Edges) | Flow C |
| L5 | Interpretation Repository | Flow C |
| L6 | Dynamics Engine | Flow C |
| L7 | Context (User‑Kontext/Konditionierung) | Flow E |
| L8 | Temporal (Zyklen/Transite) | Flow E |
| L9 | Guidance/Reflection | Flow E |
| L10 | Synthesis (canonical texts/versions) | Flow D |
| L11 | State Detection | Flow E |
| L12 | Body‑Mechanics (optional) | Flow B/C |
| L13 | Hidden Expectations (optional) | Flow C/E |
| L14 | Relationship Dynamics / Environment (optional) | Flow C/E |

Hinweis: Flow E (Query/Chat) ist bewusst **nicht** Teil dieses Dokuments (Focus: Processing), aber das Mapping zeigt, wo die späteren UX‑Layer andocken.

---

## Layer B — Content Ingest (Dokument → Textbasis)

**Zweck:** Aus “Content” (PDF/Text/Audio/Video) eine **saubere Textbasis** machen, die downstream stabil verarbeitet werden kann.

### Inputs
- Dateien/Objekte in Storage (tenant‑safe): `accounts/{account_id}/...` in Bucket `hd_uploads_raw`
- Metadaten‑Registry: `public.hd_assets` (mindestens metadata‑only möglich)

### Jobs (geplant)
- `extract_text`
  - **PDF Text Extraction** (wenn textbasiert)
  - **OCR** (wenn Scan/Images)
- optional (Audio/Video):
  - Whisper Transcript → Text

### Outputs (DB‑Artefakte)
- `public.hd_document_texts` (optional “raw text”, pragmatischer Zwischenspeicher)
- `public.hd_asset_chunks` (normierte Chunks; bevorzugt als stabile Schnittstelle)

### Qualitäts-Gates (empfohlen)
- **Detektion**: “PDF ist textbasiert vs Scan” (entscheidet OCR ja/nein)
- **Cleaning**: Entfernen von Headers/Footers, Seitenzahlen, Artefakten
- **Chunking**: deterministisch (reproduzierbar), inkl. `chunk_index`

---

## Layer C — Extraction (Textbasis → Interpretations/TermMapping/KG/Dynamics/Interactions)

**Zweck:** Aus Chunks strukturierte Wissenseinheiten machen, die KG/Dynamics speisen.

### Inputs
- `public.hd_asset_chunks` (primär)
- optional: `public.hd_document_texts`

### Jobs (geplant)
- `classify_domain` (HD|BaZi|Astro|Mixed|Other)
- `extract_interpretations` (Chunks → Interpretations)
- `extract_term_mapping` (Interpretations + Chunks → Term-Mapping)
- `text2kg` (Interpretations → KG Nodes/Edges)
- `extract_dynamics` (Interpretations + Chunks → Dynamics)
- `extract_interactions` (Interpretations + Chunks → Interaction Patterns)

### Outputs (DB‑Artefakte)
- `public.hd_interpretations` (strukturierte Extraktionen; jsonb `payload`)
- `public.hd_term_mapping` (Synonyme/Schulen → canonical_id)
- `public.hd_kg_nodes`, `public.hd_kg_edges` (Graph)
- `public.hd_dynamics` (Zyklen/Phasen/Traps/Growth Paths, zeit-/zustandsbezogen)
- `public.hd_interactions` (soziale/kontextuelle Interaktionsmuster: Typ/Profil/Zentren/Authority)

---

## Layer D — Synthesis (KG/Interpretations → Canonical)

**Zweck:** Konsolidierte, versionierbare “Canonical Descriptions” erzeugen, die im Chat/UX genutzt werden.

### Inputs
- `public.hd_kg_nodes` + relevante Edges
- Interpretations + Term-Mapping + Dynamics + Interactions als Evidenz

### Jobs (geplant)
- `synthesize_node`

### Outputs
- `public.hd_syntheses` (optional versioniert)
- optional: `public.hd_kg_nodes.canonical_description`

---

## Einordnung: Neuer Interpretations-Teil aus `hd_system_raw.md`

Der neue Abschnitt (ab ca. Zeile 4894 in `scratch/inbox/hd/hd_system_raw.md`) ist **kein Layer an sich**, sondern eine **Spezifikation** für Layer C (`extract_interpretations`):

- Er definiert eine **Interpretations‑Ontology** (Essenz, Mechanik, Ausdruck, Challenges, Growth, Interactions, Source)
- Ziel: **konsistente, LLM‑freundliche** Einträge, die später synthesis/KG stabil speisen

## Kritische Ergänzung 1: Term‑Mapping‑Layer (Synonyme/Schulen → Canonical IDs)

**Warum eigener Layer?**
- Interpretations und KG können nur stabil “zusammenwachsen”, wenn Begriffe über Schulen hinweg **normalisiert** sind.
- Ohne Term‑Mapping entstehen Inkonsistenzen: z.B. `Generator` vs `Builder` vs `Sacral Being`.

**Zweck:**
- Synonyme/Varianten/Schulbegriffe (HD Classic, 64keys, Gene Keys, moderne Terminologie) werden auf eine **canonical_id** gemappt.
- Synthesis und UX können dann konsistent “User-facing wording” ausgeben (inkl. Übersetzung/Style).

**Minimaler Output (DB): `public.hd_term_mapping`**
- `canonical_id` (string, z.B. `hd.type.generator`)
- `system` (z.B. `hd`, `genekeys`)
- `term` (string, z.B. `Generator`)
- `synonyms` (string[] oder separate rows)
- `school` / `source` (string, z.B. `HD_classic`, `64keys`)
- `language` (z.B. `de`, `en`)
- optional: `notes`, `confidence`, `evidence_chunk_ids`

**Job: `extract_term_mapping`**
- Input: Chunks + Interpretations + optional existierende Mappings
- Output: Upsert `hd_term_mapping`

---

## Kritische Ergänzung 2: Abgrenzung „KG Edges“ vs „Dynamics“ vs „Interactions“

Diese Trennung darf nicht verwischen:

### A) Strukturelle Relationen = Knowledge Graph (`hd_kg_edges`)
- “dauerhafte” semantische Beziehungen: `part_of`, `depends_on`, `amplifies`, `maps_to`, …
- eher zeitlos, erklärend, gut für Navigation/Query.

### B) Dynamische Prozesse = `hd_dynamics`
- Zustandswechsel/Zyklen/Phasen/Traps/Growth Paths.
- Beispiele: “Wenn emotionale Autorität → warte auf Klarheit”, “Not-Self Signale”, “Deconditioning Phasen”.
- Output sollte **prozess-/zustandsorientiert** sein, nicht “Kanten im KG”.

### C) Soziale/kontextuelle Muster = `hd_interactions`
- Interaktionslogik zwischen Typ/Profil/Zentren/Authority (und später Beziehungen/Partner-Dynamiken).
- Das sind **Pattern** und **Regelsets**, nicht (nur) semantische Kanten.

---

## Kritische Ergänzung 3: Meaning Dimensions (Synthesis braucht explizite Dimensionen)

Deine Interpretations‑Ontology (essence/mechanics/expression/…) ist ein sehr guter Start, aber für “deep human” Synthesis brauchen wir explizite **Dimensions‑Slots**, damit:\n- Mechanics nicht mit Social Role vermischt wird\n- Challenges nicht pauschal “Shadow” bedeutet\n- Interactions nicht die ganze Bedeutungslandschaft tragen muss

**Pflicht-Contract: payload.dimensions (Keys immer vorhanden, Werte dürfen null sein)**

Minimaler, stabiler Kern (multisystem‑fähig):
- `mechanical`: string|null
- `psychological`: string|null
- `somatic`: string|null
- `social`: string|null
- `shadow`: string|null
- `gift`: string|null
- `role`: string|null
- `archetype`: string|null

Optional (später erweiterbar, ohne Contract zu brechen):
- `practice`: string|null
- `context`: string|null
- `language`: string|null
- `examples`: string[]|null

**Wichtig:** Das muss nicht alles “immer” gefüllt sein.\nDer Nutzen ist: Synthesis kann gezielt Slots ziehen und konsistent zusammensetzen.

### Empfohlenes Mapping in HD‑SaaS

In HD‑SaaS liegt das strukturiert in:
- `public.hd_interpretations.payload` (jsonb)

Empfohlene Keys (aus dem Raw‑Teil):
- `essence`: string
- `mechanics`: string
- `expression`: string
- `challenges`: string[]
- `growth`: string[]
- `interactions`: object
  - `with_centers`: string[]
  - `with_profile`: string[]
  - `with_authority`: string[]
- `source`: string (z.B. "HD_classic", "GeneKeys", …)

Zusätzliche, systemische Felder (aus dem DB‑Modell):
- `hd_interpretations.system`: z.B. `hd`
- `hd_interpretations.element_type`: z.B. `type` | `strategy` | `authority`
- `hd_interpretations.element_id`: z.B. `generator` | `wait_to_respond` | `sacral`
- optional: `chunk_id` (Evidenz/Provenance)

### Mini-Beispiele (Schema in Aktion)

Beispiel (Typ: Generator) – Payload:

```json
{
  "essence": "Lebensenergie + Antwortmechanik.",
  "mechanics": "Die sakrale Energie arbeitet korrekt nur auf Reaktion, nicht auf Initiation.",
  "expression": "Im Flow wenn beschäftigt; Frustration bei Fehlentscheidungen.",
  "challenges": ["zu früh initiieren", "Ja sagen ohne sakrale Antwort"],
  "growth": ["Warten auf Reize", "sakrale Vokale hören (Uh-huh / Un-uh)"],
  "interactions": {
    "with_profile": ["3/5 verstärkt Trial & Error"],
    "with_centers": ["offenes Solarplexus erhöht Reaktivität"],
    "with_authority": ["emotionale Autorität → Warten auf Klarheit"]
  },
  "source": "HD_classic"
}
```

---

## Kritische Ergänzung 4: Canonical Wording (User-facing Stimme)

`canonical_description` ist die **technische** Definition. Für echte UX/Brand/Mehrsprachigkeit brauchen wir zusätzlich **canonical_wording** (user‑friendly) inkl. Stilvarianten.

**Regel:** `canonical_wording` gehört **nicht** in `hd_kg_nodes` (Graph bleibt strukturell). Es gehört in Synthesis (`hd_syntheses`) oder eine Child‑Table.

Empfohlenes Shape (in `hd_syntheses.payload` oder Child‑Table):

```json
{
  "canonical_id": "hd.type.generator",
  "canonical_description": "TECH–Definition ...",
  "canonical_wording": "USER–friendly modern language ...",
  "styles": {
    "natural": "...",
    "coaching": "...",
    "poetic": "...",
    "technical": "..."
  },
  "language": "de",
  "version": 1
}
```

---

## Kritische Ergänzung 5: System Descriptor / Registry (Multi‑System)

Damit HD ↔ GeneKeys ↔ BaZi ↔ Astro später nicht „hardcoded“ vermischt wird, definieren wir pro System einen Descriptor.

Minimaler Descriptor:

```json
{
  "system_id": "hd",
  "input_format": "datetime + birth_location",
  "element_types": ["type", "strategy", "authority", "profile", "center", "gate", "channel", "circuit"],
  "mapping_rules": {
    "canonical_id_prefix": "hd.",
    "language_defaults": ["de", "en"]
  }
}
```

## OCR/Extraction Tooling (was im Setting “Sinn macht”)

Aus den vorhandenen Docs ist die pragmatische Reihenfolge:

1. **Zuerst stabil**: `import_assets_jsonl` → `hd_assets` (läuft lokal schon)
2. **Dann**: Worker‑Jobs für Textbasis/Extraction (Flow B/C/D), typischerweise auf Spark/DGX

Für PDF‑Textbasis (Layer B) ist im Spark‑Kontext als risikoarmer Start sinnvoll:
- **Docling** oder **PyMuPDF4LLM** für textbasierte PDFs (schnell, robust)
- **Marker** (oder OCRmyPDF/Tesseract) für Scan‑PDFs/OCR‑lastige Fälle
- Whisper nur wenn Audio/Video wirklich vorkommt

Entscheidend ist ein Gate “text PDF vs scan PDF”, damit nicht alles blind durch OCR geht.

