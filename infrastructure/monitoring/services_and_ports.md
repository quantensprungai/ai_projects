<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "Monitoring/Services Port-Referenz für Homelab (Proxmox/VMs/Spark)."
  in_scope:
    - service list
    - ports reference
    - lan vs tailscale access notes
  out_of_scope:
    - deploying new services
    - secrets
notes:
  - "Quelle: konsolidiert aus Proxmox Masterdocs (Quick Reference + Ports)."
-->

# Monitoring / Services – Ports & Zugriff

## LAN (lokal)

| Dienst | URL |
|---|---|
| Proxmox | `https://192.168.0.50:8006` |
| Portainer | `https://192.168.0.12:9443` |
| Glances | `http://192.168.0.16:61208` |
| Home Assistant | `http://192.168.0.90:8123` |

## Tailscale (remote)

> Tailscale IPs können driften → `tailscale status` ist die Quelle der Wahrheit.

| Dienst | URL |
|---|---|
| Proxmox | `https://100.115.71.71:8006` |
| Portainer | `https://100.124.9.7:9443` |
| Glances | `http://100.83.17.106:61208` |
| Spark GPU (legacy entry) | `http://100.96.115.1:11000` |

## Hinweise

- Spark LLM‑Serving Ports sind dokumentiert in `infrastructure/spark/inference_endpoints.md`.


