# Glossary

<!-- Reality Block
last_update: 2026-01-13
status: stable
scope:
  summary: "Zentrale Begriffe (Repo-weit), um Terminologie stabil zu halten."
  in_scope:
    - core concepts
    - project-level terms
    - technical terms
  out_of_scope:
    - deep implementation details
notes: []
-->

Kurze, konsistente Definitionen der wichtigsten Begriffe in diesem Repo.

## Core Concepts

- **Agent**: (Semi-)autonomer Prozess, der Aufgaben mit LLM‑Reasoning und Tools ausführt.
- **Pipeline**: Sequenz aus Agenten/Tools/Funktionen, die Input → Output verarbeitet.
- **RAG (Retrieval Augmented Generation)**: Abruf aus Wissensquellen + LLM‑Reasoning.
- **Vectorization / Embeddings**: Umwandlung von Text in Vektoren für Ähnlichkeitssuche.
- **Long‑Context Model**: Modell mit sehr großem Kontextfenster (hunderttausende bis Millionen Tokens).

## Repository Terms

- **Projekt**: Produkt-/App-/Agent-/Pipeline‑Vorhaben unter `projects/`.
- **Infrastruktur**: Enabler (Proxmox/Netzwerk/Monitoring/Backups/Dev-Setup) unter `infrastructure/`.
- **Spark**: Inferenz-/Infra‑Server (Modelle/Serving/Container). **Kein Repo, kein Cursor.**

## Technical Terms

- **SGLang**: High‑speed Runtime für interaktive Chat-/Agent‑Workloads (auch multimodal).
- **vLLM**: High‑throughput Serving Engine (OpenAI‑kompatibles API, Batch/RAG).
- **TP (Tensor Parallelism)**: Aufteilung eines Modells über mehrere GPUs.
- **NVFP4 / MXFP4 / FP8**: Quantisierungs-/Präzisionsformate (Blackwell‑optimiert).


