---
last_update: 2026-04-28
status: draft
scope:
  summary: "End-to-End: pro system_id Literatur recherchieren, AA (50/Tag) beschaffen, Metadaten + PDF-Brücke nach IC (sys_*)."
  in_scope:
    - hd vs ic naming cleanup strategy
    - per-system research anchors (descriptors, entity registries, K3/K4)
    - aa output paths and daily download coupling
    - bridge sys_sources metadata and uploader
    - system_id coverage matrix (descriptor vs catalog vs registry vs aa profile)
    - aa completeness gaps and reconciliation (see literature_aa_coverage_gaps.md)
    - runbook hd_content VM102 refresh from entity_registry_hd_v02
    - target acquisition mode work_queue vs discovery (registry known_works as loop unit; same idea for hd/astro/jyotish/bazi/ziwei)
  out_of_scope:
    - illegal acquisition
    - chart engine tuning
notes:
  - "AA-Profilordner heißen historisch hd_content etc.; Umbenennung optional und breaking-sensitiv."
---

# Literaturbeschaffung: IC ↔ Anna’s Archive — ein durchgängiger Prozess

## 1. HD benennen vs. IC — Aufräumen ohne Chaos

**Problem:** Namen wie `hd_saas_uploader.py`, `.env.hd_saas`, Profil `hd_content` wecken **Legacy-HD-SaaS** — verwirrend, solange IC **`sys_*`** nutzt.

**Realistische Strategie (phasenweise):**

| Maßnahme | Risiko | Empfehlung |
|----------|--------|------------|
| **Immer `--sys-mode`** bei jedem PDF-Upload nach Supabase | gering | **Pflicht** für IC; verhindert fälschlich `hd_*`-Tabellen. |
| **Doku/Env:** `.env.ic` parallel zu `.env.hd_saas` (gleiche Keys), Runbooks nur noch `.env.ic` nennen | gering | **schnell umsetzbar** |
| **Skript:** `ic_supabase_uploader.py` als Kopie/Wrapper von `hd_saas_uploader.py` | mittel | optional, wenn alle Aufrufer angepasst |
| **AA-Profilordner `projects/hd_content` → z. B. `ic_hd_content`** | **hoch** (Skripte, `AAT_CONFIG`, Pfade auf VM102) | **erst** wenn ihr bewusst migriert |

**Kurz:** IC entsteht **nicht** durch Umbenennen von Ordnern, sondern durch **DB/Worker (`sys_*`)** und **Disziplin beim Upload**. Umbenennungen sind **Kosmetik + Risiko** — priorisiert **Betrieb** (`--sys-mode`), dann **Doku/Env**, dann optional Code/Ordner.

---

## 2. Ist von IC-Seite klar, *wie* pro System recherchiert wird?

**Teilweise ja — die Anker liegen da, ein einziges „Klick“-Runbook pro System noch nicht.**

**Pro `system_id` sollt ihr immer dieselben drei Ebenen öffnen:**

1. **Struktur (kein PDF):** `projects/inner_compass/system_descriptors/<system>.json` — was das System *überhaupt* enthält (Elemente, IDs).
2. **Literatur-Inventar (entity-first):** `projects/inner_compass/reference/entity_registry_*_v01.json` (und `entity_registry_hd_v02.json`), **falls vorhanden**. Dort steht oft schon: Schulen, Kategorien **K3 vs K4**, `target_path` ins AA-Toolkit (z. B. `code/annas-archive-toolkit/projects/bazi_content/entity_registry.json`).
3. **Was Literatur leisten muss:** `projects/inner_compass/cursor/engines.md` (K3 Regeln vs K4 Bedeutungen) und `pipeline.md` (welche Jobs nach Upload laufen).

**Wo es noch Lücken gibt:** Systeme **ohne** `entity_registry_*` → dort zuerst ein **kuratiertes Inventar** (eure „~50 Quellen“-Tabelle / separater Literatur-Agent) anlegen, dann optional Registry nachziehen.

**Konkreter Recherche-Output (pro Quelle), bevor ihr downloadet:**

- `system_id` (und ggf. `subsystem` / Schule aus Registry-Schema)
- Autor, Titel, Jahr, Sprache
- **Rechtsstatus** (eigenes PDF / OA / gekauft / Bibliothek)
- **K3/K4-Priorität** (Regelwerk vs Deutung)
- **MinerU-Tauglichkeit** (Scan vs digital-born)
- Identifikatoren: ISBN / MD5 aus AA-Metadaten, Suchbegriff für Mirror
- Optional: `curriculum_row_id` oder Ticket-ID für Nachverfolgung

