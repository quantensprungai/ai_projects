<!--
Reality Block
last_update: 2026-09-02
scope: IC Projektstatus (Phasen 0–4), Chart-Engines, Content-Akquise, Ur-Systeme, Gene Keys, Konvergenz/Meta-KG
in_scope: Stand, nächste Schritte, Systemliste, Anna's Archive entity-first, Klarstellung HD-Schulen vs. GK, Konvergenz personenbezogen vs. strukturell, Ziwei Natal-First-Cut, Astro-KARTE First Cut, KARTE-Gitter, Zusammenschau
out_of_scope: Kit-Implementierungsdetails → engines.md; Code-Pfade → inner_compass_app AGENTS.md
-->

# Inner Compass — Status & Nächste Schritte

> **Stand:** 2026-09-02 — Phasen 0–3 / Engines / Content bleiben hier. **KARTE SoT:** `cursor/handover.md` (Copy-Paste). HD: Overlay-Vertrag + `figma_karte_contract.md` §4b. Astro: `reference/astro_natal_ingest_runbook.md`.
> **App (Phase 4):** HD KARTE Graph visuell zu (helle Jovian-Fills, Kanalhälften, Hanging, Variable-Chevrons, keine Gate-Chips). Overlay-LLM v1o. HD-Docker `ic-hd-service` :8002. **Ziwei-KARTE First Cut** (`/home/karte/ziwei`): dichte 4×4-Platte, Chrome DE, Kleinsterne Position+20 EN-Lexikon, Inspector `draft`/`canon_fallback`, **Zusammenschau `ziwei_overlay_v3`**. **Astro-KARTE First Cut** (`/home/karte/astro`): tropisch Whole Sign, AC links, Big Three + Rad, Selektion-Linien, Typ-Atome EN-Draft, Chrome DE, **kein Overlay**. Keine DE-Atome.
> **Content (Phase 2):** **HD S0 Close-out ✅** — Canon-first Synth, link_role, ID-Strip. S0.5 Relink live. SoT: `reference/hd_layer_master_checklist_2026-08-11.md`. **Ziwei Natal-First-Cut ✅** (中州 Staffel 1 + Welle 1b) — SoT + Qualitätsschulden: `reference/ziwei_natal_ingest_runbook.md`.
>
> **Wo wir sind:** Phase 0 erledigt. Phase 1 — Chart-Engines (historisch „Staffel 1“ genannt, Label nicht mehr reihenfolge-bindend): fünf Kerne + **Maya Tzolkin, Nine Star Ki, Numerologie, Akan** in `@ic/engines` + API-Routen + Kataloge v0 ✅
> - **Ziwei Doushu** (iztro): TS, Katalog + Validierung ✅
> - **BaZi** (@yhjs): TS, Katalog + Validierung ✅
> - **Jyotish** (PyJHora): Python-Microservice, D1+D9+Dasha+Bhavas+Yogas+16 Vargas ✅
> - **Human Design** (dturkuler): Python-Microservice, alle 13 Layer + Composite/Transit/BodyGraph ✅ — **Ephemeris:** Swiss Ephemeris via **pyswisseph**, Modus **tropical** (Standard). **Sidereal / Hybrid** (`compute_profile`, contracts §13): spezifiziert in `reference/hd_compute_profiles_kg_and_roadmap.md`, **Code noch nicht** — optional später.
> - **Westl. Astrologie** (**celestine**, MIT): TS in `@ic/engines`, `computeAstroChart` + `astro_catalog_v0.json` + Validierung ✅ *(alter Planename „CircularNatalHoroscopeJS“ — im Code: celestine; optional: Präzisions-/Ephemeris-Abgleich als Spike offen)*
> - **Maya Tzolkin** (`mayan_tzolkin`): **v1** `ic_maya_tzolkin_v1` — GMT 584283 + Dreamspell-Slugs; **lokales Zivildatum** aus Instant (`utcMillisForWallTimeInZone`); Vitest **Step 3** vs. `mayan_tzolkin_catalog_v0.json` ✅
> - **Nine Star Ki**: K1/K2 **v1** (`ic_nine_star_ki_v1`) — Honmei + Getsumei + **energetic**; feste Sonnenmonats-Schnitte; Vitest **Step 3** Katalog-Regeln ✅ — `reference/decisions.md` **2026-04-16**
> - **Numerologie / Akan**: Engines + Kataloge + `POST /api/.../calculate` ✅ *(Playbook-Validierung optional)*
>
> **Nächste Reihenfolge (jetzt):** Astro-KARTE First Cut liegt; Interpret+text2kg 14/14 durch; Relink 58/58 + scoped Synth 16 (Häuser+AC/DC/IC/MC). Nächster Gate: Inspector-Stichprobe, dann Commit zwei Repos wenn gefragt. BaZi-Klassiker weiter die nächste *andere* Literaturwelle, nicht parallel. Overlay-Sprache / DE-Atome / 来因 / 流年 / Astro-Overlay / Horary-KG geparkt. Decision 2026-08-27 Natal-Parität + 2026-09-02 Rad + Relink/Synth-Nachzug. Nicht Mandala, nicht Handbuch-Generator.
>
> **Roter Faden (Gesamtplan):** HD Close-out → System-Wellen → Phase 3 (nach 2 Reviews) → **Makerkit v4 ✅** → MVP Phase 4 → Voll — kanonisch in `cursor/handover.md` § Roter Faden. Content-Nachrüst: `reference/hd_layer_master_checklist_2026-08-11.md`. Wave: `cursor/reference/literature_content_wave_2026-07-18.md`. UX: `reference/ux_konzept_2026-07.md`.

## Was EXISTIERT und FUNKTIONIERT

### Infrastruktur ✅
- Makerkit-App (Next.js + Supabase): Auth, Accounts, UI-Shell
- Spark GPU-Server: MinerU (PDF-Parsing), SGLang/vLLM (LLM-Inferenz)
- Tailscale VPN: Spark ↔ Supabase ↔ Dev
- **System-Deskriptoren:** `projects/inner_compass/system_descriptors/*.json` — u. a. HD, BaZi, Ziwei, Astro, Jyotish, Maya, Gene Keys, Enneagram, Numerology, Nine Star Ki, Akan **plus** Ur-/Struktur-Systeme (**`i_ching.json`**, **`kabbalah.json`**, **`chakra.json`**, `wu_xing`, `pancha_bhuta`, `western_elements`, …). Deskriptor ≠ fertige Engine ≠ Literatur-Registry.

