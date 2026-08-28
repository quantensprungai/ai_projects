<!-- Reality Block
last_update: 2026-06-30
status: draft
scope:
  summary: "Konsolidierte Endpoint-Übersicht für Spark-Services (intern/extern), inkl. Health & Example Calls."
  in_scope:
    - endpoint list
    - port mapping (documentation)
    - example curls
    - Cursor Custom Model Setup (Funnel + Bearer)
  out_of_scope:
    - auth/secrets (Token-Werte nie committen)
    - public exposure / firewall rules
notes:
  - "2026-06-30: Cursor Custom Model bestätigt — Bearer + neues Chat-Fenster; Base URL ohne /v1 ok."
-->

# Inference Endpoints (Spark)

## Ziel

Eine einzige Referenz für: **Hostnames/IPs, Ports, URLs** und minimale Test-Calls.

> Model-Assets / Ist-Stand auf Disk: siehe `infrastructure/spark/model_inventory.md`.

## Endpoints (Default)

### SGLang
- **Base URL (Port 30000, optional/secondary)**: `http://<spark-host>:30000`
- **Base URL (Primary Slot, per Switch – z. B. Qwen ↔ DeepSeek R1‑8B BF16)**: `http://<spark-host>:30001`
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

**Bestätigtes Setup (2026-06-30, Funnel + Caddy-Proxy aktiv):**

| Feld | Wert |
|---|---|
| **Base URL** | `https://spark-56d0.tail2d2ae0.ts.net` (ohne `/v1` — bestätigt) oder mit `/v1` |
| **Custom Model** | `qwen3-32b-nvfp4` (exakt wie in `GET /v1/models`) |
| **API Key** | Bearer Token aus `~/ai/configs/caddy/cursor_bearer_token.txt` auf Spark |
| **API Key Toggle** | an |

**Pflicht nach Config-Änderung:** **neues Chat-Fenster** (oder Reload Window). Cursor cached Provider/Model pro Chat — alte Sessions nutzen die alte Config.

**`sk-local` gilt hier nicht:** Tailnet verbunden zu sein reicht nicht. Der Traffic geht über Funnel → Caddy (`:31001`) → SGLang. Caddy verlangt Bearer; `sk-local` liefert `401`.

**Agent-Modus:** Custom Spark-Modelle sind primär für **Chat/Ask**. Im **Agent-Modus** kann Cursor kurz „Planning next moves“ zeigen und dann hängen (Tool-Protokoll nicht voll unterstützt). Für Agent-Arbeit Cursor-eigene Modelle nutzen.

**PowerShell-Schnelltest (Windows):**

```powershell
$token = "DEIN_TOKEN_AUS_SPARK"
Invoke-WebRequest -UseBasicParsing `
  -Uri "https://spark-56d0.tail2d2ae0.ts.net/v1/models" `
  -Headers @{ Authorization = "Bearer $token" } |
  Select-Object StatusCode, Content
```

Erwartet: `200` und `"id":"qwen3-32b-nvfp4"`.

**Base URL — mit oder ohne `/v1`:**

- **Ohne `/v1`:** bei uns bestätigt funktionierend (`https://spark-56d0.tail2d2ae0.ts.net`).
- **Mit `/v1`:** Alternative, wenn „Refresh“ / Model-Liste zickt (`https://<spark>.ts.net/v1`).

- **Model Name**: `qwen3-32b-nvfp4` (oder wie du ihn via `--served-model-name` gesetzt hast)

> Für reine CLI-Tests/`curl` kannst du weiterhin `http://<spark-host>:30001` nutzen. Für Cursor bevorzugen wir HTTPS via Funnel.

**API Key Feld — wann welcher Key:**

- **Funnel + Caddy-Proxy (unser Standard):** Bearer Token aus `cursor_bearer_token.txt` — **Pflicht**.
- **Tailnet-only, direkt SGLang ohne Proxy:** Dummy wie `sk-local` kann reichen (selten bei Cursor wegen SSRF-Block).
- **Internet (Funnel) ohne Auth:** **nicht** — Token am Proxy erzwingen.

