# Inner Compass — Handover

> Copy-Paste diesen Block am Anfang eines neuen Chat-Fensters (Cursor oder Claude).

---

## Kontext-Block (kopieren)

```
Projekt: Inner Compass — geburtsbasiertes Meta-System (11 Quellsysteme + Basisstrukturen → 3-Schichten-KG → personalisiertes Handbuch)
Tech: Next.js (Makerkit 3.1.3) + Supabase + Spark (GPU, Worker, MinerU, LLM)

Gesamtprozess (5 Phasen):
  Phase 0: Fundament          ████████████ 100%  (Schema sys_*, Worker, Minimal-K2-Seed ~832 Nodes)
  Phase 1: Engine Eval+Integ. ███████████░  ~95%  (Chart-Engines + Kataloge v0; Seed↔Structure-Sync offen)
  Phase 2: Content-Pipeline   ██████░░░░░░  ~50%  (S5a E2E ✅ · S5b ✅ 64/64 Gates)
  Phase 3: Cross-System       ░░░░░░░░░░░░   0%
  Phase 4: App                ██░░░░░░░░░░  15%  (Architektur+Scope dokumentiert)

ROTER FADEN (Masterplan — wo wir im Prozess stehen, Stand 2026-07-03 ~22:40):
  1. ✅ S5a E2E-TEST done · ✅ **S5b** Complete Rave I'Ching (65 Chunks, 64 Gates, 64/64 Synthesis)
  2. ⏳ SYSTEM-WELLEN (je System: Seed aus system_structure/* → PDFs → Pipeline → QA):
     HD zuerst (läuft), dann Gene Keys → Astro → BaZi → Maya → … (decisions.md Wellen-Reihenfolge)
  3. ⏳ PHASE 3 CROSS-SYSTEM — ERST nach Entscheidung zu ZWEI offenen Reviews:
     a) reference/cross_system_mapping_methodology_review.md (Embedding-Methodik)
     b) reference/gesamtbetrachtung_review_2026-07.md (Genealogie-Gewichtung, contradicts-Pipeline)
  4. ⏳ MVP "Die Vier Spiegel" (Phase 4): Onboarding + Mandala + Handbuch T1–2 + Share
     → UX-Design: reference/ux_konzept_2026-07.md (v1 vorhanden, vor Umsetzung reviewen)
  5. ⏳ VOLL: WERKSTATT + ZEIT komplett + Staffel 2–3 + Resonanz-Feedback-Loop
  Aktueller Punkt: **Schritt 2 (HD-System-Welle)** — S6 *Life Force — The Channels* ✅ **36/36** (2026-07-08). Nächstes: **S5d BaZi**. Learnings: `cursor/reference/s6_pipeline_learnings.md`
  → cursor/status.md ist die Live-Wahrheit; diesen Block bei Meilensteinen aktualisieren.

Phase 1 = Engine Evaluation Sprint:
  - Pro System: Spike → Bewerten → Integrieren → Strukturbaum extrahieren
  - Kits: packages/engines/{hd,ziwei,bazi,astro,maya,jyotish}/
  - NEU: Ziwei Doushu (iztro, MIT, TS-nativ, 3.5k Stars) als chinesisches Hauptsystem
  - NEU: @yhjs/bazi (MIT, TS) ersetzt alvamind (Luck Cycles + Nayin)
  - NEU: Westl. Astro: **celestine** (MIT, TS in `packages/engines`)
  - Jyotish: PyJHora (AGPL) als isolierter Microservice BEHALTEN (max. K1/K2-Tiefe)
  - Architektur: Hybrid TS-first (TS in Next.js + Python-Microservices für HD + Jyotish)
  - Kein Spark für Engines (Spark = nur GPU: MinerU, LLM)
  - K1–K4 Framework: K1+K2 aus Kits (~40%), K3+K4 aus Literatur-PDFs (~60%)
  - Evidenzklassen: A (math. sicher) → D (hypothetisch)
  - Zwei System-Rollen: 'calculation' (Engines) + 'structural' (I Ging, Kabbalah, Chakras)
  - IC-Sprache entsteht aus Konvergenz-Klumpen (Datenschicht E / Meta-Knoten)
  - Staffel Phase 1 (Ist): Ziwei → BaZi → Jyotish → HD → Astro → Maya Tzolkin (**v1** + Step 3) → Nine Star Ki (**v1** + Step 3) → Numerologie → Akan (Engines + API-Routen + v0-Kataloge)
  - Ziel Phase 1 (offen): ~~Seed aus system_structure/* statt hardcoded Skeleton; HD zuerst (PHS + Crosses + Variables)~~ ✅ HD-JSON-Seed 2026-07-02; andere Systeme noch offen
  - HD: Swiss Ephemeris (pyswisseph) im Python-Service aktiv = **tropical Standard**. Sidereal/Hybrid = contracts §13 + Roadmap-Doku, **Implementierung optional**.

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

## Human Design — Rechenmodi (tropical / sidereal / hybrid)

```
Kurz:
- system_id bleibt immer `hd` — Unterschiede stecken in compute_profile.hd (cursor/contracts.md §13).
- Swiss Ephemeris ist im HD-Service SCHON angebunden (pyswisseph im vendored dturkuler); Standardmodus = tropical (Jovian-kompatibel).
- Sidereal-Flag + Ayanamsha sowie Hybrid (Design tropisch / Persönlichkeit sidereal) sind SPEC + Roadmap, NICHT implementiert.
  → reference/hd_compute_profiles_kg_and_roadmap.md · decisions.md 2026-05-06

