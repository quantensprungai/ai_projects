<!-- Reality Block
last_update: 2026-01-13
status: stable
scope:
  summary: "VM105 (Windows 11) Remote-Display: warum Auflösung in RustDesk/Windows gesperrt ist und wie man es sauber fixt (Proxmox Display + Treiber)."
  in_scope:
    - proxmox display settings (documentation)
    - windows driver install steps (documentation)
    - rustdesk client settings (documentation)
  out_of_scope:
    - storing credentials
    - changing unrelated VM hardware
notes: []
-->

# VM105 – Remote Display (RustDesk) sauber & scharf

## Status

✅ In deinem aktuellen Setup **gelöst/verified**. Dieser Guide bleibt als Runbook, falls die Auflösung später wieder gesperrt ist.

## Symptom

- Windows zeigt nur **1280×800** und die Auflösung ist **ausgegraut**.
- RustDesk wirkt unscharf/skalierend, obwohl du “Qualität hoch” wählst.

## Ursache (typisch auf Proxmox/Windows)

Windows bekommt kein “richtiges” virtuelles Display/keinen passenden Treiber → daher sind höhere Auflösungen nicht verfügbar.

## Fix (empfohlen): Proxmox Display → VirtIO‑GPU + Treiber

### 1) Proxmox: Display auf VirtIO‑GPU stellen

In Proxmox:

- VM105 → **Hardware** → **Display** → **Edit**
- **Display = VirtIO‑GPU** (oder VirtIO‑GPU (SPICE), falls verfügbar)
- Speichern
- VM **neu starten**

> Hinweis: Wenn du aktuell “Default”/Standard‑VGA nutzt, ist 1280×800‑Lock ein häufiger Effekt.

### 2) Windows: VirtIO Guest Tools / Display Treiber installieren

In Windows VM105:

- VirtIO ISO einlegen (falls nicht schon): `virtio-win.iso`
- **Empfohlen**: `virtio-win-guest-tools.exe` ausführen (installiert Treiber gebündelt)
- Danach **neu starten**

Kontrolle:
- Gerätemanager → **Grafikkarten**
  - Erwartung: Ein VirtIO/RedHat/QEMU Display Adapter (nicht “Microsoft Basic Display Adapter”)

### 3) Windows: Auflösung setzen

Danach:
- Einstellungen → System → Anzeige
- Auflösung z. B. **1920×1080** oder **2560×1440**
- Skalierung nach Bedarf (für scharfe Schrift meist 100–125% je nach Auflösung)

## RustDesk: “Scharf statt matschig”

Im RustDesk Client:

- **Scaling/Skalierung**: **Original / 1:1** (nicht Auto)
- **Qualität**: High/Best

Wenn es danach immer noch “weich” wirkt:
- Prüfen, ob RustDesk “Smooth scaling” aktiviert hat → deaktivieren


