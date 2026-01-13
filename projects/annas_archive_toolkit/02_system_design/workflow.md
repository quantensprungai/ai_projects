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
3. **Select**: Kandidaten priorisieren (Heuristiken/Rules)
4. **Acquire**: Inhalte beschaffen/holen (Quelle abhängig; rechtmäßig)
5. **Organize**: Sortieren/Dedupe/Katalog
6. **Publish**: Export/Index (z. B. CSV/JSON) und Übergabe an HD‑SaaS/RAG/KG

## Run Location

- **VM105**: Code/Doku, Parameter/Profiles pflegen
- **VM102**: Pipeline ausführen (Runtime)

## Links

- Code: `../../code/annas-archive-toolkit/`
- Runtime Setup Docs (code repo): `../../code/annas-archive-toolkit/docs/README.md`
- Infra: `../../infrastructure/docker/vm102_docker_host.md`


