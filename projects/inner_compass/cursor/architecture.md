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
| Chart-Engines (TS) | hdkit (JS/MIT), alvamind (TS/MIT), @swisseph/node (AGPL/Komm.) |
| Chart-Engines (Python) | VedAstro.Python (MIT), jyotishganit (MIT), pyswisseph (AGPL/Komm.), tzolkin-calendar (MIT) |
| Embeddings | text-embedding-3-large oder lokales Modell, in pgvector |
| VPN | Tailscale (Spark ↔ Supabase ↔ Dev) |

## 6. Infrastruktur-Topologie

```
[Spark / DGX]                          [Supabase Cloud]
├── MinerU (PDF-Parsing, GPU)          ├── Postgres + pgvector
├── SGLang/vLLM (LLM-Inferenz)        ├── Auth + RLS
├── Python Worker (systemd)            ├── Storage (PDFs)
├── Embedding Model                    └── Realtime (optional)
└── (KEIN Chart-Engine-Service hier)
        ↕ Tailscale VPN ↕
[Dev Machine / Vercel / App-Host]
├── Next.js App (Makerkit)
│     ├── TS-Engines: hdkit, alvamind, @swisseph/node
│     └── API Routes: HD, BaZi, Maya, Numerologie, NSK, Akan
├── Python Microservice (Docker, FastAPI)
│     ├── VedAstro.Python / jyotishganit → Jyotish
│     ├── pyswisseph + immanuel → Westl. Astrologie
│     └── Transit-Service (aktuelle Positionen)
├── Supabase Local (Dev)
└── ai_projects/ (Docs+Infra)
```

**Änderung (2026-04):** Chart-Engines laufen NICHT auf Spark. Spark = nur GPU-Tasks (MinerU, LLM). Engines sind CPU-leicht (~10ms). TS-Engines direkt in Next.js; Python-Engines in eigenem Microservice. → engines.md §4

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

**Konkret für das Code-Repo (inner_compass_app):**

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

## 12. User Data Model (NEU — aus Gesamtinventur v0.5)

Neben dem sys_*-Schema (KG-Wissen) braucht IC ein User-Schema für persönliche Daten.

### User-Tabellen

```sql
-- Personen (ICH + Partner/Familie)
user_persons (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  account_id uuid REFERENCES accounts(id),
  role text NOT NULL DEFAULT 'self',  -- contracts.md §12: person_role
  label text,                          -- "Anna", "Mama", frei wählbar
  birth_date date NOT NULL,
  birth_time time,                     -- nullable (weniger präzise Charts)
  birth_place text,                    -- nullable
  birth_lat numeric,
  birth_lng numeric,
  full_name text,                      -- für Numerologie/Gematria
  created_at timestamptz DEFAULT now()
);

-- Berechnete Charts pro Person pro System (JSONB)
user_charts (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  person_id uuid REFERENCES user_persons(id),
  system_id text NOT NULL,             -- 'hd' | 'bazi' | 'astro' | ...
  chart_data jsonb NOT NULL,           -- System-spezifisch: Gates, Stems, Planets, ...
  computed_at timestamptz DEFAULT now(),
  engine_version text                  -- Versionierung der Berechnung
);

-- Beziehungen zwischen Personen (v2)
user_relationships (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  person_a_id uuid REFERENCES user_persons(id),
  person_b_id uuid REFERENCES user_persons(id),
  relationship_type text NOT NULL,     -- 'partner' | 'parent_child' | 'friends' | ...
  created_at timestamptz DEFAULT now()
);

-- Relationship-Charts (v2: Composite, Synastry)
user_relationship_charts (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  relationship_id uuid REFERENCES user_relationships(id),
  chart_type text NOT NULL,            -- contracts.md §12: relationship_chart_type
  system_id text NOT NULL,
  chart_data jsonb NOT NULL,
  computed_at timestamptz DEFAULT now()
);

-- Fortschritt pro Domäne
user_progress (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  person_id uuid REFERENCES user_persons(id),
  domain text NOT NULL,                -- contracts.md §2: life_domain enum
  phase integer DEFAULT 1,             -- 1–7 (User-Phasen)
  brunnen_depth integer,               -- 1–4 (aktuelle Brunnen-Schicht, null = nicht aktiv)
  leiter_stufe integer,                -- 1–5 (aktuelle Leiter-Stufe, null = nicht aktiv)
  active_theme text,                   -- Freitext: aktuelles Arbeitsthema
  updated_at timestamptz DEFAULT now()
);

-- Sessions (Anker, Brunnen→Leiter Flows)
user_sessions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  person_id uuid REFERENCES user_persons(id),
  session_type text NOT NULL,          -- 'anker' | 'brunnen_leiter' | 'reflexion'
  domain text,                         -- Zugehöriger Lebensbereich
  state jsonb NOT NULL DEFAULT '{}',   -- Flow-Zustand (aktueller Schritt, Ergebnisse)
  started_at timestamptz DEFAULT now(),
  completed_at timestamptz             -- null = laufend
);

-- Reflexions-Texte (für NLP, v2)
user_reflections (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  person_id uuid REFERENCES user_persons(id),
  session_id uuid REFERENCES user_sessions(id),
  reflection_type text NOT NULL,       -- 'narrativ_frage' | 'brunnen_reflexion' | 'traum' | 'frei'
  content text NOT NULL,
  nlp_result jsonb,                    -- KI-Analyse-Ergebnis (EG-Cluster, Phase, Emotion)
  created_at timestamptz DEFAULT now()
);
```

