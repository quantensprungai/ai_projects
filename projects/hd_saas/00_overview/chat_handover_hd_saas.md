# Chat Handover – HD-SaaS (Copy/Paste Block)

<!--
last_update: 2026-02-12
status: aktuell
scope:
  summary: "Ausgefülltes Handover für Chat-Wechsel – HD-SaaS Fokus."
notes:
  - "Template: projects/_meta/chat_handover_template.md"
-->

## Schritte vorher (vor dem Chat-Wechsel)

1. **Current Status prüfen** – `current_status_local_dev.md` lesen; ggf. Reality Block aktualisieren (letzte Änderungen, Blocker, Datenstand).
2. **Next Steps abgleichen** – `02_system_design/next_steps_was_fehlt_noch.md` prüfen; Reihenfolge ggf. anpassen.
3. **Handover-Block aktualisieren** – Abschnitt 3 (Zustand), 5 (Hypothese), 6 (Nächste Schritte) mit aktuellem Stand füllen.
4. **Links prüfen** – Abschnitt 7: Alle Pfade existieren? (master_map, README, plan_option_b, etc.)
5. **Dann:** Block unten kopieren und in neuen Chat einfügen.

---

**Kopiere den Block unten in einen neuen Chat.**

---

## Copy/Paste Block

```
### 1) Kontext: „In welchem Universum sind wir?“

- **Workspace**: `ai_projects.code-workspace` (Multi-Root: `projects/`, `infrastructure/`, `code/`)
- **Aktives Projekt**: HD-SaaS
- **Ziel / Outcome**: Backend-Datenbasis vollständig ausbauen (Option B), dann UI. Pipeline: PDF → Chunks → Interpretations → KG-Nodes → Synthesis läuft; nächste Schritte: Edges, Dynamics, Interactions.
- **Nicht-Ziele / Guardrails**: Keine Secrets in Logs/Terminal, keine Service Role Keys im Browser/Client, keine Scope-Ausweitung.

### 2) Repo-Orientierung

- **Docs/Infra**: `projects/hd_saas/`, `infrastructure/spark/`
- **Code**: `code/hd_saas_app/` (eigenes Git-Repo, nicht Teil des Root-Repos)

### 3) Aktueller Zustand

- **Status**: Partially working – Pipeline bis text2kg + synthesize_node läuft (Cloud + Spark).
- **Letzte bestätigte gute Version**: 2026-02-12 – text2kg, LLM-Extraktion, MinerU, Worker als systemd-Service auf Spark. Zwei-Phasen-Betrieb: HD_WORKER_JOB_TYPES auf VM102 für Phase 1 (keine Stubs).
- **Datenstand**: 681 hd_assets, 111 PDFs hochgeladen; Interpretations system = hd/bazi/mixed/other (classify_domain).
- **Blocker**: Keine aktuell.

### 4) Architektur-Schnittstellen

- **Control Plane**: Supabase Cloud (HD Tabellen, RLS, Worker service_role)
- **Data Plane**: Spark Worker (`spark-56d0`), systemd `hd-worker.service`, `~/srv/hd-worker`; VM102 (docker-apps) für Phase 1 oder Uploads
- **Speicher**: Buckets (hd_uploads_raw), Tabellen (hd_assets, hd_asset_chunks, hd_interpretations, hd_kg_nodes, hd_kg_edges, hd_synthesis_wordings)
- **Endpoints**: HD_LLM_EXTRACTION_URL (SGLang/Qwen auf Spark Port 30001), MinerU für PDFs

### 5) Aktive Arbeits-Hypothese

Option B: Datenbasis zuerst. Nächster Fokus: KG-Edges (payload.relations vom LLM liefern, text2kg schreibt Edges). Dann extract_dynamics, extract_interactions, danach Insight-Engine-UI + Sprache.

### 6) Nächste Schritte (max. 5)

1. KG-Edges – payload.relations definieren/erzeugen, text2kg erweitern (Schema bereit)
2. extract_dynamics (optional) – Dimensions + challenges/growth → hd_dynamics
3. extract_interactions (optional) – payload.interactions → hd_interactions
4. UI/UX Insight Engine – KG + Synthesis in App anzeigen
5. Sprache aus App – debug.language beim Job-Anlegen

### 7) Kanonische Links

- **Global Map**: projects/_meta/master_map.md
- **Projekt Index**: projects/hd_saas/README.md
- **Current Status**: projects/hd_saas/00_overview/current_status_local_dev.md
- **Plan / Nächste Schritte**: projects/hd_saas/02_system_design/plan_option_b_roadmap.md, next_steps_was_fehlt_noch.md
- **Erkenntnisse für später**: projects/hd_saas/02_system_design/erkenntnisse_und_fuer_spaeter.md
- **Infra/Worker**: infrastructure/spark/hd_worker_ops.md, HD_WORKER_HANDOVER.md
- **Code Entry**: code/hd_saas_app/apps/web/scripts/hd_worker_mvp.py

### 8) Sicherheits-Hinweise

- Keine Secrets tippen. Nur env-files / systemd EnvironmentFile.
- Nie Service Role Keys im Browser/Client.
- Bei Key-Leak: rotieren.
```
