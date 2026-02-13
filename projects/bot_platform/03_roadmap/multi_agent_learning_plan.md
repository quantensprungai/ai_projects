<!-- Reality Block
last_update: 2026-02-11
status: draft
scope:
  summary: "Umsetzungsplan: 4 Agents (heiko, noah, flora, familie) mit individuellem Fokus."
  in_scope:
    - Recherche-Ergebnis (bestätigt möglich)
    - Schritt-für-Schritt-Plan
  out_of_scope:
    - Ops Profil / andere Bots
notes: []
-->

# Plan: Multi-Agent Learning (ein Agent pro Person)

## Status (2026-02-12)

**Erledigt (via SSH auf VM102):**
- [x] 4 Agents angelegt: `heiko`, `noah`, `flora`, `familie`
- [x] Workspaces erstellt: `~/clawd/workspace-{heiko,noah,flora,familie}`
- [x] AGENTS.md, SOUL.md, USER.md pro Agent mit Fokus
- [x] Bindings in Config (Platzhalter für Signal-IDs)
- [x] Gateway neu gestartet

**Noch zu tun:**
- [ ] **Java + signal-cli** auf VM102 installieren → siehe `infrastructure/docker/CLAWDBOT_SIGNAL_SETUP_CHECKLISTE.md`
- [ ] **Signal-Bot-Nummer** verlinken: `signal-cli link -n "Clawdbot"` → QR-Code
- [ ] **Config:** `channels.signal` aktivieren, `account` eintragen
- [ ] **Bindings:** Platzhalter in `~/.clawdbot-personal/clawdbot.json` ersetzen durch echte E.164-Nummern (Heiko, Noah, Flora) bzw. Gruppen-ID (Familie)
- [ ] **Pairing:** Jede Person pairen, `clawdbot --profile personal pairing approve signal <CODE>`

---

## 1) Recherche-Ergebnis: Ja, es ist möglich

**Bestätigt durch:**
- Offizielle Docs: https://docs.clawd.bot/concepts/multi-agent
- Blog (Feb 2026): Complete Guide to OpenClaw Multi-Agent Routing (EastonDev)
- Session-Docs: Secure DM mode für Multi-User-Setups

**Kernaussagen:**
- "Multiple agents = multiple people, multiple personalities"
- "True isolation requires one agent per person"
- Jeder Agent: eigener Workspace, eigenes agentDir, eigene Sessions
- **Keine Datenvermischung** zwischen Agents
- Routing via **Bindings** (match auf `peer.id`, `channel`, `accountId`)

**Hinweis:** Clawdbot = OpenClaw (gleiches Projekt, Rebrand Jan 2026). Docs unter docs.clawd.bot gelten.

---

## 2) Design-Entscheidungen (bestätigt)

| Frage | Antwort |
|-------|---------|
| **Ein Agent pro Person?** | Ja. Ein Agent pro Person für vollständige Isolation (Workspace, Sessions, Memory). |
| **Person 1 hat andere Themen (nicht Learning)?** | Kein Problem. Jeder Agent kann individuell konfiguriert werden (AGENTS.md, SOUL.md, USER.md). |
| **Individueller Fokus pro Agent?** | Ja. Pro Agent: eigenes Workspace mit AGENTS.md (Betriebsanweisungen), SOUL.md (Persona, Ton), USER.md (User-Profil). Optional: verschiedenes Modell, Tool-Allow/Deny. |
| **Starten mit 3–4 Personen?** | Ja. Plan ist für 3–4 Agents ausgelegt; Erweiterung trivial. |
| **Ressourcen-Probleme?** | Siehe Abschnitt 2b unten. |
| **Erweiterbar?** | Ja. Neuen Agent anlegen + Binding hinzufügen. |

### 2b) Ressourcen (VM102, Gateway-Modus)

**Wichtig:** Alle Agents laufen im **einen** Gateway-Prozess. Es gibt keine separaten Prozesse pro Agent – nur Routing + getrennte Workspaces/Sessions.

