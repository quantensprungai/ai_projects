<!-- Reality Block
last_update: 2026-01-16
status: draft
scope:
  summary: "Mission/Zielbild für HD-SaaS (HD-System + Multi-System Perspektive)."
  in_scope:
    - mission statement
    - success criteria
  out_of_scope:
    - implementation details
notes: []
-->

# Mission – HD‑SaaS

HD‑SaaS ist ein **Human‑Design Knowledge & Guidance System**, das Human Design (und perspektivisch weitere geburtsdatenbasierte Systeme wie BaZi/Astrologie/Gene Keys) **konsistent, nachvollziehbar und interaktiv** nutzbar macht.

Kernprinzip: **LLM als Interface**, aber **Wissen/Regeln/Prozesse** werden **explizit gespeichert** (statt “im Prompt zu hoffen”).

## Mission Statement

Wir bauen ein System, das:
- **Wissen strukturiert** (Knowledge Graph: Elemente + Relationen)
- **Interpretationsquellen verwaltet** (Interpretations‑Repository, versionierbar)
- **Prozesswissen abbildet** (Dynamics Engine: Phasen, Fallen, Wege)
- **Kontext & Zeit berücksichtigt** (Context/Temporal Layer)
- **für Menschen verständlich kommuniziert** (Chat + UI, mit Referenzen/Quellen)

## Erfolgskriterien (v1)

- **Traceability**: Jede Aussage im Output kann auf **Quellen/Chunks** zurückgeführt werden.
- **Konsistenz**: Wiederholte Fragen liefern **stabile, nicht widersprüchliche** Antworten (bei gleichem Kontext).
- **Ingestion‑fähig**: Externe Collections (z. B. `assets.jsonl` aus Anna’s Archive Toolkit) können als “Input Contract” verarbeitet werden.
- **Operabel**: Verarbeitung ist als Job/Pipeline ausführbar (VM102/DGX Spark), UI ist Makerkit‑fähig (Next.js + Supabase).


