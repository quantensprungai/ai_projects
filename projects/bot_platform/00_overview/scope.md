<!-- Reality Block
last_update: 2026-01-27
status: draft
scope:
  summary: "Scope (v1) für Bot Platform (Clawdbot): was wir jetzt bauen/dokumentieren vs. später."
  in_scope:
    - in/out of scope list
    - assumptions
  out_of_scope:
    - detailed implementation
notes: []
-->

# Scope – Bot Platform (Clawdbot)

## In Scope (v1)
- Clawdbot als **remote Gateway auf VM102** (Always‑On).
- Zwei Trust‑Zonen als **Profiles**:
  - `ops`: Multi‑System/Ops (Spark via SSH, Supabase Service Role für Worker Ops)
  - `personal`: Home Assistant + Learning + Friends/Chat
- 4 Bots als dokumentierte Use‑Cases inkl. minimaler Konfiguration/Guardrails:
  - Ops Bot
  - Home Assistant Bot
  - Learning Bot
  - Project Bot (Test‑Bot für ein Projekt; HD‑SaaS als eigenes Thema später)
- Zugriff/Steuerung über:
  - Chat Surface (noch offen: Telegram/Signal/…)
  - Control UI/WebChat (tailnet-only via Tailscale Serve)
  - CLI (admin via SSH von VM105)

## Out of Scope (v1)
- Vollständige In‑App Integration in HD‑SaaS (separat).
- Voice “end-to-end” (Wake word, Room routing, etc.) als Produktfeature.
- “Full computer access” ohne Allowlist (keine unbounded Shell‑/Browser‑Autonomie).
- Upstream‑Fork/Spiegelung des Clawdbot‑Repos in `code/`.

## Annahmen
- VM102 ist der primäre Host für Docker‑Utilities und kann Always‑On Dienste tragen.
- Spark bleibt Inference‑Server; Bot‑LLM Calls gehen über die dokumentierten Endpoints.