### Funnel (Internet) – Security Minimalstandard (Bearer Token Pflicht)

Reality Check aus unserem Setup: Cursor kann `127.0.0.1`/private IPs teils nicht nutzen (SSRF-Block). Mit Funnel klappt’s – aber
Funnel ist öffentlich. Deshalb: Proxy vor SGLang mit Bearer-Token schützen.

- **Token-Datei (auf Spark, nicht committen)**: `~/ai/configs/caddy/cursor_bearer_token.txt`
- **Proxy Configs (auf Spark)**:
  - `~/ai/configs/caddy/cursor-openai-proxy.Caddyfile` (Qwen, `:31001` → `127.0.0.1:30001`)
  - `~/ai/configs/caddy/cursor-openai-proxy-scout.Caddyfile` (Scout, `:31000` → `127.0.0.1:30000`)
- **Container**:
  - `cursor-openai-proxy`
  - `cursor-openai-proxy-scout`

#### Token erzeugen/rotieren

```bash
TOK=$(openssl rand -hex 32)
echo "$TOK" > ~/ai/configs/caddy/cursor_bearer_token.txt
```

#### Caddy: Bearer Token erzwingen (Beispiel, Qwen)

> Wichtig: Caddy v2.7.x hat bei `header Authorization "Bearer ..."` in Matcher-Blöcken in unserem Container gezickt.
> Stabil war `header_regexp` mit Whitespace-Matcher.

```caddyfile
:31001 {
  @authed {
    header_regexp authed Authorization ^Bearer[[:space:]]+<TOKEN>$
  }

  handle @authed {
    # ... reverse_proxy Regeln ...
  }

  respond 401
}
```

Nach Änderungen (weil `/etc/caddy/Caddyfile` read-only gemountet ist): Container neu starten, damit Mount-Inhalt sicher aktiv ist:

```bash
docker restart cursor-openai-proxy cursor-openai-proxy-scout
```

#### Quick Test (muss 401/200 sein)

```bash
# ohne Header -> 401
curl -s -o /dev/null -w '%{http_code}\n' https://<spark>.ts.net/v1/models

# mit Header -> 200
TOK=$(cat ~/ai/configs/caddy/cursor_bearer_token.txt)
curl -s -o /dev/null -w '%{http_code}\n' \
  -H "Authorization: Bearer $TOK" \
  https://<spark>.ts.net/v1/models
```

### Cursor: SSRF-Block / “private IP is blocked”

Wenn Cursor meldet `ssrf_blocked` / “connection to private IP is blocked”, dann versucht Cursor die Model-URL nicht “lokal”
zu erreichen, sondern über einen Provider-/Proxy-Flow. `127.0.0.1` (oder `100.x` Tailnet IPs) werden dann blockiert.

Pragmatischer Fix:
- **Funnel URL** nutzen (z. B. `https://spark-56d0.<tailnet>.ts.net/`)
- **API Key in Cursor** = dein Bearer Token (aus `cursor_bearer_token.txt`)

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

### Wichtiger Reality Check: Config wird pro Chat “gecacht”

Wenn du Base URL / API Key / Model in Cursor änderst, gilt das **nicht** für bereits offene Chats/Agent-Sessions.
Symptome:
- “We're having trouble connecting…” obwohl `/v1/models` via Test **200** liefert
- kurz „Planning next moves“, dann Stille (besonders im Agent-Modus)

**Pflicht-Fix (bestätigt 2026-06-30):**
- **Neues Chat-Fenster** starten (oder Cursor „Reload Window“)
- Custom Model erneut auswählen
- Für Spark: **Chat/Ask**, nicht Agent

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

### Optional: GUI zum Umschalten (Spark Model Switcher)

Wenn du Modelle **visuell auswählen** willst (und die Switch‑Skripte automatisch via SSH ausgeführt werden), nutze:

