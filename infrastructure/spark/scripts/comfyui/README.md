<!--
last_update: 2026-09-17
status: draft
scope:
  summary: "ComfyUI Setup/Download/Start-Skripte für DGX Spark."
  in_scope:
    - Spark-side scripts
  out_of_scope:
    - LLM serving
notes:
  - "Ops-Doku: ../../comfyui.md"
-->

# ComfyUI scripts (Spark)

Deploy nach `~/ai/scripts/comfyui/` auf Spark, dann:

```bash
bash ~/ai/scripts/comfyui/setup_comfyui.sh
python3 ~/ai/scripts/comfyui/download_image_models.py
bash ~/ai/scripts/comfyui/start_comfyui.sh
```

UI: `http://100.96.115.1:8188` (Tailscale) oder `http://spark-56d0:8188`.
