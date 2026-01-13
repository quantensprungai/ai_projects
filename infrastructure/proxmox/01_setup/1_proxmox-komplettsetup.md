# Proxmox‑Komplettsetup – Vollständige Dokumentation (Master, Dezember 2025)

<!-- Reality Block
last_update: 2026-01-13
status: stable
scope:
  summary: "Konsolidierte Master-Version des Proxmox-Setups inkl. VM/CT-Übersicht, Netzwerk, Remotezugriff, Backups und Troubleshooting."
  in_scope:
    - system overview
    - VM/CT inventory
    - network/firewall config (documentation)
    - service/ports reference
    - operational workflows (documentation)
  out_of_scope:
    - executing commands on the cluster
    - secrets/credentials
notes:
  - "Quelle: User-provided Master (Dez 2025), in Repo übertragen (Doku-Only)."
-->

Diese Datei ist die **zusammengeführte Master‑Version** aus:
- dem bisherigen `Haupt.md`
- `Proxmox Komplettsetup und Projektplan.md` (Downloads)

Alle Inhalte sind konsolidiert, doppelte Stellen wurden bereinigt.

**Teil des 3‑Dokumente‑Systems:**
1. **`1 Proxmox‑Komplettsetup.md`** ← Dieses Dokument (Haupt‑Setup)
2. **`2 Proxmox Erweiterte Anleitung und Anhänge.md`** (Troubleshooting & Details)
3. **`3 Anna's Archive Wissenssystem.md`** (Download‑Strategien & Archivierung)

## Querschnitts-Doku (Single Source of Truth im Repo)

Einige Inhalte aus diesem Dokument sind Querschnitt (gelten nicht nur “Proxmox”, sondern das ganze Homelab):

- **Tailscale Zugriff/SSH**: `infrastructure/tailscale/README.md`
- **Docker Host VM102**: `infrastructure/docker/vm102_docker_host.md`
- **Backups**: `infrastructure/backups/proxmox_backups.md`
- **Monitoring/Ports**: `infrastructure/monitoring/services_and_ports.md`

Dieses Dokument bleibt weiterhin das **Setup-Narrativ**, aber Querschnitt wird bevorzugt in den oben genannten Dateien gepflegt.

---

## Inhaltsverzeichnis

1. Systemübersicht  
2. Workflow im Alltag  
3. Überblick der VMs und Container  
4. Proxmox Host Netzwerk & Firewall  
5. VM 101 – Management & RustDesk‑Server  
6. VM 102 – Docker‑Apps / Downloader  
7. VM 103 – Linux Mint (optional)  
8. VM 105 – Windows 11 Pro  
9. CT 110 – Home Assistant (LXC)  
10. Windows 11 Installation ohne Microsoft‑Konto  
11. RustDesk‑ und Tailscale‑Konfiguration  
12. Backup‑Strategie  
13. Troubleshooting (Erweitert)  
14. Quick Reference  
15. Projektplan Phase 1–7  
16. Übersicht: Dienste & Ports  
17. Tailscale – Erweiterte Konfiguration  
18. Archivierte Inhalte & Legacy‑Dokumentation  
19. Wartung, Pflege & Weiterentwicklung  

---

## 1. Systemübersicht

Dieses Setup stellt dein modernes, robustes und sicheres Homelab bereit:

- **Management & Remotezugriff** über VM101 (`management`, RustDesk + Tailscale + Portainer)  
- **Docker‑Host & Downloader‑Stack** über VM102 (`docker-apps`)  
- **Windows‑11‑Entwicklungsumgebung** (VM105, WSL2, Dev‑Tools)  
- **Home Assistant Smart Home** (LXC110)  
- **Optional: Linux Mint** (VM103)  
- **Proxmox Host** als Hypervisor (`pve`, 192.168.0.50)  

Remote‑Management über:
- **Tailscale** (Zero‑Config VPN, globaler Zugriff)  
- **RustDesk** (Remote Desktop ohne Portweiterleitungen)  

### Ziele des Systems

- Klare Trennung der Aufgabenbereiche  
- Remote‑Verwaltung über Tailscale & RustDesk  
- Docker‑Host für Self‑Hosting & Downloader‑Stack  
- Windows 11 VM für KI‑/Software‑Entwicklung  
- Home Assistant LXC für Smart Home  

