<!-- Reality Block
last_update: 2026-01-27
status: draft
scope:
  summary: "Roadmap/Milestones für Bot Platform (Clawdbot), damit wir unabhängig von Chat-Historie weiterarbeiten können."
  in_scope:
    - milestones
    - acceptance criteria
    - sequencing / dependencies (high-level)
  out_of_scope:
    - exact commands / secrets
    - implementation tasks inside code repos
notes: []
-->

# Roadmap – Bot Platform (Clawdbot)

## Current Status (Snapshot, damit man ohne Chat-Kontext weiterkommt)
Stand: **2026-01-28**

- **VM102**
  - `personal` Gateway läuft **always-on** auf **Port `18789`** und ist per **Tailscale Serve** erreichbar.
  - Control UI/WebChat ist erreichbar; **Device‑Pairing** ist erforderlich (Fix dokumentiert).
  - `health` ist serverseitig **ok**.
- **Docs**
  - Runbook: `infrastructure/docker/clawdbot_vm102.md`
  - Hosting Überblick: `projects/bot_platform/02_system_design/hosting_vm102.md`

## Next Up (konkret)
- **`ops` Profil fertigstellen** (Port `18790`):
  - UI exposure (Serve) + Device‑Pairing + `health` ok
- **Spark als LLM Provider aktiv nutzen**:
  - Provider/Model so konfigurieren, dass ein Chat tatsächlich über Spark läuft (nicht über Default Cloud Provider)
- **1 Channel anbinden** (Telegram als v1-Default):
  - DM Policy `pairing`, Approve‑Workflow, Smoke-Test
- **Guardrails für `ops`**:
  - Tool-/Command‑Allowlist + “human-in-the-loop” für risky Actions
- **Backup konkretisieren & testen**:
  - Welche `~/.clawdbot*` + `~/clawd-*` Pfade werden gesichert, Restore‑Probe

## Prinzipien (damit’s nicht entgleist)
- **Doku zuerst**, dann Setup, dann Tools, dann Automatisierung.
- **Zwei Trust‑Zonen** (Profile) sind Pflicht: `ops` und `personal`.
- Keine “unbounded autonomy”: risky Aktionen brauchen Guardrails + Bestätigung.

## Phase 0 — Doku & Entscheidungen (Done-ish)
**Ziel:** Repo‑Struktur steht, Zuständigkeiten sind klar.

- **Akzeptanzkriterien**
  - Projektstruktur unter `projects/bot_platform/` existiert.
  - Master Map verlinkt das Projekt.
  - Runbook für VM102 existiert (ohne Secrets).

## Phase 1 — Minimum Running System (VM102)
**Ziel:** Clawdbot läuft als Remote Gateway auf VM102 stabil und ist administrierbar.

- **Deliverables**
  - Gateway läuft always-on (Service/Daemon).
  - Zugriff von VM105 (SSH) für Admin.
  - WebChat/Control UI im Tailnet erreichbar (Tailscale Serve, kein Funnel).

- **Akzeptanzkriterien**
  - `health/status/logs` sind von Admin-Seite abrufbar.
  - Persistente State‑Pfade sind bekannt und gesichert (Plan dokumentiert).
  - Erster Zugriff auf Control UI/WebChat ist möglich (inkl. notwendigem Device‑Pairing).

## Phase 2 — Profiles & Baseline Security
**Ziel:** Saubere Trennung ops/personal + sichere Defaults.

- **Deliverables**
  - Profile `ops` und `personal` existieren.
  - DM Pairing/Allowlist ist aktiv (keine offenen DMs).
  - Tool Policy: `ops` allowlisted; `personal` low‑privilege.

- **Akzeptanzkriterien**
  - Ein Test‑DM von “unknown” wird nicht verarbeitet (Pairing greift).
  - `ops` kann keine “personal” Credentials sehen (getrennter State).

## Phase 3 — LLM Backend (Spark) anbinden
**Ziel:** Bots können Spark als OpenAI‑compatible LLM nutzen.

- **Deliverables**
  - Spark Endpoint (HTTPS im Tailnet) als Provider konfiguriert.
  - Mindestens ein Modell erfolgreich genutzt (Chat Completion).

- **Akzeptanzkriterien**
  - Bot kann eine Antwort über Spark generieren.
  - Keine globalen Cursor‑Overrides nötig (Spark‑Setup bleibt separat).
  - Model‑ID entspricht exakt `GET /v1/models` (keine “fantasy model names”).

## Phase 4 — Die 4 Bots (v1) benutzbar machen
**Ziel:** Jeder Bot hat ein klares “Minimum Feature Set”.

### Ops Bot (Profile `ops`)
- **MVP**
  - Spark: Health + /v1/models + “Switch ausführen” (SSH allowlist)
  - Worker Ops: Jobs ansehen + requeue (Supabase service role; allowlist)
- **Akzeptanzkriterien**
  - 1 erfolgreicher Switch + 1 erfolgreicher Job‑Requeue (mit Bestätigung)

### Home Assistant Bot (Profile `personal`)
- **MVP**
  - HA Status + 3–5 Entities/Scenes steuern
- **Akzeptanzkriterien**
  - Eine definierte Szene wird zuverlässig getriggert (mit “are you sure” bei risky Actions)

### Learning Bot (Profile `personal`)
- **MVP**
  - 1 Memory‑Workflow (Notizen → Struktur)
  - 1 Cron‑Job (z. B. daily recap)
- **Akzeptanzkriterien**
  - Cron läuft, produziert Output, ohne Tools außerhalb Workspace zu nutzen

### Project Bot (Test)
- **MVP**
  - Zusammenfassung/Plan/Change‑Request aus Doku
  - Optional: Ticket/Task-Liste generieren (ohne Deploy/Code‑Writes)
- **Akzeptanzkriterien**
  - Kann eine Änderung als “Plan + Files to touch” formulieren, ohne unbounded Tools

## Phase 5 — Stabilität & Betrieb
**Ziel:** Update/Backup/Recovery sind nicht “tribal knowledge”.

- **Deliverables**
  - Backup‑Runbook (State + Workspace) ist konkret und getestet.
  - Update‑Flow ist definiert (Upstream update ohne Tailoring zu verlieren).
  - Monitoring minimal (Logs + Health).

## Optional (später)
- Trading Bot Assistant als Project‑Bot Use‑Case (separate Entscheidung im Trading‑Bot Projekt).
- Voice End-to-End (HA Assist ↔ Bot Routing) als eigener Track.

