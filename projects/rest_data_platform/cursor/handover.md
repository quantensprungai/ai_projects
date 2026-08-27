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
  - Branch UI: `feat/assets-ia-restructure` (Waves + Park-Dossier); Parties-CSV auf Akteuren
  - Makerkit catalog + Passkeys/react-email/native-sharing auf main (PR #1 merged)
  - Schema: IMC v1/v1.2 + MaStR + Natura + Häfen + ERA5 daily/hourly + CAPEX/OPEX/Events + Vessel-Katalog
  - Dual-Track: Postgres = SoT; AAS = Export. Partner: CSV/View, nicht AAS.
  - Zahlen lokal: Farms 3606 · MaStR 33 accepted / 1593 Units · Natura ~205 · Häfen 118 / 677 Links
  - ERA5 daily: 3 Parks / 1858 Tage. Hourly: AV **CDS** ~23k h (2024-01→2026-08, `cds+hourly`).
  - Nav (Produktbegriffe DE=EN): Assets → Waves → Economics → Vessels
  - Waves `/assets/waves` — Gegenverkehr Ausbau/Rückbau (MW, Schätzung); CTA vom Register
  - Economics `/assets/economics` · Vessels `/assets/vessels`
  - Park-Dossier (Collapsibles): Steckbrief · Economics · Lebenszyklus · Einheiten (BOM-Anker) · Standort · Wetter · Akteure · Schiffe
  - Park-Detail Logistik-Schichten (nicht vermischen):
      1) Akteure — 4C Supply Chain DE (~3633 Links); Kernkacheln + Parties-CSV
      2) Schiffseinsätze (VPI) — DE Contracts light ~1183; Filter O&M/Install; AV ~60
      3) Sim-Rollen (Pilot) — kuratierte Typ×Phase für Simulation (UI ohne Partnernamen)
  - Locale: Workspace-Switch hält EN; i18n-Messages `use cache`+`cacheLife(max)` → nach Key-Änderungen `next dev` neu starten
  - IA Drafts: 01_spec/interface_agreement_marc_anylogic_v0.md + …_thomas_lca_v0.md
  - Präsi-Inhalt: 04_communication/team_stand_plan_2026_08.md (PPTX optional neu bauen)
  - Cloud IMC pausiert; lokal Docker + pnpm supabase:web:*

Zielbild MVP (5–12 Wochen):
  Login/Rollen, Offshore-Asset-Register, minimaler Export.
  Upload später. Kein Voll-DPP, keine Simulation in der App, kein Custom-Dashboard-Service.
  Produkt A light: Waves Gegenverkehr (Kapazität über Jahre); voller Screener noch offen.

Scope Shield: projects/rest_data_platform/00_overview/scope_shield.md

Lies zuerst:
  - projects/rest_data_platform/cursor/next_plan.md
  - projects/rest_data_platform/00_overview/naming_canon.md
  - projects/rest_data_platform/00_overview/mvp.md

Nächster Schritt:
  1) ~~Demo-Daten/UI-Freeze Stage A Backbone~~ · ~~Assets-IA (Waves + Dossier)~~
  2) Partner-Sync Marc (Stunden-CSV + Katalog + was er wirklich braucht) — Sequenz/Sim-CSV blockiert
  3) Optional: Waves MW↔Parks-Toggle; Einheiten→BOM light; DE-ERA5-Tagesbatch; Thomas BOM/LCA
  Geblockt fachlich: BOM Thomas; Sequenz/Sim-CSV Marc; Vessel-Wetter final
  Nicht: Contracts-17k blind; Decom-Steps aus 4C ableiten; Sim/LCA in der Plattform; MCP-Cloud-Seed; Mega-Dashboard

Produkt-Klarstellung Logistik:
  - Akteure ≠ Partner-Sequenz; Schiffseinsätze = Historie; Sim-Rollen = kuratierter Typ-Bridge
  - Aus Akteuren/Contracts keine automatischen Decom-Steps — AAS-Parties/Demo ok, Sim-Plan nicht
  - Einheiten = Inventar/BOM-Anker; Lebenszyklus = Events/Meilensteine (getrennt)

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