---

## 2. Workflow im Alltag

### ▶ VM101 – Management (immer an)

- RustDesk‑Server  
- Portainer  
- Tailscale Node  
- SSH & Monitoring  
- → Zentrale Steuer‑VM für dein gesamtes System.

### ▶ VM102 – Docker‑Apps / Downloader

- qBittorrent (ohne VPN im Bridge‑Netzwerk)  
- JDownloader2 (Port 5800)  
- Filebrowser (Port 8093)  
- Glances Monitoring (Port 61208)  
- IPFS Gateway (Port 8081)  
- Watchtower Auto‑Updates  
- → Für Downloads, Selfhosting, Automations‑Tasks.

**Option A (Empfohlen) – Downloader ohne VPN:**
- Der Downloader benötigt kein VPN
- Nur der Browser muss über VPN laufen, um die AA‑Website zu öffnen
- Torrents selbst laufen direkt über die normale Internetverbindung
- Torrent‑Ports 6881 TCP/UDP und 8092 HTTP sind direkt erreichbar

### ▶ VM105 – Windows 11 (Hauptarbeitsmaschine)

- WSL2 (Ubuntu)  
- Node.js, Claude Code, Dev‑Tools  
- Hochschule‑VPN  
- → Deine Entwicklungs‑ und KI‑Arbeitsumgebung.

### ▶ CT110 – Home Assistant (LXC)

- Host‑Netzwerk  
- Docker‑basiert  
- → Zentrale Smart‑Home‑Steuerung.
- Ressourcen: 2 GB RAM, 2 Cores  
- Firewall deaktiviert, DHCP empfohlen  

### ▶ VM103 – Linux Mint (optional)

- Wird nur bei Bedarf gestartet.

### ▶ Remote‑Zugriff insgesamt

- RustDesk (intern + extern)  
- Tailscale (globaler Zugriff auf Proxmox & VMs)  

---

## 3. Überblick der VMs und Container

| Typ  | ID  | Name         | RAM  | Cores | Lokale IP       | Tailscale Name | Funktion                         |
|------|-----|--------------|------|-------|----------------|----------------|----------------------------------|
| Host | –   | pve          | –    | –     | 192.168.0.50   | pve            | Proxmox Hypervisor               |
| VM   | 101 | management   | 4 GB | 1     | 192.168.0.12   | management     | RustDesk, Portainer, Tailscale   |
| VM   | 102 | docker-apps  | 8 GB | 2     | 192.168.0.16   | docker-apps    | Docker + Downloader (ohne VPN)  |
| VM   | 103 | linux-mint   | 8 GB | 2     | DHCP           | –              | Optional                         |
| VM   | 105 | win11pro     | 20 GB| 4     | DHCP           | win11pro105    | Entwicklung & WSL2               |
| LXC  | 110 | homeassistant| 2 GB | 2     | 192.168.0.90   | –              | Home Assistant                   |

---

## 4. Proxmox Host Netzwerk & Firewall

### Netzwerk‑Konfiguration (Host `pve`)

```text
auto lo
iface lo inet loopback

auto nic0
iface nic0 inet manual

auto vmbr0
iface vmbr0 inet static
    address 192.168.0.50/24
    gateway 192.168.0.1
    bridge-ports nic0
    bridge-stp off
    bridge-fd 0
```

### Proxmox‑VM‑Firewall

- Muss bei **allen VMs deaktiviert** sein:  
  `VM → Hardware → Network Device → Firewall: deaktiviert`

### Windows‑VMs NIC‑Modell

- **E1000** verwenden  
- Verhindert Verbindungsverluste nach Neustarts.

### DHCP für Windows

- Statische IPs unnötig → Tailscale übernimmt die „logische“ Adressierung.

### FritzBox 7530 im IP‑Client‑Modus (Kein Doppel‑NAT mehr)