Wenn ihr das BAUEN wollt — Startreihenfolge:
1) Governance: Default-Ayanamsha (wenn sidereal), Verhalten des Design-Datums (−88°) bei full sidereal festlegen.
2) API: BirthData + compute_profile.hd in services/hd (FastAPI) und @ic/engines hd-client-Typen spiegeln.
3) Engine: vendored humandesign_api …/core.py — calc_ut mit Sidereal-Mode parametrisieren ODER zwei Läufe + Merge (Hybrid).
4) Tests: feste Geburtszeit → erwartete Gates (Regression gegen Jovian tropical bleibt Pflicht-Fixture).
5) App: Chart-Snapshot persistiert compute_profile; UI-Label; keine stillen Cross-Modus-Vergleiche.
```

## Wenn der Chat über ENGINES geht

```
Zusätzlich lesen:
- cursor/engines.md (K1-K4 Framework, Kit-Kandidaten mit Lizenzen, Prüf-Checkliste, Architektur)
- code/inner_compass_app/packages/engines/README.md (TS-Engines, npm-basiert)
- code/inner_compass_app/services/jyotish/README.md (Python-Microservice, AGPL-isoliert)
- kern/IC_System_Pruef_Framework.docx (Originalquelle K1-K4 + Evidenzklassen)
- reference/hd_kit_structure_extraction.md (HD-Kit-Analyse, was fehlt)
- **EarthStar Human Design** = IC-Produktname für Hybrid (`hybrid_design_tropical_personality_sidereal`); UI-Spez Stufe 1/2 → `reference/hd_compute_profiles_kg_and_roadmap.md` §6.1
- reference/structure_descriptor_seed.md (Deskriptor vs. Seed vs. Structure Klarstellung)
- cursor/contracts.md §13 (compute_profile für hd)

Wichtige Entscheidungen:
- PyJHora (AGPL): BEHALTEN als isolierter Microservice (Code open-sourced, App privat)
- Ziwei Doushu: iztro (MIT, TS) — größter Kit-Fund
- BaZi: @yhjs/bazi (MIT, TS) ersetzt alvamind
- Westl. Astro: **celestine** (MIT, in `@ic/engines`)
- node-jhora: PROPRIETÄR, NICHT nutzbar (trotz GitHub)
- IC-Sprache: emergiert aus Konvergenz-Klumpen im KG, NICHT vorausgesetzte Hierarchie (architecture.md §15)
```

## Wenn der Chat über ARCHITEKTUR geht

```
Zusätzlich lesen:
- cursor/architecture.md (Schema, Datenschichten, Tech Stack, §12-14 NEU, §15 KG-Übereinanderlegen & IC-Sprache NEU)
- cursor/contracts.md (Dimensions-Contract, Payloads, Enums, §10-13 NEU)
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
- reference/gesamtbetrachtung_review_2026-07.md (Konzept-Review: Genealogie-Gap, Phasen-Detection,
  Resonanz-Feedback-Loop, Content-Ökonomie, UX-Empfehlungen — offener Review)
- reference/ux_konzept_2026-07.md (UX-Deep-Dive v1: IA, Onboarding, Mandala, WERKSTATT-Ritual,
  Konvergenz-UX, Freemium, MVP-Schnitt)
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

## S5 E2E — VM105 (Stand 2026-07-02)

> **Ziel:** 1 HD-PDF → Supabase Upload → Spark Worker → Chunks → Interpretationen → text2kg → synthesize_node.  
> **Nicht:** alle 216 Literatur-Dateien — nur **1 Test-PDF**.

