# Clawdbot Voice/TTS – Analyse-Dokument für externe KI

**Zweck:** Vollständige Dokumentation aller durchgeführten Schritte und aufgetretenen Probleme, damit eine andere KI das Setup analysieren kann.

---

## 1. Umgebung

| Komponente | Details |
|------------|---------|
| **Plattform** | OpenClaw/Clawdbot (2026.1.24-3) |
| **Host** | VM102 (docker-apps), Debian, per Tailscale erreichbar |
| **Channel** | Signal (signal-cli, Daemon auf Port 8081) |
| **LLM** | Spark (SGLang, Qwen 32B) auf Port 30001 |
| **Agents** | heiko, noah, flora, familie (Multi-Agent-Setup) |

---

## 2. Ziel

- **STT:** Sprachnachrichten des Users verstehen (Whisper)
- **TTS:** Antworten als Sprachnachricht senden (Edge TTS)
- **Channel:** Signal (kein Telegram im Einsatz)

---

## 3. Durchgeführte Konfiguration

### 3.1 Voice-Config (`update_clawdbot_voice_config.py`)

- **STT:** `tools.media.audio` mit Whisper-CLI (`--model base`)
- **TTS:** `messages.tts` mit Edge TTS, `auto: "always"`, `edge.enabled: true`, Stimme `de-DE-KatjaNeural` (audioAsVoice ist ungültiger Key)
- **tools.deny:** `["tts"]` – TTS-Tool für Agent deaktiviert
- **modelOverrides.enabled:** `false` – keine [[tts:...]]-Direktiven im Prompt
- **prefsPath:** `~/.clawdbot-personal/settings/tts.json` mit `summarize: false`, `maxLength: 8000`

### 3.2 System-Abhängigkeiten (laut Checkliste)

- **ffmpeg:** `sudo apt install ffmpeg` (für Opus→WAV bei Signal)
- **Node.js 22+:** für `node-edge-tts`
- **Whisper:** `pip install openai-whisper` (lokal, kein API-Key)

### 3.3 Agent-Workspaces

- **Flora:** Eigenes Setup (Sage), AGENTS.md mit CRITICAL-Block: kein [[tts]], kein tool_call tts, keine Emojis
- **Heiko, Noah, Familie:** Patch-Skripte fügen TTS-Regeln hinzu (patch_all_agents_tts.py, patch_all_agents_tts_v2.py)

---

## 4. Aufgetretene Probleme

### 4.1 Emoji-Bug (behoben durch Workaround)

**Symptom:** `signal block reply failed: ENOENT ... open '.../media/inbound/UUID 🌿'`

**Ursache:** Reply-Text (inkl. Emoji) wurde in den Media-Pfad eingebaut → ungültiger Dateiname.

**Workaround:** Emojis aus allen Agent-Prompts entfernt, Regel „Keine Emojis“ in AGENTS.md.

### 4.2 Agent gibt [[tts:...]] oder [[tts:text]] aus

**Symptom:** User erhält Rohtext wie `[[tts:Ich antworte gerne per Sprache!]]` statt Audio.

**Ursache:** Modell hat gelernt, TTS-Markup zu erzeugen; Plattform wandelt es nicht in Audio um.

**Versuche:**
- `modelOverrides.enabled: false` in Config
- `tools.deny: ["tts"]` – TTS-Tool deaktiviert
- CRITICAL-Block in AGENTS.md: „NIEMALS [[tts:...]] ausgeben“
- Sessions zurückgesetzt

**Ergebnis:** Agent ignoriert Anweisungen weiterhin, gibt [[tts:...]] oder [[tts:text]] aus.

### 4.3 Agent nutzt message-Tool mit asVoice

**Symptom:** `tool_call` mit `"name": "message"`, `"asVoice": true` – Agent versucht, über message-Tool Audio zu senden.

**Hinweis:** `tools.deny: ["tts"]` blockiert nur das tts-Tool, nicht das message-Tool mit asVoice.

### 4.4 TTS-Audio kommt nicht an

**Symptom:** Bei `auto: "always"` sollte die Plattform jede Antwort automatisch in Audio umwandeln. Stattdessen:
- Entweder Rohtext ([[tts:...]]) oder
- Text ohne Audio

**Unklar:** Ob TTS überhaupt ausgeführt wird und nur der Versand scheitert, oder ob TTS gar nicht gestartet wird.

### 4.5 Echo-Bug: Sprachnachricht wird zurückgeschickt (2026-02)

