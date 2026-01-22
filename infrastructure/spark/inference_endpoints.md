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
- **Base URL (Port 30000, optional/secondary)**: `http://<spark-host>:30000`
- **Base URL (Qwen3‑32B NVFP4 “uncensored”, current default)**: `http://<spark-host>:30001`
- **Health**: `GET /health`

```bash
curl http://<spark-host>:30000/health
curl http://<spark-host>:30001/health
```

#### SGLang – OpenAI-kompatibel (praktisch für Apps/Tools)

Viele Clients (Cursor/OpenWebUI/SDKs) erwarten OpenAI‑Endpoints. SGLang kann diese anbieten:

- **Models**: `GET /v1/models`
- **Chat**: `POST /v1/chat/completions`

```bash
curl http://<spark-host>:30000/v1/models

curl http://<spark-host>:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"local","messages":[{"role":"user","content":"Hallo"}]}'
```

## Cursor Integration (wichtig: Cursor-Modelle nicht “kaputt-konfigurieren”)

Reality Check: Wenn du in Cursor **global** “OpenAI API Key aktivierst” und gleichzeitig “Override OpenAI Base URL” setzt,
route’t Cursor damit oft **auch seine eigenen Cursor-Modelle** (z. B. GPT‑5.2) auf diese Base URL.
Dann kommt `Unauthorized`/`Invalid API key`, weil Spark keine Cursor‑Auth versteht.

**Empfehlung:**
- Cursor‑eigene Modelle (GPT‑5.2 etc.) weiter normal nutzen (kein Override auf deren Traffic).
- Spark‑Modelle als **separater OpenAI‑kompatibler Endpoint** anbinden (falls Cursor das als “Custom/OpenAI-Compatible Provider” anbietet).

**Wenn du im UI nur diesen einen Override‑Schalter hast (Workaround):**
- Für Cursor‑GPT‑5.2: Override **aus** (sonst geht GPT‑5.2 kaputt).
- Für Spark‑Tests: Override **temporär an**, danach wieder **aus**.

### Base URL Empfehlung (robust: HTTPS via Tailscale Serve)

Reality Check aus unserem Debugging: Wenn Cursor beim “Refresh” **keine** Requests an `GET /v1/models` auf Spark schickt,
ist es oft ein Client-/Network-Stack Thema (z. B. `http://` wird blockiert/abgelehnt, Proxy/VPN-Middleware, etc.).

Unser stabilster Pfad ist daher: **Spark per HTTPS innerhalb des Tailnets exponieren** und Cursor nur auf diese HTTPS‑URL zeigen lassen.

#### 1) Admin-Panel (Tailnet) – einmalig

Wenn du Fehler siehst wie:
- `Serve is not enabled on your tailnet`
- `Access denied: cert access denied`

dann muss im Tailscale Admin‑Panel (Tailnet Settings) Folgendes erlaubt sein:
- Serve/Funnel Features aktiviert
- HTTPS Certificates erlaubt
- (falls nötig) deinem Gerät/User die Berechtigung geben, Zertifikate für `*.ts.net` zu beziehen

#### 2) Auf Spark (Beispiel: Qwen auf Port 30001) – einmalig/bei Änderungen

```bash
sudo tailscale serve reset
sudo tailscale serve --bg --yes 30001
tailscale serve status
```

Ergebnis: du bekommst eine **HTTPS**‑URL im Tailnet (typisch `https://spark-56d0.<tailnet>.ts.net`), die intern auf `http://127.0.0.1:30001` forwarded.

#### 3) Cursor Settings (Spark Provider)

- **Base URL**: nutze die **HTTPS**‑URL von `tailscale serve status`.
  - Manche Cursor‑Builds erwarten hier **explizit** ein Suffix `/v1` (dann wird intern `GET /models` → effektiv `GET /v1/models`).
  - Wenn du **ohne** `/v1` einträgst, kann Cursor `GET /models` callen → das ist bei SGLang typischerweise **404**.
  - Deshalb, wenn bei “Refresh” **no models available** kommt, setze die Base URL auf: `https://<spark>.ts.net/v1`
