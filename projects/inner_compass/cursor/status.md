# Inner Compass — Status & Nächste Schritte

> **Stand:** 2026-04-15 | Bei jedem Meilenstein aktualisieren!
>
> **Wo wir sind:** Phase 0 erledigt. Phase 1 — 4 von 6 Berechnungssystemen integriert:
> - **Ziwei Doushu** (iztro): TS, Katalog + Validierung ✅
> - **BaZi** (@yhjs): TS, Katalog + Validierung ✅
> - **Jyotish** (PyJHora): Python-Microservice, D1+D9+Dasha+Bhavas+Yogas+16 Vargas ✅
> - **Human Design** (dturkuler): Python-Microservice, alle 13 Layer + Composite/Transit/BodyGraph ✅
> - **Westl. Astrologie**: Noch offen (CircularNatalHoroscopeJS)
> - **Maya Tzolkin**: Noch offen (trivial)
>
> Nächster Schritt: Verbleibende Systeme (Astro, Maya, triviale), dann Phase 2 (Content-Pipeline).

## Was EXISTIERT und FUNKTIONIERT

### Infrastruktur ✅
- Makerkit-App (Next.js + Supabase): Auth, Accounts, UI-Shell
- Spark GPU-Server: MinerU (PDF-Parsing), SGLang/vLLM (LLM-Inferenz)
- Tailscale VPN: Spark ↔ Supabase ↔ Dev
- System-Deskriptoren: 10 JSON-Dateien (HD, BaZi, Astro, Jyotish, Maya, Gene Keys, Enneagram, Numerology, Nine Star Ki, Akan)

### Jyotish Microservice (Code-Repo) — Phase 1a ✅
- Pfad: `code/inner_compass_app/services/jyotish/` — FastAPI, `POST /calculate` mit `BirthData` wie `@ic/engines`
- **D1 (Rāśi):** PyJHora `rasi_chart` (Swiss Ephemeris via `pyswisseph`)
- **Docker:** `python:3.12-slim` + `build-essential` (Build `pyswisseph`); `requirements.txt` enthält u. a. explizit **`pytz`**, **`geocoder`**, **`geopy`**, **`timezonefinder`**, **`python-dateutil`** — PyJHora listet nicht alle Laufzeit-Imports als pip-Dependencies; ohne diese Module bricht die Berechnung mit ImportError ab
- **E2E (2026-04-13):** Image bauen, Container starten, nach ~25 s `GET /health` + `POST /calculate` (Test: Berlin 1990-01-15 12:30) → `raw.placeholder: false`, `raw.bodies`: 13 Einträge, `raw.chart: D1`, `nodes` mit `jyotish.lagna` / `jyotish.rasi.*` / `jyotish.graha.*`
- **Noch offen:** Aufruf aus Next.js (Env-URL), Playbook-Artefakte (`jyotish_catalog_v0.json`, …) wie Ziwei/BaZi, weitere Charts (D9, Dasha, …)

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
- Datenqualität: ~85% Noise bei HD-Keywords (Lösung: Zwei-Gate-Filtering, siehe pipeline.md §8)
- hd_saas_uploader.py: `--sys-mode` für PDF-Upload (sys_sources, sys_ingestion_jobs, sys_uploads_raw) — S5 nutzbar
- Bestehende DB-Daten: Nur Stubs, werden NICHT migriert (Clean Data Restart)
- assets.jsonl in scratch/: Falsch platziert, werden bei Clean Restart neu generiert

## Gesamtprozess (5 Phasen)

```
Phase 0: Fundament          ████████████ 100%  S1–S4 erledigt
Phase 1: Engine Eval+Integ. █████████░░░  ~70%  Ziwei+BaZi+Jyotish+HD komplett; Astro+Maya+Triviale offen
Phase 2: Content-Pipeline   ░░░░░░░░░░░░   0%  blockiert durch Phase 1
Phase 3: Cross-System       ░░░░░░░░░░░░   0%  → IC-Sprache entsteht hier (Datenschicht E)
Phase 4: App                ██░░░░░░░░░░  15%  Architektur+Scope dokumentiert
```

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

### S4 — Seed-Script + Strukturbäume ✅
- 832 Nodes + 698 Edges (10 Systeme, HD: 526 Nodes)
- Idempotent, Cross-System (Gene Keys → HD Gates)
- **Aber:** Nur Basis-Skeletons — vollständige Bäume fehlen (→ Phase 1)

</details>

---

## Phase 1: Engine Evaluation & Integration ← NÄCHSTER SCHRITT

> **Kernidee:** Engines sauber in den Stack integrieren, dabei Strukturbäume extrahieren. Nicht separat analysieren und dann nochmal integrieren.
>
> **Wiederholbares Vorgehen pro System:** `reference/engine_integration_playbook.md` (Katalog → Struktur → Engine-Validierung → später KG-Seed).

