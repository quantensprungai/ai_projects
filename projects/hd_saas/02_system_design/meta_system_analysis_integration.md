# Meta-System-Analyse: Integration & Abgleich

<!--
last_update: 2026-02-13
status: living doc
scope:
  summary: "Abgleich externer KI-Analyse (Meta-System, Staffeln, Architektur) mit aktuellem Projektstand. Entscheidungsmatrix: was übernehmen, was zurückstellen, was diskutieren."
notes:
  - "Quelle: Externe KI-Ausarbeitung (3 Teile + Clean Restart). Projektstand: current_status_local_dev.md, next_steps_was_fehlt_noch.md, Handover."
-->

## 1. Kurzüberblick

Eine separate KI hat eine umfangreiche Meta-System-Analyse erstellt (Idee, Architektur, Schema, Extraktion, Staffeln, Engines, Clean Restart). Dieses Dokument gleicht die Analyse mit dem **aktuellen Projektstand** ab und gibt konkrete Empfehlungen.

---

## 2. Abgleich: Analyse vs. Projekt

### 2.1 Was übereinstimmt

| Thema | Analyse | Projekt | Status |
|-------|---------|---------|--------|
| **Option B (Daten zuerst)** | Backend vor UI, KG vollständig | plan_option_b_roadmap.md, next_steps | ✅ |
| **Interpretations-Contract** | essence, mechanics, dimensions, interactions | interpretations_contract.md | ✅ |
| **Dimensions (12 Keys)** | Core + Layer | dimensions_contract.md | ✅ |
| **Relation Types** | part_of, amplifies, depends_on, maps_to | erkenntnisse_und_fuer_spaeter.md, text2kg_spec | ✅ |
| **Edges vs. Dynamics vs. Interactions** | Klare Trennung | text2kg_spec §1 | ✅ |
| **Multi-System** | system-Feld, sys_* oder hd_* | hd_interpretations.system, Descriptoren | ✅ |
| **MinerU, Spark, Supabase** | Tech Stack | current_status_local_dev | ✅ |
| **Staffel 1 (4 Systeme)** | HD, BaZi, Astro, Maya | Descriptoren existieren (9 Systeme) | ✅ |
| **Chart Engines** | hdkit, alvamind, pyswisseph, tzolkin | app_picture_and_user_journey.md | ✅ |
| **Story / Human-first** | Muster statt Mechanik | ui_ux_principles_and_flow, story_and_mythology | ✅ |

### 2.2 Wo es abweicht

| Thema | Analyse | Projekt | Empfehlung |
|-------|---------|---------|------------|
| **Schema-Namen** | sys_* (Clean Restart) | hd_* (13 Tabellen) | **Zurückstellen.** Erst KG-Edges + pgvector im bestehenden Schema. Umbenennung später, wenn Multi-System produktiv. |
| **Extraktion** | 4 Schritte: entities, meanings, triples, processes | 1 Schritt: extract_interpretations | **Erweitern, nicht ersetzen.** payload.relations ergänzen (wie geplant), extract_dynamics separat. Kein Big Bang. |
| **Embeddings** | Fundamental, pgvector sofort | Nicht vorhanden | **Priorisieren.** Nach KG-Edges: pgvector + embedding-Spalte. Cross-System-Mapping braucht das. |
| **Strukturbäume** | Phase 0, aus Deskriptoren, VOR PDFs | Nicht in Descriptoren | **Phase 2.** Erst Edges aus Interpretationen. Strukturbäume wenn BaZi/Astro in Pipeline. |
| **Dimensions +3** | elemental_quality, temporal_phase, destiny_pattern | 12 Keys | **Optional ergänzen.** jsonb erlaubt das ohne Migration. Bei BaZi-Extraktion prüfen. |
| **NVIDIA Triple-Extraktion** | Direkte (S,P,O)-Extraktion | Interpretation → Node | **Behalten.** Unser Ansatz ist Interpretation-zentriert; Triples kommen aus payload.relations. |

### 2.3 Was das Projekt hat, die Analyse nicht kennt

- **Term-Mapping** (extract_term_mapping): Seed-basiert, canonical_id-Lookup vor text2kg
- **classify_domain**: system = hd/bazi/mixed/other
- **synthesize_node**: 4 Styles (natural, coaching, poetic, technical), hd_synthesis_wordings
- **Zwei-Phasen-Betrieb**: HD_WORKER_JOB_TYPES auf VM102
- **9 System-Deskriptoren**: hd, bazi, astro, jyotish, mayan_tzolkin, genekeys, enneagram, numerology, nine_star_ki, akan

---

## 3. Entscheidungsmatrix

### Sofort übernehmen (kein Konflikt)