### Prinzipien

- **user_persons statt user_profile:** Von Anfang an Multi-Person (ICH + Partner + Familie). Jede Person hat eigene Charts.
- **chart_data als JSONB:** Jedes System hat andere Datenstrukturen. JSONB ist flexibel genug. Kein ORM für Chart-Daten.
- **user_progress pro Domäne:** Ein User kann in Beruf bei Phase 5 und Liebe bei Phase 2 sein. Nicht-linear.
- **user_sessions sind unterbrechbar:** Brunnen→Leiter-Flows können über Tage dauern. State wird in JSONB gespeichert.
- **RLS:** Alle user_*-Tabellen mit RLS (account_id Check). user_persons.account_id als Filterbasis.

## 13. Echtzeit-Services (NEU — neben Batch-Worker)

Der bestehende Worker (ic_worker.py) verarbeitet PDFs im Batch. Daneben braucht IC Echtzeit-Services:

```
BATCH (bestehend)                    ECHTZEIT (neu)
PDF-Pipeline auf Spark               Chart-Engine-Service
  extract → classify → interpret       Geburtsdaten → Charts (alle Systeme)
  → text2kg → synthesize               Einmalig pro Person bei Onboarding
  → cross_mapping → meta_nodes
                                     Transit-Service
                                       Aktuelle Positionen → aktive Elemente
                                       15-Min-Cache, pyswisseph

                                     Overlay-Service
                                       Statisch × Transit × KG → Text
                                       LLM on-demand oder Template

                                     Konvergenz-Service
                                       Cross-Edges + Transite → Highlights
                                       15-Min-Cache, deterministisch

                                     Flow-Engine
                                       Brunnen/Leiter State Machine
                                       JSONB in user_sessions

                                     NLP-Service (v2)
                                       User-Text → EG/Phase/Emotion
                                       LLM on-demand
```

### Wo laufen die Services?

| Service | Wo | Warum |
|---------|-----|-------|
| Chart-Engine (HD, BaZi, Maya, Num, NSK, Akan) | Next.js API Routes | TS-Engines laufen direkt in Node |
| Chart-Engine (Jyotish, Astro) | Python Microservice (FastAPI, Docker) | VedAstro.Python / pyswisseph brauchen Python. NICHT auf Spark. |
| Transit-Service | Python Microservice | pyswisseph, 15-Min-Cache |
| Overlay-Service | Spark (LLM) | Braucht LLM-Zugang |
| Konvergenz-Service | Supabase Edge oder Next.js | Deterministisch, SQL-basiert |
| Flow-Engine | Next.js API Routes | State-Management, kein LLM nötig |
| NLP-Service | Spark (LLM) | Braucht LLM-Zugang |

