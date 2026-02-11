# User Journeys – HD‑SaaS

<!-- last_update: 2026-02-10 -->

User Flows und Hauptszenarien. Ausführliches App-Bild und Hintergrund: **00_overview/app_picture_and_user_journey.md**.

---

## 1) Curator / Admin (intern, MVP-nah)

| Schritt | Aktion | Ziel |
|--------|--------|------|
| Upload | PDFs/Quellen hochladen (pro Account). | Assets, Documents, extract_text-Jobs in Queue. |
| Pipeline | Jobs auf Spark abarbeiten (extract_text → … → synthesize_node), LLM per Model-Switcher. | Chunks, Interpretations, KG-Nodes, Synthesis in DB. |
| Sichten | Dokumentliste, Job-Status; Chunks/Interpretations/Nodes/Synthesis pro Asset anzeigen (Insight-Engine-UI). | Nachvollziehbarkeit, Qualitätssicherung, Korpus-Aufbau. |

**Hintergrund:** Interner Workflow für Korpus-Aufbau; keine End-User-Uploads im MVP (vgl. mvp.md).

---

## 2) Nutzer – Inhalte lesen und navigieren (prioritär)

| Schritt | Aktion | Ziel |
|--------|--------|------|
| Einstieg | Geburtsdaten erfassen (optional: Kontext-Fragebogen). Nach Integration: Chart-Berechnung (Open-Source-Engine). | Type, Strategy, Authority, Definition, … in gewählter Persona. |
| Dashboard | Tages-Insight, Fokus-Bereiche, Quick Actions. | Orientierung, Einstieg in Inhalte oder Chat. |
| Inhalte | Nach Asset/System/Sprache/Life Area suchen und filtern; Nodes/Synthesis (canonical_description, wordings, Styles) **lesen**. | Wissen versioniert und persona-/sprachgerecht konsumieren. |

**Prinzip:** Inhalte zuerst (interface_and_vision). Die App ist kein reines Chat-Interface – Lesen und Navigation der Synthesis/KG-Inhalte sind Kern.

---

## 3) Nutzer – Chat (RAG/Synthesis)

| Schritt | Aktion | Ziel |
|--------|--------|------|
| Frage | Frage oder Situation eingeben (ggf. Life Area wählen). | Kontext für LLM. |
| Antwort | System nutzt Chart (wenn berechnet), KG, Synthesis, RAG. LLM antwortet persona-angepasst. | Persönliche, quellenbasierte Guidance (AI-Ra-ähnlich, auf unserem KG). |
| Follow-up | Nachfragen, in Bibliothek speichern, in Dashboard einbinden. | Kontinuität, Lernfortschritt. |

---

## 4) Optional – Graph-Exploration

| Rolle | Aktion | Ziel |
|--------|--------|------|
| Curator | Node-Visualisierung (KG-Nodes/Edges) für Analyse und QS. | Interne Prüfung von Struktur, Dichte, Lücken. |
| Nutzer (fortgeschritten) | „Explore“-Ansicht: Zusammenhänge (z. B. Gate ↔ Center, amplifies/depends_on). | Nur wenn klarer Nutzen und Erklärung; sonst eher „Spielerei“ (interface_and_vision). |

---

## 5) Offen / geplant

- **Chart Calculation Engine (Open Source)** integrieren → dann vollständiger Flow: Geburtsdaten → Chart → alle weiteren Journeys.
- **Life Areas** als UX-Rahmen (Career, Relationships, Health, …) pro Persona – in Scratch beschrieben, für spätere Phasen.
- **Voice/Proactive Insights** (Scratch) – optional, nicht MVP.

Referenzen: app_picture_and_user_journey.md, interface_and_vision.md, vision_and_scope_frame.md, mvp.md.
