<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "Systemdesign: Workflow (high-level) von Topics/Profile → Metadaten → Auswahl → Verarbeitung."
  in_scope:
    - pipeline stages (high-level)
    - interfaces between stages
  out_of_scope:
    - implementation details
notes: []
-->

# Workflow (high level)

## Pipeline-Stufen

1. **Input**: Topics/Profile (z. B. `projects/esoteric/topics.txt`, `projects/survival/config.json`)
2. **Collect**: Metadaten sammeln (Checkpoint/Resume)
3. **Select**: Kandidaten priorisieren (Heuristiken/Rules/Manuell)
4. **Acquire (optional)**: Inhalte beschaffen/holen (**quelle abhängig, rechtmäßig**)
5. **Organize**: Sortieren/Dedupe/Katalog (falls Inhalte vorhanden sind)
6. **Publish**:
   - **metadata-only**: Export/Index (CSV/JSON/`assets.jsonl`) für Downstream‑Pipelines
   - **content**: Übergabe an Verarbeitung (OCR/Whisper → Extraction → Text2KG → KG)

> Wichtig: `assets.jsonl` ist ein **Ingest‑Contract** und kann **metadata‑only** sein. “Acquire” ist davon getrennt.

## Run Location

- **VM105**: Code/Doku, Parameter/Profiles pflegen
- **VM102**: Pipeline ausführen (Runtime)

## Links

- Code: `../../code/annas-archive-toolkit/`
- Runtime Setup Docs (code repo): `../../code/annas-archive-toolkit/docs/README.md`
- Infra: `../../infrastructure/docker/vm102_docker_host.md`


