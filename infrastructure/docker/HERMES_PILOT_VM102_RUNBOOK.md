<!-- Reality Block
last_update: 2026-04-16
status: active
scope:
  summary: "Hermes-Agent Pilot parallel zu Clawdbot auf VM102 (docker-apps): Installation, Profil pilot, Migration, Telegram-Gateway (eigener Bot), systemd user unit; Phase 2 Signal nur mit getrennter Identität."
  in_scope:
    - Hermes-Installation (manuell via uv, ohne interaktives install.sh)
    - Profil pilot unter ~/.hermes/profiles/pilot
    - Migration aus ~/.clawdbot-personal (ohne ~/.openclaw)
    - Workspace-Dateien (SOUL/USER/AGENTS) aus ~/clawd/workspace-flora
    - systemd user unit hermes-gateway-pilot
    - E2E-Checkliste (CLI + Telegram)
    - Signal-Strategie (Konfliktvermeidung)
  out_of_scope:
    - konkrete Secrets/Tokens (nur Platzhalter und Pfade)
    - Clawdbot-Produktionskonfiguration ändern
notes:
  - "Falls Geheimnisse während der Einrichtung in Logs sichtbar wurden: betroffene Keys rotieren (Anthropic, Hermes-Gateway-Token, Telegram-Bot-Token, …)."
-->

# Hermes Pilot auf VM102 (docker-apps) – Runbook

## Ziel

**Hermes** (Profil `pilot`) läuft **parallel** zu **Clawdbot**: eigener Telegram-Pilot-Bot, eigene Ports/Prozesse, kein Produktions-Cutover bis die Akzeptanztests grün sind.

Verwandte Doku:

- [`clawdbot_vm102.md`](clawdbot_vm102.md) – Clawdbot auf derselben VM
- [`CLAWDBOT_SIGNAL_SETUP_CHECKLISTE.md`](CLAWDBOT_SIGNAL_SETUP_CHECKLISTE.md) – Signal/signal-cli (für Phase 2 relevant)

## Architektur (Kurz)

| Komponente | Rolle |
|------------|--------|
| Clawdbot | Produktions-Gateway (unverändert lassen bis Freigabe) |
| Hermes Profil `pilot` | Pilot: Anthropic-Modell, Flora-Workspace, **neuer** Telegram-Bot |
| `~/.hermes` (default) | Optional für andere Hermes-Nutzung; Secrets getrennt vom Profil `pilot` |

**Telegram:** Ein **neuer** Bot bei @BotFather – **nicht** denselben Token wie der produktive Sage-/Clawdbot-Bot.

**Signal (Phase 2):** Dieselbe Signal-Identität nicht gleichzeitig an zwei Gateways hängen; separate Nummer/Profil oder bewusster Kanalwechsel dokumentieren.

---

## 1. Voraussetzungen (VM102)

- SSH: `ssh user@docker-apps` (siehe [`clawdbot_vm102.md`](clawdbot_vm102.md))
- Backup von `~/.clawdbot-personal` liegt typischerweise unter `~/backups/` (wie bei euch üblich)
- Ports: Clawdbot-Gateway nutzt u. a. **127.0.0.1:18789**; Hermes-Gateway läuft als **eigener Prozess** (kein Port-Konflikt mit Clawdbot, solange keine doppelte Belegung derselben Listener-Konfiguration)
- Pilot-Allowlist: Telegram-User-ID **665037248** (Flora) in `TELEGRAM_ALLOWED_USERS` im Profil `pilot`

---

## 2. Hermes installieren (ohne interaktives `install.sh`)

Das offizielle `install.sh` kann über SSH ohne TTY abbrechen (`/dev/tty`). Bewährt hat sich:

```bash
cd ~
git clone --depth 1 https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
uv venv .venv --python 3.11
uv pip install -e ".[all]"
mkdir -p ~/.local/bin
ln -sf ~/hermes-agent/.venv/bin/hermes ~/.local/bin/hermes
```

CLI prüfen:

```bash
~/.local/bin/hermes --version
~/.local/bin/hermes doctor
```

`PATH`: `~/.local/bin` in `~/.bashrc` aufnehmen, falls noch nicht geschehen.

---

## 3. Modell (Anthropic)

Beispiel (Namen an euren Hermes-Katalog anpassen):

```bash
~/.local/bin/hermes config set model.provider anthropic
~/.local/bin/hermes config set model.default anthropic/claude-sonnet-4-5-20250929
```

---

## 4. Migration aus Clawdbot (`~/.clawdbot-personal`)

Hermes erwartet typischerweise OpenClaw-Pfade; bei euch ist der State unter **`~/.clawdbot-personal`**.

Vorschau:

```bash
~/.local/bin/hermes claw migrate --dry-run --source ~/.clawdbot-personal --migrate-secrets
```

Anwenden (nach Review):

```bash
~/.local/bin/hermes claw migrate --source ~/.clawdbot-personal --migrate-secrets -y
```

**Hinweis:** `model-config` kann kollidieren, wenn ihr das Modell schon manuell gesetzt habt – das ist beabsichtigt (Pilot behält Anthropic-Konfiguration).

---

## 5. Workspace (SOUL / USER / AGENTS) für Flora

