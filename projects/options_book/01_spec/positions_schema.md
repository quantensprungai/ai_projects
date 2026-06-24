<!-- Reality Block
last_update: 2026-06-23
status: draft
scope:
  summary: "positions.json Schema für Layer 1."
  in_scope:
    - field definitions
    - pricing conventions
  out_of_scope:
    - validation code
notes: []
-->

# positions.json — Schema

Eingabedatei für den Daily Run. Quelle: **IBKR-Sync** (`scripts/sync_positions.py`) oder manuell.

## Konventionen

- **Options-Preise** (`entry_price`, `target_price`, `stop_price`): **pro Share**
- **Kontrakt-Multiplikator:** 1 Kontrakt = **100 Shares** → Dollar-Wert = `price × 100 × contracts`
- **`id`:** optional; Auto-Format `ticker+strike+expiry` für Options

## Option

```json
{
  "id": "NOK20C2027-01-15",
  "asset_type": "option",
  "ticker": "NOK",
  "option_type": "call",
  "strike": 20.0,
  "expiry": "2027-01-15",
  "entry_price": 2.45,
  "contracts": 5,
  "entry_date": "2026-05-01",
  "target_price": 5.00,
  "stop_price": 1.20
}
```

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| `asset_type` | ✅ | `"option"` |
| `ticker` | ✅ | Underlying-Symbol |
| `option_type` | ✅ | `"call"` \| `"put"` |
| `strike` | ✅ | Strike-Preis |
| `expiry` | ✅ | `YYYY-MM-DD` |
| `entry_price` | ✅ | Premium pro Share beim Einstieg |
| `contracts` | ✅ | Anzahl Kontrakte |
| `entry_date` | ✅ | Eröffnungsdatum |
| `target_price` | ⬜ | Take-Profit pro Share |
| `stop_price` | ⬜ | Stop-Loss pro Share |

## Shares

```json
{
  "id": "MP-shares",
  "asset_type": "shares",
  "ticker": "MP",
  "entry_price": 18.50,
  "contracts": 200,
  "entry_date": "2026-05-01",
  "target_price": 28.00,
  "stop_price": 14.00
}
```

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| `asset_type` | ✅ | `"shares"` |
| `ticker` | ✅ | Symbol |
| `entry_price` | ✅ | Kaufkurs pro Aktie |
| `contracts` | ✅ | Anzahl Aktien |
| `entry_date` | ✅ | Kaufdatum |
| `target_price` | ⬜ | Zielkurs |
| `stop_price` | ⬜ | Stop-Kurs |

## Beispiel-Datei (Minimal)

2–3 Positionen (Mix Options + Shares) als Seed beim Layer-1-Build mitliefern.
