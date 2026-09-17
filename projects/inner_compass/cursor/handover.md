<!--
Reality Block
last_update: 2026-09-17
scope: Chat-Handover Inner Compass, kurz
in_scope: Einstieg für neuen Chat
out_of_scope: Historie (siehe reference/handover_2026-09_archiv.md)
-->

# Inner Compass — Handover

Neuer Chat: zuerst [roadmap.md](roadmap.md) lesen, dann den dort verlinkten Phasen-Plan. Nordstern: [nordstern.md](nordstern.md).

```
Projekt: Inner Compass
Docs: projects/inner_compass/   Code: code/inner_compass_app/  (eigenes Git)
Branch: cursor/astro-natal in beiden. Kein Merge main, kein Force-Push, kein supabase db reset.
Anker: cursor/roadmap.md → Phasen-Plan. Verträge: cursor/vertraege/. Decisions: reference/decisions.md.
Login: test@makerkit.dev / testingpassword · Geburten im Slice: 1980-11-18 und 1978-11-10, 19:20 Berlin
Lokal: Next :3000, Supabase API :54321, HD-Service :8002 (services/hd)
LLM: Langdock gpt-5.4-mini (Pin in der App noch offen). Nicht Spark-Qwen als Interpret/Synth. Key in .env.development.local (nicht committen).
```

**Stand:** Track Tiefe. Phase 9 zu. Sprachregel: EN = Rohstoff, DE wird formuliert ([tiefe.md](vertraege/tiefe.md)). **Nächster Plan:** [plans/10_facetten_schicht2.md](plans/10_facetten_schicht2.md) — `HandbookInput` bauen, Schicht-2-Spec, kein LLM, kein DE-Gate. Lauf = 10a. Jiazi nicht parallel. Verbreitung: Namen kanonisch, Handles reservieren, keine Posts.

**Leitplanken:** nested Code nicht ins Docs-Repo. Flora/`.env`/`_tmp_*` nicht committen. HD-Zombie `5ba2f841` nicht anfassen. Auto-Synth aus. Handbuch-Text formulieren, nicht übersetzen. Seed vor text2kg.

**Alte Fläche:** Overlay-Vertrag `reference/hd_bodygraph_overlay_contract.md`. Pipeline-Wörter `pipeline.md` §1a. Archiv-Handover: [reference/handover_2026-09_archiv.md](reference/handover_2026-09_archiv.md).
