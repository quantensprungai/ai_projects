<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "Spezifikation: Topics/Profiles (z. B. Human Design) als wiederverwendbare Konfiguration."
  in_scope:
    - topic format
    - profile format
    - constraints
  out_of_scope:
    - implementation code
    - instructions for illegal acquisition
notes: []
-->

# Topics & Profiles – Spec

## Ziel

Eine einzige, einfache Eingabeform, damit das System für verschiedene Domänen wiederverwendbar ist.

## Topics

- Eine Liste von Keywords/Begriffen (1 pro Zeile oder JSON Liste)
- Optional: Sprache, Priorität, Synonyme

Beispiel (konzeptionell):
- `human design`
- `bazi`
- `gene keys`

## Profiles

Ein “Profile” definiert:
- Output‑Ordner/Namensschema
- Limits (z. B. max Ergebnisse)
- Priorität/Ranking‑Heuristiken
- nachgelagerte Verarbeitung (RAG‑Ingest / KG‑Ingest)

Siehe auch: `profile_schema.md` (verbindliche Felder, `query_mode`, Beispiele).

### Profile sind der richtige Mechanismus (kein extra Unterprojekt nötig)

Dein aktueller Use‑Case passt perfekt zu Profiles:

- **Survival**: “Post‑Apokalypse / Überleben & Wiederaufbau” Wissen sammeln, kuratieren, ggf. teilen/LLM‑verarbeiten.
- **HD Content** (statt “esoteric”): Content‑Sammlung für `projects/hd_saas` aus mehreren Systemen (Human Design, BaZi, …).
- Später: weitere Themen → einfach **neues Profile** hinzufügen.

Das heißt: **Input‑Workflow bleibt gleich**, aber **Output/Downloads/Metadaten** werden pro Profile getrennt.

### Namenskonvention (empfohlen)

Statt “esoteric”:
- `hd_content` oder `hd_saas_content` (klarer Bezug)
- oder generisch `domain_hd` / `domain_survival`

### Struktur (Code-Repo)

Konzeptuell (im Code‑Repo):

- `projects/survival/…` (z. B. config)
- `projects/hd_content/…` (topics + config)

Jedes Profile enthält:
- **Input**: `topics.txt` oder `config.json`
- **Output Root**: eigener Zielordner (damit nie gemischt wird)
- **Pipeline Flags**: Selenium/Proxy/Rate‑Limit/etc.

### Wann wäre ein separates Unterprojekt sinnvoll?

Nur wenn sich *eines* davon stark unterscheidet, z. B.:
- andere Runtime (nicht VM102), anderes Security‑Modell
- komplett andere Quellen/Parsing‑Logik (nicht nur andere Topics)
- anderes Publishing/Governance (separate Releases, separate Permissions)

## Nicht-Ziele

- Keine hardcodierten, domänenspezifischen Pipelines pro Thema
- Keine “nur für HD” Sonderlogik


