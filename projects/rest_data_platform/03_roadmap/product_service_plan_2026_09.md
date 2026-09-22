<!-- Reality Block
last_update: 2026-09-22
status: active
scope:
  summary: "Produkt- und Serviceplan — fünf Dienste. Literatur-Position gebaut (Stück und Anteil, Stahl-Szenario BDSV 08/2026). Kupfer, Blei, Rückstellung und Pass-GWP offen."
  in_scope:
    - five services
    - reference position grain
    - piece vs allocated share
    - horizons and dependencies
  out_of_scope:
    - schema migration
    - loading the study into Alpha Ventus
    - republishing the study inventory tables
    - rewriting mvp.md or scope.md
notes:
  - "Begründung: vier Canvas-Übersichten 2026-09-22 (greenfield, data-gaps, scenario-layer, reference-plant)."
  - "2026-09-22: Position und Stahl-Szenario gebaut. Modell ist eine datierte Annahme je Stoff. Kupfer, Blei, Szenario-Editor und Niedrig/Basis/Hoch stehen aus."
  - "66 Anlagen = 990 MW / 15 MW in der öffentlichen Vestas-Studie, nicht das Register."
  - "BOM-Schnitt Anlage × Stoffklasse liegt zwischen BOM-light und BOM-full."
-->

# Produkt- und Serviceplan (2026-09-22)

Die Akte trägt Identität, Menge, Herkunft und Lücke. Dienste sind Sichten darauf. Preise, Entgelte und Zins sind ein Szenario mit Datum und Quelle. Der Pass liest. Er schreibt nicht.

`mvp.md` und `scope.md` beschreiben den Register-Prototyp. Dieses Dokument beschreibt die fünf Dienste. Die Literatur-Position ist die erste gebaute Schicht davon: Stück und Anteil, Materialkonto, Restwert für Stahl. Kupfer, Blei und die Rückstellung stehen noch aus.

## Stand

| Größe | Wert | Bedeutung |
|-------|------|-----------|
| Parks im Register | 3.606 | weltweit, Industry-Quelle |
| DE aktiv | 76 | Lifecycle nicht cancelled, von 181 DE-Parks |
| Einheiten | 1.651 auf 33 Parks | Behördenregister, nur freigegebene Namensmatches |
| Wellen | Jahr, Proxy, Lückenliste | Fehlendes zählt nicht als Null |
| Partnerdateien | leer | Stückliste, Impacts, Simulationslauf |
| Literaturposition | 1 Fall, 66 Anlagen, 990 MW | nicht im Parkregister. Stahl 287 €/t, BDSV Sorte 3, Stand 2026-08-20. Kupfer und Blei ohne Preis |

Preise im Register sind modellierte und gemeldete Anlagenkosten. Stahl, Kupfer, Sprit und Schrott der Literaturposition sitzen in `imc_material_assumptions`, nicht in den 4C-Anlagenkosten.

## Drei Schnitte der Stückliste

| Schnitt | Körnung | Wofür |
|---------|---------|--------|
| BOM-light | Gondel, Blatt, Turm, Fundament × grober Stoff × Entsorgungsweg | Vordergrund für die Ökobilanz. Feldkatalog Thomas. |
| Anlage × Stoffklasse | Turbine, Fundament, Parkkabel, Exportkabel, See- und Landstation × Stahl, Kupfer, Blei, Beton, SF6, Magnete | Materialkonto, Restwert, Verwerter. Dieser Plan. |
| BOM-full | Teil, Güte, Serie, Verschnitt, Ersatzteil | Fertigung. Liegt außerhalb. |

Dieselbe Tabelle kann beide ersten Schnitte halten. Die Zeile trägt Herkunft, Proxy und die Tiefe des Bauteils. Literatur und Partnerlieferung bleiben unterscheidbar.

## Fünf Dienste

| Dienst | Nutzer | Sieht | Braucht zusätzlich |
|--------|--------|-------|--------------------|
| Materialkonto | Forschung, Betreiber, Pass | Tonne je Stoff und Bauteil | die Zeilen, zwei Sichten |
| Restwert | Betreiber, Region | Schrottgutschrift minus Entsorgung | Preis oder Entgelt, Datum, Weg |
| Rückstellung | Betreiber, als Vorlage | Rückbaukosten minus Restwert, abgezinst | Kostenannahme, Zins. Die Buchung bleibt beim Betreiber |
| Hafen und Verwerter | Hafen, Recycler | physisches Stück und Stoffstrom | Kapazität, Fläche, Weg |
| Pass | Interop | Identität, Massen, später nur GWP | Impacts. Tonnen ergeben kein CO₂ |

## Referenzposition

Öffentliche Vestas-LCA der Klasse V236-15 MW, as-built, ohne Ersatzteile und ohne Produktionsabfall. Der Studienpark hat 990 MW. 990 / 15 = **66 Anlagen**. Dieselbe Stückzahl steht in der Studie: 66 Turbinen, 66 Fundamente, 66 Parkkabelstücke, 4 Exportkabel, 2 Seestationen, 1 Landstation.

Das ist nicht Alpha Ventus (12 Anlagen) und nicht die 33 Parks mit Einheiten.

Abgeleitete Größen, gerundet, Quelle die Studie. Die Inventartabellen werden hier nicht abgeschrieben.