### 1.0 Architekturentscheidung ✅ (Planung)

**Entschieden:** Hybrid TS-first (→ engines.md §4)
- TS in Next.js: HD, Ziwei (iztro), BaZi (@yhjs), Astro (CircularNatalHoroscopeJS), Maya, Triviale
- Python-Microservice (FastAPI, Docker): Jyotish (PyJHora AGPL isoliert + VedAstro.Python MIT für KP)
- Kein Spark für Engines (Spark = nur GPU)

**Noch offen (Spikes nötig):**
- [x] Spike: iztro (Ziwei) — `@ic/engines` + `system_descriptors/ziwei.json` + `system_structure/ziwei_catalog_v0.json` + `ziwei_structure_v0.json` + Vitest-Abgleich Chart-`nodes`↔Katalog (`ziwei-catalog-validation`); Doku `engines.md` §15, `contracts.md` (`ziwei`)
- [x] Spike: @yhjs/bazi — `@ic/engines`: `computeBaziChart`, Katalog/Struktur/Test wie Playbook (`bazi_catalog_v0.json`, `bazi_structure_v0.json`); `engines.md` §16
- [x] Spike: HD — dturkuler/humandesign_api als Engine (alle 13 Layer, Composite, Transit, BodyGraph). GPL-3.0 Docker-isoliert.
- [ ] Spike: CircularNatalHoroscopeJS — Präzisionsvergleich mit Swiss Ephemeris
- [x] Spike: PyJHora als FastAPI-Microservice — `services/jyotish/` (Docker, D1); AGPL bleibt auf diesem Service isoliert; siehe `services/jyotish/README.md`
- [ ] Swiss Ephemeris **kommerzielle** Lizenz nur nötig, wenn ihr Swiss Ephemeris **ohne** AGPL-konforme Open-Source-Kette nutzen wollt; aktuell: `pyswisseph`+PyJHora im AGPL-Service = üblicher Open-Source-Pfad (rechtlich mit eurem Anwalt finalisieren)
- Code-Repo: `code/inner_compass_app/` (Makerkit 3.1.3, frischer Clone 2026-03-31)
- TS-Engines: `packages/engines/` (@ic/engines, npm-basiert)
- Python-Service: `services/jyotish/` (PyJHora + jyotishganit + VedAstro, Docker)
- ⚠️ Noch zu installieren: CircularNatalHoroscopeJS, hdkit (iztro ✅, @yhjs/bazi ✅)
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
| 4 | Astro | **CircularNatalHoroscopeJS** (TS) + pyswisseph (Python) | Unlicense / 💰 | TS+Py | CircularNatalJS: kein Swiss-Eph-Lizenzproblem! Spike: Präzisionsvergleich. |
| 5 | Maya | tzolkin-calendar | MIT ✅ | Python | Komplett (einfachstes System). |
| 6 | Jyotish | **PyJHora** (AGPL, isoliert) + VedAstro.Python (MIT, KP) | ⚠️ AGPL + MIT | Python | PyJHora als isolierter Microservice (AGPL-Code open-sourced). Max. K1/K2-Tiefe. |
| 7 | Gene Keys | — (= HD-Positionen + Lookup) | — | — | ©-Problem: Nur Paraphrase, keine Rudd-Zitate. |
| 8–11 | Num, NSK/Mewa, Akan, EG | Eigene TS-Impl. / JSON | — | TS | Trivial. |

**Stand (April 2026):** 4 von 6 Berechnungssystemen integriert. HD mit dturkuler (GPL-3.0, Docker-isoliert) — vollständigste Engine mit allen 13 Layern. Jyotish mit PyJHora (AGPL, Docker-isoliert) — Phase 2/3 komplett (D1+D9+Dasha+Bhavas+Yogas+16 Vargas). Ziwei + BaZi als TS in-process.

**Nächste Spikes:** Astro (CircularNatalJS) → Maya (trivial) → Triviale (Numerologie, NSK, Akan).

### 1.2 Erweiterter Seed

- [ ] ic_seed_structure.py aktualisieren — vollständige Bäume statt 832-Node-Skeleton
- [ ] Deskriptoren erweitern (structure-Block pro System)
- [ ] Konsistenz-Check: Kit-Struktur vs. Deskriptor element_types vs. geseedete Nodes
- → Backlog: `reference/deep_structure_plan.md` (Ziel-Node-Zahlen pro System)

---

## Phase 2: Content-Pipeline (nach Phase 1)

### S5 — HD E2E-Validierung
- [x] PDF-Upload (VM102 → sys_uploads_raw, sys_sources, sys_ingestion_jobs)
- [ ] extract_text → classify_domain → extract_interpretations → text2kg → synthesize_node
- [ ] Prüfen: canonical_ids matchen auf vollständigen Strukturbaum (aus Phase 1)
- → Voraussetzung: Phase 1 (HD) + Spark GPU-Server
- → Runbook: `reference/s5_runbook.md`

