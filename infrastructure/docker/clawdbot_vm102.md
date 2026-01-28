<!-- Reality Block
last_update: 2026-01-28
status: draft
scope:
  summary: "Runbook für Clawdbot auf VM102 (docker-apps): offizieller Install-Flow + Anpassungen für unser Tailnet/Spark-Setup."
  in_scope:
    - hosting/runbook documentation
    - installation flow (official, with placeholders)
    - backup-relevant paths
    - access patterns (Tailscale/SSH)
  out_of_scope:
    - secrets/tokens
    - deep hardening (beyond basics)
notes: []
-->

# Clawdbot auf VM102 (docker-apps) – Runbook

## Ziel
Clawdbot läuft **always-on** auf **VM102** als Remote‑Gateway (Control Plane). LLM‑Compute läuft auf **Spark**.

Verwandte Projektdoku:
- `projects/bot_platform/README.md`

## Architektur (kurz)
- **VM102**: Clawdbot Gateway + Channels + Tools + WebChat/Control UI
- **Spark**: OpenAI‑kompatibles LLM‑Backend (SGLang)
- **CT110**: Home Assistant Runtime (Bot greift remote zu)

## Zugriff
- **Admin (VM105 → VM102)**: SSH (Setup, Logs, Updates)
- **User**:
  - Chat Surfaces (Telegram/Signal/…)
  - WebChat/Control UI (bevorzugt Tailnet‑only via Tailscale Serve)

## Offizieller Installationspfad (Linux, empfohlen)
Quellen:
- `https://docs.clawd.bot/start/setup`
- `https://docs.clawd.bot/install/installer`
- `https://docs.clawd.bot/platforms/linux`

### Prereqs
- **Node.js ≥ 22** (Gateway Runtime; Bun ist laut Docs *nicht empfohlen* für Gateway wegen WhatsApp/Telegram Bugs)
- **Git** (für manche Installwege / um `spawn git ENOENT` zu vermeiden)
- **Tailscale** auf VM102 installiert + eingeloggt (wenn wir Serve nutzen)

### Install (Installer Script, “recommended”)
Die Docs nennen ein Install-Skript, das Node 22+ sicherstellt und typische npm‑Prefix/EACCES‑Footguns mitigiert:

```bash
curl -fsSL https://clawd.bot/install.sh | bash
```

Tipp: Help/Flags anzeigen:

```bash
curl -fsSL https://clawd.bot/install.sh | bash -s -- --help
```

Alternative (ohne Installer Script, direkt via npm):

```bash
npm install -g clawdbot@latest
```

> Hinweis: In manchen Docs/Seiten heißt das Binary `moltbot`. Praktisch: nach der Installation prüfen, ob `clawdbot` oder `moltbot` verfügbar ist.

### Onboarding/Wizard + Daemon
Offizieller Quickstart (Wizard + Gateway als Daemon):

```bash
clawdbot onboard --install-daemon
```

Alternative laut Linux Docs:

```bash
clawdbot gateway install
```

### Always-on: systemd user service vs system service
Die Linux Setup Docs erwähnen: Default ist ein **systemd user service**; für Always‑On auf Servern muss ggf. “lingering” an:

```bash
sudo loginctl enable-linger $USER
```

Wenn du lieber explizit bist (und damit unabhängig von User-Logins), nutze eine systemd **system** service (siehe Gateway Runbook upstream). In v1 reicht user+lingering.

## Unser Setting (VM102): Remote Gateway, loopback + Tailnet-only UI
Quellen:
- Remote Guide: `https://docs.clawd.bot/gateway/remote`
- Tailscale Guide: `https://docs.clawd.bot/gateway/tailscale`

### Empfehlung
- Gateway bind bleibt **loopback** (sicherster Default).
- Control UI/WebChat wird **tailnet-only** via **Tailscale Serve** exponiert (HTTPS).

Konfig-Beispiel aus den Tailscale Docs:

```js
{
  gateway: {
    bind: "loopback",
    tailscale: { mode: "serve" }
  }
}
```

CLI‑Beispiel aus den Tailscale Docs (runtime):

```bash
clawdbot gateway --tailscale serve
```

> Security note: In Serve‑Mode können Requests (optional) über Tailscale Identity Headers authen, wenn `gateway.auth.allowTailscale` true ist. Wenn wir strikt Token/Passwort erzwingen wollen: `gateway.auth.allowTailscale: false` setzen.

