

# Inner Compass — Chart Engines & System-Prüf-Framework

> Welche Engine berechnet was, welche Daten kommen woher, wie prüfen wir jedes System.
> Engine ≠ KG: Engine berechnet WAS aktiviert ist, KG weiß WAS DAS BEDEUTET.

**Phase 1 — gleiches Vorgehen für jedes System:** siehe **[engine_integration_playbook.md](../reference/engine_integration_playbook.md)** (Katalog → Struktur → Validierung → KG-Seed).

**Grenze „Kit-Analyse vs. volle Ontologie“** (Ziwei/BaZi: was in v0-JSON steht, was Laufzeit/ später bleibt, grobe %-Einordnung): **Playbook §7**. **Hanzi in JSON / UTF-8:** **§7.5**.

---

## 1. Engines vs. Knowledge Graph


| Ebene       | Verantwortung                                                    | Beispiel                                                         |
| ----------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Engine**  | Berechnung: "Person X hat Gate 34 aktiviert"                     | hdkit.calculate(birth) → gates: [34, 20, 57]                     |
| **KG**      | Bedeutung: "Gate 34 bedeutet rohe sakrale Kraft"                 | sys_kg_nodes WHERE node_key = 'hd.gate.34'                       |
| **Mapping** | Verbindung: Chart-Daten → KG-Nodes → Interpretationen → Handbuch | gates[34] → 'hd.gate.34' → canonical_description → Lebensbereich |


---

## 2. Die vier Datenkategorien (K1–K4)

Jedes Quellsystem liefert Daten aus vier Kategorien. Die Kategorie bestimmt **woher** die Daten kommen und **wie** sie in den KG gelangen.


| Kat.   | Name               | Inhalt                                                                              | Quelle                                               |
| ------ | ------------------ | ----------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **K1** | Numerisch          | Grad-Grenzen, Positionen, Zeitzykluslängen — alles rein Mathematische               | ✅ Open-Source-Kit (automatisch)                      |
| **K2** | Strukturregeln     | Gate-Kanal-Mapping, Typ-Logik, Exaltationen, Dignitäten — Konstanten im Kit-Code    | ✅ Open-Source-Kit (automatisch, im Code)             |
| **K3** | Gewichtungslogiken | Wenn-Dann-Regeln, Einflussstärken (70%/30%), Kombinationsregeln — NUR in Lehrtexten | ⚠️ Literatur PDF → sys_kg_edges (rules)              |
| **K4** | Bedeutungen        | Symbol, Narrativ, Archetyp, Schatten, Gabe, Einladung, Kontextinterpretation        | ❌ Ausschließlich Literatur PDF → sys_interpretations |


**Konsequenz für die Pipeline:**

- **K1+K2** = Struktur-Seed (Phase 0/1, aus Kits extrahierbar, ~40% des KG)
- **K3** = MinerU+LLM Modus A (Regeln extrahieren, Phase 2)
- **K4** = MinerU+LLM Modus B+C (Eigenschaften + Bedeutungen extrahieren, Phase 2)
- **Ontologie** = K1+K2 als Gerüst + K3+K4 als Anreicherung. Alles zusammen IST der KG.

**Mapping auf Supabase-Schema (architecture.md §2):**


| K-Kat.              | Ziel-Tabelle                    | Felder                                            |
| ------------------- | ------------------------------- | ------------------------------------------------- |
| K1                  | sys_kg_nodes                    | properties JSONB (degree_start, degree_end, ...)  |
| K2                  | sys_kg_nodes + sys_kg_edges     | node-Struktur + intra_system-Edges                |
| K3                  | sys_kg_edges + sys_interactions | condition JSONB, effect JSONB, weight, evidence   |
| K4a (Eigenschaften) | sys_kg_nodes                    | properties JSONB (guna, symbol, devata, keywords) |
| K4b (Bedeutungen)   | sys_interpretations             | context, text, evidence, source, embedding        |


---

## 3. Evidenzklassen

Jeder Datenpunkt im KG bekommt eine Evidenzklasse. Bestimmt Vertrauenswürdigkeit und Darstellung im UI.


| Klasse | Name                | Bedeutung                                                                 | Beispiel                                     |
| ------ | ------------------- | ------------------------------------------------------------------------- | -------------------------------------------- |
| **A**  | Mathematisch sicher | Direkt aus Kit-Berechnung, deterministisch, unveränderlich                | Nakshatra-Grad-Grenzen, Planetenposition     |
| **B**  | Traditions-Konsens  | In mehreren Primärquellen übereinstimmend beschrieben                     | Ashwini = Heilung (3+ Quellen)               |
| **C**  | Einzelquelle        | In einer Quelle klar beschrieben, nicht breit bestätigt                   | Spezifische Yoga-Interpretation eines Autors |
| **D**  | Hypothetisch        | IC-eigene Ableitung, Cross-System-Mapping, LLM-Inferenz ohne Quellenbeleg | "Gate 34 resoniert mit Mars in Widder"       |


→ UI zeigt Evidenzklasse an. A/B = Aussage. C = "laut [Quelle]". D = Hypothesen-Sprache ("möglicherweise", "IC vermutet").

---

## 4. Architekturentscheidung: Wo laufen die Engines?

### Status: OFFEN — Entscheidung steht aus

Drei Optionen wurden evaluiert. Empfehlung: **Option C (Hybrid TS-first)**.

### Option A: Unified Python Service

```
Next.js App ←HTTP→ FastAPI (Python) ← alle Engines
                    ├── pyswisseph (HD, Astro, Jyotish)
                    ├── VedAstro.Python / jyotishganit
                    ├── tzolkin-calendar
                    └── alvamind (als Python-Port oder CLI)
```


| Pro                             | Contra                                                 |
| ------------------------------- | ------------------------------------------------------ |
| Ein Service, ein Deploy         | TS-Engines (hdkit, alvamind) müssten portiert werden   |
| pyswisseph als gemeinsamer Kern | Extra Netzwerk-Hop für jede Berechnung                 |
| Einfachste Ops                  | Python-Service = extra Infrastruktur (Docker, Hosting) |


### Option B: Mixed (TS + Python)

```
Next.js App
  ├── API Routes: hdkit (JS), alvamind (TS)
  └── ←HTTP→ FastAPI: pyswisseph, VedAstro, tzolkin-calendar
```


| Pro                                    | Contra                   |
| -------------------------------------- | ------------------------ |
| TS-Engines nativ in Next.js            | Zwei Laufzeit-Umgebungen |
| Weniger Netzwerk-Latenz für TS-Engines | Zwei Deploy-Targets      |


### Option C: Hybrid TS-first (EMPFEHLUNG)

```
Next.js App (Makerkit)
  ├── API Routes / Server Actions:
  │     ├── HD: hdkit (JS) + @swisseph/node für Berechnung
  │     ├── Ziwei Doushu: iztro (TS, MIT) ← NEU!
  │     ├── BaZi: @yhjs/bazi (TS, MIT)
  │     ├── Westl. Astro: CircularNatalHoroscopeJS (Unlicense, kein Swiss-Eph!)
  │     ├── Maya: Eigene TS-Implementierung (~50 Zeilen)
  │     ├── Numerologie / Nine Star Ki / Akan: Trivial (TS)
  │
  └── ←HTTP→ Python Microservice (FastAPI, Docker):
        ├── Jyotish: PyJHora (AGPL, isoliert, open-sourced) — max. K1/K2-Tiefe
        │            + VedAstro.Python (MIT) für KP-Ergänzung
        │            + jyotishganit (MIT) als Fallback
        ├── Westl. Astro: pyswisseph + immanuel (höchste Präzision, falls nötig)
        └── Transit-Service: pyswisseph (aktuelle Positionen)
```


