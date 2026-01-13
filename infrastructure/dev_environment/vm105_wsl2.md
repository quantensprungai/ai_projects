<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "WSL2 Setup & Troubleshooting für VM105 (Windows 11 in Proxmox)."
  in_scope:
    - wsl2 checks
    - common fixes
  out_of_scope:
    - storing credentials
notes:
  - "Quelle: Proxmox Teil 2 (WSL2 Deep Debugging) – extrahiert."
-->

# VM105 – WSL2 (Setup & Debugging)

## WSL Version prüfen

```powershell
wsl --list --verbose
```

Erwartet (Beispiel):

```text
Ubuntu    Running      2
```

## WSL2 startet nicht / Fehler 0x80370114

```powershell
wsl --update
wsl --set-default-version 2
```

Wenn “Hardware virtualization must be enabled”:
- BIOS/UEFI: VT‑x/AMD‑V aktivieren (Host)

## Node.js / npm – EACCES Fehler

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
```

`~/.bashrc` ergänzen:

```bash
export PATH=~/.npm-global/bin:$PATH
```


