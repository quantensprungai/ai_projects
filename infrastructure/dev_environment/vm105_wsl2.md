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

## TL;DR (häufigster Blocker in Proxmox)

Wenn Docker Desktop beim Start meldet **„Virtualization support not detected“** oder WSL2 Fehler wie **0x80370114** ausgibt, fehlt fast immer **Nested Virtualization** in der Windows‑VM.

**Proxmox‑Seite (VM105):**
- CPU Type: **`host`** (oder mindestens `+vmx`)
- KVM hardware virtualization: **Yes**
- Host‑Kernel: **`kvm_intel nested=1`** (Intel) / `kvm_amd nested=1` (AMD)

**Windows‑Check (in VM105 PowerShell):**
```powershell
Get-CimInstance Win32_Processor | Select-Object VirtualizationFirmwareEnabled,SecondLevelAddressTranslationExtensions,VMMonitorModeExtensions
```
Erwartet: alles **True**. Wenn False → Problem ist Proxmox/Host‑Passthrough, nicht Windows.

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
- Proxmox Host: Nested Virtualization aktivieren (siehe unten)
- Proxmox VM105: CPU Type `host` oder Flags inkl. `+vmx`

## Docker Desktop in VM105: „Virtualization support not detected“

### Ursache
Docker Desktop nutzt WSL2/Hypervisor‑Features. In einer Proxmox‑Windows‑VM funktioniert das nur, wenn die CPU‑Virtualisierungs‑Extensions in die VM **durchgereicht** werden (Nested Virtualization inkl. SLAT/EPT).

### Fix (Proxmox Host, Intel Xeon E‑2234)
Auf dem Proxmox Host:
```bash
cat /sys/module/kvm_intel/parameters/nested
```
Erwartet: `Y` (oder `1`).

Wenn nicht aktiv:
```bash
echo "options kvm_intel nested=1" > /etc/modprobe.d/kvm-intel.conf
modprobe -r kvm_intel
modprobe kvm_intel
```
Hinweis: Wenn `modprobe -r` wegen laufender VMs blockiert, musst du entweder VMs stoppen oder einen Reboot einplanen.

### Fix (Proxmox VM105)
In Proxmox GUI:
- VM105 → **Hardware** → **Processors** → **Edit**
- **Type**: `host` (empfohlen)

Alternative (wenn ihr bewusst nicht `host` nutzt):
- VM105 → Config: `cpu: x86-64-v2-AES,flags=+vmx` (Intel)

### Windows‑Validierung
Nach VM‑Neustart:
```powershell
Get-CimInstance Win32_Processor | Select-Object VirtualizationFirmwareEnabled,SecondLevelAddressTranslationExtensions,VMMonitorModeExtensions
```
Wenn jetzt True → Docker Desktop erneut starten.

## Node.js / npm – EACCES Fehler

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
```

`~/.bashrc` ergänzen:

```bash
export PATH=~/.npm-global/bin:$PATH
```


