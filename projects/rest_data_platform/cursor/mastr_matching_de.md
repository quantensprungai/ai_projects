<!-- Reality Block
last_update: 2026-08-07
status: draft
scope:
  summary: "MaStR-DE Anreicherung — verständliche Pipeline + sauberer Stand."
  in_scope:
    - DE farm enrichment matching
    - Gesamtdatenexport XML UTF-16 ingest
    - review/accept/apply explained
  out_of_scope:
    - full MaStR Gesamtdownload automation
    - EU/non-DE registers
    - auto-overwrite of 4C primary fields
notes:
  - "Migration: code/astra-imc-platform/.../20260807120000_imc_mastr_matching.sql"
  - "ETL: scripts/etl/ingest_mastr.py, match_mastr_de.py, apply_mastr_matches.py"
  - "XML-Dir: .../02_Data/Extraction/MaStR"
-->

# MaStR → unsere Parks (einfach erklärt)

**Ziel:** Aus dem Behördenregister MaStR die **deutschen Offshore-Parks** in unserer DB anreichern (IDs, Inbetriebnahme). 4C bleibt die Hauptquelle für Design/Kapazität.

---

## Die drei Schritte in Alltagssprache

| Schritt | Was passiert | Vergleich |
|--------|----------------|-----------|
| **1. Match / Scoring** | Computer schlägt vor: „Park A in unserer DB = Park B in MaStR“ und vergibt eine **Note 0–1**, wie sicher das ist | Tinder-Vorschläge mit Score |
| **2. Accept** | Mensch (oder Batch-Regel) sagt: **ja, das stimmt** → Status `accepted` | Haken setzen |
| **3. Apply** | Erst jetzt werden Daten **geschrieben**: Alias `MaStRPark:…` + optional Inbetriebnahme | Speichern |

Ohne Accept+Apply ändert sich an den Farm-Stammdaten nichts — nur Vorschlagstabellen.

### Scoring (die „Note“)

| Note / Status | Bedeutung |
|---------------|-----------|
| `needs_review` / hoch | Name passt klar (+ Kapazität plausibel) → gut zum Accepten |
| `candidate` | möglich, aber unsicherer (z. B. nur Nähe) |
| `accepted` | freigegeben zum Schreiben |
| `rejected` | bewusst verworfen (z. B. Trianel II Doppelpark) |

Methoden: `exact_name`, `alias`, `fuzzy_name`, `geo` — nur **wie** der Vorschlag entstanden ist.

---

## Pipeline (technisch)

```
XML (EinheitenWind See + EEG + Kataloge)
  → ingest_mastr.py      # Rohdaten ablegen
  → match_mastr_de.py    # Vorschläge + Score
  → Accept (SQL)         # freigeben
  → apply_mastr_matches.py  # Aliases + Milestone schreiben
```

Datenort: `…/02_Data/Extraction/MaStR/`  
Lizenz: dl-de/by-2.0 (BNetzA).

### Lokal

```powershell
cd C:\Users\he5013\ai-projects\projects\rest_data_platform\scripts\etl
$env:DATABASE_URL="postgresql://postgres:postgres@127.0.0.1:54330/postgres"

python ingest_mastr.py --xml-dir "C:\Users\he5013\academiccloudsync\ASTRA_Maritime_Circularity\02_Data\Extraction\MaStR"
python match_mastr_de.py --latest
Get-Content .\accept_mastr_needs_review.sql -Raw |
  docker exec -i supabase_db_next-supabase-saas-kit-turbo psql -U postgres -d postgres
python apply_mastr_matches.py --reapply-aliases
```

Review: `review_mastr_matches.sql`  
Aufräumen Trianel-Ambiguität: `cleanup_mastr_trianel.sql`

### Tabellen

| Tabelle | Rolle |
|---------|--------|
| `imc_source_raw_rows` | Roh-XML als JSON |
| `imc_mastr_park_agg` | MaStR-WEA zu Parknamen summiert |
| `imc_mastr_farm_matches` | Vorschläge / Accept / Reject |

Apply schreibt nur: `aliases` (`MaStRPark:` + max. 1 `MaStR:SEE…`) und `full_commissioning` wenn leer.
