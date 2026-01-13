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

### Ports & Dienste

RustDesk benötigt:
- TCP 21115–21119 (Client‑Kommunikation)
- hbbs = Broker
- hbbr = Relay

### Dienste prüfen
```bash
ss -tulpn | grep -E '21115|21116|21117|21118|21119'
```

### Logs anzeigen
```bash
docker logs hbbr
docker logs hbbs
```

### Schlüssel anzeigen
```bash
cat /opt/rustdesk/data/id_ed25519.pub
```

**Wichtig:** Bei „connection failed" immer prüfen:
- Ports offen?
- Key korrekt eingegeben? (häufig l/1 & O/0 Fehler)
- Broker erreichbar?

### Container reparieren
```bash
docker ps -a | grep hb
```

Falls Container fehlen:
```bash
docker run -d --name hbbr --restart always --network host -v /opt/rustdesk/data:/root rustdesk/rustdesk-server:latest hbbr

docker run -d --name hbbs --restart always --network host -v /opt/rustdesk/data:/root rustdesk/rustdesk-server:latest hbbs
```

### NAT‑Loopback & LAN/Remote Fixes

Viele FritzBox‑Router blockieren NAT‑Loopback.

**Lösung über dnsmasq:**
```text
address=/rustdesk.local/192.168.188.12
```

**Windows Hosts File:**
```text
192.168.188.12 rustdesk.local
```

Damit funktioniert Zugriff:
- im LAN
- aus dem Internet (über Relay)
- ohne DNS‑Konflikte

### Externer Zugriff
- TCP 21115–21119
- UDP 21116

---

## 3. Tailscale – Vollständige technische Sektion

### Installation
```bash
curl -fsSL https://tailscale.com/install.sh | sh
systemctl enable --now tailscaled
```

### Login
```bash
tailscale up --ssh
```

### Status
```bash
tailscale status
```

### Netzcheck
```bash
tailscale netcheck
```

**Ergebnisse:**
- `direct` = optimale Verbindung
- `relay` = geht über DERP (langsamer)
- `udp blocked` = Firewall/Router Problem

### Ping zu Nodes
```bash
tailscale ping 100.x.x.x
```

### MagicDNS & Hostnames

MagicDNS erlaubt Zugriff via:
- `pve.tailnet-name.ts.net`
- `management.tailnet-name.ts.net`
- `docker-apps.tailnet-name.ts.net`

**Aktivieren in der Admin‑Konsole:**
https://login.tailscale.com/admin/dns

**Empfehlung:** immer aktivieren.

### ACL‑Konfiguration (erweiterte Version)

**Minimal‑ACL example:**
```json
{
  "default": "accept",
  "acls": [
    {"action": "accept", "src": ["tag:server"], "dst": [":"]}
  ],
  "tagOwners": {
    "tag:server": ["*"],
    "tag:critical": ["*"],
    "tag:ha": ["*"]
  }
}
```

**Empfohlene Tags:**
- `tag:server` → VM101, VM102
- `tag:critical` → pve
- `tag:ha` → Home Assistant

### Key Management

**Key‑Verlängerung deaktivieren:**

Für Server unbedingt:
- Admin Panel → Machines → Node → Edit → Disable key expiry

**Keys erneuern:**
```bash
tailscale up --auth-key <KEY> --ssh
```

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

### WSL Version prüfen
```powershell
wsl --list --verbose
```

**Erwartet:**
```text
Ubuntu    Running      2
```

### WSL2 startet nicht / Fehler 0x80370114

**Fix:**
```powershell
wsl --update
wsl --set-default-version 2
```

**Fehler: „Hardware virtualization must be enabled"**
- → BIOS/UEFI prüfen: Intel VT‑x oder AMD‑V aktivieren.

**CPU‑Flags in Proxmox ergänzen:**
```text
args: -cpu 'host,+vmx,+pdpe1gb,+spec-ctrl,+pcid,-hypervisor,kvm=on'
```

### Node.js/npm – EACCES Fehler

**Symptome:**
- `npm install -g` bricht ab
- Permission denied

**Fix:**
```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
```

`.bashrc` erweitern:
```bash
export PATH=~/.npm-global/bin:$PATH
```

### PowerShell – WSL Komfortprofil
```powershell
if (!(Test-Path -Path $PROFILE)) {
  New-Item -ItemType File -Path $PROFILE -Force
}
Add-Content -Path $PROFILE -Value 'function Start-WSL { wsl }'
Add-Content -Path $PROFILE -Value 'Set-Alias -Name linux -Value Start-WSL'
```

### Hyper‑V Dienste bereinigen (falls WSL hängt)
```powershell
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Hypervisor
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Hypervisor
```

### Netzwerkisolation in Windows VMs beheben

**VirtIO fliegt raus → E1000 nutzen**

Falls WSL2 dennoch Probleme macht, zusätzlich:
```text
args: -cpu 'host,+vmx,+pdpe1gb,-hypervisor'
```

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

