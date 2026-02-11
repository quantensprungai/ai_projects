# text2kg – Interpretations → Knowledge Graph (Spec)

<!--
last_update: 2026-02-10
status: draft (v2 nach HILOG-Abgleich)
scope:
  summary: "Spezifikation des Jobs text2kg: Input (Interpretations + Term-Mapping), Output (hd_kg_nodes, hd_kg_edges), Mapping-Logik, Idempotenz, Multi-System."
  in_scope:
    - Input/Output, DB-Schema-Referenz
    - Node-/Edge-Erzeugung aus payload und element_*
    - Relationstypen, Abgrenzung zu Dynamics/Interactions
    - Dimensions in metadata, Interactions nicht als Edges, canonical_description leer, Term-Mapping Pflicht
  out_of_scope:
    - Implementierung im Worker (folgt später)
    - extract_dynamics, Synthesis
notes:
  - "Abgestimmt mit HILOG-System-Design, Layer-Modell; Korrekturen aus Analyse 2026-02-10 eingearbeitet."
  - "NVIDIA txt2kg-Playbook kann optional als Visualisierung/GraphRAG-Sidecar genutzt werden; Kern-Pipeline bleibt Supabase (Interpretations → Nodes/Edges)."
  - "Pipeline-Stand: Interpretations + Dimensions + System-Descriptor (9 Systeme, Seed-Skript) abgeschlossen. text2kg nutzt Descriptor (node_type aus kg_rules.node_types, node_key-Prefix aus canonical_prefix); Edges später. Nächste Schritte: Synthesis, Dynamics, UI/UX."
-->

Diese Spec beschreibt den **text2kg**-Job: Aus **hd_interpretations** und **hd_term_mapping** werden **hd_kg_nodes** und **hd_kg_edges** befüllt. **Term-Mapping ist Pflicht vor text2kg** (Pipeline: extract_interpretations → extract_term_mapping → text2kg), damit stabile canonical_id-basierte Node Keys entstehen. Ein externes „NVIDIA txt2kg“-Playbook kann **optional** als Visualisierung/GraphRAG-Sidecar eingesetzt werden, ersetzt aber **nicht** unsere Kern-Pipeline in Supabase.

## 1) Zweck und Abgrenzung

- **Zweck:** Strukturierte, abfragbare Wissenseinheiten (Knoten) und semantische Beziehungen (Kanten) erzeugen, die aus den bereits extrahierten Interpretations-Payloads ableitbar sind. Der Graph dient Navigation, Query und später Synthesis – nicht der Speicherung von Prozesslogik (dafür **hd_dynamics**) oder von Interaktionsmustern als eigenständige Objekte (dafür **hd_interactions**).
- **Abgrenzung (laut layers_overview):**
  - **KG-Edges** = „dauerhafte“ semantische Relationen: `part_of`, `depends_on`, `amplifies`, `maps_to`, … (zeitlos, erklärend).
  - **Dynamics** = Phasen/Traps/Growth Paths, Zustandswechsel → **nicht** als Kanten modellieren.
  - **Interactions** = Pattern/Regelsets (Typ/Profil/Zentren/Authority) → **dürfen niemals** als KG-Edges abgebildet werden; nur in node.metadata.interactions bzw. in **hd_interactions**.

## 2) Input

| Quelle | Verwendung |
|--------|------------|
| **public.hd_interpretations** | Primärer Input. Pro Zeile: `id`, `account_id`, `chunk_id`, `system`, `element_type`, `element_id`, `payload` (jsonb). |
| **public.hd_term_mapping** (Pflicht) | Liefert `canonical_id` zu Begriffen/Synonymen. **text2kg setzt voraus, dass extract_term_mapping vorher gelaufen ist**, damit Node Keys stabil und schulübergreifend normalisiert sind (keine Duplikate wie „Manifestor“ / „Initiator“ / „Firestarter“ als getrennte Nodes). |

Relevante Felder im **payload** (vgl. `interpretations_contract.md`):

