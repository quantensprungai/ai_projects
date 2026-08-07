# ReST Data Platform / ASTRA IMC — Handover

> Copy-Paste diesen Block am Anfang eines neuen Chat-Fensters (Cursor oder Claude).
> Workspace: `ai_projects.code-workspace` (Root `ai-projects`) — nicht nur `projects/rest_data_platform/`.

---

## Kontext-Block (kopieren)

```
Projekt: ReST Data Platform (ASTRA WP 5.2) — Pilot WP 2.1 Offshore Circular Economy / IMC
UI-Kurzname: ASTRA IMC
Tech: Next.js (Makerkit Turbo) + Supabase (Postgres, PostGIS, Auth, Storage, RLS)
Workspace: ai-projects Root — Doku + Code + Infra zusammen (NICHT nur projects/rest_data_platform/)

Stand (2026-08-07):
  - Doku: projects/rest_data_platform/ (Scope, Architektur, Roadmap, IMC-Referenz-SQL)
  - Code: code/astra-imc-platform/ → git@github.com:quantensprungai/astra-imc-platform.git
  - Schema: IMC v1 + v1.2 + MaStR + imc_turbines + imc_protected_areas
  - ETL: 4C + MaStR-DE + Units + BfN marine Schutzgebiete (alle Layer)
  - Slice-1 UI: Assets Working Board (KPI, Filter, OSM-Karte, Schutzgebiete-Toggle, sortierbare Tabelle, Detail, CSV)
  - Specs: cursor/ui_slice1_working_board.md · cursor/mastr_matching_de.md · cursor/natura_overlay_de.md
  - MaStR: ~33 DE-Parks accepted/applied; ~1593 Einheiten lokal
  - Schutzgebiete: ~205 (FFH/SPA/NSG/LSG/NLP/NRP/BR); Overlay + Detail-Nähe
  - Meta-Branch: docs/rest-data-platform-mastr-etl
  - Supabase Cloud: Ref `pfprwudrfkugvzpjyrvj` — db push + Natura-Ingest noch offen
  - Lokal: Docker Desktop für `pnpm supabase:web:*`

Zielbild MVP (5–12 Wochen):
  Login/Rollen, Offshore-Asset-Register (DE/Nordsee-Default), minimaler Export.
  Upload bewusst später. Kein Voll-DPP, keine Simulation, kein Custom-Dashboard-Service.

Scope Shield (harte Grenzen):
  Standard statt Sonderanfertigung. Self-Service statt Full-Service. Prototyp statt Produktbetrieb.
  Details: projects/rest_data_platform/00_overview/scope_shield.md

Lies zuerst:
  - projects/rest_data_platform/00_overview/naming_canon.md (Namen, WP-Zuordnung, Repo)
  - projects/rest_data_platform/00_overview/mvp.md
  - projects/rest_data_platform/03_roadmap/imc_app_bootstrap.md

Dann je nach Aufgabe:
  - Architektur/Grenzen: 02_system_design/architecture.md
  - Technische Reihenfolge: 03_roadmap/technical_next_steps.md
  - Schema/RLS/4C-Sourcing: reference/imc/README.md + 01_spec/imc_rls_policy_patterns.md
  - Daten-Leitfaden: 03_roadmap/imc_data_implementation_leitfaden.md
  - Makerkit/DB im Code: code/astra-imc-platform/AGENTS.md + apps/web/supabase/AGENTS.md
  - Kit-Spiegel: infrastructure/next-supabase-turbo/

Nächster sinnvoller Schritt (Implementierung):
  1. Cloud db push (Migrationen) + `ingest_natura_bfn.py --replace` gegen Cloud
  2. Optional dünn: Emden/Häfen-Seed (imc_ports) ODER ERA5 Alpha-Ventus
  3. Demo-Runbook einmal durchspielen (makerkit / Assets)
  4. BOM/AAS erst mit Partner-Feldliste
  5. Upload erst bei Partner-CSV-Bedarf

Git-Regeln:
  - Meta-Repo (ai-projects): nur Doku/Infra committen
  - Code-Repo (astra-imc-platform): App/Migrationen — Commits nur auf explizite Anweisung
  - Nicht vermischen mit code/hd_saas_app (Inner Compass)
```

---

## Wenn der Chat über ARCHITEKTUR / SCHEMA geht

```
Zusätzlich lesen:
- projects/rest_data_platform/02_system_design/architecture.md
- projects/rest_data_platform/reference/imc/IMC_Schema_v1.sql
- projects/rest_data_platform/01_spec/imc_rls_policy_patterns.md
- code/astra-imc-platform/apps/web/supabase/migrations/
- Multi-Tenant: imc_wind_farms.account_id → accounts (has_role_on_account)
```

## Wenn der Chat über IMPLEMENTIERUNG / UI geht

```
Zusätzlich lesen:
- code/astra-imc-platform/AGENTS.md
- code/astra-imc-platform/apps/web/AGENTS.md
- projects/rest_data_platform/03_roadmap/imc_app_bootstrap.md (Integrationsvariante A)
- Scope: kein Feature außerhalb 00_overview/scope.md ohne Rückfrage
```

## Wenn der Chat über STAKEHOLDER / COMMS geht

```
Zusätzlich lesen:
- projects/rest_data_platform/00_overview/scope_shield.md
- projects/rest_data_platform/04_communication/stakeholders_and_comms.md
- projects/rest_data_platform/04_communication/status_update_template.md
- projects/rest_data_platform/03_roadmap/phase_a_timeline_2026_2028.md
```
