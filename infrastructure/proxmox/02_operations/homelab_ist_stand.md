<!-- Reality Block
last_update: 2026-09-11
status: stable
# last_update reflects VM103 Debian install + LAN IP correction (0.x not 188.x)
scope:
  summary: "Aktueller Ist-Stand Proxmox-Homelab (Hardware, VMs, Storage, Tailscale) — zentrale Referenz."
  in_scope:
    - hardware inventory
    - VM/CT inventory (IDs, RAM, Disk)
    - storage layout (local, local-lvm, bigdata)
    - tailscale status notes
    - planned roles (NOMAD, Nextcloud, Archiv)
  out_of_scope:
    - executing changes on pve
    - credentials
notes:
  - "Quelle: Proxmox UI Screenshots + User-Input 2026-09-09."
  - "Tailscale IPs: tailscale status / Admin-Panel ist Quelle der Wahrheit."
-->

# Homelab Ist-Stand (Proxmox)

**Zentrale Referenz** für Hardware, VMs und Storage. Ältere VM-Listen in `01_setup/1_proxmox-komplettsetup.md` können abweichen — **dieses Dokument hat Vorrang** bei Ist-Fragen.

## Physische Hardware (Host)

| Komponente | Ist |
|---|---|
| Gerät | Lenovo ThinkStation P330 Tower (2nd Gen) |
| CPU | Intel Xeon E-2234 (4C/8T, bis ~4,8 GHz) — Proxmox zeigt **8 CPUs** (HT) |
| RAM | **46 GiB** (Erweiterung nachgerüstet; `free -h` auf pve) |
| System-SSD | **Samsung 990 PRO 2 TB** NVMe → LVM `local-lvm` ~1,84 TB |
| Archiv-Platte | **Toshiba MG10 20 TB** (`/dev/sda1` ext4 → `/mnt/bigdata`) |
| GPU | NVIDIA Quadro P620 2 GB (Display; **nicht** für LLM) |
| Hypervisor | Proxmox VE auf Node `pve` |

> **Hinweis:** Ältere Doku nannte 32/48 GB — **Ist: 46 GiB** (Stand 2026-09-09). Swap-Nutzung (~6 GiB) trotzdem beobachten.

## Storage

| Storage | Typ | Kapazität | Content (Proxmox) | Rolle |
|---|---|---|---|---|
| `local-lvm` | LVM-Thin | ~1,84 TB | Disk image, Container | VM-/CT-Bootdisks |
| `local` | Directory | ~101 GB | Backup, ISO, Templates | ISOs, kleine Backups |
| `bigdata` | Directory | ~19,92 TB | **Backup** (Proxmox-UI) | vzdump-Backups + **manuell** Archiv-Ordner möglich |

### bigdata — nicht nur „leerer Platz“

Proxmox registriert `bigdata` mit `content: backup`. Das bedeutet:

- **Proxmox verwaltet** dort primär `dump/` (vzdump-Dateien).
- **Auf Dateisystem-Ebene** können zusätzliche Ordner existieren oder angelegt werden (z. B. `archive/`, `nextcloud/`, `incoming/`).
- Diese Extra-Ordner erscheinen **nicht** automatisch als Proxmox-Storage — sie werden per **Bind-Mount / SMB / NFS** an VMs gehängt.

**Stand 2026-09-10:** ~**6 %** belegt (~1 TB von ~20 TB; `df` auf nomad: `1001G` used). `archive/nomad-storage/` wächst durch NOMAD-Downloads (Maps ~75 GB, ZIMs ~800 MB+). NFS-Export aktiv (siehe `bigdata_archive_setup.md`).

**Wichtig:** `storage.cfg` hatte `prune-backups keep-all=1` (= alles behalten). Mit Backup-Job-Retention korrigieren.

Geplante Ordnerstruktur (auf dem Host, Pfad je nach `storage.cfg` — typisch `/mnt/bigdata/`):

```text
/mnt/bigdata/
├── dump/                 # vzdump (Proxmox Backup)
├── archive/
│   ├── zim/              # Kiwix / NOMAD große ZIMs
│   ├── videos/           # yt-dlp, Offline-Video
│   ├── books/            # AA-Downloads, Calibre
│   └── laptops/          # Rettungs-Kopien alter Rechner
├── nextcloud/            # NC-Daten (wenn lokal migriert)
└── incoming/             # Staging vor Sortierung
```

Pfad auf `pve` prüfen: `grep bigdata /etc/pve/storage.cfg` und `ls -la <path>`.

## VMs und Container (Ist)

