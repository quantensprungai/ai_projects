<!-- Reality Block
last_update: 2026-06-23
status: draft
scope:
  summary: "Daily run: Python vs Cursor Automations."
  in_scope:
    - recommendation
    - automation draft outline
  out_of_scope:
    - creating automation in chat
notes: []
-->

# Daily Run — Python vs. Cursor Automations

## Kurzantwort

| Was | Wo |
|-----|-----|
| **Layer 1–4 Logik** (Macro, News, Alerts) | **Code** in `options-book` |
| **Täglich ausführen** nach Close | **Cursor Automation** *oder* Windows Task Scheduler |

Layer 3 **Claude News** läuft über **Anthropic API** im Python-Script — **nicht** über Cursor Automations als Ersatz.

---

## Warum nicht Automations statt Layer 3?

Cursor Automations = geplanter **Agent**, der im Repo arbeitet (PR, Slack, …).

Unser Morning Monitor braucht:
- deterministische Pipeline (`run.py`)
- SQLite + Snapshots
- IB Gateway lokal
- ~$1/Tag Anthropic API (gecacht)

→ **Python-Script** ist stabiler, billiger, reproduzierbar.

Automations **danach** sinnvoll für: *„Mo–Fr 22:00 CET: `git pull && python run.py`“*

**Research-Wartung (wöchentlich/monatlich):** [`research_cadence.md`](research_cadence.md)

---

## Empfohlene Automation (später)

| Feld | Vorschlag |
|------|-----------|
| **Trigger** | Cron werktags 22:00 (nach US-Close CET) |
| **Repo** | `quantensprungai/options-book` |
| **Prompt** | Gateway muss laufen; `python run.py --asof $(date)`; Log committen optional |
| **Tools** | Kein MCP nötig — Shell im Agent |

**Voraussetzung:** IB Gateway auf dem gleichen Rechner läuft (oder VM).

Alternativ Windows: **Task Scheduler** + `run_daily.ps1` — ohne Cursor Cloud.

---

## Nächster Schritt

1. Layer 4 bauen (Alerts + Dashboard)
2. Dann Automation **oder** Task Scheduler für Daily Run
3. `ANTHROPIC_API_KEY` in `.env` für News
