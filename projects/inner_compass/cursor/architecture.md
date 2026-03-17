# Inner Compass — Architektur

> Schema, Datenschichten, Tech Stack. Technische Wahrheit für Implementierung.

## 1. Die fünf Datenschichten

```
A: Rohmechanik       ✅ implementiert    sys_kg_nodes (Strukturbäume)
B: Bedeutungen       ✅ implementiert    sys_interpretations (LLM-extrahiert)
C: Dynamiken         ⚠️ Schema da       sys_dynamics + process-Feld
D: Cross-System      ❌ FEHLT (kritisch) sys_kg_edges (maps_to, cross_system)
E: Meta-Knoten       ❌ FEHLT           sys_kg_nodes (system=meta)
```

Ohne D+E = Multi-App. Mit D+E = Meta-System.

## 2. Schema (10 Tabellen, sys_*-Präfix)

### Registry
```sql
sys_systems              -- System-Deskriptoren (HD, BaZi, Astro, ...)
```

### Ingestion
```sql
sys_sources              -- PDF-Quellen (ehemals hd_assets + hd_documents)
sys_source_chunks        -- Textchunks aus PDFs
sys_ingestion_jobs       -- Pipeline-Job-Tracking
```

### Knowledge Graph
```sql
sys_kg_nodes             -- Nodes mit system, embedding (pgvector), canonical_id
sys_kg_edges             -- Edges mit edge_scope, review_status
sys_interpretations      -- LLM-extrahierte Bedeutungen (pro Chunk, pro Element)
sys_dynamics             -- Prozesse, Zyklen, Spektren
```

### Normalisierung
```sql
sys_term_mapping         -- Term-Normalisierung (Multi-School, Multi-Language)
sys_synthesis_wordings   -- Kanonische Texte + Styles + Sprachen
sys_interactions         -- N:M Interaktionsregeln (Hyperedges, 2+ Elemente)
```

## 3. Kritische Schema-Felder (NEU vs. aktuell)

Was bei der Migration von `hd_*` → `sys_*` hinzukommt:

```sql
-- sys_kg_nodes:
system text NOT NULL,                    -- 'hd' | 'bazi' | 'meta' etc.
canonical_id text,                       -- = node_key (konsistent mit term_mapping)
embedding vector(1536),                  -- pgvector für Similarity Search

-- sys_kg_edges:
edge_scope text DEFAULT 'intra_system',  -- 'intra_system' | 'cross_system'
review_status text DEFAULT 'approved',   -- 'approved' | 'candidate' | 'rejected'

-- sys_interpretations.payload (jsonb):
-- NEU: "process" Objekt (trap, gift_activation, experiment_seed)
-- NEU: "life_domain" Tag
-- NEU: 3 Dimension-Keys (elemental_quality, temporal_phase, destiny_pattern)
```

## 4. Datenfluss

```
PHASE 0: STRUKTURBÄUME (vor PDF-Verarbeitung)
  Deskriptor JSON → Seed-Script → sys_kg_nodes + sys_kg_edges
  Ergebnis: Leerer aber strukturierter Graph pro System

PHASE 1: QUELLEN-EXTRAKTION
  PDF → MinerU (GPU) → sys_source_chunks
  Chunk → 4 parallele LLM-Jobs:
    extract_entities      → Matched gegen existierende Nodes
    extract_meanings      → sys_interpretations
    extract_relationships → sys_kg_edges (intra_system)
    extract_processes     → sys_dynamics

PHASE 2: SYNTHESIS + EMBEDDINGS
  Alle Interpretationen pro Node → synthesize_node
    → canonical_description + synthesis_wordings
    → embedding (pgvector)

PHASE 3: CROSS-SYSTEM-MAPPING
  Embedding Cosine Similarity zwischen Systemen
    → Kandidaten (>0.75) → LLM-Validierung
    → sys_kg_edges (maps_to, cross_system, candidate)
    → Human Review → approved/rejected

PHASE 4: META-KNOTEN
  Cross-System-Edges → Clustering
    → 3+ Systeme zeigen auf dasselbe → Meta-Knoten
    → LLM benennt Archetyp
    → sys_kg_nodes (system=meta)
```

## 5. Tech Stack

| Komponente | Technologie |
|-----------|-------------|
| App | Next.js (Makerkit) + Supabase (Auth, DB, Storage, RLS) |
| Datenbank | Postgres + pgvector + jsonb |
| PDF-Parsing | MinerU (Open Source, GPU auf Spark) |
| LLM-Inferenz | SGLang/vLLM auf Spark, OpenAI-kompatible API |
| Worker | Python systemd-Services auf Spark, via Supabase service_role |
| Chart-Engines | hdkit (JS), alvamind (TS), pyswisseph (Python), tzolkin-calendar (Python) |
| Embeddings | text-embedding-3-large oder lokales Modell, in pgvector |
| VPN | Tailscale (Spark ↔ Supabase ↔ Dev) |

## 6. Infrastruktur-Topologie

```
[Spark / DGX]                          [Supabase Cloud]
├── MinerU (PDF-Parsing, GPU)          ├── Postgres + pgvector
├── SGLang/vLLM (LLM-Inferenz)        ├── Auth + RLS
├── Python Worker (systemd)            ├── Storage (PDFs)
├── Embedding Model                    └── Realtime (optional)
└── Chart Engines
        ↕ Tailscale VPN ↕
[Dev Machine / Cursor]
├── Next.js App (Makerkit)
├── Supabase Local (Dev)
└── ai_projects/ (Docs+Infra)
```

## 7. Sprachstrategie (KG → User)