**Symptom:** User schickt Sprachnachricht → Bot schickt dieselbe Sprachnachricht (octet-stream, ~28 kB) als Media zurück und antwortet zusätzlich per Text.

**Vermutung:** 
- STT (Whisper) transkribiert evtl. nicht korrekt, oder
- Die Plattform hängt das eingehende Audio fälschlich an die Reply an statt es nur für Transkription zu nutzen,
- oder der Reply-Flow bei Voice-Inbound ist fehlerhaft.

**Workaround-Vorschlag:** Telegram als zusätzlichen Kanal testen – evtl. besseres Voice-Handling.

---

## 5. Erwartetes Verhalten (laut OpenClaw-Docs)

- Bei `messages.tts.auto: "always"`: Plattform wandelt jede Reply in Audio um und hängt es an.
- Kein Agent-Markup nötig – Agent schreibt nur normalen Text.
- Edge TTS nutzt `node-edge-tts`, keine API-Keys nötig.

---

## 5b. Ursache für [[tts:...]]-Output gefunden (2026-02)

**Quelle:** `clawdbot/dist/tts/tts.js` injiziert in den System-Prompt:
- "Only use TTS when you include [[tts]] or [[tts:text]] tags."
- "Use [[tts:...]] and optional [[tts:text]]...[[/tts:text]] to control voice/expressiveness."

Dadurch lernt das Modell, dieses Markup zu verwenden – obwohl bei `auto: "always"` die Plattform TTS automatisch übernimmt.

**Fix:** `patch_clawdbot_tts_prompt.py` ersetzt diese Strings durch "write plain text only". Nach Clawdbot-Updates erneut ausführen.

---

## 6. Offene Fragen

1. **Warum wird TTS nicht automatisch ausgeführt?** Liegt es an der Config, an Signal, oder an der Reihenfolge der Verarbeitung?
2. **Wird [[tts:...]] vom Modell erzeugt, weil es irgendwo im System-Prompt/Skill steht?** Trotz `modelOverrides.enabled: false`.
3. **Sollte `message`-Tool mit `asVoice` ebenfalls eingeschränkt werden?**
4. **Telegram:** Würde Telegram als Channel dieselben Probleme zeigen, oder ist es Signal-spezifisch?
5. **Echo-Bug:** Warum hängt die Plattform das eingehende Audio an die Reply an? Ist das ein Signal-Channel-Bug oder generelles Media-Handling?

---

## 8. Telegram Voice Note vs. Audio File (2026-02)

**Problem:** Telegram unterscheidet Voice Note (Sprachmemo-Bubble) von Audio File (Musik-Player). OpenClaw sendet standardmäßig als Audio File.

**Lösung:**
- **Nicht:** `messages.tts.audioAsVoice` – ungültiger Key, führt zu Config-Invalidität und Crash-Loop!
- **Agent-Fallback:** `[[audio_as_voice]]` am Anfang der Antwort – Plattform sendet dann sendVoice statt sendAudio

**Skill (optional):** `telegram-offline-voice` – Edge-TTS, Markdown-Cleanup, Segmentierung. Install z.B. via `clawhub install telegram-offline-voice` (Pfad ggf. abweichend).

---

## 8a. Troubleshooting: TTS liefert nur Text, keine Sprachnachricht

**Symptom:** STT funktioniert (Sprachnachricht wird verstanden), Antwort kommt aber immer als Text, nie als Audio.

**Root Cause (tts.js Zeile 828–829):** `if (!config.edge.enabled) { lastError = "edge: disabled"; continue; }` – der Edge-Provider wird übersprungen. Config: `~/.clawdbot-personal/clawdbot.json` (nicht ~/.clawdbot/). Fix: `messages.tts.edge.enabled: true` setzen.

### Wahrscheinlichste Ursache (Clawdbot-Docs)

> *"If the reply exceeds maxLength and summary is off (or no API key for the summary model), audio is skipped and the normal text reply is sent."*

**Flora neigt zu langen Antworten** → Antwort > 8000 Zeichen + `summary.enabled: false` → **Audio wird komplett übersprungen**.

### Fix-Optionen

| Möglichkeit | Fix |
|-------------|-----|
| Antworten zu lang + Summary aus | Flora-Prompt kürzen **ODER** `maxLength` auf 15000 setzen **ODER** Summary aktivieren (mit API-Key) |
| tts.json überschreibt `auto` mit `"off"` | `cat ~/.clawdbot-personal/settings/tts.json` prüfen – `auto` darf nicht `"off"` sein |
| node-edge-tts fehlt (nur Python edge-tts) | `npm install -g node-edge-tts` – OpenClaw nutzt Node.js-Variante |
| **Antwort < 10 Zeichen** | OpenClaw überspringt TTS bei sehr kurzen Replies – z.B. „Hallo!“ |
| `auto: "inbound"` + Text gesendet | TTS nur bei Sprachnachricht – Text-Inbound → keine TTS-Antwort |

