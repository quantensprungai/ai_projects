#!/bin/bash
# Schnelle Diagnose – auf VM102 ausführen wenn nichts mehr funktioniert
echo "=== 1. Gateway-Status ==="
systemctl --user is-active clawdbot-gateway-personal.service 2>/dev/null || echo "NICHT AKTIV"

echo ""
echo "=== 2. Letzte Gateway-Logs (Fehler) ==="
journalctl --user -u clawdbot-gateway-personal.service -n 30 --no-pager 2>/dev/null | tail -25

echo ""
echo "=== 3. signal-cli Daemon (Port 8081) ==="
ss -tlnp 2>/dev/null | grep -E "8080|8081" || echo "Kein Signal-Daemon auf 8080/8081?"

echo ""
echo "=== 4. Config JSON gültig? ==="
python3 -c "
import json
try:
    with open('/home/user/.clawdbot-personal/clawdbot.json') as f:
        json.load(f)
    print('JSON OK')
except Exception as e:
    print('FEHLER:', e)
" 2>/dev/null || echo "Config prüfen fehlgeschlagen"

echo ""
echo "=== 5. channels.signal (evtl. Problem?) ==="
python3 -c "
import json
try:
    with open('/home/user/.clawdbot-personal/clawdbot.json') as f:
        c = json.load(f)
    sig = c.get('channels', {}).get('signal', {})
    print('channels.signal:', sig)
except Exception as e:
    print('Fehler:', e)
" 2>/dev/null
