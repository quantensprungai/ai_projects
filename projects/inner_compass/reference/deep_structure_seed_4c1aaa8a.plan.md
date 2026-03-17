---
name: Deep Structure Seed
overview: Vertiefung des Strukturgraphen auf maximale Tiefe fuer alle 10 Systeme, mit klarer Trennung zwischen Struktur-Nodes (feste Bedeutungen), Engine-Berechnung (Chart-Positionen), und LLM-Interpretation (Kombinationen).
todos:
  - id: phase1-hd-lines
    content: "HD Lines anreichern: Keynotes + Exaltation/Detriment Planeten als Metadata auf 384 Line-Nodes"
    status: pending
  - id: phase1-hd-phs
    content: "HD PHS Layer: 6 Colors + 6 Tones + 5 Bases + 4 Arrows als neue Nodes"
    status: pending
  - id: phase1-hd-crosses
    content: "HD Incarnation Crosses: ~192 Cross-Nodes (Right Angle, Juxtaposition, Left Angle)"
    status: pending
  - id: phase1-hd-partners
    content: HD Programming Partners (32 Paare) + Not-Self/Signature Themes als Metadata
    status: pending
  - id: phase2-jyotish-padas
    content: "Jyotish: 108 Padas + Navamsa-Zuordnungen"
    status: pending
  - id: phase2-jyotish-yogas
    content: "Jyotish: 200-300 Yogas (Raja, Dhana, Pancha Mahapurusha, Nabhasa, Chandra, etc.)"
    status: pending
  - id: phase2-jyotish-rest
    content: "Jyotish: Dignity-Tabelle, Dasha-Strukturen, Divisional Charts"
    status: pending
  - id: phase3-bazi
    content: "BaZi: 60 Jiazi + Na Yin + Hidden Stems + Branch-Interaktionen + 12 Stages"
    status: pending
  - id: phase3-astro-maya-rest
    content: Astro (Decanates, Dignities) + Maya (Wavespells, Earth Families) + Enneagram/Num/NSK/Akan vertiefen
    status: pending
isProject: false
---

# Deep Structure Seed — Alle Systeme auf volle Tiefe

## Kernerkenntnis: Engines vs. Struktur vs. Interpretation

- **Engines** (hdkit, pyswisseph, etc.) = CALCULATORS — berechnen "welche Positionen hat diese Person"
- **Strukturgraph** (sys_kg_nodes) = FESTE BEDEUTUNGEN — "was bedeutet Gate 34 / Color 3 / Nakshatra Ashwini"
- **Interpretation** (LLM-Pipeline) = KOMBINATIONEN — "was bedeutet Gate 34 IN Color 3 für diese Person"
- Engines kommen in P3 (Chart-Berechnung für User). Jetzt geht es NUR um den Strukturgraphen.

## Aktueller Stand vs. Ziel


| System       | Jetzt (Nodes) | Ziel (Nodes)   | Delta                                                  |
| ------------ | ------------- | -------------- | ------------------------------------------------------ |
| HD           | 526           | ~780           | +254 (Lines anreichern, Crosses, PHS-Layer, Partners)  |
| Jyotish      | 60            | ~500-700       | +450-650 (108 Padas, 200+ Yogas, Dignities, Dashas)    |
| BaZi         | 37            | ~130           | +93 (60 Jiazi, Na Yin, Hidden Stems, 12 Stages)        |
| Astro        | 39            | ~90            | +51 (Decanates, Elements, Modalities, Dignities)       |
| Gene Keys    | 64            | 64             | +0 (Shadow/Gift/Siddhi schon als Metadata)             |
| Maya         | 38            | ~80            | +42 (20 Wavespells, Earth Families, Oracle-Positionen) |
| Enneagram    | 12            | ~40            | +28 (Wings, Tritype Centers, Passions/Virtues)         |
| Numerologie  | 28            | ~50            | +22 (Personal Year, Pinnacles, Soul Urge)              |
| Nine Star Ki | 14            | ~25            | +11 (Directions, Star-Element Zuordnungen)             |
| Akan         | 14            | ~20            | +6 (Obosom-Gottheiten)                                 |
| **TOTAL**    | **832**       | **~1900-2100** | **+1100-1300**                                         |


## Phase 1: HD Deep Structure (Prioritaet)

Datei: [ic_seed_structure.py](code/hd_saas_app/apps/web/scripts/ic_seed_structure.py) — Funktion `build_hd()` erweitern

### 1a. Line-Metadata anreichern (384 Lines)

- Jede der 384 Lines bekommt: `keynote`, `exaltation_planet`, `detriment_planet`
- Datenquelle: Rave I'Ching Referenztabelle (offen verfuegbar als Planetenzuordnungen)
- Modellierung: Metadata-Felder auf existierenden Line-Nodes (kein neuer Node noetig)
- Beispiel: `hd.line.34_2` bekommt `metadata: {"keynote": "Momentum", "exaltation": "mars", "detriment": "uranus"}`

### 1b. PHS Layer: Colors, Tones, Bases (17 neue Nodes)

- 6 Color-Nodes: `hd.color.1` bis `hd.color.6` (Fear, Hope, Desire, Need, Guilt, Innocence)
- 6 Tone-Nodes: `hd.tone.1` bis `hd.tone.6` (Smell, Taste, Outer/Inner Vision, Feeling, Touch)
- 5 Base-Nodes: `hd.base.1` bis `hd.base.5` (Caves, Markets, Kitchens, Mountains, Valleys)

### 1c. Variables/Arrows (12 neue Nodes)