### Diagnose auf VM102 (der Reihe nach)

**Schritt 1:** node-edge-tts prüfen (nicht Python edge-tts!)

```bash
which node-edge-tts 2>/dev/null || npm list -g node-edge-tts 2>/dev/null
# Alternativ:
ls ~/.clawdbot/node_modules/ 2>/dev/null | grep edge
```

**Schritt 2:** tts.json prüfen – **entscheidend!** Prefs überschreiben clawdbot.json.

```bash
cat ~/.clawdbot-personal/settings/tts.json
```

Wenn `"auto": "off"` oder `"auto": "inbound"` → bei Text-Nachrichten kein Audio. Fix: `"auto": "always"` setzen oder `auto`-Key entfernen.

**Schritt 3:** Live-Test mit kurzer Nachricht (damit maxLength nicht greift)

In Telegram/Signal an Flora:
```
/tts always
```
Dann eine Nachricht, die eine **mind. 10 Zeichen lange** Antwort auslöst (OpenClaw überspringt TTS bei < 10 Zeichen!):
```
Erzähl mir in einem Satz, wer du bist
```
Nicht „Hallo Welt“ – Flora antwortet oft mit „Hallo!“ (< 10 Zeichen) → TTS wird übersprungen.

**Schritt 4:** Sprachnachricht testen (nicht Text!)

Schick Flora eine **Sprachnachricht**. Wenn dann Audio zurückkommt → `auto: "inbound"` (TTS nur bei Voice-Input, nicht bei Text).

**Schritt 5:** Live-Logs während Textnachricht senden

```bash
# Terminal 1:
journalctl --user -u clawdbot-gateway-personal.service -f

# Terminal 2 / Handy: Textnachricht an Flora, z.B. "Erzähl mir in einem Satz wer du bist"
```

Suche nach: `tts` / `edge` / `audio` / `auto` / `mode` (TTS getriggert) oder `skipping audio` / `text too long` (Antwort zu lang) oder gar nichts zu TTS (TTS wird nie aufgerufen).

**Schritt 6:** Falls TTS nie getriggert wird

```bash
~/.clawdbot/bin/clawdbot --profile personal doctor
```

### Sonderfall: /tts always → MP3, aber folgende Nachricht → nur Text

**Beobachtung:** `/tts always` liefert MP3, die nächste Nachricht (z.B. „Hallo Welt“ oder „Erzähl mir in einem Satz, wer du bist“) liefert nur Text.

**Wahrscheinlichste Erklärung:** `/tts always` hat nur seine eigene Bestätigung als Audio gesendet – die Session-Einstellung greift nicht dauerhaft. **tts.json** (Prefs) überschreibt den Wert wieder.

**Diagnose (der Reihe nach):**

| Test | Was es zeigt |
|------|--------------|
| `cat ~/.clawdbot-personal/settings/tts.json` | Ob Prefs `auto` überschreiben (`"off"` oder `"inbound"` → kein TTS bei Text) |
| Sprachnachricht an Flora schicken | Wenn Audio zurückkommt → `auto: "inbound"` (TTS nur bei Voice-Input) |
| Logs bei Textnachricht: `journalctl --user -u clawdbot-gateway-personal.service -f` | Ob TTS überhaupt getriggert wird (`tts` / `auto` / `mode` in Logs) |

**Fix:** `update_clawdbot_voice_config.py` erneut ausführen – setzt tts.json mit clawdbot.json synchron. Oder manuell: `echo '{"summarize":false,"maxLength":8000,"auto":"always"}' | jq . > ~/.clawdbot-personal/settings/tts.json`

### Hypothese: tools.deny: ["tts"] blockiert auch Auto-TTS

**Situation:** auto: "always" ✓, tts.json überschreibt nichts ✓, edge-tts funktioniert ✓, STT funktioniert ✓ – trotzdem nie Audio-Antwort.

**Hypothese:** `tools.deny: ["tts"]` blockiert nicht nur Agent-Tool-Calls, sondern die gesamte Auto-TTS-Pipeline. `/tts always` funktioniert, weil es ein System-Befehl ist (kein Tool-Call).

**Test auf VM102:**

