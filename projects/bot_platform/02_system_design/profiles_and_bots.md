<!-- Reality Block
last_update: 2026-01-27
status: draft
scope:
  summary: "Profile-/Bot-Schnitt: 2 Trust-Zonen und die initialen Bots (v1)."
  in_scope:
    - profiles (trust zones)
    - bot list + responsibilities
    - high-level tool access rules
  out_of_scope:
    - detailed prompts
    - secrets / tokens
notes: []
-->

# Profiles & Bots – Bot Platform (Clawdbot)

## Prinzip
Wir schneiden nicht “pro Bot ein Server”, sondern **pro Trust‑Zone ein Profil**.

## Profile `ops` (Admin / Multi‑System)
**Zweck:** Betrieb & Orchestrierung (Spark, Worker Ops, Statuschecks).

- **Darf**
  - SSH nach Spark (`2222`) für: Start/Stop/Switch/Health/Logs (allowlisted)
  - Supabase Service Role (nur server-side) für: Job status/requeue (allowlisted)
  - Tailscale Checks (read-only)
- **Darf nicht**
  - “Social posting” / unreviewed outbound actions außerhalb definierter Channels
  - unbounded Shell/Browse (nur allowlisted Tools/Commands)

## Profile `personal` (Alltag / Low Privilege)
**Zweck:** Home Assistant, Learning, Friends/Chat.

- **Darf**
  - Home Assistant API Calls (token, scope über HA “exposed entities”/Policies)
  - Learning: Memory/Notizen/Reminders (lokaler Workspace; später ggf. DB)
  - Chat: DMs nur per Pairing/Allowlist
- **Darf nicht**
  - SSH/Supabase Service Role / Spark Ops

## Bots (v1)

### 1) Ops Bot (Profile `ops`)
- Spark‑Serving verwalten (Model wechseln, Health prüfen)
- Worker‑Ops: Jobs anschauen/retry (Supabase)
- “Morning brief” (optional): Status Spark/VM102/Jobs

### 2) Home Assistant Bot (Profile `personal`)
- Steuerung von HA‑Entities/Scenes
- Später optional: Voice-Frontend via HA Assist (separates Thema)

### 3) Learning Bot (Profile `personal`)
- Lernpläne/Spaced repetition (Cron)
- Wissensbasis im Workspace (Memory‑Files), später optional DB/Embeddings

### 4) Project Bot (Test) (Profile `personal` oder eigenes Agent‑Binding)
- “Projekt‑Support” (Zusammenfassungen, TODOs, Doku‑Hilfe)
- Für Coding Workflows: **nicht** “Cline fernsteuern”, sondern klarer Trigger:
  - Bot erzeugt ein Ticket/Plan/Change‑Request
  - Umsetzung passiert im jeweiligen `code/<repo>` (Cursor/Cline), oder später via separatem CI/Runner

## Optional (später): Trading Bot Assistant
Falls wir im Trading Bot einen Agent‑Support wollen, ist das ein **Project Bot** Use‑Case:
- Doku/Analyse/Backtests orchestrieren
- Risk/Execution Regeln prüfen (human-in-the-loop)
- Umsetzung/Code-Änderungen bleiben im Trading‑Bot Code‑Repo (kein unbounded “Bot macht Deploy”).

