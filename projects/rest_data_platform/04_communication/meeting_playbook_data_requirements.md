<!-- Reality Block
last_update: 2026-03-19
status: draft
scope:
  summary: "Moderationsleitfaden fuer das Data/Requirements-Meeting (Marc, Shubham, Heiko, Thomas)."
  in_scope:
    - agenda
    - roles
    - decisions
  out_of_scope:
    - legal contract text
notes: []
-->

# Meeting Playbook: Daten- und Anforderungs-Klaerung

Zielgruppe: Marc, Shubham, Heiko, Thomas  
Dauer: 90 Minuten  
Format: Arbeitsmeeting mit Entscheidungen (kein allgemeines Brainstorming)

## 1) Ziel des Meetings
Am Ende stehen:
- priorisierte Stage-A-Datenpunkte (fuer Vertical Slice),
- 2-3 verbindliche Interface-Agreement-Kickoffs mit Ownern und Terminen,
- klare Modulgrenzen fuer Simulation, LCA, DPP-Light,
- ein gemeinsames "Nicht jetzt" fuer Stage-B/C-Themen.

## 2) Rollen im Meeting
- **Moderator (Heiko):** fuehrt durch Agenda, stoppt Scope-Creep, sichert Entscheidungen.
- **Fach-Owner LCA/BOM (Thomas):** benoetigte Felder, Proxyannahmen, Toolentscheidungspfad.
- **Fach-Owner Simulation (Marc):** Input/Output-Parameter, realistische Szenarien fuer Stage A.
- **Fach-Owner DPP/AAS (Shubham):** minimaler DPP-Light Scope, Mapping auf Datenentitaeten.
- **Protokoll (rotierend):** Entscheidungen, Owner, Termine live mitschreiben.

## 3) Vorab-Paket (48h vorher versenden)
- Architekturkurzbild (2 Layer + 3 Andockmodi)
- Daten-Ampel (Gruen/Gelb/Rot) mit Stage-A-Fokus
- Entwurf `interface_agreement_template.md`
- 1-seitiger Scope Shield
- Vorschlag "Definition of Ready fuer Modul-Kickoff"

## 4) Agenda (90 Minuten)
### 0-10 Min: Setup und Zielbild
- Ziel des Meetings und harte Leitplanken bestaetigen:
  - Vertical Slice vor Breite
  - Stage A nur Gruen + wenige Gelb-Proxy
  - Keine ungesicherten ROT-Abhaengigkeiten

### 10-30 Min: Datenpunkte priorisieren (Ampel-Board)
- Liste durchgehen und markieren:
  - **Must (Stage A now)**
  - **Should (wenn Zeit)**
  - **Later (Stage B/C)**
- Regel: jeder neue Wunsch braucht Owner + Datenzugang + Aufwandsschaetzung.

### 30-60 Min: Modul-Slots klaeren (LCA, Simulation, DPP)
- Pro Modul 10 Minuten:
  - Welche Inputs braucht ihr minimal?
  - Welche Outputs liefert ihr sicher bis Datum X?
  - Welches Format (CSV/JSON/API)?
  - Welche Keys fuer Join (`asset_id`, `component_id`)?
- Ergebnis: je Modul ein IA-Kickoff-Termin.

### 60-75 Min: Offene Entscheidungen mit Deadline
- DPP-Light Tiefe (Events+BOM+QR vs naehere ESPR-Abdeckung)
- LCA-Toolpfad (SimaPro/openLCA, ecoinvent-Frage)
- Simulationsszenarien Stage A
- 4C Trial/Lizenzbedingungen (Academic-Zugang, API-Nutzung, Persistenzrechte)

### 75-90 Min: Abschluss und Commitments
- Entscheidungen vorlesen und bestaetigen
- Owner + Termin + naechster Checkpoint
- Meeting endet erst mit konkreten "bis wann, von wem, in welchem Format"

## 5) Decision Log (im Protokoll)
| Thema | Entscheidung | Owner | Deadline | Risiko | Naechster Check |
|---|---|---|---|---|---|
| BOM-Light Felder | ... | Thomas/Heiko | ... | ... | ... |
| Sim-Output Schema | ... | Marc/Heiko | ... | ... | ... |
| DPP-Light Scope | ... | Shubham/Heiko | ... | ... | ... |

## 6) Definition of Ready fuer IA-Kickoff
Ein Modul darf in Integration gehen, wenn:
- [ ] Scope und Non-Scope sind dokumentiert
- [ ] Beispieldaten (3-5 Zeilen) liegen vor
- [ ] Mapping-Key ist festgelegt
- [ ] Lieferfrequenz und Qualitaetskriterien sind klar
- [ ] Owner und Plattform haben IA freigegeben

## 7) Eskalationsregel bei Scope-Creep
Wenn ein neues Thema auftaucht:
1. Ampelfarbe zuordnen (Gruen/Gelb/Rot)
2. Stage zuordnen (A/B/C)
3. Owner fuer Datenzugang benennen
4. Aufwand/Nutzen grob schaetzen
5. Entscheidung: jetzt ins Backlog oder explizit verschieben

Ohne diese 5 Punkte keine Aufnahme in Stage A.
