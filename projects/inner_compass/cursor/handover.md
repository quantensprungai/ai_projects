# Inner Compass — Handover

> Copy-Paste diesen Block am Anfang eines neuen Chat-Fensters (Cursor oder Claude).

---

## Kontext-Block (kopieren)

```
Projekt: Inner Compass — geburtsbasiertes Meta-System (11 Quellsysteme + Basisstrukturen → 3-Schichten-KG → personalisiertes Handbuch)
Tech: Next.js (Makerkit 3.1.3) + Supabase + Spark (GPU, Worker, MinerU, LLM)

Gesamtprozess (5 Phasen):
  Phase 0: Fundament          ████████████ 100%  (Schema, Worker, 832-Node-Seed)
  Phase 1: Engine Eval+Integ. ██░░░░░░░░░░  10%  ← NÄCHSTER SCHRITT (Setup ok, erster Spike)
  Phase 2: Content-Pipeline   ░░░░░░░░░░░░   0%  (blockiert durch Phase 1)
  Phase 3: Cross-System       ░░░░░░░░░░░░   0%
  Phase 4: App                ██░░░░░░░░░░  15%  (Architektur+Scope dokumentiert)

Phase 1 = Engine Evaluation Sprint:
  - Pro System: Spike → Bewerten → Integrieren → Strukturbaum extrahieren
  - Kits: packages/engines/{hd,ziwei,bazi,astro,maya,jyotish}/
  - NEU: Ziwei Doushu (iztro, MIT, TS-nativ, 3.5k Stars) als chinesisches Hauptsystem
  - NEU: @yhjs/bazi (MIT, TS) ersetzt alvamind (Luck Cycles + Nayin)
  - NEU: CircularNatalHoroscopeJS (Unlicense, TS, kein Swiss-Eph)
  - Jyotish: PyJHora (AGPL) als isolierter Microservice BEHALTEN (max. K1/K2-Tiefe)
  - Architektur: Hybrid TS-first (TS in Next.js + Python-Microservice NUR für Jyotish)
  - Kein Spark für Engines (Spark = nur GPU: MinerU, LLM)
  - K1–K4 Framework: K1+K2 aus Kits (~40%), K3+K4 aus Literatur-PDFs (~60%)
  - Evidenzklassen: A (math. sicher) → D (hypothetisch)
  - Zwei System-Rollen: 'calculation' (Engines) + 'structural' (I Ging, Kabbalah, Chakras)
  - IC-Sprache entsteht aus Konvergenz-Klumpen (Datenschicht E / Meta-Knoten)
  - Spike-Reihenfolge (aktuell): Ziwei → BaZi → HD → Astro → Maya → Jyotish
  - Ziel: Engines sauber integriert + vollständige Strukturbäume statt 832er-Skeleton

Dokumenten-Landkarte:
  Philosophisch:  consolidation/z1 (Gesamtwerk v0.5), z3 (Modelle v0.4), Glossar v1.2
  Produktplanung: consolidation/z2 (User-Journey v0.1, veraltet), ic_gesamtinventur.md (Inventur+Scope)
  Technisch:      cursor/{architecture, pipeline, contracts, engines, status}.md (= "Z4")
  
Lies zuerst: projects/inner_compass/cursor/status.md
Dann je nach Aufgabe:
- Engine-Integration (Phase 1 wiederholbar): reference/engine_integration_playbook.md + cursor/engines.md + packages/engines/ im Code-Repo
- Schema/DB: cursor/architecture.md + cursor/contracts.md
- Pipeline/Worker: cursor/pipeline.md
- App-Architektur: cursor/architecture.md §12–14 (User-Schema, Services, 4 Spaces)
- Scope/Inventur: consolidation/ic_gesamtinventur.md (v0.5, §XX Scope, §XXI Delta)
- Philosophie/Modelle: consolidation/z1_gesamtwerk.md + z3_modell_referenz.md

Kernzahlen: 15 Dimensionen, 12 Lebensbereiche (erweitert von 10, März 2026), 5 Datenschichten, 11 Berechnungs- + 3 Struktursysteme, 4 App-Spaces.
Schema: sys_* Tabellen (11) + user_* Tabellen (6 designed), Postgres+pgvector, jsonb Payloads.
Code-Repo: code/inner_compass_app/ (Makerkit 3.1.3, frischer Clone 2026-03-31)

MCP-Tools (KI nutzt diese automatisch):
  Makerkit Kit MCP: packages/mcp-server/ → Schema, Migrations, DB-Ops, Env, Dev, Translations
  Supabase MCP:     Cursor Plugin → Cloud-DB, Management API, SQL-Queries
  CLI MCP:          npx @makerkit/cli → Plugin-Install, Upstream-Updates (optional)
  Config:           .cursor/mcp.json (Workspace-Root)
```