## 14. App-Architektur: 4 Spaces (NEU)

### Space-Struktur

```
JETZT (space_now)         — Home / Personalisierter Radar
KARTE (space_map)         — Erkunden / Mandala / Charts
WERKSTATT (space_workshop) — Vertiefen / Brunnen→Leiter
ZEIT (space_time)          — Timing / Transite / Zyklen
```

Namen sind Arbeitstitel (→ contracts.md §11). Interne IDs (`space_*`) sind stabil.

### Datenfluss pro Space

```
JETZT
  Transit-Service → aktive Transite (Top 1–3)
  Konvergenz-Service → Highlights ("3 Systeme zeigen auf Liebe")
  user_progress → offene Arbeit, Phase-Fortschritt
  → Personalisierte Startseite

KARTE
  user_charts → Chart-Daten pro System
  sys_kg_nodes → Interpretationen pro Element
  sys_synthesis_wordings → Personalisierte Texte (Tiefe 1–2)
  → 3 View-Ebenen:
    1. IC Mandala (12 Domänen, 3 Ringe, Phase-Indikatoren)
    2. System-Charts (BodyGraph, Geburtsrad, BaZi-Säulen, Maya-Kin)
    3. Rohdaten (Tabelle aller Chart-Elemente)
  → Lens-Switcher: Synthese (Default) / Einzelsystem
  → WIR-Modus (v2): Umschalter ICH/WIR mit Personenauswahl

WERKSTATT
  user_progress → aktives Thema, aktuelle Phase/Domäne
  sys_dynamics (traps) → Pattern Trap Detection
  Flow-Engine → Brunnen→Leiter State Machine:
    1. Thema wählen (aus KARTE oder JETZT)
    2. Brunnen-Abstieg (Schicht 1→2→Gate→3→4→Schwelle)
    3. Anker (5 Komponenten, v2: Focusing-erweitert)
    4. Leiter-Aufstieg (Sehen→Fühlen→Verstehen→Handeln→Ernten)
    5. Experiment (konkretes Verhalten)
  user_sessions → Fortschritt speichern (unterbrechbar)

ZEIT
  Transit-Service → aktive Transite (alle Systeme)
  sys_dynamics (phase_cycle) → Langfrist-Zyklen
  Konvergenz-Service → Konvergenz-Highlights
  → Timeline-Visualisierung
  → Klick → KARTE (Domäne) oder WERKSTATT (wenn Trap aktiv)
```

### Chart-Visualisierungen

Pro System eine eigene Render-Komponente in KARTE (System-Charts View):

| System | Komponente | Komplexität | Technologie | Version |
|--------|------------|-------------|-------------|---------|
| **IC Mandala** | `<IcMandala />` | Hoch | SVG/Canvas, Eigenentwicklung | v1 |
| **HD BodyGraph** | `<HdBodygraph />` | Hoch | SVG, basierend auf hdkit Sample-App | v1 |
| **Astro Wheel** | `<AstroWheel />` | Hoch | SVG, Open-Source-Renderer (astrochart.js o.ä.) | v1 |
| **BaZi Pillars** | `<BaziPillars />` | Niedrig | HTML/CSS Tabelle | v1 |
| **Maya Kin** | `<MayaKin />` | Niedrig | HTML/CSS Karte | v1 |
| **Ziwei Doushu** | `<ZiweiChart />` | Mittel | SVG 12-Paläste-Gitter (iztro-hook) | v1 |
| **Jyotish Rasi** | `<JyotishChart />` | Mittel | SVG Quadrat-Chart | v2 |
| **Gene Keys Profile** | `<GeneKeysProfile />` | Mittel | SVG Sphären-Diagramm | v2 |
| **Numerologie** | `<NumerologyProfile />` | Niedrig | HTML/CSS | v1 |

