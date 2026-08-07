<!-- Reality Block
last_update: 2026-08-07
status: draft
scope:
  summary: "Slice-1 DQ-Ampel DE aktiv — leichter Check nach Alpha-Ventus-Kuratierung."
  in_scope:
    - DE active farm quality
    - Alpha Ventus pilot checks
  out_of_scope:
    - full DQ framework
    - MaStR matching
notes:
  - "SQL: scripts/etl/dq_check_de_active.sql"
-->

# DQ-Ampel — Slice 1 (DE aktiv)

**Scope:** `country = Germany`, `lifecycle_phase <> cancelled`  
**Stand:** 2026-08-07 · lokal · SQL: `scripts/etl/dq_check_de_active.sql`

## Gesamturteil: **GELB → Demo-grün**

Slice-1 ist **demo-fähig**. Pflichtfelder und Pilot sind in Ordnung; Foundation/Kapazität bei einem Teil der DE-Pipeline noch lückenhaft — für Stage A akzeptabel, nicht für „vollständige DE-Statistik“.

## Checks

| Check | Ergebnis | Ampel |
|-------|----------|-------|
| DE aktiv Gesamt | **76** | grün |
| Name fehlt | 0 | grün |
| Status fehlt | 0 | grün |
| Quelle fehlt | 0 | grün |
| Standort fehlt | 0 | grün |
| Dubletten Name+Land | 0 | grün |
| Kapazität fehlt | **7 / 76** (~9 %) | gelb |
| Foundation fehlt/`unknown` | **29 / 76** (~38 %) | gelb |
| Status operational | 32 | grün |
| Status under_construction | 5 | grün |
| Status planning (+ early/pre/…) | Rest plausibel | grün |

## Alpha Ventus (Pilot)

| Feld | Wert | Ampel |
|------|------|-------|
| Status | operational | grün |
| ext_id | DE01 | grün |
| Foundation | tripod (kuratiert) | grün |
| Kapazität / Turbinen | 60 MW / 12 | grün |
| Lat/Lon | 54.01 / 6.61 | grün |
| Quelle | 4C Wind Farm Database | grün |
| Kuratierungsnotiz | ja | grün |

**Pilot: GRÜN**

## Interpretation

- **Grün für Demo-Pfad** (Liste → Alpha Ventus → CSV).
- **Gelb für Register-Vollständigkeit:** viele frühe/geplante Parks ohne klare Foundation in 4C — erwartbar, nicht Transform-Crash.
- **Nicht Rot:** keine Dubletten, keine fehlenden Stammdaten-Namen/Status/Quellen/Koordinaten.

## Nächster Schritt (empfohlen)

1. MVP Slice-1 als Stage-A-Demonstrator **einfrieren** (Commit/Cloud optional).
2. Inhaltlich: **MaStR-Enrichment** oder Turbine-Modell an Alpha Ventus — nicht UI-Aufbohrung.
3. Foundation-Lücken erst angehen, wenn ein Use Case sie braucht (nicht pauschal normalisieren).
