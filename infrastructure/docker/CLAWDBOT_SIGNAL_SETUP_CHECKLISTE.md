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