| Pro                                                                    | Contra                                        |
| ---------------------------------------------------------------------- | --------------------------------------------- |
| Meiste Engines direkt in Next.js (HD, Ziwei, BaZi, Astro, Maya)        | Zwei Laufzeiten                               |
| Python-Microservice nur für Jyotish (max. Tiefe via PyJHora)           | PyJHora AGPL → Microservice-Code open-sourced |
| Kein Spark für Engines (Spark = nur GPU/LLM)                           |                                               |
| Ziwei Doushu (iztro) + BaZi (@yhjs) nativ in TS                        |                                               |
| Westl. Astro: CircularNatalHoroscopeJS (kein Swiss-Eph-Lizenzproblem!) |                                               |


**Warum kein Spark für Engines?** Spark ist für GPU-intensive Tasks (MinerU, LLM-Inferenz). Chart-Berechnungen sind CPU-leicht (~10ms) und gehören nicht auf einen GPU-Server.

**Swiss Ephemeris Lizenz:** Swiss Ephemeris ist AGPL-3.0 oder kommerziell ($600 CHF einmalig von Astrodienst). Betrifft: pyswisseph, @swisseph/node, alle Wrapper. Für kommerziellen SaaS-Betrieb → kommerzielle Lizenz kaufen ODER AGPL-konformen isolierten Service.

**PyJHora-Entscheidung (revidiert):** PyJHora als isolierter AGPL-Microservice BEHALTEN. Nur der Microservice-Code wird open-sourced — KG, App, Interpretationen bleiben privat. Begründung: PyJHora liefert die tiefste K1/K2-Abdeckung (Shadbala, Ashtakavarga, KP Sub-Lords, Jaimini, D1-D300). jyotishganit + VedAstro.Python decken ~70-75% von PyJHora ab — für IC v1 reicht das, aber langfristig ist die volle Tiefe wertvoll.

### Offene Fragen (vor Entscheidung zu klären)

- Spike: iztro in Next.js — Ziwei Doushu Basis-Chart generieren, K1/K2-Tiefe prüfen
- Spike: PyJHora als isolierter FastAPI-Microservice (Docker, AGPL-konform)
- Spike: @swisseph/node in Next.js API Route — funktioniert WASM auf Vercel/Serverless?
- Spike: CircularNatalHoroscopeJS vs. @swisseph/node — Präzisionsvergleich
- Swiss Ephemeris Lizenz: Kaufen ($600 CHF) oder AGPL-isolierter Service?
- Kann HD komplett in TS gelöst werden (geodetheseeker-Port) oder braucht es Python?

---

## 5. System-Übersicht & Kit-Kandidaten

### Lizenz-Legende


| Symbol           | Bedeutung                                                            |
| ---------------- | -------------------------------------------------------------------- |
| ✅ MIT/BSD/Apache | Frei nutzbar, kommerziell, keine Code-Offenlegung                    |
| ⚠️ AGPL-3.0      | Code muss bei Netzwerk-Nutzung veröffentlicht werden (SaaS-Problem!) |
| ⚠️ GPL-3.0       | Code muss bei Verteilung veröffentlicht werden                       |
| ❌ Proprietär     | Nicht nutzbar ohne kommerzielle Lizenz                               |
| 💰 Dual          | AGPL oder kommerzielle Lizenz kaufbar                                |


### Gesamtübersicht — Berechnungssysteme (system_role = 'calculation')


| System                  | Empfohlener Kit                                          | Lizenz         | Sprache          | K1+K2 aus Kit? | Prio |
| ----------------------- | -------------------------------------------------------- | -------------- | ---------------- | -------------- | ---- |
| **Human Design**        | hdkit + geodetheseeker (Port)                            | MIT            | JS + Python(MIT) | ~60%           | 1    |
| **Ziwei Doushu** 🆕     | **iztro** (SylarLong)                                    | MIT ✅          | **TS**           | ~75%           | 2    |
| **BaZi**                | **@yhjs/bazi** (primär) + alvamind (Fallback)            | MIT ✅          | **TS**           | ~65%           | 3    |
| **Westl. Astrologie**   | CircularNatalHoroscopeJS (TS) ODER pyswisseph (Python)   | Unlicense / 💰 | TS / Python      | ~70%           | 4    |
| **Maya Tzolkin**        | tzolkin-calendar oder TS-Port                            | MIT            | Python/TS        | ~80%           | 5    |
| **Jyotish**             | PyJHora (AGPL, Microservice) + VedAstro.Python (MIT, KP) | ⚠️ AGPL + MIT  | Python           | ~65%           | 6    |
| **Gene Keys**           | Kein eigener Calc (= HD-Positionen + Lookup)             | —              | —                | ~10% (©!)      | 7    |
| **Enneagramm**          | GitHub JSON-Strukturen                                   | Open Source    | —                | ~50%           | 8    |
| **Numerologie**         | Eigene TS-Implementierung                                | —              | TS               | ~40%           | 9    |
| **Nine Star Ki / Mewa** | Kein Kit nötig (~20 Zeilen Modulo-9)                     | —              | TS               | ~90%           | 10   |
| **Akan Day Name**       | Kein Kit nötig (~5 Zeilen Wochentag)                     | —              | TS               | ~95%           | 11   |


### Struktursysteme (system_role = 'structural') — keine Engine, nur KG

Diese berechnen kein persönliches Chart, sondern beschreiben das Terrain über das die Berechnungssysteme sprechen. Sie sind zusätzliche Netze im KG — nicht hierarchisch über den anderen. → Details: §13


| System       | Einheiten                      | Verknüpft mit                       | KG-Aufbau           |
| ------------ | ------------------------------ | ----------------------------------- | ------------------- |
| **I Ging**   | 64 Hexagramme × 6 Linien = 384 | HD (Gates = Hex 1:1), Gene Keys     | Manuell + Literatur |
| **Kabbalah** | 10 Sephiroth + 22 Pfade = 32   | HD (Zentren, behauptete Verbindung) | Manuell + Literatur |
| **Chakras**  | 7 (oder 9) Zentren             | HD (Zentren), Jyotish, Yoga         | Manuell + Literatur |


---

## 6. System-Details

### 6.1 Human Design

**Kit-Kandidaten:**


| Kit                                | Sprache          | Lizenz     | Tiefe                                                                             | Status                          |
| ---------------------------------- | ---------------- | ---------- | --------------------------------------------------------------------------------- | ------------------------------- |
| **hdkit** (jdempcy)                | JS/Node          | MIT ✅      | Gate/Kanal/Typ/Profil/Authority. KEIN Tone/Color/Base. Braucht externe Ephemeris. | Geklont: `packages/engines/hd/` |
| **geodetheseeker/human-design-py** | Python           | MIT ✅      | Komplett bis Base (Gate→Line→Color→Tone→Base). pyswisseph-basiert.                | Nicht geklont                   |
| **MicFell/human_design_engine**    | Python           | GPL-3.0 ⚠️ | Komplett bis Base.                                                                | Lizenz-Problem                  |
| **dturkuler/humandesign_api**      | Python (FastAPI) | GPL-3.0 ⚠️ | Komplett, REST-API fertig.                                                        | Lizenz-Problem                  |
| **SharpAstrology**                 | C#               | ?          | Alternative HD-Engine.                                                            | Nicht evaluiert                 |


