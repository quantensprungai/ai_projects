# Flora PDF-Extract (MinerU)

Scripts for lecture PDF → Markdown used by Flora learning subjects (ESF follow-ups, Neurologie, …).

| Script | Where | Role |
|--------|-------|------|
| `extract_lecture_pdf.py` | Spark (or local pypdf) | Core extract |
| `run_extract_on_spark.py` | Windows / VM105 | SCP + SSH orchestration |

See `infrastructure/docker/workspace-flora/learning/neuro/README.md`.
