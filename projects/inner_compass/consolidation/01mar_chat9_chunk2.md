# IC Extraktion — Chat 9, Chunk 2/4: Quellenstrategie + Engines + Strukturbaum

> **Chunk-Scope:** Anna's Archive Redesign, Entity-Registry Format, Open-Source HD-Engines, MicFell Gate→Base Algorithmus, Strukturbaum-Seeding, Swiss Ephemeris Lizenz
> **Kürzel:** WL9

---

## SCHICHT A — SUBSTANZ

---

### A-WL9-11: Anna's Archive Pipeline-Redesign — Entity-first statt Keyword-first
**Inhalt:** Aktuelles Problem: simple_collector.py nimmt Topics aus topics.txt → Keyword-Suche → 85% Noise ("human design" findet "UX Design for Humans"). Neuer Ansatz: Entity-Registry (Autoren+Titel+ISBN) → strukturierte Query-Liste → gezielter Lookup. Drei Suchmodi: (1) Autor-zentriert (höchste Präzision), (2) ISBN-basiert (100% wenn bekannt), (3) Semantischer Cluster (Alias-Gruppen statt einzelne Keywords). Gate 1 LLM-Filtering bekommt Registry-Kontext statt Titel-only.
**Tag(s):** [ARCHITEKTUR] [CODE-KONZEPT-GAP]
**Reifegrad:** ARGUMENTATION
**Ziel-Bereich:** code/annas-archive-toolkit/
**Herkunft:** CHAT

---

### A-WL9-12: Entity-Registry JSON-Format definiert
**Inhalt:** entity_registry_hd_v01.json mit 8 Autoren-Einträgen als Seed. Format pro Autor: entity_type, id, name, aliases, language[], school_affiliation[], platform_affiliation, known_works[], known_works_count, thematic_coverage[], unique_topics[], gaps[], notes. Dient als Input für umgebauten Collector (statt topics.txt).
**Tag(s):** [SCHEMA]
**Reifegrad:** IMPLEMENTIERT (JSON erzeugt)
**Ziel-Bereich:** code/annas-archive-toolkit/projects/hd_content/
**Herkunft:** ARTEFAKT

---

### A-WL9-13: MicFell/human_design_engine — vollständigstes HD-Berechnungs-Repo
**Inhalt:** Python, nutzt pyswisseph. Liefert ALLE Layer: Gate, Line, Color, Tone, Base (bis runter!). Plus: Profile, Type, Authority, Channels, Split, Variables, Composite. Algorithmus: longitude_to_gate_data() mit 58°-Offset (IGING_offset), Segmentgrößen 5.625°→0.9375°→0.15625°→0.026042°→0.005208°. IGING_CIRCLE_LIST = Reihenfolge der 64 Gates im Zodiak. GATES_CHAKRA_DICT = Gate→Center Zuordnung. Design-Datum via swe_solcross (88° Solar Arc). Lizenz: UNKLAR (kein License-File!) → Autor kontaktieren.
**Tag(s):** [ARCHITEKTUR] [SCHEMA]
**Reifegrad:** ARGUMENTATION
**Ziel-Bereich:** Strukturbaum-Seeding, Chart-Engine
**Herkunft:** CHAT (GitHub-Repo-Analyse)

---

### A-WL9-14: Gate→Base Berechnungslogik (Kernalgorithmus)
**Inhalt:** 360° Zodiak ÷ 64 Gates = 5.625°/Gate. 5.625° ÷ 6 Lines = 0.9375°/Line. 0.9375° ÷ 6 Colors = 0.15625°/Color. 0.15625° ÷ 6 Tones = 0.026042°/Tone. 0.026042° ÷ 5 Bases = 0.005208°/Base. Gesamt: 64 × 6 × 6 × 6 × 5 = 69.120 Segmente. Reine Arithmetik aus Planeten-Grad — alle Ebenen aus demselben Ephemeris-Wert berechenbar.
**Tag(s):** [SCHEMA]
**Reifegrad:** IMPLEMENTIERT (in MicFell-Repo)
**Ziel-Bereich:** Strukturbaum, Chart-Engine
**Herkunft:** CHAT (Code-Analyse)

---