**Empfehlung:** hdkit (JS, MIT) für Typ/Profil/Gates/Channels + **geodetheseeker** (Python, MIT) als Referenz/Port für die tieferen Ebenen (Color/Tone/Base). Langfristig: Custom TS-Engine mit @swisseph/node für alle 13 HD-Ebenen.

**K1–K4 Aufschlüsselung:**


| K1 — Numerisch (aus Kit) | K2 — Strukturregeln (aus Kit)         | K3 — Gewichtung (Literatur)             | K4 — Bedeutungen (Literatur)            |
| ------------------------ | ------------------------------------- | --------------------------------------- | --------------------------------------- |
| ✅ 64 Gate-Nummern        | ✅ Gate → Kanal Mapping                | ⚠️ Bewusstes Gate 70% / Unbewusstes 30% | ❌ Gate: Thema, Schatten, Gabe           |
| ✅ 36 Kanal-Verbindungen  | ✅ Kanal → Zentrum Mapping             | ⚠️ Definierte Zentren dominieren        | ❌ Kanal: Synergiewirkung                |
| ✅ 9 Zentren              | ✅ Typ-Bestimmungsregeln (Motor→Kehle) | ⚠️ Offene Zentren = Konditionierung     | ❌ Zentrum: Lebensprinzip                |
|                          | ✅ Profil-Kombinationen (1/1 bis 6/3)  | ⚠️ Motorstärken im Vergleich            | ❌ Profil: Lebensthema                   |
|                          | ✅ Authority-Regeln                    |                                         | ❌ Typ: Strategie & Autorität (Narrativ) |
|                          | ✅ Inkarnationskreuze (Struktur)       |                                         |                                         |


**⚠️ Gene Keys:** Schatten/Gabe/Siddhi je Gate sind urheberrechtlich geschützt (Richard Rudd). Nur Paraphrase oder eigene Ableitung möglich.

**Literatur:** Ra Uru Hu: The Definitive Book of HD | Lynda Bunnell: Dictionary of HD | Karen Curry Parker: Understanding HD

**Ziel-Nodes:** ~~9 Center + 64 Gates + 384 Lines + 6 Colors + 6 Tones + 5 Bases + 36 Channels + 5 Types + 12 Profiles + 192 Crosses = **~~700+ Nodes**

---

### 6.2 Jyotish (Vedische Astrologie) — Komplexestes System

Jyotish enthält mehrere Sub-Systeme (Parashari, KP, Jaimini) und hat die tiefste Struktur aller IC-Systeme.

**Kit-Kandidaten:**


| Kit                      | Sprache    | Lizenz       | Umfang                                            | Subsysteme                       | Bemerkung                                         |
| ------------------------ | ---------- | ------------ | ------------------------------------------------- | -------------------------------- | ------------------------------------------------- |
| **VedAstro.Python**      | Python     | MIT ✅        | 596+ Berechnungen, 47 Ayanamsa                    | Parashari, teilw. KP             | Umfangreichste MIT-Lib. 9 Jahre aktiv.            |
| **jyotishganit**         | Python     | MIT ✅        | Professionell, NASA JPL Ephemeris                 | Parashari, Dashas, Vargas        | Type-checked, black-formatiert.                   |
| **PyJHora**              | Python     | AGPL ⚠️      | Maximum (D-1 bis D-300, 20 Ayanamsa, ~6300 Tests) | Parashari + KP + Jaimini + Raman | Vollständigste Lib, aber AGPL = SaaS-Showstopper  |
| **VedicAstro (diliprk)** | Python     | MIT ✅        | KP-fokussiert, Sub-Lords, Signifikanten           | KP (Krishnamurti Paddhati)       | Basiert auf flatlib (sidereal). 53 Stars.         |
| **jyotishyamitra**       | Python     | MIT ✅        | Basis (Planeten, Nakshatras, JSON-Output)         | Parashari Basis                  | Einfach, gut für Prototyp. 23 Stars.              |
| **node-jhora**           | TypeScript | ❌ PROPRIETÄR | Umfangreich (WASM Swiss Eph)                      | Parashari, KP, Jaimini           | Source-Available, Royalty-Pflicht! NICHT nutzbar. |


**Empfehlung (revidiert):** **PyJHora** (AGPL) als primäre Engine im isolierten Python-Microservice — Code wird open-sourced, App bleibt privat. Maximale K1/K2-Tiefe (Shadbala, Ashtakavarga, KP, Jaimini, D1-D300). **VedAstro.Python** (MIT) als KP-Ergänzung. **jyotishganit** (MIT) als lizenzfreier Fallback (NASA JPL statt Swiss Ephemeris).

**⚠️ Wichtig: node-jhora ist NICHT open source.** Trotz GitHub-Verfügbarkeit hat es eine proprietäre "Source Available"-Lizenz mit Royalty-Pflicht. In der Vordiskussion fälschlicherweise als Open Source empfohlen.

**KP-System (Krishnamurti Paddhati):** Modernisierte, regelbasierte Variante von Jyotish. Algorithmus-freundlich. Nutzt Placidus-Häuser + eigene Ayanamsha + Sub-Lord-System. VedicAstro (diliprk) deckt KP ab; VedAstro.Python teilweise.

**Subsysteme und Umschaltung:** Jyotish erlaubt per Parameter-Wechsel verschiedene Schulen:

- Parashari (Standard): `ayanamsa=LAHIRI, bhava_system=EQUAL`
- KP: `ayanamsa=KP, bhava_system=PLACIDUS`
- Jaimini: Eigene Dashas (Chara), Karakas, Arudha Padas

In der App: Tab/Dropdown für System-Wechsel mit denselben Geburtsdaten.

**K1–K4 Aufschlüsselung:**


| K1 — Numerisch (aus Kit)        | K2 — Strukturregeln (aus Kit)       | K3 — Gewichtung (Literatur)        | K4 — Bedeutungen (Literatur)            |
| ------------------------------- | ----------------------------------- | ---------------------------------- | --------------------------------------- |
| ✅ Nakshatra Grad-Grenzen (27)   | ✅ Nakshatra-Lord-Sequenz            | ⚠️ Exaltierter Planet = 3x Stärke? | ❌ Nakshatra: Guna, Devata, Symbol, Tier |
| ✅ Graha-Positionen (9 Planeten) | ✅ Graha-Rashi-Herrschaft            | ⚠️ Rahu verstärkt Konjunktion      | ❌ Graha: Archetyp, Qualität, Wirkung    |
| ✅ Ayanamsa-Berechnung           | ✅ Exaltationen & Debilitationen     | ⚠️ Vargottama-Gewichtung           | ❌ Bhava: Lebensbereich, Bedeutung       |
| ✅ Vimshottari Dasha-Längen      | ✅ Haus-Kategorien (Kendra, Trikona) | ⚠️ KP: Sub-Lord > Lord             | ❌ Yoga: Auswirkung & Kontext            |
| ✅ Varga-Chart Divisoren         | ✅ Planetenfreundschaften            | ⚠️ Planeten in Kendra stärken Haus | ❌ Schatten & Gabe je Nakshatra          |
|                                 | ✅ Yoga-Erkennungsregeln             |                                    |                                         |
|                                 | ✅ KP Sub-Lord Logik                 |                                    |                                         |


