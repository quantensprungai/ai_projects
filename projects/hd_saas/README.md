<!-- Reality Block
last_update: 2026-01-29
status: draft
scope:
  summary: "HD-SaaS – Doku Index + Code/Infra Crosslinks (Multi-System Setup)."
  in_scope:
    - index + crosslinks
    - cursor workspace guidance
  out_of_scope:
    - implementation details
    - secrets
notes: []
-->

# HD‑SaaS – Doku Index

## Kanonische Doku (hier)

- `00_overview/` (Mission, Problem, Value, Scope Frame, Makerkit Orientierung)
- `01_spec/` (Requirements, PRD, Journeys, Edge Cases)
- `02_system_design/` (Architektur, Datenflüsse, Agents, Worker-Contract Spark↔Supabase)
- `03_roadmap/` (MVP, Milestones, v1/v2/v3, Risiken)
- `04_assets/` (Prompts, Datasets, Diagrams)

## Aktueller Stand (damit neue Chats sofort Kontext haben)

- **Local Dev (Supabase + HD ingestion):** `00_overview/current_status_local_dev.md`
- **Priorität & Reihenfolge (Option B):** `02_system_design/next_steps_was_fehlt_noch.md`
- **Roadmap:** `02_system_design/plan_option_b_roadmap.md`
- **Chat-Handover (Copy-Paste für neue Chats):** `00_overview/chat_handover_hd_saas.md`

Für Implementierung: `interpretations_contract.md`, `text2kg_spec.md`, `dimensions_contract.md`, `layer_implementation_abgleich.md`, Worker-Contracts in `02_system_design/`.

## Code (separates Repo unter `code/`)

- **Code-Repo (working copy)**: `code/hd_saas_app/` (eigenes Git-Repo)

## Infra / Shared Docs

- Spark Serving / Modelle / Endpoints: `infrastructure/spark/`
- Tailscale / VPN: `infrastructure/tailscale/`

## Cursor Setup (wichtig)

Damit die “Code KI” beim Arbeiten im HD‑SaaS Code gleichzeitig Kontext aus `projects/` und `infrastructure/` hat:

- Öffne als Workspace: `ai_projects.code-workspace` (Multi‑Root, 1 Fenster)

