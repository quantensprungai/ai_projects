<!-- Reality Block
last_update: 2026-09-17
status: draft
scope:
  summary: "Mail-Vorlage an Thomas nach Gespräch openLCA/BOM-Light/Decom-first. Keine persönlichen Kontaktdaten."
  in_scope:
    - email body
    - mini-proposal in/out
  out_of_scope:
    - sending
    - personal emails / phone numbers
notes:
  - "IA: 01_spec/interface_agreement_thomas_lca_v0.md"
  - "2026-09-17 Thomas: BAFU statt ecoinvent; EF 3.1 + optional ReCiPe; mehrere Kategorien."
-->

# Mail an Thomas — LCA-Schnittstelle (2026-09)

**Versand:** erste Mail raus. Unten Kurzantwort auf seine BAFU-/Methoden-Mail.  
**Neu mitschicken nur wenn er die Impact-Vorlage noch nicht befüllt:** `lca_impacts_sample.csv` + `feldkatalog.csv`. Park/Einheiten/BOM unverändert.

---

## Kurzantwort (nach seiner BAFU-Mail)

**Betreff:** ASTRA IMC — BAFU + EF 3.1 / ReCiPe, passt so

Hallo Thomas,

danke — das ziehen wir so nach:

- Hintergrund-DB bei dir: **BAFU** (nicht ecoinvent). Wir spiegeln den Katalog weiterhin nicht.
- Methoden: **EF 3.1**, optional zusätzlich **ReCiPe 2016**.
- Ergebnisse: **alle Kategorien der Methode** je C1–C4 (nicht nur GWP). Eine CSV-Zeile = Methode × Kategorie × C-Modul. Namen und Einheiten bitte **wie openLCA exportiert**.
- AAS-Carbon-Footprint später nur GWP; Tox-Kategorien bleiben in unserer DB.

Wenn du magst, hängt die aktualisierte leere Impact-Tabelle plus Feldkatalog an (gleiche Köpfe, mehr Beispielzeilen). Stückliste und Park-Kontext bleiben.

Eine Bitte: für `lci_db` den **genauen BAFU-Datensatz plus Jahr/Version**.

Nachtrag Register: die 12 Einheiten haben jetzt den **MaStR-Typ** (AV01–06 REpower/Senvion 5M, AV07–12 Areva M5000). Areva-Linie heute **Siemens Gamesa** (Adwen); Nameplate bleibt Areva. Massen in der Stückliste weiter von dir — 4C-Gewichte nur als Vergleich.

Viele Grüße  
Heiko

---

**Betreff:** ASTRA IMC — Arbeitsteilung Plattform ↔ openLCA (Decom zuerst)

Hallo Thomas,

danke für den Austausch und die Bestätigung: **openLCA 2 + ecoinvent**. BOM-Light und Start beim **Rückbau (nicht Produktion)** passen gut zu dem, was öffentlich belastbar ist.

Damit du ein klares Bild hast, unten der Vorschlag: was die Plattform hat/macht, was bei dir in openLCA bleibt, und wie Massen, Recycling und Ergebnisse in die Datenbank kommen. Erstmal **kein Live-Kopplung** — nur ein klarer In/Out-Vertrag per CSV.

Wenn der Schnitt grob stimmt, füllst du die Stückliste für die zwei Turbinentypen (Senvion 5M / Areva M5000-116). Die 12 Einheiten sind nur Inventar-Anker (Name, MaStR, Inbetriebnahme) — ohne Massen und ohne Typ-Zuordnung je Einheit, die haben wir nicht.

Der **Feldkatalog** (Anhang 5) ist die Legende dazu: welches Feld Pflicht ist, welches Format, welches Beispiel — zum Nachschlagen, nicht zum Ausfüllen.

Viele Grüße  
Heiko

---

## Mini-Vorschlag