**Prüfen:** Extraktion-Script für VedAstro.Python — Nakshatras, Lords, Rashis, Grahas → JSON. Dann prüfen welche K2-Felder tatsächlich als Konstanten im Code stecken.

**Literatur:** Bepin Behari: Myths & Symbols of Vedic Astrology | B.V. Raman: 300 Important Combinations | K.N. Rao: Navamsa in Astrology | PVR Narasimha Rao: Vedic Astrology — An Integrated Approach

**Ziel-Nodes:** ~~9 Grahas + 12 Rashis + 27 Nakshatras + 108 Padas + 12 Bhavas + 50+ Yogas + Dasha-Perioden + Vargas = **~~500-800 Nodes** (vor Interpretationen)

---

### 6.3 Westliche Astrologie

**Kit-Kandidaten:**


| Kit                             | Sprache | Lizenz        | Umfang                                                  | Bemerkung                                                          |
| ------------------------------- | ------- | ------------- | ------------------------------------------------------- | ------------------------------------------------------------------ |
| **CircularNatalHoroscopeJS** 🆕 | ES6/TS  | Unlicense ✅   | Tropical+Sidereal, 7 Häusersysteme, Aspekte, Retrograde | KEIN Swiss-Eph — eigene Berechnung. 354 Stars. Kein Lizenzproblem! |
| **@nrweb/astro-calc** 🆕        | TS      | MIT ✅         | Planeten, Häuser, Aspekte, Arab. Lots, Scoring          | NUTZT Swiss Ephemeris → AGPL/Komm. Lizenzfrage bleibt.             |
| **pyswisseph**                  | Python  | 💰 AGPL/Komm. | Industriestandard, höchste Präzision                    | Swiss Ephemeris Wrapper. $600 CHF für kommerziell.                 |
| **immanuel**                    | Python  | MIT ✅         | Natal, Solar Returns, Progressions, Composites          | Baut auf pyswisseph auf.                                           |
| **Kerykeion**                   | Python  | AGPL ⚠️       | Gut dokumentiert, aktiv (602 Stars)                     | AGPL = SaaS-Problem                                                |
| **@swisseph/node**              | Node.js | 💰 AGPL/Komm. | Swiss Ephemeris für Node.js, WASM                       | Höchste Präzision in TS                                            |
| **flatlib**                     | Python  | MIT ✅         | Basis-Astrologie                                        | Älter, weniger aktiv                                               |


**Empfehlung:** **CircularNatalHoroscopeJS** (Unlicense, TS-nativ, kein Swiss-Eph) als TS-first-Lösung für Next.js. Für höchste Präzision (Forschungsgrad): pyswisseph + immanuel im Python-Microservice. Spike nötig: Präzisionsvergleich CircularNatalHoroscopeJS vs. Swiss Ephemeris.

**K1–K4 Aufschlüsselung:** Analog zu Jyotish — Kits liefern K1+K2 (Positionen, Aspekte, Häuser), K3+K4 aus Literatur.

**Ziel-Nodes:** ~~10 Planeten + 12 Zeichen + 12 Häuser + Aspekttypen + Rulerships = **~~100-150 Nodes**

---

### 6.4 BaZi (Four Pillars)

**Kit-Kandidaten:**


| Kit                          | Sprache | Lizenz | Umfang                                                                                         | Bemerkung                                                                        |
| ---------------------------- | ------- | ------ | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **@yhjs/bazi** 🆕            | TS      | MIT ✅  | Stems, Branches, Ten Gods, Nayin, **Luck Cycles**, Twelve Life Stages, Supernatural Indicators | Zero deps, basiert auf Shouxing Astronomical Calendar. Teil des @yhjs Monorepos. |
| **alvamind/bazi-calculator** | TS      | MIT ✅  | Stems, Branches, Elements, Hidden Stems, FiveFactors                                           | Keine Luck Pillars, kein Nayin. Bereits geklont.                                 |
| **bazica**                   | Go      | ?      | Aktiv 2025                                                                                     | Alternativer Ansatz                                                              |


**Empfehlung:** **@yhjs/bazi** (MIT, TS, umfangreicher) als primärer Kit. alvamind als Fallback. @yhjs deckt Luck Cycles + Nayin + Twelve Life Stages ab, die alvamind fehlen.

**Ziel-Nodes:** 10 Stems + 12 Branches + 60 Jiazi + 10 Ten Gods + 5 Elements + Luck Pillars + Nayin = **~150-200 Nodes**

---

### 6.5 Maya Tzolkin


| Kit                  | Sprache | Lizenz | Umfang                                  |
| -------------------- | ------- | ------ | --------------------------------------- |
| **tzolkin-calendar** | Python  | MIT ✅  | 20 Seals, 13 Tones, 260 Kin, Wavespells |


Einfachstes System. Kit sollte vollständig sein. Alternative: Triviale TS-Implementierung (~50 Zeilen).

**Ziel-Nodes:** 20 Seals + 13 Tones + 260 Kin + 20 Wavespells + 5 Earth Families = **~320 Nodes**

---

### 6.6 Ziwei Doushu (紫微斗数 / Purpurstern-Astrologie) — NEU

Ziwei Doushu ist das technisch ausgefeilteste chinesische System — strukturell vergleichbar mit Jyotish in Tiefe und Komplexität. Mondkalender-basiert, 14 Hauptsterne + 30+ Nebensterne, 12 Paläste. Ergänzt BaZi fundamental (BaZi = Sonnenkalender/Elemente, Ziwei = Mondkalender/Sterne).

**Kit:**


| Kit                   | Sprache    | Lizenz | Stars | Umfang                                                                                                |
| --------------------- | ---------- | ------ | ----- | ----------------------------------------------------------------------------------------------------- |
| **iztro** (SylarLong) | TypeScript | MIT ✅  | 3.5k+ | 14 Hauptsterne, 30+ Nebensterne, 12 Paläste, Mutagen-System (四化), verschiedene Schulen konfigurierbar |
| **iztro-hook**        | React      | MIT ✅  | 46    | React-Hook-Wrapper für iztro                                                                          |


**Warum iztro ein Glücksfund ist:**

- TS-nativ → direkt in Next.js, kein Python nötig
- MIT-Lizenz → keine Lizenzprobleme
- Multi-language Output (EN/CN/JP/KR/VI)
- React-Komponente verfügbar
- 610+ Commits, sehr aktiv maintained
- K1+K2 sehr vollständig aus dem Kit extrahierbar

**K1–K4 Aufschlüsselung:**


| K1+K2 (aus iztro, ~75%)                                                                                                      | K3 (Literatur)              | K4 (Literatur)                    |
| ---------------------------------------------------------------------------------------------------------------------------- | --------------------------- | --------------------------------- |
| ✅ 14 Hauptsterne + Positionen                                                                                                | ⚠️ Stern-Stärke in Palästen | ❌ Stern: Archetyp, Qualität       |
| ✅ 30+ Nebensterne                                                                                                            | ⚠️ Mutagen-Gewichtung       | ❌ Palast: Lebensbereich-Bedeutung |
| ✅ 12 Paläste (Leben, Eltern, Wohlstand, Gesundheit, Kinder, Beziehung, Migration, Freunde, Karriere, Immobilien, Glück, Ich) | ⚠️ Schulen-Unterschiede     | ❌ Stern-Palast-Kombinationen      |
| ✅ Mutagen-System (四化)                                                                                                        |                             | ❌ Zeitperioden-Bedeutungen        |
| ✅ Verschiedene Schulen konfigurierbar                                                                                        |                             |                                   |