### Jyotish Microservice (Code-Repo) — Phase 1a ✅
- Pfad: `code/inner_compass_app/services/jyotish/` — FastAPI, `POST /calculate` mit `BirthData` wie `@ic/engines`
- **D1 (Rāśi):** PyJHora `rasi_chart` (Swiss Ephemeris via `pyswisseph`)
- **Docker:** `python:3.12-slim` + `build-essential` (Build `pyswisseph`); `requirements.txt` enthält u. a. explizit **`pytz`**, **`geocoder`**, **`geopy`**, **`timezonefinder`**, **`python-dateutil`** — PyJHora listet nicht alle Laufzeit-Imports als pip-Dependencies; ohne diese Module bricht die Berechnung mit ImportError ab
- **E2E (2026-04-13):** Image bauen, Container starten, nach ~25 s `GET /health` + `POST /calculate` (Test: Berlin 1990-01-15 12:30) → `raw.placeholder: false`, `raw.bodies`: 13 Einträge, `raw.chart: D1`, `nodes` mit `jyotish.lagna` / `jyotish.rasi.*` / `jyotish.graha.*`
- **Next.js (Chart-API, `apps/web/app/api/`):** `hd` · `ic/hd-chart` (UI) · `jyotish` (Env-URLs) · `ziwei` · `bazi` · `astro` · **`maya-tzolkin`** · **`nine-star-ki`** · **`numerology`** · **`akan`**. **Chart-UI:** `/home/karte/hd` ✅ · `/home/karte/ziwei` ✅ · `/home/karte/astro` ✅ First Cut. Übrige Systeme: API ohne Chart-Seite. Artefakte unter `projects/inner_compass/system_structure/` (siehe Playbook).

### Philosophische Konsolidierung ✅ (Z-Dokumente)
- Z1 Gesamtwerk v0.5, Z2 User-Journey v0.1, Z3 Modell-Referenz v0.4, Glossar v1.2
- ic_gesamtinventur.md v0.5 als Brücke Philosophie→Technik
- Z4 = cursor/ Dateien (kein separates Dokument)
- Konsolidierung abgeschlossen (→ 00_konsolidierungs-status.md)

### Alter HD-Worker (Referenz, wird neu geschrieben)
- hd_worker_mvp.py (~2400 Zeilen) — Pipeline funktioniert end-to-end für HD
- 10 Custom-Migrations mit hd_*-Präfix — werden durch 1-2 saubere sys_*-Migrations ersetzt
- Patterns/Logik werden übernommen, Code wird neu geschrieben

### Content-Akquise (Anna's Archive Toolkit)
- Pipeline-Architektur: Solide (Topics → Scraping → metadata.json → assets.jsonl → Download → Upload)
- Datenqualität: ~85% Noise bei **reinen Keywords** (Lösung: **entity-first** + Zwei-Gate-Filtering, siehe pipeline.md §8)
- **`simple_collector.py`:** Profil `query_mode: entity_registry` lädt `projects/<profile_id>/entity_registry.json` (Suchstrings aus `download_priority_order` + Autoren-Queries + `non_author_works`). **`AAT_TOPICS`** überschreibt; sonst Fallback `topics.txt`.
- **Aktive / angelegte Entity-Registries (Starter bis v0.2):** `hd_content`, `astro_content`, `jyotish_content`, `ziwei_content`, `bazi_content` — Referenzkopien zusätzlich unter `projects/inner_compass/reference/entity_registry_*_v0x.json`. **Primärsprache der Suche:** je System **lokal** (zh/sa/…), Englisch nur als Brücke wo sinnvoll.
- **„Werklandschaft“:** HD hat die **tiefste** manuelle Inventur (`entity_registry_hd_v02.json` + Konsolidierungsdocs). Andere Systeme nutzen **dieselbe Methode** (Subsystem-Tags, Phasen, Schulen) — **nicht** zwingend denselben Recherche-Umfang; Tiefe nach Extraktions-Priorität nachziehen.
- hd_saas_uploader.py: `--sys-mode` für PDF-Upload (sys_sources, sys_ingestion_jobs, sys_uploads_raw) — S5 nutzbar
- Bestehende DB-Daten: Nur Stubs, werden NICHT migriert (Clean Data Restart)
- assets.jsonl in scratch/: Falsch platziert, werden bei Clean Restart neu generiert

### Ur-Systeme (I Ging, Kabbala, Chakren, …) — Deskriptor vs. Katalog vs. Literatur
- **Schichtung (sauber):** `system_descriptors/*.json` = **Vertrag** (element_types, Regeln, Lebensbereich-Zuordnung, `system_role`). `system_structure/*_catalog_v0.json` = **K1/K2-Inventar**, wo Kit oder Extraktion es hergibt. **K3/K4** = Literatur-Pipeline (MinerU+LLM, `entity_registry` pro `system_id`) — gleiches Muster für alle Systeme inkl. Ur-Systemen.
- **Vorhanden:** Deskriptoren u. a. `i_ching.json`, `kabbalah.json`, `chakra.json` (+ Element-Raster `wu_xing`, `pancha_bhuta`, …) + teils **Kataloge** unter `system_structure/`. Architektonisch **eigene `system_id`**, nicht „Anhang von HD“.
- **Struktur-Systeme** ohne Geburts-Chart-Engine: oft **zuerst** Deskriptor + Literatur (K2-Regeln aus Texttradition möglich); Evidenzklassen **B/C** wie überall, sobald extrahiert.
- **K3+K4 / Anna's:** **eigene** `entity_registry_*` / Profil pro Ur-System — **nicht** in die HD-Registry mischen.
- **Gene Keys:** **keine** separate Chart-Engine wie HD; **K1** Gate-Lage über **dieselbe** HD-Ephemeris-Anbindung, **K2** eigenes `gk.*` (`gk_catalog_v0.json`). **Literatur / Anna's:** **wie alle anderen Systeme** — eigenes Toolkit-Profil (`genekeys_content`) + `entity_registry` nachziehen; **keine** abweichende Sonder-Policy in dieser Doku. **HD-Schulen** (Jovian, Quantum HD, …): **ein** `hd.*`-Stammbaum, Unterschiede über **`tradition`/`werk_kategorie`**, keine eigenen Engines.

