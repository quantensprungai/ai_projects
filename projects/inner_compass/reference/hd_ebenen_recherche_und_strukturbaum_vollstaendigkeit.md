# HD: Ebenen-Recherche & Vollständigkeit Strukturbaum

> Getrennte Recherche: Wie viele Ebenen hat HD offiziell? Reichen unsere 13 für den Strukturbaum? Und: Gene Keys im gleichen Baum oder pro Schule getrennt?

---

## 1. Recherche: Anzahl der Ebenen in HD

### Was offizielle / etablierte Quellen sagen

- **Bodygraph-Ebene:** 9 Centers, 64 Gates, 36 Channels — das ist die übliche „obere“ Struktur (Ra Uru Hu, Jovian Archive, Lehrbücher).
- **Hexagramm-Tiefe (Rave I Ching):** Unter der Gate-Ebene existiert eine **Substruktur pro Hexagramm**:
  - **Line** (6 Linien) → **Color** (6 Farben) → **Tone** (6 Töne) → **Base** (5 Basen).  
  Zitat-nahe Formulierung: „Below the line is where the science is“ (Ra) — Line, Color, Tone, Base sind die tieferen Ebenen.
- **Typ/Strategie/Autorität/Profil/Definition/Inkarnationskreuz** werden in der Literatur als abgeleitete, „höhere“ Konzepte beschrieben (aus den definierten Centern und Kanälen berechnet).

**Wichtig:** In keiner einzelnen Primärquelle steht explizit „HD hat genau 13 Ebenen“. Die **13** sind unsere **konsolidierte Taxonomie** im IC_KG_Node_Edge_Schema: Wir zählen jeden **Ebenentyp** (Basis, Ton, Farbe, Linie, Tor, Kanal, Zentrum, Profil, Variable, Autorität, Typ, Definition, Inkarnationskreuz) als eine Schicht. Das deckt:

- die **feine** Körpertiefe (Base → Tone → Color → Line)  
- die **Struktur** (Gate, Channel, Center)  
- die **abgeleiteten** Konzepte (Profile, Variable, Authority, Type, Definition, Incarnation Cross).

**Fazit Recherche:** Die Zahl „13“ ist **projektintern verbindlich** und vollständig; sie entspricht der Abdeckung aller in HD verwendeten Ebenentypen. Externe Quellen nennen oft nur Teilmengen (z. B. nur Bodygraph oder nur Line/Color/Tone/Base).

---

## 2. Reicht das für den Strukturbaum? Vollständigkeits-Check

**Ja.** Mit **hd_ontological_layer 1–13** sind alle Ebenentypen abgedeckt, die wir als **Struktur-Nodes** brauchen:

| Layer | Ebene | Als Struktur-Node? | Anzahl Nodes (Beispiel) |
|-------|--------|---------------------|--------------------------|
| 1 | Basis | ja (globale Base 1–5) | 5 |
| 2 | Ton | ja (globale Tone 1–6) | 6 |
| 3 | Farbe | ja (globale Color 1–6) | 6 |
| 4 | Linie | ja (globale Line 1–6) | 6 |
| 5 | Tor | ja (Gate 1–64) | 64 |
| 6 | Kanal | ja (Channel-Paare) | 36 |
| 7 | Zentrum | ja (Center 1–9) | 9 |
| 8 | Profil | ja (1/1 … 6/2) | 12 |
| 9 | Variable | ja (4 Pfeile) | 4 |
| 10 | Autorität | ja (7 Authority-Typen) | 7 |
| 11 | Typ | ja (5 Types) | 5 |
| 12 | Definition | ja (4 Definitionen) | 4 |
| 13 | Inkarnationskreuz | ja (192 Crosses) | 192 |

**Zusätzlich als Attribut (kein eigener Ebenentyp):** Strategy (5), Circuit (3), not_self_theme, signature — im Schema und Deskriptor bereits als Eigenschaften von Type/Center/Channel geführt. Sie erweitern die **Bedeutung** der Nodes, sind aber keine eigene „14. Ebene“.

**Damit haben wir alles für den HD-Strukturbaum:** Einmal seeden mit allen 13 Ebenen + den genannten Attributen; berechnete **Positionen** (z. B. „Gate 34 Line 3“) bleiben Properties auf Chart-Entitäten, keine zusätzlichen Struktur-Nodes.

---

## 3. Gene Keys (und andere Schulen): ein Strukturbaum pro Schule

**Entscheidung:** Wir bauen den Strukturbaum **pro System (pro Schule) getrennt**. Es gibt **keinen** gemeinsamen „HD+Gene-Keys-Strukturbaum“.

| System | Structure-Datei | Inhalt |
|--------|------------------|--------|
| HD | `system_structure/hd.json` | 13 Ebenen, alle HD-Nodes/Edges (Centers, Gates, Channels, Lines, Colors, Tones, Bases, Types, Profiles, …) |
| Gene Keys | `system_structure/genekeys.json` | Eigene Ebenen: Gene Key (64), Sequence Step (activation, venus, pearl), Shadow/Gift/Siddhi, Programming Partner |
| BaZi | `system_structure/bazi.json` | Stems, Branches, Elements, Luck Pillars, … |
| Astro, Maya, Jyotish, … | je `system_structure/<system>.json` | Jeweils systemeigene Hierarchie |

**Warum getrennt?**

- Jede Schule hat eine **eigene** interne Hierarchie und Terminologie.
- Gene Keys **baut auf** HD-Gates auf (64 Gene Keys ≈ 64 Gates), ist aber ein **eigenes System** (eigene Konzepte: Shadow/Gift/Siddhi, Golden Path, Programming Partner). Es nutzt dieselbe Engine (Position → Gate), aber andere **Interpretationsebenen**.
- **Verknüpfung** zwischen Schulen erfolgt über **Cross-System-Edges** im KG (z. B. `maps_to`: gk.gene_key.34 → hd.gate.34), nicht durch Vermischung in einem Baum.

**Erweiterte Konzepte (z. B. Gene Keys):**

- **Nicht** in den HD-Strukturbaum integrieren.
- **Separate** Structure-Datei `genekeys.json` mit GK-spezifischen Ebenen anlegen.
- Im KG: Edges zwischen GK-Nodes und HD-Nodes (z. B. Gene Key 34 ↔ Gate 34) für Navigation und Synthesis.

**Referenz:** structure_descriptor_seed.md (§2 Gene Keys, §3 „eine Datei pro System“), IC_KG_Node_Edge_Schema (system_tag: hd | gene_keys | …).

---

*Stand: Referenz für Ebenen-Recherche und Strukturbaum-Vollständigkeit; Gene Keys = separates System, eigener Strukturbaum.*