1. **Embeddings als nächster großer Schritt** — Nach KG-Edges: pgvector + embedding-Spalte auf hd_kg_nodes
2. **Cross-System-Mapping via Embeddings + LLM** — Kein manuelles Kuratieren; Kandidaten mit Similarity > 0.75 → LLM-Validierung
3. **Meta-Knoten aus Clustering** — Emergent, nicht vorab definiert
4. **Strukturbäume in Deskriptoren** — Wenn BaZi/Astro in Pipeline; aus Engines/JSON, nicht aus PDFs
5. **Jyotish als Stress-Test** — Staffel 1 Welle 2 (4 Wochen nach Launch)

### Erweitern (nicht ersetzen)

1. **payload.relations** — Wie geplant: LLM liefert Relations, text2kg schreibt Edges. Analyse schlägt extract_triples vor; wir haben das bereits als Konzept (text2kg_spec §4.2).
2. **Dimensions +3** — elemental_quality, temporal_phase, destiny_pattern als optionale Keys (nullable) in dimensions_contract; bei BaZi-Extraktion validieren
3. **extract_dynamics** — dynamic_types (phase_cycle, trap, growth_path, spectrum) wie in Analyse; Prompts pro Typ

### Zurückstellen

1. **Clean Restart (sys_*)** — 2–3 Tage Aufwand, kein unmittelbarer Nutzen. Erst wenn Multi-System produktiv. Aktuell: ADD COLUMN (system, embedding, edge_scope) im bestehenden Schema.
2. **4-stufige Extraktion** — entities, meanings, triples, processes als separate Jobs. Zu großer Umbau. Stattdessen: extract_interpretations um payload.relations erweitern; extract_dynamics als eigener Job.
3. **Vollständige Strukturbäume vor Phase 1** — HD ist bereits in Pipeline. Strukturbäume wenn BaZi/Astro dazukommen.

### Diskutieren

1. **hd_documents vs. hd_assets** — Analyse: konsolidieren. Projekt: hd_assets = Knowledge Pipeline, hd_documents = Upload. Klar dokumentieren; Konsolidierung später.
2. **hd_interactions vs. hd_kg_edges** — Analyse: Hyperedge vs. binäre Edge. Projekt: interactions bleiben in node.metadata + hd_interactions; Edges für part_of, amplifies, maps_to. Abgrenzung beibehalten.

---

## 4. Konkrete nächste Schritte (aktualisiert)

Reihenfolge bleibt **Option B**, aber mit Einarbeitung der Analyse:

| # | Schritt | Quelle | Hinweis |
|---|---------|--------|---------|
| 1 | **KG-Edges** — payload.relations + text2kg | next_steps, text2kg_spec | Schema bereit. LLM-Prompt um Relations erweitern. |
| 2 | **pgvector + Embedding** | Analyse | Migration: ADD COLUMN embedding vector(1536). Nach Synthesis: Embedding pro Node. |
| 3 | **extract_dynamics** | next_steps, Analyse | dynamic_types: phase_cycle, trap, growth_path, spectrum. |
| 4 | **extract_interactions** (optional) | next_steps | payload.interactions → hd_interactions, wenn Tabelle/Contract stehen. |
| 5 | **Schema-Erweiterungen** (ADD COLUMN) | Analyse Teil 23 | system auf hd_kg_nodes, edge_scope auf hd_kg_edges, review_status. Kein Restart. |
| 6 | **Strukturbäume in Deskriptoren** | Analyse | Wenn BaZi/Astro in Pipeline. hd.json: structure (Centers→Gates, Channels). |
| 7 | **Cross-System-Mapping Job** | Analyse | Nach Embeddings: Similarity + LLM-Validation → maps_to Edges. |
| 8 | **UI/UX Insight Engine** | next_steps | KG + Synthesis in App. |
| 9 | **Sprache aus App** | next_steps | debug.language beim Job-Anlegen. |

---

## 5. Wo die Analyse-Dokumente liegen

Die externe Analyse umfasst:

- **Teil 1** — Idee, Meta-System, Architektur, Schema, Story, Tech Stack
- **Teil 2** — Systemauswahl, Engines, Staffeln, Strukturbäume, Dimensions, Cross-System
- **Teil 3** — Extraktion (4 Ebenen), Embeddings, NVIDIA-Vergleich, Schema-Review, Clean Restart
- **Clean Restart** — sys_*-Tabellen, 10-Tabellen-Schema, Migration-Entwurf

**Empfehlung:** Die Analyse als Referenz in `projects/hd_saas/02_system_design/` ablegen (z.B. `meta_system_analysis_external.md` oder in 99_archive). Dieses Dokument (`meta_system_analysis_integration.md`) ist die **einzige Projekt-Referenz** — es fasst die Entscheidungen zusammen und verweist auf die Analyse bei Bedarf.

---

## 6. Referenzen

- **Projektstand:** current_status_local_dev.md, next_steps_was_fehlt_noch.md
- **Contracts:** dimensions_contract.md, interpretations_contract.md, text2kg_spec.md
- **Erkenntnisse:** erkenntnisse_und_fuer_spaeter.md
- **Plan:** plan_option_b_roadmap.md
