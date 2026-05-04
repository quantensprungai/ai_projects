#!/usr/bin/env bash
# WineHQ auf Ubuntu 22.04 (jammy) – einmal ausführen: bash ~/vps-winehq-upgrade-jammy.sh
# Benötigt sudo (Passwort wird abgefragt).

set -euo pipefail

echo "==> WineHQ-Repo einrichten (jammy) …"
sudo dpkg --add-architecture i386 2>/dev/null || true
sudo mkdir -pm755 /etc/apt/keyrings
TMPKEY="$(mktemp)"
wget -qO "$TMPKEY" https://dl.winehq.org/wine-builds/winehq.key
sudo gpg --batch --dearmor -o /etc/apt/keyrings/winehq-archive-keyring.gpg "$TMPKEY"
rm -f "$TMPKEY"
echo "deb [signed-by=/etc/apt/keyrings/winehq-archive-keyring.gpg] https://dl.winehq.org/wine-builds/ubuntu/ jammy main" | sudo tee /etc/apt/sources.list.d/winehq-jammy.list

echo "==> Altes Ubuntu-Wine entfernen (Konflikte) …"
sudo apt-get remove -y --purge wine wine64 wine32 libwine libwine:i386 fonts-wine 2>/dev/null || true
sudo apt-get autoremove -y

echo "==> apt update …"
sudo apt-get update -qq

echo "==> winehq-stable installieren …"
sudo apt-get install -y --install-recommends winehq-stable

echo "==> winetricks (Hilfsskript) …"
sudo apt-get install -y winetricks

echo "==> Version:"
wine --version || true
wine64 --version || true

echo ""
echo "Fertig. Optional neues Prefix (Zeile für Zeile):"
echo "  mv ~/.wine-fx64 ~/.wine-fx64.bak-wine6"
echo "  export WINEPREFIX=\$HOME/.wine-fx64 && export WINEARCH=win64 && wineboot --init"
echo "  WINEPREFIX=\$HOME/.wine-fx64 winetricks win10"
echo "Dann Installer (im VNC-Terminal, DISPLAY gesetzt):"
echo "  cd ~/Downloads && WINEDEBUG=-all wine64 ./fxview4setup.exe"