| Typ | ID | Name | RAM | vCPU | Bootdisk | Status (2026-09) | Rolle |
|---|---|---|---|---|---|---|---|
| VM | 101 | management | 2 GB | 1 | 20 GB | running | RustDesk, Portainer, Tailscale |
| VM | 102 | docker-apps | 12 GB | 2 | 80 GB | running (~93 % RAM) | Docker, AA-Toolkit, qBittorrent |
| VM | 103 | dev-environment | 8 GB | 2 | 80 GB | **running** | **NOMAD** (nomad): Tailscale `100.97.253.109`, `:8080`/`:8090`, Storage → bigdata, Downloads aktiv |
| VM | 104 | Windows11-Dev | 6 GB | 4 | — | **stopped** | Alt/ungenutzt; Windows |
| VM | 105 | Windows11-Pro | 24 GB | 4 | **800 GB** | running | Dev/Cursor (win11pro105) |
| CT | 110 | homeassistant | 2 GB | 2 | ~16 GB | running | Smart Home (aktuell kaum genutzt) |

### RAM-Realität (46 GiB Host)

**Aktuell laufend:** 101+102+105+110 ≈ **40 GB** zugewiesen; **~34 GiB** belegt, **~12 GiB** verfügbar, **~6 GiB Swap** in Nutzung.

Empfehlung für NOMAD auf 103:

- VM103: **8 GB** RAM (NOMAD ohne lokale KI) — passt mit 46 GiB Host
- CT 110 **stoppen** wenn HA ungenutzt
- VM 104 nicht starten

### Warum VM103 für NOMAD, nicht VM104?

| | VM103 dev-environment | VM104 Windows11-Dev |
|---|---|---|
| OS | Linux (Debian/Ubuntu erwartet) | **Windows 11** |
| NOMAD | Docker + Installer/Compose **nativ** | nur WSL2 (community path, schlechter) |
| bigdata mount | Bind-Mount / NFS einfach | umständlicher |
| Empfehlung | **NOMAD-Host** | nur wenn du Windows brauchst; sonst freigeben |

VM104 lohnt sich für NOMAD **nicht**, weil NOMAD auf **Linux + Docker** läuft. VM104 könnte gelöscht oder durch eine zweite Linux-VM ersetzt werden — aber 103 ist schon da.

### vCPU-Umverteilung

Xeon E-2234 = **4 physische Kerne**. Zugewiesen (wenn alles an): 1+2+2+4+4+2 = **15 vCPUs** → Overcommit normal.

Für NOMAD auf 103 reichen **2 vCPUs**. Kein großes Umschichten nötig, solange 104/103 gestoppt bleiben. Optional: VM105 von 4 auf 3 vCPU reduzieren, wenn CPU-bound.

## Tailscale / Remote-Zugriff

| Maschine | Tailscale-Name | SSH | Stand (2026-09-10) |
|---|---|---|---|
| Proxmox Host | `pve` | enabled | **Last seen Juli** — oft offline im Tailnet |
| VM102 | `docker-apps` | enabled | connected |
| VM101 | `management` | enabled | connected |
| VM103 | `nomad` | enabled | **`100.97.253.109`** — primärer Zugriff NOMAD + `ssh nomad` |
| VM105 | `win11pro105` | — | connected |
| Dell-Laptop | `me230701` | Windows, kein OpenSSH erwartet | **`100.125.227.52`** (2026-09-11) |
| Spark | `spark-56d0` | enabled | connected |

**pve SSH (empfohlen, 10 Min):** Klassischer Key wie bei nomad — zuverlässiger als Tailscale-SSH (ACL). Auf pve-Shell Public Key nach `/root/.ssh/authorized_keys`, Windows `~/.ssh/config` Host `pve` → `100.115.71.71`, User `root`. Danach `ssh pve` von VM105; Cursor kann `lsblk`/rclone/USB.

**KI/Cursor-Zugriff auf `pve`:** Zwei Hürden:

1. **`pve` im Tailnet connected** (nicht „last seen July“, kein `NoState`)
2. **Tailscale ACL** erlaubt SSH vom Client (z. B. `win11pro105`) — sonst: `tailnet policy does not permit you to SSH`

**Tailscale auf pve (2026-09-09):** `tailscale login` → „Login successful“. DNS zu `controlplane.tailscale.com` war zeitweise kaputt; IP-Ping 1.1.1.1 ging trotzdem.

```bash
# Auf pve als root (kein sudo)
tailscale login    # gibt URL aus → im Browser auf VM105 öffnen → Gerät bestätigen
tailscale up --ssh
tailscale status
```

**Tailscale SSH-ACL:** Alle drei Regeln **parallel** behalten (nicht ersetzen):

| Regel | `dst` | `users` |
|---|---|---|
| spark | `tag:spark` | `root`, `autogroup:nonroot` |
| docker-apps | `tag:dockerapps` | `user`, `autogroup:nonroot` |
| self (pve, …) | `autogroup:self` | `root`, `autogroup:nonroot` |

Wenn `dockerapps` durch `autogroup:self` **ersetzt** wurde → `dockerapps`-Block **zurück** in die ACL-JSON.

## LAN / Netzwerk (Ist 2026-09-09)

| Host | Interface | LAN-IP | Hinweis |
|---|---|---|---|
| **pve** | `vmbr0` | **`192.168.0.50/24`** | `ip -4 addr show vmbr0` auf pve |
| **VM103 nomad** | `ens18` | **DHCP** (z. B. `.13`, wechselt) | `hostname -I` auf nomad; keine Fritzbox-Reservierung nötig |
| Gateway (Fritzbox) | — | vermutlich `192.168.0.1` | — |

