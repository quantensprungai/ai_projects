# Proxmox – Erweiterte Anleitung und Anhänge (Teil 2)

<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "Troubleshooting, Details, Anhänge und vertiefte Konfigurationen zum Proxmox-Setup."
  in_scope:
    - troubleshooting playbooks
    - advanced networking notes
    - appendix/reference material
  out_of_scope:
    - secrets/credentials
    - live changes to the cluster
notes:
  - "Quelle: User-provided Master (Teil 2), in Repo übertragen (Doku-Only)."
-->

Dieses Dokument ergänzt das Hauptdokument mit technischen Details, Fehlerbehebungen, Legacy‑Konfigurationen und Hintergrundwissen. Alle Inhalte wurden vollständig aus deiner Master-Version übernommen.

## Querschnitt (kanonische Dateien im Repo)

Einige Sektionen sind Querschnitt und werden im Repo kanonisch an anderer Stelle gepflegt:

- RustDesk: `infrastructure/remote_access/rustdesk.md`
- Tailscale Zugriff: `infrastructure/tailscale/README.md` (+ `infrastructure/tailscale/machines.md`)
- Docker Host VM102: `infrastructure/docker/vm102_docker_host.md`
- Backups: `infrastructure/backups/proxmox_backups.md`
- Monitoring/Ports: `infrastructure/monitoring/services_and_ports.md`

Die Inhalte hier bleiben als “vollständige Master‑Notizen”, aber Querschnitt bevorzugt dort aktualisieren.

---

## 1. Detaillierte Debian‑Installationsschritte (für VM101 / VM102 / generische VMs)

### Installation über die Proxmox‑Konsole
1. Sprache auswählen
2. Hostname setzen (z. B. "management" oder "docker-apps")
3. Benutzer erstellen
4. Partitionierung: „Geführt – gesamte Festplatte verwenden"
5. Software‑Auswahl:
   - SSH Server
   - Standard‑Systemwerkzeuge
6. QEMU Guest Agent nach Installation:
```bash
apt install -y qemu-guest-agent
systemctl enable --now qemu-guest-agent
```

### Basis‑Pakete nach Installation
```bash
apt update
apt upgrade -y
apt install -y sudo curl
usermod -aG sudo user
```

---

## 2. RustDesk – Vollständige technische Details

Ausgelagert (kanonisch):

- `infrastructure/remote_access/rustdesk.md`

---

## 3. Tailscale – Vollständige technische Sektion

Ausgelagert (kanonisch):

- `infrastructure/tailscale/README.md`
- `infrastructure/tailscale/machines.md`

---

## 4. Windows 11 – Erweiterte Installation & Spezialfehler

### VirtIO‑Treiber laden
- Storage → ISO Images → `virtio-win.iso` einbinden
- Während Installation: „Treiber laden" → `vioscsi/w11/amd64`

### Netzwerktreiber
Ordner:
```text
NetKVM/w11/amd64
```

### Optionale CPU‑Flags für WSL2‑Probleme
```text
cpu: host,flags=+pdpe1gb,+spec-ctrl,+pcid
args: -cpu 'host,+vmx,-hypervisor'
```
Bei weiterhin schwierigen Setups (selten):
```text
args: -cpu 'host,+vmx,+pdpe1gb,+spec-ctrl,+pcid,-hypervisor,kvm=on'
```

### Manuelle Netzwerk‑Konfiguration (Legacy)
```powershell
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 192.168.188.18 -PrefixLength 24 -DefaultGateway 192.168.188.1
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 192.168.188.1
```

---

### VirtIO‑Treiberprobleme

**Wenn Windows during Installation keine Netzwerkgeräte findet:**
- `NetKVM/w11/amd64`

**Falls Storage fehlt:**
- `vioscsi/w11/amd64`

**Netzwerk verschwindet nach Reboot:**
- → Ursache: virtio‑net manchmal instabil in Proxmox
- Lösung: Netzwerkkarte auf E1000 setzen.

---

## 5. WSL2 – Deep Debugging & erweiterte Fehleranalyse

Ausgelagert (kanonisch):

- `infrastructure/dev_environment/vm105_wsl2.md`

---

## 6. AutoHotkey‑Skript für Proxmox‑Konsole

Für Windows‑Nutzer mit NoVNC Copy/Paste‑Problemen.

Hotkeys beginnen mit `Win + ...`
```autohotkey
#j::Send "sudo docker run -d --name hbbr --restart always --network host -v /opt/rustdesk/data:/root rustdesk/rustdesk-server:latest hbbr"
#k::Send "sudo docker run -d --name hbbs --restart always --network host -v /opt/rustdesk/data:/root rustdesk/rustdesk-server:latest hbbs"
#p::Send "sudo docker volume create portainer_data"
#o::Send "sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest"

#n::Send "ip addr add 192.168.188.50/24 dev vmbr0"
#g::Send "ip route add default via 192.168.188.1 dev vmbr0"
#v::Send "nano /etc/network/interfaces"
```

