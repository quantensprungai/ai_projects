<!-- Reality Block
last_update: 2026-06-23
status: stable
scope:
  summary: "Windows Smart App Control + Python venv Hinweise."
  in_scope:
    - SAC explanation
    - mitigations
  out_of_scope:
    - enterprise policy details
notes: []
-->

# Windows Smart App Control (SAC)

## Hängt das mit options-book zusammen?

**Sehr wahrscheinlich ja.** Beim Layer-1-Build trat bereits auf:

```text
ImportError: DLL load failed while importing strptime:
Eine Anwendungssteuerungsrichtlinie hat diese Datei blockiert.
```

Typische Auslöser in unserem Stack:
- **pandas** (über yfinance) — native DLLs
- Python **venv** unter `.venv/` — nicht signiert
- ggf. **ib_async** / andere Wheels

**Nicht** von uns: IB Gateway (Java, separat signiert) — läuft meist trotzdem.

## Was tun?

| Option | Empfehlung |
|--------|------------|
| **Weitere Informationen** im Popup → welche Datei blockiert wurde | Erst schauen, nicht blind alles erlauben |
| SAC auf **Aus** oder **Überwachung** (Evaluation) | Pragmatisch für lokale Dev-Maschine |
| Projekt in **vertrauenswürdigen Pfad** (z. B. `C:\Users\...\ai-projects`) | Hilft manchmal |
| **Kein** pandas direkt importieren | Bereits im Code vermieden; yfinance nutzt pandas intern trotzdem |

## Funktioniert options-book trotzdem?

Ja — Layer 1+2 laufen bei dir bereits erfolgreich. SAC blockiert ggf. **einzelne DLLs**, nicht das ganze Projekt.

Schutzverlauf: **Windows-Sicherheit → Viren- & Bedrohungsschutz → Schutzverlauf**

## Produktion / Cron

Für Daily Run: SAC dauerhaft störend → Evaluation-Modus oder Aus für den Dev-PC; auf Server separat entscheiden.