Alle Komponenten erhalten `chart_data` (JSONB aus user_charts) als Prop. Kein KG-Zugriff in der Visualisierung — nur Rohdaten aus der Engine.

### Frontend-Routing (Next.js App Router)

```
/app
  /jetzt              → JETZT (Home)
  /karte              → KARTE
    /karte/mandala    → IC Mandala
    /karte/[system]   → System-Chart (hd, astro, bazi, maya, ...)
    /karte/rohdaten   → Rohdaten-Tabelle
    /karte/[domain]   → Domänen-Detail (Handbuch Tiefe 1–4)
  /werkstatt          → WERKSTATT
    /werkstatt/[id]   → Aktiver Brunnen→Leiter-Flow
    /werkstatt/anker  → Anker (standalone oder embedded)
  /zeit               → ZEIT (Timeline)
  /einstellungen      → Settings, Profil, Personen-Management
  /onboarding         → Onboarding-Flow (Geburtsdaten → erster Chart)
```

### Onboarding-Flow

```
1. Geburtsdaten eingeben (Datum + Zeit + Ort + Name)
2. Chart-Engine-Service: alle Engines parallel → user_charts
3. Erster "Aha-Moment": Top-3 Insights aus Chart
4. Mandala zeigen (12 Domänen, erste Befüllung)
5. Optional: Narrativ-Frage ("Was beschäftigt dich gerade am meisten?")
6. → JETZT (Home)
```

## 15. KG-Übereinanderlegen & IC-Sprache (NEU)

### Kernprinzip

Der KG besteht aus vielen einzelnen Netzen — eines pro System. Jedes System (HD, Jyotish, BaZi, I Ging, Kabbalah, ...) hat seine eigenen Knoten und Kanten. Die bestehenden 5 Datenschichten (A–E) bleiben die technische Architektur. Dieses Kapitel beschreibt, wie aus dem Übereinanderlegen aller Netze die **IC-eigene Sprache** entsteht.

### Zwei Arten von Systemen

In `sys_systems` wird ein neues Feld `system_role` eingeführt:

| Rolle | Bedeutung | Beispiele |
|-------|-----------|----------|
| `calculation` | Berechnet personalisierte Charts aus Geburtsdaten | HD, Jyotish, BaZi, Ziwei, Westl. Astro, Maya |
| `structural` | Beschreibt das Terrain, berechnet nichts | I Ging, Kabbalah, Chakras, Enneagramm |

Kein System steht hierarchisch über einem anderen. Struktursysteme sind zusätzliche Netze, die das Bild reicher machen. Die Verbindungen zwischen Systemen werden als reguläre `cross_system`-Edges modelliert.

### Wie die Netze übereinandergelegt werden

Jedes System ist ein eigenes Netz im KG. Die Cross-System-Phase (Datenschicht D, Phase 3) legt alle Netze übereinander und findet Klumpen — Stellen, wo Knoten aus verschiedenen Systemen semantisch eng beieinanderliegen.

```
HD-Netz:        Gate 34 ——— Sakral ——— Generator
Jyotish-Netz:   Mars ——— Widder ——— 1. Haus
BaZi-Netz:      Yang-Feuer ——— Frühling ——— Holz nährt Feuer
Ziwei-Netz:     Greedy Wolf ——— Karriere-Palast
I-Ging-Netz:    Hex 34 ——— Donner unter Himmel ——— Große Stärke

Cross-System-Mapping (K4-Embeddings):
  Gate 34      ↔ Mars         (Similarity: 0.82)
  Mars         ↔ Yang-Feuer   (Similarity: 0.78)
  Yang-Feuer   ↔ Greedy Wolf  (Similarity: 0.75)
  Gate 34      ↔ Hex 34       (is_based_on, faktisch)
  → Klumpen identifiziert: 5 Knoten aus 5 Systemen
```

