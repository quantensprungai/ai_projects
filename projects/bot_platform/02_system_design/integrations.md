<!-- Reality Block
last_update: 2026-01-27
status: draft
scope:
  summary: "Integrationen: Spark (LLM), Home Assistant, Supabase (ops) und Projekt-Bots."
  in_scope:
    - integrations list (high-level)
    - auth approach (high-level)
    - boundaries and constraints
  out_of_scope:
    - secrets
    - full config dumps
notes: []
-->

# Integrations – Bot Platform (Clawdbot)

## Spark (LLM Serving)
- Clawdbot nutzt Spark als **OpenAI‑kompatibles Backend** (SGLang).
- Source of Truth: `infrastructure/spark/inference_endpoints.md`
- Empfehlung: HTTPS im Tailnet (Tailscale Serve), um Client/HTTP‑Footguns zu vermeiden.

## Home Assistant (CT110)
- Zugriff über HA APIs (Bearer Token; minimal scope).
- Clawdbot läuft **nicht** in CT110, sondern ruft HA remote auf.
- Voice: optional über HA Assist als eigenes Frontend (später).

## Supabase (Ops / Control Plane)
- Nur im Profil `ops`:
  - Service Role Key server-side (niemals Frontend)
  - Use Cases: Worker job status, requeue/retry (vgl. `infrastructure/spark/hd_worker_ops.md`)

## Projekt-Bots (z. B. Trading Bot)
Clawdbot kann als “Projekt‑Bot” helfen bei:
- Doku/Status/Backlog‑Pflege
- Research + Zusammenfassungen
- “Change Request” erzeugen (Plan/PRD/ADR-lite)

Wichtig: Code‑Änderungen passieren im jeweiligen `code/<repo>` (Cursor/Cline). Der Bot sollte in v1 **nicht** Deploys “blind” ausführen.