### Deskriptor ↔ Katalog v0 (Ist-Stand)

| `system_id` (Deskriptor-Datei) | `system_structure/*_catalog_v0.json` |
| ------------------------------ | ------------------------------------- |
| `hd.json` | `hd_catalog_v0.json` |
| `ziwei.json` | `ziwei_catalog_v0.json` |
| `bazi.json` | `bazi_catalog_v0.json` |
| `astro.json` | `astro_catalog_v0.json` |
| `jyotish.json` | `jyotish_catalog_v0.json` |
| `genekeys.json` | `gk_catalog_v0.json` |
| `enneagram.json` | `enneagram_catalog_v0.json` |
| `i_ching.json` | `i_ching_catalog_v0.json` |
| `kabbalah.json` | `kabbalah_catalog_v0.json` |
| `chakra.json` | `chakra_catalog_v0.json` |
| `wu_xing.json` | `wu_xing_catalog_v0.json` |
| `pancha_bhuta.json` | `pancha_bhuta_catalog_v0.json` |
| `western_elements.json` | `western_elements_catalog_v0.json` |
| `mayan_tzolkin.json` | `mayan_tzolkin_catalog_v0.json` |
| `numerology.json` | `numerology_catalog_v0.json` |
| `nine_star_ki.json` | `nine_star_ki_catalog_v0.json` |
| `akan.json` | `akan_catalog_v0.json` |
| — | `luoshu_catalog_v0.json` *(Hilfs-/Raster-Katalog; kein eigener Deskriptor in `system_descriptors/` v0)* |

## Gesamtprozess (5 Phasen)

```
Phase 0: Fundament          ████████████ 100%  Infrastruktur (Schema sys_*, Worker, Minimal-K2-Seed)
Phase 1: Engine Eval+Integ. ███████████░  ~95%  Chart-Engines + Kataloge v0; **offen:** Seed ↔ system_structure/*
Phase 2: Content-Pipeline   █████████░░░  ~75%  HD S0–S6 ✅ · BaZi Mechanik ✅ · **Ziwei Natal-First-Cut ✅** (Qualität: Runbook)
Phase 3: Cross-System       ░░░░░░░░░░░░   0%  → IC-Sprache entsteht hier (Datenschicht E)
Phase 4: App                ████░░░░░░░░  ~35%  HD KARTE Graph visuell zu; andere Spaces 0%
```

**Phase 0 = 100 %** bezieht sich auf **Infrastruktur**, nicht auf vollständige 13-Layer-Strukturbäume in der DB. Vollständiger K2-Seed ist **Phase-1-Nachzug** (Daten in `system_structure/` teils schon da).

---

## Phase 0: Fundament ✅ (S1–S4, erledigt 2026-02-16)

<details>
<summary>Details (S1–S4, abgeschlossen)</summary>

### S1 — Makerkit Pull ✅
- Upstream-Updates: Makerkit v2.23.14 + MCP Server 2.0
- Clean Data Restart (keine alten Stubs migrieren)

### S2 — Schema-Migration ✅
- 1 Migration: `20260216150000_inner_compass_core.sql` (11 sys_*-Tabellen)
- pgvector + Embedding-Spalte, RLS, Storage Bucket
- Helper-Schema: ic statt hd

### S3 — Neuer Worker ✅
- ic_worker.py (~650 Zeilen), sys_*-nativ, 6 Job-Typen, --dry-run, Retry

### S3.5 — Lokaler Smoke-Test ✅
- Supabase start + Schema ok + Worker dry-run ok
- Hinweis: `supabase start --ignore-health-check` auf Windows

### S4 — Seed-Script + Strukturbäume ✅ (Minimal-Skeleton)

- 832 Nodes + 698 Edges (10 Systeme, HD: **759 Nodes** nach JSON-Erweiterung 2026-07-02, vorher 526)
- Idempotent, Cross-System (Gene Keys → HD Gates)
- **Klarstellung:** Das ist ein **Minimal-K2-Skeleton** für Pipeline-Tests — **nicht** der vollständige 13-Layer-Baum. `hd_structure_v0.json` + `hd_crosses_extracted.json` sind weiter als der DB-Seed.
- **Nächster Schritt:** ~~`ic_seed_structure.py` liest `system_structure/*` (HD zuerst: +17 PHS, +192 Crosses, +4 Variables)~~ ✅ **2026-07-02:** HD-Seed liest `hd_catalog_v0.json`, `hd_structure_v0.json`, `hd_crosses_extracted.json` — siehe `reference/deep_structure_plan.md`

### Schema-Naming ✅ (2026-01 Clean Restart)

- Tabellen: **`sys_*`** (nicht `hd_*`) — Meta-System für alle Quellsysteme
- Spalte `system`: `'hd'`, `'bazi'`, … — Quellsystem-ID
- Canonical IDs: `hd.gate.34` — **`hd.` = System-Namespace**, nicht Tabellenname
- Helper-Schema Postgres: **`ic`** (ersetzt `hd`)
- Entscheidung: `reference/decisions.md` §2026-01

</details>

---

## Phase 1: Engine Evaluation & Integration ← NÄCHSTER SCHRITT

> **Kernidee:** Engines sauber in den Stack integrieren, dabei Strukturbäume extrahieren. Nicht separat analysieren und dann nochmal integrieren.
>
> **Wiederholbares Vorgehen pro System:** `reference/engine_integration_playbook.md` (Katalog → Struktur → Engine-Validierung → später KG-Seed).

### 1.0 Architekturentscheidung ✅ (Planung)

**Entschieden:** Hybrid TS-first (→ engines.md §4)
- TS in Next.js: HD-Client, Ziwei (iztro), BaZi (@yhjs), **Astro (celestine)**, Maya, Triviale
- Python-Microservice (FastAPI, Docker): Jyotish (PyJHora AGPL isoliert + VedAstro.Python MIT für KP)
- Kein Spark für Engines (Spark = nur GPU)

