---
last_update: 2026-09-03
status: draft
scope:
  summary: "High-level HD TOC ↔ K2/Themen-Abgleich für lokale hd/ + other_hd/ Werke. Delta 2026-09-03: dünne Auth — Restbücher parken, nicht für ego_* ingestieren. Delta 2026-09-01: Cosmology V + Codon Mapping in hd/neu (disk unused). Delta 2026-08-17: Live-DB vs Disk."
  in_scope:
    - TOC/Outline-Scan ohne MinerU
    - Theme-Tags vs. Pipeline-Nutzung vs. Layer-Qualität
    - Live-Abgleich sys_sources ↔ lokale PDFs (2026-08-17)
    - Park-Liste Restbücher vs. dünne Authority (2026-09-03)
  out_of_scope:
    - Volltext-Extract / Re-Synth
    - andere Systeme (BaZi, Gene Keys, …)
notes:
  - "Skript: code/inner_compass_app/apps/web/scripts/ic_hd_toc_coverage_audit.py"
  - "Rohdaten: literature_hd_toc_scan_2026-08-11.csv + literature_hd_toc_theme_matrix_2026-08-11.csv"
  - "Queue-CSV status oft stale; pipeline_use mit Known-Done-Override 2026-08-11"
  - "2026-08-17: sys_sources live 41 / 8588 Chunks. Die 22 unused Authority-Hits sind TOC-Keywords, keine ungechunkten Bücher."
  - "2026-09-03: Definitive 632/632; Mix-Demote self_projected; Black Book/Letters/Resonance Mapping parken."
---

# HD TOC Coverage Audit (2026-08-11)

High-Level-Abgleich: **lokale Werke** (`Downloads/Literatur/hd` + `other_hd`) → **TOC-Themen** → **K2/Produkt-Layer** → **Pipeline-Nutzung / Qualität**.

## Methode

1. PDF-Outline/Bookmarks (pypdf)
2. Fallback: Frontmatter nur wenn Outline < 8 Einträge (max. ~12 Seiten; Timeout 40s → Titel)
3. Keyword-Map auf Theme-Tags; Titel-Hints wenn TOC dünn
4. Join Queue-CSV + **Known-Done-Override** (Queue-Status oft veraltet)
5. **Kein MinerU**, kein GPU

> **Caveat:** `literature_content_wave_queue_2026-07-18.csv` markiert viele Werke noch als `queued`, obwohl sie schon in der Pipeline waren. `pipeline_use=in_pipeline` enthält deshalb manuelle Overrides für bekannte Waves/Enrich.

## Live-Abgleich 2026-08-17 (DB vs Disk)

Kein MinerU, kein Upload. Disk: `Downloads/Literatur/hd` (52 PDF) + `other_hd` (13 PDF) = **65**. DB lokal: **41 `sys_sources` / 8588 Chunks**.

Die Zahl **22** in der Checkliste (`authority`-Theme) sind **unused TOC-Keyword-Hits**, nicht 22 ungechunkte Werke. Four Views, HA2, Never Mind, Shadow, Type 1–4, PHS q1–q8, Winn, Schoeber, I’Ching, Circuitry, Crosses **sind in der DB**.

CW-Titel in der DB (`CW HD q3 - Channels by Type 2`) = dieselben Dateien wie Anna-Archive-Namen auf Disk. Hash-Titel sind Upload-Artefakte, nicht fehlende Bücher:

| DB-Titel | Chunks | Ist |
|---|---:|---|
| `e337cd77….pdf` | 175 | Life Force (Source-ID `2a9272bc-…`) |
| `03e4a007….pdf` | 169 | ungeklärt; schon extractet — nicht nochmal MinerU |
| `0e057eb7….pdf` | 0 | Extract-Leiche |
| Never Mind (zwei Zeilen) | 15+15 | Duplikat-Source |

**S0-Pipeline auf Disk ist weitgehend in der DB** (Type 1–4, Design Concepts, PHS Sem 1–3, Quarters, 36 Roles, Six Lines, Life Force). Dateiname ≠ CW-Titel ≠ fehlend.

**Wirklich nicht in `sys_sources` (echte Lücken):**