---

## Wenn der Chat über ENGINES geht

```
Zusätzlich lesen:
- cursor/engines.md (K1-K4 Framework, Kit-Kandidaten mit Lizenzen, Prüf-Checkliste, Architektur)
- code/inner_compass_app/packages/engines/README.md (TS-Engines, npm-basiert)
- code/inner_compass_app/services/jyotish/README.md (Python-Microservice, AGPL-isoliert)
- kern/IC_System_Pruef_Framework.docx (Originalquelle K1-K4 + Evidenzklassen)
- reference/hd_kit_structure_extraction.md (HD-Kit-Analyse, was fehlt)
- reference/structure_descriptor_seed.md (Deskriptor vs. Seed vs. Structure Klarstellung)

Wichtige Entscheidungen:
- PyJHora (AGPL): BEHALTEN als isolierter Microservice (Code open-sourced, App privat)
- Ziwei Doushu: iztro (MIT, TS) — größter Kit-Fund
- BaZi: @yhjs/bazi (MIT, TS) ersetzt alvamind
- Westl. Astro: CircularNatalHoroscopeJS (Unlicense, kein Swiss-Eph-Problem)
- node-jhora: PROPRIETÄR, NICHT nutzbar (trotz GitHub)
- IC-Sprache: emergiert aus Konvergenz-Klumpen im KG, NICHT vorausgesetzte Hierarchie (architecture.md §15)
```

## Wenn der Chat über ARCHITEKTUR geht

```
Zusätzlich lesen:
- cursor/architecture.md (Schema, Datenschichten, Tech Stack, §12-14 NEU, §15 KG-Übereinanderlegen & IC-Sprache NEU)
- cursor/contracts.md (Dimensions-Contract, Payloads, Enums, §10-12 NEU)
- reference/structure_descriptor_seed.md (Deskriptor vs. Seed vs. Structure)
```

## Wenn der Chat über PIPELINE geht

```
Zusätzlich lesen:
- cursor/pipeline.md (Jobs, Flows, Prompts, §10-12 NEU)
- Worker-Specs in cursor/pipeline.md §7
- Infra: infrastructure/spark/ (MinerU, LLM-Serving)
```

## Wenn der Chat über PRODUKT/DESIGN geht

```
Zusätzlich lesen:
- consolidation/ic_gesamtinventur.md (Gesamtinventur + Scope v1/v2/v3)
- consolidation/z2_user_journey.md (User-Journey, ACHTUNG: v0.1, App-Spaces fehlen noch)
- reference/prd_v3.md (vollständiges PRD)
- reference/decisions.md (alle Design-Entscheidungen)
```

## Wenn der Chat über DB/SCHEMA geht

```
MCP-Tools nutzen (automatisch verfügbar in Cursor):
- Makerkit Kit MCP: get_schema_files, get_database_summary, get_table_info, create_migration, diff_migrations
- Supabase MCP: Direkte SQL-Queries gegen Cloud-DB
- Voraussetzung für lokale DB-Tools: supabase start (Port 54322)

Zusätzlich lesen:
- cursor/architecture.md (Schema, sys_*-Tabellen, Datenschichten)
- cursor/contracts.md (Enums, Dimensions, Payloads)
- code/inner_compass_app/apps/web/supabase/schemas/ (deklarative Schema-Dateien)
```

---

## Neuer Chat — nur Aufgabe (kopieren)

Wenn du einen **frischen Chat** nur für die nächste konkrete Aufgabe willst, oben den **Kontext-Block** einfügen und darunter z. B.:

```
Aufgabe: Phase 1 — erster Engine-Spike (Ziwei / iztro)

Kontext: Lokal entwickeln, Supabase MCP erst bei Cloud. Makerkit MCP: MAKERKIT_PROJECT_ROOT in .cursor/mcp.json.

Bitte:
1. pnpm --filter @ic/engines add iztro (oder workspace-konform)
2. Minimal-Script oder kleines Test: feste Geburtsdaten → Chart-Output
3. Kurz dokumentieren: welche Felder = K1 (Zahlen), welche = K2 (Struktur), JSON-Snippet

Referenz: projects/inner_compass/cursor/status.md §Phase 1, cursor/engines.md
Code: code/inner_compass_app/
```