### Session-Stand 2026-07-03 (S5b ✅)

| Item | Wert |
|------|------|
| Account | `5deaa894-2094-4da3-b4fd-1fada0809d1c` |
| Source (S5-PDF) | `3c7c0a7b-9dd1-41b1-ac47-c0cd26dedbe5` — *Complete Rave I'Ching* |
| **S5a Pipeline E2E** | ✅ **done** (2026-07-02) |
| **S5b Extract** | ✅ 65 Chunks, 64 unique `gate_number` (MinerU pipeline, `IC_CHUNK_PROFILE=rave_iching_gates`) |
| **S5b Phase 2** | ✅ classify, term_mapping, interpretations, text2kg, synthesize |
| **S5b Synthesis** | ✅ **64/64** echte Gate-Wortings (Gate 63 via `only_canonical_ids` + JSON-Fix) |
| Chunk-Profil | `ic_chunk_profiles.py` → `rave_iching_gates` (Code-Repo + Spark) |
| Spark Worker-Start | `spark_s5b_synth.sh` (pkill + `set -a` `.env.vm105`) — **immer** VM105-URL exportieren |
| Spark LLM | `qwen3-32b-nvfp4` :30001 · `IC_LLM_SYNTHESIS_TIMEOUT=300` |
| Supabase VM105 | `http://100.70.238.41:54321` (Tailscale) · Key via `pnpm exec supabase status` |

**Skripte:** `ic_s5b_rerun.py` · `ic_s5b_gate63_synthesis.py` · `ic_s5_spark_synthesis_prep.py` · `spark_s5b_extract.sh` · `spark_s5b_synth.sh`

**Verify:**

```sql
select count(*) filter (where not canonical_description like '[DRY-RUN]%') as real,
       count(*) filter (where canonical_description like '[DRY-RUN]%') as stub
from sys_synthesis_wordings
where account_id = '5deaa894-2094-4da3-b4fd-1fada0809d1c'
  and canonical_id like 'hd.gate.%';
-- Ziel: real=64, stub=0
```

### Session-Stand 2026-07-02 (S5a, historisch)

| Item | Wert |
|------|------|
| **S5a Pipeline E2E** | ✅ **done** (2026-07-02): text2kg, synthesize 47/47 echt, Job completed |
| **S5b Chunk 64/64** | ~~offen~~ → ✅ erledigt 2026-07-03 |

**Spark synthesize (Copy-Paste):**

```bash
ssh -p 2222 sparkuser@100.96.115.1
cd ~/srv/hd-worker
export SUPABASE_URL=http://100.70.238.41:54321
export SUPABASE_SERVICE_ROLE_KEY=<von VM105 supabase status>
export IC_LLM_URL=http://127.0.0.1:30001
export IC_LLM_MODEL=qwen3-32b-nvfp4
export IC_LLM_SYNTHESIS_TIMEOUT=300
export IC_WORKER_JOB_TYPES=synthesize_node
.venv/bin/python -u ic_worker.py --once   # oder --loop --sleep 5
tail -f logs/s5_synthesize.log
```

**Erfolg:** 47/47 Gate-Wortings **ohne** `[DRY-RUN]`-Prefix; Job `completed`.

---
### Repo & Branch

| | |
|---|---|
| Docs | `C:\Users\Admin105\ai_projects` *(Unterstrich, nicht `ai-projects`)* |
| Code | `C:\Users\Admin105\ai_projects\code\inner_compass_app` |
| Branch | `cursor/inner-compass-alignment-reconcile-spark-handover` |
| Stand | `d59faee` — Literatur-CSVs 2026-06-30, Ra-Katalog, Cross-System-Methodik |

```powershell
cd C:\Users\Admin105\ai_projects
git fetch; git checkout cursor/inner-compass-alignment-reconcile-spark-handover; git pull
```

### Kontext