Das Mapping läuft über **K4-Interpretationen** (semantische Ähnlichkeit der Bedeutungstexte) und **K1-K2-Strukturverbindungen** (faktische Identitäten wie HD Gate = I Ging Hex).

### Wie die IC-Sprache entsteht (Datenschicht E)

Aus den Klumpen werden **IC-Konzepte** destilliert — eine eigene Sprache, die den kulturübergreifenden Kern trifft. Nicht "4 Systeme sagen etwas Ähnliches" (das wäre Statistik), sondern ein **eigenes Wort** für das, was unter den kulturellen Färbungen liegt.

```
Phase 4 — IC-Sprache generieren:

  Input an LLM (alle Interpretationen eines Klumpens):
    "HD: 'rohe sakrale Kraft, wartet auf Reaktion'
     Jyotish: 'Mars — Mut, Aggression, Initiierung'
     BaZi: 'Yang-Feuer — Expansion, Ambition'
     Ziwei: 'Greedy Wolf — Antrieb, Charisma, Unruhe'
     I Ging: 'Hex 34 — Große Stärke, Donner unter Himmel'"

  Auftrag: "Was ist der gemeinsame Kern, der UNTER
    den kulturellen Färbungen liegt? Benenne ihn."

  → IC-Konzept: "Verkörperte Initialkraft"
  → Definition: "Die angeborene Kapazität,
     Energie in Handlung umzusetzen."

  Human Review → sys_kg_nodes (system='meta')
```

Jede Tradition sieht einen Aspekt (Mars/Kraft/Feuer/Ehrgeiz). Die IC-Sprache versucht, das zu benennen was **darunter** liegt — die Mitte aller Versuche, dasselbe zu beschreiben.

### Ausgabe an den User

Die IC-Sprache ist die **Hauptstimme**. Die Systeme sind die Quellenangaben — sichtbar für die, die tiefer wollen:

```
"VERKÖRPERTE INITIALKRAFT
 Das ist ein zentrales Thema deiner Signatur.

 [Quellen →]
   HD: Gate 34 — sakrale Kraft
   Jyotish: Mars in Widder — Mut & Antrieb
   BaZi: Yang-Feuer — Expansion
   Ziwei: Greedy Wolf — Ehrgeiz & Charisma

 [Spannungsfeld →]
   HD empfiehlt: Warte auf die sakrale Reaktion
   Jyotish empfiehlt: Handle mutig und sofort
   → Diese Spannung ist selbst eine Information"
```

Divergenzen (verschiedene Empfehlungen trotz gleichen Themas) werden nicht versteckt, sondern als eigene Erkenntnisquelle gezeigt.

### Was das für individuelle Charts bedeutet

```
User gibt Geburtsdaten ein
  ↓
Engines berechnen parallel (pro Berechnungssystem):
  HD: Gate 34 aktiv, Sakral definiert
  Jyotish: Mars in Widder, 1. Haus
  BaZi: Yang-Feuer Tagesstamm
  Ziwei: Greedy Wolf im Karriere-Palast
  ↓
Aktive Knoten identifizieren:
  hd.gate.34, jyotish.graha.mars_in_aries,
  bazi.stem.yang_fire, ziwei.star.greedy_wolf
  ↓
Meta-Knoten prüfen:
  Welche IC-Konzepte werden von MEHREREN aktiven Knoten getroffen?
  meta.verkörperte_initialkraft: 4/5 Systeme treffen → starkes Signal
  meta.emotionale_tiefe: 0/5 → kein Signal
  ↓
IC-Profil zusammenstellen:
  Starke Themen (3+ Systeme): "Verkörperte Initialkraft", ...
  Einzelsystem-Aussagen: pro System die eigene Sprache
  Spannungsfelder: wo Systeme divergieren
```

→ Details zu Engines und Kits: engines.md §13
