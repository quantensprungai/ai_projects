# Inner Compass — Chart Engines

> Welche Engine berechnet was. Engine ≠ KG: Engine berechnet WAS aktiviert ist, KG weiß WAS DAS BEDEUTET.

## 1. Engines vs. Knowledge Graph

| Ebene | Verantwortung | Beispiel |
|-------|---------------|---------|
| **Engine** | Berechnung: "Person X hat Gate 34 aktiviert" | hdkit.calculate(birth) → gates: [34, 20, 57] |
| **KG** | Bedeutung: "Gate 34 bedeutet rohe sakrale Kraft" | sys_kg_nodes WHERE node_key = 'hd.gate.34' |
| **Mapping** | Verbindung: Chart-Daten → KG-Nodes → Interpretationen → Handbuch | gates[34] → 'hd.gate.34' → canonical_description → Lebensbereich |

## 2. Staffel 1: Die Vier Spiegel (Launch)

### Human Design
| Feld | Wert |
|------|------|
| Engine | hdkit (JS/Node, ~50 Stars, aktiv seit 2016) oder SharpAstrology (C#) |
| Input | Geburtsdatum, -uhrzeit, -ort |
| Output | Typ, Profil, definierte Zentren, aktive Tore/Kanäle, Inkarnationskreuz |
| Integration | npm-Paket oder API-Wrapper |
| Nodes erzeugt | ~9 Center + 64 Gates + 384 Lines + 36 Channels + 5 Types + 12 Profiles |
| Deskriptor-Erweiterung nötig | structure.centers (Gates pro Center), structure.channels |

### BaZi (Four Pillars)
| Feld | Wert |
|------|------|
| Engine | bazi-calculator-by-alvamind (TS/npm, ~20 Stars) oder bazica (Go, aktiv 2025) |
| Input | Geburtsdatum, -uhrzeit |
| Output | 4 Säulen (Year/Month/Day/Hour), Day Master, Stems, Branches, Hidden Stems, Luck Pillars |
| Integration | npm-Paket (alvamind) oder Go-Service (bazica) |
| Nodes erzeugt | 10 Stems + 12 Branches + 60 Jiazi + 10 Ten Gods + 5 Elements |
| Deskriptor-Erweiterung nötig | structure.stems, structure.branches, structure.cycles, structure.ten_gods |

### Westliche Astrologie
| Feld | Wert |
|------|------|
| Engine | pyswisseph (Python, ~400+ Stars, Industriestandard) + immanuel-python (~100+ Stars) |
| Input | Geburtsdatum, -uhrzeit, -ort |
| Output | Planetenpositionen, Häuser, Aspekte, Zeichen. Natal + Solar Returns + Progressions + Composites. |
| Integration | Python-Packages (pip) |
| Nodes erzeugt | 10 Planeten + 12 Zeichen + 12 Häuser + Aspekttypen |
| Deskriptor-Erweiterung nötig | structure.planets, structure.signs, structure.houses, structure.rulerships |

### Maya Tzolkin
| Feld | Wert |
|------|------|
| Engine | tzolkin-calendar (Python/PyPI, ~15 Stars, stabil) |
| Input | Geburtsdatum (keine Uhrzeit nötig) |
| Output | Kin-Nummer (1-260), Sonnenzeichen (Seal, 1-20), Ton (1-13), Wavespell |
| Integration | pip install tzolkin-calendar |
| Nodes erzeugt | 20 Seals + 13 Tones + 260 Kin + 20 Wavespells + 5 Earth Families |
| Deskriptor-Erweiterung nötig | structure.seals, structure.tones, structure.kin_mapping |

## 3. Staffel 2: Die Tiefe

### Jyotish (Vedische Astrologie)
| Feld | Wert |
|------|------|
| Engine | PyJHora (Python, ~60 Stars, ~6300 Tests — umfangreichste OS-Lib) |
| Output | Vimshottari Dasha, Divisional Charts, Nakshatras, Panchanga, Yogas |
| Rolle | Stress-Test für Schema (komplexestes System) |

### Gene Keys
| Feld | Wert |
|------|------|
| Engine | Kein eigenständiger Calculator — nutzt identische Planetenpositionen wie HD |
| Methode | pyswisseph + Lookup-Tabelle (64 Hexagramme auf 360° Zodiak) |
| Output | 64 Gene Keys × 3 Frequenzen (Shadow/Gift/Siddhi) × Sphären |

### Numerologie
| Feld | Wert |
|------|------|
| Engine | numerology (Python/PyPI, ~40 Stars, Pythagorean) |
| Input | Name + Geburtsdatum (neuer Input-Typ!) |
| Output | Life Path, Heart's Desire, Personality, Destiny, Personal Year |

## 4. Staffel 3: Die Wurzeln

| System | Engine | Aufwand |
|--------|--------|---------|
| Nine Star Ki | Kein Paket nötig — Modulo-9-Berechnung, ~20 Zeilen | Trivial |
| Akan Day Name | Kein Paket nötig — Wochentag → 1 von 7 Names, ~5 Zeilen | Trivial |

## 5. Engine-Integration-Pattern

```
Geburtsdaten (Datum, Uhrzeit, Ort)
  ↓
Engines berechnen parallel:
  ├→ hdkit           → HD-Chart
  ├→ alvamind        → BaZi-Chart
  ├→ pyswisseph      → Astro-Chart
  └→ tzolkin-calendar → Maya-Kin
  ↓
Chart-Elemente → Canonical-ID-Mapping:
  [34, 20, 57] → ["hd.gate.34", "hd.gate.20", "hd.gate.57"]
  ↓
KG-Lookup: sys_kg_nodes WHERE node_key IN (...)
  → canonical_descriptions
  → interpretations
  → cross_system edges (maps_to)
  → dynamics (aktive Zyklen)
  ↓
Handbuch-Generator: Lebensbereich × Dimensionen × Tiefenschicht
  → Personalisiertes Handbuch
```

## 6. Wo die Kits wohnen — Teil des App-Repos

Die Open-Source-Kits (hdkit, alvamind, pyswisseph, tzolkin-calendar, PyJHora, …) werden **geklont** und leben **im gleichen Repo** wie die App — nicht in einem separaten Repo. Zwei Gründe:

1. **Strukturbäume (Phase 0):** Aus dem Quellcode der Kits werden Konstanten/Lookup-Tabellen geparst (Gates pro Center, Stems/Branches, etc.) → Input für Deskriptor-Erweiterung und Seed-Script. Dafür brauchen wir die **Quellen lokal**.
2. **Laufzeit-Berechnung:** User-Geburtsdaten → Engine aufrufen → Chart-Daten → Mapping auf sys_kg_nodes. Dafür werden die gleichen Kits als Bibliothek/Service genutzt.

**Ort im Repo (verbindlich):**

```
code/inner_compass_app/          (bzw. code/hd_saas_app/ bis Umbenennung)
  packages/
    engines/
      hd/           ← hdkit (JS/Node) geklont oder npm + Parser auf node_modules
      bazi/         ← bazi-calculator-by-alvamind (TS) oder bazica (Go) geklont
      astro/        ← pyswisseph + immanuel (Python) geklont oder pip + Parser
      maya/         ← tzolkin-calendar (Python) geklont oder pip
      jyotish/      ← PyJHora (Python, Staffel 2)
```

**Entscheidung:** **Geklonte Kopie** (kein Submodule). Pro System ein Unterordner unter `packages/engines/`; jedes Kit mit eigenem `.git`, damit Updates per `git pull` im jeweiligen Ordner möglich sind. Kein separates Repo „inner_compass_engines“ — alles in einem Clone. Konkret umgesetzt in `code/hd_saas_app/packages/engines/` (Repo heißt noch hd_saas_app, Umbenennung zu inner_compass_app geplant); siehe `packages/engines/README.md` im Code-Repo für URLs und Update-Befehle.

**Committen:** Zwei Varianten (siehe `packages/engines/README.md` im Code-Repo). Empfohlen: **Variante A (Code im Repo)** — einmalig `scripts/strip-engine-git.ps1` ausführen (entfernt `.git` in jedem Kit), dann `git add packages/engines` und commit. So ist ein Clone = alles dabei; Upstream-Updates später per erneutem Klonen + Script + Commit.

**Zwei Nutzungen derselben Kits:**

| Nutzung | Wann | Wo |
|--------|------|-----|
| **Struktur parsen** | Phase 0, einmalig pro Kit-Update | Parser-Script liest z.B. `packages/engines/hd/` → erzeugt/aktualisiert structure in system_descriptors oder Seed-Input |
| **Chart berechnen** | Laufzeit (User gibt Geburtsdaten ein) | App/Worker ruft Engine auf (direkt JS/TS oder via Python-API für pyswisseph etc.) → Chart → KG-Lookup |

JS/TS-Engines können direkt in Next.js laufen; Python-Engines laufen als Service (z.B. auf Spark) oder als API-Wrapper, den die App aufruft.

## 7. Parsing aus den Kits — was ansteht

**Aktueller Stand:** Die Struktur (Centers, Gates, Channels, Stems, …) ist **nicht** in den System-Deskriptoren (`projects/inner_compass/system_descriptors/*.json`), sondern **hardcoded** in `ic_seed_structure.py` (HD_CENTERS, GATE_TO_CENTER, HD_CHANNELS, BAZI_STEMS, …). Die Pipeline-Doku (pipeline.md §6) beschreibt das Ziel: `descriptor["structure"]["centers"]` und `descriptor["structure"]["channels"]` → Seed-Script liest daraus. Dafür fehlt entweder (a) das Befüllen der Deskriptor-`structure` von Hand, oder (b) **Parsing aus den Kits** und Schreiben in die Deskriptoren (oder als generierter Input fürs Seed-Script).

**Was pro System geparst werden soll und wohin:**

| System | In den Kits zu finden / zu parsen | Ziel (Deskriptor oder Seed) | Priorität |
|--------|-----------------------------------|-----------------------------|-----------|
| **HD** | Centers (IDs + Gates pro Center), Channels (Gate-Paare + Name). hdkit: z.B. `bodygraph-data.js`, `constants.js` oder Lookup-Tabellen. | `structure.centers`, `structure.channels` in hd.json; oder Seed-Script weiter mit Python-Daten, aber aus Parser generiert. | 1 (zuerst) |
| **BaZi** | 10 Stems, 12 Branches, 60 Jiazi, Ten Gods, Element-Zyklen (producing/controlling). alvamind: TS-Typen/Consts. | `structure.stems`, `structure.branches`, `structure.cycles`, `structure.ten_gods` in bazi.json. | 2 |
| **Astro** | Planeten-Liste, 12 Zeichen, Häuser, Rulerships. pyswisseph/immanuel: Konstanten oder Enum-ähnliche Definitionen. | `structure.planets`, `structure.signs`, `structure.houses`, `structure.rulerships` in astro.json. | 3 |
| **Maya** | 20 Seals, 13 Tones, Kin-Mapping (1–260). tzolkin-calendar: Kalender-Logik / Lookup. | `structure.seals`, `structure.tones`, `structure.kin_mapping` in mayan_tzolkin.json. | 4 |
| **Jyotish** | (Staffel 2) Nakshatras, Dasha-Systeme, Divisional Charts — komplex; später. | structure-Erweiterung im Deskriptor. | 5 |

**Konkrete nächste Schritte (Reihenfolge):**

1. **HD:** In `packages/engines/hd/` die Dateien identifizieren, die Center→Gates und Channel-Definitionen enthalten (z.B. bodygraph, constants, channel/gate-Mappings). Ein kleines Parser-Script (Node oder Python), das daraus JSON erzeugt: `structure.centers`, `structure.channels` im Format, das pipeline.md §6 / das Seed-Script erwarten. Optional: `hd.json` um diesen `structure`-Block erweitern und Seed-Script umstellen, sodass es aus dem Deskriptor liest statt aus HD_CENTERS/HD_CHANNELS.
2. **BaZi:** In `packages/engines/bazi/` nach Stems, Branches, Ten Gods, Zyklen suchen → Parser → `bazi.json` `structure.*`.
3. **Astro / Maya:** Analog; Struktur aus pyswisseph/immanuel bzw. tzolkin-calendar extrahieren → Deskriptor-`structure` befüllen.
4. **Seed-Script anbinden:** Entweder `ic_seed_structure.py` liest `structure` aus dem geladenen Deskriptor (eine Quelle of Truth), oder ein Build-Step generiert aus den Kits die bestehenden Python-Konstanten — dann bleibt die Struktur im Code, ist aber kit-abgeleitet.

**Wo die Parser-Scripts leben:** Entweder im Code-Repo unter `scripts/` (z.B. `scripts/parse_engines_to_descriptor.py`) oder pro System unter `packages/engines/<system>/scripts/`. Output: Structure-Dateien (siehe unten), nicht direkt die Deskriptoren.

**Deskriptor vs. Seed vs. Structure:** Siehe [reference/structure_descriptor_seed.md](../reference/structure_descriptor_seed.md). Kurz: **Deskriptor** = Regeln/Formate pro System (element_types, canonical_id); **Structure** = alle Ebenen, alle Nodes/Edges, **sauber und separat** (z.B. `system_structure/<system>.json`); **Seed** = Script, das Structure liest und in sys_kg_nodes/sys_kg_edges schreibt. Pro System einzeln bauen; Ebenen-Checklisten (HD 13 Layer inkl. Ton/Farbe/Linie, BaZi, Astro, Maya, …) stehen in structure_descriptor_seed.md, damit keine Ebene fehlt.
