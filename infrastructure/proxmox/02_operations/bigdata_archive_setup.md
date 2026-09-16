<!-- Reality Block
last_update: 2026-09-16
status: stable
scope:
  summary: "bigdata: Archiv-Ordner, NFS (192.168.0.x), apt-Fix pve, VM103-Mount."
  in_scope:
    - folder layout on /mnt/bigdata
    - NFS export + mount nomad
    - pve apt enterprise/ceph fix
  out_of_scope:
    - NOMAD install steps (vm103_nomad_planung.md)
notes:
  - "LAN Ist: 192.168.0.0/24 — pve 192.168.0.50. Alte Docs mit 188.x sind veraltet."
  - "Befehle auf pve als root (Proxmox Shell oder SSH)."
-->

# bigdata — Archiv + NFS für VM103 (nomad)

## Ist (2026-09-10)

```text
Pfad:     /mnt/bigdata
Proxmox:  content backup, prune-backups keep-all=1  ← Retention im Backup-Job setzen
Belegt:   ~1 TB (~6 %); nomad-storage wächst (Maps ~75 GB, ZIMs ~800 MB+)
Frei:     ~17 TB

/mnt/bigdata/
├── dump/                          # vzdump-Backups
└── archive/
    ├── zim/
    ├── nomad-storage/
    ├── videos/
    ├── books/
    ├── laptops/
    ├── incoming/
    └── nextcloud-mirror/
```

Host: **46 GiB RAM**, Samsung 990 PRO 2 TB (LVM ~1,84 TB).

## LAN (für NFS)

| System | IP |
|---|---|
| **pve** (`vmbr0`) | **`192.168.0.50/24`** |
| **nomad** (VM103) | **DHCP** (wechselt, z. B. `.13`, `.247`) — **Tailscale `100.97.253.109`** |
| Subnetz Export | **`192.168.0.0/24`** |

> Nicht `192.168.188.x` verwenden — veraltete Doku. Prüfen: `ip -4 addr show vmbr0` auf pve.

---

## Schritt 1: `prune-backups` in storage.cfg

`keep-all=1` = alle Backups behalten. In UI oder `storage.cfg` Retention setzen (siehe `../backups/proxmox_backups.md`).

---

## Schritt 2: Archiv-Ordner (erledigt)

```bash
mkdir -p /mnt/bigdata/archive/{zim,videos,books,laptops,incoming,nextcloud-mirror,nomad-storage}
chmod -R 755 /mnt/bigdata/archive
ls -la /mnt/bigdata/archive/
```

| Pfad | Inhalt |
|---|---|
| `archive/zim/` | Wikipedia DE+EN maxi, WikiMed, … |
| `archive/nomad-storage/` | NOMAD data dir (Bind-Mount in VM) |
| `archive/books/` | AA-Downloads, Calibre |
| `archive/videos/` | yt-dlp |
| `archive/laptops/` | Rettungs-Kopien |
| `archive/nextcloud-mirror/` | Sync von Hetzner NX10 |
| `archive/incoming/telegram-pdf/` | Telegram-Export (VM102) → Calibre |
| `archive/incoming/books-manual/` | Eigene PDF/EPUB → Import siehe **[calibre_buch_workflow.md](calibre_buch_workflow.md)** |
| `archive/incoming/` | Sonstiges Staging |

---

## Schritt 3: NFS-Server auf pve (erledigt 2026-09-09)

### apt auf pve reparieren (Enterprise/Ceph 401)

**Nicht** `.sources` halb auskommentieren — ergibt „Malformed stanza“.

```bash
mv /etc/apt/sources.list.d/pve-enterprise.sources /etc/apt/sources.list.d/pve-enterprise.sources.disabled 2>/dev/null
sed -i 's/^deb /#deb /' /etc/apt/sources.list.d/pve-enterprise.list 2>/dev/null
mv /etc/apt/sources.list.d/ceph.sources /etc/apt/sources.list.d/ceph.sources.disabled 2>/dev/null
sed -i 's/^deb /#deb /' /etc/apt/sources.list.d/ceph.list 2>/dev/null

apt update
apt install -y nfs-kernel-server
```

### `/etc/exports`

```text
/mnt/bigdata/archive 192.168.0.0/24(rw,sync,no_subtree_check,no_root_squash)
```

`no_root_squash` nötig, damit Docker-Container (nomad_admin) auf NFS schreiben können.

Optional zusätzlich `192.168.188.0/24` nur wenn dieses Subnetz wirklich existiert.

```bash
exportfs -ra
systemctl enable --now nfs-server
showmount -e localhost
# Erwartung: /mnt/bigdata/archive 192.168.0.0/24
```

Bei Paket-Update: **`/etc/exports` → „keep local version“** (nicht Maintainer-Version).

---

## Schritt 4: Mount auf nomad (VM103, erledigt)

```bash
sudo apt install -y nfs-common
sudo mkdir -p /mnt/bigdata
sudo mount 192.168.0.50:/mnt/bigdata/archive /mnt/bigdata
ls /mnt/bigdata

# fstab:
# 192.168.0.50:/mnt/bigdata/archive  /mnt/bigdata  nfs  defaults,_netdev  0  0
```

NOMAD-Installer: Storage-Pfad **`/mnt/bigdata/nomad-storage`** (in `compose.yml` als Bind-Mount, Stand 2026-09-09).

