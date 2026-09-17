<!--
last_update: 2026-09-17
status: draft
scope:
  summary: "ComfyUI auf DGX Spark: Installation, Bildmodelle, GPU-Sharing, Zugriff."
  in_scope:
    - ComfyUI layout and start/stop
    - first-wave image models (FLUX.2 Klein 4B, Z-Image-Turbo, Qwen-Image-Edit-2511)
    - ports and GPU contention with SGLang/MinerU
  out_of_scope:
    - LLM serve scripts
    - secrets / HF token values
notes:
  - "Playbook-Basis: ~/dgx-spark-playbooks/nvidia/comfy-ui (NVIDIA, CUDA 13)."
  - "Kein SD 1.5 als Default; erste Welle sind die drei Apache-2.0-Modelle."
-->

# ComfyUI auf Spark (Bildmodelle)

## Ziel

Lokale Bildgenerierung und -bearbeitung auf Spark-56d0 (GB10, 128 GB UMA) über ComfyUI.

NVIDIA-Playbook bleibt die Install-Basis (venv + PyTorch cu130 + `ComfyUI` + `--listen 0.0.0.0`). Wir legen die Installation unter `~/ai/comfyui/` statt ins Home-Root und ziehen **nicht** SD 1.5 als Default.

## GPU-Sharing (wichtig)

Auf 128 GB UMA läuft **ein** schwerer GPU-Dienst sauber:

| Dienst | Port | Gleichzeitig mit ComfyUI? |
|---|---:|---|
| ComfyUI | `8188` | — |
| SGLang | `30000` / `30001` | **nein** (vorher `sglang_stop_all.sh`) |
| MinerU / IC-Worker extract | lokal | **nein** (S5 Zwei-Phasen-Regel) |
| Ollama | `11434` | klein ok (`llama3.1:8b`); bei Engpässen stoppen |

## Layout auf Spark

```text
~/ai/comfyui/comfyui-env/     # venv, torch cu130
~/ai/comfyui/ComfyUI/         # App + models/
~/ai/scripts/comfyui/         # setup / download / start / stop
~/ai/logs/comfyui/            # comfyui.log, pid
```

Skripte im Repo: `infrastructure/spark/scripts/comfyui/`.

## Erste Modellwelle (Apache 2.0)

| Modell | Dateien (ComfyUI-Ordner) | Wofür |
|---|---|---|
| **FLUX.2 Klein 4B** distilled + base FP8 | `diffusion_models/flux-2-klein-4b-fp8.safetensors`, `flux-2-klein-base-4b-fp8.safetensors`; `text_encoders/qwen_3_4b.safetensors`; `vae/flux2-vae.safetensors` | Allround, Edit, Referenzbilder |
| **Z-Image-Turbo** BF16 | `diffusion_models/z_image_turbo_bf16.safetensors`; shared `qwen_3_4b`; `vae/ae.safetensors` | schnelle Entwürfe (~7–12 s / 1024² auf Spark) |
| **Qwen-Image-Edit-2511** FP8 mixed | `diffusion_models/qwen_image_edit_2511_fp8mixed.safetensors`; `text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors`; `vae/qwen_image_vae.safetensors`; LoRA Lightning 4-step | Foto-Edit, Identität, Text im Bild |

Templates in der ComfyUI-UI (nach aktuellem `git pull`): Flux.2 Klein, Z-Image-Turbo, Qwen-Image-Edit-2511.

## Zugriff

- Lokal auf Spark: `http://127.0.0.1:8188`
- Tailscale: `http://100.96.115.1:8188` bzw. `http://spark-56d0:8188`
- Health: `curl -I http://127.0.0.1:8188`

## Start / Stop (ohne sudo)

```bash
bash ~/ai/scripts/comfyui/start_comfyui.sh
bash ~/ai/scripts/comfyui/stop_comfyui.sh
```

## Legacy `hd-worker` (Crash-Loop)

`hd-worker.service` startet `hd_worker_mvp.py` gegen eine tote lokale Supabase (`hd_ingestion_jobs` 404) und restartet dauernd. Stoppen braucht sudo:

```bash
sudo systemctl stop hd-worker.service
sudo systemctl disable hd-worker.service
```

Inner Compass nutzt **`ic_worker.py`**, nicht diesen Dienst.