Das ist genau das **Lieferobjekt** aus dem **Literatur-Prompt** (Curriculum-Tabelle) — technisch noch **nicht** alles in der DB, aber **methodisch** die SoT für „was wir brauchen“.

### 2.1 Work-Queue vs. Discovery — was sinnvoller ist (und was umgesetzt werden muss)

**Ist-Zustand (Toolkit):** `simple_collector.py` nutzt `extract_search_queries()` → eine **Liste von Suchstrings** (z. B. HD: Dutzende Cluster). Das ist **Discovery** (AA breit durchkämmen). Passt zur **Grüne-Wiese-Idee nur bedingt**, weil die kanonische Liste **`known_works`** in der Registry **nicht** 1:1 die Schleife ist — deshalb viel Rauschen und schwache automatische Zuordnung.

**Soll-Zustand (verbindlich für alle Systeme mit `entity_registry_*`):** **Work-Queue** = äußere Schleife über **`known_works`** (optional gefiltert: `priority`, `anna_archive_likely`, Sprache). Pro Werk: **eine bis wenige enge Queries** (`anna_archive_search_queries` am Werk oder Fallback „Autor + Titel“), Ergebnisse werden **dem `curriculum_id` dieses Werks** zugeordnet (Log/CSV). **Discovery-Batch** (heutige flache Query-Liste) bleibt **optional** für Lücken und Erkundung — nicht als Primärweg für HD/Ra-Kanon.

**Systemübergreifend:** Astro, Jyotish, BaZi, ZiWei haben dieselbe Registry-Struktur (`authors`, `known_works`, Schul-Tags) — **derselbe Prozess**, andere Sprachen/Schul-Rausch-Profile. HD ist nur **am ausführlichsten** inventarisiert.

**Umsetzung (sinnvolle Reihenfolge):**

1. **Doku (dieser Abschnitt)** — gemeinsames Zielbild; kein neues Parallel-Dok nötig.
2. **Toolkit (Pilot):** `code/annas-archive-toolkit/scripts/collect_metadata_work_queue.py` — Schleife über **`known_works`**, pro Werk enge Query(s), Ausgabe **`work_acquisition_log.csv`** + `work_queue_summary.json` unter `output/<profil>/work_queue/`. Aufruf wie `simple_collector` mit **`AAT_CONFIG`** (Profil-JSON). Optionen: `--max-works N`, `--only-priority high`, `--resume`, `--skip-unlikely`, **`--aa-search-order`** (Standard **`free_text_first`**: Freitext-`q=` vor `lgrsnf_topic:` — weniger Überschneidung zwischen Zielwerken).
3. **Queue/Download:** `export_assets` / `build_acquire_queue` an **Werk-IDs** anbinden oder Mapping-Tabelle pflegen.
4. **Reconciliation:** heuristische CSV-Abgleiche nur noch **unterstützend**, nicht als SoT für „gefunden“.

---

## 3. „50 Downloads pro Tag“ — passt das zur Recherche?

**Ja, als *technisches* Tempo — nein als *alleinige* Qualitätsstrategie.**

- **50/Tag** = Limit der **Fast-Download-Pipeline** auf VM102 (`check_daily_limit.py`, `fast_download_acquire.py`, Runbooks unter `projects/annas_archive_toolkit/`).
- **Qualität** kommt aus **Schicht A** (Kuratierung): Topics, Relevanz-Score, `entity_registry`, rechtlich saubere Liste.

**Sinnvoller Ablauf:**

1. **Kuratieren** (kleine Menge hochwertiger Kandidaten in die Queue / `topics.txt` / manuelle Selektion).
2. **Downloaden** bis zum Tageslimit (50) — Stück für Stück ist ok; der Queue-Status in `acquire_queue.json` trackt Fortschritt.
3. **NICHT** alles blind hochladen: **Batch-Upload** nach IC mit `--max-pdfs` (siehe `aa_ic_toolkit_alignment.md`).

---

## 4. Die Brücke: PDF + Metadaten → IC

**Minimal heute (funktioniert):**

- PDF liegt unter dem Fast-Download-Pfad des Profils (z. B. `output/hd_content/downloads/fast_download/...`).
- **`hd_saas_uploader.py --upload-pdfs … --sys-mode`** erzeugt Storage-Objekt + `sys_sources` + `sys_ingestion_jobs` (`extract_text`).
- In **`sys_sources.metadata`** landet derzeit u. a. der Originaldateiname (Uploader); **weitere Felder** (ISBN, `system_id`, Rechtsstatus) könnt ihr **mittelfristig** im Uploader ergänzen oder **nachgelagert per SQL/Admin** — das ist ein **kleines Ticket**, wenn ihr „eine saubere Brücke“ zentral in der DB wollt.

