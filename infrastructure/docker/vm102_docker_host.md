<!-- Reality Block
last_update: 2026-09-16
status: draft
scope:
  summary: "VM102 (docker-apps): Docker Host, Remote Admin, typische Services/Ports und sichere Hinweise."
  in_scope:
    - base install
    - remote docker API (doc + risk note)
    - troubleshooting commands
  out_of_scope:
    - full docker-compose stacks
    - secrets (passwords, auth keys)
notes:
  - "Quelle: konsolidiert aus Proxmox Masterdocs (VM102 Abschnitt)."
-->

# VM102 – Docker Host (docker-apps)

## Zweck
VM102 ist dein zentraler Docker‑Host für Apps/Downloader/Utilities.

## Sizing / Ressourcen (Reality Check)

Wenn auf VM102 mehrere Stacks parallel laufen (z. B. Nextcloud + DB + Redis + Proxy), ist VM102 schnell der Engpass.

Empfehlung als Baseline:
- **2 vCPU**
- **8 GB RAM**

Wenn VM102 dauerhaft „rot“ läuft (RAM permanent >80%, viel IO), sind **10–12 GB RAM** realistischer.

## Basisinstallation (Debian)

```bash
apt update && apt install -y docker.io docker-compose-plugin
systemctl enable docker
```

## Remote Docker API (Achtung)

In den Proxmox‑Docs ist ein Setup mit `tcp://0.0.0.0:2375` beschrieben. Das ist **ohne TLS unsicher**, wenn es außerhalb eines privaten Netzes erreichbar ist.

Empfehlung (minimal sicher):
- Nur nutzen, wenn VM102 **nicht** öffentlich erreichbar ist.
- Exponierung nur über **Tailscale** (oder Firewall nur für VM105).

Beispiel (wie dokumentiert):

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

## Troubleshooting – Quick Commands

```bash
docker network ls
docker network inspect bridge
docker network prune
docker compose down && docker compose up -d
docker logs <container>
```

## Telegram → Calibre (PDF-Export)

Auf VM102 liegt **telegram-mcp** unter `/home/user/telegram-research/` (MCP per Tailscale, Session in `.env` — nicht committen).

**Push-Kette (2026-09-16):** SSH-Key `user@docker-apps` → `root@192.168.0.50` in `authorized_keys`; Test `ssh root@192.168.0.50 echo ok`. Push per `rsync` (falls installiert) oder **scp-Fallback** im Skript.

| Was | Pfad / Hinweis |
|---|---|
| Export-Skript (Repo) | `infrastructure/docker/scripts/telegram_pdf_export.py` |
| Auf VM102 | `/home/user/telegram-research/scripts/` (nach Deploy kopieren) |
| Lokaler Staging-Ordner | `/home/user/telegram-research/downloads/telegram-pdf/` |
| Telegram-Staging (pve) | `/mnt/bigdata/archive/incoming/telegram-pdf/` |
| **Eigene Bücher (Drop-Zone)** | **`/mnt/bigdata/archive/incoming/books-manual/`** auf **pve** (PDF/EPUB/MOBI/AZW3) |
| Calibre sichtbar (nomad/NFS) | `/mnt/bigdata/nomad-storage/books/incoming/books-manual/` (gleicher Inhalt nach Sync) |

**Eigene Beschaffung → Kette:** Dateien in `books-manual` legen, dann auf pve:

```bash
cp -a /mnt/bigdata/archive/incoming/books-manual/* \
  /mnt/bigdata/archive/nomad-storage/books/incoming/books-manual/
```

Vom Laptop (Tailscale/ LAN): `scp *.pdf pve:/mnt/bigdata/archive/incoming/books-manual/` — danach `cp` wie oben. In **Calibre-Web** (`:8420`, DB `/books`) Ordner **`/books/incoming/books-manual`** oder **`/books/incoming/telegram-pdf`** hinzufügen/importieren.

```bash
# Dry-run (Secret Lib chat_id default -1001344875575)
~/telegram-research/scripts/telegram_pdf_export.sh --query Prepping --limit 20 --dry-run

# Download + Push (SSH-Key user@docker-apps → root@192.168.0.50; rsync oder scp-Fallback)
RSYNC_TARGET='root@192.168.0.50:/mnt/bigdata/archive/incoming/telegram-pdf/' \
  ~/telegram-research/scripts/telegram_pdf_export.sh --query BBK --push

# Themen-Scan ohne Download (Krisen, Essen, Technik, Community, …)
~/telegram-research/scripts/telegram_pdf_export.sh --discover --limit 35
```

**MCP-Hinweis:** Wenn `TELEGRAM_EXPOSED_TOOLS=read-only`, fehlt `download_media` in Cursor — der CLI-Export nutzt dieselbe Telethon-Session direkt.

### Calibre-Web (Supply Depot)

**Anleitung neue Bücher:** [calibre_buch_workflow.md](../proxmox/02_operations/calibre_buch_workflow.md) (Staging, `calibredb add`, Modell A, Neustart bei Pfad-Änderung).