---

## 7. Legacy Netzwerk & VM‑Fehleranalyse
### Häufige Ursachen
- Windows VirtIO fliegt raus → E1000 wählen
- Bridge nutzt falsches Interface
- VM‑Firewall blockiert Verkehr

### Reparatur
```
brctl show vmbr0
ip link set enp0s31f6 master vmbr0
ip link set enp0s31f6 up
```

---

## 8. Docker & Proxmox Diagnose (Vollumfang)
Ausgelagert (kanonisch):

- VM102 Docker Host: `infrastructure/docker/vm102_docker_host.md`
- Monitoring/Ports: `infrastructure/monitoring/services_and_ports.md`

---

## 8.1. qBittorrent 4.6.x – Kategorien & Watch‑Folder

### qBittorrent 4.6.x – Kategorien werden nicht automatisch geladen

**Wichtige Änderung in Version 4.6.x:**
- qBittorrent liest `categories.json` nicht automatisch ein
- Kategorien erscheinen nur, wenn sie über die API einmal erstellt wurden
- Kategorien werden erst angezeigt, wenn mindestens ein Torrent existiert
- UI‑Option „Kategorien anzeigen" gibt es nicht mehr

### API‑Login‑Workflow (curl + cookies.txt)

**Login:**
```bash
curl -i -c cookies.txt -d "username=admin&password=<PASSWORT>" \
  http://<IP>:8092/api/v2/auth/login
```

**Kategorie erstellen:**
```bash
curl -b cookies.txt -X POST -d "category=PHASE1" -d "savePath=/downloads/PHASE1" \
  http://<IP>:8092/api/v2/torrents/createCategory
```

**Weitere Kategorien:**
```bash
curl -b cookies.txt -X POST -d "category=PHASE2" -d "savePath=/downloads/PHASE2" \
  http://<IP>:8092/api/v2/torrents/createCategory

curl -b cookies.txt -X POST -d "category=PHASE3" -d "savePath=/downloads/PHASE3" \
  http://<IP>:8092/api/v2/torrents/createCategory

curl -b cookies.txt -X POST -d "category=UNSORTED" -d "savePath=/downloads/_UNSORTED" \
  http://<IP>:8092/api/v2/torrents/createCategory

curl -b cookies.txt -X POST -d "category=SORTED" -d "savePath=/downloads/_SORTED" \
  http://<IP>:8092/api/v2/torrents/createCategory
```

### Watch‑Folder Konfiguration

**`watched_folders.json` Beispiel:**
```json
{
  "/watch": {
    "enabled": true,
    "loadMode": "Default",
    "category": "UNSORTED"
  },
  "/watch/libgen": {
    "enabled": true,
    "loadMode": "Default",
    "category": "PHASE2"
  },
  "/watch/zlibrary": {
    "enabled": true,
    "loadMode": "Default",
    "category": "PHASE3"
  }
}
```

**Kategorien‑Struktur:**
- `UNSORTED` → `/downloads/_UNSORTED`
- `SORTED` → `/downloads/_SORTED`
- `PHASE1` → `/downloads/PHASE1`
- `PHASE2` → `/downloads/PHASE2`
- `PHASE3` → `/downloads/PHASE3`

**Watch‑Ordner:**
- `/watch` → `UNSORTED`
- `/watch/libgen` → `PHASE2`
- `/watch/zlibrary` → `PHASE3`

### Troubleshooting: Torrent startet nicht

**Gründe & Fixes:**
- UDP blockiert durch VPN → Option A nutzen (Downloader ohne VPN)
- Tracker nicht erreichbar → Downloader ohne VPN
- DHT deaktiviert → aktivieren (Einstellungen → Verbindung → DHT aktivieren)
- Gluetun Durchsatzblockade → deaktivieren (qBittorrent läuft ohne VPN)
- VyprVPN blockiert P2P → Browser über VPN, Downloader ohne VPN

---

## 9. Erweiterte Backup‑Strategien (Vollversion)
Ausgelagert (kanonisch):

- `infrastructure/backups/proxmox_backups.md`

---

### VM/CT Backups (Proxmox)
- Wöchentlich Backups
- Mode: `stop`
- Retention: `4`

### Kritische Dateien sichern
```bash
mkdir -p /root/config-backup
cp /etc/network/interfaces /root/config-backup/
cp /etc/pve/qemu-server/*.conf /root/config-backup/
cp /etc/pve/storage.cfg /root/config-backup/
```