**Noch offen (Spikes nötig):**
- [x] Spike: iztro (Ziwei) — `@ic/engines` + `system_descriptors/ziwei.json` + `system_structure/ziwei_catalog_v0.json` + `ziwei_structure_v0.json` + Vitest-Abgleich Chart-`nodes`↔Katalog (`ziwei-catalog-validation`); Doku `engines.md` §15, `contracts.md` (`ziwei`)
- [x] Spike: @yhjs/bazi — `@ic/engines`: `computeBaziChart`, Katalog/Struktur/Test wie Playbook (`bazi_catalog_v0.json`, `bazi_structure_v0.json`); `engines.md` §16
- [x] Spike: HD — dturkuler/humandesign_api als Engine (alle 13 Layer, Composite, Transit, BodyGraph). GPL-3.0 Docker-isoliert.
- [x] Spike: **Westl. Astro** — **celestine** in `@ic/engines` (`computeAstroChart`, Katalog `projects/inner_compass/system_structure/astro_catalog_v0.json`, Tests). Optional offen: Präzisions-/Ephemeris-Abgleich vs. Referenz (Swiss o. ä.), falls Produkt es braucht.
- [x] Spike: PyJHora als FastAPI-Microservice — `services/jyotish/` (Docker, D1); AGPL bleibt auf diesem Service isoliert; siehe `services/jyotish/README.md`
- [ ] Swiss Ephemeris **kommerzielle** Lizenz nur nötig, wenn ihr Swiss Ephemeris **ohne** AGPL-konforme Open-Source-Kette nutzen wollt; aktuell: `pyswisseph`+PyJHora im AGPL-Service = üblicher Open-Source-Pfad (rechtlich mit eurem Anwalt finalisieren)
- Code-Repo: `code/inner_compass_app/` (Makerkit **4.0.6**, Next 16.3.3; Branch `cursor/makerkit-v4`)
- TS-Engines: `packages/engines/` (@ic/engines, npm-basiert)
- Python-Service: `services/jyotish/` (PyJHora + jyotishganit + VedAstro, Docker)
- ⚠️ Noch zu installieren / priorisieren: **Maya**-Kit, triviale Systeme (iztro ✅, @yhjs/bazi ✅, **celestine** ✅)
- → Details: engines.md §4 (Architektur) + §5 (Kit-Kandidaten) + §8 (Prüf-Checkliste)

### 1.1 Pro System: Spike → Bewerten → Entscheiden → Integrieren

Pro System diese 4 Schritte:

| # | Schritt | Ergebnis |
|---|---------|----------|
| a | **SPIKE** — Kit zum Laufen bringen. Input rein, Output raus? | Funktioniert: ja/nein, was liefert es? |
| b | **BEWERTEN** — Deckt es unsere Anforderungen? Was fehlt? | Decision: Keep / Replace / Supplement |
| c | **INTEGRIEREN** — Sauber in Engine-Service einbauen | API-Contract, Input/Output definiert |
| d | **EXTRAHIEREN** — Vollständigen Strukturbaum aus laufendem Kit | Deskriptor + Structure JSON erweitert |

Reihenfolge der Systeme:

| Prio | System | Kit (Empfehlung) | Lizenz | Sprache | Bekannte Issues |
|------|--------|-----------------|--------|---------|-----------------|
| 1 | HD | **dturkuler/humandesign_api** (vendored, Docker) | GPL-3.0 isoliert | Python | ✅ Komplett: 13 Layer + Composite/Transit/BodyGraph. 65 Tests grün. |
| 2 | **Ziwei Doushu** 🆕 | **iztro** (SylarLong) | MIT ✅ | **TS** | 3.5k Stars, React-Hook, TS-nativ. Reichste chin. Tradition. |
| 3 | BaZi | **@yhjs/bazi** (primär) + alvamind | MIT ✅ | TS | @yhjs: Luck Cycles + Nayin + Ten Gods. Umfangreicher als alvamind. |
| 4 | Astro | **celestine** (TS, in `@ic/engines`) | MIT | TS | Implementiert. Optional: Präzisionsvergleich mit Referenz-Ephemeris. |
| 5 | Maya | tzolkin-calendar | MIT ✅ | Python | Komplett (einfachstes System). |
| 6 | Jyotish | **PyJHora** (AGPL, isoliert) + VedAstro.Python (MIT, KP) | ⚠️ AGPL + MIT | Python | PyJHora als isolierter Microservice (AGPL-Code open-sourced). Max. K1/K2-Tiefe. |
| 7 | Gene Keys | **Kein** separates Chart-Engine-Paket wie HD: **K1** geteilt (Gate-Lage), **K2** eigen (`gk.*`) | — | TS (Lookup + HD-Client) | Literatur-Pipeline wie übrige `system_id` (`genekeys_content` / `entity_registry` noch anzulegen). |
| 8–11 | Num, NSK/Mewa, Akan, EG | Eigene TS-Impl. / JSON | — | TS | Trivial. |

**Stand (April 2026):** Chart-Engines: **HD** (Python), **Jyotish** (Python), **Ziwei + BaZi + Astro** (TS), plus in `@ic/engines`: **Maya Tzolkin**, **Nine Star Ki (v1)**, **Numerologie**, **Akan** — siehe Abschnitt „Wo wir sind“ oben. **Ur-Systeme** (I Ging, Kabbala, Chakren): Deskriptoren (+ teils Kataloge), **Literatur-Pipeline** wie oben noch zu eröffnen.

**Nächste Spikes / Backlog:** Trivial-Engines K1/K2 weiter schärfen (Maya/Numerologie/Akan: Validierung + Feintuning) → optional Astro-Präzision → **Ur-Systeme:** je `system_id` Registry + MinerU-Pfad.

### 1.2 Erweiterter Seed

- [x] ic_seed_structure.py — HD aus `system_structure/*` (**2026-07-02:** +233 Nodes, +115 Edges: PHS, Variables, Crosses, Strategy/NotSelf/Signature, Catalog-Circuits)
- [ ] ic_seed_structure.py — übrige Systeme aus `system_structure/*` (nicht nur hardcoded Skeleton) — **BaZi zuerst** (Blocker aus S5d-Qualitäts-Gate: ohne Seed erfindet text2kg Nodes, siehe Phase 2 / S5d)

### HD: 69.120 vs. Struktur-Vollständigkeit