**NOMAD-Downloads** (ZIMs, Global Map ~128 GB, …) landen unter `nomad-storage/` — physisch auf pve in `/mnt/bigdata/archive/nomad-storage/`. Vor erstem Download:

```bash
sudo mkdir -p /mnt/bigdata/nomad-storage
du -sh /mnt/bigdata/nomad-storage   # wächst während Content-Downloads
```

**NOMAD-Ports auf nomad:** Command Center `:8080`, Information Library (Kiwix) `:8090`.

### Troubleshooting NFS

| Symptom | Ursache | Fix |
|---|---|---|
| `ping 192.168.188.50` timeout | Falsches Subnetz | `192.168.0.50` nutzen |
| `access denied` | Export-Subnetz | `192.168.0.0/24` in `/etc/exports` |
| Mount hängt | fstab ohne funktionierenden Mount | Erst manuell mounten, dann fstab |
| `showmount` auf nomad | Paket fehlt | `nfs-common` |

---

## Schritt 5: VM-Disk von pve bearbeiten (ohne Console)

Wenn nomad-Netzwerk/SSH kaputt:

```bash
qm stop 103 --timeout 1
mount -o offset=1048576 /dev/pve/vm-103-disk-0 /mnt/nomad-fix
# Dateien unter /mnt/nomad-fix/etc/...
umount /mnt/nomad-fix
qm start 103
```

`offset=1048576` = Start Partition 1 (Sektor 2048 × 512). Alternative: `kpartx` nach `apt install kpartx`.

---

## ZIM-Größen (Plan)

| Paket | ca. | Pfad |
|---|---|---|
| Wikipedia DE maxi | ~12 GB | `archive/zim/` |
| Wikipedia EN maxi | ~95 GB | `archive/zim/` |
| Maps DACH+ | ~5–20 GB | `archive/nomad-storage/maps/` |

VM103 Boot-Disk (80 GB): nur OS + Docker — **keine** ZIMs.

---

## Hetzner NX10 (Nextcloud-Mirror) — geparkt, rclone steht

- NX10 = Storage Share 100 GB (`nx19806.your-storageshare.de`), Live-Daten **bei Hetzner** (~23 GB)
- **Nicht** umschalten, bis Mirror + lokale NC stehen
- rclone auf **pve** (User + App-Passwort, `bearer_token` leer, Advanced `n`):

| Remote | WebDAV-User | Ziel |
|---|---|---|
| `nx10-admin` | `Nextcloudadmin` | `/mnt/bigdata/archive/nextcloud-mirror/Nextcloudadmin/` |
| `nx10-heiko` | `Heiko` | `/mnt/bigdata/archive/nextcloud-mirror/Heiko/` |
| `nx10-lily` | `Lily` | `/mnt/bigdata/archive/nextcloud-mirror/Lily/` |

URL-Muster: `https://nx19806.your-storageshare.de/remote.php/dav/files/<User>/`  
`rclone lsd` muss Ordner listen (401 = falscher `user`, oft Default `nextcloud`). Dann:

```bash
rclone sync nx10-heiko: /mnt/bigdata/archive/nextcloud-mirror/Heiko/ -P --transfers 4
```

Hetzner sperrt manche Einstellungs-URLs („Seite gesperrt“) — WebDAV funktioniert trotzdem. Admin-Export/ZIP ist **kein** Instanz-Mirror.

---

## USB an pve (Laptop-Sicherung)

Stick/Platte an den **Host** (Lenovo P330), **nicht** an eine VM. Hinten bevorzugen (Front-Hub oft unzuverlässig).

**Ports (User 2026-09-11):** vorne 4× USB-A + 1× kleiner (USB-C); ein A-Port mit **SS10**. USB-Kabel zuletzt **hinten Slot 5**.

Auf **pve-Shell** (Cursor hat keinen SSH-Key auf pve):

```bash
lsblk -o NAME,SIZE,FSTYPE,LABEL,MOUNTPOINT,TRAN,MODEL
lsusb
dmesg | tail -40
```

Erwartung: extra Disk `sdb`/`sdc` (nicht nur `sda` 18,2 T und NVMe). Dann:

```bash
mkdir -p /mnt/usb-dell /mnt/bigdata/archive/laptops/dell
mount /dev/sdX1 /mnt/usb-dell          # sdX1 aus lsblk
ls -la /mnt/usb-dell
rsync -avh --progress /mnt/usb-dell/ /mnt/bigdata/archive/laptops/dell/
umount /mnt/usb-dell
```

BitLocker auf dem USB: Linux mountet nicht — auf dem Dell entsperren / unverschlüsselt kopieren. **Nichts formatieren.**

### Dell danach (geplant)

1. Stichprobe: Dateien auf bigdata öffnen  
2. BitLocker-Recovery-Key + optional Product-Key sichern  
3. Windows zurücksetzen (OEM Digital License reicht meist)  
4. Optional später: **Omarchy** als zweites Boot + **NOMAD Simple** auf dem Laptop — **ersetzt nicht** VM103

ThinkPad / Gaming-PC / WD 2,7 TB: gleiches Muster nach `archive/laptops/<name>/` bzw. `archive/incoming/wd-externe/`.

---

## Verwandte Doku

- `homelab_ist_stand.md` — IPs, Hardware
- `vm103_nomad_planung.md` — Debian-Install, nomad Ist-Stand
