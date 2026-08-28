---
last_update: 2026-08-05
status: active
scope:
  summary: "Flora Lernfach Neurologie — Ingest mit MinerU auf Spark, danach Canon/Story wie ESF."
---

# Neurologie (Flora) — Setup

## Pipeline (kurz)

```
Vorlesungs-PDF
  → MinerU auf Spark (strukturiertes Markdown)
  → source/*.md
  → Canon (Dozentin/Prüfungsthemen)
  → Module / Geschichte / PDF für iPad
```

**Nicht:** MinerU als Flora-UI. Nur Extraktion.

## Extract (MinerU)

Voraussetzung: Spark `sparkuser@100.96.115.1:2222`, MinerU in `~/srv/hd-worker/.venv`.

Von Repo-Root (Windows):

```powershell
python infrastructure\spark\scripts\flora\run_extract_on_spark.py `
  --pdf "C:\Pfad\zu\Neuro_Skript.pdf" `
  --subject neuro `
  --max-pages 15 `
  --compare
```

Ergebnis:

- `source/<stem>.md` — MinerU
- `source/<stem>_pypdf.md` — Vergleich (wenn `--compare`)
- `source/<stem>_mineru_meta.json` — Laufzeit/Backend

Direkt auf Spark:

```bash
~/srv/hd-worker/.venv/bin/python \
  ~/ai_projects/infrastructure/spark/scripts/flora/extract_lecture_pdf.py \
  --pdf Vorlesung.pdf --out ~/flora_extract/out --engine mineru --max-pages 12
```

## Ordner

| Pfad | Zweck |
|------|--------|
| `source/` | Rohextrakt (MinerU) |
| `modules/` | Kuratierte Kapitel (später) |
| `reader/` | Flora-PDFs (später) |
| `geschichte/` | Story-Pilot (optional, wie ESF) |

## Hinweise

- **GPU:** Auf Spark läuft oft SGLang (~100 GB VRAM). Extract-Default ist deshalb **`--device cpu`**. Wenn die GPU frei ist: `--device cuda`.
- Bild-/Scan-lastig → `--method ocr`
- Text-PDF mit Layout → `--method auto` (Default)
- Erst **Pilot** (15–20 Seiten) gegen pypdf vergleichen, dann volles Skript
- Prüfungs-Canon vor LLM-Modulen festlegen (wie `esf/PRUEFUNGS_CANON.md`)
