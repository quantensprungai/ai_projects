<!-- Reality Block
last_update: 2026-09-17
status: active
scope:
  summary: "Was an Thomas geht vs. intern. Feldkatalog ist die mitreisende Erklaerung zu §5/§6."
  in_scope:
    - which files travel
    - pointer to feldkatalog.csv
  out_of_scope:
    - ecoinvent catalog
    - invented masses
-->

# CSV-Paket Thomas (Stage A)

Die **Fuell-CSVs** bleiben Daten (Kopf + Zeilen). Pflicht, Typ, Beispiel stehen **nicht** in denselben Dateien — sonst landet die Anleitung im Import.

Mitreisende Erklaerung: [`feldkatalog.csv`](feldkatalog.csv) (Excel, Semikolon). Intern spiegeln IA §5/§6 dasselbe.

| Datei | Rolle | Thomas |
|-------|-------|--------|
| `av_park_context_v1.csv` | In | lesen |
| `av_units.csv` | In | lesen |
| `bom_light_sample.csv` | Out | fuellen je Typ |
| `lca_impacts_sample.csv` | Out | fuellen nach Rechnung |
| `feldkatalog.csv` | Anleitung | lesen, nicht importieren |

Alte `av_park_context.csv` (ohne Quelle-Spalte) nicht mitschicken.
