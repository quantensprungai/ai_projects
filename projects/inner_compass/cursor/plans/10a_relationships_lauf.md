<!--
Reality Block
last_update: 2026-09-17
scope: Phasen-Plan 10a — extract_relationships Lauf, nach Schema Plan 10
in_scope: LLM-Lauf auf HD-Chunks Login-OS + Mechanik-Hit, 3–5 Charts, candidate-Kanten mit condition + interp_id
out_of_scope: Formulierer (Plan 11), Backfill-Wipe, Jiazi, 418, DE-Gate, Fläche, Worker-Prio dauerhaft ohne Review
-->

# Plan 10a — Relationships-Lauf

Selbsttragend. Warum jetzt: Plan 10 hat `HandbookInput` und das Schicht-2-Schema. Der Job existiert im Worker noch nicht. Backfill bleibt ungelesen.

**Matrix-Zelle:** HD × Schicht-2-Literaturkanten (`candidate`, mit `condition` + Interp-ID). Vertrag: [../vertraege/tiefe.md](../vertraege/tiefe.md). Spec: [../pipeline.md](../pipeline.md) `extract_relationships`.

Code-Repo: `code/inner_compass_app`, Branch `cursor/astro-natal`.

## These

Eine Kante pro Beleg aus Chunk + `elements[]`. `review_status=candidate`. Nicht der Backfill. Nicht die Fläche.

## Reihenfolge

1. Job in Worker (einmalig, nicht `_JOB_PRIORITY` dauerhaft ohne Review) — *(D)*
2. Lauf: HD-Chunks Login-OS-Knoten + Mechanik-Hit, 3–5 Charts, Langdock `gpt-5.4-mini` — *(D)*
3. Stichprobe: Kante hat `metadata.condition`, `metadata.interp_id`, `evidence.chunk_id` + Zitat — *(D)*
4. Review 10a — *(S)*

## Nicht

Formulierer, Backfill auf `approved`, Wipe, Jiazi, 418, EN auf der Fläche.
