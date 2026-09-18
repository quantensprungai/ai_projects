<!-- Reality Block
last_update: 2026-09-18
status: draft
scope:
  summary: "Stufe-0 Inventar Alpha Ventus: 4C Specs, VPI Measurements, MaStR AV01."
  in_scope:
    - filled vs empty fields for two AV turbine types
    - MaStR EinheitWind keys on AV01
  out_of_scope:
    - schema / ETL
    - inventing unit-to-type mapping
notes:
  - "Excel: academiccloudsync Reference_Data; MaStR EinheitenWind.xml UTF-16."
-->

# AV Stufe-0 — Specs / Measurements / MaStR

Quelle: 4C Turbine-DB + VPI + MaStR-XML (lokal). **Kein Schema.**

## 4C Typ am Park (`Turbine on Windfarms`, WindfarmId DE01)

| TurbineId | OEM | Modell | MW min/max | n min/max | Foundation | Expired |
|-----------|-----|--------|------------|-----------|------------|---------|
| 35 | Senvion GmbH | 5M (Senvion) | /5 | /12 | Grounded: Various | No |
| 2 | Siemens Gamesa Renewable Energy | M5000-116 (Areva Wind) | /5 | /12 | Grounded: Various | No |

Zeilen DE01: **2**. 4C liefert **keine WEA-IDs** und **kein n=6+6** — nur zwei Typ-Zeilen am Park.

### 4C Specs (`Offshore Wind Turbine Specs`)

| Feld | tid 35 | tid 2 |
|------|---|---|
| `TurbineId` | 35 | 2 |
| `TurbineName` | 5M | M5000-116 |
| `Manufacturer` | Senvion | Areva Wind |
| `CommerciallyAvailable` | Discontinued                                       | No Longer Commercially Available                   |
| `ExpectedYearCommercialisation` | — | — |
| `RatedPowerMW` | 5.075 | 5 |
| `CutInWindSpeedmps` | 3.5 | 4 |
| `RatedWindSpeedmps` | 14 | 12.5 |
| `CutOutWindSpeedmps` | 30 | 25 |
| `WindClass` | IEC IB, Repower S-Classes | IEC 1B/0 GL-TK 1 offshore |
| `RotorDiameterm` | 126 | 116 |
| `SweptAream2` | 12469 | 10568 |
| `PowerDensitym2pkW` | 2.49 | 2.11 |
| `RotorSpeedrpm` | 12.1 | 14.8 |
| `RotorOperationalIntervalrpm` | 7.7-12.1 | 4.5-14.8 |
| `RotorWeightt` | 130 | 112 |
| `PowerRegulation` | Electrical blade angle adjustment-pitch and speed control | Electrical single pitch |
| `GeneratorType` | Double-fed asynchronous generator, 6 pole | Synchronous, permanent magnet |
| `GeneratorPowerkWpUnit` | 5075 | 5260 |
| `GeneratorUnits` | 1 | 1 |
| `GeneratorSpeedrpm` | 750-1170 | 45.1-148.5 |
| `VoltageV` | 660 | 3300 |
| `FrequencyHz` | 50/60 | 50 |
| `Converter` | Pulse-modulated IGBTs | ABB PCS 6000. 4-quadrant-converter |
| `GearboxType` | Two helical planetary stage and one spur gear stage | Step-planetary gear, helical |
| `GearboxRatio` | 1:97 | 1:10 |
| `BladesNumber` | 3 | 3 |
| `BladesLengthm` | 62.5 | 56 |
| `BladesMaterial` | GFRP shell construction, pre-bent | Carbon fiber reinforced plastics |
| `BladesType` | LM 61.5 | — |
| `BladesWeightt` | 24 | 16.5 |
| `TowerType` | Steel tubular/cylindrical tower | Tubular/conical steel tower |
| `TowerHeightm` | 85/95 | 90 |
| `TowerWeightt` | Site-specific | 350 |
| `NacelleHeightm` | 6 | — |
| `NacelleLengthm` | 18 | — |
| `NacelleWidthm` | 6 | — |
| `NacelleWeightt` | 325 | 233 |
| `Insurance` | — | — |
| `SellingPoints` | Proven technology in a new dimension. Powerful, economical, reliable. Modular st | The turbine was designed so that it has minimum number of assembly operations re |
| `Comments` | The 5M turbine was taken out fo the manufacturing portfolio when the 6M was rele | The wind turbine M5000 was manufactured in Bremerhaven. 250 AREVA M5000 turbines |
| `WindfarmSEOurl` |  ormonde-united-kingdom-uk17.html, beatrice-demonstration-united-kingdom-uk46.ht |  alpha-ventus-germany-de01.html, global-tech-i-germany-de09.html, trianel-windpa |
| `SEOurl` | turbine-senvion-5m-tid35.html | turbine-areva-wind-m5000-116-tid2.html |
| `WindfarmIds` |  UK17, UK46 |  DE01, DE09, DE27 |

