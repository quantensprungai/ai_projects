# ReST Data Platform / ASTRA IMC — Cursor Documentation Index

> **Projekt:** ReST Data Platform (ASTRA WP 5.2) — Pilot WP 2.1 Offshore Circular Economy / IMC  
> **UI-Kurzname:** ASTRA IMC  
> **Status:** Working Board lokal **und** auf https://imc.ostfriesland.ai; curated Cloud-Daten = lokal  
> **Stand:** 2026-09-04

## Was ist ASTRA IMC?

Eine schlanke **Next.js + Supabase**-Plattform für **Offshore-Wind-Assets**, Dokumente und strukturierte Kreislaufdaten — ohne Service-Falle, ohne Voll-DPP, ohne WP-Sonderportale.

- **WP 5.2** liefert die Plattform (ReST Data Platform)
- **WP 2.1** liefert den maritimen Offshore-/Kreislauf-Pilot (Alpha Ventus u. a.)

## Docs in diesem Ordner

| Datei | Inhalt | Wann lesen |
|-------|--------|------------|
| **handover.md** | Copy-Paste-Kontext für neue Chats + Zusatzblöcke | Immer bei Chat-Wechsel |
| **next_plan.md** | Aktiver Arbeitsplan + Klarstellungen (Events/Häfen/VPI) | Nächster Schritt / Prioritäten |
| **ui_slice1_working_board.md** | Slice-1 UI: KPI + Filter + Tabelle + Detail + CSV + Häfen | Bei Asset-UI / Vertical Slice |
| **demo_runbook_slice1.md** | 2-Minuten Demo-Pfad Alpha Ventus | Nur der Klickpfad; Team-Session: `04_communication/team_stand_plan_2026_08.md` |
| **dq_ampel_slice1.md** | Leichter DQ-Check DE aktiv + Pilot | Nach Daten-/Transform-Änderungen |
| **mastr_matching_de.md** | MaStR-DE Matching-Skelett (Ingest → Review → Apply) | Enrichment / IDs / Inbetriebnahme |
| **natura_overlay_de.md** | BfN-marin Overlay | Schutzgebiete Karte/Detail |
| **cloud_bootstrap.md** | Coolify + Supabase Cloud, Demo-Login, Re-Seed ohne MCP | Cloud, Deploy, Daten nachladen |

**Doku-Regel:** `cursor/` = max. 6–8 aktive Docs. Tiefe liegt in `00_overview/`, `01_spec/`, `02_system_design/`, `03_roadmap/`, `reference/` — nicht alles nach `cursor/` duplizieren.

## Lesereihenfolge (außerhalb cursor/)

| Thema | Einstieg |
|-------|----------|
| Namen, WP-Zuordnung, Repo | `00_overview/naming_canon.md` |
| MVP & Erfolgskriterien | `00_overview/mvp.md` |
| Scope / Non-Scope | `00_overview/scope.md`, `00_overview/scope_shield.md` |
| Architektur | `02_system_design/architecture.md` |
| Technische Reihenfolge | `03_roadmap/technical_next_steps.md` |
| App-Bootstrap | `03_roadmap/imc_app_bootstrap.md` |
| Schema / RLS / 4C | `reference/imc/README.md`, `01_spec/imc_rls_policy_patterns.md` |
| Stakeholder / Comms | `04_communication/stakeholders_and_comms.md` |
| Stand + Plan + Team-Session (Aug 2026) | `04_communication/team_stand_plan_2026_08.md` |

## Verwandte Orte

- **Doku-Index:** `projects/rest_data_platform/README.md`
- **Code-Repo:** `git@github.com:quantensprungai/astra-imc-platform.git` — optionaler Klon: `code/astra-imc-platform/`
- **Kit-Spiegel:** `infrastructure/next-supabase-turbo/`
- **Kanonisches DDL:** `reference/imc/IMC_Schema_v1.sql`
- **Migration bauen:** `node projects/rest_data_platform/scripts/build_imc_migration.mjs`

## Kernzahlen & Konventionen

- **Schema:** Tabellen/ENUMs/Views mit Präfix `imc_*`; Orgs: `imc_orgs`; alles in `public` (kein Schema `imc`)
- **Multi-Tenant:** `imc_wind_farms.account_id` → Makerkit `accounts` (`has_role_on_account`)
- **MVP-Module:** Portal/Rollen, Asset-Register + Upload, schlanke Outputs, optionale KI
- **Scope Shield:** Standard statt Sonderanfertigung · Self-Service statt Full-Service · Prototyp statt Produktbetrieb

## Workspace

**Root `ai-projects`** (`ai_projects.code-workspace`) — Doku + Code + Infra zusammen. Nicht nur `projects/rest_data_platform/` öffnen.

## Abgrenzung

- **Nicht** `code/hd_saas_app/` (Inner Compass) — separates Projekt, separates Repo
- Meta-Repo (`ai-projects`): nur Doku/Infra committen; App-Code nur in `astra-imc-platform` (Commits auf explizite Anweisung)
