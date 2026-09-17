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
-->

# Mail an Thomas — LCA-Schnittstelle (2026-09)

**Versand:** nach Review Heiko  
**Anhang optional:** IA-PDF/Markdown + die zwei Sample-CSVs unter `01_spec/templates/`

---

**Betreff:** ASTRA IMC — Arbeitsteilung Plattform ↔ openLCA (Decom zuerst)

Hallo Thomas,

danke für den Austausch und die Bestätigung: **openLCA 2 + ecoinvent**. BOM-Light und Start beim **Rückbau (nicht Produktion)** passen gut zu dem, was öffentlich belastbar ist.

Damit du ein klares Bild hast, unten der Vorschlag: was die Plattform hat/macht, was bei dir in openLCA bleibt, und wie Massen, Recycling und Ergebnisse in die Datenbank kommen. Erstmal **kein Live-Kopplung** — nur ein klarer In/Out-Vertrag per CSV.

Wenn der Schnitt grob stimmt, ziehen wir als Nächstes eine Alpha-Ventus-Stückliste (wenige Zeilen) fest.

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

1. Ich schicke dir den **Park-Kontext** (Alpha Ventus).
2. Du füllst **eine Stücklisten-CSV** (Subsystem, grobes Material, Masse t, Recyclingweg, Quote, Quelle, Proxy, Stand).
3. Ich importiere sie — das ist die veröffentlichte Stückliste im Register.
4. Du rechnest in openLCA mit **genau diesen** Vordergrundzahlen.
5. Du schickst eine **Impact-CSV** (GWP, C1–C4, Methode, ecoinvent-Version) zurück. Die landet am Park neben den Simulationsläufen.

Neue Erkenntnisse = neue Version (`as_of`), kein stilles Überschreiben.

### Reihenfolge

Nur **C-Module** (Rückbau, Transport, Behandlung, Rest). Produktion (A1–A3), sobald bessere BOM da ist.

### Bitte kurz abnicken

1. Schnitt so ok?
2. Stage-A Impact: **IPCC GWP100** oder **EF 3.0 Climate change**?
3. Dataset-UUIDs schon in der Stückliste — oder erstmal nur Ergebnisse?

Spaltenköpfe (Entwurf): `01_spec/templates/thomas_bom_light_sample.csv` und `thomas_lca_impacts_sample.csv`.
