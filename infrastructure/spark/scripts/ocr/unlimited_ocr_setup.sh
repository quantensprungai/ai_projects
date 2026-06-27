#!/usr/bin/env bash
set -euo pipefail

# Spark-only setup for Baidu Unlimited-OCR.
# Keep this environment separate from MinerU and the IC worker venv so the
# experiment cannot disturb the productive extract_text path.

INSTALL_DIR="${UNLIMITED_OCR_HOME:-$HOME/srv/unlimited-ocr}"
PYTHON_BIN="${PYTHON_BIN:-python3.12}"

mkdir -p "$INSTALL_DIR"
cd "$INSTALL_DIR"

if ! command -v uv >/dev/null 2>&1; then
  echo "uv is required. Install it first: https://docs.astral.sh/uv/"
  exit 1
fi

uv venv --python "$PYTHON_BIN" .venv
source .venv/bin/activate

uv pip install \
  "torch==2.10.0" \
  "torchvision==0.25.0" \
  "transformers==4.57.1" \
  "Pillow==12.1.1" \
  "matplotlib==3.10.8" \
  "einops==0.8.2" \
  "addict==2.4.0" \
  "easydict==1.13" \
  "pymupdf==1.27.2.2" \
  "psutil==7.2.2" \
  "accelerate"

python - <<'PY'
import torch
print("cuda_available=", torch.cuda.is_available())
if torch.cuda.is_available():
    print("device=", torch.cuda.get_device_name(0))
PY

echo "Unlimited-OCR venv ready at: $INSTALL_DIR/.venv"