### Docker Netzwerk‑Analyse

**Aktive Netzwerke anzeigen:**
```bash
docker network ls
```

**Bridge‑Netzwerk prüfen:**
```bash
docker network inspect bridge
```

**Erwartete Punkte:**
- Gateway: 172.17.0.1
- Subnet: 172.17.0.0/16
- Containers: deine aktiven Container

**Fehlerindikatoren:**
- Keine Subnets → Docker wurde defekt neu installiert
- Leere Containerliste trotz laufender Container

### Docker Netzwerk bereinigen

**Ungenutzte Netzwerke löschen:**
```bash
docker network prune
```

**Kompletter Stack neu starten:**
```bash
docker compose down && docker compose up -d
```

**Einzelnen Container neu starten:**
```bash
docker restart <containername>
```

### Docker Socket & API Fehler

**Docker Socket Berechtigungen prüfen:**
```bash
ls -l /var/run/docker.sock
```

**Remote Docker API aktivieren (falls defekt):**
```bash
mkdir -p /etc/systemd/system/docker.service.d
cat > /etc/systemd/system/docker.service.d/override.conf << 'EOF'
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2375
EOF
systemctl daemon-reload
systemctl restart docker
```

### Container verschiedene Fehlerbilder

**Container startet sofort neu (Restart loop):**
```bash
docker logs <container>
```

**Ursachen:**
- falscher Mount
- Port blockiert
- fehlende ENV Variablen

**Container startet nicht wegen Berechtigungen:**
```bash
chmod -R 1000:1000 /opt/docker
```

**Unbekannter Fehler → komplettes Rebuild:**
```bash
docker compose down -v
rm -rf /opt/docker/<app>/config
```

**Achtung:** Datenbank‑Container NICHT löschen.

### DNS‑Probleme in Containern

**Test:**
```bash
docker exec -it <container> ping google.com
```

**Wenn DNS fail:**
```bash
echo "nameserver 1.1.1.1" >> /etc/resolv.conf
```

**Best practice für Debian Host:**
```bash
echo "DNS=1.1.1.1" >> /etc/systemd/resolved.conf
systemctl restart systemd-resolved
```

### Gluetun (VPN) Diagnose (Optional – nur für Direct Downloads)

**Hinweis zu VyprVPN:**
- VyprVPN blockiert Torrent‑Protokolle (UDP, DHT, PeX)
- Es ist ungeeignet für P2P‑Downloads
- Daher läuft qBittorrent ohne VPN
- Nur Browser über VPN für Website‑Zugriff

**Logs anzeigen (falls Gluetun für Direct Downloads genutzt wird):**
```bash
docker logs gluetun
```

**Typische Fehler:**
- `AUTH_FAILED` → Login falsch
- `DNS_FAIL` → DNS blockiert
- `ROUTE_REJECTED` → falscher Server

**IP Prüfen:**
```bash
docker exec -it gluetun wget -qO- https://ifconfig.me
```

Soll NICHT deutsche IP sein.

### Proxmox Netzwerk – Tiefenanalyse

**Bridge anzeigen:**
```bash
brctl show
```

**Interfaces prüfen:**
```bash
ip a
```

**Routing prüfen:**
```bash
ip route
```

**DHCP prüfen:**
```bash
journalctl -u systemd-networkd --no-pager
```

### Proxmox Host – Netzwerk Hard Reset

**(GTK only as last resort)**
```bash
rm /etc/network/interfaces.d/*
systemctl restart networking
```

**Gefahr:**
- Host verliert Verbindung → Konsole nötig.

### Proxmox Firewall Debugging

**Status:**
```bash
pve-firewall status
```

**Deaktivieren (für Homelabs empfohlen):**
```bash
pve-firewall stop
```

**VM‑Firewall unbedingt abschalten:**
- VM → Hardware → Network → Firewall: OFF

### LXC Permissions / Nesting Probleme

**Container kann Docker nicht starten:**
- `features: nesting=1,keyctl=1`

**Overlay Probleme:**
```bash
pct set 110 -features fuse=1,mount=nfs
```

### Systematische Debugging‑Checkliste

- Kann Host DNS auflösen?
- Kann Host Internet erreichen?
- Kann Container DNS auflösen?
- Nutzt Container richtigen User (uid/gid)?
- Sind Mounts korrekt?
- Sind ENV Variablen gesetzt?
- Sind Ports frei?
- Ist Firewall deaktiviert?
- Läuft der VPN‑Dienst? (nur für Direct Downloads, nicht für qBittorrent)
- qBittorrent läuft ohne VPN im Bridge‑Netzwerk

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
```bash
mkdir -p /root/config-backup
cp /etc/network/interfaces /root/config-backup/
cp /etc/pve/qemu-server/*.conf /root/config-backup/
cp /etc/pve/storage.cfg /root/config-backup/
```

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


