<!-- Reality Block
last_update: 2026-03-19
status: draft
scope:
  summary: "Template fuer Interface Agreements zwischen Plattform und Modul-Ownern."
  in_scope:
    - template structure
    - governance checklist
  out_of_scope:
    - project-specific schema details
notes: []
-->

# Interface Agreement (Template)

Zweck: Verbindliche Vereinbarung zwischen Modul-Owner und Plattform (Heiko), bevor Daten geliefert oder integriert werden.

## 1) Meta
- Modulname:
- Modul-Owner:
- Plattform-Owner:
- Version:
- Datum:
- Status: Draft | Review | Approved

## 2) Fachlicher Scope
- Ziel des Moduls (1-2 Saetze):
- In Scope:
- Out of Scope:
- Stage: A | B | C
- Ampelstatus der Datenpunkte: Gruen | Gelb | Rot

## 3) Lieferobjekt
- Welche Ergebnisse liefert das Modul?
- Frequenz: einmalig | zyklisch (woechentlich/monatlich) | on-demand
- Erstliefertermin:

## 4) Datenmodell (Co-Spezifikation)
| Feld | Datentyp | Pflicht? | Beschreibung | Beispiel | Mapping-Key |
|---|---|---|---|---|---|
| `asset_id` | text | ja | Eindeutige Asset-ID | `alpha_ventus_001` | `offshore_assets.asset_id` |
| `...` | ... | ... | ... | ... | ... |

## 5) Verknuepfung
- Primarschluessel:
- Fremdschluessel:
- Join-Logik:
- Umgang mit fehlenden Keys:

## 6) Lieferformat
- Format: CSV | JSON | API
- Encoding/Trennzeichen (falls CSV):
- Dateinamenskonvention:
- Transportweg (Storage/API/Git):
- Beispiel-Datei mit 3-5 Datensaetzen vorhanden: ja | nein

## 7) Qualitaetsregeln
- Pflichtfelder:
- Wertebereiche/Plausibilitaet:
- Dublettenregel:
- Versionierung (Source/Stand):
- Fehlerbehandlung (reject/warn/default):

## 8) Akzeptanzkriterien
- [ ] Import laeuft ohne Schemafehler
- [ ] Join auf Zielentitaet funktioniert
- [ ] Stichprobe fachlich valide
- [ ] Qualitaetsreport erstellt
- [ ] Owner-Abnahme erfolgt

## 9) Verantwortlichkeiten (RACI light)
- Datenbeschaffung: Owner
- Fachliche Validierung: Owner
- Schema/Migration: Plattform
- Import/Verknuepfung: Plattform
- Abnahme: Owner + Plattform

## 10) Risiken und Annahmen
- Risiko:
- Auswirkung:
- Mitigation:

## 11) Offene Punkte
- Punkt 1:
- Punkt 2:

## 12) Entscheidung
- Entscheidungstermin:
- Freigegeben durch:
