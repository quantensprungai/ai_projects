# dev_environment

<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "Dev-Setup (VM105/Laptop): wie du Repo, Tailscale und Spark-Remote-Operations zusammen benutzt."
  in_scope:
    - workflow description
    - remote ops (via SSH/Tailscale)
  out_of_scope:
    - storing private keys in repo
notes: []
-->

Dev-Setup (Laptop/VM105), Cursor/Tools, OS/Driver, Repo-Konventionen.

## Empfohlenes Workflow-Setup

- **Repo** liegt auf VM105/Laptop (`ai_projects/`)
- **Spark** ist reiner Runtime-Server (Modelle/Container/Serving)
- Steuerung erfolgt von VM105 aus via **Tailscale SSH**

## Remote-Operations (VM105 → Spark)

Minimal (WSL2 oder Linux Shell):

- Status: `ssh sparkuser@spark-56d0 'systemctl status vllm --no-pager'`
- Start/Stop: `ssh sparkuser@spark-56d0 'sudo systemctl restart vllm'`
- Logs: `ssh sparkuser@spark-56d0 'journalctl -u vllm -n 200 --no-pager'`

Dokumentation der Endpoints/Ports liegt in:
- `infrastructure/spark/inference_endpoints.md`

## VM105 Anzeige/Remote (RustDesk)

Wenn Windows die Auflösung nicht ändern lässt (z. B. nur 1280×800, ausgegraut), siehe:

- `vm105_remote_display.md`

## VM105 WSL2

- `vm105_wsl2.md`



