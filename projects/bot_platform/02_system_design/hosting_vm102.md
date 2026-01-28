<!-- Reality Block
last_update: 2026-01-28
status: draft
scope:
  summary: "Hosting/Runbook (high-level) für Clawdbot Gateway auf VM102."
  in_scope:
    - hosting choices
    - state locations to backup
    - access patterns (Tailscale/SSH)
  out_of_scope:
    - exact commands / secrets
notes: []
-->

# Hosting – VM102 (Clawdbot Gateway)

## Ziel
Clawdbot läuft **always-on** als Remote Gateway auf **VM102 (`docker-apps`)**.

## Install/Runtime (Prinzip)
- Runtime: Node.js ≥ 22
- Optional Docker für Sandbox/Isolation
- Betrieb als Daemon/Service (keine “nur im Terminal offen” Installation)

## State (Backup-relevant)
Auf dem Gateway Host liegen die wichtigen Daten:
- `~/.clawdbot/clawdbot.json` (Konfig)
- `~/.clawdbot/credentials/` (Channel/Auth)
- `~/.clawdbot/agents/<agentId>/...` (Sessions/Agent State)
- Workspace (default): `~/clawd` (Skills/Memory/Prompts)

> Wichtig: Diese Pfade sind **nicht** Repo‑Inhalt. Backups müssen infrastrukturseitig passieren.

## Zugriff/Interfaces
- **Admin**: VM105 → SSH → VM102 (CLI, Logs, Updates)
- **User**:
  - Chat Surfaces (Telegram/Signal/…)
  - Control UI/WebChat: bevorzugt **Tailscale Serve** (tailnet-only HTTPS)

> Hinweis: Beim ersten Zugriff der Web‑UI von einem neuen Browser/Device ist **Device‑Pairing** nötig. Symptom ist häufig `Disconnected (1008): pairing required`. Fix/Runbook: `infrastructure/docker/clawdbot_vm102.md`.

## Tailscale Serve + Always-on (VM102, verified)
Damit die Clawdbot Gateways als **systemd user services** auch nach Logout/Reboot laufen und die UI tailnet-only erreichbar ist:

- **Systemd lingering** (einmalig):
  - `sudo loginctl enable-linger user`
- **Tailscale operator** (einmalig, damit `user` Serve ändern darf):
  - `sudo tailscale set --operator=user`
- **Serve UI** (Beispiel: `personal` auf `18789`):
  - `tailscale serve --bg --yes 18789`

> Details/Runbook: `infrastructure/docker/clawdbot_vm102.md`

## Profiles als Separation
- Mindestens zwei Profile: `ops`, `personal`
- Je Profil: eigener State‑Root (`~/.clawdbot-<profile>`), eigener Gateway Port (falls parallel)