**`assets.jsonl`:** bleibt die **AA-seitige Metadaten-Spur** (Titel, MD5, …) und hilft dem Uploader bei der **Titel-Auflösung** — auch ohne alten HD-`hd_assets`-Weg.

**Nach dem Upload:** K3/K4-Extraktion läuft **in IC** (MinerU → Chunks → LLM-Jobs), nicht im AA-Toolkit.

---

## 5. Zielbild: eine durchgängige Kette (eure Formulierung)

```
IC Bedarf (system_id, K3/K4, Registry)
    → Recherche-Artefakt (kuratierte Metadaten + Legal)
        → AA: Collector/Queue/Pfade
            → Download (≤50/Tag)
                → Lokaler Ordner (PDF + acquire_queue + assets.jsonl)
                    → Uploader --sys-mode (PDF + vorhandene Meta in sys_sources)
                        → Worker (extract_text …) → K3/K4 im KG
```

**Zum Starten des Prozesses:** Ja — ihr könnt **jetzt** mit **Schicht C (Daily Download)** beginnen, **sofern** Member-Limit und VM102-Setup stehen; parallel oder vorher **Schicht A** minimal absichern (welches Profil / welche Topics / welche Registries). Die **Brücke** ist **`--sys-mode`**, nicht HD-Legacy-Ingest.

---

## Überblick: `system_id` → Struktur → Literatur-Registry → AA-Profil

**Zweck:** Ein Blick, **wo** ihr schon eine **Werklandschaft** (Literatur-Registry) habt, **wo** nur der **Strukturkatalog** (Engine/Seed) existiert, und **wo** im AA-Toolkit bereits ein **`*_content`-Profil** mit `query_mode: entity_registry` hängt.

| `system_id` (Deskriptor) | `system_structure/*_catalog_v0.json` | `reference/entity_registry_*` (Literatur/Werke) | AA `projects/*_content` + `entity_registry.json` |
|--------------------------|----------------------------------------|-----------------------------------------------|---------------------------------------------------|
| `hd` | ja (`hd_catalog_v0`) | **ja** (`entity_registry_hd_v02`) | **ja** (`hd_content`) |
| `bazi` | ja | **ja** (`entity_registry_bazi_v01`) | **ja** (`bazi_content`) |
| `ziwei` | ja | **ja** (`entity_registry_ziwei_v01`) | **ja** (`ziwei_content`) |
| `astro` | ja | **ja** (`entity_registry_astro_v01`) | **ja** (`astro_content`) |
| `jyotish` | ja | **ja** (`entity_registry_jyotish_v01`) | **ja** (`jyotish_content`) |
| `mayan_tzolkin` | ja | nein | nein |
| `nine_star_ki` | ja | nein | nein |
| `numerology` | ja | nein | nein |
| `akan` | ja | nein | nein |
| `genekeys` | ja (`gk_catalog_v0`) | nein | nein |
| `enneagram` | ja | nein | nein |
| `i_ching` | ja | nein | nein |
| `kabbalah` | ja | nein | nein |
| `chakra` | ja | nein | nein |
| `pancha_bhuta` | ja | nein | nein |
| `wu_xing` | ja | nein | nein |
| `western_elements` | ja | nein | nein |

**„Ur-Systeme“** im Sinne von Deskriptoren ohne Chart-Engine (z. B. `i_ching`, `kabbalah`, `chakra`, `pancha_bhuta`, `wu_xing`, `western_elements`) stehen in der Tabelle mit **Strukturkatalog**, aber **ohne** eigene Literatur-Registry im `reference/`-Ordner — dort wäre der nächste Schritt analog zu HD/BaZi: **`entity_registry_<system>_v01.json`** definieren und ein AA-Profil anlegen.

**Interpretation:**

- **Downloads „sinnvoll anschieben“** ohne neue Registry: für die **fünf** Zeilen mit **ja / ja / ja** — dort ist die **entity-first Werklandschaft** bereits mit AA verdrahtet.
- **Maya, NSK, Numerologie, Akan, Gene Keys, …:** vor dem **großflächigen** Daily-Download **entweder** (a) **Literatur-Registry + AA-Profil** nachziehen **oder** (b) bewusst mit **`topics.txt` / Keyword-Modus** arbeiten — höheres Risiko für **False Positives** und schlechtere K3/K4-Priorität.
- **Logik anpassen?** Nur wenn Smoke-Tests zeigen, dass Collector/Proxy/Relevanz für ein Profil **nicht** passt; das ist **profil-spezifisch**, nicht „alles neu“.

