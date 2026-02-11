# App-Bild, User Journey und Hintergrund (konsolidiert)

<!-- last_update: 2026-02-10 -->

Konsolidierung aus **Projekt-Docs** (vision_and_scope_frame, mission, interface_and_vision, mvp) und **Scratch** (scratch/wissen/hd, scratch/inbox/hd): Was ist die App, für wen, welcher Ablauf – inkl. **Chart Calculation Engine (Open Source)** und Story/UI-Logik.

---

## 1) Nordstern und Kern der App

- **Vision (vision_and_scope_frame):** HD Knowledge & Guidance System – **Mechanik deterministisch**, **Wissen versioniert**, **LLM als Interface** (Synthesis/Erklärung), nicht als Speicher.
- **Mission:** Human Design (und perspektivisch BaZi, Astro, Gene Keys, …) **konsistent, nachvollziehbar und interaktiv** nutzbar machen.
- **Eine Engine, viele „Skins“:** Personas/Schools = **Rendering Layer** (UI/UX + Terminologie + Output-Style), keine separaten Apps. Canonical IDs + Layered Interpretations (Multi-School).

Daraus: Die **App** ist ein **Personal Knowledge & Guidance System**: Geburtsdaten → Chart (Berechnung) → strukturiertes Wissen (KG + Synthesis) → Zugang über **Inhalte** (Listen, Detail, Suche) und **Chat** (RAG/Synthesis). Inhalte zuerst, Chat als zweite Nutzungsform (interface_and_vision).

---

## 2) Schichten (technisch / logisch)

Aus **scratch/wissen/hd/multicultural_personality_app_architecture.md** und **scratch/inbox/hd/hd_system_raw.md**:

| Schicht | Inhalt | Status / Quelle |
|---------|--------|------------------|
| **Calculation Layer** | BodyGraph/Chart aus Geburtsdaten: Type, Strategy, Authority, Definition, Centers, Channels, Gates, Profile, Incarnation Cross, … HD + BaZi + weitere Systeme. | **Noch zu integrieren:** Chart Calculation Engine (Open Source, z. B. **hdkit** auf GitHub). In Scratch explizit als „Core“ genannt (hdkit, BaZi calculator, Jyotish, …). |
| **Knowledge Layer** | KG (Nodes, optional Edges), Interpretations, Synthesis, Term-Mapping. Versioniertes Wissen aus Quellen/PDFs. | Pipeline implementiert (extract_text → interpretations → text2kg → synthesize_node); Edges optional. |
| **AI Synthesis / RAG** | Personalisierte Insights, Cross-System-Muster, Antworten aus KG + Synthesis. | LLM auf Spark (Model-Switcher); RAG-Anbindung für Chat geplant. |
| **Persona Rendering** | Business / Spiritual / Curious Explorer / System Expert – Sprache, Ton, Begriffe. | In Vision und Scratch beschrieben; Styles (natural, coaching, poetic, technical) in Synthesis bereits angelegt. |
| **Life Areas** (optional) | Career, Relationships, Health, Finance, Personal Growth, … pro Persona unterschiedlich benannt. | In Scratch detailliert; für MVP nicht zwingend, aber als Rahmen für spätere UX nutzbar. |

**Chart Calculation Engine:**  
Explizit **noch zu integrieren**. Ziel: Open-Source-Engine (z. B. hdkit) einbinden, damit die App aus Geburtsdaten den Chart berechnet (Type, Authority, definierte Centers, Gates, …) und alle weiteren Layer (KG, Synthesis, Chat) darauf aufsetzen können. Ohne diese Integration fehlt die „persönliche“ Berechnung; mit ihr wird die App zum vollständigen HD (plus Multi-System) Tool.

---

## 3) User Journey – konsolidiert

Aus **scratch/wissen/hd** (UX/Journey Framework), **scratch/inbox/hd** (HD-System, AI Ra–ähnliche Nutzung) und **interface_and_vision** (Inhalte zuerst):

### A) Curator / Admin (intern, MVP-nah)

1. **Upload** → PDFs/Quellen in Korpus (Assets, Documents).
2. **Pipeline** → extract_text (MinerU) → interpretations → text2kg → synthesis (auf Spark, LLM per Model-Switcher).
3. **Sichten** → Dokumentliste, Status, ggf. Chunks/Interpretations/Nodes/Synthesis (Insight-Engine-UI, noch zu bauen).

### B) End-User – Einstieg und tägliche Nutzung (Zielbild)

1. **Entry & Onboarding**  
   Geburtsdaten erfassen → (nach Integration) **Chart-Berechnung** → kurzer Kontext (optional) → Ergebnis-Reveal (Type, Strategy, Authority, …) in gewählter Persona-Sprache → Dashboard.

2. **Dashboard**  
   Tages-Insight, Fokus-Bereiche, Quick Actions, letzte Gespräche, Fortschritt (vgl. multicultural_personality_app_architecture).

