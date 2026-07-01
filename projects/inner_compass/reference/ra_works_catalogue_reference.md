---
reality:
  scope: Ra Uru Hu Werkskatalog — Disk-Abgleich für IC Literaturbeschaffung
  last_update: 2026-06-30
  source:
    - entity_registry_hd_v02.json (known_works, Prioritäten)
    - literature_local_inventory_2026-06-30.csv (Disk-Scan)
    - AA-Autorenliste / Kobler-Katalog (User-Referenz, nicht SoT)
  in_scope:
    - Disk-Status pro Ra-Kernserie
    - IC-P0-Lücken (Curriculum)
    - Verwechslungen (Line Companion vs Complete Rave I'Ching)
  out_of_scope:
    - Vollständige 300+-Werk-Liste aller Seminare/Audio
---

# Ra Uru Hu — Werkskatalog-Referenz (Disk-Abgleich)

**Disk-Pfad:** `Nextcloud/.../Human Design/App/Literatur/hd/` (+ `archiv/` für Alt-Ausgaben)  
**Maschinenlesbar:** [`literature_local_inventory_2026-06-30.csv`](literature_local_inventory_2026-06-30.csv) — Filter `top_folder=hd`  
**Entity-Registry:** [`entity_registry_hd_v02.json`](entity_registry_hd_v02.json) — `known_works` mit Kategorie A–D

Stand Scan: **216 Dateien gesamt**, **~55 Ra-PDFs** in `hd/` (+ 4 Archiv-Dubletten).

---

## Kurzantwort: Line Companion, Holistic Analysis, Incarnation Crosses

| Werk (Katalog-Name) | Auf Disk? | Datei / Hinweis |
|---|---|---|
| **Incarnation Crosses by Profile (Complete)** | **Ja, vollständig** | `Incarnation Crosses by Profile (Complete)` (2012, ~15 MB) + Bonus `The Incarnation Cross Clinic` (2022) |
| **Holistic Analysis** (3 Teile) | **Teilweise** | Nur **Teil 2** — `Holistic Analysis 2 Diagnostics 2` (2010). **Teile 1 und 3 fehlen.** |
| **Rave I'Ching Line Companion** (384 Linien, ~542 S.) | **Nein** | Nicht vorhanden. Verwechslung möglich mit *The Complete Rave I'Ching* oder *The Six Lines* — das sind **andere** Werke (siehe unten). |

---

## Verwechslungsgefahr — I'Ching-Linie

| Titel auf Disk | Was es ist | Ersetzt Line Companion? |
|---|---|---|
| *The Complete Rave I'Ching* (2011) | Hexagramm-/Tor-Kommentare, Kreuze, Übersicht | Nein — kürzer, andere Tiefe |
| *The Six Lines — Decoding of the Hexagram* (2008) | Einführung in die 6 Linien pro Hexagramm | Nein — kein 384-Linien-Kommentar |
| *The 36 Roles — Genetic Continuity and Mastery of Lines* (2010) | Rollen/Linien-Thema, kompakt (~1 MB) | Nein |
| **Rave I'Ching Line Companion** (2002, ~542 S.) | **Alle 384 Linien** im Detail | — **fehlt** |

Für IC-K4 (Linien-Deutungstexte) ist der **Line Companion** die tiefste Ra-Primärquelle laut `entity_registry_hd_v02` — optional nachbeschaffen, wenn K4-Linien-Pass ansteht.

---

## IC-P0-Lücken (Curriculum-Blocker)

| Priorität | Werk / Serie | Disk | Beschaffung |
|---|---|---|---|
| **P0 high** | Rave Cosmology **IV, V, VI, VII** | Fehlen | In Katalog-Listen oft sichtbar; auf AA bisher **nicht** gefunden → Jovian / IHDS / andere Quelle |
| **P0 ok** | Rave Cosmology I, II, III, VIII | Vorhanden | — |
| optional | Holistic Analysis **1 + 3** | Fehlen | AA-Suche: `Ra Uru Hu Holistic Analysis` |
| optional | Rave I'Ching Line Companion | Fehlt | AA: `Ra Uru Hu Rave I'Ching Line Companion` |
| optional | The Global Incarnation Index (192 Kreuze, 2000) | Fehlt | Ergänzt *Incarnation Crosses by Profile* strukturell |

---

## Serien-Übersicht (Katalog ↔ Disk)

Legende: **ja** = PDF in `hd/` · **teilw** = unvollständige Serie · **nein** = nicht auf Disk · **archiv** = Dublette in `archiv/`

### BodyGraph / I'Ching / Kanäle

| Serie / Werk | Disk | Anmerkung |
|---|---|---|
| The Black Book (1991) | ja | |
| Book of Letters (1995) | ja | |
| The Complete Rave I'Ching | ja + archiv | 2 Ausgaben (hd + archiv) |
| Rave I'Ching Line Companion | **nein** | siehe oben |
| The Six Lines | ja | |
| The 36 Roles | ja | |
| Keynotes: Circuits, Channels and Gates | nein | |
| The Nine Centres and their Gates | nein | |
| Channels by Type 1–4 | ja | komplett |
| The Life Force — The Channels | ja | |
| Rave BodyGraph Circuitry | ja | |
| Rave Anatomy I–II | ja | |

### Analyse / Ausbildung (IHDS)

| Serie / Werk | Disk | Anmerkung |
|---|---|---|
| Holistic Analysis 1–3 | **teilw** | nur Teil 2 |
| Design Concepts | ja | |
| Design / Personality Resonance Mapping | ja | Way of Flesh + Way of Mind |
| From the Left / From the Right | ja | |
| Post-Graduate Rave Psychology | ja | |
| Rave Psychology External Color (Black/White) | ja | |
| Quarters and Angles | ja | |
| Partnership Analysis | ja | |
| Human Design — Life Cycles Analysis | ja | |
| You and the Shadow | ja | |
| How We Connect (2024) | ja | |

### PHS / Variablen

| Serie / Werk | Disk | Anmerkung |
|---|---|---|
| PRIMARY HEALTH SYSTEM Sem 1–3 (Year 1) | ja | 3 PDFs |
| Lunar & Planetary Color (+ Analysis) | ja | |

### Kosmologie

| Teil | Disk |
|---|---|
| Rave Cosmology I — Bhan Tugh | ja |
| Rave Cosmology II — Six Mystical Ways | ja |
| Rave Cosmology III — Dying, Death, Bardo | ja |
| Rave Cosmology **IV–VII** | **nein** |
| Rave Cosmology VIII — Mystic Monologues | ja |

### Inkarnationskreuze

| Werk | Disk |
|---|---|
| Incarnation Crosses by Profile (Complete) | ja |
| The Incarnation Cross Clinic (2022) | ja |
| Scenes From The Cross Of Life — Nodal Environments | ja |
| The Global Incarnation Index | nein |

### Typen / Spezialthemen

| Werk | Disk |
|---|---|
| Manifestor Manifesto | ja |
| Projector Empowerment Part 1 | ja |
| Radical Transformations | ja |
| Dream Rave Introduction + DREAMRAVE I | ja |
| BG5 Career Manual 1 | ja |
| Sex Manual | ja |
| Never Mind Final | ja |
| The Four Views | ja |
| A Complete Guide | ja |
| Die Prophezeiung (DE) | ja |

### Nicht-Ra in `hd/` / `other_hd/`

Karen Curry Parker, Robin Winn, Steve Rhodes, Lynda Bunnell u. a. — siehe Inventory-Filter `bucket=hd_other`. Für IC-P0-Ra-Kern irrelevant, aber für K3-Erweiterung nutzbar.

---

## Nächste Schritte (Beschaffung)

1. **Cosmology IV–VII** — außerhalb AA (Jovian Archive / IHDS-Kontext), höchste IC-Priorität.
2. **Line Companion** — AA-Suche, wenn Linien-K4-Pass geplant.
3. **Holistic Analysis 1 + 3** — Serie vervollständigen (Teil 2 ist da).
4. Scan wiederholen: `python projects/inner_compass/scripts/build_literature_inventory.py`

---

## Verweise

- Beschaffungsprozess: [`literature_acquisition_ic_aa.md`](literature_acquisition_ic_aa.md)
- AA-Lückenliste: [`literature_aa_need_2026-06-30.csv`](literature_aa_need_2026-06-30.csv) (4 offene HD-Einträge: Cosmology IV–VII)
- Have vs Need: [`literature_have_vs_need_2026-06-30.csv`](literature_have_vs_need_2026-06-30.csv)