| Stück | Physisch | Je Position |
|-------|----------|-------------|
| Turbine | 66 × etwa 1.622 t | Stahl etwa 1.340 t, Verbund etwa 145 t, Kupfer etwa 16 t, Magnete unter 1 t, SF6 etwa 48 kg |
| Fundament | 66 × etwa 1.622 t | fast nur Stahl |
| Parkverkabelung | 66 × etwa 67 t | Blei im Kabel |
| Exportkabel | 4 × etwa 8.320 t | Anteil 1/66, nicht ein Stück. Kupfer- und Bleianteile dominieren die Position |
| Stationen | 2 See, 1 Land | Beton etwa 12.000 t sitzt an Land |

Kupfer in der Maschine etwa 16 t. Mit Kabel- und Stationsanteil etwa 164 t je Position. Blei etwa 128 t je Position, fast nur in den Kabeln.

Milligramm je Kilowattstunde aus derselben Studie brauchen Ertrag und Lebensdauer. Sie gehören nicht ins Materialkonto.

## Zwei Sichten

Verbindlich, bevor ein Schema entsteht.

| Sicht | Bedeutung | Wer sie nutzt |
|-------|-----------|----------------|
| `piece` | transportierbares Stück | Hafen, Verwerter, Kran |
| `allocated_share` | rechnerischer Anteil 1/66 an Kabel und Station | Materialkonto, Restwert |

Ein Sechsundsechzigstel Exportkabel ist kein Stück, das ein Kai annimmt. Das Exportkabel bleibt ein Stück von etwa 8.320 t.

## Kabel und Konverter

Für die Literatur-Position liefert die Studie die Massen. Ein Nachziehen der Transmission-Tabelle ist dafür nicht nötig. Die Referenzakte bekommt eigene Zeilen, Herkunft Literatur.

Für echte Parks gilt etwas anderes. Netz und Plattformen sind Steckbriefe, keine Tonnen Kupfer, Blei oder Beton. Ein Transmission-Import würde Anlagen und Leitungen ergänzen, nicht diese Stoffmassen. Ohne Massen bleiben Restwert und Verwerter auf echten Parks eine Lücke.

## Abhängigkeiten

| Fehlt | Folge |
|-------|--------|
| Kabel und Stationen | Restwert und Verwerter zählen nur die Maschine und liegen beim Kupfer und Blei falsch |
| Entsorgungsweg | Stahl ist `recycle`. Die übrigen Stoffe haben keinen Weg, deshalb keinen Erlös. Die Studie nennt den Weg nicht |
| Preis oder Entgelt | Stahl gesetzt (BDSV). Kupfer und Blei fehlen. Die Rückstellung hat noch keine Kostenannahme und keinen Zins |
| Impacts | Pass ohne Klimazahl. Die Preisrechnung läuft |
| Ertrag und Lebensdauer | kein Vergleich je kWh. Tonnen bleiben gültig |
| Anteil an die Logistik gegeben | der Hafen rechnet ein Kabel, das es so nicht gibt |

## Horizonte

| Horizont | Gültig | Gebaut |
|----------|--------|--------|
| Jetzt | Register, Wellen, eine Literatur-Position | Stück und Anteil, Stahl-Szenario BDSV 08/2026. Nichts aus der Studie an Alpha Ventus |
| Nächste Schicht | eine weitere datierte Preisannahme | Kupfer mit belegtem Schrottabschlag, in €/t. Blei danach. Bänder und eine editierbare Szenariofläche, wenn diese Annahmen dieselbe Form haben |
| Später | Hafenlimits, Verwerterkapazität | Engpassjahr. Pass, wenn Impacts da sind |

## Technik, beschrieben und angebunden

Form wie `01_spec/templates/feldkatalog.csv`: Bauteil, Stoff, Tonne, Quelle, Proxy, Stand. Bauteile um Parkverkabelung, Exportkabel, See- und Landstation erweitern. Jede Zeile trägt `piece` oder `allocated_share`.

**Umgesetzt (2026-09-22):** Migration `apps/web/supabase/migrations/20260922120000_imc_material_reference.sql` — `imc_reference_cases`, `imc_material_lines`, `imc_material_assumptions`. Dualer Anker: genau eines von `case_id` oder `farm_id`. Oberfläche: `/home/[account]/assets/reference`. Kein Eintrag in `imc_wind_farms`.

**Stahl-Szenario (2026-09-22):** `20260922160000_imc_steel_scrap_scenario.sql`. Eine Annahme: BDSV-Durchschnitt Deutschland 08/2026, Sorte 3 (schwerer Stahlaltschrott, mindestens 6 mm), 287,0 €/t, Ab-Station, Stand 2026-08-20. Nur Stahlzeilen haben `eol_route = recycle`. Die Anteilsicht rechnet daraus die Gutschrift. Kupfer, Blei, Entsorgungsentgelte und die Rückstellung bleiben Lücken. Ein Editor für Preise und die Bänder Niedrig/Basis/Hoch sind nicht gebaut.

## Literatur

Sortierung der sieben Papers: `Inhalt Literatur.docx` im LCA-Literature-Ordner. PDFs nicht ins Register.

SeeOff-Handbuch: Checkliste Hafen, Schiff, Sequenz. PCF Guidance: was der Pass an CO₂ berichten soll. Seidel-Massen zur 5-MW-Anlage prüft die Ökobilanz. Sie werden nicht in die Pilot-Oberfläche geschrieben.

## Präsentation

Außen-Deck: eine Folie „Vorhaben“ mit den fünf Diensten, ohne Tonnen und ohne den Studien-Anlagennamen. Team-Deck und Whitepaper bleiben wie sie sind.
