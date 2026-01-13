<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "Projekt: Wiederverwendbares Toolkit/Service für topic-basierte Bibliotheks-/Dokumenten-Collections (HD/BaZi/…)."
  in_scope:
    - project scope
    - workflow description (high-level)
    - deployment model (VM105 -> VM102)
  out_of_scope:
    - instructions for illegal acquisition of copyrighted works
    - secrets/credentials
notes: []
-->

# Anna’s Archive Toolkit (Projekt)

## Ziel

Ein wiederverwendbares System, das aus einer **Themenliste** (“topics”) eine Collection erzeugt (Metadaten → Auswahl → Verarbeitung), z. B. für:
- Human Design (HD)
- BaZi
- weitere Wissensdomänen

## Trennung (wichtig)

- **Infrastruktur/Stack** (VM102/Proxmox/Tailscale/Backups/Monitoring): `infrastructure/`
- **Projekt/Workflow/Tooling**: `projects/annas_archive_toolkit/`

## Code-Source-of-Truth & Deployment

Empfohlen:
- Code liegt versioniert (Git) in/bei VM105.
- VM102 ist Runtime und zieht Releases/Updates (kein manuelles Copy‑Paste).

### VM105 (dieser Workspace)

- **Code-Repo (working copy)**: `code/annas-archive-toolkit/`
- **Doku/Projektstruktur**: `projects/annas_archive_toolkit/`

## Kanonische Doku (hier)

- `00_overview/` (Mission, Problem, Value)
- `01_spec/` (Topics/Profiles)
- `02_system_design/` (Deployment/Sync, Workflow)

Siehe auch:
- `infrastructure/proxmox/01_setup/3_annas-archive-wissenssystem.md`
- `projects/annas_archive_toolkit/02_system_design/deployment_and_sync.md`


