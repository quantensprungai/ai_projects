# proxmox

<!-- Reality Block
last_update: 2026-01-13
status: stable
scope:
  summary: "Index und Struktur für Proxmox-Dokumentation (Homelab/VMs/Netzwerk/Backups)."
  in_scope:
    - document index
    - file organization
    - links between proxmox docs
  out_of_scope:
    - changes to the actual environment
notes:
  - "Inhalte sind Doku-Only; Änderungen am System erfolgen außerhalb des Repos."
-->

Diese Sektion enthält die **Proxmox-Masterdokumentation** und dazugehörige Anhänge.

## Status (Wichtig)

- Diese Dokumente sind für dein Homelab aktuell und gelten als **Source of Truth (Doku)**.
- Trotzdem: **nicht blind copy/pasten/ausführen**, wenn du nicht sicher bist, dass der Abschnitt zu deinem aktuellen Stand passt (z. B. Legacy-IP-Abschnitte).
- Wo Werte dynamisch sind (z. B. **Tailscale IPs**), ist `tailscale status` / Admin‑Panel die Quelle der Wahrheit.

## Struktur

- `01_setup/` – Setup-Dokumente (das “3‑Dokumente‑System”)
- `02_operations/` – Betrieb (Wartung, Backups, Routine-Tasks)
- `99_archive/` – Legacy / alte Versionen

## 3‑Dokumente‑System (Setup)

1. `01_setup/1_proxmox-komplettsetup.md` – Haupt-Setup (Master)
2. `01_setup/2_proxmox-erweiterte-anleitung-und-anhaenge.md` – Troubleshooting & Details (folgt)
3. `01_setup/3_annas-archive-wissenssystem.md` – Download-Strategien & Archivierung (folgt)