### Home Assistant Backup (LXC)
```bash
tar -czf /root/ha-backup.tar.gz -C /var/lib/lxc/110/rootfs/opt homeassistant
```

### Docker‑Stacks Backup
```bash
tar -czf /root/docker-backup.tar.gz /opt/docker
```

---

## 10. Zusätzliches Troubleshooting

### Docker Netzwerk‑Diagnose
```bash
docker network ls
docker network prune
docker compose down && docker compose up -d
```

### Proxmox Netzwerk Reset
```bash
rm /etc/network/interfaces.d/*
systemctl restart networking
```

---

## 11. Legacy‑Netzwerkkonfigurationen (für alte VMs)

### Alte VM‑IPs
- VM101: 192.168.188.12
- VM102: 192.168.188.16
- VM103: 192.168.188.xx
- VM104 (alt): 192.168.188.18
- VM105 (neu): DHCP

### Alte Netzwerkkonfiguration
```text
auto ens18
iface ens18 inet static
  address 192.168.188.xx/24
  gateway 192.168.188.1
```

Diese Konfiguration wird heute **nicht mehr eingesetzt**, ist aber hier archiviert.

---

## 12. Proxmox Host: Tools & Scripts (Altbestand)

### Post‑Install Script (Hinweis: optional)
```bash
bash -c "$(wget -qLO - https://tteck.github.io/Proxmox/proxmox-ve-post-install.sh)"
```

### Backup‑Script (optional)
```bash
bash -c "$(wget -qLO - https://tteck.github.io/Proxmox/proxmox-ve-host-backup.sh)"
```

---

## 13. Archivierte Inhalte & Legacy‑Dokumentation

### Historische Home Assistant VM (Legacy)

Frühere HA‑Version war eine vollständige KVM‑VM:
- höhere CPU‑Last
- träge Updates
- schwieriger Containerzugriff

**Aktueller Standard (empfohlen):**
- CT110 + Docker Home Assistant (host‑network)

### Alte statische IP‑Layouts (veraltet)
```text
auto ens18
iface ens18 inet static
  address 192.168.188.xx/24
  gateway 192.168.188.1
```

**Gründe gegen statische IPs:**
- Tailscale übernimmt Remote/Berechtigungen
- DHCP viel stabiler

### Alte VM104
- alte Downloader‑VM
- vollständig ersetzt durch neue VM102

### Alte Docker‑Stacks
- `downloads-v1`
- `services-old`
- `stack-test`

**Nicht mehr verwenden.**

### Weitere archivierte Inhalte
- Alte statische Windows‑IPs
- Alte Ressourcenverteilung
- Alte Nextcloud‑Konfigurationen (vollständig migriert)

---

## 14. Langfristige Systempflege

### Regelmäßige Aufgaben
- **Docker:** automatische Updates via Watchtower
- **Proxmox:** monatliche Kernel‑ & Systemupdates
- **Tailscale:** Key‑Verlängerung prüfen (alle 6 Monate)
- **Snapshots:** VM101 & VM102 monatlich
- **Backups:** quartalsweise auf externe Offline‑HDDs sichern

### Langfristige Pläne
- Spark GPU Node Integration (Phase 4)
- Anna's Archive Automatisierung (Phase 2/3)
- PDF/A Konvertierung & OCR Pipeline
- Deduplizierung großer Archive
- KI‑basierte Vektorsuche

---

## 15. Systemlevel Debugging (Linux allgemein)

### Offene Ports
```bash
ss -tulpn
```

### Laufende Prozesse
```bash
ps aux --sort=-%cpu | head
```

### RAM‑Verbrauch
```bash
free -h
```

### Netzwerkverkehr live
```bash
tcpdump -i vmbr0
```

### Proxmox Storage Fehleranalyse

**Storage‑Konfiguration prüfen:**
```bash
cat /etc/pve/storage.cfg
```

**Prüfen, ob LVM aktiv ist:**
```bash
lvs
vgs
pvs
```

**Datenbank reparieren (selten notwendig):**
```bash
systemctl restart pvedaemon
systemctl restart pveproxy
```

---

**Ende der erweiterten Anleitung (Vollständige Master-Version)**

Dies ist die vollständige, konsolidierte und bereinigte erweiterte Anleitung zu deinem Proxmox‑Setup.

**Beinhaltet:**
- vollständige Debugging‑Tools
- alle Netzwerk‑Artefakte
- Legacy‑Konfigurationen
- Host‑Werkzeuge & Backup‑Richtlinien
- Windows/WSL2 Tiefenanalyse
- RustDesk/Tailscale Vollversion
- Docker & Proxmox Diagnose (Vollumfang)

Damit ist Dokument 2 nun 100 % vollständig.


