<!-- Reality Block
last_update: 2026-01-12
status: stable
scope:
  summary: "Overview of quantization formats used on DGX Spark."
  in_scope:
    - NVFP4
    - FP8
    - MXFP4
    - compatibility notes
  out_of_scope:
    - quantization training workflows
-->

# Quantization Formats (DGX Spark)

## NVFP4 (NVIDIA FP4)
- Optimized for Blackwell architecture  
- 4‑bit weights  
- 8‑bit activations  
- Very fast inference  
- Low VRAM footprint  
- Ideal for Llama‑4‑Scout‑17B  
- Fully supported by SGLang and vLLM

## FP8
- Higher precision  
- Slightly slower than NVFP4  
- Recommended for: reasoning, math, coding  
- Used by some Qwen3 and Phi‑4 variants

## MXFP4
- Mixed 4‑bit format  
- Used by GPT‑OSS‑120B  
- High throughput, large models