3. **Inhalte (prioritär)**  
   **Lesen und navigieren:** Assets/Quellen, KG-Nodes, Synthesis (canonical_description, wordings, Styles) in Nutzer-Sprache. Suche, Filter nach System/Persona/Life Area. „Meine“ oder öffentliche Inhalte – je nach Tenant/Account.

4. **Chat**  
   Frage stellen → Kontext (Chart, Life Area, Situation) → Antwort aus RAG/Synthesis/Mechanik, persona-angepasst. Wie „AI Ra“, aber auf unserem KG + Multi-School.

5. **Vertiefung & Fortschritt**  
   Life-Area-Exploration, Multi-System-Analyse, Speichern in persönlicher Bibliothek; optional Fortschritts-Checks, Gamification (Scratch).

### C) Optional: Graph-Exploration

- **Intern:** Node-Visualisierung für Analyse/QS (Curator).  
- **User:** Optional „Explore“-Ansicht (was hängt mit diesem Gate/Center zusammen?), sofern klarer Nutzen und Kontext (interface_and_vision).

---

## 4) Was in den Docs steht vs. was noch fehlt

| Thema | Wo gefunden | Stand |
|-------|-------------|--------|
| Vision, Personas, Canonical IDs | vision_and_scope_frame.md, mission.md | ✔ |
| Inhalte zuerst, Chat zweitens, Node-Viz | interface_and_vision.md | ✔ |
| Calculation Layer, Personas, Life Areas, User Journey (Entry → Dashboard → Chat → Progress) | scratch/wissen/hd/multicultural_personality_app_architecture.md | Referenz; Chart-Engine **noch nicht** in Code integriert |
| HD-Hierarchie, Graph/Regel/LLM-Schichten | scratch/inbox/hd/hd_system_raw.md | Konzept; KG + Synthesis + Chat entsprechen dieser Aufteilung |
| AI Ra / Jovian-ähnliches Chat-Modell, Wissensbasis | scratch/inbox/hd/hd_learning_hub_scrapes.md | Orientierung für Chat + Wissensbasis; unsere Basis = eigener KG + Synthesis |
| Story/Narrative (z. B. 2027-Serie) | scratch/wissen/story/*.md | Eigenes Thema (Content/Marketing), nicht Kern der App-Logik |
| Konkrete User Journeys (Flows) | user_journeys.md | War TODO → wird unten ergänzt |

---

## 5) Konkrete User-Journey-Flows (für user_journeys.md)

- **Curator:** Upload → Job-Status → Chunks/Interpretations/Nodes/Synthesis sichten (Insight-Engine).
- **Nutzer (Leser):** Geburtsdaten (→ Chart, sobald Engine da) → Dashboard → **Inhalte** nach Asset/System/Sprache durchsuchen und lesen (Synthesis, canonical_description).
- **Nutzer (Chat):** Frage eingeben → Kontext (Chart, Life Area) → Antwort aus KG/Synthesis/RAG, persona-angepasst.
- **Optional:** Graph-Exploration („Zusammenhänge sehen“) für fortgeschrittene User.

Diese Flows sind in **01_spec/user_journeys.md** als konkrete Szenarien eingetragen (siehe dort).

---

## 6) Vision, Story, UI (2026/2027)

Die erweiterte **Vision** (Agent-first, Voice-first, MCP, kein klassisches SaaS), die **Story-Welt** (Wiederkehr der inneren Stimme, Charaktere, Ethik, Loslassen) und die **UI-Prinzipien** (Human-first, Muster statt Systeme, Flow Arrival → Gespräch → Muster → Deep Insight → optional Mechanik) sind in eigenen Docs festgehalten und fließen in die Priorisierung ein:

- **vision_2026_2027.md** – Was die App 2026/27 ist; 3 Modi; MCP-ready; Produktpositionierung.
- **story_and_mythology.md** – Origin-Story, Charaktere, Plattform als Übersetzung nicht Autorität, Ethik, 2027, episode-based Unlock.
- **ui_ux_principles_and_flow.md** – Sprache der User („Warum fühle ich mich so?“), Flow, „Mechanik anzeigen“ für Profis.

**Implementierungsreihenfolge** (next_steps_was_fehlt_noch.md) baut zuerst das „Gehirn“ (KG, Synthesis, Edges) und die erste sichtbare Schicht (Insight-Engine, Sprache); Voice, Visual Patterns, MCP und Story-basiertes Unlock folgen phasenweise gemäß Vision und Realitäten.

---

## 7) Referenzen

- **Projekt:** vision_and_scope_frame.md, mission.md, interface_and_vision.md, mvp.md, next_steps_was_fehlt_noch.md  
- **Vision/Story/UI:** vision_2026_2027.md, story_and_mythology.md, ui_ux_principles_and_flow.md  
- **Scratch:** scratch/wissen/hd/multicultural_personality_app_architecture.md, scratch/inbox/hd/hd_system_raw.md, scratch/inbox/hd/hd_learning_hub_scrapes.md  
- **Technisch:** text2kg_spec.md, layers_overview.md, process_batch_llm_and_stub.md