```
Quellsprache (DE, EN, ZH, SA, ...)
  → LLM-Extraktion: IMMER Englisch → sprachneutraler KG
  → Synthesis: Kanonische Beschreibungen (EN im KG)
  → Wording-Styles pro Sprache: { de: { natural, coaching, poetic }, en: {...} }
```

Einzige multilinguale Schicht ist die letzte (Synthesis Wordings). KG bleibt sprachneutral.

## 8. Wo System-Artefakte wohnen (Docs vs. Code)

**Prinzip:** Root-Repo ai_projects = Docs/Infra/Meta. Code = eigenes Repo. System-Daten haben ihre **Source of Truth** in den Docs; der Code liest sie von dort oder von einer synchronisierten Kopie.

| Artefakt | Ort (Source of Truth) | Im Code-Repo? | Begründung |
|----------|------------------------|---------------|------------|
| **System-Deskriptoren** (hd.json, bazi.json, …) | `projects/inner_compass/system_descriptors/` | Optional Kopie | Seed-Script/Worker brauchen die JSONs. Entweder: Script läuft im Workspace-Kontext und liest `../../projects/inner_compass/system_descriptors/`, oder es gibt eine Kopie unter z.B. `apps/web/data/system_descriptors/` (Sync per Script/Manuell). |
| **System-Taxonomie** (system_taxonomy_v01.json) | `projects/inner_compass/reference/` oder `meta/` | Nein | Planungs-/Referenz-Artefakt. Wird nicht zur Laufzeit gelesen. |
| **Coverage-Matrix** (coverage_matrix_v01.csv) | `projects/inner_compass/reference/` oder `meta/` | Nein | Planung/Vollständigkeits-Check. Kein Runtime-Bedarf. |
| **Projektplan / IC_Projektplan** | `projects/inner_compass/reference/` | Nein | Doku. |
| **KG-Schema, Extraction Prompts** (IC_KG_Node_Edge_Schema, IC_Extraction_Prompts) | `projects/inner_compass/transfer/` | Nein | Specs für Implementierung; Code orientiert sich daran, speichert sie nicht. |
| **Chart-Engine-Kits** (hdkit, alvamind, pyswisseph, tzolkin-calendar, PyJHora, …) | — | **Ja, im Code-Repo** | Geklonte OSS-Kits leben unter `code/inner_compass_app/packages/engines/<system>/`. Werden für (1) Struktur-Parsing (Phase 0) und (2) Laufzeit-Berechnung (User-Charts) genutzt. Details: [engines.md §6](engines.md#6-wo-die-kits-wohnen--teil-des-app-repos). |

**Konkret für das Code-Repo (hd_saas_app → inner_compass_app):**

- **Falls Seed-Script/Worker im Monorepo-Kontext laufen** (z.B. von ai_projects-Root): Pfad auf Deskriptoren = `projects/inner_compass/system_descriptors/` (relativ zum Workspace-Root). Keine Kopie nötig.
- **Falls App-Repo allein deployed wird** (ohne projects/): Deskriptoren in den Code kopieren, z.B. `apps/web/data/system_descriptors/` oder `packages/ic-data/descriptors/`. In README oder Doku festhalten: „Source of Truth: projects/inner_compass/system_descriptors/; bei Änderungen dort in den Code syncen.“
- **Engine-Kits:** Immer im App-Repo unter `packages/engines/<system>/` (geklont oder Submodule). Kein separates Repo — ein Clone = Struktur-Parser + Laufzeit-Engines.

**Neue Planungs-Artefakte** (Taxonomie, Coverage-Matrix, Projektplan): immer unter `projects/inner_compass/` anlegen (reference/ oder eigener Ordner `meta/`), **nicht** ins Code-Repo legen.

## 9. Schlüsselentscheidungen (Kurzform)

- **Postgres statt ArangoDB**: Supabase-Ökosystem, pgvector reicht für unsere Größenordnung.
- **Strukturbäume aus Deskriptoren, NICHT aus PDFs**: Struktur ist deterministisch.
- **Embeddings für Cross-System-Mapping**: Kein manuelles Kuratieren nötig.
- **4-stufige Extraktion statt ein LLM-Call**: Verschiedene Wissensebenen brauchen fokussierte Prompts.
- **jsonb statt feste Spalten**: Dimensions erweiterbar ohne Migration.
- **system-Feld überall**: Multi-System von Anfang an.

## 10. Operatives: Local vs. Cloud Guardrails

**Grundregel:** Control Plane ist genau EINE Supabase-Instanz pro Umgebung. Alles was Jobs erzeugt und verarbeitet muss auf dieselbe Instanz zeigen.

| Komponente | Lokal (Dev) | Cloud (E2E) | Zeigt auf |
|-----------|-------------|-------------|-----------|
| Web UI | ✅ | ✅ | Die Instanz deren Jobs du sehen willst |
| Worker (Spark) | optional | ✅ typisch | **Cloud** (Control Plane) |
| Uploader | optional | ✅ typisch | **Cloud** (damit Worker Jobs sieht) |

**Typische Fehler:**
- "Worker sieht keine Jobs" → UI schreibt lokal, Worker pollt Cloud. Fix: gleiche Instanz.
- "Cloud fehlen Tabellen" → `supabase db push` vergessen.
- "Jobs hängen auf running" → Worker abgestürzt. Fix: Job auf queued zurücksetzen.

## 11. Migration: hd_* → sys_*

Aufwand: ~2-3 Tage. EINE Migration statt 10 Patches.

Was sich NICHT ändert: Spark/Worker, MinerU, LLM-Prompts, systemd Services, Supabase-Instanz.
Was sich ändert: Tabellennamen, +pgvector, +system/edge_scope/review_status Felder.

Vollständiges SQL: siehe `reference/decisions.md` → Clean Restart Sektion.