- FritzBox arbeitet jetzt im **IP‑Client‑Modus** (vorhandene Internetverbindung mitbenutzen)
- Alle Geräte sind im Netz **192.168.0.x**
- DHCP kommt von der **Vodafone CableBox (192.168.0.1)**
- Die FritzBox hat die feste IP **192.168.0.2** und **DHCP ist deaktiviert**
- Die FritzBox dient nur noch als **Access Point / Switch** und ist unter `192.168.0.2` erreichbar (WLAN‑Einstellungen etc.)
- **Port‑Weiterleitungen** müssen in der **Vodafone‑Box** eingerichtet werden, nicht mehr in der FritzBox

---

## 5. VM 101 – Management & RustDesk‑Server (Debian 12)

**Ressourcen:**
- 1 Core  
- 4 GB RAM  
- IP: 192.168.0.12  

**Funktionen:**
- RustDesk hbbr + hbbs  
- Portainer  
- Docker Engine  
- Tailscale  
- SSH  

### Basisinstallation

```bash
apt update && apt install -y curl docker.io
```

### RustDesk Server

```bash
mkdir -p /opt/rustdesk/data

docker run -d --name hbbr --restart always --network host \
  -v /opt/rustdesk/data:/root rustdesk/rustdesk-server:latest hbbr

docker run -d --name hbbs --restart always --network host \
  -v /opt/rustdesk/data:/root rustdesk/rustdesk-server:latest hbbs
```

### Portainer

```bash
docker volume create portainer_data

docker run -d -p 8000:8000 -p 9443:9443 --name portainer \
  --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest
```

### Tailscale

```bash
curl -fsSL https://tailscale.com/install.sh | sh
tailscale up --ssh
```

---

## 6. VM 102 – Docker‑Apps / Downloader (Debian 12)

**Ressourcen:**
- 2 Cores  
- 8 GB RAM  
- IP: 192.168.0.16  

**Architektur:**
- Docker‑Apps / Downloader (ohne VPN für qBittorrent)
- Browser‑basierter VPN‑Zugriff auf AA

### Basisinstallation

```bash
apt update && apt install -y docker.io docker-compose-plugin
systemctl enable docker
```

### Remote Docker API

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

### Tools / Stack (Überblick)

- qBittorrent (läuft ohne VPN im normalen Bridge‑Netzwerk)  
- JDownloader 2 (Port 5800)  
- Filebrowser  
- IPFS Node  
- Glances  
- Watchtower  

**Option A (Empfohlen) – Downloader ohne VPN:**

- Der Downloader benötigt kein VPN
- Nur der Browser muss über VPN laufen, um die AA‑Website zu öffnen
- Torrents selbst laufen direkt über die normale Internetverbindung
- Torrent‑Ports 6881 TCP/UDP und 8092 HTTP sind direkt erreichbar

**Hinweis zu Gluetun:**
- Gluetun wird nicht mehr für Torrents verwendet (da VyprVPN P2P blockiert)
- Optional kann Gluetun weiterhin für Direct Downloads genutzt werden

Details zum vollständigen `docker-compose.yml` kannst du bei Bedarf separat ergänzen.

---

## 7. VM 103 – Linux Mint (optional)

- Optional, im Normalbetrieb gestoppt.  
- 2 Cores, 8 GB RAM.  
- Für GUI‑Tests oder alternative Linux‑Workflows.  

---

## 8. VM 105 – Windows 11 Pro (Hauptarbeitsmaschine)

**Ausstattung:**
- 4 Cores  
- 20 GB RAM  
- 800 GB NVMe  
- UEFI (OVMF), TPM 2.0  
- VirtIO‑Treiber  

### WSL2 aktivieren

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl --install -d Ubuntu
```

### Dev‑Tools in WSL (Node.js & Claude Code)

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
npm install -g @anthropic-ai/claude-code
```

Tailscale für Windows: Download von der offiziellen Seite (`https://tailscale.com/download`).

---

## 9. CT 110 – Home Assistant (LXC)

### Container erstellen

```bash
pct create 110 local:vztmpl/debian-12-standard_12.12-1_amd64.tar.zst \
 --hostname homeassistant --memory 2048 --cores 2 --rootfs local-lvm:16 \
 --net0 name=eth0,bridge=vmbr0,firewall=0,ip=dhcp --unprivileged 1 \
 --features nesting=1,keyctl=1 --onboot 1
pct start 110
```

### Home Assistant via Docker starten

