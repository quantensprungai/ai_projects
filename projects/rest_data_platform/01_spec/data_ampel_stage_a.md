<!-- Reality Block
last_update: 2026-03-19
status: draft
scope:
  summary: "Arbeitsliste Daten-Ampel fuer Vertical Slice Alpha Ventus (Stage A Fokus)."
  in_scope:
    - stage-a prioritization
    - owners and delivery format
  out_of_scope:
    - full 49-point master list
notes:
  - "Arbeitsstand fuer Teammeeting; wird danach konsolidiert."
-->

# Daten-Ampel (Stage A Fokus)

Zweck: Gemeinsame Priorisierung fuer Vertical Slice (Alpha Ventus + Emden).  
Regel: Nur Eintraege mit Owner und Lieferformat duerfen in Stage A als "Must" markiert werden.

## Arbeitsboard
| Datenpunkt | Quelle | Ampel | Stage | Prioritaet | Owner | Lieferformat | Zugang geklaert? |
|---|---|---|---|---|---|---|---|
| Windpark-Standorte + Koordinaten | 4C / MaStR / BSH | Gruen | A | Must | Heiko | CSV/SQL Import | teilweise |
| Turbinentypen + Spezifikationen | 4C | Gruen | A | Must | Heiko | CSV/SQL Import | teilweise |
| Installationsjahr / Status | 4C / MaStR | Gruen | A | Must | Heiko | CSV/SQL Import | teilweise |
| Leistung (MW) | 4C / MaStR | Gruen | A | Must | Heiko | CSV/SQL Import | teilweise |
| Decom-Zeitfenster (aggregiert) | 4C / Literatur | Gruen | A | Must | Heiko | CSV/Lookup | offen |
| Hafen-Basisdaten Emden | NPorts / oeffentliche Quellen | Gruen | A | Must | Marc/Dirk | CSV | offen |
| Seeroute Alpha Ventus <-> Emden | Literatur/Annahme | Gruen | A | Should | Marc | 1 Wert (CSV) | offen |
| Materialschaetzung (t/MW) | Literatur / interne Proxy-Tabelle | Gelb | A | Must (Proxy) | Thomas/Eike | CSV | offen |
| CO2-Faktoren Basisset | Literatur / ggf. ecoinvent | Gelb | A | Must (Proxy) | Thomas | CSV Lookup | offen |
| LCA-Proxy (Stahl/Kabel) | Vestas/Literatur | Gelb | A | Should | Thomas | CSV | offen |
| Wetter ERA5 Monatsmittel | Copernicus ERA5 | Gruen | A | Should | Heiko | CSV/aggregiert | offen |
| Natura2000 Layer | EEA/GeoJSON | Gruen | A | Later | Eike/Marc | GeoJSON | offen |
| AIS-Echtzeit-Tracking | MarineTraffic o. a. API | Rot | C | Later | tbd | API | nein |
| OEM-BOM Detaildaten | OEM / Betreiber | Rot | C | Later | Projektleitung | NDA/CSV | nein |
| As-built / Betriebsdaten | Betreiber | Rot | C | Later | Projektleitung | NDA/API | nein |

## Entscheidungslogik im Meeting
- **Must:** Ohne diesen Datenpunkt keine glaubwuerdige Demo.
- **Should:** Wertvoll, aber nicht kritisch fuer Foundation MVP.
- **Later:** bewusst nicht Stage A.

## Offene Punkte fuer Entscheidung
- Welche 8-10 Datenpunkte sind final "Must" fuer Stage A?
- Welche 2-3 Gelb-Datenpunkte werden als Proxy akzeptiert?
- Wer klaert 4C-Lizenzbedingungen und Persistenzrechte bis wann?