**Idee:** Wir spiegeln **nicht** ecoinvent in unserer Datenbank (kein „welcher Stahl genau“, kein Fahrzeugjahr). Das bleibt in openLCA. Du recherchierst **Massen und Recycling**; die landen versioniert bei uns. openLCA rechnet; zurück kommen die **Impacts**.

```
Plattform (IMC)                         openLCA (du)
----------------                        -----------------
Park, Turbinen, Foundation,        -->  Product System (Vordergrund)
Decom-Jahr, optional Dauer/Distanz

Stückliste: grobe Massen +         <--  deine Recherche (Excel/CSV)
Recyclingweg/-quote                     = SoT in unserer DB nach Import

dieselben Massen als Vordergrund   -->  Dataset-Wahl (Stahl, Lkw, …)
                                        in ecoinvent

GWP je C1–C4 + Methode +           <--  Berechnung
ecoinvent-Version
```

| | Plattform (ich) | openLCA (du) |
|---|---|---|
| **Hat** | Asset-Register, MaStR-Einheiten, Decom-Jahr, Hafen/Distanz | ecoinvent, Product Systems, LCIA-Methoden |
| **Macht** | Kontext exportieren; Stückliste + Impacts speichern/zeigen | Massen/Recycling recherchieren; Datasets wählen; rechnen |
| **Macht nicht** | Stahlgüten/Lkw-Jahre nachbauen; LCA in der App rechnen; Massen erfinden | ecoinvent-Katalog an uns dump-en |

### Wie Massen und Recycling in die DB kommen

Nicht aus openLCA-Hintergrund exportieren und nicht in der UI tippen.

**Von mir zu dir (In):** Park-Kontext plus die 12 MaStR-Einheiten (Name, Nummer, MW, Inbetriebnahme, Status, **Typ/Nabe/Rotor aus MaStR**). Massen leer. AV01–06 Senvion/REpower 5M, AV07–12 Areva M5000-116 (Linie heute Siemens Gamesa). Decom-Jahr 2030 ist nur Schätzung (Inbetriebnahme + 20 Jahre); 4C-Event nennt 2027/2028. Hafen Emden ist von uns kuratiert, Distanz 82.4 km.

**Von dir zu mir (Out):** grobes Material, Masse, Recycling — in die Stückliste **je Turbinentyp** (nicht 12-mal kopieren, solange die Massen gleich sind). Danach Impacts (GWP je C1–C4).

Die Buchstaben C1–C4 sind EN-15804-Lebenszyklusmodule (Rückbau / Transport / Behandlung / Rest). Dieselbe Gliederung kann später ins AAS-Submodel **Carbon Footprint (IDTA 02023)** als LifeCyclePhases. Welche CO2-Methode (IPCC GWP100 oder EF 3.0) ist unabhängig davon — bitte in openLCA festlegen.

Ablauf:

1. Anhang 1 = Park-Kontext, Anhang 2 = 12 Einheiten. Anhang 5 = welche Felder Pflicht sind.
2. Du füllst Anhang 3 (Stückliste je Typ).
3. Ich importiere sie ins Register.
4. Du rechnest in openLCA mit diesen Vordergrundzahlen.
5. Du füllst Anhang 4 (Impacts) und schickst zurück.

Neue Erkenntnisse = neue Version (`as_of`), kein stilles Überschreiben.

### Reihenfolge

Nur **C-Module** (Rückbau, Transport, Behandlung, Rest). Produktion (A1–A3), sobald bessere BOM da ist.

### Bitte kurz abnicken

1. Schnitt so ok?
2. Klimamethode in openLCA: **IPCC GWP100** oder **EF 3.0 Climate change**? (nur die Rechenvorschrift für kg CO2-eq; C1–C4 bleiben die Phasen)
3. Dataset-UUIDs schon in der Stückliste — oder erstmal nur Ergebnisse?

Anhang: Park-Kontext + 12 Einheiten (ohne Massen) + leere Stückliste je Typ + leere Impact-Tabelle + Feldkatalog.