**Cross-System-Potenzial:**

- Ziwei 12 Paläste ↔ Jyotish 12 Bhavas ↔ Westl. Astro 12 Häuser → direktes Mapping
- Ziwei Sterne ↔ Jyotish Grahas → Funktions-Mapping (nicht 1:1, aber konzeptuell)
- BaZi 5 Elemente sind auch in Ziwei relevant → intra-chinesisches Mapping

**Varianten:** Tu Vi (Vietnam) ist eine eigenständige Variante von Ziwei Doushu. iztro unterstützt bereits Vietnamesisch als Sprache.

**Ziel-Nodes:** 14 Hauptsterne + 30+ Nebensterne + 12 Paläste + Mutagen + Perioden = **~200-300 Nodes**

---

### 6.7 Gene Keys


| Aspekt           | Detail                                                                                                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Engine           | Kein eigenständiger Calculator — nutzt identische Planetenpositionen wie HD                                                                                               |
| Methode          | pyswisseph/@swisseph/node + Lookup-Tabelle (64 Hexagramme auf 360° Zodiak)                                                                                                |
| Output           | 64 Gene Keys × 3 Frequenzen (Shadow/Gift/Siddhi) × Sphären                                                                                                                |
| **⚠️ Copyright** | Gene Keys Inhalte (Schatten/Gabe/Siddhi) sind urheberrechtlich geschützt (Richard Rudd). Nur Paraphrase oder eigene Ableitung. K4 = ausschließlich eigene Interpretation. |


---

### 6.7 Enneagramm

**Besonderheit:** Kein Geburtsdaten-basiertes System. Typ wird per Fragebogen/Selbsteinschätzung ermittelt.

**K1–K4 Aufschlüsselung:**


| K1+K2 (Struktur, aus GitHub JSONs)              | K3 (Literatur)                | K4 (Literatur)                       |
| ----------------------------------------------- | ----------------------------- | ------------------------------------ |
| ✅ 9 Typen, Triade-Zuordnung                     | ⚠️ Entwicklungsniveaus (1-9)  | ❌ Kernmotivation, Grundangst         |
| ✅ Flügel-Struktur                               | ⚠️ Dominanz Triade vs. Flügel | ❌ Untertypen (3 je Typ)              |
| ✅ Pfeil-Richtungen (Integration/Desintegration) | ⚠️ Stressmuster-Gewichtung    | ❌ Schattenmuster, Transformationsweg |
| ✅ Untertyp-Kategorien                           |                               | ❌ Flügel-Nuancen                     |


**Literatur:** Don Riso & Russ Hudson: Personality Types | Beatrice Chestnut: The Complete Enneagram | Sandra Maitri: The Spiritual Dimension

---

### 6.8 Numerologie


| Aspekt | Detail                                                                          |
| ------ | ------------------------------------------------------------------------------- |
| Engine | numerology (Python/PyPI, ~40 Stars, Pythagorean) oder eigene TS-Implementierung |
| Input  | Name + Geburtsdatum (neuer Input-Typ!)                                          |
| Output | Life Path, Heart's Desire, Personality, Destiny, Personal Year                  |
| K1+K2  | ~40% aus Kit (Berechnungslogik). Fast alles Semantische aus Literatur.          |


---

### 6.9 Nine Star Ki / Akan Day Name

Triviale Systeme. Kein Kit nötig.


| System        | Berechnung                | Aufwand       |
| ------------- | ------------------------- | ------------- |
| Nine Star Ki  | Modulo-9-Berechnung       | ~20 Zeilen TS |
| Akan Day Name | Wochentag → 1 von 7 Names | ~5 Zeilen TS  |


---

## 7. Extraktions-Prozess & LLM-Modi

MinerU + LLM läuft auf Spark (GPU) in drei Modi — je nach Ziel-Kategorie:


| Modus | Ziel                                | Prompt-Kern                                                                                                          | Output → Tabelle                                                 |
| ----- | ----------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **A** | K3: Regeln & Gewichtungen           | "Identifiziere alle Wenn-Dann-Regeln, Gewichtungen und Stärkeverhältnisse."                                          | → sys_kg_edges (condition, effect, evidence, source)             |
| **B** | K4a: Qualitative Eigenschaften      | "Extrahiere alle Eigenschaften von [Konzept X]: Guna, Symbol, Devata, Dosha. Nur diskrete Werte."                    | → sys_kg_nodes.properties JSONB                                  |
| **C** | K4b: Bedeutungen & Interpretationen | "Extrahiere alle Bedeutungsaussagen zu [Konzept X]. Format: Kontext (Stärke/Schatten/Einladung), Text, Evidenzgrad." | → sys_interpretations (node_id, context, text, evidence, source) |


**Reihenfolge:** Erst K1+K2 aus Kits seeden (Struktur steht) → dann K3 (Modus A) → dann K4a (Modus B) → dann K4b (Modus C).

**Details:** → pipeline.md §6–8 für vollständige Pipeline-Architektur.

---

## 8. Prüf-Checkliste (je System)

Für jedes System diese 4 Schritte durchführen — in dieser Reihenfolge:

### Schritt 1 — Kit installieren & Struktur extrahieren

- Kit klonen / installieren
- Basis-Output erzeugen (Beispielchart berechnen)
- Code nach Konstanten und Lookup-Tabellen durchsuchen
- Alle extrahierbaren Listen in JSON exportieren (K1+K2)
- JSON reviewen: Was fehlt? (→ Schritt 2)

### Schritt 2 — Differenz identifizieren (K1–K4)

- Was fehlt in K1? (Welche numerischen Felder sind nicht im Kit?)
- Was fehlt in K2? (Welche Strukturregeln fehlen als Konstante?)
- K3-Kandidaten sammeln: Welche Gewichtungsregeln werden im Kit vorausgesetzt aber nicht definiert?
- K4-Felder definieren: Was soll später aus Literatur extrahiert werden?
- Lücken durch strukturierte Quellen füllen (Wikipedia, Wikia → LLM-assistiert + Review)

### Schritt 3 — Literatur identifizieren

- Primärquellen je System auflisten (Autor, Titel, Ausgabe)
- PDFs beschaffen (legal: Kauf, Open Access, Bibliothek)
- Priorität festlegen: Welches Buch deckt K3+K4 am vollständigsten?
- MinerU-Extraktion testen (Qualität prüfen)

### Schritt 4 — Seed aufbauen & Interpretationen extrahieren

- Seed-Script schreiben: JSON → sys_kg_nodes + sys_kg_edges INSERT
- In Supabase Dev-DB importieren
- Vollständigkeit prüfen: Alle Entitäten vorhanden?
- LLM-Extraktion für K3 starten (Modus A → Regeln)
- LLM-Extraktion für K4a starten (Modus B → Eigenschaften)
- LLM-Extraktion für K4b starten (Modus C → Bedeutungen)
- Human-in-the-Loop Review (Evidenzklassen vergeben)
- Embeddings generieren (pgvector)

---

## 9. Engine-Integration-Pattern