| Priorität | Werk | Warum |
|---|---|---|
| S1 | Life Cycles; Partnership; How We Connect | ZEIT / Composite — wake bei Feature |
| S1 transit | Type 4 **schon in DB**, Packer skip; Planets extractet | kein neues PDF; Cosmology V ist nicht der Transit-Ingest |
| S2 / deferred | DreamRave; Cosmology I–III+**V**+VIII; Anatomy I–II; BG5; Sex Manual; From the Left/Right; Biology Design; Resonance Mapping; Book of Letters; Radical Transformations; Black Book; **Codon Mapping** | bewusst nicht S0 |
| Disk `hd/neu` (2026-09-01) | **Rave Cosmology V**; **Codon Mapping** | lokal, unused, **kein** Ingest jetzt. IC-by-Profile-PDF in `neu` = Duplikat des Complete in `hd/` |
| Noch nicht auf Disk | Cosmology **IV / VI / VII**; HA1/HA3; Ra LYD; Line Companion | nicht jagen außer Staffel 2 / HA2-Mehrwert (HA2 hatte 0 Ego/Quad-Hits) |
| Schulen | Karen Curry / Quantum / Winn Clients / Rhodes BaanTu | `other_hd`, nicht Default-Jovian |

Nächster MinerU-Schnitt: **Planeten-Buch ✅ extract 2026-08-17** (Source `7e52cc9a-…`, 22 Chunks). Seed `hd.planet.*` ✅. Interpret Langdock (nosynth) 2026-08-17. Four Views Relink ego/quad ✅; HA2 Diagnostics hatte 0 Ego/Quad-Hits (kein Re-Extract).

## Delta 2026-09-03 — dünne Authority, nicht diese vier Bücher

Definitive (`ec0aedc4`) Interpret **632/632**. text2kg `39b0fbf6` completed (kein Synth). 200 unmatched = strict-Cap, nicht ego_*. Nodes `ego_manifested` 11 / `ego_projected` 10 / `self_projected` 16 unverändert; 188 neue Interps ohne Ego-Essence. Mix-Primary `10829c13` → `mention` (Self-Projected + Mental Projector). SoT Umgang: `synthesis_canon_first.md` §3.4 + Decision 2026-09-03.

**Nicht ingestieren für ego_*/self_projected** (TOC 11.08. + Live-DB):

| Werk | TOC | Später, anderes Layer | Jetzt |
|---|---|---|---|
| **The Four Views** | Authority + Definition | — | ✅ in DB (`c3135579`, 211/211) |
| **The Black Book** | Intro / I’Ching / JUT; Theme nur Kreuze | Primer, wenig Unique vs. Complete I’Ching | parken |
| **Book of Letters** | 9 Zentren, Circuitry, 64 Tore; „Ego Circuit“ = Schaltung | Analyse-Handbuch; Overlap Circuitry + I’Ching. CSV `in_pipeline` ist stale | parken |
| **Design Resonance Mapping** (Flesh) | Environment, PHS, Definition | `hd.environment.*` (Atome too thin) / Fleisch | parken |
| **Personality Resonance Mapping** (Mind) | „Beta: Outer Authority“ | `hd.authority.mental` — **nicht** self_projected | parken; würde den Mix verschärfen |

`other_hd` (Quantum/Curry/Winn/Rhodes-Pop) bleibt Zweitstimme, kein Ra-Ersatz. Ra LYD weiter lokal fehlend.

## Scan-Stats (historisch 2026-08-11)

| Metrik | Wert |
| --- | --- |
| Werke gesamt | 68 |
| `hd/` | 52 |
| `other_hd/` | 16 |
| TOC via Outline | 50 |
| TOC via Frontmatter | 13 |
| nur Titel-Fallback | 5 |
| Open/Extract/Timeout-Fehler | 2 |

### Pipeline-Nutzung (Werk-Ebene, nach Override)

| Status | Anzahl |
| --- | --- |
| `queued_not_run` | 44 |
| `in_pipeline` | 20 |
| `in_pipeline_enrich` | 3 |
| `local_only_not_in_queue` | 1 |

## Theme-Coverage (Zusammenfassung)

