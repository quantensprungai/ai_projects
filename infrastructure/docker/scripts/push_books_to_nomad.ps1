# Auf dem Rechner ausführen, der die Dateien hat (z. B. externer Laptop he5013).
# Voraussetzung: OpenSSH-Client, `ssh pve` funktioniert (Tailscale/LAN).
param(
    [Parameter(Mandatory = $false)]
    [string]$Source = "$env:USERPROFILE\Downloads\Bücher",
    [string]$PveHost = "pve",
    [string]$RemoteIncoming = "/mnt/bigdata/archive/incoming/books-manual",
    [string]$RemoteCalibre = "/mnt/bigdata/archive/nomad-storage/books/incoming/books-manual"
)

$ErrorActionPreference = "Stop"
if (-not (Test-Path $Source)) {
    Write-Error "Quellordner fehlt: $Source"
}

$files = Get-ChildItem -Path $Source -File | Where-Object {
    $_.Extension -match '^\.(pdf|epub|mobi|azw3)$'
}
Write-Host "Gefunden: $($files.Count) Dateien in $Source"

if ($files.Count -eq 0) {
    Write-Error "Keine PDF/EPUB/MOBI im Ordner."
}

foreach ($f in $files) {
    scp -o BatchMode=yes $f.FullName "${PveHost}:${RemoteIncoming}/"
    Write-Host "OK scp $($f.Name)"
}

ssh $PveHost @"
set -e
mkdir -p '$RemoteIncoming' '$RemoteCalibre'
cp -a '$RemoteIncoming/'* '$RemoteCalibre/' 2>/dev/null || true
calibredb add '$RemoteCalibre/'* --automerge=ignore --duplicates \
  --with-library=/mnt/bigdata/archive/nomad-storage/books
sqlite3 /mnt/bigdata/archive/nomad-storage/books/metadata.db 'select count(*) from books;'
"@

Write-Host "Fertig. Calibre-Web neu laden: http://100.97.253.109:8420"
