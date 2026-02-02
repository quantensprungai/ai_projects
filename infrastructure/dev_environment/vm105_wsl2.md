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

## Performance-Tuning (wenn VM105 “in die Knie geht”)

Typisches Symptom: Cursor + TypeScript Indexing + Docker Desktop/WSL2 fühlen sich „zäh“ an, UI hängt, Fans drehen hoch.
In unserem Setup ist VM105 **eine Windows‑VM auf einem Proxmox Host**. Damit sind Performance-Probleme oft **Ressourcen-Contention** (vCPU/RAM/IO), nicht ein einzelner Bug.

### 1) Proxmox CPU-Passthrough (Basis)

- VM105 CPU Type: **`host`** (sonst schlechtere Performance, und Nested Virtualization kann kaputt sein).
- Nested Virtualization muss „sauber“ durchgereicht sein (siehe Checks oben).

### 2) Docker Desktop Ressourcen limitieren (damit Windows/Cursor nicht verhungern)

Wenn Docker Desktop „alles nimmt“, wird die VM unbenutzbar. Setze Limits und taste dich hoch:

- **CPUs**: Start mit **2–3**
- **Memory**: Start mit **8–10 GB**
- **Swap**: **1–2 GB**
- **Disk image size**: nicht zu klein (z. B. **80–120 GB**), sonst häufige „no space left“-Probleme

Ziel: VM bleibt **interaktiv**, Container dürfen „nur so schnell wie nötig“ sein.

### 3) WSL2 hart deckeln (empfohlen)

Zusätzlich/alternativ kann WSL2 begrenzt werden, damit Docker/WSL2 nicht unendlich RAM/CPU wachsen:

Datei anlegen/ändern: **`%UserProfile%\.wslconfig`**

```ini
[wsl2]
memory=10GB
processors=3
swap=2GB
```

Danach WSL neu starten:

```powershell
wsl --shutdown
```

### 4) Dateisystem: Node/Next im Linux-FS betreiben (großer Hebel)

Für Projekte mit vielen kleinen Dateien (`node_modules`, `.next`, pnpm store):
- **Besser**: Repo **im WSL Linux-Filesystem** (z. B. `/home/<user>/…`)
- **Schlechter**: Repo unter `C:\…` und in WSL via `/mnt/c/…` arbeiten

Das reduziert IO‑Overhead und macht Watcher/Builds spürbar schneller.

### 5) Reality Check: Host-Limits sind echte Limits

Wenn der Proxmox Host nur wenige Kerne/RAM hat, hilft “in der VM tunen” nur begrenzt:
- viele parallele Workspaces/Watcher + Docker + mehrere VMs → CPU/RAM/IO‑Contention
- dann: Workspaces reduzieren, Docker auslagern (separate VM), oder Host upgraden

## Node.js / npm – EACCES Fehler

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
```

`~/.bashrc` ergänzen:

```bash
export PATH=~/.npm-global/bin:$PATH
```

## Docker Desktop Fehler: HCS_E_CONNECTION_TIMEOUT

### Symptom
```
There was a problem with WSL
An error occurred while running a WSL command. Please check your WSL configuration and try again.

running wslexec: The operation timed out because a response was not received from the virtual machine or container. 
Wsl/Service/RegisterDistro/CreateVm/HCS_E_CONNECTION_TIMEOUT: 
c:\windows\system32\wsl.exe --import-in-place docker-desktop <home>\appdata\local\docker\wsl\main\ext4.vhdx: 
exit status 0xffffffff
```

### Ursache
Docker Desktop kann seine WSL-Distribution nicht importieren/starten. Häufige Ursachen:
1. **Nested Virtualization nicht aktiviert** (häufigste Ursache)
2. **WSL2-Dienst hängt oder ist beschädigt**
3. **Beschädigte Docker Desktop WSL-Distribution**
4. **Ressourcenprobleme** (zu wenig RAM/CPU für WSL2)

### Lösung Schritt für Schritt

#### Schritt 0: Einfacher Restart (oft ausreichend)

**Häufig hilft bereits:**
1. Docker Desktop komplett beenden
2. VM105 neu starten
3. Docker Desktop erneut starten

Falls das nicht hilft → weiter mit Schritt 1.

#### Schritt 1: Nested Virtualization prüfen (WICHTIGSTE Prüfung)

**Auf Proxmox Host (SSH):**
```bash
# Prüfe ob Nested Virtualization aktiviert ist
cat /sys/module/kvm_intel/parameters/nested
```
Erwartet: `Y` oder `1`. Wenn `N` → aktivieren (siehe unten).

**In Proxmox GUI (VM105):**
- VM105 → **Hardware** → **Processors** → **Edit**
- **Type**: `host` (empfohlen) oder mindestens Flags mit `+vmx`
- **KVM hardware virtualization**: **Yes** (aktivieren)

**Wenn Nested Virtualization nicht aktiv ist (Proxmox Host):**
```bash
# Aktivieren (Intel)
echo "options kvm_intel nested=1" > /etc/modprobe.d/kvm-intel.conf
modprobe -r kvm_intel
modprobe kvm_intel