- **Model Name**: `qwen3-32b-nvfp4` (oder wie du ihn via `--served-model-name` gesetzt hast)
- **API Key**: falls Cursor eins verlangt, Dummy wie `sk-local`

> Für reine CLI-Tests/`curl` kannst du weiterhin `http://<spark-host>:30001` nutzen. Für Cursor bevorzugen wir HTTPS.

**API Key Feld (wenn Cursor eins verlangt):**
- Oft reicht ein Dummy wie `sk-local` (Spark validiert standardmäßig keinen Key).

### vLLM (OpenAI compatible)
- **Base URL**: `http://<spark-host>:8000`
- **Chat Completions**: `POST /v1/chat/completions`

```bash
curl http://<spark-host>:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"local","messages":[{"role":"user","content":"Hallo"}]}'
```

> Hinweis (Reality Check): vLLM ist auf unserem Spark/GB10 aktuell **nicht stabil** (Toolchain/`ptxas`/SM-Arch).  
> Daher ist **SGLang** unser Primary. vLLM später wieder aktivieren mit einem GB10‑kompatiblen Image (nicht `latest`).

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

### SSH Admin-Zugriff (robust)

Wir nutzen zusätzlich klassisches OpenSSH auf Spark, da Tailscale SSH je nach Installationsart (snap confinement) “operation not permitted” verursachen kann.

- **SSHD Port (Spark)**: `2222`
- **Test (von VM105)**:

```powershell
ssh -p 2222 sparkuser@<spark-ts-ip> whoami
```

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

## Cursor Workaround (wenn “No models available” trotz funktionierendem `/v1/models`)

Reality Check aus unserem Setup: Cursor kann den Endpoint **nutzen**, zeigt aber im Settings‑Screen oft trotzdem dauerhaft
`No models available` (auch nach Refresh). Das ist dann meist nur UI/Caching/Provider‑Flow – nicht dein Server.

**Pragmatischer Weg:**

- **Custom Model manuell hinzufügen** (über “Add Custom Model”)
- **Model Name** = exakt die `id` aus `GET /v1/models`
- Wenn “Refresh” in Cursor nichts anzeigt, ist das ok – entscheidend ist, ob Chat funktioniert.

### Stabiler Pfad für Cursor: lokale Port‑Forwards (SSH)

Wenn Cursor `*.ts.net`/HTTPS/Proxy‑Pfad nicht zuverlässig nutzt, ist der stabilste Workaround:
du forwardest die Spark‑Ports lokal und verwendest `http://127.0.0.1:<port>` in Cursor.

Beispiel (VM105/Windows PowerShell):

```powershell
# Qwen-Proxy (Spark:31001 -> lokal:18001)
ssh -N -L 18001:127.0.0.1:31001 -p 2222 sparkuser@100.96.115.1

# Scout-Proxy (Spark:31000 -> lokal:18000)
ssh -N -L 18000:127.0.0.1:31000 -p 2222 sparkuser@100.96.115.1
```

Dann in Cursor:
- **Qwen Base URL**: `http://127.0.0.1:18001`  → Model: `qwen3-32b-nvfp4`
- **Scout Base URL**: `http://127.0.0.1:18000` → Model: `llama4-scout-17b-nvfp4`

### Minimaler “Switch”-Workflow (praktisch)

1. Entscheide: welches Modell läuft “always-on”?
2. Lege **ein** systemd Service als Default fest.
3. Alles andere läuft **on-demand** (start/stop).

## Notizen

- “Extern erreichbar” (Tailscale, Reverse Proxy, etc.) wird in `infrastructure/tailscale/` bzw. Networking-Doku beschrieben.
- Wenn du später Auth brauchst: hier nur das Doku-Interface, keine Secrets.


