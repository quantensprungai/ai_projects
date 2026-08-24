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

Stand (2026-08-17) — ausführlich: projects/rest_data_platform/04_communication/team_stand_plan_2026_08.md
  - Doku: projects/rest_data_platform/ · Code: code/astra-imc-platform/ → quantensprungai/astra-imc-platform
  - Schema: IMC v1/v1.2 + MaStR-Einheiten + Schutzgebiete + imc_farm_ports.distance_km + ERA5 + View imc_v_farm_era5_days
  - ETL: 4C + MaStR-DE + Units + BfN marin + Nordsee-Häfen + ERA5 CLI (CDS, Zell-Cache; nicht aus der UI)
  - Slice-1 UI: Working Board + Natura + Häfen-Filter + ERA5 Detail/CSV + Rückbau-Zeitstrahl + sortierbare Tabelle
  - Dual-Track: Postgres = SoT; AAS = Export/Projektion. Marc/Thomas lesen DB (CSV/View), nicht AAS.
  - DE aktiv 76, davon 61 mit Inbetriebnahme. MaStR ~33 Parks / ~1593 Einheiten. Natura ~205. Häfen 118 / 677 Links.
  - ERA5: 3 Parks / 1858 Tage (AV 680, Albatros + Amrumbank West je 589); DE-Batch läuft. Vessels: 0 Zeilen (bewusst).
  - Team-Folien: projects/rest_data_platform/04_communication/ASTRA_IMC_Team_Stand_2026_08.pptx
  - Marketing: de/en Landing mit Working-Board-Screenshot (public/images/working-board-hero.png)
  - Cloud IMC pfprwudrfkugvzpjyrvj pausiert — kein MCP-Chunk-Seed; Häfen/ERA5 nicht in Cloud.
  - Lokal: Docker + pnpm supabase:web:* · Team-Slug oft research-team (nicht makerkit)
  - Meta-Branch: docs/rest-data-platform-mastr-etl

Zielbild MVP (5–12 Wochen):
  Login/Rollen, Offshore-Asset-Register (DE/Nordsee-Default), minimaler Export.
  Upload bewusst später. Kein Voll-DPP, keine Simulation, kein Custom-Dashboard-Service.
  Produkt A (Decom Capacity Screener) ist noch nicht gebaut — nur Datenbausteine.

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

Nächster sinnvoller Schritt:
  Spur A Daten: ERA5-DE-Batch zu Ende (ein CDS-Job); Marc-Kanal = Serie day/wind_ms/hs_m (operable nur KPI)
  Spur B Interop: Industrie-Normen ablegen → mit Shubham AAS-Schnitt AV + Interface Agreement DB→AAS; erst dann Exporter
  Team-Session: Eisberg vor UI — 04_communication/team_stand_plan_2026_08.md
  Geblockt: BOM auf Thomas; Sequenz/Sim-CSV auf Marc; Upload erst bei Partnerbedarf
  Nicht: VPI-Vollflotte, Simulation in der Plattform, MCP-Cloud-Seed, zweites CDS parallel

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
- projects/rest_data_platform/04_communication/team_stand_plan_2026_08.md
- projects/rest_data_platform/04_communication/status_update_template.md
- projects/rest_data_platform/03_roadmap/phase_a_timeline_2026_2028.md
```
