<!--
Reality Block
last_update: 2026-09-17
scope: Phasen-Plan 10a — extract_relationships Lauf, nach Schema Plan 10
in_scope: LLM-Lauf auf HD-Chunks Login-OS + Mechanik-Hit, 3–5 Charts, candidate-Kanten mit condition + interp_id
out_of_scope: Formulierer (Plan 11), Backfill-Wipe, Jiazi, 418, DE-Gate, Fläche, Worker-Prio dauerhaft ohne Review
-->

# Plan 10a — Relationships-Lauf

Selbsttragend. Warum jetzt: Plan 10 hat `HandbookInput` und das Schicht-2-Schema. Der Job existierte im Worker nicht. Backfill bleibt ungelesen.

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

## Ist (2026-09-17)

Handler `_handle_extract_relationships` in `apps/web/scripts/ic_worker.py`. Nicht in `_JOB_PRIORITY`. Claim nur mit `IC_WORKER_JOB_TYPES=extract_relationships`. Chunk-Auswahl: `primary` → `contrast` → ohne Rolle, `mention` raus, Cap 15/Node, Chunks global dedupliziert. Kanten: `edge_scope=intra_system`, `review_status=candidate`, `metadata.run=plan_10a`. Backfill (`metadata.source=interactions_backfill_2026-08-05`) unangetastet.

**Scopes (echte Charts, nicht Plan-10-Minimal-Fixture):**

| Chart | Herkunft | OS + Hit |
|---|---|---|
| 1978-11-10 | `user_charts` | Generator, wait_to_respond, emotional, `hd.channel.59_6` defined |
| 1980-11-18 19:20 Berlin | HD-Service `:8002` | Projector, wait_for_invitation, splenic, `hd.channel.10_57` defined |
| 1990-06-15 14:30 Berlin | HD-Service `:8002` | Manifesting Generator, wait_to_respond, sacral, `hd.channel.13_33` defined |

Plan-10-Fixture (Kanal 8–1 / hängendes Tor 1) bleibt synthetisch und war nicht der Lauf-Scope.

**Jobs (completed, 0 LLM-Fail):**

- `3e923cdc-3a1e-47c0-b867-cad7a1c986d6` 1978 — 60 Chunks, written 276
- `8d2d098a-6872-4d2a-b416-795c9b216da0` 1980 — 60 Chunks, written 309
- `1b32ebdf-9b29-4048-b634-f07be8a453a6` 1990 — 60 Chunks, written 284

**Bestand `metadata.run=plan_10a`:** 869 Kanten. `depends_on` 314, `modifies` 194, `produces` 146, `amplifies` 113, `controls` 54, `clashes_with` 48. `condition`: defined 411, none 408, undefined 44, split 6, hanging 0. Fehlende `condition` / `interp_id` / `chunk_id` / Zitat: 0. `amplifies`+`clashes_with` gleiches Paar: 7 (Leseregel: beide stumm, sobald Schicht 2 gelesen wird). Stichprobe 10: 8/10 Zitate wörtlich im Chunk (2 Paraphrase/OCR-Tabelle).

Modell: Langdock `gpt-5.4-mini` (Pin bestätigt, Testcall `pong`). ~180 LLM-Calls. Kosten nicht aus dem Langdock-Konto gelesen.

Fläche unverändert. Formulierer liest diese Kanten noch nicht.
