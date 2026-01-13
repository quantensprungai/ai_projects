<!-- Reality Block
last_update: 2026-01-13
status: stable
scope:
  summary: "Backup-Strategie für Proxmox VMs/CTs sowie HA/Docker Backups (Doku)."
  in_scope:
    - proxmox backup schedule (doc)
    - example commands for HA/Docker archives (doc)
  out_of_scope:
    - executing backups
    - external/offsite logistics details
notes:
  - "Quelle: Proxmox Masterdocs (Backup-Abschnitt)."
-->

# Proxmox Backups (VMs/CTs) + Zusatz-Backups

## Proxmox VMs / CTs

- Wöchentliche Backups  
- Mode: `snapshot`  
- Retention: `4`  

Warum `snapshot` (insb. für Windows VMs):
- vermeidet “stop”/Shutdown-Probleme
- nutzt QEMU Guest Agent (freeze/thaw) wenn verfügbar
- minimiert Downtime

## Home Assistant (LXC) – Beispiel

```bash
tar -czf /root/ha-backup.tar.gz -C /var/lib/lxc/110/rootfs/opt homeassistant
```

## Docker Daten – Beispiel

```bash
tar -czf /root/docker-backup.tar.gz /opt/docker
```


