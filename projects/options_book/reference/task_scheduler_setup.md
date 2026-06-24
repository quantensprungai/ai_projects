<!-- Reality Block
last_update: 2026-06-23
status: draft
scope:
  summary: "Windows Task Scheduler für täglichen AlgoBot-Run."
  in_scope:
    - setup steps
    - schedule notes
  out_of_scope:
    - Cursor Automations
notes: []
-->

# Task Scheduler — Daily Run

## Läuft das wirklich nur 1×/Tag?

**Ja, so gedacht** — ein Morning Monitor nach US-Close:

| Mechanismus | Verhalten |
|-------------|-----------|
| **Task Scheduler** | 1× pro geplantem Trigger (z. B. Mo–Fr 22:00) |
| **News-Cache** (`news.cache_per_day: true`) | Pro Ticker max. **1 Claude-Call pro Kalendertag**, auch bei Re-Runs |
| **Manueller Re-Run** | `python run.py` jederzeit möglich — Layer 1–2 holen frische Quotes; News wird nicht erneut abgerechnet am selben Tag |

Später mehrfach täglich: Task duplizieren oder Intervall ändern — Cache schützt vor News-Doppelkosten.

---

## Pfade

| Was | Pfad |
|-----|------|
| **API-Key (.env)** | `code/options-book/.env` (von `.env.example` kopieren) |
| **Daily Script** | `code/options-book/scripts/run_daily.ps1` |
| **Logs** | `code/options-book/logs/run_YYYY-MM-DD.log` |

---

## Langdock (Claude)

In `.env`:

```env
ANTHROPIC_API_KEY=dein_langdock_api_key
ANTHROPIC_BASE_URL=https://api.langdock.com/anthropic/eu/
```

Modell in `config.yaml`:

```yaml
claude:
  model: claude-opus-4-8@default
```

Dedicated Deployment? Base-URL laut [Langdock-Doku](https://docs.langdock.com/en/developer/completion-api/anthropic) anpassen.

---

## Task Scheduler einrichten (Windows)

**Einmalig (automatisch):**

```powershell
cd C:\Users\he5013\ai-projects\code\options-book
.\scripts\register_task.ps1
```

Registriert **AlgoBot Morning Monitor** — Mo–Fr 22:00.

**Manuell testen:**

```powershell
Start-ScheduledTask -TaskName "AlgoBot Morning Monitor"
# oder
.\scripts\run_daily.ps1
```

Log: `logs/daily_YYYY-MM-DD.log`

---

## Task Scheduler manuell (Alternative)

1. **IB Gateway** muss zum Laufzeitpunkt laufen (Live **4001**).
2. Aufgabe erstellen → Trigger: **Mo–Fr, 22:00** (nach US-Close CET/CEST anpassen).
3. Aktion: **Programm starten**
   - Programm: `powershell.exe`
   - Argumente: `-ExecutionPolicy Bypass -File "C:\Users\he5013\ai-projects\code\options-book\scripts\run_daily.ps1"`
   - Starten in: `C:\Users\he5013\ai-projects\code\options-book`
4. Optionen: „Unabhängig von der Benutzeranmeldung“ nur wenn Gateway als Dienst/Autostart läuft.

Test manuell:

```powershell
cd C:\Users\he5013\ai-projects\code\options-book
.\scripts\run_daily.ps1
```
