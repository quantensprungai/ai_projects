<!-- Reality Block
last_update: 2026-06-23
status: draft
scope:
  summary: "IB Gateway Setup-Checkliste für options-book (Live, Read-Only Stufe 1)."
  in_scope:
    - settings checklist
    - ports
    - safety
  out_of_scope:
    - credentials
notes: []
-->

# IB Gateway — Setup-Checkliste

## Dein aktueller Stand (2026-06-23)

| Setting | Status | Bewertung |
|---------|--------|-----------|
| Gateway verbunden | ✅ API-Server verbunden | OK |
| Marktdaten | ✅ usfarm | OK |
| Socket Port | **4001** | ✅ **Live** Gateway (korrekt ohne Paper) |
| Read-Only API | ✅ aktiv | ✅ **Sehr gut** für Stufe 1 |
| Nur localhost | ✅ + 127.0.0.1 | OK |
| Vorsichtseinstellungen | alle aus | OK (Read-Only = keine Orders sowieso) |

## Ports

| Modus | IB Gateway | TWS |
|-------|------------|-----|
| **Live** | **4001** ← du | 7496 |
| Paper | 4002 | 7497 |

## Live ohne Paper — Sicherheit

1. **Read-Only API** bleibt an, bis wir explizit Orders bauen
2. Kein Auto-Execution in options-book MVP
3. Optional später: **Paper-Sub-Account** bei IBKR beantragen (kostenlos) zum Testen

## Log-Meldungen (harmlos)

Zeilen wie `Parent for Dialog does not implement IToFrontAsGroupWindow` sind **Java-UI-Infos**, keine Fehler. Gateway läuft.

## Was die KI braucht / nicht braucht

| Braucht **nicht** (nie in Chat posten) | Braucht lokal |
|----------------------------------------|---------------|
| Passwort, 2FA | Gateway läuft |
| Volle Kontonummer | `.env` mit Port 4001 |
| API nicht nötig wenn Read-Only | `pip install -r requirements.txt` |
| | `python scripts/test_connect.py` |

Erfolg = `Connected: True` + Account-Liste (maskiert ok).

## „ActiveX und Socket-Clients aktivieren“ fehlt?

**Normal bei IB Gateway.** Diese Checkbox gibt es primär in **TWS**, nicht zwingend in Gateway.

Laut IBKR-Doku: **IB Gateway akzeptiert Socket-API-Verbindungen standardmäßig** — anders als TWS, wo die Option erst aktiviert werden muss.

Entscheidend sind stattdessen:
- Socket-Port sichtbar (bei dir **4001**)
- **Nur Verbindungen vom lokalen Host** + **127.0.0.1**
- Gateway eingeloggt, Status „API-Server verbunden“

**Verbindungstest 2026-06-23:** `Connected: True` auf Port 4001 ✅  
**Stufe 1 Sync:** `python scripts/sync_positions.py` — 0 Positionen (leeres Konto) ✅

## API-Popup („API aktivieren“)

Beim **ersten** Python-Connect kann Gateway kurz fragen, ob eingehende API-Verbindungen erlaubt sind → **Ja / Allow**.  
Popup verschwindet oft schnell; bei erneutem Connect ggf. nochmal bestätigen.

Log bei Read-Only (normal):
```text
Die API befindet sich im schreibgeschützten Modus.
```

Log bei leerem Konto (normal):
```text
Book is absent during iserver update.
Positions are received for accounts: {U...=0}
```

```powershell
cd code/options-book
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# .env: IBKR_PORT=4001
python scripts/test_connect.py
```