**Schon in `imc_turbine_models`:** Manufacturer, TurbineName, RatedPowerMW, RotorDiameterm, TowerHeightm (Nabe, oft leer).

**Gewicht/BOM-relevant in Specs:**

| Feld | tid 35 | tid 2 |
|------|---|---|
| `RotorWeightt` | 130 | 112 |
| `BladesNumber` | 3 | 3 |
| `BladesLengthm` | 62.5 | 56 |
| `BladesMaterial` | GFRP shell construction, pre-bent | Carbon fiber reinforced plastics |
| `BladesType` | LM 61.5 | — |
| `BladesWeightt` | 24 | 16.5 |
| `TowerType` | Steel tubular/cylindrical tower | Tubular/conical steel tower |
| `TowerHeightm` | 85/95 | 90 |
| `TowerWeightt` | Site-specific | 350 |
| `NacelleHeightm` | 6 | — |
| `NacelleLengthm` | 18 | — |
| `NacelleWidthm` | 6 | — |
| `NacelleWeightt` | 325 | 233 |
| `GearboxType` | Two helical planetary stage and one spur gear stage | Step-planetary gear, helical |
| `GeneratorType` | Double-fed asynchronous generator, 6 pole | Synchronous, permanent magnet |

### VPI `Turbine Measurements`

| Feld | tid 35 | tid 2 |
|------|---|---|
| `TurbineId` | 35 | 2 |
| `RatedPowerMW` | 5.075 | 5 |
| `RotorDiameterm` | 126 | 116 |
| `RotorWeightt` | 130 | 112 |
| `BladesNumber` | 3 | 3 |
| `BladesLengthm` | 62.5 | 56 |
| `BladesType` | LM 61.5 | — |
| `BladesWeightt` | 24 | 16.5 |
| `TowerType` | Steel tubular/cylindrical tower | Tubular/conical steel tower |
| `TowerHeightm` | 85/95 | 90 |
| `TowerWeightt` | Site-specific | 350 |
| `NacelleHeightm` | 6 | — |
| `NacelleLengthm` | 18 | — |
| `NacelleWidthm` | 6 | — |
| `NacelleWeightt` | 325 | 233 |

## VPI Fixed Foundation (WindfarmId DE01)

2 Zeile(n). Erste Keys/Werte (non-null):

| Feld | Wert |
|------|------|
| `FoundationId` | 484 |
| `Foundation` | Grounded: Various |
| `WindfarmId` | DE01 |
| `Name` | Alpha Ventus |
| `WindfarmStatus` | Fully Commissioned |
| `ParkConstructionStarts` | 25 Jun 2008 |
| `DevDepthMinM` | 27 |
| `DevDepthMaxM` | 27 |
| `FoundationType` | Tripod |
| `MainFoundationQty` | 6 |
| `FoundationWeightAvgTons` | 700 |
| `FoundationWeightPlotTons` | 700 |
| `FoundationLengthAvgM` | 45 |
| `FoundationLengthPlotM` | 45 |
| `OtherLengthMinM` | 35 |
| `OtherLengthMaxM` | 45 |
| `TurbineModelAndOEM` | M5000-116 (Areva Wind), Also using 6x 5M(Senvion) turbines |
| `TurbineMWMax` | 5 |
| `OEM` | Areva Wind |
| `Model` | M5000-116 |
| `TurbineOthers` | Also using 6x 5M(Senvion) turbines |

| Feld | Wert |
|------|------|
| `FoundationId` | 136 |
| `Foundation` | Grounded: Various |
| `WindfarmId` | DE01 |
| `Name` | Alpha Ventus |
| `WindfarmStatus` | Fully Commissioned |
| `ParkConstructionStarts` | 25 Jun 2008 |
| `DevDepthMinM` | 27 |
| `DevDepthMaxM` | 27 |
| `FoundationType` | Jacket (Piled) |
| `MainFoundationQty` | 6 |
| `FoundationWeightAvgTons` | 500 |
| `FoundationWeightPlotTons` | 500 |
| `FoundationLengthAvgM` | 56 |
| `FoundationLengthPlotM` | 56 |
| `FoundationFootMaxM` | 20 |
| `FoundationFootPlotM` | 20 |
| `OtherLengthMinM` | 20 |
| `OtherLengthMaxM` | 40 |
| `OtherFootMaxM` | 1.8 |
| `TurbineModelAndOEM` | M5000-116 (Areva Wind), Also using 6x 5M(Senvion) turbines |
| `TurbineMWMax` | 5 |
| `OEM` | Areva Wind |
| `Model` | M5000-116 |
| `TurbineOthers` | Also using 6x 5M(Senvion) turbines |


