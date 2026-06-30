---
last_update: 2026-06-29
status: draft
scope:
  summary: "A/B-Vergleich Unlimited-OCR vs MinerU: BaZi (三命通会) und Scan (Parasara Hora Sastra)."
  in_scope:
    - Laufzeit, Textqualitaet, Halluzinationen, Struktur
    - Gesamtentscheidung fuer extract_text
  out_of_scope:
    - Worker-Integration
---

# OCR A/B: BaZi + Scan (je 20 Seiten)

**Datum:** 2026-06-29  
**Spark-PDFs:**
- BaZi: `/home/sparkuser/sample_bazi_sanming.pdf` (三命通会 上, 26 MB)
- Scan: `/home/sparkuser/sample_scan_parasara1.pdf` (Brihat Parasara Hora Sastra 1, 11 MB)

## Ergebnisse

### BaZi — 三命通会 上 (chinesisch, gemischt digital/klassisch)

| Engine | Laufzeit | Bytes | Qualitaet |
|---|---:|---:|---|
| Unlimited-OCR | 279.8 s | 43 045 | Frontmatter ok, klassische Seiten mit Halluzinationen |
| MinerU (`--lang ch`) | **172.4 s** | 40 274 | **Deutlich besser** — Fliesstext + BaZi-Fachinhalt |

**MinerU:** Extrahiert CIP, Vorwort, 前言, lange Abschnitte zu 李虚中/徐子平/万民英, 纳音, 用神, 格局 — durchsuchbar und chunkbar.

**Unlimited-OCR:** Auf „古书版样“-Seiten Wiederholungen (`王世平等点`), `[Unreadable]`-Spam, rohe `<|det|>`-Tags, teils komplett fehlende Seiteninhalte.

### Scan — Brihat Parasara Hora Sastra Vol. 1 (1984, OCR-lastig)

| Engine | Laufzeit | Bytes | Woerter (wc) | Qualitaet |
|---|---:|---:|---:|---|
| Unlimited-OCR | 479.2 s | 89 433 | 13 005 | Inhalt + massiver Muell |
| MinerU (`--lang latin`) | **107.2 s** | 28 829 | 4 562 | **Nutzbare Struktur** |

**MinerU:** Titelseite, Inhaltsverzeichnis, Kapitelueberschriften sauber; leichte OCR-Typo (`famons`, `Pbysical`, `ŠIGNS`).

**Unlimited-OCR:** TOC und fruehe Seiten brauchbar; ab ~Seite 17 hunderte Wiederholungen von `The image is too blurry to recognize any text content.` — **nicht pipeline-tauglich**.

## Gesamtentscheidung (3 Tests)

| Dokumenttyp | Gewinner |
|---|---|
| HD digital-born (Ra I'Ching) | MinerU |
| BaZi chinesisch (三命通会) | MinerU |
| Jyotish-Scan (Parasara) | MinerU |

**Unlimited-OCR:** Spike abgeschlossen, **kein produktiver Ersatz**. Bei schwierigen Scans ggf. MinerU-Tuning (`--lang`, Backend) oder separater EasyOCR-Pfad pruefen — nicht Unlimited-OCR out of the box.

## Reproduktion

PDFs von **VM105 (PowerShell)** nach Spark — nicht von Spark aus:

```powershell
$bazi = (Get-ChildItem "C:\Users\Admin105\Downloads\Literatur\bazi" -Filter "*5793f92af01976a8bd9a6c85a6a3e0e2*.pdf").FullName
$scan = (Get-ChildItem "C:\Users\Admin105\Downloads\Literatur\jyotish" -Filter "*8d0c28cbdc3327fdb3737efba478b3a3*.pdf").FullName
scp -P 2222 -O "$bazi" sparkuser@spark-56d0:/home/sparkuser/sample_bazi_sanming.pdf
scp -P 2222 -O "$scan" sparkuser@spark-56d0:/home/sparkuser/sample_scan_parasara1.pdf
```

Spark-Laeufe siehe `ocr_ab_complete_rave_iching_20p.md` (MinerU BaZi mit `--lang ch`).

Lokale Ergebnisse:
- `mineru_bazi_sanming_20p_result.md`
- `unlimited_ocr_bazi_sanming_20p_result.md`
- `mineru_scan_parasara1_20p_result.md`
- `unlimited_ocr_scan_parasara1_20p_result.md`