```bash
# Schritt 1: tts aus tools.deny entfernen
# Option A – Skript (scp infrastructure/docker/remove_tts_from_deny.py user@docker-apps:/tmp/):
python3 /tmp/remove_tts_from_deny.py

# Option B – Inline:
python3 -c "
import json
path = '/home/user/.clawdbot-personal/clawdbot.json'
with open(path) as f: cfg = json.load(f)
deny = cfg.get('tools', {}).get('deny', [])
print('Vorher:', deny)
if 'tts' in deny:
    deny.remove('tts')
    with open(path, 'w') as f: json.dump(cfg, f, indent=2)
    print('tts ENTFERNT')
else:
    print('tts war nicht in deny')
"

# Schritt 2: Gateway neu starten
systemctl --user restart clawdbot-gateway-personal.service
sleep 5
systemctl --user status clawdbot-gateway-personal.service

# Schritt 3: Flora testen – z.B. "Erzähl mir in zwei Sätzen, wer du bist"

# Schritt 4: Logs beobachten
journalctl --user -u clawdbot-gateway-personal.service -f | grep -i -E "tts|edge|audio|voice|deny|skip"
```

**Wenn danach Audio kommt:** tools.deny war die Ursache. CRITICAL-Block in AGENTS.md beibehalten (verhindert [[tts:...]]-Output).

### Nächste Hypothesen (wenn tools.deny-Entfernung nichts brachte)

Config-Ursachen ausgeschlossen. Verbleibende Möglichkeiten:

**Hypothese A: patch_clawdbot_tts_prompt.py hat tts.js beschädigt**

patch_clawdbot_tts_prompt.py patcht `dist/tts/tts.js` – der Gateway lädt aber `gateway/server-methods/tts.js`! Beide Dateien existieren.

```bash
# Gateway lädt diese Datei:
TTS_JS=~/.clawdbot/lib/node_modules/clawdbot/dist/gateway/server-methods/tts.js
# dist/tts/tts.js wird vom Gateway NICHT verwendet

# Wurde tts.js gepatcht?
grep -c "write plain text" "$TTS_JS"
# Wenn > 0 → gepatcht. Backup wiederherstellen:
ls -la "$TTS_JS"*
cp "${TTS_JS}.bak" "$TTS_JS"   # falls .bak existiert
systemctl --user restart clawdbot-gateway-personal.service
```

**Hypothese B: node-edge-tts fehlt in Clawdbot's node_modules**

node-edge-tts steht in package.json, ist aber **nicht** in Clawdbot's node_modules installiert. npx lädt es on-the-fly in ~/.npm/_npx/ – dort sucht Clawdbot aber nicht. → TTS schlägt still fehl.

```bash
cd ~/.clawdbot/lib/node_modules/clawdbot && npm install node-edge-tts
systemctl --user restart clawdbot-gateway-personal.service
```

**Hypothese D: messages.tts.edge.enabled = false** ✅ ECHTE ROOT CAUSE

tts.js prüft `if (!config.edge.enabled) { lastError = "edge: disabled"; continue; }` – der Edge-Provider wird übersprungen. Config-Pfad: `~/.clawdbot-personal/clawdbot.json` (nicht ~/.clawdbot/).

```bash
# Prüfen:
python3 -c "import json; d=json.load(open('/home/user/.clawdbot-personal/clawdbot.json')); print(json.dumps(d.get('messages',{}).get('tts',{}), indent=2))"

# FIX – edge.enabled auf True setzen:
python3 -c "
import json
p = '/home/user/.clawdbot-personal/clawdbot.json'
d = json.load(open(p))
tts = d.setdefault('messages', {}).setdefault('tts', {})
edge = tts.setdefault('edge', {})
edge['enabled'] = True
json.dump(d, open(p, 'w'), indent=2)
print('Fixed: messages.tts.edge.enabled = True')
"

~/.clawdbot/bin/clawdbot --profile personal gateway restart
```

**Hypothese C: Logs zeigen die Ursache**

Alle Logs ungefiltert bei einer Nachricht beobachten:

```bash
# Terminal 1 – ALLE Logs live (ungefiltert):
journalctl --user -u clawdbot-gateway-personal.service -f

# Terminal 2 / Handy: "Erzähl mir in zwei Sätzen wer du bist" an Flora

# Letzte 100 Zeilen komplett sichern/teilen
```