| Theme | Layer-Qualität (Produkt) | Bücher mit TOC/Titel-Hit | davon in Pipeline | noch unused | Hinweis |
| --- | --- | --- | --- | --- | --- |
| `authority` | gemischt_duenn_ego | 36 | 14 | 22 | ungenutzte lokale Quellen prüfen |
| `bg5` | nicht_mvp_kern | 6 | 0 | 6 | bewusst deferred ok |
| `centers` | gut | 35 | 12 | 23 |  |
| `channels` | gut | 17 | 6 | 11 |  |
| `circuits` | gut | 12 | 7 | 5 |  |
| `cosmology` | nicht_mvp_kern | 17 | 7 | 10 | bewusst deferred ok |
| `cross_theme` | offen_nicht_geseedet | 0 | 0 | 0 | kein lokales TOC/Titel-Signal |
| `definition` | gemischt_duenn_quadruple | 13 | 5 | 8 | ungenutzte lokale Quellen prüfen |
| `dream_rave` | nicht_mvp_kern | 7 | 1 | 6 | bewusst deferred ok |
| `gates` | gut | 35 | 10 | 25 |  |
| `incarnation_crosses` | gut_genug | 11 | 3 | 8 |  |
| `life_cycles` | optional | 2 | 0 | 2 | nur lokal / Queue-unused — prüfen ob schon verarbeitet |
| `lines` | gut | 25 | 5 | 20 |  |
| `living_your_design` | luecke_ra_lyd | 1 | 1 | 0 |  |
| `nodes_environment` | optional | 24 | 9 | 15 |  |
| `not_self` | gut | 22 | 10 | 12 |  |
| `partnership` | optional | 5 | 1 | 4 |  |
| `phs` | gut | 32 | 14 | 18 |  |
| `profiles` | gut | 17 | 4 | 13 |  |
| `rave_psychology` | teilweise | 14 | 5 | 9 |  |
| `sexuality` | optional | 6 | 1 | 5 |  |
| `signature` | gut | 7 | 2 | 5 |  |
| `strategy` | gut | 24 | 10 | 14 |  |
| `transit` | optional | 8 | 5 | 3 |  |
| `types` | gut | 29 | 9 | 20 |  |

## Handlungsrelevante Lücken

> **08-17:** Die Listen darunter sind TOC-Keyword-Hits vom 11.08. Viele Einträge sind **stale** (HA2, Four Views, Never Mind, Shadow, Lunar Color = schon in der DB). SoT für Extract: Abschnitt **Live-Abgleich 2026-08-17** oben. Nicht blind hochladen.

Fokus: dünne Produkt-Layer × ungenutzte Bücher mit Theme-Hit. Keyword-Hits sind **Hinweise**, keine Kapitelgarantien.

### `authority` (gemischt_duenn_ego)

- **Biology Design System -- Ra Uru Hu, Eleanor Haspel, Marvin Portner -- 2000** (`hd`) — `queued_unused`
- **Dream Rave Introduction -- Ra Uru Hu** (`hd`) — `queued_unused`
- **DREAMRAVE I_ Introduction to Personal Analysis -- Ra Uru Hu -- 2007 -- International Human** (`hd`) — `queued_unused`
- **From the Left_ Strategic Cognition - Personal and -- Ra Uru Hu -- 2010 -- International Hu** (`hd`) — `queued_unused`
- **From the Right -- Ra Uru Hu -- Personal and Trans-Personal Analytical Training -- Internat** (`hd`) — `queued_unused`
- **Holistic Analysis 2 Diagnostics 2 -- Ra Uru Hu -- Personal and Trans-Personal Analytical T** (`hd`) — `queued_unused`
- **Human design - You and the Shadow -- Ra Uru Hu -- 2020** (`hd`) — `queued_unused`
- **Lunar & Planetary Color -- Ra Uru Hu -- 2010 -- International Human Design School (IHDS)** (`hd`) — `queued_unused`
- **Lunar & Planetary Color Analysis -- Ra Uru Hu -- 2008 -- International Human Design School** (`hd`) — `queued_unused`
- **Never Mind Final -- RA URU HU** (`hd`) — `queued_unused`
- … +12 weitere

### `definition` (gemischt_duenn_quadruple)

- **Design Resonance Mapping - The Way of the Flesh -- Ra Uru Hu -- 2009 -- International Huma** (`hd`) — `queued_unused`
- **DREAMRAVE I_ Introduction to Personal Analysis -- Ra Uru Hu -- 2007 -- International Human** (`hd`) — `queued_unused`
- **Holistic Analysis 2 Diagnostics 2 -- Ra Uru Hu -- Personal and Trans-Personal Analytical T** (`hd`) — `queued_unused`
- **Human Design - Life Cycles Analysis -- Ra Uru Hu** (`hd`) — `queued_unused`
- **Never Mind Final -- RA URU HU** (`hd`) — `queued_unused`
- **The Four Views -- Ra Uru Hu -- 2007 -- Jovian Archive Corporation** (`hd`) — `queued_unused`
- **Understanding the Planets in our Design - A COURSE IN -- Ra Uru Hu; Richard Rudd -- 2003** (`hd`) — `queued_unused`
- **Intro to Human Design System -- Karen Curry Parker -- 2019** (`other_hd`) — `queued_unused`

### `living_your_design` (luecke_ra_lyd)

