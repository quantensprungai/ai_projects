#!/bin/bash
# Install ComfyUI on DGX Spark (NVIDIA playbook + CUDA 13 / GB10).
# Layout: ~/ai/comfyui/{comfyui-env,ComfyUI}
set -euo pipefail

ROOT="${HOME}/ai/comfyui"
LOG_DIR="${HOME}/ai/logs/comfyui"
mkdir -p "$ROOT" "$LOG_DIR"

python3 --version
python3 -m venv "${ROOT}/comfyui-env"
# shellcheck disable=SC1091
source "${ROOT}/comfyui-env/bin/activate"
python -m pip install -U pip wheel

echo "Installing PyTorch CUDA 13.0 (aarch64 / GB10)..."
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu130

if [ ! -d "${ROOT}/ComfyUI/.git" ]; then
  if [ -d "${ROOT}/ComfyUI" ]; then
    echo "ComfyUI exists without git — moving aside"
    mv "${ROOT}/ComfyUI" "${ROOT}/ComfyUI.bak.$(date +%s)"
  fi
  git clone https://github.com/comfyanonymous/ComfyUI.git "${ROOT}/ComfyUI"
else
  git -C "${ROOT}/ComfyUI" pull --ff-only || true
fi

python -m pip install -r "${ROOT}/ComfyUI/requirements.txt"
# requirements.txt may pull a generic torch; pin CUDA 13 again
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu130

if [ ! -d "${ROOT}/ComfyUI/custom_nodes/ComfyUI-Manager/.git" ]; then
  git clone https://github.com/Comfy-Org/ComfyUI-Manager.git \
    "${ROOT}/ComfyUI/custom_nodes/ComfyUI-Manager"
fi

mkdir -p \
  "${ROOT}/ComfyUI/models/checkpoints" \
  "${ROOT}/ComfyUI/models/diffusion_models" \
  "${ROOT}/ComfyUI/models/text_encoders" \
  "${ROOT}/ComfyUI/models/vae" \
  "${ROOT}/ComfyUI/models/loras"

python - <<'PY'
import torch
print("torch", torch.__version__, "cuda", torch.version.cuda, "available", torch.cuda.is_available())
assert torch.cuda.is_available(), "CUDA not available in ComfyUI venv"
print("device", torch.cuda.get_device_name(0))
PY

echo "ComfyUI setup OK. Start with: bash ${HOME}/ai/scripts/comfyui/start_comfyui.sh"