| Konzept | Anzahl | Im KG als Node? |
|---------|--------|-----------------|
| Berechenbare Positionen (Gate×Line×Color×Tone×Base) | ~69.120 | **Nein** — Chart-Ergebnis (K1), Property auf Chart |
| Atomare Struktur-Nodes (Gates, Lines, PHS, Crosses, …) | ~700–780 | **Ja** — K2-Seed |
| PHS (Color/Tone/Base) | 17 global | **Ja** — „Color 3“ bedeutet überall dasselbe |

Mit vollständigem atomarem Seed können **alle** Kombinationen interpretiert werden, ohne 69k Nodes. Siehe `reference/hd_structure_13_layers_and_engines.md` §2.
- [ ] Deskriptoren erweitern (structure-Block pro System)
- [ ] Konsistenz-Check: Kit-Struktur vs. Deskriptor element_types vs. geseedete Nodes
- → Backlog: `reference/deep_structure_plan.md` (Ziel-Node-Zahlen pro System)

---

## Phase 2: Content-Pipeline (nach Phase 1)

### S5 — HD E2E-Validierung ✅ (S5a 2026-07-02 · S5b 2026-07-03)

- [x] PDF-Upload (VM105, `--sys-mode`)
- [x] **S5a:** extract_text + Gate-Chunk-Profil (~47 Gates erster Lauf), text2kg → `hd.gate.{N}`, synthesize
- [x] **S5b:** `ic_chunk_profiles.py` (`rave_iching_gates`) → 65 Chunks / 64 unique Gates (MinerU pipeline)
- [x] Phase 2 LLM + text2kg + synthesize für Complete Rave I'Ching — **64/64** echte Gate-Wortings
- [x] Gate-Lines Layer (2026-08-07): additive Line-Chunks + PDF-Refill + Relink 1:1 + Synth — **384/384** Wordings
- [x] Verifikation: Gate-Nodes mit `interpretation_ids`, Synthesis ohne `[DRY-RUN]`-Stubs
- **Skripte:** `ic_s5b_rerun.py`, `spark_s5b_extract.sh`, `spark_s5b_synth.sh`, `ic_s5b_gate63_synthesis.py`
- → Runbook: `reference/s5_runbook.md` · Handover: `cursor/handover.md` §S5

### S5c — Gene Keys 64 Ways ✅
- [x] GK linking + synthesis 64/64 — produktive K4 behalten

### S5d — BaZi (Joey Yap Destiny Code) — Pipeline-Mechanik ✅ · K2 Foundation ✅ (2026-07-11)
- [x] Source `cbe86636-…` — 648p PDF, MinerU **page batches** (50), 420 Chunks
- [x] Phase 2: 420 Interpretationen (10×40 Batch-Recovery), text2kg, synthesize — **Mechanik E2E bewiesen**
- [x] Wu 午 via `ic_s5d_bazi_branch_relink.py` · Learnings: `cursor/reference/s5d_pipeline_learnings.md`
- [x] **Qualitäts-Gate + Sanierung (2026-07-10):**
  - Wildwuchs bereinigt: **460 → 37** Katalog-Kern (`ic_s5d_bazi_wildwuchs_cleanup.py`, 438 gelöscht)
  - K2-Seed: **97 Nodes** (37 Kern + **60 Jiazi**, 140 Edges) — `ic_seed_structure.py --system bazi`
  - Whitelist: `ic_bazi_k2_catalog.BAZI_K2_STRICT_IDS` · text2kg strict mode
  - Re-Link: **1253 Links, 0 neue Nodes**; Re-Synthese **37/37** Kern-Nodes
  - Ten-God-Relink: `shishen`/`pianyin`/`zhengyin` via `ic_s5d_bazi_tengod_relink.py`
- **Nächste Welle:** Jiazi-PDF → Interpretationen auf `bazi.jiazi.*` · Playbook: `reference/k2_foundation_wave_playbook.md`
- **Skripte:** `ic_bazi_k2_catalog.py`, `ic_s5d_bazi_*`, `spark_s5d_extract.sh`, `spark_s5d_phase2.sh`

### K2 Foundation — Gesamtsanierung ✅ (2026-07-12)
- [x] **Alle 3 aktiven Systeme sauber** (`ic_k2_state_audit.py`): 0 Wildwuchs, 0 offene Jobs, jede Interp-Node hat Synthese
  - BaZi: 97 Nodes · 37 Synthese | HD: 777 Nodes · 114/114 | GK: 64 · 64/64
- [x] **Re-Seed-Bug behoben:** Seed überschrieb `interpretation_ids`/`canonical_description` → Metadata-Erhalt in `ic_seed_structure.py`; Sanierung via `ic_relink_strict.py` (678 HD-Links) + `ic_restore_desc_from_wordings.py` (137 Descriptions ohne LLM)
- [x] HD Alias-Remap (`g_center`→`g` etc., 8 remapped) · GK-Cleanup (167 asset_chunks) · 3 Zombie-Jobs geschlossen
- **Neue Kern-Tools:** `ic_k2_state_audit.py` (Abschluss-Gate pro Welle), `ic_relink_strict.py`, `ic_restore_desc_from_wordings.py`, `ic_k2_synth_batch.py`

### S6 — Life Force (HD Channels) ✅ (2026-07-08)
- [x] Source `2a9272bc-…` — 175 Chunks, `elements`-Rerun, Channel-Migration, text_relink
- [x] **36/36** Kanon-Channels linked+syn (`ic_s6_channel_report.py`)
- [x] Orphan Reverse-/Bogus-Nodes bereinigt (`ic_s6_orphan_channel_cleanup.py`)
- [x] Worker-Learnings dokumentiert: `reference/s6_pipeline_learnings.md` (lokal vs. Spark, 1000-Limit, CRLF)
- **Skripte:** `ic_elements_rerun.py`, `ic_s6_channel_*`, `spark_s6_phase2.sh`, `spark_s6_synth_only.sh`

### Ziwei Natal-First-Cut (中州) ✅ First Cut 2026-08-29 — nicht verified

Pfad A Natal-Parität (Decision 2026-08-27). Compute = iztro. LLM = Langdock gpt-5-mini. Spark nur MinerU. Zwischenstand-Sprache der Atome = **en** (DE später zweite `wordings.language`-Zeile).