---

## Brauchen wir erst Registries für die Lücken — und was testen wir vor „50/Tag“?

**Registry-Pflicht:** **Nein** für einen **Start** bei den **fünf** fertigen Profilen. **Ja** (empfohlen), bevor ihr für **Maya/NSK/Numerologie/Ur-Systeme** dieselbe Qualität wollt wie bei HD — sonst fehlt die **gemeinsame Ground Truth** zwischen „was wir beschaffen“ und „was IC später extrahiert“.

**Vor dem dauerhaften 50/Tag (empfohlene Mindesttests):**

1. **AA:** Pro Profil ein kurzer Lauf — `check_daily_limit`, kleines `--max-items` (z. B. 3–5), **Metadaten** in `assets.jsonl` / `acquire_queue.json` plausibel (Titel, MD5, Status).
2. **Brücke:** Ein bis wenige PDFs mit **`--sys-mode`** → in Supabase **`sys_sources`** + Job **`extract_text`** prüfen.
3. **IC:** Ein **S5-Smoke** (MinerU-Phase + optional ein LLM-Job) laut `s5_runbook.md` — damit sind **Scraping/Metadaten/Pfad**, **Upload** und **Extraktion** einmal durchgesteckt.

Wenn das grün ist, ist **50/Tag** primär eine **Kapazitäts- und Kuratierungsfrage**, keine unbekannte Pipeline.

---

## AA-Vollständigkeit — mit Lücken planen

**Annahme:** Auf Anna’s Archive sind **nicht** alle Werke, die ihr aus Registries oder Curriculum anstrebt (Ausgaben, Sprachen, Seltenes, Rechte, Scan-Qualität).

**Umgang (ohne Prozess-Bruch):**

1. **AA bleibt ein Beschaffungskanal**, nicht die Definition von „wir haben alle Primärquellen“.
2. **Lücken festhalten** in **[literature_aa_coverage_gaps.md](literature_aa_coverage_gaps.md)** — Status pro Werk (`found` / `not_found` / `wrong_edition` / `alternate_legal`), kurze Notiz, **legaler** Fallback (Kauf, Bibliothek, OA, eigener Scan wo erlaubt).
3. **Nach jedem Batch oder monatlich** die offenen Zeilen durchgehen und **Priorität** nach `system_id` + K3/K4 setzen.
4. **Später abgleichen:** Diese Datei + `assets.jsonl` / `sys_sources` — dann seht ihr **schnell**, was **nie** über AA kam und bewusst anders beschafft oder vorerst **ausgelassen** wurde.

Rohnotizen dürfen vorübergehend unter `scratch/` liegen; **kuratierte** Lückenliste soll in **`reference/`** bleiben, damit sie nicht als volatile SoT verloren geht.

---

## Runbook: `hd_content` auf IC-Registry neu aufsetzen (VM102)

**Wann:** Alte `output/hd_content/acquire_queue.json` stammt aus **veralteter** Sammlung (z. B. viele False Positives „Design“); **IC-Stand** ist `projects/inner_compass/reference/entity_registry_hd_v02.json` → Ziel **`projects/hd_content/entity_registry.json`** im Toolkit.

**Was bereits getan werden kann (Backup + Registry):**

1. **Backup** des alten Output-Baums: auf VM102 liegt (nach Durchführung) ein Archiv unter  
   `~/annas-archive-toolkit/output/hd_content_backup_pre_ic_20260421.tgz`  
   (vollständiger Snapshot von `output/hd_content/` inkl. alter Queue/Metadaten).
2. **Registry ersetzen:** `entity_registry_hd_v02.json` von VM105 nach  
   `~/annas-archive-toolkit/projects/hd_content/entity_registry.json` **kopieren** (SoT: Inner-Compass-`reference/`).

**Pflicht: Kette neu erzeugen** (alte Artefakte liegen z. B. unter `output/hd_content_stale_20260421/`; ohne neue Queue schlägt `scripts/run_daily_downloads.sh` bei Schritt 2 fehl):

```bash
cd ~/annas-archive-toolkit
export AAT_CONFIG=projects/hd_content/config.json

# 1) Collector (entity_registry) — oft **Stunden**; Hintergrund + Log:
nohup python3 src/simple_collector.py >> output/hd_content/collect_nohup.log 2>&1 &
tail -f output/hd_content/collect_nohup.log   # zur Kontrolle; Ctrl+C beendet nur tail

# 2) Wenn metadata.json wieder sinnvoll gewachsen ist:
python3 src/export_assets.py
python3 src/build_acquire_queue.py

# 3) Daily-Download (Skript im Repo: code/annas-archive-toolkit/scripts/run_daily_downloads.sh)
#    Standard: **ohne** topics.txt-Zweitfilter (IC/entity_registry). Altverhalten: export AAT_FAST_DOWNLOAD_NO_TOPIC_FILTER=0
bash scripts/run_daily_downloads.sh 3 false
```