- Phase 1 Engines ~95 % · Phase 2 Pipeline **0 %** — **S5 = nächster Meilenstein**
- Literatur-SoT: he5013/Nextcloud (216 Dateien); VM105 Teilbestand unter `Downloads\Literatur`
- MinerU-Spike abgeschlossen (MinerU > Unlimited-OCR); Worker-Env: **`IC_USE_MINERU=true`**
- Test-PDF: `Downloads\Literatur\hd\` — *Complete Rave I'Ching* (MD5 `9daaa92…` in `hd/`, nicht `archiv/`)
- MinerU-Referenz: `reference/mineru_complete_rave_iching_20p_result.md`
- Spark hat bereits `~/sample_complete_rave_iching.pdf` (OCR-Spike)

### Doku

- `reference/s5_runbook.md` — Haupt-Runbook
- `cursor/pipeline.md` — Job-Kette
- `infrastructure/spark/HD_WORKER_HANDOVER.md` — Spark/MinerU (`sys_*`, nicht `hd_*`)
- `reference/aa_ic_toolkit_alignment.md` — Uploader `--sys-mode`

### Topologie

| Komponente | Host | Tailscale |
|---|---|---|
| Supabase lokal | VM105 | `100.70.238.41` |
| Worker + MinerU | Spark `spark-56d0` | `100.96.115.1` |
| AA-Downloads | VM102 | — |

**Worker auf Spark:** `SUPABASE_URL=http://100.70.238.41:54321` (nicht `localhost`).

### Schritte A–C (Phase 1 nur MinerU)

**A) VM105 — Supabase**

```powershell
cd C:\Users\Admin105\ai_projects\code\inner_compass_app
pnpm run supabase:web:start
# ggf. pnpm exec supabase start --ignore-health-check
# Optional Seed: cd apps\web; python scripts\ic_seed_structure.py
```

**B) VM105 — PDF + Job**

Uploader (Toolkit + `.env` mit `SERVICE_ROLE_KEY`, `ACCOUNT_ID=5deaa894-…`):

```powershell
python src/hd_saas_uploader.py --upload-pdfs "C:\Users\Admin105\Downloads\Literatur\hd\<Complete_Rave>.pdf" --max-pdfs 1 --sys-mode
```

Oder Studio + SQL laut `s5_runbook.md` Option B.

**C) Spark — nur `extract_text`**

```bash
# SGLang stoppen; dann:
export SUPABASE_URL="http://100.70.238.41:54321"
export SUPABASE_SERVICE_ROLE_KEY="<supabase status auf VM105>"
export IC_USE_MINERU=true
export IC_MINERU_LANG=latin
export IC_WORKER_JOB_TYPES=extract_text
~/srv/hd-worker/.venv/bin/python3 ~/ai_projects/code/inner_compass_app/apps/web/scripts/ic_worker.py --loop --sleep 5
```

(Pfad Worker/venv auf Spark ggf. anpassen — siehe `HD_WORKER_HANDOVER.md`.)

### Validierung

```sql
select count(*) from sys_source_chunks where source_id = '<SOURCE_ID>';
select status, job_type, debug from sys_ingestion_jobs order by created_at desc limit 5;
```

**Erfolg Phase 1:** `sys_source_chunks > 0`, sinnvolle Gate-Texte, kein leerer OCR-Fallback.

### Phase 2 — LLM + text2kg (Stand 2026-07-01)

**Voraussetzung:** Seed gelaufen (`python scripts/ic_seed_structure.py`) — sonst legt text2kg asset_chunk-Nodes an.

| Schritt | Env / Aktion |
|---------|----------------|
| Chunk-Profil | `IC_CHUNK_PROFILE=rave_iching_gates` (Gate-Chunks mit `gate_number` in Metadata) |
| LLM-Phase | `IC_WORKER_JOB_TYPES` ohne Filter; `IC_LLM_URL` auf Spark |
| text2kg | Linkt Interpretationen → `hd.gate.{N}` via Chunk-Metadata (nicht asset_chunk) |
| synthesize | Priorisiert Nodes **mit** `interpretation_ids`; Timeout: **`IC_LLM_SYNTHESIS_TIMEOUT`** (Default 240s) |

**Verifikation nach Phase 2:**

```sql
-- Keine asset_chunk-Nodes für Gates (sollte 0 sein wenn Seed + Fix aktiv)
select node_key from sys_kg_nodes
where system = 'hd' and node_key like 'hd.asset_chunk.%' limit 5;

-- Gate-Nodes mit Interpretationen
select node_key, metadata->'interpretation_ids' as interps
from sys_kg_nodes
where node_key like 'hd.gate.%' and metadata ? 'interpretation_ids'
limit 5;
```

**S5-Ablauf (empfohlen):**

1. **Testlauf** — 1 PDF, Pipeline E2E (Phase 1 Chunking + Phase 2 LLM/text2kg)
2. **Verifikation** — SQL oben; Stichprobe Gate 1/7
3. **DB-Cleanup** — Test-Artefakte löschen (`hd.asset_chunk.*`, Duplikat-Jobs, alte Interpretationen des Test-Source); **Seed-Nodes behalten** oder Seed neu
4. **Sauberer Lauf** — optional `supabase db reset` + Seed + Pipeline nochmal (nach Seed-Erweiterung sinnvoll)

