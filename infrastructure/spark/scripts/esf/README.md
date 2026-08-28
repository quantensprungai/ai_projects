# ESF – lokale Pipeline (Spark optional)

Wenn Spark offline ist: alles auf VM105 mit Anthropic API.

## Setup

```powershell
cd c:\Users\Admin105\ai_projects
pip install anthropic pypdf python-dotenv

copy infrastructure\docker\workspace-flora\learning\esf\.env.example `
     infrastructure\docker\workspace-flora\learning\esf\.env
# .env bearbeiten: ANTHROPIC_API_KEY + ggf. Modell-IDs
```

## Modell-Mix (kostensparend)

| Schritt | Modell | ca. Kosten |
|---------|--------|------------|
| Outline, Karten, Übungen, Glossar | Haiku 4.5 | ~0,50–1,50 € |
| Quant-Module + Prüfungssimulation | Sonnet 4.6 | ~1–3 € |
| **Gesamt `all`** | | **~2–5 €** |

## Befehle

```powershell
# Nur PDF-Extraktion (kostenlos)
python infrastructure\spark\scripts\esf\esf_local_pipeline.py extract

# Vorschau ohne API
python infrastructure\spark\scripts\esf\esf_local_pipeline.py all --dry-run

# Komplett (nach .env) — extract schon erledigt:
python infrastructure\spark\scripts\esf\esf_local_pipeline.py all --skip-extract

# Nur Probeklausur (nach modules/)
python infrastructure\spark\scripts\esf\esf_local_pipeline.py pruefung
```

Output: `infrastructure/docker/workspace-flora/learning/esf/`

## Bessere PDF-Extraktion (MinerU / Neuro & Co.)

Für scan-/layout-lastige Vorlesungen (z. B. Neurologie) statt `pypdf`:

→ `infrastructure/spark/scripts/flora/` und `learning/neuro/README.md`

## Langdock API

In `.env`:

```
LANGDOCK_REGION=eu
ANTHROPIC_API_KEY=<Langdock Token>
ESF_MODEL_HAIKU=claude-haiku-4-5@20251001
ESF_MODEL_SONNET=claude-sonnet-4-6
```

Test:

```powershell
python infrastructure\spark\scripts\esf\esf_local_pipeline.py list-models
python infrastructure\spark\scripts\esf\esf_local_pipeline.py test-auth
```

Doku: https://docs.langdock.com/en/developer/completion-api/anthropic

Spark-Batch (wenn wieder online): `mineru_batch_esf.sh`
