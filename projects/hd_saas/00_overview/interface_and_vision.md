# Interface und Vision – Inhalte zuerst, Chat, Node-Visualisierung

<!-- last_update: 2026-02-10 -->

Anknüpfung an **vision_and_scope_frame.md** und **MVP/Milestones**: Wie bauen wir das Interface auf, was steht im Vordergrund, und was ist die Rolle der Node-Visualisierung?

---

## 1) Vision-Rückblick (entscheidungsrelevant)

Aus **vision_and_scope_frame.md**:

- **Nordstern:** HD Knowledge & Guidance System – Mechanik deterministisch, Wissen versioniert, LLM als **Interface** (Synthesis/Erklärung), nicht als Speicher.
- **Personas/Schools = Rendering Layer:** UI/UX Skin + Terminology + Output Style; eine Engine, viele Darstellungen.
- **Canonical IDs + Layered Interpretations** – Multi-School kompatibel.

Daraus folgt fürs Interface: Der **Inhalt** (Synthesis, kanonische Beschreibungen, nach School/Persona gefärbt) ist das Kerngeschäft. Chat ist **eine** Nutzungsform, nicht die einzige.

---

## 2) Priorität: Inhalte vor Chat

| Priorität | Was | Begründung |
|-----------|-----|------------|
| **1 – Inhalte** | Sichtbare, durchsuch-/navigierbare **Content-Schicht**: Assets, KG-Nodes, Synthesis (canonical_description, wordings, Styles), pro Sprache. Nutzer soll „seine“ oder die verfügbaren Quellen/Nodes/Synthesis **sehen und lesen** können – mit klarer Zuordnung zu Quelle/Asset/System. | Ohne das ist die Pipeline Backend-only; der Mehrwert (versioniertes Wissen, Multi-School) wird erst in der UI sichtbar. Vision: „Wissen versioniert gespeichert“ → muss abrufbar und darstellbar sein. |
| **2 – Chat** | Chat als **eine** Form des Zugriffs: Fragen stellen, Antworten aus RAG/Synthesis/Mechanik. | Wichtig, aber zweitrangig gegenüber „Inhalte strukturiert anzeigen und navigieren“. Chat baut auf der gleichen Content-Schicht auf. |
| **3 – Erweiterungen** | Persona/School-Umschaltung, erweiterte Suche, Favoriten, Export. | Nach dem stabilen Content-Zugang. |

**Konsequenz für nächste Schritte:** Die **Reihenfolge** (Option B) steht in **02_system_design/next_steps_was_fehlt_noch.md**: zuerst Edges, Dynamics, Interactions; danach Insight-Engine-UI (Listen/Detail für Assets, Nodes, Synthesis); Chat darauf aufsetzen oder parallel.

---

## 3) Node-Visualisierung: intern vs. User

**Frage:** Node-Visualisierung (Graph/Knoten-Kanten) – eher Analyse-Tool für dich intern, oder kann der User dort auch etwas erkennen / ist es mehr „Spielerei“?

**Empfehlung (als Arbeitshypothese):**

| Nutzung | Rolle | Begründung |
|---------|--------|------------|
| **Intern (Curator/Admin)** | **Analyse und Qualitätssicherung:** Prüfen, ob Nodes/Edges (wenn implementiert) plausibel sind; Dichte pro Quelle/System; Lücken oder Doppelungen. Wichtig für Korpus-Aufbau und Descriptor-Tuning. | Hoher Nutzen, wenig Aufwand in der bestehenden Admin/Curator-Welt. |
| **End-User (Produkt)** | **Optional, klar als Zusatz anbieten:** Graph als „Exploration“ oder „Wie hängt das zusammen?“ – kann Mehrwert bieten (z. B. „welche Konzepte hängen mit meinem Gate zusammen?“), aber nicht Kern des Produkts. Ohne gute Erklärung und Kontext wirkt es schnell wie Spielerei. | Erst wenn Content-Liste/Detail und ggf. Chat stehen; dann entscheiden, ob Graph als **zusätzliche** Ansicht für interessierte User sinnvoll ist (z. B. „Experten-Modus“ oder „Explore“-Tab). |

**Kurz:**  
- **Intern:** Node-Visualisierung klar einplanen als Analyse-/QS-Tool.  
- **User:** Eher nachgelagert; nur dann einführen, wenn klar ist, welcher konkrete Nutzen (z. B. „Zusammenhänge erkunden“) und mit welchem Kontext (Persona, Erklärung). Sonst Gefahr: „sieht cool aus, bringt wenig“.

---

## 4) Wo steht das in den Projekt-Docs?

| Thema | Referenz |
|-------|----------|
| Vision, Personas, Canonical IDs | **vision_and_scope_frame.md** |
| MVP Cut (Ingestion, Curator-Workflow) | **mvp.md**, **milestones.md** |
| Nächste Schritte (Insight Engine, Sprache) | **02_system_design/next_steps_was_fehlt_noch.md** |
| User Journeys | **01_spec/user_journeys.md** (noch TODO – kann mit „Inhalte zuerst, dann Chat“ gefüllt werden) |

**Vorschlag:** In **user_journeys.md** als erste Szenarien festhalten: (1) Curator: Upload → Status → Inhalte (Chunks/Interpretations/Nodes/Synthesis) sichten. (2) Leser/Nutzer: Inhalte nach Asset/System/Sprache durchsuchen und lesen. (3) Chat: Frage stellen, Antwort aus Synthesis/Mechanik. (4) Optional: Graph-Exploration für Fortgeschrittene.