- 4 Arrow-Typen: Determination, Environment, Perspective, Motivation
- 2 Orientierungen pro Arrow: Left (Strategic) / Right (Receptive)
- Plus: Transferred/Natural Distinction als Metadata

### 1d. Incarnation Crosses (~192 neue Nodes)

- Right Angle (64), Juxtaposition (64), Left Angle (64)
- Jedes Kreuz = 4 Gates (Conscious Sun/Earth + Design Sun/Earth)
- Datenquelle: Mathematisch ableitbar aus Gate-Positionen + bekannte Listen

### 1e. Programming Partners + Harmonics (~32 Edges)

- 32 gegenueberliegende Gate-Paare auf dem Mandala (z.B. Gate 1 ↔ Gate 2)
- Modellierung: Neue Edges `programming_partner` zwischen existierenden Gate-Nodes

### 1f. Not-Self / Signature Themes (Metadata auf existierenden Nodes)

- 9 Centers: je ein Not-Self-Theme als Metadata (z.B. Sacral open = "Weiß nicht wann genug ist")
- 5 Types: je Signature + Not-Self (z.B. Generator: Satisfaction / Frustration)

## Phase 2: Jyotish Full Depth

### 2a. Padas (108 neue Nodes)

- 27 Nakshatras x 4 Padas, jeder Pada mit eigenem Rashi-Lord und Navamsa-Zeichen
- Edges: Pada → Nakshatra (part_of), Pada → Navamsa-Rashi (maps_to)

### 2b. Yogas (~200-300 neue Nodes)

- Kategorien: Raja Yogas (~~20), Dhana Yogas (~~15), Pancha Mahapurusha (5), Nabhasa (~~32), Chandra (~~30), Surya (~~10), weitere (~~100+)
- Jeder Yoga: Name, beteiligte Grahas/Bhavas, Effekt
- Datenquelle: Brihat Parashara Hora Shastra + Saravali (oeffentlich verfuegbar)

### 2c. Graha Dignity Table (Edges)

- 9 Grahas x 12 Rashis = Exaltation/Debilitation/Mooltrikona/Own/Friendly/Enemy
- Modellierung: Edges mit `relation_type` = `exalted_in`, `debilitated_in`, etc.

### 2d. Dasha-Strukturen (~15-20 neue Nodes)

- Vimshottari-System: 9 Mahadashas mit Reihenfolge + Dauer
- Optional: Ashtottari, Yogini
- Modellierung: Dasha-Nodes mit Metadata (years, sequence)

### 2e. Divisional Charts (~16 neue Nodes)

- D1 (Rashi), D2 (Hora), D3 (Drekkana), D4 (Chaturthamsa), D7 (Saptamsa), D9 (Navamsa), D10 (Dasamsa), D12 (Dwadashamsha), D16 (Shodashamsha), D20 (Vimshamsha), D24 (Chaturvimshamsha), D27 (Saptavimshamsha), D30 (Trimshamsha), D40 (Khavedamsha), D45 (Akshavedamsha), D60 (Shashtyamsha)

## Phase 3: BaZi, Astro, Maya, Rest vertiefen

### 3a. BaZi (+93 Nodes)

- 60 Jiazi (Sexagenary-Paare: Jia-Zi, Yi-Chou, ...) mit Na Yin Element
- Hidden Stems pro Branch (Edges: Branch → hidden Stem)
- Branch-Interaktionen: 6 Clashes, 6 Combines, 6 Harms, 3 Penalties (Edges)
- 12 Stages of Life (Chang Sheng: birth, bath, crown, ...)

### 3b. Astro (+51 Nodes)

- 36 Decanates (3 pro Zeichen, mit Sub-Ruler)
- 4 Elemente (Fire, Earth, Air, Water) + 3 Modalitaeten (Cardinal, Fixed, Mutable) als Nodes
- Erweiterte Dignities-Tabelle: Planet→Sign Exaltation/Detriment/Fall (Edges)

### 3c. Maya (+42 Nodes)

- 20 Wavespells (je 13 Kin, benannt nach dem ersten Seal)
- 5 Earth Families (Polar, Cardinal, Core, Signal, Gateway)
- Oracle-Positionen pro Seal (Analog, Antipode, Occult, Guide)

### 3d. Enneagram, Numerologie, NSK, Akan (+67 Nodes)

- Enneagram: Wings (18), Tritype Centers (3), Passions/Virtues (9/9)
- Numerologie: Personal Year Cycle (9), Pinnacles (4), Soul Urge descriptions
- Nine Star Ki: 8 Directions, Star→Element Zuordnungen
- Akan: 7 Obosom (Gottheiten), Adaduanan-Zyklus

## Engines: Wann und wo?

Engines (hdkit, pyswisseph, etc.) kommen in **P3** (nach S5-S7), weil:

- Sie berechnen CHARTS (welche Positionen hat Person X), nicht Strukturdaten
- Strukturdaten kommen aus Domaenwissen (Rave I'Ching, BPHS, traditionelle Tabellen)
- Engine-Integration erfordert npm/pip Packages + API-Wrapper = eigener Arbeitsschritt

Reihenfolge: **Strukturgraph vertiefen (jetzt) → PDFs + Interpretationen (S5-S6) → Engines fuer User-Charts (P3)**

## Implementierung

Alles in einer erweiterten Version von `ic_seed_structure.py`:

- Phase 1 (HD): ~4-6h Arbeit (Line-Daten kuratieren, Crosses berechnen)
- Phase 2 (Jyotish): ~6-8h Arbeit (Yogas kuratieren, Dignity-Tabelle)
- Phase 3 (Rest): ~4-6h Arbeit (Jiazi, Decanates, Wavespells)
- Script bleibt idempotent (merge-duplicates)

