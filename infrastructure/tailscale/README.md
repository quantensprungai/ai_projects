# tailscale

<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "Zugriffsschicht: wie VM105/Repo sicher via Tailscale auf Spark/Proxmox/VMs zugreift."
  in_scope:
    - access patterns
    - SSH usage
    - naming conventions (MagicDNS)
  out_of_scope:
    - storing secrets/keys in repo
notes:
  - "Tailscale IPs können sich ändern; 'tailscale status' ist die Quelle der Wahrheit."
-->

VPN/Netzwerkzugang, ACLs, Geräte-Policies, Zugriff auf Spark/VMs.

## Quelle der Wahrheit für Maschinen/IPs

Die detaillierte Tabelle (inkl. historischen IPs) liegt in:

- `infrastructure/proxmox/01_setup/1_proxmox-komplettsetup.md` (Abschnitt Tailscale)
- Zusätzlich (logische Inventory ohne feste IPs): `machines.md`

Da IPs sich ändern können, gilt für den Alltag:

- auf dem Client: `tailscale status`
- im Admin-Panel: Machines / DNS (MagicDNS)

## Empfohlenes Zugriffsmuster (clean)

- **VM105** ist dein Client (Cursor/Tools).
- **Spark** ist Server (Inference).
- Zugriff läuft **immer** über Tailscale (IP oder MagicDNS), nicht über “zufällige” LAN IPs.

Beispiele:
- `ssh sparkuser@spark-56d0` (MagicDNS)
- `ssh sparkuser@100.x.x.x` (Tailscale-IP)

## HTTPS Exposure im Tailnet (für Cursor / “OpenAI-compatible” Endpoints)

Reality Check: Manche Clients (insb. IDEs/Enterprise-Setups) sind bei `http://`/SSE empfindlich oder blocken “unsichere” Base URLs.
Für Cursor↔Spark ist daher unser Standard:

- **Spark** bleibt privat (nur Tailnet)
- **SGLang** bleibt lokal auf Spark (z. B. `127.0.0.1:30001`)
- **Tailscale Serve** stellt eine **HTTPS**‑URL bereit (mit `*.ts.net` Zertifikat), die intern auf den lokalen Port forwarded

### Voraussetzungen (Admin‑Panel)

Wenn auf Spark beim Serve/Cert sowas kommt:
- `Serve is not enabled on your tailnet`
- `Access denied: cert access denied`

dann muss im Tailscale Admin‑Panel (Tailnet Settings) aktiviert sein:
- Serve/Funnel Feature
- HTTPS Certificates
- (optional, je nach Policy) Berechtigung für dein Gerät/User, Zertifikate zu beziehen

### Commands (Spark)

Beispiel: SGLang/Qwen läuft auf `:30001`:

```bash
sudo tailscale serve reset
sudo tailscale serve --bg --yes 30001
tailscale serve status
```

Die Ausgabe von `tailscale serve status` ist die **Source of Truth** für die HTTPS‑URL, die du in Cursor als Base URL eintragen solltest.

### Hinweis: Tailscale als snap (Spark) – Operator/Root erforderlich

Wenn Tailscale auf Spark als **snap** installiert ist, sind `tailscale serve ...` Änderungen oft nur als root erlaubt.
Typische Fehlermeldung:

- `Access denied: serve config denied`

Dann hast du zwei saubere Optionen:

1) **Einmalig Operator setzen** (empfohlen), danach kann `sparkuser` `tailscale serve` ohne sudo:

```bash
sudo tailscale set --operator=sparkuser
tailscale serve --bg --yes 30001
tailscale serve status
```

2) Alternativ immer via Root-Socket (wenn du explizit sein willst):

```bash
sudo tailscale --socket /var/snap/tailscale/common/socket/tailscaled.sock serve --bg --yes 30001
sudo tailscale --socket /var/snap/tailscale/common/socket/tailscaled.sock serve status
```

## SSH (für Remote-Operations)

Ziel: von VM105/WSL2 aus Spark steuern (Start/Stop, Deploy von Configs), ohne dass Repo auf Spark liegen muss.

- systemd start/stop: `sudo systemctl start vllm`
- Logs: `journalctl -u vllm -f`

## Tailscale SSH ACL – Minimalbeispiel (Server via Tag)

Wenn `tailscale ssh ...` oder `ssh user@100.x.y.z` mit **`operation not permitted`** endet, ist das fast immer:
- SSH‑Policy matched nicht, oder
- Tailscale SSH Server ist auf dem Ziel nicht aktiv.

**Empfohlener Minimal‑Rule‑Set** (Spark als `tag:spark`):

```jsonc
{
  "tagOwners": {
    "tag:spark": ["autogroup:admin"]
  },
  "ssh": [
    {
      "action": "accept",
      "src": ["autogroup:member"],
      "dst": ["tag:spark"],
      "users": ["autogroup:nonroot", "root"]
    }
  ]
}
```

**Hinweise:**
- `dst` in `ssh` Rules enthält **nur Hosts/Tags**, keine User‑Strings.
- Auf dem Ziel (Spark) muss Tailscale SSH aktiv sein: `sudo tailscale set --ssh` (oder `sudo tailscale up --ssh`).

## Troubleshooting – SSH

**Client (VM105):**
```powershell
tailscale ping spark-56d0
tailscale whois 100.96.115.1
tailscale ssh sparkuser@spark-56d0 "hostname && whoami"
tailscale debug prefs
```

**Server (Spark):**
```bash
sudo tailscale debug prefs | head -60
sudo snap services tailscale || true
sudo snap logs tailscale -n 200 | tail -120 || true
```

## Hinweis: Tailscale via snap (Spark)

Wenn Spark Tailscale via **snap** nutzt, existiert oft kein `tailscaled.service` unter systemd. Nutze dann:

```bash
sudo snap logs tailscale -n 200
```