- Tool: `infrastructure/spark/tools/spark_model_switcher/`
- Es zeigt live `/health` + `/v1/models` für `30001` (Primary) und `30000` (Secondary).
- Es hat Buttons für “Stop Secondary (30000)” und “Stop ALL SGLang”.

Reality Check (Cursor):
- Nach einem Switch (oder nach Änderungen an Base URL / API Key / Model) in Cursor ggf. **neuen Chat öffnen** oder **Reload Window**.

## Ops Cheat Sheet (praktisch)

### Modelle “umschalten” (Qwen ↔ Scout)

Reality Check: parallel große Modelle ist meist RAM/KV‑Cache‑Limit → Switch per Start/Stop.

```bash
# Qwen stoppen
docker stop sglang-qwen-uncensored

# Scout starten (served-model-name: llama4-scout-17b-nvfp4)
bash ~/ai/scripts/serve/sglang_scout_17b.sh

# Check
curl -s http://127.0.0.1:30000/v1/models
```

Analog zurück:

```bash
docker stop sglang-scout 2>/dev/null || true
bash ~/ai/scripts/serve/sglang_qwen_32b.sh
curl -s http://127.0.0.1:30001/v1/models
```

### Cursor: Model-Namen, die wir aktuell nutzen

- Qwen: `qwen3-32b-nvfp4`
- Scout: `llama4-scout-17b-nvfp4`
- DeepSeek R1 8B (abliterated, BF16): `deepseek-r1-8b-abliterated-bf16`
- Llama 3.1 8B: `llama-3.1-8b-instruct`
- Llama 3.2 11B: `llama-3.2-11b-instruct`

### Neues Modell hinzufügen (z. B. “echtes uncensored”, NVFP4/FP8)

Minimaler Flow:
- **1) Model besorgen**: Weights nach `~/ai/models/<vendor>/<model>/` (Speicher + Lizenz beachten)
- **2) Quantization wählen**: siehe `infrastructure/spark/quantizations.md`
  - **FP8 (Default)**: in der Praxis oft der stabilste Sweet Spot auf GB10 (Performance/Qualität/Kompatibilität).
  - **NVFP4/MXFP4 (FP4)**: theoretisch “best” (Blackwell), aber nur dann wirklich schnell, wenn Engine/Kernels den nativen FP4‑Pfad sauber treffen (sonst Fallbacks).
  - **Wichtig**: Viele Community‑“FP8/NVFP4” Repos sind **`compressed-tensors`**. Unser aktuelles SGLang‑Image ist damit (Stand heute) unzuverlässig → lieber NVIDIA‑Playbook/ModelOpt Checkpoints oder plain BF16/FP16.
- **3) Serve Script anpassen**:
  - `--model-path` auf den neuen Pfad
  - `--served-model-name <sauberer_name>` setzen (damit `/v1/models` eine brauchbare ID liefert)
  - passende Flags, z. B. `--quantization modelopt_fp4 --modelopt-quant nvfp4` (siehe `infrastructure/spark/sglang_config.md`)
- **4) Start/Health/Models testen**: `/health`, `/v1/models`, `/v1/chat/completions`
- **5) Cursor: Custom Model Name** = exakt die `id` aus `GET /v1/models`

## Notizen

- “Extern erreichbar” (Tailscale, Reverse Proxy, etc.) wird in `infrastructure/tailscale/` bzw. Networking-Doku beschrieben.
- Wenn du später Auth brauchst: hier nur das Doku-Interface, keine Secrets.

## Reality Check (GB10): wenn “FP8/NVFP4” nicht startet

Wenn ein Download “FP8/NVFP4” im Repo-Namen hat, heißt das nicht automatisch, dass es mit unserem SGLang‑Image lädt.
Der schnellste Diagnose-Schritt ist:

- `config.json` öffnen und `quantization_config.quant_method` prüfen.
  - Bei **`compressed-tensors`**: aktuell häufige Ursache für “kommt nie ready / Scheme not found”.
  - Bei **ModelOpt/NVIDIA NVFP4/FP8** oder **plain BF16/FP16**: deutlich höhere Chance, dass es sofort läuft.


