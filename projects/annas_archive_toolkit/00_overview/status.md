<!-- Reality Block
last_update: 2026-01-16
status: draft
scope:
  summary: "Aktueller Stand (Snapshot) + nächste Schritte für Anna's Archive Toolkit (HD + Survival)."
  in_scope:
    - current status
    - next steps
    - run locations
  out_of_scope:
    - instructions for illegal acquisition of copyrighted works
    - secrets/credentials
notes: []
-->

# Status Snapshot – Anna’s Archive Toolkit

## Wo wir stehen (heute)

- **Profile vorhanden**:
  - **`hd_content`**: keyword/topic driven Collection (`code/annas-archive-toolkit/projects/hd_content/`)
  - **`survival`**: category-driven Collection (`code/annas-archive-toolkit/projects/survival/config.json`)
- **Metadaten‑Output**:
  - `hd_content` schreibt in **`output/hd_content/metadata.*`** und kann **`assets.jsonl`** exportieren.
  - `survival` schreibt in **`output/libgen_survival_collection.*`** (auf VM102 vorhanden; im Git‑Repo ist `output/` ignoriert).

## Pipeline‑Logik (wichtig: “Metadaten vs Download vs Ingestion”)

1. **Collect (Metadaten)**: Wir sammeln Metadaten (Titel/Autor/MD5/URL/Topic/Category) als **Katalog & Selektionsbasis**.
2. **Select (Priorisieren)**: Wir wählen gezielt Kandidaten aus (Heuristiken/Regeln/Manuell).
3. **Acquire (optional)**: Inhalte beschaffen (z. B. eigene Uploads/own library/licensed/free content).
4. **Ingest (Downstream Pipeline)**: Erst danach startet die eigentliche Verarbeitung (je nach Projekt, z. B. HD‑SaaS oder Survival‑Pipeline):
   - OCR/Whisper → Cleaning → Chunking → Extraction → **Text2KG** → Knowledge Graph + Dynamics.

> **Hinweis**: `assets.jsonl` ist ein **Ingest‑Contract**, der zunächst **metadata‑only** ist. Der “Acquire/Download”-Schritt ist davon getrennt.

## Wo läuft was?

- **VM105**: Doku/Profiles pflegen, Code committen/pushen.
- **VM102**: Runtime (Runs ausführen). Standard: **pull‑only**.

## Nächste Schritte (empfohlen)

- **HD (`hd_content`)**:
  - `assets.jsonl` als Ingest‑Contract in HD‑SaaS übernehmen (Supabase Tabellen + Pipeline).
  - Danach: Quellen‑Textpipeline (Dokumente/Transkripte) anbinden.
- **Survival (`survival`)**:
  - Optional: analog einen `assets.jsonl` Export ergänzen (damit Survival denselben Ingest‑Contract wie `hd_content` hat).
  - Danach: “Acquire/Download”-Stufe (wenn benötigt) + anschließende Verarbeitung im Survival‑Downstream.