- [x] K2-Seed + Strict-Whitelist `ic_ziwei_k2_catalog.py` (`zw.*`→`ziwei.*`, Homophone 天府/天福, 四化-Aliase)
- [x] Staffel 1 Extract+OCR+interpret+text2kg (初级/星曜/深造/补注/全集); 流年-Buch Extract geparkt
- [x] Welle 1b: 安星法 86 · 谈斗数 32 · 八喜楼 34 · 骨髓赋 28 · 太微赋-Note 5
- [x] Homophone-Repair, Palast-Relink **v2**, 四化-Relink v1 (4/4 Synth), 辅星-Relink+Synth v1 **8/8**
- [x] Scoped Synth EN: 14 Maj + 身 + 命/财/官 nach v2 + 四化 + 辅星 — **kein** Full-Synth
- **Qualität / was nicht 100 %:** `reference/ziwei_natal_ingest_runbook.md` (安星法-Mentions lassen, 来因/煞/Band 1/DE/流年-KG offen). 命宫/化权/天钺 scoped Re-Synth 2026-08-31; EN-Pinyin „Tianyue“ bleibt bis DE-Atome.
- [x] KARTE Natal-Gitter 2026-08-29: 4×4 地支, 辅星+四化 im Inspector, Badge draft/canon_fallback (nicht verified)
- [x] KARTE Chrome+dichte Platte 2026-08-31: DE-Labels, Helligkeit, Kleinsterne als Position, Dekade, Legende, 命主≠命宫-Sterne. Plate-Contract **5/5** (inkl. Fixture 1980-11-18)
- [x] Zusammenschau 2026-08-31: `ziwei_overlay_v3` (Lebenssatz+Belege, DE, keine Buchzitate; Cache-Ruleset v3). URL in `.env.development`, Key in `.env.development.local`.
- [x] Kleinstern-Lexikon First Cut 2026-08-31: Relink `ziwei_sha_adj_relink_v1`, scoped Synth EN **20** Nodes mit primary (六煞 + u. a. 天刑/天喜/华盖/咸池). Rest ohne primary = Position-only.
- [x] Paläste+身 scoped Re-Synth nach v2 (10/10); 命宫 Life Palace; 化权 Authority; 天钺 Patronage (`tianyueMin`). 天月 unberührt.
- **Nicht:** Mandala, Handbuch-Generator, Qwen, 三合/飞星, DE-Atome, 来因/流年-UI. 杂 ohne primary nicht Label-Spray. Overlay-Alltagssprache = spätere Welle. `verified`-Gate für Ziwei-Atome aus.

### S6 — Anna's Archive Pipeline
- [x] hd_saas_uploader.py: `--sys-mode`
- [x] **Entity-first:** `entity_registry.json` pro Profil (`hd`, `astro`, `jyotish`, `ziwei`, `bazi`) + `simple_collector`-Anbindung (Toolkit `code/annas-archive-toolkit/`)
- [ ] Gate 1: LLM-Vorklassifikation
- [ ] Metadata-Collection + Download + Upload **flächendeckend** (inkl. Ur-Systeme, Gene Keys, HD bereits anstoßbar)
- → Kann teilweise parallel zu S5 laufen; **HD-Downloads** nach `download_priority_order` sind sinnvoll sobald VPN/VM102 bereit

### S7 — Cloud-Deployment
- [ ] Cloud-Supabase + Worker auf Spark + E2E-Test

---

## Phase 3: Cross-System + IC-Sprache (nach Phase 2)

> **Hier entsteht die IC-Sprache.** Netze übereinanderlegen → Klumpen finden → eigene Konzepte destillieren.
>
> ⚠️ **Vor Start lesen:** `reference/cross_system_mapping_methodology_review.md` (2026-07-01) — die dokumentierte Methodik (Embedding-Cosine-Similarity auf `canonical_description` als primäres Auswahlkriterium) hat einen methodischen Konstruktionsfehler, kein reines Human-Review-Problem. Offener Review, muss vor Implementierung entschieden werden (→ ggf. `decisions.md`).
>
> ⚠️ **Ebenfalls vor Start:** `reference/gesamtbetrachtung_review_2026-07.md` (2026-07-02) — Gesamtkonzept-Review. Für Phase 3 relevant: **System-Genealogie fehlt als Daten** (Z1 §4.2 verlangt Konvergenz-Gewichtung nach Verwandtschaft — Konvergenz-Service hat das nicht) und **`contradicts`-Edges werden von keinem Job erzeugt** (Widerspruchs-Protokoll Z1 §5.2 ohne Pipeline). Priorisierte Folge-Aufgaben in §8 dort.

- [ ] Embeddings generieren (text-embedding-3-large oder lokal)
- [ ] Strukturelle Cross-Edges anlegen (HD Gate = I Ging Hex, faktisch)
- [ ] Semantische Cross-Mappings (Embedding-Similarity + LLM-Validierung)
- [ ] Klumpen-Analyse: Wo konvergieren 3+ Systeme?
- [ ] IC-Konzepte destillieren: LLM extrahiert kulturübergreifenden Kern pro Klumpen
- [ ] Human Review: IC-Sprache bestätigen/verfeinern → sys_kg_nodes (system='meta')
- [ ] Review-Workflow für Mapping-Kandidaten
- → Details: architecture.md §15 (KG-Übereinanderlegen & IC-Sprache)

---

## Phase 4: App + Visualisierung (Details: architecture.md §12–14)

- [ ] User Data Model (user_persons, user_charts, user_progress, user_sessions)
- [ ] Chart-Engine-Service (nutzt Phase-1-Engines)
- [ ] IC Mandala Visualisierung
- [x] System-Chart-Renderer First Cut: HD BodyGraph ✅ · Ziwei-Platte ✅ · Astro-Rad ✅ (2026-09-02). Offen: BaZi Pillars, Maya Kin, Overlay Astro
- [ ] Handbuch-Generator (Tiefe 1–2)
- [ ] 4 App-Spaces: JETZT, KARTE, WERKSTATT, ZEIT
- [ ] WERKSTATT: Brunnen→Leiter Flow-Engine + Anker v1
- [ ] Transit-Service, Konvergenz-Service, Lens-Switcher
- [x] Onboarding-Gate nach Signup (`role=self`); JETZT Signatur-Highlight
- → Scope: consolidation/ic_gesamtinventur.md §XX (v1/v2/v3)
- → Delta: consolidation/ic_gesamtinventur.md §XXI (8 Lücken)