```bash
pct exec 110 -- bash -c "apt update && apt install -y curl ca-certificates && curl -fsSL https://get.docker.com | sh"

pct exec 110 -- docker run -d --name homeassistant --restart=unless-stopped \
  --privileged -e TZ=Europe/Berlin \
  -v /opt/homeassistant:/config --network=host \
  ghcr.io/home-assistant/home-assistant:stable
```

**Zugriff:** `http://192.168.0.90:8123`

---

## 10. Windows 11 Installation ohne Microsoft‑Konto

Während des Setups:

```text
Shift + F10
OOBE\BYPASSNRO
```

→ Nach Neustart ist ein **lokales Konto** möglich.

---

## 11. RustDesk‑ & Tailscale‑Konfiguration

### RustDesk Key anzeigen

```bash
cat /opt/rustdesk/data/id_ed25519.pub
```

### Tailscale Best Practices

- Key Expiry deaktivieren  
- `tailscale up --ssh` verwenden  
- Zugriff über Tailscale‑Adressen `100.x.x.x`

### Tailscale IPs – Aktuelle Maschinen

| Maschine        | Tailscale Name | Lokale IP        | Tailscale IP        | SSH | Status     |
|-----------------|----------------|------------------|---------------------|-----|------------|
| Proxmox Host    | pve            | 192.168.0.50     | `100.115.71.71`     | ✅  | Connected  |
| VM 101          | management     | 192.168.0.12     | `100.124.9.7`       | ✅  | Connected  |
| VM 102          | docker-apps    | 192.168.0.16     | `100.83.17.106`    | ✅  | Connected  |
| VM 105          | win11pro105    | DHCP             | `100.70.238.41`    | ❌  | Connected  |
| Windows 10      | me230701       | –                | `100.125.227.52`    | ❌  | Connected  |
| Spark GPU       | spark-56d0     | –                | `100.96.115.1`      | ✅  | Connected  |

**IPs aktualisieren:**
- Auf Linux: `tailscale ip` oder `tailscale status`
- Im Tailscale Admin‑Panel: https://login.tailscale.com/admin/machines
- Die `100.x.x.x` Adressen können sich ändern – immer aktuell im Admin‑Panel prüfen  

---

## 12. Backup‑Strategie

### Proxmox VMs / CTs

- Wöchentliche Backups  
- Mode: `stop`  
- Retention: `4`  

### Home Assistant

```bash
tar -czf /root/ha-backup.tar.gz -C /var/lib/lxc/110/rootfs/opt homeassistant
```

### Docker‑Daten

```bash
tar -czf /root/docker-backup.tar.gz /opt/docker
```

---

## 13. Troubleshooting (Erweitert)

### Tailscale

```bash
systemctl restart tailscaled
tailscale status
tailscale ping 100.x.x.x
tailscale netcheck
```

**Common Issues:**
- MagicDNS deaktiviert → DNS‑Probleme
- Key expired → VM nicht erreichbar
- ACL blockiert → Zugriff verweigert

### Proxmox Netzwerk Reset

```bash
rm /etc/network/interfaces.d/*
systemctl restart networking
```

### Docker Netzwerk‑Diagnose

```bash
docker network ls
docker network inspect bridge
docker network prune
docker compose down && docker compose up -d
```

### Gluetun VPN Debug (Optional – nur für Direct Downloads)

```bash
docker logs gluetun
```

**Hinweis:** Gluetun wird nicht mehr für qBittorrent verwendet, da VyprVPN Torrent‑Protokolle (UDP, DHT, PeX) blockiert.

**Typische Fehler (falls Gluetun für Direct Downloads genutzt wird):**
- `AUTH_FAILED` → falscher VPN‑Account
- `DNS_FAIL` → DNS‑Server blockiert
- `ROUTE_REJECTED` → falscher Provider‑Server

### qBittorrent Troubleshooting

**WebUI „Unauthorized" Fix:**

In `qBittorrent.conf`:
```text
WebUI\HostHeaderValidation=false
```
Danach:
```bash
service qbittorrent-nox restart
```