```
Geburtsdaten (Datum, Uhrzeit, Ort)
  ↓
Engines berechnen parallel:
  ├→ hdkit/@swisseph   → HD-Chart       (TS, Next.js)
  ├→ iztro             → Ziwei-Chart    (TS, Next.js) ← NEU
  ├→ @yhjs/bazi        → BaZi-Chart     (TS, Next.js)
  ├→ CircularNatalJS   → Astro-Chart    (TS, Next.js)
  ├→ PyJHora           → Jyotish-Chart  (Python, Microservice)
  ├→ tzolkin-calendar  → Maya-Kin       (Python oder TS)
  └→ eigene Logik      → Num, NSK, Akan (TS, Next.js)
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

### Text-Generierung: Drei Kategorien


| Kategorie              | Was                                                      | Wann generiert                                  | Gespeichert                        |
| ---------------------- | -------------------------------------------------------- | ----------------------------------------------- | ---------------------------------- |
| **A — Statisch**       | Geburtschart-Interpretationen ("Dein Mond in Rohini...") | Einmalig bei Onboarding                         | user_charts + user_profiles        |
| **B — Semi-dynamisch** | Dasha-Perioden, Jahres-Zyklen                            | Bei Perioden-Wechsel (Scheduler)                | user_charts (mit Gültigkeitsdatum) |
| **C — Dynamisch**      | Tages-/Wochen-Transite ("Heute steht Jupiter...")        | Täglich (Batch) + persönlicher Bezug on-the-fly | 24h Cache                          |


---

## 10. Wo die Kits wohnen

Die Open-Source-Kits werden **geklont** und leben **im gleichen Repo** wie die App.

**Ort im Repo (verbindlich):**

```
code/inner_compass_app/
  packages/
    engines/
      hd/           ← hdkit (JS/Node, MIT)
      ziwei/        ← iztro (TS, MIT) ← NEU
      bazi/         ← @yhjs/bazi (TS, MIT) — alvamind als Fallback
      astro/        ← CircularNatalHoroscopeJS (Unlicense) + pyswisseph (AGPL/Komm.)
      maya/         ← tzolkin-calendar (Python, MIT)
      jyotish/      ← PyJHora (AGPL, isolierter Microservice) + VedAstro.Python (MIT, KP)
```

**Zwei Nutzungen:**


| Nutzung             | Wann                             | Wo                                                      |
| ------------------- | -------------------------------- | ------------------------------------------------------- |
| **Struktur parsen** | Phase 1, einmalig pro Kit-Update | Parser-Script liest Kits → JSON → Seed                  |
| **Chart berechnen** | Laufzeit (User-Onboarding)       | Engine-Service (TS in Next.js oder Python-Microservice) |


**Committen:** Empfohlen: Variante A (Code im Repo) — `.git` entfernen, committen. Details: `packages/engines/README.md`.

---

## 11. Parsing aus den Kits — was ansteht

**Was pro System geparst werden soll:**


| System       | Im Kit zu finden / zu parsen                                                  | Ziel                                                       | Prio |
| ------------ | ----------------------------------------------------------------------------- | ---------------------------------------------------------- | ---- |
| **HD**       | Centers, Gates, Channels, Profile. hdkit: `bodygraph-data.js`, `constants.js` | structure.centers, structure.channels                      | 1    |
| **Ziwei** 🆕 | 14 Hauptsterne, 30+ Nebensterne, 12 Paläste, Mutagene. iztro: `src/data/`     | structure.stars, structure.palaces                         | 2    |
| **BaZi**     | Stems, Branches, Jiazi, Ten Gods, Nayin, Luck Cycles. @yhjs/bazi: TS-Types    | structure.stems, structure.branches, structure.luck_cycles | 3    |
| **Astro**    | Planeten, Zeichen, Häuser, Rulerships. CircularNatalJS + pyswisseph           | structure.planets, structure.signs                         | 4    |
| **Maya**     | 20 Seals, 13 Tones, Kin-Mapping. tzolkin-calendar: Kalender-Logik             | structure.seals, structure.tones                           | 5    |
| **Jyotish**  | Nakshatras, Grahas, Rashis, Bhavas, Dasha-Systeme. PyJHora + VedAstro         | Komplexeste Extraktion                                     | 6    |


**Konkrete nächste Schritte:**

1. **HD:** Dateien identifizieren (bodygraph, constants, channel/gate-Mappings). Parser → JSON.
2. **Jyotish:** VedAstro.Python installieren, alle extrahierbaren Konstanten identifizieren, K1+K2-Differenz dokumentieren.
3. **BaZi / Astro / Maya:** Analog — Parser → JSON → Seed.

**Deskriptor vs. Seed vs. Structure:** Siehe [reference/structure_descriptor_seed.md](../reference/structure_descriptor_seed.md).

---

## 12. Visualisierung (Übersicht)

Für Chart-Darstellung in der App (KARTE-Space):


| Einsatz                             | Kandidaten                              | Sprache     | Bemerkung                                      |
| ----------------------------------- | --------------------------------------- | ----------- | ---------------------------------------------- |
| Jyotish-Charts (North/South Indian) | jyotichart (SVG), astrochartjs          | Python / JS | North Indian (Diamant), South Indian (Quadrat) |
| Ziwei Doushu Astrolabe              | iztro-hook (React), Custom SVG          | TS          | 12-Paläste-Gitter mit Sternen                  |
| Western Astro Wheel                 | CircularNatalHoroscopeJS, astrochart.js | JS          | Radix-Chart                                    |
| HD BodyGraph                        | hdkit Sample-App, Custom SVG            | JS          | Eigenentwicklung wahrscheinlich                |
| BaZi Pillars                        | Custom HTML/CSS                         | TS          | Einfach (4 Säulen)                             |
| Maya Kin                            | Custom HTML/CSS                         | TS          | Einfach (Seal + Ton)                           |


→ Details: architecture.md §14 (Chart-Visualisierungen)

---

## 13. Zwei Arten von Systemen im KG & IC-Sprache

### Das Kernprinzip

Im KG gibt es zwei funktional verschiedene Arten von Systemen. Technisch sind sie gleich modelliert (`sys_kg_nodes`, `sys_kg_edges`), aber sie spielen verschiedene Rollen:


|                      | Berechnungssystem (`calculation`)     | Struktursystem (`structural`)           |
| -------------------- | ------------------------------------- | --------------------------------------- |
| **Berechnet Chart?** | Ja (Engine)                           | Nein                                    |
| **Personalisiert?**  | Ja (pro Geburtsdaten)                 | Nein (universal)                        |
| **Beispiel**         | HD, Jyotish, BaZi, Ziwei, Astro, Maya | I Ging, Kabbalah, Chakras, Enneagramm   |
| **Rolle im KG**      | "Was ist bei DIR aktiv?"              | "Was BEDEUTET das, kulturübergreifend?" |


In `sys_systems` wird die Rolle als Feld `system_role` gespeichert ('calculation' oder 'structural'). Kein System steht hierarchisch über einem anderen — Struktursysteme sind zusätzliche Netze die man mit drüberlegt.

### Struktursysteme im KG


| System        | system-ID  | Knoten                                                                                                                                          | Wozu                                                                            |
| ------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| I Ging        | `i_ching`  | 64 Hex + 384 Linien + 8 Trigramme                                                                                                               | Fundament für HD Gates + Gene Keys. Faktische 1:1-Identität.                    |
| Kabbalah      | `kabbalah` | 10 Sephiroth + 22 Pfade                                                                                                                         | Weitere Perspektive auf HD Zentren (behauptete Verbindung, nicht faktisch 1:1). |
| Chakras       | `chakra`   | 7-9 Zentren                                                                                                                                     | Weitere Perspektive auf HD Zentren + Jyotish Körper-Bezüge.                     |
| Fünf Elemente | —          | Nicht als EIN System modelliert. Wu Xing (BaZi/Ziwei), Pancha Bhuta (Jyotish), westl. 4 Elemente sind **verschiedene** Systeme, nicht dasselbe. | Cross-System-Mapping entdeckt Ähnlichkeiten empirisch.                          |


**Warum kein "Tier 0" oder "Basisstrukturen"-Hierarchie?** Weil das manche Traditionen als "fundamentaler" behandeln würde als andere. I Ging ist nicht wahrer als Jyotish — es ist eine andere Linse. Die Verbindungen zwischen Systemen (z.B. HD Gate 34 basiert auf I Ging Hex 34) werden als reguläre `cross_system`-Edges modelliert, nicht als hierarchische Schichten.

### Wie die IC-Sprache entsteht

Alle Systeme (Berechnungs- und Struktursysteme) bilden jeweils eigene Netze im KG. Wenn man diese Netze übereinanderlegt, entstehen **Klumpen** — Stellen wo Knoten aus verschiedenen Systemen semantisch eng beieinanderliegen.

```
Phase 3 (Cross-System-Mapping):
  Embeddings aller K4-Interpretationen berechnen
  → Cosine-Similarity zwischen Systemen
  → Klumpen identifizieren (z.B. HD Gate 34, Jyotish Mars,
    BaZi Yang-Feuer, Ziwei Greedy Wolf liegen nah beieinander)

