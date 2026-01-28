<!-- Reality Block
last_update: 2026-01-27
status: draft
scope:
  summary: "Security/Guardrails: was wir erlauben, was nicht, und warum."
  in_scope:
    - threat model (high-level)
    - guardrails and defaults
    - access policies (pairing/allowlist)
  out_of_scope:
    - secrets
    - exhaustive security hardening guide
notes: []
-->

# Security & Guardrails – Bot Platform (Clawdbot)

## Threat Model (kurz)
- Inbound Messages sind **untrusted input** (Prompt‑Injection, Social Engineering).
- Credentials/Service Role Keys sind “God mode” → Blast Radius muss klein bleiben.
- “Computer access” ohne Grenzen ist gefährlich → wir bevorzugen allowlisted Tools.

## Defaults (v1)
- **DM Pairing + Allowlist** (keine offenen DMs standardmäßig).
- **Profiles als Trust Boundaries** (`ops` vs `personal`).
- **Human-in-the-loop** für irreversible Aktionen (restart/switch/requeue/post).

## Tool Policy (Prinzip)
- `ops` Profil: nur eine klar definierte Allowlist (SSH‑Commands, Supabase Ops).
- `personal` Profil: keine Shell/SSH; HA‑API scoped; Learning nur auf Workspace.

## Netzwerk/Exposure
- Gateway UI/WebChat nur **tailnet-only** (Serve), kein Public Funnel in v1.
- Spark Endpoints: wenn öffentlich, dann nur mit echter Auth (Bearer Token am Proxy).

