---
last_update: 2026-06-25
status: draft
scope:
  summary: "Spike-Runbook fuer baidu/Unlimited-OCR als moegliches OCR-Backend neben MinerU."
  in_scope:
    - Spark-seitiger Setup- und Testpfad
    - Vergleich gegen MinerU auf repräsentativen PDFs
    - Entscheidungskriterien fuer IC extract_text
  out_of_scope:
    - Produktive Worker-Integration
    - Ersatz von MinerU ohne Benchmark
    - VM102/AA-Download-Betrieb
notes:
  - "Unlimited-OCR ist MIT-lizenziert, nutzt aber trust_remote_code=True; deshalb isoliert testen."
  - "Ort fuer den Spike: Spark. VM105 orchestriert/Supabase; VM102 beschafft und uploaded."
---

# Unlimited-OCR Spike Runbook

## Entscheidung vorab

`baidu/Unlimited-OCR` wird **nicht** direkt produktiv aktiviert. Es ist ein
OCR/Document-Parsing-Kandidat fuer schwierige Scans und lange PDFs. MinerU bleibt
der Default fuer `extract_text`, bis dieser Spike bessere Ergebnisse zeigt.

## Topologie

| Komponente | Rolle |
|---|---|
| VM105 | Repo, Supabase/Dev, Orchestrierung, Vergleichsauswertung |
| VM102 | Anna's Archive Download + `--sys-mode` Upload |
| Spark | GPU-Runtime fuer MinerU, Unlimited-OCR und LLM |

## Setup auf Spark

```bash
cd ~/ai_projects
bash infrastructure/spark/scripts/ocr/unlimited_ocr_setup.sh
```

Das Script legt standardmaessig `~/srv/unlimited-ocr/.venv` an. Die Umgebung ist
absichtlich getrennt vom MinerU-/Worker-venv.

## Einzelnen PDF-Spike laufen lassen

```bash
source ~/srv/unlimited-ocr/.venv/bin/activate

python infrastructure/spark/scripts/ocr/unlimited_ocr_pdf_spike.py \
  --pdf /path/to/sample.pdf \
  --output-dir ~/ocr_spikes/unlimited_ocr/sample \
  --max-pages 20
```

`--max-pages` ist fuer Smoke-Tests wichtig. Fuer den finalen Vergleich pro Werk
kann das Limit entfernt werden.

## Vergleichsset

Mindestens diese Dokumenttypen testen:

| System | Zweck |
|---|---|
| HD / Ra | englische Fach-PDFs, viele Begriffe und Tabellen |
| I Ching | klassische Textstruktur, Linien/Hexagramme |
| BaZi | chinesische Schrift + Tabellen |
| Jyotish | Sanskrit/Diakritika + astrologische Tabellen |
| Kabbalah | Hebraeische Begriffe, gemischte Umschrift |
| Schlechter Scan | OCR-Robustheit |

## Bewertung

Pro PDF gegen MinerU vergleichen:

- Textvollstaendigkeit
- Heading-/Kapitelstruktur
- Tabellen und Listen
- Seiten-/Abschnittsreihenfolge
- Unicode/Diakritika/chinesische Zeichen
- Halluzinationen oder hinzugefuegte Zwischenueberschriften
- Laufzeit
- GPU-Speicherbedarf
- Eignung fuer 500-1000-Token-Chunks

## Entscheidung

| Ergebnis | Aktion |
|---|---|
| MinerU besser/gleich gut | MinerU bleibt Default; Unlimited-OCR nur dokumentieren. |
| Unlimited-OCR besser bei Teilklassen | Optionales Backend fuer diese Dokumentklasse vorsehen. |
| Unlimited-OCR deutlich besser allgemein | Worker-Integration planen: `IC_OCR_ENGINE=mineru|unlimited_ocr`. |

## Spaetere Worker-Integration

Wenn der Spike erfolgreich ist, sollte die produktive Einbindung nicht die
Dateiablage aendern. Stattdessen:

```text
sys_sources
  -> extract_text job
     -> OCR backend via env/config:
        IC_OCR_ENGINE=mineru
        IC_OCR_ENGINE=unlimited_ocr
```

Die PDF wird weiterhin einmal uploaded. K2/K3/K4-Paesse laufen danach auf den
Chunks, nicht auf separaten Dateikopien.
