# Global Master Map

<!-- Reality Block
last_update: 2026-03-27
status: stable
scope:
  summary: "Globale Projektlandkarte: Was existiert, wo liegt es, wie hängt es zusammen."
  in_scope:
    - project list and status
    - cross-dependencies
    - architecture layers
  out_of_scope:
    - per-project implementation details
notes: []
-->

## Aktive Projekte

| Projekt | Docs | Code | Infra | Status |
|---------|------|------|-------|--------|
| **Inner Compass** | `projects/inner_compass/` | `code/inner_compass_app/` | Spark (Worker, MinerU, LLM) | Aktiv — Pre-Launch |
| **Trading Bot** | `projects/trading_bot/` | `code/trading-bot/` | — | Aktiv |
| **Rest Data Platform (ASTRA IMC)** | `projects/rest_data_platform/` | `quantensprungai/astra-imc-platform` | — | Planung |
| **Bot Platform** | `projects/bot_platform/` | — | Spark (LLM-Backend) | Pause |
| **Anna's Archive Toolkit** | `projects/annas_archive_toolkit/` | `code/annas-archive-toolkit/` | — | Wartung |

## Ruhende / Frühe Projekte

| Projekt | Docs | Status |
|---------|------|--------|
| IHK SaaS | `projects/ihk_saas/` | Pause |
| Kiosk Agent | `projects/kiosk_agent/` | Idee |
| Super Buddy | `projects/super_buddy/` | Idee |
| AL Meta | `projects/al_meta/` | Idee |
| AI 2027 | `projects/ai_2027/` | Idee |
| LinkedIn Serie | `projects/linkedin_serie/` | Idee |

## Architektur-Ebenen

```
Layer 1 — Spark (LLM Serving)
  SGLang / vLLM als Inferenz-Backends
  Docs: infrastructure/spark/

Layer 2 — Shared Data / RAG
  Embeddings, Vector Stores, Ingestion (pro Projekt)

Layer 3 — Agents / Pipelines
  Tool-Using Agents, Routing, Workflows

Layer 4 — Applications
  Trading Bot, Inner Compass, Assistants
```

## Infrastruktur

| Bereich | Pfad | Inhalt |
|---------|------|--------|
| Spark / LLM | `infrastructure/spark/` | Serving, Engines, Worker Ops |
| Proxmox | `infrastructure/proxmox/` | VM-Setup, Homelab |
| Tailscale | `infrastructure/tailscale/` | VPN, Machines |
| Docker | `infrastructure/docker/` | Container-Setup |
| Makerkit | `infrastructure/next-supabase-turbo/` | Framework-Referenz |

## Konventionen

- **Doku-Strategie:** `projects/_meta/doc_and_rules_strategy.md`
- **Glossar:** `projects/_meta/glossary.md`
- **Projekt-Struktur-Muster:** Jedes aktive Projekt hat `cursor/` + `reference/` (siehe Inner Compass als Referenz)
