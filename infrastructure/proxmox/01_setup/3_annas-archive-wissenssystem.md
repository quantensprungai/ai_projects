# Anna's Archive – Wissenssystem (Teil 3)

<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "Download-Strategien, Archivierungs- und Wissenssystem-Design (Anna's Archive) im Kontext des Homelabs."
  in_scope:
    - download strategy
    - storage and organization
    - automation ideas (documentation)
  out_of_scope:
    - actual downloader scripts / automation code


## Zweck

Dieses Dokument ist **Teil 3** des 3‑Dokumente‑Systems und beschreibt die **Strategie/Prozesse** für:

- Sammlung/Quellen (nur legal)
- Archivierung & Metadaten
- Automatisierungsideen (Doku)
- Wiederverwendbare “Topic‑Pipelines” (z. B. Human Design / BaZi / …)

## Wichtig: Trennung in Stack vs Projekt

Ja: Das muss getrennt werden.

- **Stack (Infrastruktur)**: wo läuft es, welche Services, welche Ports, Backups, Monitoring (VM102/Proxmox/Tailscale).
- **Projekt (Inhalt/Workflow/Tooling)**: das eigentliche Toolkit/Service (Konfiguration, Topics, Pipeline, Roadmap).

### Was gehört wohin?

| Bereich | Ort im Repo | Beispiel |
|---|---|---|
| Runtime/Hosting (VM102, Docker, Zugriff) | `infrastructure/` | `infrastructure/docker/vm102_docker_host.md` |
| Remote Access (RustDesk) | `infrastructure/remote_access/` | `infrastructure/remote_access/rustdesk.md` |
| Netzwerk (Tailscale) | `infrastructure/tailscale/` | `infrastructure/tailscale/machines.md` |
| Backups/Restore | `infrastructure/backups/` | `infrastructure/backups/proxmox_backups.md` |
| Projekt-Doku & Roadmap | `projects/` | `projects/annas_archive_toolkit/` (neu) |

## Wo liegt der Code aktuell (Laptop/VM102)?

Dein aktueller Stand ist: Code/Docs liegen teils auf dem Laptop, teils auf VM102 (`~/libgen-survival-project`).

**Empfohlen (Enterprise-clean):**
- **Source of Truth für Code**: in einem Git‑Repo (z. B. unter diesem Workspace: `ai_projects/` oder als eigenes Repo).
- **Deployment/Runtime**: VM102 zieht per `git pull` (oder per CI/rsync), kein “Hand‑Copy”.

> Wichtig: Spark bleibt dabei unberührt. VM102 ist Docker‑Host/Utility, nicht Spark.

## Wiederverwendbarkeit für weitere Themen (HD/BaZi/…)

Zielbild: **Topic‑Driven Collections** – du pflegst eine Liste von Themen/Keywords und erzeugst daraus eine Collection (Metadaten → Auswahl → Verarbeitung).

Praktische Konfiguration (Design, keine Code‑Anleitung):
- `topics.txt`: 1 Topic pro Zeile (z. B. “human design”, “bazi”, “…”)
- `collection.yml/json`: Limits, Sprachen, Prioritäten, Ausgabeordner, “profile”

Späterer Ausbau: kleiner Service, der
- Topics annimmt (UI/CLI/API)
- eine Collection erzeugt
- den Workflow orchestriert (Queue/Retry/Checkpoint)

## Verlinkungen (kanonische Doku im Repo)

- VM102 Docker Host: `infrastructure/docker/vm102_docker_host.md`
- Backups: `infrastructure/backups/proxmox_backups.md`
- Monitoring/Ports: `infrastructure/monitoring/services_and_ports.md`
- Tailscale Zugriff: `infrastructure/tailscale/README.md`



