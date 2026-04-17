# Clawdbot Signal Setup – Checkliste

**Ziel:** Java + signal-cli installieren, Signal aktivieren, Bindings fertigstellen.

---

## Schritt 1: SSH zu VM102 (interaktiv)

**In Cursor:** Terminal → New Terminal öffnen, dann:

Öffne ein **Terminal** (PowerShell oder Cursor Terminal) und verbinde dich:

```powershell
ssh user@docker-apps
```

**Falls `docker-apps` nicht auflöst**, nutze die Tailscale-IP:

```powershell
ssh user@100.83.17.106
```

**IP prüfen:** `tailscale status` (auf VM105) – VM102 heißt `docker-apps`.

---

## Schritt 2: Java + signal-cli installieren

**Auf VM102** (nach SSH-Login).

### Option A: signal-cli native (ohne Java)

Das **Linux-native**-Build enthält Java und braucht keine separate Installation:

```bash
cd /tmp
SIGNAL_VER=0.13.24
wget https://github.com/AsamK/signal-cli/releases/download/v${SIGNAL_VER}/signal-cli-${SIGNAL_VER}-Linux-native.tar.gz
sudo tar -xzf signal-cli-${SIGNAL_VER}-Linux-native.tar.gz -C /usr/local
sudo ln -sf /usr/local/signal-cli-${SIGNAL_VER}/bin/signal-cli /usr/local/bin/signal-cli
```

### Option B: Standard-Build (mit Java)

Falls Option A nicht funktioniert:

```bash
# Java 17 (in Bookworm verfügbar – openjdk-21 evtl. nur in Backports)
sudo apt-get update
sudo apt-get install -y openjdk-17-jre

# signal-cli Standard-Build (mit Java)
cd /tmp
SIGNAL_VER=0.13.24
wget https://github.com/AsamK/signal-cli/releases/download/v${SIGNAL_VER}/signal-cli-${SIGNAL_VER}.tar.gz
sudo tar -xzf signal-cli-${SIGNAL_VER}.tar.gz -C /usr/local
sudo ln -sf /usr/local/signal-cli-${SIGNAL_VER}/bin/signal-cli /usr/local/bin/signal-cli
```

**Hinweis:** Der Dateiname ist `-Linux-native.tar.gz` bzw. `.tar.gz` (nicht `-Linux.tar.gz`).

Prüfen:

```bash
signal-cli --version
```

---

## Schritt 3: Signal-Bot-Account verlinken

**Wichtig:** Nutze eine **separate Nummer** für den Bot (nicht deine Privatnummer). Oder: eine eigene Nummer, die du als Hauptaccount für den Bot nutzen willst.

**Vorheriger Account ersetzen:** Falls signal-cli bereits einen Account hat, zuerst registrieren:

```bash
signal-cli -a +49NEUE_NUMMER register
# Oder: alten Account entfernen, dann link mit neuer Nummer
```

`signal-cli link` zeigt einen `sgnl://`-Link – **keinen** QR-Code. Die Signal-App braucht aber einen QR-Code. Lösung: **qrencode**.

### 3a) qrencode installieren (einmalig)

```bash
sudo apt-get install -y qrencode
```

### 3b) Link mit QR-Code im Terminal

```bash
signal-cli link -n "Clawdbot" | tee /tmp/signal-link.txt | xargs -I {} qrencode -t utf8 "{}"
```

- QR-Code erscheint als Terminal-Text
- **Signal** auf dem Handy (der Nummer, die du für den Bot nutzen willst): Einstellungen → Verknüpfte Geräte → Gerät verknüpfen
- QR-Code mit der Handykamera scannen

**Nicht beenden** – der Prozess wartet auf den Scan und beendet sich danach.

### 3c) Alternative: QR als PNG speichern

```bash
signal-cli link -n "Clawdbot" | tee /tmp/signal-link.txt | xargs -I {} qrencode -o /tmp/signal-qr.png -v 10 "{}"
```

Dann per SCP auf VM105 kopieren:

```powershell
scp user@docker-apps:/tmp/signal-qr.png .
# Datei öffnen und mit Signal scannen
```

### Troubleshooting