- **Core:** `essence`, `mechanics`, `expression`, `challenges`, `growth`, `source`
- **dimensions:** Objekt mit allen Keys aus **dimensions_contract.md** (Core: mechanical, psychological, somatic, social, shadow, gift, role, archetype; Layer: body_mechanics, environment, relationship_pattern, projection_field; Werte string oder null)
- **interactions:** `with_centers`, `with_profile`, `with_authority` (Arrays)
- **evidence:** z. B. `chunk_id`, `quotes`, `source_ref`

## 3) Output (DB-Schema)

Tabellen existieren bereits (Migration `20260119165000_hd_knowledge_core.sql`):

### hd_kg_nodes

| Spalte | Typ | Bedeutung |
|--------|-----|-----------|
| id | uuid | PK |
| account_id | uuid | Tenant, NOT NULL |
| node_key | text | Eindeutiger logischer Schlüssel pro Account, z. B. `{system}.{element_type}.{element_id}` |
| node_type | text | Kategorie: z. B. Gate, Line, Profile, Type, Authority, Day_Master, … |
| canonical_description | text | **Immer leer lassen.** Synthesis-Job (`synthesize_node`) füllt ihn später. Nicht aus `essence` ableiten – essence ist Interpretation, canonical_description ist struktureller Fachkanon. |
| metadata | jsonb | **MUST:** `interpretation_ids[]`, `chunk_ids[]`, `source`, **`dimensions`**, **`interactions`**. **Dimensions MUST be written into node.metadata.dimensions** (vollständig aus payload.dimensions). Interactions MUST be written into node.metadata.interactions (nicht als Edges). Ohne dimensions in metadata wären Query, Synthesis und state detection nicht möglich. Optional: `first_essence_snippet`. |

**Unique:** `(account_id, node_key)`.

### hd_kg_edges

| Spalte | Typ | Bedeutung |
|--------|-----|-----------|
| id | uuid | PK |
| account_id | uuid | Tenant |
| from_node_id | uuid | FK → hd_kg_nodes |
| to_node_id | uuid | FK → hd_kg_nodes |
| relation_type | text | Semantischer Typ der Kante (s. u.) |
| strength | text | z. B. low \| medium \| strong \| dominant (Default: medium) |
| metadata | jsonb | Optional: Herkunft (interpretation_id, dimension_slot), Zitate |

Kein Unique-Constraint auf (from, to, relation_type) in der Migration – bei Implementierung entweder DB-Constraint ergänzen oder im Job deduplizieren (Upsert-Logik).

## 4) Mapping-Logik

### 4.1 Knoten (Nodes)

- **Eine Zeile hd_interpretations** → mindestens **ein** Knoten.
- **node_key:** Deterministisch aus **canonical_id** (hd_term_mapping), falls vorhanden; sonst Fallback `{system}.{element_type}.{element_id}`. **system** immer einbeziehen (Multi-System).
- **node_type:** Aus `element_type` normalisiert (z. B. Gate, Line, Profile, Type, Day_Master, …). Pro System konsistent.
- **canonical_description:** **Immer leer lassen.** Darf nicht aus `payload.essence` generiert werden (essence = Interpretation; canonical_description = struktureller Kanon, kommt aus Synthesis).
- **metadata:** Muss enthalten: `interpretation_ids`, `chunk_ids`, `source`, **`dimensions`** (vollständig `payload.dimensions`), **`interactions`** (vollständig `payload.interactions`). So bleiben Dimensions und Interactions auffindbar für Query, Synthesis und spätere hd_interactions-Migration; sie werden **nicht** als KG-Edges abgebildet.

**Idempotenz:** Upsert auf `(account_id, node_key)`. Bei erneutem Lauf: Node laden, `updated_at` und `metadata` aktualisieren (inkl. dimensions/interactions); `canonical_description` **nicht** überschreiben (bleibt leer bis Synthesis).

### 4.2 Kanten (Edges)