Die Migration hat u. a. kein `SOUL.md` aus „OpenClaw“-Pfaden gezogen. Für den Flora-Pilot manuell aus dem bestehenden Workspace synchronisieren:

```bash
for f in SOUL.md USER.md AGENTS.md WELCOME_MESSAGE.md HEARTBEAT.md CRON.md; do
  cp -a ~/clawd/workspace-flora/"$f" ~/.hermes/"$f"
done
```

Für das **Profil `pilot`** dieselben Dateien nach `~/.hermes/profiles/pilot/` kopieren (oder Profil erst später anlegen und dann kopieren – siehe Abschnitt 6).

---

## 6. Profil `pilot` (Isolation gegenüber Default)

```bash
~/.local/bin/hermes profile create pilot --clone --no-alias
```

Anpassungen im **Profil `pilot`** (Pfad `~/.hermes/profiles/pilot/`):

1. **`MESSAGING_CWD`** auf Floras Workspace: `~/clawd/workspace-flora`
2. **`TELEGRAM_ALLOWED_USERS=665037248`**
3. **Kein** `TELEGRAM_BOT_TOKEN` aus dem produktiven Bot – Zeile entfernen, bis der **neue** Pilot-Bot bei @BotFather existiert
4. **Signal (nur Telegram-Phase):** Für Hermes **keine** gleichzeitige Signal-Anbindung über fehlerhafte Rest-Env: `SIGNAL_ACCOUNT` und `SIGNAL_HTTP_URL` im Profil `pilot` nur setzen, wenn signal-cli für Hermes wirklich geplant und erreichbar ist (sonst startet das Gateway nicht oder nur mit Warnung)

Wrapper (Pfad prüfen, ggf. absolut zu `hermes`):

```bash
~/.local/bin/hermes profile alias pilot
# Falls nötig: erste Zeile im Wrapper auf /home/user/.local/bin/hermes zeigen
```

---

## 7. Telegram: neuen Pilot-Bot anlegen

1. In Telegram: **@BotFather** → `/newbot` → Token kopieren
2. Auf VM102 in **`~/.hermes/profiles/pilot/.env`** eine Zeile ergänzen:

   `TELEGRAM_BOT_TOKEN=<vom neuen Bot>`

3. Niemals den Token des laufenden Produktionsbots wiederverwenden

---

## 8. systemd (user) – `hermes-gateway-pilot`

Installation (wird `hermes-gateway-pilot.service` anlegen):

```bash
/home/user/.local/bin/pilot gateway install --force
```

Status und Logs:

```bash
systemctl --user status hermes-gateway-pilot
journalctl --user -u hermes-gateway-pilot -f
```

**Wichtig:** Ohne gültigen `TELEGRAM_BOT_TOKEN` ist kein Telegram-Adapter aktiv – das Gateway kann mit Warnung laufen oder fehlschlagen, bis der Token gesetzt ist. Nach Setzen des Tokens:

```bash
/home/user/.local/bin/pilot gateway restart
```

---

## 9. E2E-Tests (Akzeptanz)

### 9.1 Modell / CLI (ohne Telegram)

```bash
/home/user/.local/bin/pilot chat -q 'Antworte nur mit dem Wort OK.'
```

Erwartung: Antwort **OK** (oder gleichwertig), kein Modellfehler.

### 9.2 Telegram (nach Bot-Token)

1. Kurze Nachricht an den Pilot-Bot → Antwort
2. Längere Anfrage (kein Timeout)
3. **Sparring-Phrase** (intern vereinbart) → erwartetes Verhalten
4. Bei Fehlern: `journalctl --user -u hermes-gateway-pilot` muss einen Eintrag haben (kein „stiller“ Ausfall)

### 9.3 Optional: Voice

Später gemäß Hermes-Doku (Voice Mode), wenn Text stabil ist.

---

## 10. Phase 2: Signal

- **Nicht** dieselbe Signal-Identität parallel an Clawdbot-Gateway und Hermes binden
- Optionen: zweite Nummer / separates signal-cli-Profil / zeitweise nur ein Gateway mit Signal
- Health-Checks und HTTP-URL wie in eurer bestehenden Signal-Doku ([`CLAWDBOT_SIGNAL_SETUP_CHECKLISTE.md`](CLAWDBOT_SIGNAL_SETUP_CHECKLISTE.md)) – Hermes-seitig eigene Konfiguration im Profil

---

## 11. Rollback

```bash
systemctl --user stop hermes-gateway-pilot
systemctl --user disable hermes-gateway-pilot
```

Clawdbot bleibt unberührt; Pilot-Bot einfach nicht mehr verwenden.

---

## Referenz: Wichtige Pfade auf VM102

| Pfad | Inhalt |
|------|--------|
| `~/hermes-agent/` | Git-Checkout + `.venv` |
| `~/.local/bin/hermes` | Symlink zur CLI |
| `~/.hermes/` | Default-Hermes-Home |
| `~/.hermes/profiles/pilot/` | Profil inkl. `.env`, `config.yaml`, SOUL/… |
| `~/.clawdbot-personal/` | Quelle für `hermes claw migrate` |
| `~/clawd/workspace-flora/` | Flora-Workspace (AGENTS/SOUL/…) |
