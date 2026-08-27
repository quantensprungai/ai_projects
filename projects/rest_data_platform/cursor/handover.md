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

Stand (2026-08-27) — Plan: projects/rest_data_platform/cursor/next_plan.md
  - Doku: projects/rest_data_platform/ · Code: code/astra-imc-platform/ → quantensprungai/astra-imc-platform
  - Branch UI: `feat/assets-ia-restructure` (Waves + Dossier + Grid/OHVS + 4C-Turbine-Typ + MaStR Units)
  - Makerkit catalog + Passkeys/react-email/native-sharing auf main (PR #1 merged)
  - Schema: IMC v1/v1.2 + MaStR + Natura + Häfen + ERA5 + CAPEX/OPEX/Events + Vessel + Grid/Platforms + Turbine-Models
  - Dual-Track: Postgres = SoT; AAS = Export. Partner: CSV/View, nicht AAS.
  - Zahlen lokal: Farms 3606 · Grid ~1423 · Platforms ~686 · Turbine-Models ~369 (~619 Farms gelinkt) · MaStR 33 accepted / 1651 Units · Natura ~205 · Häfen 118 / 677
  - ERA5 daily: 3 Parks / 1858 Tage. Hourly: AV **CDS** ~23k h (2024-01→2026-08, `cds+hourly`).
  - Nav: Assets → Waves → Economics → Vessels
  - Park-Steckbrief: Site-Design + Netz/OHVS (Owner) + **4C-Turbine-Typ (MW/Ø/HH)**; Einheiten = MaStR-Stückliste
  - ETL u.a.: transform_4c_farm_grid / platforms / turbine_models; MaStR Units park_key
  - GIS: Map-light — kein Router. Marc: Snapshot + Wetter-CSV — kein Dauerstream; Barge nur jack_up_barge (offen)
  - Logistik am Park: Akteure (~3633) · VPI-Einsätze DE (~1183) · Sim-Rollen nur AV-Pilot
  - Locale: EN Workspace; nach i18n-Keys `next dev` neu starten
  - IA: marc_anylogic_v0 + thomas_lca_v0 · Präsi: team_stand_plan_2026_08.md (+ PPTX)
  - Cloud IMC pausiert; lokal Docker + pnpm supabase:web:*

Zielbild MVP (5–12 Wochen):
  Login/Rollen, Offshore-Asset-Register, minimaler Export.
  Upload später. Kein Voll-DPP, keine Simulation in der App, kein Custom-Dashboard-Service.
  Produkt A light: Waves Gegenverkehr; voller Screener noch offen.

Scope Shield: projects/rest_data_platform/00_overview/scope_shield.md

Lies zuerst:
  - projects/rest_data_platform/cursor/next_plan.md
  - projects/rest_data_platform/00_overview/naming_canon.md
  - projects/rest_data_platform/00_overview/mvp.md

Nächster Schritt:
  1) ~~Stage A Backbone / Assets-IA / Grid-OHVS / MaStR / 4C-Turbine-Typ~~ — Daten-Backlog light fertig
  2) **Marc-Sync** (Stunden-CSV + Katalog + Barge/IA) · parallel **PR → main** wenn Demo ok
  3) Optional: DE-ERA5; Thomas BOM; Shubham AAS
  Geblockt: BOM Thomas; Sequenz/Sim-CSV Marc; Vessel-Wetter final; Barge-Typ
  Nicht: Transmission-Vollimport; GIS-Router; 4C↔MaStR unit-Join; Contracts-17k; Decom aus 4C; Sim/LCA in App

Pilot AV vs andere:
  - Breit: Design, Grid, oft 4C-Typ, MaStR-Units (33 Parks), Akteure/Contracts DE
  - AV extra: ERA5-Stunden, Sim-Rollen, Kuratierung (Emden/Tripod) — Demo-Pfad, nicht einziger Datenpark

Produkt-Klarstellung:
  - 4C-Typ = Katalog/Steckbrief; MaStR-Einheiten = Inventar/BOM-Anker; OHVS ≠ Einheiten
  - Akteure ≠ Sequenz; Schiffseinsätze = Historie; Sim-Rollen = Typ-Bridge

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
- i18n: apps/web/i18n/request.ts — neue Keys brauchen next-dev-Restart
```

## Wenn der Chat über STAKEHOLDER / COMMS geht

```
Zusätzlich lesen:
- projects/rest_data_platform/00_overview/scope_shield.md
- projects/rest_data_platform/04_communication/stakeholders_and_comms.md
- projects/rest_data_platform/04_communication/team_stand_plan_2026_08.md
- projects/rest_data_platform/04_communication/status_update_template.md
- projects/rest_data_platform/03_roadmap/phase_a_timeline_2026_2028.md
```