Phase 4 (IC-Sprache / Meta-Knoten):
  LLM bekommt ALLE Interpretationen eines Klumpens:
    "HD: 'rohe sakrale Kraft, wartet auf Reaktion'
     Jyotish: 'Mars — Mut, Aggression, Initiierung'
     BaZi: 'Yang-Feuer — Expansion, Ambition'
     Ziwei: 'Greedy Wolf — Antrieb, Charisma, Unruhe'
     I Ging: 'Hex 34 — Donner unter Himmel, Große Stärke'"
  
  Auftrag: "Was ist der gemeinsame Kern, der UNTER
    den kulturellen Färbungen liegt?"
  
  → IC-Konzept: "Verkörperte Initialkraft — die angeborene
    Kapazität, Energie in Handlung umzusetzen."
  
  Human Review: Bestätigen / Verfeinern / Ablehnen
  → sys_kg_nodes (system='meta')
```

Das Ergebnis ist eine **eigene IC-Sprache**: Konzepte die keine einzelne Tradition so benennt, die aber den kulturübergreifenden Kern treffen. Jede Tradition sieht einen Aspekt (Mars/Kraft/Feuer/Ehrgeiz) — das IC-Konzept versucht, das zu benennen was **darunter** liegt.

### Ausgabe an den User

Die IC-Sprache ist die **Hauptstimme**. Die Systeme sind die Quellenangaben:

```
"VERKÖRPERTE INITIALKRAFT
 Das ist ein zentrales Thema deiner Signatur.

 [Quellen]
   HD: Gate 34 — sakrale Kraft
   Jyotish: Mars in Widder — Mut & Antrieb
   BaZi: Yang-Feuer — Expansion
   Ziwei: Greedy Wolf — Ehrgeiz & Charisma

 [Spannungsfeld]
   HD empfiehlt: Warte auf die sakrale Reaktion
   Jyotish empfiehlt: Handle mutig und sofort
   → Diese Spannung ist selbst eine Information"