- Keine ungenutzten lokalen Hits (oder alle Known-Done).

### `incarnation_crosses` (gut_genug)

- **Dream Rave Introduction -- Ra Uru Hu** (`hd`) — `queued_unused`
- **Lunar & Planetary Color -- Ra Uru Hu -- 2010 -- International Human Design School (IHDS)** (`hd`) — `queued_unused`
- **Lunar & Planetary Color Analysis -- Ra Uru Hu -- 2008 -- International Human Design School** (`hd`) — `queued_unused`
- **Partnership Analysis -- Ra Uru Hu -- International Human Design School** (`hd`) — `queued_unused`
- **Quarters and Angles -- Ra Uru Hu -- International Human Design School** (`hd`) — `queued_unused`
- **Rave Cosmology III_ Dying Death and the Bardo Stages -- Ra Uru Hu** (`hd`) — `queued_unused`
- **Scenes From The Cross Of Life_ The Nodal Environments(Human -- Ra Uru Hu -- 2005** (`hd`) — `queued_unused`
- **The Incarnation Cross Clinic _ Lectures Day 1 _ Part 1 and 2 -- Ra Uru Hu -- 2022 -- Jovia** (`hd`) — `queued_unused`

### `cross_theme` (offen_nicht_geseedet)

- Keine ungenutzten lokalen Hits (oder alle Known-Done).

## Kandidaten-Priorität — Update 2026-08-11 (P1 Close-out)

TOC-Stichprobe + Upload (Details: `hd_layer_master_checklist_2026-08-11.md`):

| Werk | Befund | Aktion |
| --- | --- | --- |
| **The Four Views** | Lectures zu Definition (single/split/triple/**quadruple**), Authority, Type/Strategy | ✅ uploaded `c3135579-…` extract queued |
| **Holistic Analysis 2** | Auth/Def streifen; Fokus Diagnostik/PHS | ✅ uploaded `5517ac0c-…` extract queued |
| HA1 + HA3 | lokal fehlend | erst nach HA2-Synth-Nutzen |
| Ra LYD | not_found | **deferred** (Rudd nicht nutzen) |
| `cross_theme.*` | Parent für Kreuz-Kurznamen | default **nicht seeden** |

Weiter: extract → interpret → Auth/Def-Relink → Synth.

## Werke ohne brauchbares TOC-Signal

10 Werke mit sehr dünnem TOC:

- `hd` / Biology Design System -- Ra Uru Hu, Eleanor Haspel, Marvin Portner -- 2000 — method=`frontmatter_text` themes=`authority|centers|channels|circuits|cosmology|dream_rave|gates|partnership`
- `hd` / Rave BodyGraph Circuitry -- Ra Uru Hu -- 2012 — method=`title_fallback` themes=`circuits`
- `hd` / The Human Design System - Sex Manual -- Ra Uru Hu -- 1996 — method=`frontmatter_text` themes=`partnership|sexuality`
- `hd` / The Incarnation Cross Clinic _ Lectures Day 1 _ Part 1 and 2 -- Ra Uru Hu -- 2022 -- Jovia — method=`title_fallback` themes=`incarnation_crosses`
- `hd` / Understanding the Planets in our Design - A COURSE IN -- Ra Uru Hu; Richard Rudd -- 2003 — method=`frontmatter_text` themes=`channels|definition|gates|lines|not_self|profiles|transit|types`
- `other_hd` / How Do You Choose_ -- Erin Claire Jones -- 2025 -- HarperCollins — method=`non_pdf_title_only` themes=`—`
- `other_hd` / Human Design Made Simple_ Unlock Your Strengths and Discover -- Emma Dunwoody -- 2025 -- P — method=`non_pdf_title_only` themes=`—`
- `other_hd` / Intro to Human Design System -- Karen Curry Parker -- 2019 — method=`frontmatter_text` themes=`centers|channels|definition|lines|profiles|sexuality|types`
- `other_hd` / Quantum Wellness -- Karen Curry Parker -- 2025 -- Human Design Press -- isbn13 97819613478 — method=`non_pdf_title_only` themes=`—`
- `other_hd` / Understanding the profiles in human design 3 3 -- Robin Winn MFT -- 3, 2022 -- Independent — method=`frontmatter_text` themes=`authority|bg5|phs|profiles|signature|types`

## Rohdaten

- [`literature_hd_toc_scan_2026-08-11.csv`](literature_hd_toc_scan_2026-08-11.csv)
- [`literature_hd_toc_theme_matrix_2026-08-11.csv`](literature_hd_toc_theme_matrix_2026-08-11.csv)