> **Doku-Korrektur:** Ältere Docs (`01_setup/`) nennen **`192.168.188.x`** — **veraltet**. Ist: **`192.168.0.0/24`**, pve **`192.168.0.50`**.

**NOMAD (VM103):** Command Center **http://100.97.253.109:8080**, Kiwix **:8090**, Dozzle **:9999** (Tailscale). Daten unter `/mnt/bigdata/nomad-storage` (NFS → pve `/mnt/bigdata/archive/nomad-storage/`). Content-Downloads laufen (Global Map ~58 %). Details: `vm103_nomad_planung.md`.

## Geplante Rollen (Architektur)

```text
pve (ThinkStation P330, 46 GiB RAM, LAN 192.168.0.50)
├── bigdata (~20 TB)
│   ├── dump/           Backups (mit Retention, siehe proxmox_backups.md)
│   └── archive/        ZIMs, Videos, Bücher, Laptop-Rettung, NC-Daten
├── VM102 docker-apps   AA-Toolkit, Downloads, Docker-Utilities
├── VM103 nomad         NOMAD :8080/:8090, Storage auf bigdata (ohne lokale KI → Spark)
├── VM105 win11pro105   Dev-Workspace
├── VM101 management    Admin
└── Spark (extern)      KI-Inference für NOMAD/HD-SaaS
```

**NOMAD + bigdata:** NOMAD-System (Docker, DB) auf VM103-Disk (~80 GB). Große ZIMs/Videos auf `bigdata/archive/` per Bind-Mount in NOMAD-Storage-Pfad — **sinnvoll und empfohlen**.

**Nextcloud:** Datenverzeichnis auf `bigdata/nextcloud/`, App in VM103 oder VM102 — **nicht** in vzdump `dump/`.

**Alte Laptops retten:** Dateien nach `bigdata/incoming/` oder `archive/laptops/<name>/` (USB hinten am pve-Host, siehe `bigdata_archive_setup.md`) → erst dann Windows zurücksetzen.

## Geparkt (2026-09-11) — nicht vergessen

Aktive Arbeit: **Dell sichern → Windows Reset**; Rest liegt, bis NOMAD-Downloads und Mirror stehen.

| Spur | Status | Nächster Schritt |
|---|---|---|
| NOMAD Content-Queue | läuft auf bigdata | nicht `stop_nomad.sh`; Wikipedia EN maxi wartet |
| **Dell-Laptop sichern** | **jetzt** | USB an pve hinten → `lsblk` → rsync nach `archive/laptops/dell/` |
| Dell: Windows Reset | nach Backup-Stichprobe | BitLocker-Recovery + OEM-Lizenz (Digital License) |
| Dell: dual boot Omarchy | optional, **nach** Windows | zweites System; NOMAD-Simple nur wenn extra Linux-Partition gewollt |
| Dell: NOMAD Simple | optional | leichtgewichtig, **nicht** VM103 ersetzen |
| ThinkPad + Gaming-PC + WD 2,7 TB | später | gleiches Muster; WD war vermutlich manuelles Kopieren |
| Nextcloud NX10 Mirror | rclone-Remotes `nx10-admin/heiko/lily` auf pve | `rclone sync` nach `archive/nextcloud-mirror/<User>/`; Lily-Passwort offen |
| NC lokal umschalten | **nicht jetzt** | erst Mirror voll + lokale Instanz |
| Spark → NOMAD KI | geparkt | Endpoint `:30001`, kein ACL-Thema |
| Fotos/Videos sortieren | geparkt | erst kopieren, dann Immich/Czkawka auf bigdata — nicht in-place auf vollen Platten |
| Eigene PDFs | Calibre-Web (Supply Depot), nicht Kiwix | Workflow: `calibre_buch_workflow.md` |
| Website→ZIM | Zimit (CLI), nicht NOMAD-UI | |
| YouTube→ZIM | **youtube2zim außerhalb NOMAD**; API-Key Google Cloud; **kein** Odysee | Creator Packs in UI = fertige ZIMs, keine Link-Eingabe |
| Tailscale ACL nomad | bewusst übersprungen | `ssh nomad` reicht |
| VM102 docker-apps | Tailscale zeitweise offline | NC-Check dort später |

## Verwandte Doku

| Thema | Datei |
|---|---|
| bigdata Archiv + NFS/SMB | `bigdata_archive_setup.md` |
| VM103 NOMAD Planung | `vm103_nomad_planung.md` |
| Calibre neue Bücher | `calibre_buch_workflow.md` |
| Backup + Retention + Prune | `infrastructure/backups/proxmox_backups.md` |
| Master-Setup (historisch) | `infrastructure/proxmox/01_setup/1_proxmox-komplettsetup.md` |
| VM102 Docker | `infrastructure/docker/vm102_docker_host.md` |
| Tailscale | `infrastructure/tailscale/machines.md` |
| AA-Toolkit | `projects/annas_archive_toolkit/` |