- **"sgnl://-Link funktioniert nicht"**: Den Link nicht im Browser öffnen – nur als QR in Signal scannen.
- **"Connection closed"**: Link abgelaufen. Befehl erneut ausführen und schnell scannen.
- **Bereits verknüpfter Account:** `signal-cli listAccounts` zeigt vorhandene Accounts. Zum Wechseln: `signal-cli -a +49ALT remove` (oder neuen Account mit `-a` anlegen).

Nach dem erfolgreichen Link wird die verknüpfte Nummer angezeigt (z.B. `+49...`). **Notiere sie** – das ist `channels.signal.account`.

---

## Schritt 4+5: Config + Bindings (automatisch)

**Einfach:** Skript vom Repo per SCP auf VM102 kopieren und ausführen.

**Auf VM105 (PowerShell):**

```powershell
scp infrastructure/docker/update_clawdbot_signal_config.py user@docker-apps:/tmp/
```

**Auf VM102 (per SSH):**

```bash
python3 /tmp/update_clawdbot_signal_config.py \
  --account "+49XXXXXXXXX" \
  --heiko "+49..." \
  --noah "+49..." \
  --flora "+49..."
```

- `--account`: Die Nummer aus Schritt 3 (die du beim Link verknüpft hast)
- `--heiko`, `--noah`, `--flora`: E.164-Nummern der jeweiligen Personen
- Optional `--familie "+49..."` für eine Einzelperson; ohne bleibt das Gruppen-Binding mit Platzhalter
- `--dry-run` zeigt nur die Änderung, schreibt aber nicht

---

## Schritt 4+5: Config + Bindings (manuell)

Falls du lieber per Hand editierst:

```bash
nano ~/.clawdbot-personal/clawdbot.json
```

**channels.signal** hinzufügen/ergänzen:

```json
  "channels": {
    "signal": {
      "enabled": true,
      "account": "+49XXXXXXXXX",
      "cliPath": "signal-cli",
      "dmPolicy": "pairing",
      "allowFrom": []
    }
  }
```

**Bindings** – Platzhalter ersetzen:

| Platzhalter | Ersetzen durch |
|-------------|----------------|
| `REPLACE_HEIKO_SIGNAL` | Heikos Signal-Nummer (E.164) |
| `REPLACE_NOAH_SIGNAL` | Noahs Signal-Nummer |
| `REPLACE_FLORA_SIGNAL` | Floras Signal-Nummer |
| `REPLACE_FAMILIE_GROUP` | Signal-Gruppen-ID oder zunächst weglassen |

**Gruppen-ID für Familie:** Nachricht in die Gruppe schicken → ID erscheint in signal-cli-Logs. Oder: Starte ohne Gruppen-Binding, nutze zunächst nur DMs.

---

## Schritt 6: Gateway neu starten

```bash
systemctl --user restart clawdbot-gateway-personal.service
systemctl --user status clawdbot-gateway-personal.service
```

---

## Schritt 7: Pairing

Jede Person (Heiko, Noah, Flora) schickt eine Nachricht an die Bot-Nummer. Sie erhalten automatisch einen Pairing-Code per Signal.

**Auf VM102:**

```bash
~/.clawdbot/bin/clawdbot --profile personal pairing list signal
```

Ausgabe zeigt pending Requests mit Code. Approve:

```bash
~/.clawdbot/bin/clawdbot --profile personal pairing approve signal <CODE>
```

**Ja** – die Person erhält eine Bestätigungsnachricht per Signal und kann danach direkt chatten.

---

## Schritt 8: signal-cli-Daemon dauerhaft laufen lassen

Falls Port 8080 belegt ist, nutzt ihr einen externen Daemon auf 8081. Dieser muss **immer** laufen:

```bash
sudo apt-get install -y screen
screen -S signal
signal-cli -a +49XXXXXXXXX daemon --http 127.0.0.1:8081
```

**Detachen** = Session im Hintergrund lassen, Terminal schließen können:
- **Ctrl+A**, dann **D** drücken (nicht gleichzeitig – zuerst Ctrl+A, loslassen, dann D)
- Die Session läuft weiter. Mit `screen -r signal` wieder anzeigen.

**Alternative:** `nohup signal-cli -a +49... daemon --http 127.0.0.1:8081 > /tmp/signal.log 2>&1 &`

---

## Familie als Signal-Gruppe