# Für AMD:
# echo "options kvm_amd nested=1" > /etc/modprobe.d/kvm-amd.conf
# modprobe -r kvm_amd
# modprobe kvm_amd
```
**Wichtig:** Wenn `modprobe -r` wegen laufender VMs blockiert, VM105 stoppen oder Host neu starten.

#### Schritt 2: Windows Virtualization Features prüfen

**In VM105 (PowerShell als Administrator):**
```powershell
# Prüfe ob Virtualization-Features verfügbar sind
Get-CimInstance Win32_Processor | Select-Object VirtualizationFirmwareEnabled,SecondLevelAddressTranslationExtensions,VMMonitorModeExtensions
```
Erwartet: alles **True**. Wenn False → Problem ist Proxmox/Host-Passthrough, nicht Windows.

#### Schritt 3: WSL2 komplett zurücksetzen

**In VM105 (PowerShell als Administrator):**
```powershell
# Alle WSL-Distributionen herunterfahren
wsl --shutdown

# WSL aktualisieren
wsl --update

# Prüfe WSL-Status
wsl --list --verbose
```

#### Schritt 4: Docker Desktop WSL-Distribution entfernen

**In VM105 (PowerShell als Administrator):**
```powershell
# Docker Desktop WSL-Distributionen entfernen (falls vorhanden)
wsl --unregister docker-desktop
wsl --unregister docker-desktop-data

# Docker Desktop WSL-Verzeichnis löschen (falls beschädigt)
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Docker\wsl" -ErrorAction SilentlyContinue
```

#### Schritt 5: Hyper-V Dienste neu starten

**In VM105 (PowerShell als Administrator):**
```powershell
# Hyper-V Dienste neu starten
Restart-Service vmms
Restart-Service vmcompute

# Falls das nicht hilft, Hyper-V Feature neu aktivieren:
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Hypervisor -NoRestart
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Hypervisor -NoRestart
```
**Wichtig:** Nach dem Neustart von Hyper-V Features muss VM105 neu gestartet werden.

#### Schritt 6: VM105 neu starten

Nach allen Änderungen:
1. VM105 komplett herunterfahren
2. In Proxmox prüfen, dass CPU Type = `host` und KVM hardware virtualization = `Yes`
3. VM105 starten
4. Windows vollständig booten lassen (2-3 Minuten warten)

#### Schritt 7: Docker Desktop neu installieren/starten

**In VM105:**
1. Docker Desktop starten
2. Falls Fehler weiterhin auftritt → Docker Desktop komplett deinstallieren und neu installieren

**Alternative: Docker Desktop ohne WSL2 nutzen (nur als Workaround)**
- Docker Desktop → Settings → General → **"Use the WSL 2 based engine"** deaktivieren
- **Achtung:** Deutlich schlechtere Performance, nicht empfohlen für Produktion

### Wenn nichts hilft: Alternative Docker-Setup

Falls Docker Desktop in VM105 weiterhin Probleme macht, kann Docker direkt in WSL2 installiert werden:

**In WSL2 (Ubuntu):**
```bash
# Docker in WSL2 installieren (ohne Docker Desktop)
sudo apt update
sudo apt install -y docker.io docker-compose-plugin
sudo usermod -aG docker $USER
```

Dann Docker Desktop deinstallieren und nur WSL2-Docker nutzen.


