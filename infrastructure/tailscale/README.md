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



