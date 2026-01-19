<!-- Reality Block
last_update: 2026-01-19
status: draft
scope:
  summary: "Langfristiges, wartbares Setup für DGX Spark als Data-Plane (Ollama/ArangoDB/txt2kg + Worker)."
  in_scope:
    - filesystem layout
    - service layout (docker/systemd)
    - port & dependency strategy
    - cleanup & ops hygiene
  out_of_scope:
    - konkrete Business-Logik der HD-Extraktion
    - Zugangsdaten / Secrets
notes: []
-->

# DGX Spark – Long‑Term Setup (Data Plane)

## Ziel

DGX Spark soll stabil als **Data Plane** laufen:
- verarbeitet Jobs (Batch/Worker)
- hostet lokale AI‑Services (optional)
- schreibt Resultate in Supabase/Makerkit (Control Plane)

Wichtig: **einfach reproduzierbar**, wenig „Ops‑Drama“, klar getrennte Verantwortlichkeiten.

## Grundprinzipien

- **Ein Service pro Port** (keine Doppel‑ArangoDB/Ollama Instanzen).
- **Base Services** (z. B. Ollama, ArangoDB) sind „shared“, Projekte (txt2kg, Worker) docken an.
- **Keine großen Playbooks als harte Abhängigkeit**: Playbooks sind „nice“, Worker bleibt der stabile Kern.
- **Secrets niemals in Git** (nur env files, die lokal liegen).

## Empfohlene Ordnerstruktur (Spark)

```text
~/srv/
  compose/                # docker compose stacks (app-level)
    base/                 # shared services (ollama, arangodb)
    txt2kg/               # optional: txt2kg app (nur UI/API)
    whisper/              # optional
  hd-worker/              # worker code (git checkout)
    venv/                 # python venv (nur worker deps)
    config/               # yaml/env templates (ohne secrets)
    logs/                 # worker logs
  data/
    arangodb/             # persistent arango volume bind (optional)
    ollama/               # persistent ollama models (optional)
    staging/              # temp files (downloaded assets, extracted text)
```

## Ports / Services (Standard)

| Service | Port | Ownership | Kommentar |
|---|---:|---|---|
| Ollama | 11434 | base | ein Ollama für alles |
| ArangoDB | 8529 | base | eine ArangoDB für alles |
| txt2kg UI/API | 3001 | optional | nur wenn wir es nutzen |
| Whisper | 9000 | optional | nur wenn wir es nutzen |

Regel: wenn ein Port belegt ist, **nicht** neuen Container mit gleichem Port starten – stattdessen:
- bestehende Instanz **wiederverwenden**, oder
- Port bewusst ändern (z. B. Arango 8530), aber dann in allen Configs konsistent.

## Docker Permission Hygiene

Wenn du `permission denied while trying to connect to the Docker daemon socket` siehst:

```bash
sudo usermod -aG docker $USER
newgrp docker
docker ps
```

Oder: konsequent `sudo docker ...` nutzen.

## txt2kg Playbook: sauberer Betrieb im „shared services“ Setup

Dein aktueller Konflikt (aus `keep10-spark.md`) ist erwartbar:
- Playbook startet eigene `arangodb` + `ollama`
- du hast aber bereits `arangodb:8529` und `ollama:11434`

**Target State**:
- `base/` stellt ArangoDB + Ollama bereit
- `txt2kg` Stack startet **nur** die App (UI/API)
- App zeigt auf `host.docker.internal:8529` und `host.docker.internal:11434`

Wichtig:
- `depends_on` auf arangodb/ollama entfernen oder Services im Compose nicht definieren
- `extra_hosts: host.docker.internal:host-gateway` nutzen (Linux)

## MinerU / PDF Extraction: Empfehlung

Deine Logs zeigen, dass Docker‑Builds gerade Reibung erzeugen (Base Image Tag / Docker perms).

Pragmatischer Weg:
- **erst venv** auf Spark, wenn du MinerU/Marker wirklich brauchst
- oder zunächst **Marker/Docling/PyMuPDF4LLM** (geringeres Setup-Risiko)

Für den Start des Systems ist PDF‑Extraction **nicht** nötig: wir beginnen mit `import_assets_jsonl`.

## Modelle / Storage Cleanup (aus `keep.md`)

Du hast sehr große Modelle herumliegen (z. B. DeepSeek‑V3). Für langfristige Stabilität:
- Modelle in **einem** Verzeichnis konsolidieren (z. B. `~/ai/models/…`)
- klare Entscheidung: was bleibt, was fliegt
- „Default“ Modelle definieren:
  - **Extraction**: `qwen3-32b-nvfp4` (oder kleiner fürs erste)
  - **Embeddings**: `bge-m3`
  - **Long context / Planning**: `llama4-scout-17b`

## Minimaler Start (empfohlen)

1) Base Services stabil: Ollama + ArangoDB laufen (oder nur Ollama, wenn Arango noch nicht gebraucht wird).
2) Worker v0 läuft: `import_assets_jsonl` Job → `hd_assets` in Supabase.
3) Erst danach: PDF/Text/Audio‑Extraktion + Text2KG‑Integration.

## Ist‑Zustand Check (bitte auf Spark ausführen)

Damit wir entscheiden können „aufräumen vs. weiterbauen“, poste bitte diese Outputs:

```bash
whoami
groups

docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"
sudo ss -lntp | egrep ':(11434|8529|3001|9000)\\b' || true
```

Optional (wenn vorhanden):

```bash
ls -la ~/dgx-spark-playbooks/nvidia/txt2kg/assets/deploy/compose
```

