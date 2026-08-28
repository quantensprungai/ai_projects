---
last_update: 2026-08-05
status: active
scope:
  summary: "Ergebnis des ersten MinerU-vs-pypdf-Laufs (Pipeline-Smoke, kein Neuro-Skript)."
---

# Pilot-Vergleich 2026-08-05

**PDF:** `03b_Physiopraxis_2teiler.pdf` (unser generiertes ESF-PDF, 5 Seiten Subset)  
**Zweck:** Pipeline-Smoke auf Spark, nicht Qualitäts-Showdown für Scans.

| Engine | Chars | Zeit | Gerät |
|--------|------:|-----:|-------|
| MinerU | 9375 | 92 s | CPU (GPU von SGLang belegt) |
| pypdf | 8987 | <1 s | CPU |

**Nächster echter Test:** Original-Vorlesungs-PDF Neurologie (gern scan-/tabellenlastig) mit:

```powershell
python infrastructure\spark\scripts\flora\run_extract_on_spark.py `
  --pdf "C:\Pfad\Neuro.pdf" --subject neuro --max-pages 15 --compare --device cpu
```