Kanten entstehen **nur** aus **strukturellen** Beziehungen. Keine Prozesslogik, keine Soziallogik als Kanten.

- **Dimensions:** Erzeugen **keine** Edges. Dimensions-Inhalte werden ausschließlich in **node.metadata.dimensions** gespeichert (s. o.). Spätere Erweiterung: „Concept Nodes“ (z. B. `node_type=concept` für Shadow/Gift/Archetype); dann könnten Kanten `expresses_as` von Element-Node zu Concept-Node gelegt werden – **nicht** im MVP.
- **interactions:** `with_centers`, `with_profile`, `with_authority` sind **Soziallogik**, keine Strukturlogik. Sie dürfen **nicht** als semantische KG-Edges gespeichert werden. Stattdessen: **nur** in **node.metadata.interactions** übernehmen. Sobald die Tabelle **hd_interactions** existiert, gehören diese Regeln dorthin; text2kg schreibt sie nicht in `hd_kg_edges`.
- **Explizite Relationen:** Nur wenn später ein Feld `payload.relations: { type, target_canonical_id }[]` definiert wird, daraus echte KG-Edges erzeugen (`part_of`, `depends_on`, `amplifies`, `maps_to`). Keine prozesshaften Typen („triggers“, „leads_to“) → die gehören in Dynamics.

**relation_type (KG nur):** `part_of`, `depends_on`, `amplifies`, `maps_to`. Bewusst beschränkt – Prozesslogik gehört in Dynamics, Soziallogik in metadata.interactions. Kein `references`/`relates_to` aus interactions – diese bleiben in metadata. Siehe erkenntnisse_und_fuer_spaeter.md §1.

**strength (Gewichtung):** Spalte `strength` in hd_kg_edges: `low` | `medium` | `strong` | `dominant` | `overriding` (Default: medium). Wird aus payload.relations übernommen, falls z. B. `relation.strength` oder `relation.weight` geliefert wird. Für HD-Regeln wie „Sonnentor ~70 % Einfluss, Erdentor ~30 %“: entweder strength (strong vs. medium) oder optional **metadata** (z. B. `metadata.influence_score: 0.7`, `metadata.source_planet: "sun"`) – je nachdem, ob ihr quantitativ oder nur qualitativ abbilden wollt.

**Idempotenz:** Pro (from_node_id, to_node_id, relation_type) höchstens eine Kante.

## 5) Job-Parameter und Trigger

- **Job-Typ:** `text2kg` (in `hd_ingestion_jobs.job_type`).
- **Trigger:** Entweder manuell (nach Batch extract_interpretations) oder automatisch nach Abschluss von `extract_interpretations` für ein Asset/Dokument (analog zu classify_domain → extract_term_mapping → extract_interpretations). Genauere Trigger-Logik (pro Asset, pro Dokument, global) in Implementierung festlegen.
- **Input-Scope:** Job-Payload bzw. `debug` könnte z. B. `asset_id`, `document_id` oder „alle Interpretationen eines Accounts“ enthalten. Empfehlung: pro Asset oder pro Dokument, damit Runs begrenzt und wiederholbar sind.

## 6) Multi-System (HD, BaZi, Astro, …)

- **system** aus `hd_interpretations` fließt in **node_key** ein (z. B. `hd.type.generator`, `bazi.day_master.geng`). So kollidieren Begriffe verschiedener Schulen nicht.
- **hd_term_mapping** ist pro `system` und liefert z. B. `canonical_id`; diese ID kann als Basis für `node_key` dienen, sobald Term-Mapping für das Element existiert. Fallback: `system.element_type.element_id` wie oben.

## 7) Abhängigkeiten und Reihenfolge

