<!-- Reality Block
last_update: 2026-01-27
status: draft
scope:
  summary: "Bot Platform (Clawdbot): Zielbild, Struktur und Verlinkungen ins Multi‑System (VM102/Spark/HA)."
  in_scope:
    - project purpose and scope
    - document index / pointers
    - high-level decisions (ADR-lite)
  out_of_scope:
    - implementation details (belongs to code repos)
    - secrets / tokens
notes: []
-->

# Bot Platform (Clawdbot)

## Zweck
Dieses Projekt beschreibt, **wie wir Clawdbot als Bot-Framework** in unserem Multi‑System einsetzen:
- mehrere Bots/Use‑Cases (ops, home, learning, project)
- klare **Security‑Zonen** (Profiles) und **Tool‑Allowlists**
- Hosting/Runtime auf **VM102** (Docker Host), LLM‑Compute auf **Spark**

## Quick Links (Source of Truth)

- **Hosting (VM102 / Docker Host)**: `infrastructure/docker/vm102_docker_host.md`
- **Tailscale Zugriff/HTTPS Patterns**: `infrastructure/tailscale/README.md`
- **Spark OpenAI‑kompatible Endpoints**: `infrastructure/spark/inference_endpoints.md`
- **Home Assistant Runtime (CT110)**: `infrastructure/proxmox/01_setup/1_proxmox-komplettsetup.md` (CT110 Abschnitt)

## Doku‑Struktur

- `00_overview/mission.md`: Zielbild & Erfolgskriterien
- `00_overview/scope.md`: In/Out of scope (v1)
- `02_system_design/architecture.md`: Komponenten (Gateway/Agents/Profiles/Nodes), Datenflüsse
- `02_system_design/profiles_and_bots.md`: Profile‑Schnitt (ops/personal) + die 4 Bots
- `02_system_design/hosting_vm102.md`: Betrieb auf VM102 (Ports, State, Backups, Updates)
- `02_system_design/security_and_guardrails.md`: Threat Model, Pairing/Allowlist, Tool Policy
- `02_system_design/integrations.md`: Spark / HA / Supabase / “Project bots” (z. B. Trading Bot)
- `03_roadmap/roadmap.md`: Milestones & Akzeptanzkriterien (chat‑history‑unabhängig)

## Decision (ADR‑lite)

### Decision
Clawdbot läuft als **remote Gateway** auf **VM102**. Spark bleibt **Inference/Data‑Plane** (SGLang). Home Assistant bleibt auf **CT110**.

### Rationale
- VM102 ist der “App Host” (Docker‑Utilities) und eignet sich für Always‑On Gateways.
- Spark ist teuer/fragil/compute‑orientiert → dort keine Bot‑Control‑Plane.
- HA soll stabil bleiben → keine zusätzlichen Frameworks in CT110.

### Consequences
- Clawdbot‑State (`~/.clawdbot*`, `~/clawd*`) muss auf VM102 gesichert werden.
- Für risky Ops (SSH/Supabase service role) trennen wir Profile/Zonen.