**Familie = Gruppe:** Gruppen-ID ermitteln, dann Config mit `--familie <GRUPPEN_ID>` aktualisieren.

### Gruppen-ID ermitteln (auf VM102)

```bash
# 1. Optional: Gruppenliste synchronisieren (falls kürzlich beigetreten)
signal-cli -a +49XXXXXXXXX receive

# 2. Alle Gruppen mit IDs anzeigen
signal-cli -a +49XXXXXXXXX listGroups
```

Beispiel-Ausgabe: `Id: zV7XHDr+JUOEc2xGISGMm+XJH0iuuD/ldzYXtTBNUMQ= Name: Familie …`  
→ **Id** ist die Gruppen-ID (base64, ohne `+` am Anfang).

### Binding durchführen

```bash
# Skript von VM105 auf VM102 kopieren (falls noch nicht)
scp infrastructure/docker/update_clawdbot_signal_config.py user@docker-apps:/tmp/

# Auf VM102: Config mit Gruppen-ID aktualisieren
python3 /tmp/update_clawdbot_signal_config.py \
  --account "+49XXXXXXXXX" \
  --heiko "+49..." --noah "+49..." --flora "+49..." \
  --familie "zV7XHDr+JUOEc2xGISGMm+XJH0iuuD/ldzYXtTBNUMQ="

# Gateway neu starten
systemctl --user restart clawdbot-gateway-personal.service
```

**Hinweis:** Kein `+` am Anfang → wird als Gruppe interpretiert. Gruppe muss dem Bot hinzugefügt sein (Bot-Nummer in der Gruppe).

**Gruppen-Verhalten:** Das Skript setzt automatisch `groupAllowFrom` (Heiko, Noah, Flora) und `requireMention: false` – der Bot reagiert auf **jede** Nachricht in der Familie-Gruppe.

---

## Workspaces anpassen (AGENTS.md, SOUL.md, USER.md)

**Pro Agent:** Fokus, Persona, Nutzerprofil in den Workspace-Dateien anpassen.

**Automatisch (Templates vorhanden):**

```bash
# Skript von VM105 auf VM102 kopieren
scp infrastructure/docker/apply_agent_templates.py infrastructure/docker/agent_templates.yaml user@docker-apps:/tmp/

# Auf VM102
python3 /tmp/apply_agent_templates.py
```

**Manuell:** `~/clawd/workspace-{heiko,noah,flora,familie}/AGENTS.md` bearbeiten.

### Voice (STT + TTS)

Sprachnachrichten verstehen + Sprachantwort bei Voice-Inbound:

```bash
# 1. ffmpeg (STT) + Node.js (TTS) – auf VM102 (einmalig, sudo nötig):
sudo apt install ffmpeg
# Node 22+ für Edge TTS:
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs

# 2. Voice-Config deployen
scp infrastructure/docker/update_clawdbot_voice_config.py user@docker-apps:/tmp/
# Auf VM102:
python3 /tmp/update_clawdbot_voice_config.py
systemctl --user restart clawdbot-gateway-personal.service
```

**STT:** Whisper-CLI (lokal, kein API-Key). `pip install openai-whisper` auf VM102. Alternative: faster-whisper (4× schneller, weniger RAM) – erfordert Anpassung der Config.
**TTS:** Edge TTS (kein Key), weibliche Stimme (Katja). Braucht Node.js 22+ (node-edge-tts). `auto: "always"` – jede Antwort als Sprachnachricht.
**ffmpeg:** Pflicht für Signal-Voice – Opus→WAV. Ohne ffmpeg: „ffmpeg-Decoder nicht installiert“.

**Wichtig bei TTS:**
- **Emojis** im Reply-Text brechen den Signal-Versand (Bug: Media-Pfad enthält Emoji). In **allen** Agent-Workspaces in AGENTS.md: *„Keine Emojis – technische Einschränkung bei Sprachnachrichten.“*
- **Kein TTS-Tool:** Agent darf kein `<tool_call>` mit name "tts" verwenden – Plattform übernimmt TTS automatisch. Nur normalen Text schreiben. Falls Agent „Ich habe keine Sprachausgabe“ sagt oder `[[tts:...]]` / `tool_call tts` ausgibt: In AGENTS.md ergänzen. **Familie:** `scp infrastructure/docker/patch_familie_agents_tts.py user@docker-apps:/tmp/` → `python3 /tmp/patch_familie_agents_tts.py`: *„Sprachausgabe wird von der Plattform automatisch übernommen. Einfach normalen Text schreiben – kein tool_call tts, kein [[tts]]-Tag.“*