### S6 — Anna's Archive Pipeline
- [x] hd_saas_uploader.py: `--sys-mode`
- [ ] Gate 1: LLM-Vorklassifikation
- [ ] Metadata-Collection + Download + Upload für alle Systeme
- → Kann teilweise parallel zu S5 laufen

### S7 — Cloud-Deployment
- [ ] Cloud-Supabase + Worker auf Spark + E2E-Test

---

## Phase 3: Cross-System + IC-Sprache (nach Phase 2)

> **Hier entsteht die IC-Sprache.** Netze übereinanderlegen → Klumpen finden → eigene Konzepte destillieren.

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
- [ ] System-Chart-Renderer: HD BodyGraph, Astro Wheel, BaZi Pillars, Maya Kin
- [ ] Handbuch-Generator (Tiefe 1–2)
- [ ] 4 App-Spaces: JETZT, KARTE, WERKSTATT, ZEIT
- [ ] WERKSTATT: Brunnen→Leiter Flow-Engine + Anker v1
- [ ] Transit-Service, Konvergenz-Service, Lens-Switcher
- [ ] Onboarding-Flow
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
| 2026-04 | Hybrid TS-first Engine-Architektur (Empfehlung) | TS für HD/BaZi/Maya/triviale in Next.js; Python-Microservice nur für Jyotish+Astro. Kein Spark für Engines. |
| 2026-04 | PyJHora (AGPL) als isolierter Microservice BEHALTEN | Max. K1/K2-Tiefe. Code wird open-sourced, App bleibt privat. VedAstro.Python (MIT) als KP-Ergänzung. |
| 2026-04 | node-jhora ist NICHT open source | Proprietäre "Source Available"-Lizenz mit Royalty. In Vordiskussion fälschlicherweise als OS empfohlen. |
| 2026-04 | K1–K4 Datenkategorien + Evidenzklassen | Aus IC_System_Pruef_Framework.docx integriert. Bestimmt Datenherkunft + Vertrauenswürdigkeit. |
| 2026-04 | Ziwei Doushu (iztro) als neues System | TS-nativ, MIT, 3.5k Stars. Ergänzt BaZi fundamental (Mond- vs. Sonnenkalender). |
| 2026-04 | @yhjs/bazi ersetzt alvamind als primärer BaZi-Kit | MIT, TS, Luck Cycles + Nayin + Ten Gods. Umfangreicher. |
| 2026-04 | CircularNatalHoroscopeJS für Westl. Astro | Unlicense, TS, KEIN Swiss-Eph — eliminiert Lizenzproblem für Basis-Astrologie. |
| 2026-04 | Zwei System-Rollen: calculation + structural | I Ging, Kabbalah, Chakras als reguläre Systeme (nicht hierarchisch). IC-Sprache emergiert aus Konvergenz-Klumpen (Datenschicht E). |
| 2026-03 | **Fresh Clone Makerkit 3.1.3** | hd_saas_app (v2.24) → inner_compass_app (v3.1.3). IC-Eigenarbeit (~2200 Zeilen) portiert/wird neu geschrieben. Engine-Struktur: npm statt Vendoring (TS), Python-Microservice für Jyotish. |
| 2026-03 | **GitHub-Repo: inner-compass-app** | quantensprungai/inner-compass-app (privat). Upstream: makerkit/next-supabase-saas-kit-turbo. Altes Repo hd-saas-app archiviert. |
| 2026-04 | **3 MCP-Server konfiguriert** | Makerkit Kit MCP (lokal, 56 Tools: Schema/DB/Env/Dev), Supabase MCP (Cloud), CLI MCP (optional). Cursor `.cursor/mcp.json` angelegt. KI hat direkten Zugriff auf DB-Schema, Migrations, Env, Dev-Services. |
| 2026-04 | **dturkuler/humandesign_api als HD-Engine** | GPL-3.0 vendored in Docker (SaaS-konform). Ersetzt hdkit+geodetheseeker. Alle 13 Layer + Composite/Transit/BodyGraph. K2-Daten extrahiert (192 Crosses, 8 Awareness Streams, evidence A). |
| 2026-04 | **Gene Keys als eigenständiges System** | GK ist NICHT "HD mit anderer Sprache". Shared K1 (Ephemeris), eigenes K2 (Shadow/Gift/Siddhi, Codon Rings, Sequences). Im KG: `gk.*` Prefix, Cross-Link über `hd.gate.N ←→ gk.gate.N`. |
| 2026-04 | **HD-Schulen als Tradition-Tag** | Jovian Archive, Quantum HD, 64Keys, Parkyn teilen K1+K2. Unterschiede nur in K3/K4 (Interpretation). Modelliert als `tradition`-Tag auf Interpretation-Nodes, nicht als separate Systeme. |
