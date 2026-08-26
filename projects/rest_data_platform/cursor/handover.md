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

Stand (2026-08-26) — Plan: projects/rest_data_platform/cursor/next_plan.md
  - Doku: projects/rest_data_platform/ · Code: code/astra-imc-platform/ → quantensprungai/astra-imc-platform
  - Makerkit catalog + Passkeys/react-email/native-sharing auf main (PR #1 merged)
  - Schema: IMC v1/v1.2 + MaStR + Natura + Häfen + ERA5 daily/hourly + CAPEX/OPEX/Events + Vessel-Katalog
  - Dual-Track: Postgres = SoT; AAS = Export. Marc/Thomas: CSV/View, nicht AAS.
  - Zahlen lokal: Farms 3606 · MaStR 33 accepted / 1593 Units · Natura ~205 · Häfen 118 / 677 Links
  - ERA5 daily: 3 Parks / 1858 Tage. Hourly: AV **CDS** ~23k h (2024-01→2026-08, `cds+hourly`).
  - CAPEX/OPEX am Park + Portfolio UI `/assets/economics`. Vessel-UI: Katalog+Flotte+Contracts/Assignments Pilot.
  - Vessels: 8 Typenkatalog + 2210 VPI-Flotte; Contracts/Assignments Pilot; day_rate Katalog-Platzhalter
  - Locale: Workspace-Switch hält EN (`WorkspaceDropdown` + Team-Home-Redirect)
  - IA Drafts: 01_spec/interface_agreement_marc_anylogic_v0.md + …_thomas_lca_v0.md
  - Präsi-Inhalt: 04_communication/team_stand_plan_2026_08.md (PPTX optional neu bauen)
  - Cloud IMC pausiert; lokal Docker + pnpm supabase:web:*

Zielbild MVP (5–12 Wochen):
  Login/Rollen, Offshore-Asset-Register, minimaler Export.
  Upload später. Kein Voll-DPP, keine Simulation in der App, kein Custom-Dashboard-Service.
  Produkt A (Decom Capacity Screener) noch nicht gebaut.

Scope Shield: projects/rest_data_platform/00_overview/scope_shield.md

Lies zuerst:
  - projects/rest_data_platform/cursor/next_plan.md
  - projects/rest_data_platform/00_overview/naming_canon.md
  - projects/rest_data_platform/00_overview/mvp.md

Nächster Schritt:
  1) ~~Logistics · CAPEX-Portfolio · CDS AV Stunden~~
  2) Optional: DE-ERA5-Tagesbatch, VPI-Contracts light, Stakeholders/OEM
  3) Partner-IA-Review parallel
  Geblockt fachlich: BOM Thomas; Sequenz/Sim-CSV Marc; Vessel-Wetter final
  Nicht: Contracts-17k blind, Sim/LCA in der Plattform, MCP-Cloud-Seed

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
