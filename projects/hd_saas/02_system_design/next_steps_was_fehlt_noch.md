# Wie geht es weiter? Was fehlt noch?

<!-- last_update: 2026-02-10 -->

Kurzer Status: **Was ist fertig**, **was fehlt**, **in welcher Reihenfolge** weitermachen.  
**Vision, Story und UI** sind in den Overview-Docs beschrieben (vision_2026_2027, story_and_mythology, ui_ux_principles_and_flow); die Reihenfolge unten baut das „Gehirn“ (KG, Synthesis, Edges) und die erste sichtbare Schicht (Insight-Engine) auf, die die Agent/Voice/Visual-Experience später nutzt.

---

## ✔ Bereits umgesetzt (Pipeline A → D)

| Schritt | Status | Wo |
|--------|--------|-----|
| Upload, Asset, extract_text (PDF/MinerU/OCR) | ✔ | Worker, Server Actions |
| classify_domain | ✔ | Worker |
| extract_term_mapping (HD/BaZi Seeds) | ✔ | Worker |
| extract_interpretations (LLM oder Stub) | ✔ | Worker |
| text2kg (Nodes + Descriptor, keine Edges) | ✔ | Worker |
| synthesize_node (Stub + optional LLM, 4 Styles) | ✔ | Worker, nach text2kg gequeued |
| Dimensions (12 Keys), 9 System-Descriptoren, Seed hd_systems | ✔ | Contract, JSON, seed_hd_systems.py |
| Sprachmodell (Interpretations quellenbasiert, KG neutral, Synthesis multilingual) | ✔ | language_and_pipeline_overview.md §0 |

**End-to-End:** PDF → Chunks → Interpretations → KG-Nodes → Synthesis (canonical_description + hd_synthesis_wordings) läuft. UI kann theoretisch Synthesis abfragen (sofern API/Seiten existieren).

---

## 🔲 Noch offen (priorisiert)

### Priorität 1 – Datenbasis (Option B: Backend zuerst)

| Was | Kurzbeschreibung |
|-----|-------------------|
| **KG-Edges** | text2kg erzeugt nur Nodes. Edges aus `payload.relations` (falls definiert) mit `allowed_relation_types` aus Descriptor – Schema und Spec vorbereitet. **Wichtig für Abhängigkeiten und Pattern-Reasoning** (siehe unten). |
| **extract_dynamics** | Job: Dimensions + challenges/growth → hd_dynamics (Phasen, Traps, Growth). Optional; Descriptor `dynamic_types`-Validierung langfristig. |
| **extract_interactions** | Job: payload.interactions → hd_interactions (wenn Tabelle/Contract stehen). Optional; aktuell bereits in node.metadata.interactions. |

### Priorität 2 – Nutzbarkeit (nach Backend-Phase)

| Was | Kurzbeschreibung |
|-----|-------------------|
| **UI/UX Insight Engine** | Abfragen, Navigation, Darstellung von KG + Synthesis. Nutzer soll z. B. nach Upload „seine“ Nodes/Synthesis in der App sehen (Liste, Detail, ggf. nach Sprache). Ohne das bleibt die Pipeline Backend-only. |
| **Sprache aus App in Pipeline** | Beim Anlegen des ersten Jobs (z. B. nach Upload) **User-Locale** oder Account-Sprache in `debug.language` übergeben, damit Interpretationen/Synthesis in der gewünschten Sprache erzeugt werden. Aktuell: Default EN, keine Koppelung an UI-Sprache. Zusammen mit Insight Engine sinnvoll. |
| **Chart Calculation Engine (Open Source)** | Integration einer Open-Source-Engine (z. B. hdkit) für BodyGraph/Chart aus Geburtsdaten (Type, Authority, Centers, Gates, …). Ohne sie fehlt die persönliche Berechnung; mit ihr wird die App zum vollständigen HD-Tool. Siehe 00_overview/app_picture_and_user_journey.md. |

### Priorität 3 – Später / Optional

| Was | Kurzbeschreibung |
|-----|-------------------|
| **Synthesis in mehreren Sprachen** | Pro Sprache eine Zeile in hd_synthesis_wordings (Schema bereit). Entweder: Batch-Jobs mit `debug.language=de|fr|es` oder on-the-fly bei Abruf fehlender Sprache. |
| **Research-Layer** | Experimentelle Hypothesen (z. B. HD↔Enneagram), Community-Validierung – bewusst nicht im MVP. |
| **Channel-Duality-Dynamics** | 36 Kanäle mit 4-Phasen-Spektrum (incorrect/correct positive/negative) – als Erweiterung von L6/Dynamics dokumentiert, nicht implementiert. |
| **Concept Nodes / expresses_as Edges** | Optional: node_type=concept, Kanten von Element-Node zu Concept-Node (text2kg_spec §8). |

