# Inner Compass — Handover

> Copy-Paste diesen Block am Anfang eines neuen Chat-Fensters (Cursor oder Claude).

---

## Kontext-Block (kopieren)

```
Projekt: Inner Compass — geburtsbasiertes Meta-System
Tech: Next.js (Makerkit v2.23.14) + Supabase + Spark (GPU, Worker, MinerU, LLM)
Stand (2026-02-16): S1-S4 erledigt. Schema, Worker, Strukturgraph stehen.
  - Schema: 20260216150000_inner_compass_core.sql (11 sys_*-Tabellen + pgvector)
  - Worker: ic_worker.py (~650 Zeilen, sys_*-nativ, 6 Job-Typen, --dry-run)
  - Strukturgraph: 832 Nodes + 698 Edges (10 Systeme, HD: 526 Nodes)
  - Nächster Schritt: S5 E2E-Validierung (1 HD-PDF durch neue Pipeline)
  - S5 Runbook: reference/s5_runbook.md (VM102 PDF → MinerU → LLM, Zwei-Phasen)
  - Deep Structure: Demand-driven, Backlog in reference/deep_structure_plan.md
  - Offen: S6 Rest (assets_jsonl-Import sys_*), S7 Cloud-Deployment

Lies zuerst: projects/inner_compass/cursor/status.md
Dann je nach Aufgabe:
- Schema/DB: cursor/architecture.md + cursor/contracts.md
- Pipeline/Worker: cursor/pipeline.md + code/hd_saas_app/apps/web/scripts/ic_worker.py
- Engine-Integration: cursor/engines.md
- Produkt-Kontext: reference/prd_v3.md
- Content-Akquise: code/annas-archive-toolkit/ + cursor/pipeline.md §8 (Zwei-Gate-Filtering)

Kernzahlen: 15 Dimensionen, 10 Lebensbereiche, 5 Datenschichten, 4 Staffel-1-Systeme.
Schema: sys_* Tabellen (11), Postgres+pgvector, jsonb Payloads.
Code-Repo: code/hd_saas_app/ (wird zu inner_compass_app umbenannt)
```

---

## Wenn der Chat über ARCHITEKTUR geht

```
Zusätzlich lesen:
- cursor/architecture.md (Schema, Datenschichten, Tech Stack)
- cursor/contracts.md (Dimensions-Contract, Payloads, Enums)
- Aktuelles SQL: code/hd_saas_app/apps/web/supabase/migrations/ (Repo wird zu inner_compass_app umbenannt)
- Wo System-Artefakte wohnen (Deskriptoren, Taxonomie, Matrix): architecture.md §8
- Wo Engine-Kits wohnen (geklont, Struktur + Laufzeit): architecture.md §8 (Tabelle) + engines.md §6
- Deskriptor vs. Seed vs. Structure, alle Ebenen pro System, Speicherformat: reference/structure_descriptor_seed.md
```

## Wenn der Chat über PIPELINE geht

```
Zusätzlich lesen:
- cursor/pipeline.md (Jobs, Flows, Prompts)
- Worker-Specs in cursor/pipeline.md Abschnitt 7
- Infra: infrastructure/spark/ (MinerU, LLM-Serving)
```

## Wenn der Chat über PRODUKT/DESIGN geht

```
Zusätzlich lesen:
- reference/prd_v3.md (vollständiges PRD)
- reference/decisions.md (alle Design-Entscheidungen mit Begründung)
- reference/inspirations.md (AQAL, IFS, Gene Keys, Poster-Analyse)
```
