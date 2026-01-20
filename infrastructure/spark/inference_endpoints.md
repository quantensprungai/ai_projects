<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "Konsolidierte Endpoint-Übersicht für Spark-Services (intern/extern), inkl. Health & Example Calls."
  in_scope:
    - endpoint list
    - port mapping (documentation)
    - example curls
  out_of_scope:
    - auth/secrets
    - public exposure / firewall rules
notes: []
-->

# Inference Endpoints (Spark)

## Ziel

Eine einzige Referenz für: **Hostnames/IPs, Ports, URLs** und minimale Test-Calls.

## Endpoints (Default)

### SGLang
- **Base URL**: `http://<spark-host>:30000`
- **Health**: `GET /health`

```bash
curl http://<spark-host>:30000/health
```

### vLLM (OpenAI compatible)
- **Base URL**: `http://<spark-host>:8000`
- **Chat Completions**: `POST /v1/chat/completions`

```bash
curl http://<spark-host>:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"local","messages":[{"role":"user","content":"Hallo"}]}'
```

### Ollama (Fallback, wenn Open WebUI schnell “online” muss)
- **Base URL**: `http://<spark-host>:11434`

```bash
curl http://<spark-host>:11434/api/tags
```

## Zugriff & Steuerung (VM105 / Tailscale / OpenWebUI)

### Zugriffspfade (empfohlen)

- **VM105 (dein Dev-PC/Workspace)** ist der Client:
  - Cursor/Tools/Projekte senden Requests an Spark (über Tailscale oder LAN).
- **Spark** hostet nur Inferenz (SGLang/vLLM).
- **OpenWebUI**:
  - Entweder auf Spark (optional) oder besser auf einer VM (z. B. VM105/VM102), die über Tailscale Spark erreicht.

### Tailscale (typisch “Enterprise‑sauber”)

- Spark bekommt eine Tailscale-IP (`100.x.x.x`) oder MagicDNS Name.
- Du nutzt in Projekten **immer** die Tailscale-Adresse (stabiler als LAN).

Beispiel:
- `http://spark-56d0:8000` (MagicDNS) oder `http://100.xx.xx.xx:8000`

### Steuerung: “welches Modell ist aktiv?”

Wichtig: **der Port gehört zum laufenden Server**, nicht zum Projekt.

Du hast zwei saubere Optionen:

1. **Ein Default‑Endpoint** (Port bleibt gleich), Modell wird durch Start/Stop gewechselt:
   - `systemctl stop vllm` → Modelpfad ändern → `systemctl start vllm`
   - Alle Projekte nutzen weiter `http://spark:8000`

2. **Mehrere Endpoints** (mehrere Ports), je Modell ein eigener Service:
   - z. B. `vllm-scout.service` auf `8000`, `vllm-deepseek.service` auf `8001`
   - Nur sinnvoll, wenn Memory reicht (oft nicht für mehrere “große” Modelle parallel).

### Minimaler “Switch”-Workflow (praktisch)

1. Entscheide: welches Modell läuft “always-on”?
2. Lege **ein** systemd Service als Default fest.
3. Alles andere läuft **on-demand** (start/stop).

## Notizen

- “Extern erreichbar” (Tailscale, Reverse Proxy, etc.) wird in `infrastructure/tailscale/` bzw. Networking-Doku beschrieben.
- Wenn du später Auth brauchst: hier nur das Doku-Interface, keine Secrets.