### A-WL9-15: Swiss Ephemeris Lizenz — CHF 750 reicht für eine SaaS-App
**Inhalt:** Swiss Eph Dual-Lizenz: AGPL (Open Source, erzwingt eigenen Code auch Open Source) ODER Professionallizenz (CHF 750 erste App, CHF 400 weitere, CHF 1.550 Unlimited). Für eine SaaS-Plattform: CHF 750. Moshier-Modus (eingebaut, keine Datendateien) reicht für HD-Genauigkeit (<0.1", Gate-Grenzen sind ~5.6° breit). pyswisseph = Binding für Python. Deckt ab: Westliche Astrologie + HD + Jyotish (siderisch). BaZi braucht KEIN Ephemeris (reine Kalenderarithmetik).
**Tag(s):** [ENTSCHEIDUNG] [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Ziel-Bereich:** Tech-Stack, Lizenzierung
**Herkunft:** CHAT

---

### A-WL9-16: Strukturbaum = ~362 Knoten, einmalig, VOR PDF-Extraktion
**Inhalt:** Vollständige Aufzählung: System-Root (1), Centers (9), Gates (64), Channels (36), Circuits (~8), Types (5), Strategies (5), Authorities (7), Profiles (12), Lines (6 globale), Colors (6), Tones (6), Bases (5), Incarnation Crosses (192) = ~362 Nodes. Alles Schicht A — berechenbar, deterministisch, keine Interpretation. Quelle: Deskriptor-JSON + Engine-Code (NICHT PDFs). PDFs reichern Nodes AN (Interpretationen = Schicht B), sie erzeugen sie nicht.
**Tag(s):** [ARCHITEKTUR] [SCHEMA]
**Reifegrad:** ARGUMENTATION
**Ziel-Bereich:** KG-Schema, Phase 0 Seeding
**Herkunft:** CHAT

---

### A-WL9-17: IGING_CIRCLE_LIST — Gate-Reihenfolge im Zodiak
**Inhalt:** [41,19,13,49,30,55,37,63,22,36,25,17,21,51,42,3,27,24,2,23,8,20,16,35,45,12,15,52,39,53,62,56,31,33,7,4,29,59,40,64,47,6,46,18,48,57,32,50,28,44,1,43,14,34,9,5,26,11,10,58,38,54,61,60]. Beginnt bei 58° vor 0° Widder. Dies ist die deterministische Zuordnung Planetengrad→Gate.
**Tag(s):** [SCHEMA]
**Reifegrad:** IMPLEMENTIERT (in MicFell hd_constants.py)
**Ziel-Bereich:** Strukturbaum-Seeding
**Herkunft:** CHAT (Code-Extraktion)

---

### A-WL9-18: Werke-Taxonomie — 4 Kategorien (A–D) für jedes System
**Inhalt:** (A) Primäre Quelltexte (Kanon): Kosmologie, Philosophie, Design-Mechanik, Physik. (B) Anwendungs-/Interpretationswerke: Profile, Beziehungs-Werke, Themenwerke, Lebensphasen. (C) Lehr-/Schulungswerke: Curricula, Anleitungen zur Lesart, Vermittlungshinweise. (D) Meta-Werke: Positionality, Kritik, Integration. Pro System: diese 4 Kategorien × 3 Dimensionen (Abstraktionsebene, Domäne, Werkformat).
**Tag(s):** [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Ziel-Bereich:** Quellenstrategie
**Herkunft:** CHAT

---

## SCHICHT D — NUTZER-KLÄRUNGSMOMENTE

### D-WL9-03
**Nutzer-Impuls:** "Sollte ich die system taxonomien aus den opensource berechnungskit extrahieren?"
**Ergebnis:** Ja — das ist der richtige nächste Schritt. Repos pullen → Konstanten-Parser → Coverage-Matrix-Zeilen automatisch generieren. Für HD liefert MicFell/hdkit alle 64 Gates, Channels, Centers maschinenlesbar.
**Relevanz:** HOCH

### D-WL9-04
**Nutzer-Impuls:** "Schießen wir über das Ziel hinaus?"
**Ergebnis:** "Nein in der Architektur, ja im gleichzeitigen Umfang." Taxonomie VOR Quellen ist richtig. Aber: Phase 1 = nur HD + Ur-Systeme. BaZi/Jyotish/Enneagram = Phase 2–3. Matrix darf Platzhalter haben. Pipeline startet sobald HD-Gates minimal belegt sind (3+ Quellen pro Gate).
**Relevanz:** HOCH — kalibriert den Scope

---

## ZUSAMMENFASSUNG CHUNK 2

| Schicht | Einträge |
|---------|----------|
| A — Substanz | 8 |
| D — Nutzer-Klärungen | 2 |
| **Gesamt** | **10** |

**Top-3 Erkenntnisse:**
1. **MicFell = Kern-Engine** — vollständigstes HD-Repo (Gate→Base komplett). Liefert den Strukturbaum maschinenlesbar.
2. **~362 Strukturknoten VOR PDF-Extraktion** — der Strukturbaum ist endlich und abgeschlossen. Schicht A ist fertig bevor eine Quelle gelesen wird.
3. **Entity-first Pipeline-Redesign** — Anna's Archive wird mit bekannten Entitäten abgefragt statt mit generischen Keywords. 85% Noise eliminiert.
