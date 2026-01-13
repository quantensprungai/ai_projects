<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "RustDesk Betrieb & Troubleshooting (Homelab)."
  in_scope:
    - ports
    - container setup notes
    - troubleshooting checklist
  out_of_scope:
    - exposing services to the public internet
    - secrets/keys
notes:
  - "Quelle: Proxmox Setup (VM101) + Proxmox Erweiterte Anleitung (RustDesk Sektion)."
-->

# RustDesk (Homelab)

## Ports & Dienste

RustDesk benötigt typischerweise:
- TCP `21115–21119` (Client Kommunikation)
- UDP `21116`
- `hbbs` = Broker, `hbbr` = Relay

## Logs / Checks

```bash
ss -tulpn | grep -E '21115|21116|21117|21118|21119'
docker logs hbbr
docker logs hbbs
```

## Keys

```bash
cat /opt/rustdesk/data/id_ed25519.pub
```

## NAT Loopback (falls nötig)

Wenn dein Router NAT‑Loopback blockiert, kann ein lokales DNS/Hosts Mapping helfen.