## Tooling: MCP-Server (3 Server für KI-gestützte Entwicklung)

### Makerkit Kit MCP (lokal, gebaut)

**Pfad:** `code/inner_compass_app/packages/mcp-server/`
**Konfiguration:** `.cursor/mcp.json` (Workspace-Root)
**Rebuild:** `pnpm --filter "@kit/mcp-server" build`

| Kategorie | Tools | Beschreibung |
|-----------|-------|-------------|
| **Schema** | `get_schema_files`, `get_schema_content`, `get_schemas_by_topic`, `get_schema_by_section` | Liest Schema-Dateien aus `apps/web/supabase/schemas/` |
| **DB-Live** | `get_database_summary`, `get_database_tables`, `get_table_info`, `get_all_enums`, `get_enum_info` | Queries gegen laufende lokale DB (Port 54322) |
| **Functions** | `get_database_functions`, `get_function_details`, `search_database_functions` | Postgres-Funktionen analysieren |
| **Migrations** | `get_migrations`, `get_migration_content`, `create_migration`, `diff_migrations` | Migrations verwalten + Schema-Diff |
| **DB-Ops** | `kit_db_status`, `kit_db_migrate`, `kit_db_seed`, `kit_db_reset` | DB-Lifecycle via Supabase CLI |
| **Env** | `kit_env_*` | Umgebungsvariablen verwalten |
| **Dev** | `kit_dev_*` | Dev-Server starten/stoppen |
| **Translations** | `kit_translations_*` | i18n-Dateien verwalten |
| **Emails** | `kit_emails_*`, `kit_email_templates_*` | E-Mail-Templates + Mailbox |
| **Status** | `kit_status_*`, `kit_prerequisites_*` | Projekt-Status + Voraussetzungen prüfen |
| **Code** | `components_*`, `scripts_*`, `run_checks_*`, `deps_upgrade_advisor_*` | Komponenten, Scripts, Checks, Dependency-Upgrades |
| **PRD** | `prd_*` | Product Requirements verwalten |

### Supabase MCP (Cursor Plugin)

**Konfiguration:** `.cursor/settings.json` → `plugins.supabase.enabled: true`
**Auth:** Muss beim ersten Zugriff authentifiziert werden (`mcp_auth`)
**Zugriff:** Supabase Management API (Cloud-Projekte), direkte SQL-Queries

### Makerkit CLI MCP (optional, noch nicht aktiv)

**Start:** `npx @makerkit/cli@latest makerkit-cli-mcp`
**Nutzen:** Plugin-Installation, Upstream-Updates (`project update`), Merge-Konflikte lösen
**Wann:** Wenn wir Makerkit-Plugins installieren oder Upstream-Updates ziehen

### Zusammenspiel

```
Lokale Supabase ──────── Makerkit Kit MCP ──── Cursor KI
     (Port 54322)           (Schema, Migrations, Dev)
                                    │
Supabase Cloud ────────── Supabase MCP ──────── Cursor KI
     (Prod/Staging)        (Management API, SQL)
                                    │
Makerkit Upstream ─────── CLI MCP ──────────── Cursor KI
     (Updates, Plugins)    (project update, plugins)
```

---

## Dokumenten-Landkarte

| Schicht | Dokumente | Zweck | Stand |
|---------|-----------|-------|-------|
| **Philosophisch** | consolidation/z1 (Gesamtwerk v0.5), z3 (Modelle v0.4), Glossar v1.2 | Was ist der IC? | ✅ Fertig |
| **Produktplanung** | consolidation/z2 (User-Journey v0.1, veraltet), ic_gesamtinventur.md v0.5 | Wie erlebt der User das? | 🟡 Z2 Update nach Phase 1 |
| **Technisch** | cursor/{architecture, pipeline, contracts, engines, status}.md | Wie ist es gebaut? | 🔄 Aktiv (engines.md aktuell) |
| **Engine-Framework** | kern/IC_System_Pruef_Framework.docx | K1–K4 Datenkategorien, Evidenzklassen, Prüf-Checkliste | ✅ Integriert in engines.md |
| **Inventur** | consolidation/ic_gesamtinventur.md §I–XIX | Komplettes Baustein-Inventar | ✅ Stabil |
| **Scope** | consolidation/ic_gesamtinventur.md §XX–XXI | v1/v2/v3 Feature-Cut + Delta | ✅ Stabil |

**Z4 (Architecture) = cursor/ Dateien.** Kein separates Z4-Dokument — cursor/ ist die technische Dokumentation.

---

## Entscheidungs-Log (Kurzform)

Vollständig: `reference/decisions.md`

