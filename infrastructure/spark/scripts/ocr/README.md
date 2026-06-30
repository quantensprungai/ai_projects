# OCR Spikes on Spark

This folder contains isolated OCR experiments for Inner Compass. The production
`extract_text` path remains MinerU until a candidate is benchmarked and wired
into the worker deliberately.

## Unlimited-OCR

`baidu/Unlimited-OCR` is a 3B BF16 document parsing model. Use it on Spark, not
VM105 or VM102:

- VM105: orchestration, Supabase, local dev.
- VM102: Anna's Archive downloads/uploads.
- Spark: GPU OCR/LLM runtime.

## Files

- `unlimited_ocr_setup.sh` creates a dedicated virtualenv and installs the
  tested dependencies from the model card.
- `unlimited_ocr_pdf_spike.py` runs a single PDF through Unlimited-OCR and writes
  model outputs into a chosen output directory.

## Minimal flow on Spark

```bash
cd ~/ai_projects
bash infrastructure/spark/scripts/ocr/unlimited_ocr_setup.sh

source ~/srv/unlimited-ocr/.venv/bin/activate
python infrastructure/spark/scripts/ocr/unlimited_ocr_pdf_spike.py \
  --pdf /path/to/sample.pdf \
  --output-dir ~/ocr_spikes/unlimited_ocr/sample
```

MinerU spike (same interface):

```bash
source ~/srv/hd-worker/.venv/bin/activate
python infrastructure/spark/scripts/ocr/mineru_pdf_spike.py \
  --pdf /path/to/sample.pdf \
  --output-dir ~/ocr_spikes/mineru/sample \
  --max-pages 20
```

Compare the result against the same PDF processed by Unlimited-OCR before changing the
worker.
