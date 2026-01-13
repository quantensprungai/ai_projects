<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "Maschinen-Übersicht (Namen/Rollen) + Hinweis zur dynamischen IP-Auflösung über tailscale status."
  in_scope:
    - machine inventory (names/roles)
    - pointers to how to get current IPs
  out_of_scope:
    - secrets
notes:
  - "Tailscale IPs können driften; verwende tailscale status als Quelle der Wahrheit."
-->

# Tailscale Machines (Inventory)

## Aktuelle Rollen (logisch)

| Maschine | Rolle |
|---|---|
| `pve` | Proxmox Host |
| `management` | VM101 (RustDesk, Portainer, Tailscale) |
| `docker-apps` | VM102 (Docker Host / Downloader) |
| `win11pro105` | VM105 (Dev/WSL2) |
| `spark-56d0` | Spark GPU Server |

## IPs (Quelle der Wahrheit)

IPs können sich ändern. Nutze:

```bash
tailscale status
```

oder das Admin-Panel (Machines).