## MaStR EinheitWind — AV01

Gesucht: `SEE982527987333`. AV-Einheiten im Scan: **12**.

Katalog-IDs wo auflösbar als `*_label` ergänzt (nur Anzeige hier).

| Feld | Roh | Katalog | In `imc_turbines` heute |
|------|-----|---------|-------------------------|
| `AnlagenbetreiberMastrNummer` | ABR963930749794 | — | — |
| `AuflageAbschaltungLeistungsbegrenzung` | 0 | — | — |
| `Breitengrad` | 54.021660 | — | location |
| `Bruttoleistung` | 5000.000 | — | rated_power_mw (kW→MW) |
| `Bundesland` | 1416 | Ausschließliche Wirtschaftszone | — |
| `DatumLetzteAktualisierung` | 2026-03-30T14:56:11.6879787 | — | — |
| `EegMaStRNummer` | EEG917894430182 | — | — |
| `EinheitBetriebsstatus` | 35 | In Betrieb | status_label (via Katalog) |
| `EinheitMastrNummer` | SEE982527987333 | — | ext_unit_key |
| `EinheitSystemstatus` | 472 | Aktiviert | — |
| `Einspeisungsart` | 688 | Volleinspeisung | — |
| `Energietraeger` | 2497 | Wind | — |
| `FernsteuerbarkeitDv` | 1 | *(Katalog global nicht eindeutig — 0/1 ignorieren)* | — |
| `FernsteuerbarkeitNb` | 1 | *(Katalog global nicht eindeutig — 0/1 ignorieren)* | — |
| `GebietNachDemFlaechenentwicklungsplanNordsee` | 1547 | N-2 | — |
| `GenMastrNummer` | SGE909902927777 | — | — |
| `HausnummerNichtGefunden` | 0 | — | — |
| `Hausnummer_nv` | 0 | — | — |
| `Hersteller` | 2888 | REpower Systems SE | — |
| `Inbetriebnahmedatum` | 2010-04-08 | — | commissioning_date |
| `Kraftwerksnummer_nv` | 0 | — | — |
| `Kuestenentfernung` | 30.100 | — | — |
| `Laengengrad` | 6.593498 | — | location |
| `Land` | 84 | Deutschland | — |
| `LokationMaStRNummer` | SEL947778987563 | — | — |
| `Nabenhoehe` | 91.900 | — | — |
| `Nachtkennzeichnung` | 1 | *(Katalog global nicht eindeutig — 0/1 ignorieren)* | — |
| `NameStromerzeugungseinheit` | AV01 | — | name |
| `NameWindpark` | alpha ventus | — | — |
| `Nettonennleistung` | 5000.000 | — | — |
| `NetzbetreiberpruefungDatum` | 2025-08-18 | — | — |
| `NetzbetreiberpruefungStatus` | 2954 | Geprüft | — |
| `NichtVorhandenInMigriertenEinheiten` | 0 | — | — |
| `Registrierungsdatum` | 2020-12-23 | — | — |
| `Rotorblattenteisungssystem` | 0 | — | — |
| `Rotordurchmesser` | 126.000 | — | — |
| `Seelage` | 640 | Nordsee | — |
| `StrasseNichtGefunden` | 0 | — | — |
| `Technologie` | 691 | Horizontalläufer | — |
| `Typenbezeichnung` | REpower5M | — | — |
| `Wassertiefe` | 29.300 | — | — |
| `Weic` | 11WD2OAV-000350Z | — | — |
| `WeicDisplayName` | OWP-ALPHAVENTUS | — | — |
| `Weic_nv` | 0 | — | — |
| `WindAnLandOderAufSee` | 889 | Windkraft auf See | — |

Zusätzliche gefüllte Keys (nicht im Transform): `AnlagenbetreiberMastrNummer`, `AuflageAbschaltungLeistungsbegrenzung`, `Bundesland`, `DatumLetzteAktualisierung`, `EegMaStRNummer`, `EinheitSystemstatus`, `Einspeisungsart`, `Energietraeger`, `FernsteuerbarkeitDv`, `FernsteuerbarkeitNb`, `GebietNachDemFlaechenentwicklungsplanNordsee`, `GenMastrNummer`, `HausnummerNichtGefunden`, `Hausnummer_nv`, `Hersteller`, `Kraftwerksnummer_nv`, `Kuestenentfernung`, `Land`, `LokationMaStRNummer`, `Nabenhoehe`, `Nachtkennzeichnung`, `NameWindpark`, `Nettonennleistung`, `NetzbetreiberpruefungDatum`, `NetzbetreiberpruefungStatus`, `NichtVorhandenInMigriertenEinheiten`, `Registrierungsdatum`, `Rotorblattenteisungssystem`, `Rotordurchmesser`, `Seelage`, `StrasseNichtGefunden`, `Technologie`, `Typenbezeichnung`, `Wassertiefe`, `Weic`, `WeicDisplayName`, `Weic_nv`, `WindAnLandOderAufSee`.

