---
last_update: 2026-04-20
status: stable
scope:
  summary: "Anna's Archive Toolkit ↔ Inner Compass (S5/sys_*): empfohlener Git-Betrieb auf VM102, Ist/Soll-Prüfliste, Verifikationsschritte."
  in_scope:
    - vm102 deployment options (ssh deploy key vs scp from vm105)
    - ic sys-mode uploader alignment checklist
    - incident note 2026-04-20 vm102 folder rename + restore
    - daily download limit 50 vs ic ingestion coupling
  out_of_scope:
    - mineru tuning
    - chart engine precision
notes:
  - "VM102 HTTPS git clone scheitert ohne GitHub-Credentials (privates Repo)."
---

# AA-Toolkit ↔ Inner Compass — Alignment & Betrieb

## Betriebsnotiz 2026-04-20 (VM102)

Ein automatisierter Versuch, `~/annas-archive-toolkit` per `git clone https://github.com/quantensprungai/annas-archive-toolkit.git` neu anzulegen, ist **fehlgeschlagen** (`could not read Username for 'https://github.com'` — privates Repo). Der bisherige Ordner war kurz nach `~/annas-archive-toolkit.nogit.bak.` umbenannt worden; er wurde wieder nach **`~/annas-archive-toolkit`** zurückbenannt — **Betrieb wieder wie vorher**.

**Lehre:** Auf VM102 nur **`git@github.com:…`** mit **Deploy Key** (oder PAT nur bewusst / nicht im Klartext-Skript) — nicht blind HTTPS von unattended Scripts.

---

## Empfehlenswert: VM102 git-tracked machen

**Ziel:** reproduzierbarer Stand = `origin/main`, kein „lose Kopie ohne `.git`“.

1. **GitHub:** Im Repo `quantensprungai/annas-archive-toolkit` einen **Deploy Key (read-only)** anlegen; Public Key auf VM102 in `~/.ssh/`.
2. **VM102:** `~/.ssh/config` mit `Host github.com` + `IdentityFile` (siehe auch `projects/annas_archive_toolkit/02_system_design/deployment_and_sync.md`).
3. **Clone in neuen Ordner** (laufenden Baum nicht zerstören):
   - `git clone git@github.com:quantensprungai/annas-archive-toolkit.git ~/annas-archive-toolkit.git.new`
4. **Secrets & Runtime übernehmen** von altem `~/annas-archive-toolkit`:
   - `.env.hd_saas` (oder gleichwertige Env-Datei), ggf. `~/.config/annas-archive-toolkit/member.env`
   - Python: vorhandenes `.venv` kopieren **oder** auf VM102 die im Toolkit dokumentierte venv-/Installationsweise nachziehen (mit demselben Python wie bisher).
5. **Smoke:** `python3 src/hd_saas_uploader.py --help` und ein **Dry-Run**/ein PDF mit **`--sys-mode`** gegen die gewünschte Supabase-Instanz (siehe `s5_runbook.md`).
6. **Umstellung:** Skripte/Cron/Pfade auf `~/annas-archive-toolkit.git.new` zeigen lassen, danach alten Ordner nach `~/annas-archive-toolkit.legacy-YYYYMMDD` verschieben und Symlink `annas-archive-toolkit` → neuer Clone (optional).

**Interim ohne Git auf VM102:** Nach Änderungen am Uploader auf VM105 **`scp`** — fertiges Skript: **`infrastructure/spark/sync_aa_uploader_to_vm102.ps1`** (Host `docker-apps`, Ziel `~/annas-archive-toolkit/src/`). Entspricht Option A in `s5_runbook.md`.

---

## Ist vs. Soll (Review-Matrix)

| Thema | Ist (typisch heute) | Soll (IC-optimal) |
|--------|---------------------|-------------------|
| **Upload in IC-Pipeline** | `hd_saas_uploader.py` + **`--sys-mode`** → `sys_uploads_raw`, `sys_sources`, `sys_ingestion_jobs` | Unverändert nutzen; in Runbooks/Cron **immer** `--sys-mode` für Produktion |
| **Ohne `--sys-mode`** | Legacy `hd_*` Tabellen / alter SaaS-Pfad | Nur noch für Migration/Debug; nicht für IC-Betrieb |
| **Benennung** | Datei/Env heißen noch `hd_saas_*` | Mittelfristig optional: `ic_*`-Namen + dünner Wrapper (reine Klarheit, kein Muss) |
| **VM102-Arbeitskopie** | Oft **ohne** `.git` (Kopie/SCP) | **Git clone (SSH)** + regelmäßiges `git pull` |
| **VM105** | Repo unter `code/annas-archive-toolkit`, oft **lokale Config-Änderungen** | `git pull` vor Deploy; Configs nicht committen oder klar `.gitignore` |
| **Doku `projects/annas_archive_toolkit`** | Teils noch `hd_assets` / HD-SaaS-Flow | IC-Kapitel: explizit **`sys_*` + `--sys-mode`** verweisen (dieses Doc + `s5_runbook.md`) |
| **Infra `HD_WORKER_HANDOVER.md`** | Noch `hd_saas_app` / `hd_ingestion_jobs` an Stellen | Schrittweise auf **`inner_compass_app`** / **`sys_ingestion_jobs`** angleichen |

---

## Daily-Download (50) + IC (K3/K4) — sinnvolle Kopplung