### VM102-Pragmatik: Tailscale Serve braucht Root oder Operator
Wenn `tailscale serve ...` als normaler User scheitert mit `Access denied: serve config denied`, ist das normal.
Offizieller Hinweis von Tailscale/CLI:

```bash
# einmalig (als root) – danach darf "user" tailscale serve ändern
sudo tailscale set --operator=$USER
```

Alternativ (ohne Operator): `sudo tailscale serve ...` nutzen.

### Status in unserem Setup (verified)
Auf VM102 ist das bereits gesetzt/ausgeführt:

```bash
sudo loginctl enable-linger user
sudo tailscale set --operator=user
```

Und das Gateway `personal` (Port `18789`) ist via Tailnet HTTPS exposed:

```bash
tailscale serve --bg --yes 18789
tailscale serve status
```

Erwartung (Beispiel-Ausgabe):
- Tailnet URL wie `https://docker-apps.<tailnet>.ts.net/`
- Proxy auf `http://127.0.0.1:18789`

### Troubleshooting: Web UI “Disconnected (1008): pairing required”
**Symptom:** In der Control UI/WebChat siehst du “Disconnected from gateway” und/oder `disconnected (1008): pairing required` (häufig zusammen mit “health offline” in der UI).

**Ursache:** Die Web‑UI ist ein **Device** (z. B. `clawdbot-control-ui`) und muss beim ersten Zugriff **explizit gepairt** werden (Owner Approval).
Das passiert **pro Profil/Gateway** (also z. B. separat für `personal`/`ops`) und **pro Browser/Device**.

**Fix (auf VM102, pro Profil):**

```bash
# pending/paired Devices anzeigen
~/.clawdbot/bin/clawdbot --profile personal devices list --json

# pending request approve (requestId aus der Liste)
~/.clawdbot/bin/clawdbot --profile personal devices approve <requestId>
```

Danach im Browser:
- Tab **neu laden** (oder schließen/neu öffnen)

**Hinweise:**
- `requestId` ist kurzlebig. Wenn “unknown requestId” kommt: UI neu laden → neue pending request erzeugen → erneut approve.
- Wenn du ein anderes Profil (z. B. `ops`) per UI öffnest, musst du es dort analog pairen.

### Hinweis: “Proxy headers detected from untrusted address” (bei Tailscale Serve)
Bei Zugriff über **Tailscale Serve** siehst du ggf. Gateway‑Logs wie:
- `Proxy headers detected from untrusted address ... Configure gateway.trustedProxies ...`

Das ist ein Hinweis, dass Reverse‑Proxy‑Header (Serve) nicht als “trusted” markiert sind.
Für v1 ist das **nicht blockierend**; wir lassen das bewusst als Warnung stehen, bis wir entscheiden, ob wir `gateway.trustedProxies` setzen wollen.

### Fallback: Remote Admin via SSH tunnel (VM105 → VM102)
Offizieller Flow aus “Remote” Docs:

```bash
ssh -N -L 18789:127.0.0.1:18789 <user>@<vm102-host>
```

Dann ist die UI lokal erreichbar unter:
- `http://127.0.0.1:18789/`

## Profiles (ops/personal) als Trust-Zonen
Prinzip: zwei getrennte State‑Roots, ggf. zwei Gateway‑Ports.

Beispiel (konzeptionell; Ports sind frei wählbar):
- `personal`: Port `18789`
- `ops`: Port `18790`

Wizard pro Profil:

```bash
clawdbot --profile personal onboard --install-daemon --gateway-port 18789
clawdbot --profile ops onboard --install-daemon --gateway-port 18790
```

## Channel Setup (Beispiel: Telegram, ohne öffentliche Webhooks)
Quelle: `https://docs.clawd.bot/channels/telegram`

Telegram ist “production-ready” und nutzt **Long‑Polling by default** (kein Public URL nötig).

Minimaler Setup (Docs):
- Token per Env `TELEGRAM_BOT_TOKEN=...` (default account) oder per config `channels.telegram.botToken`.
- DM Policy default `pairing` (empfohlen).

Beispiel-Konfig aus den Telegram Docs:

```js
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "123:abc",
      dmPolicy: "pairing"
    }
  }
}
```