Nicht „alles wegwerfen“: Schema + Katalog-JSONs + Code bleiben; nur **account-spezifische Ingest-Daten** aus dem Test.

### DB-Naming (sys_* vs. hd.*)

| Ebene | Alt (HD-App) | Jetzt (Inner Compass) |
|-------|--------------|------------------------|
| Tabellen | `hd_kg_*`, `hd_*` | **`sys_*`** (`sys_kg_nodes`, `sys_interpretations`, …) |
| Helper-Schema | `hd` | **`ic`** |
| System-Spalte | — | `system = 'hd'` \| `'bazi'` \| … (Quellsystem, nicht Tabellenname) |
| Canonical ID | — | **`hd.gate.34`** — `hd.` = Namespace des Quellsystems, **nicht** Tabellenpräfix |

Legacy-Pfad `code/hd_saas_app/` existiert parallel; **aktive Pipeline:** `code/inner_compass_app/`.

### 69.120 Kombinationen — vollständig ohne 69k Nodes?

**Nein.** 64 Gates × 6 Lines × 6 Colors × 6 Tones × 5 Bases ≈ **69.120** berechenbare Positionen pro Aktivierung — das sind **Chart-Ergebnisse** (K1), keine Struktur-Nodes.

**Strukturbaum (K2)** enthält **atomare** Bedeutungs-Nodes (~700–780 für HD):
- 64 Gates, 384 Lines (gate-spezifisch im Seed), 36 Channels, 9 Centers, …
- **17 PHS-Nodes** (6 Color + 6 Tone + 5 Base — global, nicht pro Gate)
- 192 Incarnation Crosses, 4 Variables, …

Kombinationen entstehen zur **Laufzeit**: Engine liefert Position → App/LLM kombiniert Bedeutungen der atomaren Nodes. Details: `reference/hd_structure_13_layers_and_engines.md`, `reference/deep_structure_plan.md` §PHS.

**Vollständig für K2** = alle 13 Layer als atomare Nodes geseedet — **nicht** 69k Einzel-Nodes. **Stand 2026-07-02:** PHS (17), Variables (4), Crosses (192), Strategy/NotSelf/Signature + Catalog-Circuits aus JSON geseedet; Layer 1–4 + 9 + 13 abgedeckt.

### K1/K2 vs. K4 (Kurz)

- **K1/K2:** Struktur/Seed aus Engines + `ic_seed_structure.py` — Graph **vor** PDFs.
- **K4:** PDF-Text → `sys_interpretations` → text2kg **PATCH** auf Seed-Nodes.
- **Wellen-Modell:** Struktur **pro System** seeden (HD zuerst), nicht alle 14 gleichzeitig.
- **gate_number → hd.gate.N:** HD-first in `_resolve_canonical_id_from_interp`, erweiterbar für andere Systeme via Chunk-Metadata.
- **Cross-System:** Synthese für UI; Roh-Interpretationen für Phase 3 — Review `reference/cross_system_mapping*.md`.

### Seed-Verifikation HD (2026-07-02)

| Check | Ergebnis |
|-------|----------|
| 64 Gates `hd.gate.1`–`64` vs. `hd_catalog_v0.json` | ✅ PASS |
| Center-Zuordnung Seed vs. Katalog | ✅ PASS (0 Mismatches) |
| 36 Channels | ✅ PASS |
| 17 PHS (`hd.color.1`–`6`, `hd.tone.1`–`6`, `hd.base.1`–`5`) | ✅ PASS — aus `hd_catalog_v0.json` |
| 4 Variables (`hd.variable.digestion` … `perspective`) | ✅ PASS |
| 192 Incarnation Crosses (`hd.incarnation_cross.*`) | ✅ PASS — aus `hd_crosses_extracted.json` |
| Type→Strategy/NotSelf/Signature + Channel→Circuit | ✅ PASS — 115 Edges aus `hd_structure_v0.json` |
| Offene Gaps vs. Katalog/Structure | ⚠️ Awareness Streams (8), Cross→Gate-Edges, PHS-Hierarchie (Line→Color→Tone→Base), Legacy-Circuit-Keys (`individual`/`tribal`/`collective` vs. Katalog-Subcircuits) |

### Rückmeldung an he5013

Upload-Methode · Chunk-Count · 1–2 Textbeispiele · Job-`debug` bei Fehler · ob Phase 2 (LLM) starten.

---

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
