# LLM-Alternativen für HD-SaaS (Recherche 2025)

Für **strukturierte JSON-Extraktion**, **mehrsprachig** (DE/EN/ZH) und **HD/BaZi-Nischen-Inhalte** auf Spark (SGLang, DGX/GB10).

## Online-Recherche (Kurzfassung)

### Empfohlene 32B-Klasse für unser Setting

| Modell | Vorteile | Nachteile | Status auf Spark |
|--------|----------|-----------|------------------|
| **Qwen3-32B** (aktuell) | Multilingual (100+ Sprachen), JSON/Structured Output, Apache-2.0 | Standard-Alignment | ✅ NVFP4, läuft |
| **DeepSeek R1 8B (abliterated)** | Weniger streng, stabil, BF16 | Kleiner Kontext | ✅ läuft |
| **Phi4-Reasoning** | Starke Reasoning-Baseline, strukturierte Extraktion | ~28G, nicht NVFP4-optimiert | On disk |
| **Qwen3-Coder 30B** | Coding/Struktur-Fokus | Unbekannt für Nischen-Inhalte | On disk |

### Quellen

- SGLang Supported Models: Qwen, Kimi K2, Gemma
- LangStruct: schema-first JSON extraction, model-agnostisch
- DeepSeek R1 vs Qwen3 32B Benchmarks (ArtificialAnalysis, Galaxy.ai)
- Qwen3-32B: 100+ Sprachen, reasoning modes, structured output

### Empfehlung für HD/BaZi

1. **Qwen 32B behalten** als Default – multilingual, bekannt gut, läuft.
2. **DeepSeek R1 8B abliterated** testen, wenn Inhalte zu stark gefiltert werden.
3. **Phi4-Reasoning** als Alternative für bessere JSON-Qualität (falls RAM reicht).

### Nächster Schritt

- A/B-Test: 5–10 gleiche Chunks mit Qwen vs DeepSeek R1 – Qualität vergleichen.
- `HD_LLM_EXTRACTION_URL` auf Spark einfach Port/Modell wechseln (Switch-Workflow).