- **Vor text2kg (Pflicht):** 1) extract_interpretations, 2) **extract_term_mapping**. Term-Mapping muss vor text2kg laufen, damit canonical_id-basierte node_keys entstehen und keine Synonym-Duplikate (z. B. mehrere Nodes für dieselbe Sache).
- **Nach text2kg:** Synthesis (`synthesize_node`) füllt `canonical_description` und canonical_wording; Query/Chat nutzt `hd_kg_nodes` + `hd_kg_edges`. extract_dynamics und hd_interactions (eigene Layer) lesen weiterhin primär Interpretations bzw. metadata.interactions.

## 8) Zukünftige Erweiterung: Concept Nodes

Später können **Konzept-Knoten** (z. B. `node_type=concept` für Shadow, Gift, Archetype) in `hd_kg_nodes` oder einer Tabelle `hd_concepts` modelliert werden. Dann: Dimensions-Werte nicht nur in metadata, sondern als Kanten `expresses_as` von Element-Node zu Concept-Node. **Nicht** im MVP; hier nur dokumentiert, damit die Architektur erweiterbar bleibt.

## 9) Pipeline-Stand & Nächste Schritte

| Schritt | Status | Hinweis |
|--------|--------|---------|
| 1 – Dimensions & Descriptoren finalisieren | ✔ | dimensions_contract, interpretations_contract, Worker-Payload, LLM-Prompt, 9 System-Descriptoren |
| 2 – Descriptoren in public.hd_systems | ✔ | Seed-Skript `seed_hd_systems.py` |
| 3 – text2kg mit Descriptor | ✔ | Worker lädt Descriptor aus hd_systems; node_type aus kg_rules.node_types; node_key-Prefix aus canonical_prefix; allowed_relation_types für spätere Edges vorbereitet |
| 4 – Synthesis | ✔ | Job `synthesize_node` nach text2kg; schreibt `hd_synthesis_wordings` + `hd_kg_nodes.canonical_description`; Stub-Aggregation (essence/mechanics/expression); Styles natural/coaching/poetic/technical; LLM-Erweiterung später |
| 5 – Dynamics-Layer | optional | extract_dynamics, hd_dynamics; Descriptor dynamic_types-Validierung langfristig |
| 6 – UI/UX Insight Engine | geplant | Abfragen, Navigation, Darstellung |

**Multi-Quellen:** Unterschiedliche „Wahrheiten“ aus mehreren Büchern bleiben in hd_interpretations getrennt; text2kg aggregiert in node.metadata (Dimensions/Interactions); Synthesis kann alle Quellen konsolidieren oder quellenspezifisch darstellen. Research-Layer (experimentelle Hypothesen) optional, kein Einfluss auf KG/Synthesis.

---

## 10) Referenzen

- **Interpretations-Contract:** `interpretations_contract.md` (payload, dimensions, downstream „KG nutzt …“).
- **Layer C:** `layers_overview.md` (text2kg als Job, Output hd_kg_nodes/hd_kg_edges, Abgrenzung KG vs Dynamics vs Interactions).
- **Worker-Contract:** `worker_contract_spark_supabase.md` (text2kg Input/Output, tenant-safe, Idempotenz, Laufort Spark).
- **Implementierung:** `hd_worker_mvp.py` (text2kg mit Descriptor-Loading, node_type aus Descriptor, node_key-Prefix); **Worker-Contract:** `worker_contract_system_descriptor.md`.
- **Implementierungsskizze:** `text2kg_implementation_sketch.md` (Pseudo-Code, DB-Queries).
- **Testablauf:** `text2kg_test_procedure.md` (Schritte lokal/Spark, erwartete DB-Inhalte, Option Term-Mapping für node_key).
- **Export-Entwurf:** `export_supabase_to_arangodb.md` (optional: Mapping Supabase → ArangoDB, Skriptskizze für Visualisierung/GraphRAG).
- **Schema:** `code/hd_saas_app/apps/web/supabase/migrations/20260119165000_hd_knowledge_core.sql` (Tabellen hd_kg_nodes, hd_kg_edges).
- **Pipeline-Übersicht:** `language_and_pipeline_overview.md` (Schritt C nach B6 extract_interpretations).