### Hersteller / Typ / Nabe / Rotor über die 12 AV-Einheiten

| Name | SEE | Hersteller | Typ | Nabe m | Rotor m | Brutto kW |
|------|-----|------------|-----|--------|---------|-----------|
| AV01 | SEE982527987333 | REpower Systems SE | REpower5M | 91.900 | 126.000 | 5000.000 |
| AV02 | SEE969857558105 | REpower Systems SE | REpower5M | 91.500 | 126.000 | 5000.000 |
| AV03 | SEE951984161846 | REpower Systems SE | REpower 5M | 92.000 | 126.000 | 5000.000 |
| AV04 | SEE908234374938 | REpower Systems SE | REpower 5M | 91.400 | 126.000 | 5000.000 |
| AV05 | SEE909821745483 | REpower Systems SE | REpower 5M | 91.600 | 126.000 | 5000.000 |
| AV06 | SEE981139983375 | REpower Systems SE | REpower 5M | 91.600 | 126.000 | 5000.000 |
| AV07 | SEE964572095980 | AREVA GmbH | Areva Wind M5000 | 91.000 | 116.000 | 5000.000 |
| AV08 | SEE956940278347 | AREVA GmbH | Areva Wind M5000 | 90.000 | 116.000 | 5000.000 |
| AV09 | SEE998641256224 | AREVA GmbH | Areva Wind M5000 | 90.000 | 116.000 | 5000.000 |
| AV10 | SEE926100574534 | AREVA GmbH | Areva Wind M5000 | 91.500 | 116.000 | 5000.000 |
| AV11 | SEE934107523776 | AREVA GmbH | Areva Wind M5000 | 91.500 | 116.000 | 5000.000 |
| AV12 | SEE919842961458 | AREVA GmbH | Areva Wind M5000 | 91.000 | 116.000 | 5000.000 |

## Bewertung

Abbruchkriterium **nicht** gegriffen: 4C-Gewichte sind für **beide** AV-Typen gefüllt. VPI `Turbine Measurements` ist für tid 35/2 **identisch** mit Specs (kein zweiter Messwert) — Specs als Primärquelle, Measurements nur Lückenfüller.

4C `Turbine on Windfarms` zählt **12+12** (beide Zeilen `NoTurbinesMax=12`) und bleibt ohne WEA-ID. Der **6+6-Split** steht woanders:

- MaStR: AV01–AV06 `REpower5M` / Rotor 126 m; AV07–AV12 `Areva Wind M5000` / Rotor 116 m.
- VPI Foundation: zwei Zeilen à `MainFoundationQty=6` (Tripod 700 t vs Jacket 500 t) plus Text `Also using 6x 5M(Senvion)`.

Das ist **kein Raten** — der Typ klebt an der MaStR-Einheit, wir haben ihn nur nicht transformiert. OEM-Namen weichen ab (MaStR REpower vs 4C Senvion; Farm-Link OEM für tid 2 fälschlich Siemens Gamesa, Spec sagt Areva Wind). Match über Rotor-Ø + Alias, nicht über den 4C-Link-OEM.

`Katalogwerte.Id` ist nicht global eindeutig — 0/1-Flags nicht über den flachen Lookup auflösen.

## Empfehlung Stufe 1–2

1. **Modell:** Specs-Felder (Gewichte, Blatt, Getriebe, Generator, Cut-in/out) an `imc_turbine_models` — nullable / `specs jsonb`. Quelle 4C, `is_proxy` für Massen. Measurements nicht separat speichern, solange sie Specs duplizieren.
2. **Einheit:** MaStR `Hersteller`, `Typenbezeichnung`, `Nabenhoehe`, `Rotordurchmesser`, `Wassertiefe`, `Kuestenentfernung`, `Seelage`, `EegMaStRNummer` auf `imc_turbines`. Katalog-Labels nur für echte Katalogfelder (Hersteller, Status, Seelage, …).
3. **Join:** `turbine_model_id` setzen wo MaStR-Rotor (126 vs 116) bzw. Typname eindeutig auf ein 4C-Modell am Park zeigt. AV damit 6+6, ohne 4C-WEA-IDs.
4. **Thomas:** `av_units.csv` darf Typ aus MaStR tragen. 4C-Massen bleiben Proxy am Typ, nicht SoT. Fundamente: VPI 700/500 t je 6 Stück — eigener Block, nicht in die Turbinen-BOM mischen.
5. **Nicht jetzt:** Foundation-Messtabelle voll normalisieren; GIS-Punkte; 0/1-MaStR-Flags.

