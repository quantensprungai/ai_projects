#!/bin/bash
# Flora-Binding und Pairing prüfen – auf VM102 ausführen
# ssh user@docker-apps
# bash /tmp/check_flora_binding.sh

echo "=== 1. Flora-Bindings in Config (mit peer.id) ==="
grep -A5 '"agentId": "flora"' ~/.clawdbot-personal/clawdbot.json 2>/dev/null || echo "Kein flora-Binding gefunden!"

echo ""
echo "=== 2. Pending Pairings (Flora muss gerade eine Nachricht geschickt haben) ==="
~/.clawdbot/bin/clawdbot --profile personal pairing list signal 2>/dev/null || echo "Befehl fehlgeschlagen"

echo ""
echo "=== 3. Letzte Gateway-Logs ==="
journalctl --user -u clawdbot-gateway-personal.service -n 50 --no-pager 2>/dev/null | grep -iE "flora|delivered|pairing|agent:" | tail -n 15
