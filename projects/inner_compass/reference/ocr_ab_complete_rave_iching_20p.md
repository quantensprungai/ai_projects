---
last_update: 2026-06-29
status: draft
scope:
  summary: "A/B-Vergleich Unlimited-OCR vs MinerU auf 20 Seiten Ra Complete Rave I'Ching."
  in_scope:
    - Laufzeit, Textmenge, Struktur, OCR-Fehler
    - Entscheidungsempfehlung fuer extract_text
  out_of_scope:
    - Worker-Integration
    - Andere Dokumenttypen (BaZi, Scan)
---

# OCR A/B: Complete Rave I'Ching (20 Seiten)

**PDF:** `The Complete Rave I'Ching` (Ra Uru Hu)  
**Spark-Pfad:** `/home/sparkuser/sample_complete_rave_iching.pdf`  
**Datum:** 2026-06-29

| Engine | Output | Laufzeit | Woerter | Bytes |
|---|---|---:|---:|---:|
| Unlimited-OCR | `ocr_spikes/unlimited_ocr/complete_rave_iching_20p/` | 271.5 s | 5650 | 36 580 |
| MinerU (hybrid-auto-engine) | `ocr_spikes/mineru/complete_rave_iching_20p/` | 234.5 s | 4808 | 31 308 |

Lokale Kopien:
- `unlimited_ocr_complete_rave_iching_20p_result.md`
- `mineru_complete_rave_iching_20p_result.md`

## Kurzfazit

**MinerU bleibt Default** fuer diesen Dokumenttyp (digital-born HD-Fach-PDF).

Unlimited-OCR liefert etwas mehr Rohtext, aber mit mehr OCR-Artefakten und schlechterer Markdown-Struktur. MinerU ist schneller, besser fuer Heading-aware Chunking und integriert bereits in die IC-Pipeline.

## Detailvergleich

### Struktur / RAG-Tauglichkeit

| Kriterium | Unlimited-OCR | MinerU |
|---|---|---|
| Ueberschriften | Flach, `<PAGE>`-Marker | Markdown `#`-Headings (Gate, Linien) |
| Index-Seite | Nur Bild-Referenzen | Gate-Nummern als Text extrahiert |
| Tabellen/Layout | Gemischt, teils rohe Det-Tags | Bilder + Textbloecke, konsistenter |
| Chunking | Manuell nachbearbeiten noetig | Direkt heading-aware nutzbar |

### Inhalt / OCR-Qualitaet (Beispiele)

**Gate 1 – Self-Expression**
- Beide: Fliesstext der Gate-Beschreibung gut lesbar.
- Unlimited-OCR: `youngest (six yang lines)` — vermutlich Fehllesung von *yangiest*.
- MinerU: `yangest` — ebenfalls nicht ideal, aber naeher am Original.

**Gate 2 – Higher Knowing**
- Unlimited-OCR: `THE GRATE OF HIGHER KNOWING`, Astrologie `N./W.` statt Gradangaben.
- MinerU: Gate-2-Text korrekt als *receptive* / *Driver* / *Higher Self* erkannt.

**Linien-Kommentare (Exaltation/Detriment)**
- Unlimited-OCR: `Vanus`, `Materials concern das`, `☑`/`②`/`V`-Muell.
- MinerU: Sonderzeichen als `Í p`, `É s`, `Ä p` — nicht ideal, aber Venus/Uranus/Mars meist korrekt im Fliesstext.

**Index**
- MinerU deutlich besser: extrahiert `Gate 25`, `Gate 17`, … als durchsuchbaren Text.
- Unlimited-OCR: Index rein als Bilder.

### Artefakte

| Unlimited-OCR | MinerU |
|---|---|
| `<PAGE>`-Tags | Leerzeichen in `OFTHE`, `OF DEFIANCE` |
| `<\|det\|>title [...]` am Ende | Astrologie-Symbol `ˆ` statt Grad |
| `GRATE` statt `GATE` | Exaltation-Icons als Einzelbuchstaben |

## Entscheidung

| Ergebnis | Aktion |
|---|---|
| MinerU >= Unlimited-OCR auf HD-Ra-PDF | **MinerU bleibt Default** |
| Unlimited-OCR | Nur weiter testen bei **schlechten Scans** oder **Multi-Page-Long-Horizon**-Faellen |

Naechster Spike optional: gleicher Test mit einem **Scan-PDF** oder **BaZi/chinesischem Tabellen-PDF**.

## Reproduktion auf Spark

```bash
# Unlimited-OCR
source ~/srv/unlimited-ocr/.venv/bin/activate
python infrastructure/spark/scripts/ocr/unlimited_ocr_pdf_spike.py \
  --pdf ~/sample_complete_rave_iching.pdf \
  --output-dir ~/ocr_spikes/unlimited_ocr/complete_rave_iching_20p \
  --max-pages 20

# MinerU
source ~/srv/hd-worker/.venv/bin/activate
python infrastructure/spark/scripts/ocr/mineru_pdf_spike.py \
  --pdf ~/sample_complete_rave_iching.pdf \
  --output-dir ~/ocr_spikes/mineru/complete_rave_iching_20p \
  --max-pages 20
```

Vor dem Lauf: SGLang stoppen (`sglang_stop_all.sh`), damit genug VRAM frei ist.