### Flora (Sage) – vollständiges Custom-Setup

Flora hat ein eigenes, umfangreiches Setup (Sage-Persona, WELCOME_MESSAGE, etc.):

```bash
# Von VM105: Templates + Skript auf VM102 kopieren
scp -r infrastructure/docker/workspace-flora infrastructure/docker/apply_flora_workspace.py user@docker-apps:/tmp/

# Auf VM102: deployen
python3 /tmp/apply_flora_workspace.py

# Gateway neu starten
systemctl --user restart clawdbot-gateway-personal.service
```

Dateien: `AGENTS.md`, `SOUL.md`, `USER.md`, `WELCOME_MESSAGE.md`, `HEARTBEAT.md`, `CRON.md` – siehe `infrastructure/docker/workspace-flora/`.

### Flora Heartbeat + Cron

**Heartbeat (4h, 09:00–20:00):**
```bash
scp infrastructure/docker/update_clawdbot_flora_config.py user@docker-apps:/tmp/
# Auf VM102:
python3 /tmp/update_clawdbot_flora_config.py
systemctl --user restart clawdbot-gateway-personal.service
```

**Flora: Claude Sonnet 4.6 (Anthropic API) statt lokalem Spark-Default:**

- Voraussetzung: Anthropic API-Key (z. B. `openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"` auf VM102, oder Key in der systemd-Umgebung des Gateways). Pro-Agent-Auth beachten — bei Fehlern `openclaw models status`.
- Skript setzt nur für Agent `flora` in `agents.list` das Modell `anthropic/claude-sonnet-4-5` (Clawdbot ≤2026.1.x kennt `…-4-6` oft noch nicht → „unknown model“); andere Agents bleiben bei `agents.defaults.model` (typisch Spark). Nach Gateway-Update ggf. auf `…-4-6` wechselbar.

```bash
scp infrastructure/docker/update_clawdbot_flora_sonnet.py user@docker-apps:/tmp/
python3 /tmp/update_clawdbot_flora_sonnet.py
systemctl --user restart clawdbot-gateway-personal.service
```

Zurück auf den gemeinsamen Default (ohne flora-spezifisches Modell): `python3 /tmp/update_clawdbot_flora_sonnet.py --clear`

**Cron-Jobs (Pflanze der Woche, Jahreszeitenimpuls):**
```bash
scp infrastructure/docker/setup_flora_cron.py user@docker-apps:/tmp/
# Auf VM102 (beliebiges Verzeichnis):
python3 /tmp/setup_flora_cron.py
```
*Python-Version vermeidet CRLF-Probleme bei SCP von Windows (setup_flora_cron.sh hatte Zeilenenden-Fehler).*

---

## Externes Wissen (PDFs, Word, Text)

| Methode | Wie | Einschränkung |
|---------|-----|---------------|
| **Backend** | Dateien per SCP in Workspace legen | Empfohlen. `.md`/`.txt` kann der Agent lesen. |
| **PDF → Text** | `pdftotext skript.pdf ~/clawd/workspace-noah/lernthema.md` | PDF muss vorher konvertiert werden. |
| **Per Chat (Signal)** | Anhang schicken | Bilder funktionieren. Audio/Video werden transkribiert. **PDFs** landen als Datei, werden nicht automatisch verarbeitet. |

**Workflow für Lernmaterial:** PDF/Word lokal mit `pdftotext` oder `pandoc` in Text wandeln → per SCP in Workspace legen → Agent kann den Inhalt lesen und nutzen.

### Lose Texte per Signal als Wissen speichern

Clawdbot nutzt `memory_save` – der Agent kann Inhalte in `MEMORY.md` oder `memory/*.md` schreiben. **Nutzer können per Signal-Nachricht explizit Wissen hinterlegen:**

- Beispiel: *"Speichere als Wissen: Urlaub Malle 15.–22. Juli"*
- Beispiel: *"Merke dir: Omas Geburtstag ist am 3. März"*