| Schritt | Befehl | Warum |
|---------|--------|-------|
| 1 | `grep -c "write plain text" ~/.clawdbot/.../tts.js` | Wenn > 0 → tts.js gepatcht, evtl. kaputt |
| 2 | `ls ~/.clawdbot/lib/node_modules/clawdbot/node_modules/ \| grep edge` | node-edge-tts muss hier sein, nicht nur im npx-Cache |
| 3 | Ungefilterte Logs bei Nachricht | Zeigt echte Fehlermeldung |

**Log-Mitschnitt für Diagnose:**
```bash
journalctl --user -u clawdbot-gateway-personal.service -f > /tmp/tts_debug.log 2>&1 &
# Nachricht schicken, warten, dann:
kill %1 2>/dev/null
tail -150 /tmp/tts_debug.log
```

**Detail-Log (Clawdbot):**
```bash
tail -200 /tmp/clawdbot/clawdbot-*.log | grep -i -E "tts|edge|audio|error"
```

**TTS-Debug-Logging einfügen** (wenn textToSpeech nie aufgerufen wird):

**WICHTIG:** Es gibt **zwei** tts.js-Dateien – der Gateway lädt `gateway/server-methods/tts.js`, nicht `dist/tts/tts.js`!

```bash
# Prüfen welche Datei verwendet wird:
grep -n "PAST ALL CHECKS\|textToSpeech\|FINAL FALLBACK" \
  ~/.clawdbot/lib/node_modules/clawdbot/dist/gateway/server-methods/tts.js

# Patch-Skript patcht die RICHTIGE Datei (gateway/server-methods/tts.js):
scp infrastructure/docker/patch_tts_debug_logging.py user@docker-apps:/tmp/
python3 /tmp/patch_tts_debug_logging.py
systemctl --user restart clawdbot-gateway-personal.service
journalctl --user -u clawdbot-gateway-personal.service -f | grep TTS-DEBUG
```

Zeigt: `[TTS-DEBUG] calling textToSpeech...` und Rückgabewert bzw. Fehler. Nach Debug: `cp tts.js.bak tts.js` um Patch rückgängig zu machen.

---

## 9. Bekannte Bugs (Voice Messages)

- **Eingehende Sprachnachrichten:** Funktionieren nur ~20 % der Zeit
- **Audio-only ohne Text:** Triggert den Agent evtl. nicht
- **Rohes Audio-Binary:** Leakt manchmal als Text in den Chat-Kontext

---

## 7. Relevante Dateien im Repo

| Datei | Zweck |
|-------|-------|
| `update_clawdbot_voice_config.py` | Voice-Config (STT, TTS, tools.deny) |
| `apply_flora_workspace.py` | Flora-Workspace deployen |
| `patch_all_agents_tts.py` | TTS-Regeln zu allen Agents |
| `patch_all_agents_tts_v2.py` | CRITICAL-Block ([[tts]]-Verbot) |
| `verify_voice_setup.py` | Installation prüfen (Python, keine CRLF-Probleme) |
| `remove_tts_from_deny.py` | tts aus tools.deny entfernen (Test: blockiert tools.deny Auto-TTS?) |
| `install_node_edge_tts.sh` | node-edge-tts in Clawdbot's node_modules installieren |
| `fix_edge_tts_enabled.py` | messages.tts.edge.enabled auf True setzen (tts.js überspringt sonst mit "edge: disabled") |
| `patch_tts_debug_logging.py` | TTS-Debug in gateway/server-methods/tts.js (nicht dist/tts/!) |
| `clawdbot_voice_fix.py` | Triple-Fix: Prompt-Patch, Config-Verify, Post-Processor (angepasst für VM102) |
| `CLAWDBOT_SIGNAL_SETUP_CHECKLISTE.md` | Gesamte Setup-Doku |

---

## 8. Verifikation auf VM102

```bash
# Prüfskript ausführen (Python empfohlen – keine CRLF-Probleme)
scp infrastructure/docker/verify_voice_setup.py user@docker-apps:/tmp/
ssh user@docker-apps "python3 /tmp/verify_voice_setup.py"

# Oder manuell:
which ffmpeg whisper
node -v
edge-tts --voice de-DE-KatjaNeural --text "Test" --write-media /tmp/test.mp3
cat ~/.clawdbot-personal/clawdbot.json | jq '.messages.tts, .tools.deny'
journalctl --user -u clawdbot-gateway-personal.service -n 50 -f
```

---

## 9. Bekannter funktionierender Test

- `clawdbot message send --channel signal --target +49... --media /tmp/test.mp3` → Audio kam bei Signal an.
- **Fazit:** Signal kann Audio senden; Problem liegt vor dem Versand (TTS-Ausführung oder Reply-Verarbeitung).