Pairing Approve (Docs):

```bash
clawdbot pairing list telegram
clawdbot pairing approve telegram <CODE>
```

## Persistenter State (Backup!)
Diese Pfade sind die **Source of Truth** für Konfiguration, Credentials und Memory (auf VM102):
- `~/.clawdbot/clawdbot.json` (Konfiguration)
- `~/.clawdbot/credentials/` (Channel/Auth)
- `~/.clawdbot/agents/<agentId>/...` (Sessions/Agent State)
- Workspace (default): `~/clawd` (Skills/Memory/Prompts)

Wenn wir mehrere Trust‑Zonen als Profile fahren:
- zusätzliche State Roots: `~/.clawdbot-ops`, `~/.clawdbot-personal` (Beispiel)

## Netzwerk / Security Defaults
- Kein Public Exposure als Default (kein Funnel in v1).
- Chat DMs: Pairing + Allowlist (kein “open DM”).
- Trennung risky Ops (`ops` Profil) vs Alltag (`personal` Profil) – siehe `projects/bot_platform/02_system_design/security_and_guardrails.md`.

## Spark Integration (LLM)
Source of Truth:
- `infrastructure/spark/inference_endpoints.md`

Prinzip:
- VM102 nutzt Spark als OpenAI‑compatible Endpoint (idealerweise HTTPS im Tailnet).

### Runbook: Spark als OpenAI‑compatible Provider (für Clawdbot)
**Ziel:** Clawdbot soll für LLM‑Calls Spark/SGLang nutzen, ohne dass wir uns auf “private IP HTTP” Footguns verlassen.

**Empfohlenes Pattern (analog zu unserer Cursor↔Spark Doku):**
- Spark per **Tailscale Serve** als **HTTPS** im Tailnet bereitstellen.
- In Clawdbot die Base URL so setzen, dass OpenAI‑Clients zuverlässig `/v1/...` treffen.

**Base URL Faustregel:**
- Wenn ein Client “Base URL” erwartet und dann selbst `/v1/chat/completions` anhängt, muss die Base URL **ohne** `/v1` sein.
- Wenn ein Client intern `/models` statt `/v1/models` nutzt, brauchst du ggf. explizit `/v1` in der Base URL.

Für Spark ist die sichere Quelle der Wahrheit:
- `GET /v1/models` (muss funktionieren)

Beispiel‑Checks (von VM102 aus):

```bash
curl -sf https://<spark-magicdns>/v1/models
curl -sf https://<spark-magicdns>/health
```

> Wenn ihr statt Serve direkt `http://100.x.x.x:30001` nutzt und etwas “zickt” (SSE/HTTP/Client‑Policy): zurück auf HTTPS‑Serve wechseln.

**Welche Modell-ID nutzt Clawdbot?**
- Genau die `id` aus `GET /v1/models` (bei uns z. B. `qwen3-32b-nvfp4`, `llama4-scout-17b-nvfp4`, …).
- Der Name hängt an `--served-model-name` im SGLang‑Startscript (siehe Spark‑Doku).

**Security‑Hinweis (wichtig):**
- Wenn Spark via Funnel/public erreichbar wäre: niemals “Dummy-Key”. Dann muss ein echter Bearer‑Token/Proxy davor (siehe `infrastructure/spark/inference_endpoints.md`).

## Update-Strategie (Prinzip)
- Clawdbot Upstream wird **nicht** in dieses Repo vendored.
- Änderungen/Customizations leben außerhalb (Workspace/Config auf VM102).
- Updates dürfen die Customizations nicht überschreiben (Repo‑Pattern: “tailoring lives outside”).

## Alternative: Vollständig containerisiertes Gateway (Docker Compose)
Quelle: `https://docs.clawd.bot/install/docker`

Docker ist laut Docs **optional**. Vorteil: throwaway/isoliert; Nachteil: mehr Moving Parts.

Offizieller Quickstart (aus upstream repo root):

```bash
./docker-setup.sh
```

Manueller Flow (Docs):

```bash
docker build -t moltbot:local -f Dockerfile .
docker compose run --rm moltbot-cli onboard
docker compose up -d moltbot-gateway
```

Hinweis: Auch im Docker-Flow schreibt Clawdbot Config/Workspace auf den Host:
- `~/.clawdbot/`
- `~/clawd`