Der Agent schreibt dann ins Workspace-Memory. Für eigene Notizen: Text an den eigenen Agent (z.B. Heiko) schicken mit klarer Anweisung „Speichere das“ / „Merke dir“. In AGENTS.md kann man das Verhalten verstärken: *„Wenn der User dich bittet, etwas zu speichern oder zu merken, nutze memory_save.“*

---

## Nach dem Setup: Bot nutzen

| Person | Aktion | Ergebnis |
|--------|--------|----------|
| Heiko | Nachricht an Bot-Nummer schicken | Routet an heiko-Agent (Projekte, Reminder) |
| Noah | Nachricht an Bot-Nummer schicken | Routet an noah-Agent (Lernagent) |
| Flora | Nachricht an Bot-Nummer schicken | Routet an flora-Agent (Physiotherapie) |
| Familie | Nachricht in Gruppen-Chat | Routet an familie-Agent |

**Neue Person hinzufügen:** Nachricht schicken → Pairing-Code erhalten → Admin approves → kann chatten.

**Wartung:** signal-cli-Daemon und Gateway müssen laufen. Nach Reboot: Daemon + `systemctl --user start clawdbot-gateway-personal.service`.

---

## Schritt 9: LLM-Backend (Spark Qwen 32B auf Port 30001) konfigurieren

Ohne LLM antwortet der Bot nicht – Fehler: `no api key found for provider anthropic`.

**Automatisch (empfohlen):**

```bash
# Skript von VM105 auf VM102 kopieren
scp infrastructure/docker/update_clawdbot_spark_config.py user@docker-apps:/tmp/

# Auf VM102: Spark erreichbar? (spark-56d0 = Tailscale MagicDNS)
curl -sf http://spark-56d0:30001/v1/models

# Config anwenden
python3 /tmp/update_clawdbot_spark_config.py

# Gateway neu starten
systemctl --user restart clawdbot-gateway-personal.service
```

**Falls spark-56d0 nicht auflöst:** `--host 100.x.x.x` (Tailscale-IP von `tailscale status`).

**Manuell:** In `~/.clawdbot-personal/clawdbot.json` ergänzen:

```json
"models": {
  "providers": {
    "spark": {
      "baseUrl": "http://spark-56d0:30001/v1",
      "apiKey": "dummy",
      "api": "openai-completions",
      "models": [{ "id": "qwen3-32b-nvfp4", "name": "Qwen 32B", "contextWindow": 32000 }]
    }
  }
},
"agents": {
  "defaults": {
    "model": { "primary": "spark/qwen3-32b-nvfp4" }
  }
}
```

**Option B – Anthropic:** `clawdbot --profile personal doctor` führt durch OAuth/API-Key-Setup.

Details: `infrastructure/docker/clawdbot_vm102.md`, `infrastructure/spark/inference_endpoints.md`.

---

## Kurzreferenz

| Befehl | Zweck |
|--------|--------|
| `ssh user@docker-apps` | SSH zu VM102 |
| `signal-cli -a +49... daemon --http 127.0.0.1:8081` | signal-cli-Daemon starten (läuft in screen) |
| `screen -r signal` | signal-Session wieder anzeigen |
| `clawdbot --profile personal pairing list signal` | Pending Pairings |
| `clawdbot --profile personal pairing approve signal <CODE>` | Pairing bestätigen |
| `systemctl --user restart clawdbot-gateway-personal.service` | Gateway neu starten |

---

## Troubleshooting

- **signal-cli nicht gefunden:** Prüfe `which signal-cli`, ggf. `PATH` erweitern oder absoluten Pfad in Config `cliPath`.
- **Daemon startet nicht:** `channels.signal.httpUrl` + externen Daemon nutzen (siehe docs.clawd.bot/channels/signal).
- **Bindings greifen nicht:** Peer-IDs müssen exakt E.164 sein (`+49...`), keine Leerzeichen.
- **`bindings.X.match.peer.kind: Invalid input`:** Das Schema erwartet `"dm"` statt `"direct"`. Im Skript `update_clawdbot_signal_config.py` Zeile `dm_kind = "dm"` ggf. auf `dm_kind = "direct"` ändern (je nach Clawdbot-Version). Oder `clawdbot --profile personal doctor --fix` ausführen.
- **Signal: "Failed to initialize HTTP Server" / "daemon not ready (HTTP 404)":** Der signal-cli-Daemon startet nicht. Lösung:
  1. Port prüfen: `ss -tlnp | grep 8080` – falls belegt, Prozess beenden oder anderen Port nutzen.
  2. **Java-Build testen:** Das native Build kann den HTTP-Server blockieren. Java 17 + Standard-Build installieren (siehe Schritt 2, Option B), dann `signal-cli` neu verlinken.
  3. **Externer Daemon (z.B. wenn 8080 belegt):** Port 8081 nutzen, Daemon dauerhaft laufen lassen (siehe Schritt 8):
     ```bash
     signal-cli -a +49XXXXXXXXX daemon --http 127.0.0.1:8081
     ```
     In `clawdbot.json` unter `channels.signal`: `"httpUrl": "http://127.0.0.1:8081"`, `"autoStart": false` setzen.