### KG-Edges – Abhängigkeiten, Klarstellung, Priorität

**Du hast recht: Es gibt Abhängigkeiten zwischen (fast) allem – und Edges sind dafür da.**

- **Was Edges sind:** Strukturelle Beziehungen zwischen **Knoten** im KG: z. B. „Gate X ist **part_of** Center Y“, „Element A **amplifies** B“, „**depends_on**“, „**maps_to**“ (cross-system). Das sind genau die **Abhängigkeiten und Verstärkungen** zwischen Konzepten.
- **Womit man Edges nicht verwechseln sollte:**  
  - **Dynamics** (extract_dynamics): zeitliche/phasen Logik – „was folgt“, Traps, Growth, Zyklen. Gehört in hd_dynamics, nicht in KG-Edges.  
  - **Interactions** (with_centers, with_profile): Soziallogik, bleibt in node.metadata bzw. hd_interactions.  
  - **Narrative/Story „was folgt“:** inhaltliche Erzählung, nicht dasselbe wie KG-Relationstypen.
- **Warum Edges für die Vision zentral sind:** Agent und „Muster erklären“ brauchen **Verbindungen**: was hängt womit zusammen, was verstärkt was, was gehört zu welchem größeren Ganzen. Ohne Edges sieht der Agent nur Einzelknoten; mit Edges kann er **Pattern-Reasoning** (Graph-Navigation, GraphRAG, „warum fühle ich mich so – welche Kräfte wirken zusammen?“). **Empfehlung:** Edges als Teil der **Datenbasis** („Gehirn“) mitdenken – parallel zu oder vor der Insight-Engine, sobald `payload.relations` vom LLM oder einem Schritt geliefert wird. Siehe text2kg_spec.md §4.2, layers_overview.md L4.

**Sind die Edges vollumfänglich?**  
- **Schema:** Bereits vorgesehen: `relation_type` (part_of, depends_on, amplifies, maps_to), **`strength`** (low | medium | strong | dominant | overriding), `metadata` (jsonb). Die Migration nutzt z. B. `strength text not null default 'medium'`.  
- **Gewichtung (HD z. B. Sonnentor ~70 %, Erdentor ~30 %):** Genau dafür ist **strength** da – stark/schwach/dominant. Prozentwerte könnten zusätzlich in **edge.metadata** (z. B. `metadata.weight` oder `metadata.influence_score`) abgebildet werden, wenn ihr es quantitativ braucht; sonst reicht strength. Diese Logik ist weder in Edges noch anderswo bisher implementiert – sie ist vorbereitet (Schema), sobald payload.relations inkl. Gewicht/Quelle geliefert wird.  
- **Konzepte/Schulen untereinander:** **maps_to** ist für Cross-System (z. B. HD-Gate ↔ BaZi-Entsprechung). part_of, amplifies, depends_on gelten innerhalb eines Systems und können bei Bedarf auch zwischen Systemen genutzt werden.  
- **Fazit:** Edges sind konzeptionell und im Schema vorbereitet (inkl. Gewichtung über strength/metadata); „vollumfänglich“ werden sie, sobald wir sie befüllen und ggf. weitere relation_types oder Regeln (z. B. Planet/Position für Sun/Earth) ergänzen.

### Zwei mögliche Reihenfolgen (Warum Insight-Engine/Sprache zuerst – oder Daten zuerst?)

**Synthesis ist bereits umgesetzt** (synthesize_node, hd_synthesis_wordings, canonical_description). Es geht also nicht um „Synthesis vor UI“, sondern um die Reihenfolge von **UI/Sprache** vs. **Edges/Dynamics/Interactions**.

| Option | Reihenfolge | Begründung |
|--------|-------------|------------|
| **A – Sichtbarkeit zuerst** | 1) Insight-Engine-UI, 2) Sprache, 3) Edges, 4) Dynamics/Interactions | Erster sichtbarer Nutzen: Nutzer/Curator sehen sofort Nodes + Synthesis. Pipeline ist nicht „nur Backend“. Danach Datenbasis verbreitern (Edges, Dynamics). |
| **B – Datenbasis zuerst** | 1) Edges (payload.relations + strength), 2) extract_dynamics, extract_interactions, 3) dann Insight-Engine-UI + Sprache | Das „Gehirn“ ist vollständig, bevor die Oberfläche kommt: Abhängigkeiten, Gewichtung, Phasen, Interaktionen sind da – die UI (und der spätere Agent) können von Anfang an auf vollere Daten zugreifen. |