```

Die Divergenzen (verschiedene Empfehlungen) werden nicht versteckt, sondern als eigene Erkenntnisquelle gezeigt.

→ Technische Details: architecture.md §15 (KG-Übereinanderlegen & IC-Sprache)

---

## 14. Kulturelle Abdeckung & Systemlandschaft

### Abgedeckte Kulturen


| Kultur                 | Berechnungssysteme (Engine) | Struktursysteme (nur KG)           |
| ---------------------- | --------------------------- | ---------------------------------- |
| **Südasien**           | Jyotish                     | Chakras                            |
| **Ostasien**           | Ziwei Doushu, BaZi          | I Ging, Nine Star Ki / Mewa        |
| **Westen**             | Westl. Astrologie           | Kabbalah                           |
| **Mesoamerika**        | Maya Tzolkin                |                                    |
| **Westafrika**         |                             | Akan Day Name                      |
| **Tibet**              |                             | Mewa (Brücke Jyotish↔BaZi)         |
| **Modern/Synthetisch** | Human Design                | Gene Keys, Enneagramm, Numerologie |


### Ehrliche Lücken (ohne verfügbare Alternative)


| Region                         | Grund                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------- |
| Australien/Ozeanien            | Kein geburtsbasiertes Berechnungssystem (Traumzeit = kosmologisch, nicht algorithmisch) |
| Sub-Sahara Afrika (außer Akan) | Ifa/Yoruba = Orakel (Ritual, kein Algorithmus) — als Archetypenlayer möglich (Tier 3)   |
| Indigenes Nordamerika          | Medicine Wheel — geburtsbasiert aber Authentizitätsprobleme (New-Age-Vereinnahmung)     |
| Arabisch/Persisch              | Bereits in westlicher Astrologie absorbiert                                             |
| Slavisch/Nordisch              | Kein systematisiertes Geburtssystem                                                     |


**Transparenz-Prinzip:** IC kommuniziert offen, welche Kulturen abgedeckt sind und wo ehrliche Grenzen liegen. Das gehört zur Systemintegrität.

### Mögliche Tier-3-Ergänzungen (Archetypenlayer, kein Engine)


| System                  | Kultur      | Einheiten            | Aufwand                 | Wert für KG                    |
| ----------------------- | ----------- | -------------------- | ----------------------- | ------------------------------ |
| Ifa/Yoruba Odus         | Westafrika  | 256 Odus             | Hoch (Literatur)        | Archetypensystem, nicht Engine |
| Aztekisch/Tonalpohualli | Mesoamerika | 260 Tage (wie Maya)  | Niedrig (Maya-Verwandt) | Ergänzt Maya-Perspektive       |
| Kabbalah Lebenspfad     | Jüdisch     | Gematria + Sephiroth | Mittel                  | Bereits als Basisstruktur B2   |
| Äthiopische Tradition   | Ostafrika   | Heiligen-Kalender    | Hoch (wenig Quellen)    | Einzigartig aber schwer        |


---

## 15. Ziwei Doushu (iztro) — Phase 1 abgeschlossen (Spike → Bewerten → Contract → Mapping)

> Code: `code/inner_compass_app/packages/engines/` — `computeZiweiRaw`, `computeZiweiChart`, `buildZiweiCanonicalNodes`.

### 15.1 Bewertung (1b) — Entscheidung **Keep**


| Kriterium | Einschätzung                                                                                                                                                                                                         |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lizenz    | MIT — vereinbar mit Closed-Source-App.                                                                                                                                                                               |
| Stack     | TS, npm, aktiv gepflegt (Stand: iztro ^2.5.x im Monorepo-Katalog).                                                                                                                                                   |
| Abdeckung | 12 Paläste, Haupt-/Neben-/Zusatzsterne, Vier-Wandlungen, Helligkeiten, Konfig/Plugins für Schulen.                                                                                                                   |
| Risiken   | Kein Swiss-Eph-Bezug (chinesischer Kalender-Pfad); **keine** Nutzung von `latitude`/`longitude`/`timezone` im nativen Plate — nur Solar-/Lunar-Datum + Stunden-Index (IC speichert Geo trotzdem für andere Systeme). |
| Wartung   | Abhängigkeit von `lunar-typescript` / `lunar-lite` — mit semver im Blick halten.                                                                                                                                     |


**Kein Ersatz nötig** für Phase 1; spätere Validierung gegen Referenzliteratur (K3/K4) ist unabhängig vom Kit.

### 15.2 Contract (1c) — Stabile API

- **Input:** `ZiweiComputeInput` — `BirthData` + `gender` (`male`  `female`  `男`  `女`) + optional `language`, `fixLeap`.
- **Output:** `ZiweiChartSerialized` — typisiertes JSON-äquivalent des iztro-Ergebnisses inkl. `_ic.engine`, `_ic.timeIndex`.
- **Fehler:** `ZiweiEngineError` mit Codes `INVALID_DATE`, `INVALID_TIME`, `IZTRO_RUNTIME`.

### 15.3 Extraktion / Canonical IDs (1d)

Format: `{system}.{element_type}.{element_id}` (siehe contracts.md §9).


| element_type | element_id                                            | Herkunft                                             |
| ------------ | ----------------------------------------------------- | ---------------------------------------------------- |
| `palace`     | iztro-Palast-Key (z. B. `soulPalace`, `spousePalace`) | Umkehr der iztro-Locale `zh-CN/palace` — Label → Key |
| `star`       | iztro-Stern-Key (z. B. `ziweiMaj`, `tianjiMaj`)       | Umkehr der iztro-Locale `zh-CN/star` — Label → Key   |


Pro Chart werden **12 Palast-Nodes** plus **distinct Stern-Instanzen** (nach iztro-Key dedupliziert) in `nodes[]` geführt. Andere Ausgabe-Sprachen: Fallback `ziwei.palace.idx_<n>` bzw. `ziwei.star.h_<hash>` bis Locale-Mapping erweitert wird.

**Schritt 1 (Katalog):** `ziwei_catalog_v0.json` — iztro: Locales + `STARS_INFO` + Konstanten + **`heavenlyStems` / `earthlyBranches`** (阴阳五行、冲、命主身主、天干四化、提示文本等), `schema_version` ≥ 1.1. Script: `extract:ziwei-catalog`. *Hinweis:* `stars_info` nur bei Teilmenge der Sterne.

**Schritt 2 (Struktur v0):** `ziwei_structure_v0.json` — **6 Ebenen**, **statische Kanten** inkl. Palast-Ring, 五虎遁/五鼠遁, **干冲/支冲**, **命主/身主 → Stern**, **stem_mutagen_**\* (禄权科忌), **`life_domain_map`**. Script: `build:ziwei-structure`. Stern→Palast: Laufzeit.

**Schritt 3 (Abgleich Engine ↔ Katalog):** `validateZiweiNodesAgainstCatalog` in `@ic/engines` — jeder Eintrag in `computeZiweiChart().nodes` muss ein bekannter Palast-/Stern-Key aus `ziwei_catalog_v0.json` sein, oder ein dokumentierter Fallback (`idx_*` Palast, `h_*` Stern-Hash bei nicht-zh-CN-Labels). Test: `ziwei-catalog-validation.test.ts` (läuft in `pnpm --filter @ic/engines run test:unit`).

**Deskriptor / KG-Seed:** Nächster technische Schritt ist **Materialisierung** in `sys_kg_*` aus Katalog + Structure + validierten Chart-Nodes, nicht mehr reine Engine-Eval.

---

## 16. BaZi (Four Pillars) — @yhjs/bazi + @yhjs/bagua (Phase 1 gleiches Muster wie Ziwei)

> Code: `computeBaziRaw` / `computeBaziChart`, `buildBaziCanonicalNodes`, Vitest `bazi-*`. Katalog: `bazi_catalog_v0.json` — **@yhjs/bagua** (60甲子等) + **`shensha_aux`** (Spiegel `@yhjs/bazi`, schema ≥ 1.2). `extract:bazi-catalog`.

### 16.1 Bewertung — Entscheidung **Keep** (Spike)


| Kriterium | Einschätzung                                                                                                                                                                 |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lizenz    | MIT                                                                                                                                                                          |
| Stack     | TS, `Bazi.create({ datetime, gender })`, `toJSON()`                                                                                                                          |
| Risiko    | **Datetime:** `birth.date` + `birth.time` werden zu einem lokalen `Date` zusammengezogen — für produktive Nutzung iana-Zeitzonen korrekt auflösen (siehe `_ic.note` im Raw). |


### 16.2 Canonical IDs (Auszug)


| Präfix                                | Beispiel                       | Bedeutung                                                  |
| ------------------------------------- | ------------------------------ | ---------------------------------------------------------- |
| `bazi.stem.`*                         | `bazi.stem.geng`               | 天干 (Slug pinyin)                                           |
| `bazi.branch.*`                       | `bazi.branch.wu`               | 地支                                                         |
| `bazi.pillar.{year|month|day|hour}.*` | `bazi.pillar.year.geng_wu`     | Säulen-Ganzheiten                                          |
| `bazi.day_master.*`                   | `bazi.day_master.geng`         | 日主                                                         |
| `bazi.ten_god.*`                      | `bazi.ten_god.shishen`         | 十神                                                         |
| `bazi.luck_pillar.*`                  | `bazi.luck_pillar.gui_wei`     | 大运柱 (erste 8 步 im Node-Set)                                |
| `bazi.jiazi.*`                        | `bazi.jiazi.geng_wu`           | 六十甲子 (Katalog; Engine nutzt weiter `bazi.pillar.*.<pair>`) |
| `bazi.twelve_state.*`                 | `bazi.twelve_state.changsheng` | 十二长生 (Katalog-Vokabular)                                   |
| `bazi.xun.head.*`                     | `bazi.xun.head.jia_zi`         | 旬首-Referenz (6 × 甲子 … 甲寅)                                  |
| `bazi.shensha.yima.*`                 | `bazi.shensha.yima.year.shen`  | 驿马-Ziel支 pro Säule (`getShensha().horses`)                   |
| `bazi.shensha.kongwang.*`             | `bazi.shensha.kongwang.day.yin_mao` | 旬空两地支 pro Säule                                     |
| `bazi.shensha.tianyi.*`               | `bazi.shensha.tianyi.year.chou_wei` | 天乙贵人 阳贵/阴贵 支 |
| `bazi.shensha.wangxiang.*`           | `bazi.shensha.wangxiang.mu.wang` | 月令 旺相休囚死 je 五行 (`seasonPower`) |

Katalog **`shensha_aux`:** dieselbe Logik tabellarisch (schema ≥ 1.2); **`nodes[]`** spiegelt Chart-**神煞** aus `Bazi.getShensha()`.

**Schritt 1–3:** wie Playbook — `extract:bazi-catalog`, `build:bazi-structure`, `validateBaziNodesAgainstCatalog` (Pillar/Luck, `bazi.shensha.*`).