- **Agent verwechselt Identität (Heiko antwortet wie Familien-Bot):**
  1. **Service-Profil prüfen:** `systemctl --user cat clawdbot-gateway-personal.service` – muss `--profile personal` enthalten.
  2. **State-Dir erzwingen** (falls ~/.clawdbot und ~/.clawdbot-personal beide existieren): In der Service-Datei `Environment="OPENCLAW_STATE_DIR=/home/user/.clawdbot-personal"` setzen.
  3. **~/.clawdbot deaktivieren:** Falls der Doctor in ~/.clawdbot geschrieben hat, Config dort prüfen/bereinigen – nur ~/.clawdbot-personal soll aktiv sein.
  4. **Session löschen:** `rm -rf ~/.clawdbot-personal/agents/heiko/sessions/*` und Gateway neu starten.
  5. **Routing prüfen:** Beim Senden Logs beobachten: `journalctl --user -u clawdbot-gateway-personal.service -f` – nach „agent:heiko“ oder „agent:familie“ suchen.

- **Voice: „ffmpeg-Decoder nicht installiert“:** Signal sendet Sprachnachrichten als Opus. Clawdbot/Whisper brauchen ffmpeg zum Decodieren. Lösung: `sudo apt install ffmpeg` auf VM102, dann Gateway neu starten.
- **TTS liefert keine Sprachnachricht:** Edge TTS braucht Node.js 22+. Prüfen: `node -v`. Wenn fehlt: `curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -` und `sudo apt-get install -y nodejs`, dann Gateway neu starten.
- **TTS mit Signal:** Log-Fehler: `signal block reply failed: ENOENT ... open '.../media/inbound/UUID 🌿'` – der Media-Pfad enthält ein Emoji (aus Reply-Text) und ist ungültig. Signal kann Audio senden (`message send --media` funktioniert). Bug in Clawdbot: Reply-Text wird fälschlich in Media-Pfad eingebaut. Issue bei openclaw/openclaw öffnen mit diesem Log-Eintrag.
- **Gateway stürzt ab (exit-code 1, auto-restart):** Logs prüfen:
  ```bash
  journalctl --user -u clawdbot-gateway-personal.service -n 80 --no-pager
  ```
  **Häufigster Fix:** `gateway.mode` fehlt → Gateway start blocked. Lösung:
  ```bash
  clawdbot --profile personal config set gateway.mode local
  clawdbot --profile personal doctor --fix
  systemctl --user restart clawdbot-gateway-personal.service
  ```
  Weitere Ursachen: ungültige Config (JSON), Signal-Account nicht in signal-cli, fehlender Spark-Zugang.