**Torrent lädt nicht trotz Seeds:**
- Prüfe Ports: 6881 TCP/UDP (müssen offen sein, kein VPN)
- Prüfe DHT/PeX aktiviert
- DHT aktivieren: Einstellungen → Verbindung → DHT aktivieren
- **Wichtig:** qBittorrent läuft ohne VPN – UDP/DHT muss funktionieren
- Falls VPN aktiv war → deaktivieren (VyprVPN blockiert P2P)

### JDownloader2 Troubleshooting

**GUI startet nicht:**
```bash
docker restart jdownloader
```

**Captchas ohne Bild:**
- `0.0.0.0:5800` lokal öffnen (nicht Tailscale!)
- Browser‑Cache leeren
- JDownloader2 aktualisieren

### Home Assistant (LXC) Fehleranalyse

**Kein Netzwerk:**
```bash
pct exec 110 -- dhclient -v
```

**Docker startet nicht:**
```bash
pct exec 110 -- systemctl restart docker
```

**Wollte nicht booten → Config reset:**
```bash
pct stop 110
pct fsck 110
pct start 110
```

### Windows 11 (VM105) – Troubleshooting

**VirtIO Treiber fehlt → kein Netzwerk:**
- Installer → Treiber laden → `NetKVM/w11/amd64`

**WSL2 startet nicht:**
```powershell
wsl --update
wsl --set-default-version 2
```

**Node/npm Berechtigungen:**
```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
```

### RustDesk – Keypair / NAT Debug

**Key anzeigen:**
```bash
cat /opt/rustdesk/data/id_ed25519.pub
```

**NAT Loopback Fix für FritzBox:**

In dnsmasq:
```text
address=/rustdesk.local/192.168.0.12
```

Hosts‑Datei unter Windows:
```text
192.168.0.12 rustdesk.local
```

---

## 14. Quick Reference

### Lokale Zugriffe (LAN)

| Dienst        | URL                          |
|--------------|------------------------------|
| Proxmox      | https://192.168.0.50:8006    |
| Portainer    | https://192.168.0.12:9443    |
| qBittorrent  | http://192.168.0.16:8092     |
| JDownloader2 | http://192.168.0.16:5800     |
| Filebrowser  | http://192.168.0.16:8093/files/ |
| Glances      | http://192.168.0.16:61208    |
| Home Assistant | http://192.168.0.90:8123   |

### Tailscale Zugriffe (Remote)

| Dienst         | URL über Tailscale                         |
|---------------|--------------------------------------------|
| Proxmox       | https://100.115.71.71:8006                |
| Portainer     | https://100.124.9.7:9443                  |
| qBittorrent   | http://100.83.17.106:8092                 |
| JDownloader2  | http://100.83.17.106:5800                 |
| Filebrowser   | http://100.83.17.106:8093/files/          |
| Glances       | http://100.83.17.106:61208                |
| Home Assistant| http://100.124.9.7:8123 (über management) |
| Spark GPU     | http://100.96.115.1:11000                 |

---

## 15. Projektplan Phase 1–7

### Phase 1 – Infrastruktur ✔

### Phase 2 – Anna's Archive Automation
- Auto Downloader  
- Auto Sorter  
- OCR Pipeline  
- Metadata Extraction  
- ➡️ **Siehe:** `Anna's Archive Wissenssystem.md` für vollständige Strategie  

### Phase 3 – Große AA‑Archive
- LibGen  
- Z‑Library  
- IA Public Domain  
- SciHub  

### Phase 4 – Spark GPU Integration
- vLLM / Ollama  
- OCR Speedup  
- Vector Search  

### Phase 5 – Monitoring & Komfort
- Uptime Kuma  
- NPM (Nginx Proxy Manager o.ä.)  
- Dashboards  

### Phase 6 – Archivierung
- PDF/A  
- Deduplizierung  

### Phase 7 – Homelab Erweiterungen
- Paperless  
- Photoprism  
- Jellyfin  

---

## 16. Übersicht: Dienste & Ports (Vollständige Referenz)

