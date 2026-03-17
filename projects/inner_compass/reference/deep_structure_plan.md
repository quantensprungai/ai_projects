# Deep Structure Seed — Backlog/Referenz

> **Status:** Backlog — wird demand-driven abgearbeitet, nicht als Block.
> Trigger: Wenn die Pipeline (S5) oder PDF-Verarbeitung Nodes vermisst, werden die fehlenden Ebenen nachgezogen.

## Kernerkenntnis: Engines vs. Struktur vs. Interpretation

- **Engines** (hdkit, pyswisseph, etc.) = CALCULATORS — berechnen "welche Positionen hat diese Person"
- **Strukturgraph** (sys_kg_nodes) = FESTE BEDEUTUNGEN — "was bedeutet Gate 34 / Color 3 / Nakshatra Ashwini"
- **Interpretation** (LLM-Pipeline) = KOMBINATIONEN — "was bedeutet Gate 34 IN Color 3 für diese Person"
- Engines kommen in P3 (Chart-Berechnung für User). Strukturvertiefung kommt demand-driven.

## Aktueller Stand (S4 erledigt): 832 Nodes, 698 Edges

| System | Nodes | Abdeckung | Was fehlt (Backlog) |
|--------|------:|-----------|---------------------|
| HD | 526 | Basis-Skeleton | Lines anreichern (Keynotes, Exalt/Detri), PHS (17 Nodes), Crosses (~192), Partners (32 Edges) |
| Jyotish | 60 | Platzhalter | 108 Padas, 200+ Yogas, Dignities, Dashas, Divisional Charts |
| BaZi | 37 | Basis | 60 Jiazi, Na Yin, Hidden Stems, Branch-Interaktionen |
| Astro | 39 | Basis | Decanates (36), Dignities-Tabelle, Elements/Modalities |
| Gene Keys | 64 | Gut (Shadow/Gift/Siddhi in Metadata) | — |
| Maya | 38 | Basis | 20 Wavespells, Earth Families, Oracle-Positionen |
| Enneagram | 12 | Basis | Wings, Tritype Centers, Passions/Virtues |
| Numerologie | 28 | Basis | Personal Year, Pinnacles, Soul Urge |
| Nine Star Ki | 14 | Basis | Directions, Star-Element Zuordnungen |
| Akan | 14 | Basis | Obosom-Gottheiten |

## HD PHS-Architektur (wichtig fuer spaeter)

Colors (6), Tones (6), Bases (5) sind FESTE Bedeutungs-Nodes, KEINE Per-Gate-Subdivision:
- Color 3 bedeutet IMMER "Desire" — egal in welchem Gate
- Die Engine berechnet welche Color jemand hat
- Die Interpretation kombiniert Gate + Line + Color + Tone + Base

Deshalb: 17 PHS-Nodes (6+6+5), nicht 69.120.

## Detailplaene pro System

### HD Deep Structure (~780 Nodes Ziel)
- 1a. Lines anreichern: Keynotes + Exaltation/Detriment als Metadata (384 Lines)
- 1b. PHS Layer: 6 Colors + 6 Tones + 5 Bases (17 Nodes)
- 1c. Variables/Arrows: 4 Typen x 2 Orientierungen (12 Nodes)
- 1d. Incarnation Crosses: ~192 Nodes (Right/Juxtaposition/Left Angle)
- 1e. Programming Partners: 32 Edge-Paare
- 1f. Not-Self/Signature Themes: Metadata auf Centers + Types

### Jyotish Full (~500-700 Nodes Ziel)
- 2a. 108 Padas (27 Nakshatras x 4) + Navamsa-Zuordnungen
- 2b. 200-300 Yogas (Raja, Dhana, Pancha Mahapurusha, Nabhasa, etc.)
- 2c. Graha Dignity Table (Edges)
- 2d. Dasha-Strukturen (Vimshottari: 9 Mahadashas)
- 2e. Divisional Charts (~16 Typen)

### BaZi Deep (~130 Nodes Ziel)
- 60 Jiazi + Na Yin, Hidden Stems, Branch-Interaktionen, 12 Stages of Life

### Astro Deep (~90 Nodes Ziel)
- 36 Decanates, 4 Elemente + 3 Modalitaeten, Dignities-Tabelle

### Maya Deep (~80 Nodes Ziel)
- 20 Wavespells, 5 Earth Families, Oracle-Positionen

### Rest (Enneagram, Numerologie, NSK, Akan)
- Wings, Tritypes, Personal Year, Pinnacles, Obosom, Directions