- **Config invalid / Unrecognized key audioAsVoice:** Gateway crasht in Restart-Loop. Sofort: `~/.clawdbot/bin/clawdbot --profile personal doctor --fix` oder `python3 remove_audio_as_voice_config.py`, dann Gateway neu starten.
- **Voice: Bot schickt Sprachnachricht zurück (Echo-Bug):** User sendet Voice → Bot antwortet mit demselben Audio + Text. Vermutung: STT-Flow oder Media-Anhang bei Reply fehlerhaft. Workaround: Telegram als zusätzlichen Kanal testen (siehe unten).
- **Telegram: TTS kommt als Musik-Datei statt Sprachmemo:** Agent fügt `[[audio_as_voice]]` in Antwort ein (AGENTS.md). Nicht: `audioAsVoice` in Config – ungültiger Key!
- **TTS liefert nur Text, keine Sprachnachricht:** (1) **messages.tts.edge.enabled = false** – häufigste Ursache! tts.js überspringt mit "edge: disabled". Fix: `messages.tts.edge.enabled: true` in ~/.clawdbot-personal/clawdbot.json setzen. (2) node-edge-tts fehlt: `cd ~/.clawdbot/lib/node_modules/clawdbot && npm install node-edge-tts`. (3) tools.deny, Antwort < 10 Zeichen. (4) Laut Clawdbot-Docs: *"If reply exceeds maxLength and summary is off, audio is skipped."* Flora neigt zu langen Antworten → oft > 8000 Zeichen → kein TTS. **Fix:** (1) `tts.json` prüfen – `auto` darf nicht `"off"` sein (überschreibt clawdbot.json!). (2) Kurztest: `/tts always` + „Sag nur: Hallo Welt“. (3) Wenn kurz funktioniert: `maxLength` auf 15000 erhöhen ODER Flora-Prompt kürzen. (4) OpenClaw nutzt `node-edge-tts` (Node.js), nicht Python edge-tts.

---

## Optional: Telegram zusätzlich einrichten

**Zweck:** Telegram als zweiten Kanal nutzen – evtl. besseres Voice-Handling als bei Signal (Echo-Bug).

**Quelle:** https://docs.clawd.bot/channels/telegram

### 1. Bot anlegen

1. In Telegram: @BotFather öffnen
2. `/newbot` → Name + Username wählen
3. Token kopieren (z.B. `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 2. Skript ausführen (Config + Bindings)

```bash
scp infrastructure/docker/update_clawdbot_telegram_config.py user@docker-apps:/tmp/
ssh user@docker-apps
python3 /tmp/update_clawdbot_telegram_config.py --bot-token "DEIN_TOKEN"
```

Optional – Agent-spezifische Zuordnung (Telegram-User-IDs nach Pairing):

```bash
python3 /tmp/update_clawdbot_telegram_config.py --bot-token "..." \
  --heiko "123456789" --noah "987654321" --flora "111222333" --familie "444555666"
```

Telegram-User-ID ermitteln: `~/.clawdbot/bin/clawdbot pairing list telegram`, Logs oder `curl "https://api.telegram.org/bot<TOKEN>/getUpdates"`.

### 3. Gateway neu starten

```bash
systemctl --user restart clawdbot-gateway-personal.service
```

### 4. Pairing

```bash
~/.clawdbot/bin/clawdbot --profile personal pairing list telegram
# Code anzeigen lassen, dann in Telegram an den Bot senden
~/.clawdbot/bin/clawdbot --profile personal pairing approve telegram <CODE>
```

**Hinweis:** Voice-Config (STT/TTS) gilt kanalübergreifend – wenn sie für Signal gesetzt ist, gilt sie auch für Telegram. Bestehende Signal-Bindings bleiben erhalten.

**Telegram Voice Note:** Standardmäßig sendet OpenClaw TTS als Audio-Datei (Musik-Player). Für Sprachmemo-Bubble: `messages.tts.audioAsVoice: true` in Config (update_clawdbot_voice_config.py setzt das automatisch). Alternativ: Agent fügt `[[audio_as_voice]]` in Antwort ein.

**Routing:** Ohne Agent-Bindings (`--flora` etc.) gehen alle Telegram-DMs an den **main**-Agent (oft = Lumi/Familie). Für Flora (Sage): `--flora <DEINE_TELEGRAM_USER_ID>` setzen. User-ID z.B. aus `getUpdates` oder Logs.

**TTS-Bug (message asVoice):** Falls du Rohtext wie `<tool_call>{"name":"message","asVoice":true}</tool_call>` erhältst: Agent nutzt fälschlich das message-Tool. Fix:
```bash
scp infrastructure/docker/patch_agents_message_asvoice.py infrastructure/docker/workspace-flora user@docker-apps:/tmp/
# Flora: apply_flora_workspace.py (AGENTS.md enthält bereits den Fix)
# Alle Agents: python3 /tmp/patch_agents_message_asvoice.py
rm -rf ~/.clawdbot-personal/agents/*/sessions/*
systemctl --user restart clawdbot-gateway-personal.service
```
