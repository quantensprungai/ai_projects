# PDF-Extraktion auf DGX Spark – Optionen

<!--
last_update: 2026-02-04
scope: Analyse externer KI-Empfehlung (MinerU/Docling/Marker) vs. aktueller Stand (PyMuPDF + EasyOCR).
-->

## Ist-Zustand (aktuell im Worker)

- **Text-PDFs:** `extract_text` → PyMuPDF oder **MinerU** (wenn `HD_USE_MINERU=true`) → strukturiertes Markdown → Chunks.
- **Scan-PDFs (ohne MinerU):** Gate „wenig Text“ → Job `extract_text_ocr` → **EasyOCR (GPU)** → Chunks.
- **Mit MinerU:** Ein Pfad für Hybrid-PDFs (Text + Scan), Markdown mit Struktur (Überschriften, Tabellen), bessere RAG-Chunking-Basis.

**MinerU:** Im Worker integriert. Auf Spark: venv mit **`requirements-hd-worker-spark.txt`** einrichten (enthält MinerU); in `.env`: `HD_USE_MINERU=true`. MinerU 2.x: Backend `hybrid` wird im Worker auf `hybrid-auto-engine` gemappt; gültige Werte: `pipeline`, `hybrid-auto-engine`, `hybrid-http-client`, `vlm-auto-engine`, `vlm-http-client`. **Sprache:** `HD_MINERU_LANG=latin` (oder `en`, `ch`) für bessere OCR/Layout. **Chunking:** MinerU-Output wird **heading-aware** gechunkt (##/###-Abschnitte bleiben zusammen), optimal für RAG/LLM-Extraktion.

---

## Externe Analyse (Kurzfassung)

Für **Hybrid-PDFs** (teils Text, teils Scan) wurde empfohlen, kein reines OCR zu nutzen, sondern eine **Document-Pipeline** mit automatischer Erkennung pro Seite:

| Option | Stärken | Aufwand |
|--------|---------|--------|
| **MinerU 2.5** | Auto Text vs. Scan, direkte Extraktion + OCR nur für Scans, VLM für Tabellen/Formeln, 109 Sprachen, CUDA, Markdown/JSON für RAG | `pip install mineru[core]` + ggf. `mineru[vlm]`, PyTorch/CUDA |
| **Docling** | Hybrid Text+OCR, Backends: EasyOCR/Tesseract/RapidOCR, stark bei Tabellen, LangChain/LlamaIndex | Eigenes Setup |
| **Marker** | Surya-basiert, `--force_ocr`, 90+ Sprachen, Markdown+JSON, CUDA | Eigenes Setup |

**DGX Spark:** 128 GB Unified Memory, GB10 Grace Blackwell, ARM – gut für VLM-basierte Ansätze (z. B. MinerU mit VLM-Backend).

**Empfehlung der Analyse:** **MinerU 2.5** als erste Wahl (Hybrid-Backend, ein Tool für Text + OCR + komplexe Layouts).

---

## Einordnung

- **Aktuell:** PyMuPDF + EasyOCR erfüllt „Text-PDF + Scan-PDF → Chunks“ stabil; GPU wird für OCR genutzt.
- **MinerU/Docling/Marker** würden:
  - **Pro:** Eine Pipeline statt zwei (Text + OCR in einem Tool), bessere Layout-Erkennung (Tabellen, Formeln), einheitlicher Output (z. B. Markdown/JSON).
  - **Con:** Neuer Stack, ggf. schwerere Dependencies (VLM), Integration in den bestehenden Worker (Job-Typ, Chunking, DB) nötig.

---

## Was damit machen?

1. **MinerU ist integriert.** Auf Spark: venv mit **`requirements-hd-worker-spark.txt`** (enthält MinerU), in `~/srv/hd-worker/.env`: `HD_USE_MINERU=true`. Dann nutzt der Worker für `extract_text` (PDF) MinerU statt PyMuPDF – strukturiertes Markdown, kein separater `extract_text_ocr`-Pfad für Hybrid-PDFs nötig.
2. **Test:** `mineru -p input.pdf -o output/ -b hybrid --device cuda` (oder `-b pipeline` für CPU).
3. **Env:** `HD_MINERU_BACKEND=hybrid` (Standard), `HD_MINERU_DEVICE=cuda`; für VLM: Backend `vlm-transformers` (höhere Hardware-Anforderungen).

**Zusammenfassung:** MinerU ist im Worker als **optionaler Pfad** für `extract_text` (PDF) umgesetzt. Mit `HD_USE_MINERU=true` und installiertem MinerU auf Spark: ein Tool für Text + OCR + Layout, bessere Basis für RAG/Chunking. Ohne MinerU: weiter PyMuPDF + EasyOCR (extract_text_ocr).

---

## Einbettung im Gesamtprozess (PDF → Cloud → LLM-Extraktion)

| Schritt | Komponente | MinerU-Rolle |
|--------|------------|--------------|
| 1 | App: PDF-Upload | Direkt-Upload in Supabase Storage; Server Action legt Asset, Document, Document_File, **extract_text**-Job an (debug: bucket, path, asset_id, kind=pdf). |
| 2 | Worker: **extract_text** (PDF) | Bei `HD_USE_MINERU=true`: **MinerU** (CLI) → strukturiertes Markdown; sonst PyMuPDF (ggf. Scan-Gate → extract_text_ocr). |
| 3 | Worker: Chunking | MinerU-Output → **heading-aware Chunking** (##/###-Abschnitte); sonst paragraph_accumulate. Chunks → `hd_asset_chunks` (text_clean, metadata mit source/mineru). |
| 4 | Worker: **classify_domain** | Liest Chunks aus `hd_asset_chunks`, klassifiziert system_id (hd/bazi/…), schreibt in Asset-Metadaten. |
| 5 | Worker: **extract_term_mapping** (optional) | Für system=hd: Seed-Term-Mapping. |
| 6 | Worker: **extract_interpretations** | Liest Chunks aus `hd_asset_chunks`, schreibt pro Chunk eine Interpretation in `hd_interpretations`. Bei gesetzter **HD_LLM_EXTRACTION_URL** (z. B. SGLang): echte **LLM-Extraktion** (JSON-Payload); sonst Stub. |

MinerU ist damit **sauber eingebettet**: gleiche Job-Queue, gleiche Tabellen (`hd_asset_chunks`, `hd_interpretations`), gleicher Downstream (classify_domain → extract_interpretations). Der einzige Unterschied: Chunk-Inhalt ist strukturiertes Markdown (Überschriften, Tabellen) und Chunking ist heading-aware – optimal für die spätere LLM-Extraktion.
