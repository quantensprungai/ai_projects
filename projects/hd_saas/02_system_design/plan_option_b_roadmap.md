# Plan: Option B – Datenbasis zuerst (HD-SaaS)

<!--
last_update: 2026-02-10
status: aktuell
scope:
  summary: "Roadmap für HD-SaaS: Backend vollständig ausbauen, dann UI. Launch später."
  in_scope:
    - Reihenfolge der Implementierung
    - Abhängigkeiten zwischen Schritten
  out_of_scope:
    - Konkrete Feature-Specs (liegen in anderen Docs)
notes:
  - "Verknüpfung: next_steps_was_fehlt_noch.md, erkenntnisse_und_fuer_spaeter.md."
-->

**Strategie:** Erst das Backend sauber ausbauen, möglichst viel vom Plan umsetzen; dann darauf aufbauend (evtl. mit neuen Erkenntnissen) die UI erstellen. Launch kommt ohnehin später.

---

## Phase 1 – Datenbasis (Backend)

1. **KG-Edges** – `payload.relations` liefern; text2kg schreibt Edges (part_of, depends_on, amplifies, maps_to) inkl. strength. Schema und Spec vorbereitet.
2. **extract_dynamics** – Dimensions + challenges/growth → hd_dynamics (Phasen, Traps, Growth). Optional.
3. **extract_interactions** – payload.interactions → hd_interactions (wenn Tabelle/Contract stehen). Optional; aktuell bereits in node.metadata.interactions.

---

## Phase 2 – Nutzbarkeit (UI)

4. **UI/UX Insight Engine** – Abfragen, Navigation, Darstellung von KG + Synthesis. Nutzer sieht Nodes/Synthesis in der App.
5. **Sprache aus App** – Beim Job-Anlegen `debug.language` = User-Locale übergeben. Zusammen mit Insight Engine sinnvoll.

---

## Phase 3 – Danach (je Bedarf)

- Synthesis multilingual (Batch/on-the-fly)
- Chart Calculation Engine (hdkit o. ä.)
- Research-Layer, Concept Nodes, weitere Erweiterungen

---

## Klarstellungen

- **Insight Engine** = UI für KG-Nodes + Synthesis. Kommt **nach** Backend.
- **Sprache** = Kleine Änderung beim Job-Erzeugen; parallel zur Insight Engine oder kurz danach.
- **Erkenntnisse für später** = erkenntnisse_und_fuer_spaeter.md (Priority Rules, Emergent Logic, Conflict Resolution, etc.)

---

## Referenzen

- **Nächste Schritte (Detail):** next_steps_was_fehlt_noch.md  
- **Erkenntnisse/Abgleich:** erkenntnisse_und_fuer_spaeter.md  
- **KG-Spec:** text2kg_spec.md  
- **Interpretations:** interpretations_contract.md
