#!/usr/bin/env python3
"""Download ComfyUI-ready image models onto Spark.

Usage on Spark:
  python3 /home/sparkuser/ai/scripts/comfyui/download_image_models.py
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

from huggingface_hub import hf_hub_download

COMFY_ROOT = Path("/home/sparkuser/ai/comfyui/ComfyUI")
MODELS = COMFY_ROOT / "models"

# dest_subdir is relative to ComfyUI/models/
DOWNLOADS = [
    # FLUX.2 Klein 4B (Apache 2.0) — distilled + base FP8
    (
        "black-forest-labs/FLUX.2-klein-4b-fp8",
        "flux-2-klein-4b-fp8.safetensors",
        "diffusion_models",
    ),
    (
        "black-forest-labs/FLUX.2-klein-base-4b-fp8",
        "flux-2-klein-base-4b-fp8.safetensors",
        "diffusion_models",
    ),
    (
        "Comfy-Org/vae-text-encorder-for-flux-klein-4b",
        "split_files/text_encoders/qwen_3_4b.safetensors",
        "text_encoders",
    ),
    (
        "Comfy-Org/vae-text-encorder-for-flux-klein-4b",
        "split_files/vae/flux2-vae.safetensors",
        "vae",
    ),
    # Z-Image-Turbo (Apache 2.0) — BF16 proven on GB10
    (
        "Comfy-Org/z_image_turbo",
        "split_files/diffusion_models/z_image_turbo_bf16.safetensors",
        "diffusion_models",
    ),
    (
        "Comfy-Org/z_image_turbo",
        "split_files/vae/ae.safetensors",
        "vae",
    ),
    # Qwen-Image-Edit-2511 (Apache 2.0) — FP8 mixed for Spark bandwidth
    (
        "Comfy-Org/Qwen-Image-Edit_ComfyUI",
        "split_files/diffusion_models/qwen_image_edit_2511_fp8mixed.safetensors",
        "diffusion_models",
    ),
    (
        "Comfy-Org/Qwen-Image_ComfyUI",
        "split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors",
        "text_encoders",
    ),
    (
        "Comfy-Org/Qwen-Image_ComfyUI",
        "split_files/vae/qwen_image_vae.safetensors",
        "vae",
    ),
    (
        "lightx2v/Qwen-Image-Edit-2511-Lightning",
        "Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors",
        "loras",
    ),
]


def already_ok(path: Path, min_bytes: int = 1_000_000) -> bool:
    return path.is_file() and path.stat().st_size >= min_bytes


def fetch(repo: str, filename: str, dest_subdir: str) -> Path:
    dest_dir = MODELS / dest_subdir
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / Path(filename).name
    if already_ok(dest):
        print(f"SKIP {dest.name} ({dest.stat().st_size / 1e9:.2f} GB)", flush=True)
        return dest

    print(f"GET  {repo} :: {filename}", flush=True)
    tmp = hf_hub_download(
        repo_id=repo,
        filename=filename,
        local_dir=str(dest_dir / ".hf_tmp"),
    )
    tmp_path = Path(tmp)
    if dest.exists():
        dest.unlink()
    shutil.move(str(tmp_path), str(dest))
    print(f"OK   {dest} ({dest.stat().st_size / 1e9:.2f} GB)", flush=True)
    return dest


def main() -> int:
    MODELS.mkdir(parents=True, exist_ok=True)
    failed: list[str] = []
    for repo, filename, dest_subdir in DOWNLOADS:
        try:
            fetch(repo, filename, dest_subdir)
        except Exception as exc:  # noqa: BLE001 — keep going, report at end
            print(f"FAIL {repo} {filename}: {exc}", flush=True)
            failed.append(f"{repo}/{filename}")
    print("--- done ---", flush=True)
    if failed:
        print("FAILED:", *failed, sep="\n  ", flush=True)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
