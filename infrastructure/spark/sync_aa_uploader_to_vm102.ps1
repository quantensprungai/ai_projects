# Sync Anna's Archive → IC Uploader (VM105 → VM102)
# Reality: Kopiert hd_saas_uploader.py (mit --sys-mode für sys_*) auf docker-apps.
# Voraussetzung: OpenSSH scp, SSH-Zugang zu docker-apps (Tailscale), Repo unter code/annas-archive-toolkit

param(
    [string]$AiProjectsRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path,
    [string]$RemoteHost = "docker-apps",
    [string]$RemoteUser = "user",
    [string]$RemotePath = "~/annas-archive-toolkit/src/hd_saas_uploader.py"
)

$ErrorActionPreference = "Stop"
$localFile = Join-Path $AiProjectsRoot "code\annas-archive-toolkit\src\hd_saas_uploader.py"

if (-not (Test-Path $localFile)) {
    Write-Error "Lokal nicht gefunden: $localFile - bitte annas-archive-toolkit unter code/ klonen oder pullen."
}

$target = "${RemoteUser}@${RemoteHost}:${RemotePath}"
Write-Host "SCP: $localFile -> $target"
scp -o BatchMode=yes -o StrictHostKeyChecking=accept-new $localFile $target
Write-Host "OK - auf VM102: python3 src/hd_saas_uploader.py --help"