| Datum | Entscheidung | Begründung |
|-------|-------------|------------|
| 2026-02 | 15 statt 12 Dimensionen | +elemental_quality, temporal_phase, destiny_pattern für Multi-System |
| 2026-02 | 10 statt 8 Lebensbereiche | Sexualität ≠ Partnerschaft, Community ≠ Familie |
| 2026-03 | **12 statt 10 Lebensbereiche** | +Austausch & Lernen (3. Haus/Bhava/兄弟宫), +Wandlung & Erneuerung (8.+12. Haus). Revision von §20d (ergebnis_modelle.md): Alte Ablehnung war HD-zentrisch, hält nicht bei 14 Systemen mit je 12 Domänen. |
| 2026-02 | Mandala statt Radar-Chart | Einzigartige Signatur, SM-teilbar, kein Bewertungscharakter |
| 2026-02 | Keine Entwicklungsstufen (anti-AQAL) | Systeme beschreiben Qualitäten, nicht Hierarchien |
| 2026-02 | Drei Sprachebenen (System/Meta/Handbuch) | Copyright + Verständlichkeit + Synthese |
| 2026-02 | Postgres+pgvector statt ArangoDB | Supabase-Ökosystem, kein separater Graph-DB-Server |
| 2026-02 | Strukturbäume aus Deskriptoren, nicht PDFs | Struktur ist deterministisch, PDFs liefern nur Interpretationen |
| 2026-04 | Engine-Integration VOR Pipeline | Vollständige Strukturbäume nötig, bevor Pipeline sinnvoll extrahieren kann |
| 2026-04 | cursor/ = Z4 | Kein separates Architecture-Enddokument — cursor/ Dateien sind die technische Doku |
| 2026-04 | Hybrid TS-first Engine-Architektur | TS in `@ic/engines` für Ziwei/BaZi/Astro (+ später Maya/trivial); **HD + Jyotish** als **HTTP-Microservices** (`services/hd`, `services/jyotish`). Kein Spark für Engines. |
| 2026-04 | `architecture.md` §5–6 = Laufzeit-Wahrheit | Topologie-Tabelle und ASCII: `iztro` / `@yhjs/bazi` / `celestine` + getrennte Python-Services; kein veraltetes hdkit/alvamind/VedAstro-Western im App-Pfad. |
| 2026-04 | PyJHora (AGPL) als isolierter Microservice BEHALTEN | Max. K1/K2-Tiefe. Code wird open-sourced, App bleibt privat. VedAstro.Python (MIT) als KP-Ergänzung. |
| 2026-04 | node-jhora ist NICHT open source | Proprietäre "Source Available"-Lizenz mit Royalty. In Vordiskussion fälschlicherweise als OS empfohlen. |
| 2026-04 | K1–K4 Datenkategorien + Evidenzklassen | Aus IC_System_Pruef_Framework.docx integriert. Bestimmt Datenherkunft + Vertrauenswürdigkeit. |
| 2026-04 | Ziwei Doushu (iztro) als neues System | TS-nativ, MIT, 3.5k Stars. Ergänzt BaZi fundamental (Mond- vs. Sonnenkalender). |
| 2026-04 | @yhjs/bazi ersetzt alvamind als primärer BaZi-Kit | MIT, TS, Luck Cycles + Nayin + Ten Gods. Umfangreicher. |
| 2026-04 | **celestine** für Westl. Astro in `@ic/engines` | MIT, TS — im Status bis 2026-04-17 als implementiert geführt (alter Arbeitstitel: CircularNatalHoroscopeJS). |
| 2026-04 | Zwei System-Rollen: calculation + structural | I Ging, Kabbalah, Chakras als reguläre Systeme (nicht hierarchisch). IC-Sprache emergiert aus Konvergenz-Klumpen (Datenschicht E). |
| 2026-03 | **Fresh Clone Makerkit 3.1.3** | hd_saas_app (v2.24) → inner_compass_app (v3.1.3). IC-Eigenarbeit (~2200 Zeilen) portiert/wird neu geschrieben. Engine-Struktur: npm statt Vendoring (TS), Python-Microservice für Jyotish. |
| 2026-03 | **GitHub-Repo: inner-compass-app** | quantensprungai/inner-compass-app (privat). Upstream: makerkit/next-supabase-saas-kit-turbo. Altes Repo hd-saas-app archiviert. |
| 2026-04 | **3 MCP-Server konfiguriert** | Makerkit Kit MCP (lokal, 56 Tools: Schema/DB/Env/Dev), Supabase MCP (Cloud), CLI MCP (optional). Cursor `.cursor/mcp.json` angelegt. KI hat direkten Zugriff auf DB-Schema, Migrations, Env, Dev-Services. |
| 2026-04 | **dturkuler/humandesign_api als HD-Engine** | GPL-3.0 vendored in Docker (SaaS-konform). Ersetzt hdkit+geodetheseeker. Alle 13 Layer + Composite/Transit/BodyGraph. K2-Daten extrahiert (192 Crosses, 8 Awareness Streams, evidence A). |
| 2026-04 | **Gene Keys als eigenständiges System** | GK ist NICHT "HD mit anderer Sprache". Shared K1 (Ephemeris), eigenes K2 (Shadow/Gift/Siddhi, Codon Rings, Sequences). Im KG: `gk.*` Prefix, Cross-Link über `hd.gate.N ←→ gk.gate.N`. |
| 2026-04 | **Gene Keys: Literatur wie alle Systeme** | Keine gesonderte Copyright-/Paraphrase-Policy in Projekt-Doku; Beschaffung + Extraktion + Evidenzklassen wie bei HD/Astro/etc.; eigenes Anna's-Profil + `entity_registry` nach Bedarf. |
| 2026-08 | **HD-Gate-Stimmen konkret** | `jovian` Default; `64keys` = Blue I Ching; `cosmic_sidereal` = Cosmic Way (64 Gates sideral, keine Engine); Schoeber *Centres* = HD-Text trotz 64keys-Orbit. Kein Schul-Ingest vor `tradition`. `decisions.md` 2026-08-13. |
| 2026-04 | **HD-Schulen als Tradition-Tag** | Jovian Archive, Quantum HD, 64Keys, Parkyn teilen K1+K2. Unterschiede nur in K3/K4 (Interpretation). Modelliert als `tradition`-Tag auf Interpretation-Nodes, nicht als separate Systeme. |
| 2026-04 | **Konvergenz: Person + strukturell; v0 Rechenbasis** | Klumpen/Meta: (1) personengebunden über Chart-Überschneidung, (2) personen-unabhängig über Cross-Edges/Embeddings zwischen Ur-/Element-KGs. Klein-Systeme v0: eine K1/K2-Konvention, eher moderne dokumentierbare Linie wo sinnvoll; Tradition über K3/K4 + Linsen. Volltext: `reference/decisions.md` 2026-04-19. |
| 2026-04 | **Phase-1 triviale Systeme: Schulwahl + Engines** | Maya GMT+Dreamspell-Slugs; NSK japanisch Li Chun 4.2.; Numerologie Pythagoreisch; Akan Wochentagstabelle. `@ic/engines` + Kataloge + Next-API. Volltext: `reference/decisions.md` 2026-04-20. |
| 2026-04 | **Nine Star Ki K1/K2 v1** | Tabellen-Honmei (+Overrides, 1986→1984), Monatsmuster statt Differenzformel, energetic (81er), feste Sonnenmonats-Schnitte, Vitest Step 3. `reference/decisions.md` 2026-04-16. |
| 2026-04 | **Maya Tzolkin v1 + Step 3** | Lokales Zivil-Datum aus `utcMillisForWallTimeInZone`; `ic_maya_tzolkin_v1`; Vitest vs. `mayan_tzolkin_catalog_v0.json`. `reference/decisions.md` 2026-04-16. |
