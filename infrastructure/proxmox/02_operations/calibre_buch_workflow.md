<!-- Reality Block
last_update: 2026-09-16
status: stable
scope:
  summary: "Checkliste: neue Bücher (Telegram, manuell) → bigdata → Calibre-Web auf NOMAD."
  in_scope:
    - Drop-Zonen auf pve
    - calibredb import
    - Calibre-Web Pfad-Modell A
    - Fehler (kaputte PDF, Container-Neustart)
  out_of_scope:
    - Telegram-Skript-Entwicklung (vm102_docker_host.md)
    - NOMAD-Erstinstallation (vm103_nomad_planung.md)
notes:
  - "Calibre-Web: http://100.97.253.109:8420 — Bibliothek auf NFS nomad-storage/books."
  - "Befehle Import: root auf pve (SSH oder Proxmox-Shell)."
-->

# Calibre-Bibliothek — neue Werke hinzufügen

Kurz-Checkliste, damit Cover, Download und Metadaten in **Calibre-Web** funktionieren.

## Einmalig / selten (Einstellungen)

| Einstellung | Wert |
|---|---|
| **Calibre-Web URL** | http://100.97.253.109:8420 |
| **Admin → Database location** | `/books` |
| **Separate book files from library** | **Aus** |
| **Secondary path** | **leer** |
| **Nach Pfad-Änderung** | App in **NOMAD** (:8080) **Stop → Start**, dann Admin → DB **neu verbinden** |

> Modell **A**: Dateien liegen nach Import unter `/books/<Autor>/<Titel> (ID)/`. Staging-Ordner `incoming/…` sind nur Zwischenablage.

---

## Weg 1 — Eigene Dateien (PDF / EPUB / MOBI)

### 1. Ablegen (Staging auf pve)

Vom PC (Tailscale oder LAN):

```bash
scp *.pdf *.epub *.mobi root@pve:/mnt/bigdata/archive/incoming/books-manual/
```

Alternativ: WinSCP → Host `192.168.0.50` oder Tailscale-IP von **pve**, Zielordner wie oben.

### 2. Import (auf pve als root)

```bash
cp -a /mnt/bigdata/archive/incoming/books-manual/* \
  /mnt/bigdata/archive/nomad-storage/books/incoming/books-manual/

calibredb add /mnt/bigdata/archive/nomad-storage/books/incoming/books-manual/* \
  --automerge=ignore --duplicates \
  --with-library=/mnt/bigdata/archive/nomad-storage/books
```

### 3. Prüfen

- Calibre-Web neu laden (Strg+F5).
- Titel erscheinen unter **Bücher**; **PDF** meist per **Download** (nicht Browser-Reader).

Optional Staging leeren (nur wenn alles in der Bibliothek ist):

```bash
rm -f /mnt/bigdata/archive/incoming/books-manual/*
```

---

## Weg 2 — Telegram (Secret Library o. ä.)

Auf **docker-apps** (VM102), siehe auch [vm102_docker_host.md](../../docker/vm102_docker_host.md):

```bash
RSYNC_TARGET='root@192.168.0.50:/mnt/bigdata/archive/incoming/telegram-pdf/' \
  ~/telegram-research/scripts/telegram_pdf_export.sh --query "Suchbegriff" --limit 25 --push
```

Danach **auf pve**:

```bash
cp -a /mnt/bigdata/archive/incoming/telegram-pdf/*.pdf \
  /mnt/bigdata/archive/nomad-storage/books/incoming/telegram-pdf/ 2>/dev/null || true

calibredb add /mnt/bigdata/archive/nomad-storage/books/incoming/telegram-pdf/*.pdf \
  --automerge=ignore --duplicates \
  --with-library=/mnt/bigdata/archive/nomad-storage/books
```

Gezielt eine Message-ID:

```bash
~/telegram-research/scripts/telegram_pdf_export.sh --message-id 12345 --push
# dann calibredb add wie oben
```

---

## Kaputte PDFs (xref / Nitro-XMP)

Calibre meldet `Syntax Error`, `Untitled`, oder bricht ab:

```bash
apt install -y qpdf
qpdf --replace-input "/mnt/bigdata/archive/.../datei.pdf"
calibredb add "/mnt/bigdata/.../datei.pdf" \
  --with-library=/mnt/bigdata/archive/nomad-storage/books
```

---

## Pfade (Merksatz)

| Rolle | Pfad auf **pve** |
|---|---|
| Staging manuell | `/mnt/bigdata/archive/incoming/books-manual/` |
| Staging Telegram | `/mnt/bigdata/archive/incoming/telegram-pdf/` |
| NFS-Spiegel (optional vor Import) | `…/nomad-storage/books/incoming/books-manual/` bzw. `…/telegram-pdf/` |
| **Calibre-Bibliothek** | `/mnt/bigdata/archive/nomad-storage/books/` (`metadata.db` hier) |

---

## SSH vom externen Laptop

Tailscale erlaubt oft **nicht** `ssh he5013@pve` → **`ssh root@pve`** oder **`root@192.168.0.50`**, WinSCP mit gleichem User.

---

## Skripte im Repo

| Datei | Zweck |
|---|---|
| [push_books_to_nomad.ps1](../../docker/scripts/push_books_to_nomad.ps1) | Windows: Ordner → pve + Import (wenn `ssh pve` geht) |
| [telegram_pdf_export.py](../../docker/scripts/telegram_pdf_export.py) | Telegram-PDF-Export |
| [fix_calibre_split.sql](../../docker/scripts/fix_calibre_split.sql) | Notfall: Split in app.db aus (nur bei Pfad-Chaos) |
