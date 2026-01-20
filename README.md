# ai_projects (Multi‑Projekt Repository)

<!-- Reality Block
last_update: 2026-01-20
status: stable
scope:
  summary: "Repo-Root: Überblick, Struktur und harte Trennregeln."
  in_scope:
    - repository structure
    - separation rules
  out_of_scope:
    - project specs
    - infrastructure implementation
notes: []
-->

Dieses Repository ist die **Entwicklungs‑ und Dokumentations‑Basis** für alle Projekte (Apps/Agents/Pipelines) und die dazugehörige Infrastruktur‑Doku.

## Struktur

- `projects/` – Produkt-/Projekt-Dokumentation (Trading Bot, IHK SaaS, Kiosk Agent, …)
- `infrastructure/` – Infrastruktur-Themen (Proxmox, Tailscale, Monitoring, Dev-Environment, …)
- `code/` – **separate** Code-Repositories (je Projekt eigenes Git-Repo; nicht Teil des Root-Repos)

## Git-Strategie (wichtig)

- Dieses Root-Repo (falls du es auf GitHub pushst) ist **Docs/Infra only**.
- Jedes Projekt unter `code/<repo>/` bleibt ein **eigenes** Git-Repo und wird separat gepusht/gezogen.
- Keine Konflikte: der Root ignoriert `code/` via `.gitignore`.

Optional (wenn du Code-Versionen *im* Root referenzieren willst): Git **Submodules**.

## Spark (wichtige Trennung)

**Spark ist ein reiner Inferenz-/Infra-Server** (Modelle/Container/Serving laufen dort), aber **im Repo liegt nur die Spark-Dokumentation** – und zwar unter:

- `infrastructure/spark/`

Dort existieren **nur** diese Dateien:
- `sglang_config.md`
- `vllm_config.md`
- `llm_serving.md`
- `inference_endpoints.md`
- `optimizations.md`
- `quantizations.md`

### Aktueller Stand (Reality Check)

- **Spark Inference** ist dokumentiert unter `infrastructure/spark/` (Ports, Engines, Endpoints).
- **Robuster Admin-Zugriff**: zusätzliches OpenSSH (`sshd`) auf Spark via Port `2222` (weil Tailscale SSH je nach Installationsart problematisch sein kann).
- **HD Worker Ops**: Debug/Retry/typische Fehlerbilder unter `infrastructure/spark/hd_worker_ops.md`.


