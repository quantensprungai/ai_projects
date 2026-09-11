<!--
Reality Block
last_update: 2026-09-11
scope: Laufender Anker — Phasen, Status, nächster Plan
in_scope: Reihenfolge, Status, Links
out_of_scope: Implementierungsdetails (stehen im Phasen-Plan)
-->

# Roadmap

Jeder neue Chat liest zuerst diese Datei, dann den verlinkten Phasen-Plan. Cursor-Plan-Dateien unter `.cursor/plans/` sind Duplikate.

**Arbeitsweise:** Innerhalb einer Phase Todos abarbeiten *(D)* schwächeres Modell, *(S)* starkes. Am Ende **Phasen-Review** *(S)*: Verträge gegen Code, Offenes zurückschreiben, Decision, nächsten Plan ausarbeiten — erst dann bauen.

| Phase | Status | Ziel | Plan |
|---|---|---|---|
| 0 Git-Hygiene | abgeschlossen 2026-09-04 | Auth-Docs + Relink-Skript auf `cursor/astro-natal`. HD-Pipeline-Skripte (`ic_hd_*`, `ic_s0_*`, `ic_start_langdock_worker.py`) bleiben untracked — zu viele, unreviewed. Astro-Working-Tree uncommitted gelassen. | — |
| 1 Nordstern + Rules | abgeschlossen 2026-09-04 | Dünnes Set, Rules als Leitplanken, Handover 60 Zeilen. Abweichungen: kein `AGENTS.md` im Code-Repo (nichts angelegt); HD-Pipeline-Skripte weiter untracked. | [plans/01_nordstern.md](plans/01_nordstern.md) |
| 2 `self_identity` vertikal | abgeschlossen 2026-09-11 | Eine Domäne echt: Kanten, Status-Gate, Resonanz, Handbuch-Stimme, Seite | [plans/02_self_identity.md](plans/02_self_identity.md) |
| 3 BaZi-Content | offen — nächster Bau | Seed vor Ingest, Langdock, kein Auto-Synth. Unabhängigkeitsbeleg + Chart-First-Cut. ZEIT bleibt Stub. | [plans/03_bazi.md](plans/03_bazi.md) |
| 4 Cross-Kanten | offen | `converges` / `complements` / `contradicts` pro Element-Paar in einer Domäne | nach Review 3 |
| 5 Werkstatt | offen | Tiefe 3–4 aus `payload.process`. Tor existiert in Phase 2 (Retrieval Typ→Strategie→Autorität noch nachziehen). | nach Review 3 |
| 6 Mandala + 11 Bereiche | offen | Chart-Belegung, nicht Katalog-Occupancy. Dann restliche Domänen. Worker-Enums 10→12 vorher. | nach Review 3 |
| 7 Verbreitung | offen | Mandala-Share, Serie/Botschafter, Social, Agent-Surface. Nicht vor Fläche. | nach Review 3 |

**Offenes (mitgeschleppt):** Worker-Prompt alte 10 Domänen-Enums → `exchange_learning`/`transformation_renewal` ohne Payload-Tags. Angleichen vor Phase 6, kein Re-Synth. Familie-2-Backfill: Widerspruchsfilter + Fan-out-Dedup vor Nutzung. 3–5 qualitative Charts jederzeit, blockieren nicht. Hub-Hydration `ic-karte-hub-view.tsx`. Assemble-Fallback für `experiment_seed` (Typ→Strategie→Autorität) beim nächsten Touch von `domain-assemble.ts`.

**Nicht-Ziele:** Merge `main`, Force-Push, `supabase db reset`, Re-Synth, Spark-Qwen als Interpret, HD-Zombie `5ba2f841`, Flora/`.env`/`_tmp_*`, next-intl-Welle, Jyotish/Maya-UI, zwölf Bereichsseiten vor Phase 6, Luck-Pillar-UI in Phase 3.

**Nordstern:** [nordstern.md](nordstern.md). **Verträge:** [vertraege/](vertraege/).