**Empfohlen: Option B.** Backend zuerst sauber ausbauen, möglichst viel vom Plan umsetzen; dann darauf aufbauend (evtl. mit neuen Erkenntnissen) die UI erstellen. Launch kommt ohnehin später – die Datenbasis soll stabil sein, bevor Nutzer sichtbare Oberflächen nutzen.

**Insight Engine vs. Sprache:**
- **Insight Engine** = UI für KG-Nodes + Synthesis (Liste, Detail, Styles). Kommt **nach** Backend (Edges, Dynamics, Interactions).
- **Sprache** = User-Locale (`debug.language`) beim Job-Anlegen in die Pipeline übergeben. Kleine Änderung beim Job-Erzeugen (Upload/API). Bequem zusammen mit der ersten UI, die Jobs anlegt – also ** parallel zur Insight Engine** oder kurz danach, nicht vorher nötig.

---

## Empfohlene Reihenfolge (Option B – Datenbasis zuerst)

1. **KG-Edges** – `payload.relations` vom LLM oder einem vorbereitenden Schritt liefern; text2kg schreibt Edges (part_of, amplifies, depends_on, maps_to) inkl. strength. Wichtig für Abhängigkeiten und Agent/Pattern-Reasoning (Vision: „Muster erklären“, Graph-Navigation). Siehe Abschnitt KG-Edges oben.
2. **extract_dynamics** – Dimensions + challenges/growth → hd_dynamics (Phasen, Traps, Growth). Optional; Descriptor `dynamic_types`-Validierung langfristig.
3. **extract_interactions** – payload.interactions → hd_interactions (wenn Tabelle/Contract stehen). Optional; aktuell bereits in node.metadata.interactions.
4. **UI/UX Insight Engine** – Mindest-Ansicht: z. B. „Meine Assets“ → „KG-Nodes / Synthesis“ pro Asset oder Account; Anzeige von canonical_description / canonical_wording / Styles in Nutzer-Sprache.
5. **Sprache aus App** – Beim Erzeugen der Jobs (Upload oder erste Verarbeitung) `debug.language` = User-Locale setzen (oder Account-Einstellung).
6. Danach je Bedarf: **Synthesis multilingual** (Batch/on-the-fly), **Chart Calculation Engine**, **Research-Layer**, etc.

---

## Realitäten (Stand 2026)

- **Fertig:** Pipeline (extract_text → … → synthesize_node), KG-Nodes, Synthesis, Dimensions, Descriptoren, LLM auf Spark (Model-Switcher). Keine Edges, keine Chart-Engine, keine Voice-UI, kein MCP, keine volle Agent-Oberfläche.
- **Vision als Ziel:** Agent-first, Voice-first, MCP-ready, Story-basiert (siehe 00_overview/vision_2026_2027.md, story_and_mythology.md, ui_ux_principles_and_flow.md). Implementierung phasenweise: zuerst nutzbare Daten und erste sichtbare Schicht (Insight-Engine, Sprache), dann Edges für Pattern-Reasoning, dann Chart-Engine, dann Voice/Visual/MCP nach Priorität und Ressourcen.

---

## Referenzen

- **Plan Option B / Roadmap:** plan_option_b_roadmap.md
- **Erkenntnisse & Ideen für später:** erkenntnisse_und_fuer_spaeter.md (Relation Types, Dimensions-Abgleich, Priority Rules, etc.)
- **Pipeline-Stand (Details):** text2kg_spec.md §9  
- **Layer-Abgleich:** layer_implementation_abgleich.md  
- **Sprachmodell:** language_and_pipeline_overview.md §0  
- **Worker-Jobs:** hd_worker_mvp.py (extract_text … synthesize_node)  
- **Batch 200+ PDFs, Stub vs. LLM, Spark (Model-Switcher):** process_batch_llm_and_stub.md  
- **Interface/Vision (Inhalte zuerst, Node-Viz):** 00_overview/interface_and_vision.md  
- **App-Bild, User Journey, Chart-Engine:** 00_overview/app_picture_and_user_journey.md  
- **Vision 2026/27 (Agent, MCP, kein klassisches SaaS):** 00_overview/vision_2026_2027.md  
- **Story & Mythologie (Origin, Ethik, Loslassen):** 00_overview/story_and_mythology.md  
- **UI/UX-Prinzipien & Flow (Human-first, Muster statt Systeme):** 00_overview/ui_ux_principles_and_flow.md  
- **True Core Story (7 Kapitel), Plattform-Phasen, Inner Compass:** 00_overview/platform_and_story_master.md