**Skript:** `run_daily_downloads.sh` ist unter **`code/annas-archive-toolkit/scripts/`** versioniert und auf VM102 nach **`~/annas-archive-toolkit/scripts/`** zu synchronisieren (SCP/`git pull`).

**Hinweis PowerShell/SSH:** Variablen wie `TS=20260421` in **einem** SSH-Befehl von Windows aus können leer ausfallen — Backups manuell **sinnvoll benennen** (`mv …backup_.tgz …backup_pre_ic_20260421.tgz`).

**Troubleshooting Collector:** Steht im Log dauernd **`Geparste Bücher: 0`** / **keine MD5-Links**, liegt es meist an **Selenium vs. aktuellem AA-HTML**, **Proxy/Gluetun**, oder **Chromedriver** — dann zuerst **manuell** die Such-URL im Browser über denselben Proxy prüfen; ggf. Parser/Selektoren im Toolkit anpassen (eigenes Ticket).

**Danach:** `--sys-mode`-Upload und S5 wie in `s5_runbook.md` / `aa_ic_toolkit_alignment.md`.

---

## Relevanz-Scoring (`topics.txt`) — passt das noch zu IC / `entity_registry`?

**Kurz:** Der **Gesamtprozess** ist weiter sinnvoll, aber **zwei Stufen** verwechseln:

| Stufe | Was passiert | Rolle für IC |
|--------|----------------|--------------|
| **1 — Sammlung** | `simple_collector.py` mit **`query_mode: entity_registry`** baut Suchanfragen aus **`entity_registry.json`** (IC: `entity_registry_hd_v02` als Ground Truth). | **Hier** entsteht eure **entity-first** Kuratierung — passt zum IC-Ansatz. |
| **2 — Fast-Download** | `fast_download_acquire.py` kann **zusätzlich** Titel/Autor gegen **`topics.txt`** scoren (Standard: nur Items mit Score ≥ Schwelle). | **Sicherheitsnetz** aus der Keyword-Ära; **kollidiert** mit Stufe 1, wenn die Queue noch **alt** ist (False Positives → alles Score 0) **oder** wenn `topics.txt` **nicht** zu den Registry-Treffern passt. |

**Für euer Setting nach dem IC-Refresh:**

- **Nach** frischer Kette (`simple_collector` → `export_assets` → `build_acquire_queue`) ist die Queue **bereits** durch die Registry vorselektiert. Dann ist die **topics.txt-Filterung oft redundant** — und war bei euch **kontraproduktiv**, solange noch **alte** Pending-Einträge (z. B. „UX Design“) in der Queue lagen.
- **Pragmatisch:** Smoke-Download mit **deaktivierter Topic-Filterung**, damit die neue Queue überhaupt abgearbeitet werden kann:

  ```bash
  python3 src/fast_download_acquire.py --max-items 3 --no-filter-by-topics
  ```

- **Mit Filter:** nur, wenn ihr **`topics.txt`** bewusst **mit** den Registry-Suchmustern aligned haltet (Wartung) **oder** ihr **keyword-lastige** Profile ohne starke Registry nutzt.

**Langfristig (optional im Toolkit):** Config-Flag „Queue ist registry-kuratier → kein zweites Topic-Scoring“ — reines UX-Thema, kein IC-Schema-Change.

**Fazit:** Ihr müsst **nicht** das gesamte Scoring „wegwerfen“ — es ist **profil- und Zustandsabhängig**. Für **HD + IC-Registry** ist **`--no-filter-by-topics`** nach Neuaufbau der Queue der **realistische Default**; für **reine Topic-Profile** bleibt das Scoring **sinnvoll**.

---

## Verwandte Docs

- [aa_ic_toolkit_alignment.md](aa_ic_toolkit_alignment.md) — Daily 50 ↔ IC, VM105→102, `--sys-mode`
- [literature_aa_coverage_gaps.md](literature_aa_coverage_gaps.md) — AA nicht vollständig: Lücken-Log & Reconciliation
- [s5_runbook.md](s5_runbook.md) — E2E technisch
- [engines.md](../cursor/engines.md) — K1–K4
- [pipeline.md](../cursor/pipeline.md) — Jobs nach Upload
- `projects/annas_archive_toolkit/02_system_design/daily_workflow.md` — Limit & Fast-Download