| Ressource | Einfluss | Hinweise |
|-----------|----------|----------|
| **RAM** | Gering. Hauptsächlich ein Gateway-Prozess; Sessions werden bei Bedarf geladen. 3–4 Agents: typisch ~500MB–1GB zusätzlich. | VM102 sollte ausreichend RAM haben. |
| **Disk** | Pro Agent: Workspace (~10–100MB je nach Inhalt), Sessions (JSONL). 4 Agents: ~500MB–1GB. | Backup-Plan existiert. |
| **LLM (Spark)** | **Hauptkosten.** Jede Nachricht = 1 LLM-Call. 4 Personen parallel chatten = 4× Inference. | Spark-Last steigt mit Nutzung, nicht mit Agent-Anzahl. |
| **CPU** | Minimal. Gateway ist I/O-lastig (Message-Routing, JSON). | Unkritisch. |

**Fazit:** Mit 3–4 Personen und normaler Nutzung gibt es kaum Ressourcen-Probleme. Limitierend ist eher Spark (LLM), wenn viele gleichzeitig chatten.

---

## 4) Agent-Definitionen (konkret)

| Agent-ID | Person/Zielgruppe | Fokus | Workspace |
|----------|-------------------|-------|-----------|
| **heiko** | Heiko | Projekte, Reminder, Multiprojektworkspace (ai_projects), Doku, TODOs | `~/clawd/workspace-heiko` |
| **noah** | Noah | Lernagent 5.–6. Klasse Gym (Fächer, Hausaufgaben, Spaced Repetition) | `~/clawd/workspace-noah` |
| **flora** | Flora | Lernagent duales Studium Physiotherapie (Examensvorbereitung, Theorien, Praxistipps) | `~/clawd/workspace-flora` |
| **familie** | Familie (alle) | Allgemeinwissen, Geburtstage, Urlaub, Wetter, Termine, Finanzen, gemeinsame Planung | `~/clawd/workspace-familie` |

**Hinweis zu Heiko:** Für vollen Zugriff auf ai_projects müsste das Repo auf VM102 verfügbar sein (z. B. git clone). Alternativ: Workspace mit Projekt-Notizen, Doku-Auszügen, Reminder-Listen – der Agent hat dann Kontext ohne direkten Code-Zugriff.

---

## 5) Channels: Signal (primär) + Telegram (optional)

**Signal** ist voll unterstützt und kann **allein** oder **zusammen mit Telegram** genutzt werden. Channels laufen parallel.

| Channel | Priorität | Setup |
|---------|-----------|-------|
| **Signal** | Primär | `signal-cli` (Java nötig), eigene Bot-Nummer empfohlen, Pairing wie Telegram |
| **Telegram** | Optional (nice to have) | Bot-Token, einfacher zu starten |

**Signal-Setup (Kurz):**
1. `signal-cli` installieren (Java erforderlich)
2. Bot-Account verlinken: `signal-cli link -n "OpenClaw"` → QR-Code
3. Config: `channels.signal.enabled: true`, `account`, `dmPolicy: "pairing"`, `allowFrom`
4. Pairing: `clawdbot pairing list signal` / `clawdbot pairing approve signal <CODE>`

**Peer-IDs für Bindings:**
- **Signal:** E.164 (`+49...`) oder `uuid:<id>` (nach Pairing)
- **Telegram:** numerische User-ID oder `+49...` je nach Connector

Quelle: https://docs.clawd.bot/channels/signal

---

## 6) Voraussetzungen (bereits vorhanden)

- [x] VM102: Clawdbot Gateway, Profil `personal` (Port 18789)
- [x] Tailscale Serve für Control UI
- [x] Spark als LLM-Backend
- [ ] Signal (signal-cli) oder Telegram als Channel
- [ ] Liste der Personen + ihre Signal-Nummern (E.164) oder Telegram-IDs

---

## 7) Umsetzungsschritte