| Service        | Port/Protokoll        | Notes                          |
|----------------|----------------------|--------------------------------|
| Proxmox        | 8006 (HTTPS)         | Hauptverwaltung                |
| Portainer      | 9443 (HTTPS)         | Docker Admin                   |
| qBittorrent    | 8092 (HTTP)          | Ohne VPN (Bridge‑Netzwerk)     |
| JDownloader2  | 5800 (HTTP)          | GUI via Browser                |
| Filebrowser    | 8093 (HTTP)          | Datei‑Explorer                 |
| Glances        | 61208 (HTTP)         | Monitoring                     |
| IPFS           | 8081 (HTTP)          | Gateway                        |
| Home Assistant | 8123 (HTTP)          | Smart Home                     |
| RustDesk hbbr  | 21117 TCP            | Relay                          |
| RustDesk hbbs  | 21118 TCP            | Broker                         |
| RustDesk Clients | 21115‑21119       | Kommunikation                  |
| Spark GPU      | 11000 (HTTP)         | GPU Services                   |

---

## 17. Tailscale – Erweiterte Konfiguration

### MagicDNS aktivieren
- Ermöglicht Zugriffe via `hostname.tailnet-name.ts.net`
- Im Admin‑Panel aktivieren

### SSH direkt über Tailscale
```bash
tailscale up --ssh
```
Dann:
```bash
ssh root@pve
ssh user@management
ssh user@docker-apps
```

### Netzwerkanalyse mit Tailscale

**Verbindungsstatus prüfen:**
```bash
tailscale status
```

**Peer‑Verbindung testen:**
```bash
tailscale ping 100.x.x.x
```

**Netzcheck ausführen:**
```bash
tailscale netcheck
```

**Typische Ergebnisse:**
- UDP blocked → Router oder Firewall Problem
- Relay mode → Verbindung über DERP‑Server (langsamer)
- Direct → optimale Verbindung

### Tailscale Admin‑Panel
Alle Maschinen findest du hier: https://login.tailscale.com/admin/machines

**Empfohlen:**
- Key‑Expiry deaktivieren für Server
- ACLs minimal halten
- SSH Zugriff aktivieren (`tailscale up --ssh`)

---

## 18. Archivierte Inhalte & Legacy‑Dokumentation

### Alte Home Assistant VM (historisch)
Vor der LXC‑basierten Lösung (CT110) wurde Home Assistant in einer vollständigen KVM‑VM betrieben. Diese Version war funktionsfähig, aber:
- schwerfällig
- update‑anfälliger
- langsamer
- verbrauchte mehr Ressourcen

**Aktuelle Empfehlung:** CT110 + Docker

### Alte statische VM‑IPs
Früher genutzt:
- VM101 → 192.168.188.12
- VM102 → 192.168.188.16
- VM103 → 192.168.188.xx
- VM104 → 192.168.188.18 (nicht mehr vorhanden)
- VM105 → statisch, später DHCP

**Aktueller Stand:** DHCP + Tailscale für Adress‑Management

### Alte Netzwerk‑Konfigurationen (nur Referenz)
```text
auto ens18
iface ens18 inet static
  address 192.168.188.xx/24
  gateway 192.168.188.1
```

Diese Variante ist obsolet, da:
- Tailscale den Remote‑Zugriff übernimmt
- DHCP stabiler ist
- kein Vorteil durch statische lokale IPs besteht

### Weitere Legacy‑Komponenten

**ehem. VM104 – „downloads-old":**
- Wurde vollständig migriert
- Nicht mehr im Einsatz
- Konfiguration daher entfernt

**Alte Docker‑Stacks:**
- `downloads-v1`
- `services-old`
- `test-stacks`

**Empfehlung:** Nicht reaktivieren — ersetzen durch den neuen unified Stack auf VM102.

---

## 19. Wartung, Pflege & Weiterentwicklung

### Regelmäßige Tasks

**Docker:**
- Watchtower überwacht Auto‑Updates

**Proxmox:**
- Monatliche Kernel‑Updates

**Tailscale:**
- Key‑Check alle 6 Monate

**Snapshots:**
- VM101 & VM102 monatlich

**Backups:**
- Quartalsweise extern sichern

### Langfristige Erweiterungen
- Spark GPU Node Integration (Phase 4)
- Vollständige Anna's Archive Automatisierung
- Globale PDF/A Transformation (Phase 6)
- KI‑gestützte Suche durch Vektor‑DB

---

**Ende des vollständigen Masterdokuments.**