**Kern:** Das **50/Tag-Limit** ist eine **Member-API-/Fast-Download-Grenze** des AA-Toolkits (Beschaffung auf der Platte). **K3/K4** passieren **in IC**, sobald PDFs über **`--sys-mode`** in **`sys_*`** landen und der **Spark-Worker** die Jobs abarbeitet. Das sind **zwei Ketten**, die ihr bewusst **nacheinander** koppelt — nicht ein einziger magischer „IC-Download“-Button.

### Schicht A — Recherche (IC / Kuratierung, „50 Quellen“-Logik)

- **Ziel:** Welche Werke/Autoren/Systeme (`system_id`) sind **legal** beschaffbar und für **K3+K4** relevant?
- **Artefakte:** Tabellen/Matrix aus dem **Literatur-Agenten-Prompt**; optional Anreicherung von **`topics.txt`** / Profilen (`projects/hd_content`, `bazi_content`, …) und **`entity_registry_*.json`** unter `projects/inner_compass/reference/` (entity-first).
- **Liefert:** Qualität und **Priorität** der Kandidaten — **ersetzt** weder AA-Limit noch Collector-Code.

### Schicht B — Metadaten & Queue (AA, klassisch)

- **Collector** (`simple_collector.py` + `export_assets.py` + `build_acquire_queue.py` … je Profil): baut **`metadata`**, **`assets.jsonl`**, **`acquire_queue.json`**.
- **Doku:** `projects/annas_archive_toolkit/00_overview/status.md`, `02_system_design/daily_workflow.md`, `complete_workflow.md`.

### Schicht C — Bis zu 50 Downloads / Tag (AA, VM102)

- **Limit prüfen:** `python3 src/check_daily_limit.py` (mit `member.env`).
- **Ausführen:** z. B. `bash scripts/run_daily_downloads.sh 50 false` auf VM102 **oder** von VM105: `run_daily_downloads.ps1 -MaxItems 50` (steuert VM102 per SSH — Pfade siehe `status.md` § Runbook).
- **Ergebnis:** PDFs unter dem Fast-Download-Pfad des Profils (typisch `output/hd_content/downloads/fast_download/...` für HD-Profil).

### Schicht D — Andocken an IC (Brücke, nicht HD-Legacy)

- **`hd_saas_uploader.py --upload-pdfs <pfad> --max-pdfs N --sys-mode`** mit **`AAT_CONFIG`** und **Supabase-Env** wie in `s5_runbook.md`.
- **Empfehlung:** `N` **kleiner** als 50 (z. B. 5–10 pro Lauf), damit **Storage**, **Job-Queue** und **MinerU/Worker** auf Spark nicht mit **50 parallelen** `extract_text`-Jobs überfordert werden — der Rest der PDFs bleibt auf der Platte bis zum nächsten Batch.
- **`assets.jsonl`:** weiter **nützlich** für Titel-Auflösung im Uploader; der alte Weg **„nur `assets.jsonl` → `hd_assets` UI-Ingest“** ist für **reines IC** **nicht** nötig, wenn ihr **direkt PDF + `--sys-mode`** nutzt.

### Schicht E — K3/K4 in der Pipeline

- Nach erfolgreichem **`extract_text`:** Folgejobs (Klassifikation, Extraktion, …) laut `projects/inner_compass/cursor/pipeline.md` und K3/K4-Zuordnung in `engines.md`.

**Kurzfassung für den Start „jetzt“:** Recherche/Curriculum parallel fahren oder zumindest **ein** Profil + klare **Relevanz** (`topics.txt` / Score); **Daily 50** auf VM102 starten; **am selben Tag oder danach** kontrolliert **`--sys-mode`-Upload-Batches** + Worker-Phase laut S5 — so nutzt ihr **AA für Beschaffung** und **IC für Bedeutung/Graph**, ohne wieder in das **reine HD-SaaS-Metadatenmodell** zurückzufallen.

---

## So prüft ihr „tatsächlich“ vs. „optimal“

1. **Codegleichheit VM102 ↔ `origin/main`:** Hash oder `diff` von `src/hd_saas_uploader.py` (VM105 nach `git pull`, VM102 aktuelle Datei).
2. **Supabase nach einem Test-Upload (`--sys-mode`):** Zeilen in `sys_sources`, Job `extract_text` in `sys_ingestion_jobs`, Objekt im Bucket `sys_uploads_raw`.
3. **Spark/Worker:** Job wird geholt, MinerU läuft, Chunks in `sys_source_chunks` (siehe `s5_runbook.md` SQL-Checks).
4. **Kein Legacy-Leak:** Sicherstellen, dass **kein** Cron ohne `--sys-mode` läuft, falls IC die einzige Ziel-DB ist.

---

## Nächste konkrete Schritte (Reihenfolge)

1. Deploy Key auf VM102 fertigstellen → sauberer **SSH-Clone** wie oben.
2. **Einmal** E2E laut `s5_runbook.md` mit `--sys-mode` dokumentieren (Screenshots/Job-IDs optional im Ticket).
3. ~~Infra-Doku (`infrastructure/spark/HD_WORKER_HANDOVER.md`) und `s5_runbook.md` Pfade **`inner_compass_app`** statt `hd_saas_app` konsolidieren~~ → **erledigt 2026-04-20** (IC-Abschnitt + Pfade + Deploy-Skript).
4. Optional: AA-Projekt-`complete_workflow.md` um einen Abschnitt „IC (sys_*)“ ergänzen — ohne die Legacy-Beschreibung zu löschen, bis nichts mehr auf `hd_*` hängt.

Verwandt: [s5_runbook.md](s5_runbook.md) · [literature_acquisition_ic_aa.md](literature_acquisition_ic_aa.md) (Recherche ↔ 50/Tag ↔ Brücke)
