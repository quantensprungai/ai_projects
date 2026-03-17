#!/usr/bin/env python3
"""Download Llama 3.1 8B and 3.2 11B to Spark. Run on Spark: python3 download_llama_models.py"""
from huggingface_hub import snapshot_download

BASE = "/home/sparkuser/ai/models/llama"

print("Downloading Llama 3.1 8B Instruct...")
snapshot_download("meta-llama/Llama-3.1-8B-Instruct", local_dir=f"{BASE}/llama-3.1-8b-instruct")
print("Llama 3.1 8B done.")

print("Downloading Llama 3.2 11B Instruct...")
snapshot_download("meta-llama/Llama-3.2-11B-Instruct", local_dir=f"{BASE}/llama-3.2-11b-instruct")
print("Llama 3.2 11B done.")
