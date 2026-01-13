<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "Verbindliches Profile-Schema: query_mode, Inputs, Outputs, und wie Profiles im Code-Repo ausgeführt werden."
  in_scope:
    - schema
    - naming conventions
    - examples
  out_of_scope:
    - implementation code changes beyond wiring/env-vars
notes: []
-->

# Profile Schema (verbindlich)

## Idee

Ein **Profile** ist eine wiederverwendbare “Collection‑Definition” (Input + Regeln + Output‑Trennung).  
Das Toolkit bleibt **eine Pipeline**, aber pro Profile können Stages/Inputs variieren.

## Profile-Ordner (im Code-Repo)

Jedes Profile lebt unter:

- `code/annas-archive-toolkit/projects/<profile_id>/`

Beispiele:
- `projects/survival/`
- `projects/hd_content/`

## Pflichtfelder (konzeptionell)

- **`profile_id`**: z. B. `survival`, `hd_content`
- **`query_mode`**:
  - `categories` (LibGen/Category-Mapping)
  - `keywords` (Topics/Schlagwörter)
- **`output_root`**: eigener Ordner je Profile (niemals mischen)
- **`metadata_outputs`**: CSV/JSON Pfade unterhalb `output_root`

## Input-Artefakte

### Mode: `categories` (Survival)

- `config.json` enthält:
  - `category_mapping` (Kategorie → Zielordner)
  - Rate Limit / Selenium / Proxy
  - Output-Dateien

### Mode: `keywords` (HD Content)

Mindestens eins von:
- `topics.txt` (1 Keyword pro Zeile)
- oder `config.json` (wenn du Keywords + Output/Proxy/Selenium sauber bündeln willst)

## Ausführung (Profile auswählen)

Konvention (bereits implementiert):

- **`AAT_CONFIG`**: Pfad zu Profile-Config (JSON)
- **`AAT_TOPICS`**: Pfad zu Topics-Datei (TXT)

Beispiele:

```text
set AAT_CONFIG=projects/survival/config.json
python src/libgen_metadata_collector.py
```

```text
set AAT_TOPICS=projects/hd_content/topics.txt
python src/simple_collector.py
```

## Wann unterschiedliche Logik “ok” ist

Unterschiedliche Logik ist **erlaubt**, solange:

- sie über `query_mode` / Config toggles erklärbar ist
- Outputs strikt getrennt bleiben
- kein neues Repo nötig ist

Ein separates Unterprojekt/Repo lohnt sich erst bei komplett anderem Source/Parser/Runtime/Governance.


