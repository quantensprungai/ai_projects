<!-- Reality Block
last_update: 2026-01-27
status: draft
scope:
  summary: "Architektur: Clawdbot im Multi‑System (VM102 Gateway, Spark LLM, CT110 HA)."
  in_scope:
    - components
    - boundaries
    - interfaces (high-level)
  out_of_scope:
    - low-level implementation
notes: []
-->

# Architecture – Bot Platform (Clawdbot)

## Komponenten (high level)

- **VM102 (`docker-apps`) – Clawdbot Gateway**
  - Control Plane: Sessions, Channels, Tools, Cron/Webhooks, WebChat/Control UI
  - Persistenter State: `~/.clawdbot*` + `~/clawd*` (Workspace)

- **Spark (`spark-56d0`) – LLM Serving**
  - SGLang (OpenAI‑kompatibel): `/v1/models`, `/v1/chat/completions`
  - Zugriff via Tailscale (idealerweise HTTPS via `tailscale serve`)

- **CT110 – Home Assistant**
  - Smart‑Home Runtime
  - Bot greift per HA API zu (Token; keine Installation von Clawdbot in CT110)

- **Supabase (Cloud) – Control Plane für Jobs (z. B. HD Worker)**
  - Service Role nur im `ops`‑Profil (server-side)

## Interfaces

- **VM102 → Spark**: OpenAI‑compatible HTTP (Base URL nach `infrastructure/spark/inference_endpoints.md`)
- **VM102 → Spark (Ops)**: SSH `2222` für Start/Stop/Switch/Health (nur `ops` Profil)
- **VM102 → Home Assistant (CT110)**: HA REST/Conversation APIs (nur `personal` Profil oder eigener Bot)
- **VM105 → VM102**: SSH Admin (Setup, Updates, Logs)

## Trust Boundaries (kurz)

- **Profiles sind Trust‑Zonen**:
  - `ops` darf riskante Tools (SSH, Supabase service role).
  - `personal` ist für Alltag/Chat/HA/Lernen und bleibt “low privilege”.