### Phase A: Vorbereitung (ohne Änderung am laufenden Gateway)

| Schritt | Aktion | Doku |
|---------|--------|------|
| A1 | **4 Agents** festgelegt: `heiko`, `noah`, `flora`, `familie`. Siehe Abschnitt 4. | — |
| A2 | **Signal:** E.164-Nummern pro Person (für Bindings). Oder **Telegram:** User-IDs (z. B. @userinfobot). Beide parallel möglich. | Pairing-Liste |
| A3 | Workspace-Pfade planen: `~/clawd/workspace-<agentId>` | Runbook State-Pfade |

### Phase B: Agents hinzufügen (auf VM102)

| Schritt | Aktion | Kommando / Ort |
|---------|--------|----------------|
| B1 | SSH nach VM102, Profil `personal` aktiv | `ssh user@vm102` |
| B2 | Neuen Agent anlegen (pro Person) | `clawdbot --profile personal agents add heiko` (analog: `noah`, `flora`, `familie`) |
| B3 | Wizard/Bindings: Workspace-Pfad setzen, ggf. Bindings für Peer-Routing | Wizard fragt nach Workspace, `--bind` optional |
| B4 | Config prüfen: `~/.clawdbot-personal/openclaw.json` (oder `clawdbot.json`) | `agents.list`, `bindings` |

**Config-Beispiel (manuell, falls Wizard nicht reicht):**

```json
{
  "agents": {
    "list": [
      {
        "id": "main",
        "default": true,
        "workspace": "~/clawd/workspace",
        "name": "General"
      },
      {
        "id": "heiko",
        "workspace": "~/clawd/workspace-heiko",
        "name": "Heiko (Projekte/Reminder)"
      },
      {
        "id": "noah",
        "workspace": "~/clawd/workspace-noah",
        "name": "Noah (Lernagent 5.–6. Klasse Gym)"
      },
      {
        "id": "flora",
        "workspace": "~/clawd/workspace-flora",
        "name": "Flora (Lernagent duales Studium Physiotherapie)"
      },
      {
        "id": "familie",
        "workspace": "~/clawd/workspace-familie",
        "name": "Familie (Allgemeinwissen, Termine, Finanzen)"
      }
    ]
  },
  "bindings": [
    { "agentId": "heiko", "match": { "channel": "signal", "peer": { "kind": "direct", "id": "+49..." } } },
    { "agentId": "noah", "match": { "channel": "signal", "peer": { "kind": "direct", "id": "+49..." } } },
    { "agentId": "flora", "match": { "channel": "signal", "peer": { "kind": "direct", "id": "+49..." } } },
    { "agentId": "familie", "match": { "channel": "signal", "peer": { "kind": "group", "id": "<SIGNAL_GRUPPEN_ID>" } } },
    { "agentId": "main", "match": { "channel": "signal" } }
  ]
}
```

**Signal:** Peer-ID = E.164 (`+49...`) oder `uuid:<id>` (nach Pairing). Für Gruppen: `peer.kind: "group"` + Gruppen-ID.

**Zusätzlich Telegram:** Wenn beides genutzt wird, einfach weitere Bindings mit `channel: "telegram"` hinzufügen. Dieselbe Person kann auf Telegram und Signal denselben Agent nutzen; `session.identityLinks` sorgt für gemeinsame Session (optionale Konfiguration).

**Familie:** Entweder Signal-Gruppe (Binding) oder je Person ein Binding mit `peer.kind: "direct"` (dann teilen sie denselben Workspace).

**Fokus pro Agent (AGENTS.md, SOUL.md, USER.md):**

| Agent | AGENTS.md / Fokus |
|-------|-------------------|
| heiko | Multiprojektworkspace ai_projects, Reminder, Doku, TODOs, Projekt-Kontext |
| noah | 5.–6. Klasse Gym: Fächer, Hausaufgaben, Spaced Repetition, Lernpläne |
| flora | Duales Studium Physiotherapie: Examensvorbereitung, Anatomie, Theorien, Praxistipps |
| familie | Allgemeinwissen, Geburtstage, Urlaub, Wetter, Termine, Finanzen, gemeinsame Planung |

**Wichtig:** Bindings sind "most-specific wins". Peer-Bindings müssen vor dem Channel-Fallback liegen.

### Phase C: Pairing & Test

| Schritt | Aktion | Kommando |
|---------|--------|----------|
| C1 | Channel mit Pairing aktiv (Signal oder Telegram) | `dmPolicy: "pairing"` in Config |
| C2 | Jede Person: Pairing-Code holen, du approve | `clawdbot --profile personal pairing list signal` / `approve` (analog: `telegram`) |
| C3 | Test: Person A schickt Nachricht → landet bei Agent A | — |
| C4 | Test: Person B schickt Nachricht → landet bei Agent B | — |
| C5 | Test: Datei in Workspace A erstellen, Agent B kann sie nicht sehen | — |

### Phase D: Learning-spezifische Anpassungen (optional)

| Schritt | Aktion | Referenz |
|---------|--------|----------|
| D1 | Pro Agent: `AGENTS.md`, `SOUL.md`, `USER.md` für Lernthemen anpassen | Agent Workspace |
| D2 | `memory/`-Struktur für Spaced Repetition / Lernpläne | `memory/YYYY-MM-DD.md` |
| D3 | Cron-Jobs für Spaced Repetition (falls gewünscht) | Cron-Tools |

---

## 8) Erweiterung (weitere Agents)

Einfach:
1. `clawdbot --profile personal agents add <agentId>`
2. Binding in Config ergänzen: `{ "agentId": "<agentId>", "match": { "channel": "telegram", "peer": { "kind": "direct", "id": "<TELEGRAM_ID>" } } }`
3. Workspace-Dateien anpassen (AGENTS.md, SOUL.md, USER.md)
4. Gateway ggf. neu starten (oder Config Hot-Reload, falls unterstützt)

Keine Änderung an bestehenden Agents nötig.

---

## 9) Fallback: Ein Agent, mehrere Personen (dmScope)

Falls du **nicht** mehrere Agents willst, sondern **einen** Learning-Agent mit mehreren Usern:

- **Problem:** Ohne `dmScope` teilen alle DMs dieselbe Session → Datenleck.
- **Lösung:** `session.dmScope: "per-channel-peer"` setzen.
- **Nachteil:** Gleicher Workspace für alle – keine getrennten Lernthemen/Wissensbasen pro Person.

**Für verschiedene Lernthemen pro Person:** Multi-Agent (ein Agent pro Person) ist die richtige Lösung.

---

## 10) Backup & State

Vor Änderungen an der Config:

- `~/.clawdbot-personal/` (oder `~/.clawdbot/` je nach Profil-Setup)
- `~/clawd/` (Workspaces)

Diese Pfade sind bereits im Runbook als backup-relevant dokumentiert.

---

## 11) Offene Punkte

- [ ] Exakte Config-Pfade für clawdbot mit Profil `personal` (`.clawdbot-personal` vs. `.clawdbot`)
- [ ] CLI: `clawdbot` ist Alias für `openclaw` – Subcommands wie `agents add`, `agents list` sollten identisch sein
- [ ] WebChat/Control UI: Wie wählt man den Agent? (Vermutlich über Session/Binding, nicht explizit)

---

## 12) Referenzen

- **Signal:** https://docs.clawd.bot/channels/signal
- **Telegram:** https://docs.clawd.bot/channels/telegram
- Multi-Agent: https://docs.clawd.bot/concepts/multi-agent
- Agent Workspace: https://docs.clawd.bot/concepts/agent-workspace
- Session (Secure DM): https://docs.clawd.bot/concepts/session
- Wizard: https://docs.clawd.bot/start/wizard
- Runbook: `infrastructure/docker/clawdbot_vm102.md`
- Profiles: `projects/bot_platform/02_system_design/profiles_and_bots.md`
