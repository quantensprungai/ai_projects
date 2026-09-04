<!--
Reality Block
last_update: 2026-09-04
scope: Ja/Teilweise/Nein an der Handbuch-Karte
in_scope: Tabelle, Granularität, Onboarding
out_of_scope: Trainingsdaten, KG-Knoten-Feedback
-->

# Vertrag: Resonanz

Signal hängt an der **Handbuch-Karte**, nicht am KG-Knoten. Wenige Dutzend `card_key`, nicht Tausende Tore.

**Antworten:** `yes` | `partly` | `no`. Anfangs qualitativ (welcher Satz trifft). Keine Trainingsdaten, keine Scores.

**Tabelle `ic_resonance` (Phase 2):**
- `account_id`, `card_key` (grob: `hd.type`, `hd.strategy`, `astro.asc_house1`, …), `domain`, `system`
- `canonical_ids[]` nur Referenz
- `answer`, `wording_version`, `created_at`
- RLS auf Account

Onboarding-Resonanz (`ic-onboarding-view.tsx`) schreibt in dieselbe Tabelle (`card_key=hd.type`, `domain=self_identity`). UI-Chip `partial` wird als `partly` gespeichert.

**Ist (2026-09-04):** Tabelle + RLS in `apps/web/supabase/migrations/20260904130339_ic_resonance.sql`. Action `karte/bereich/_lib/resonance-action.ts`. Append-only, `account_id` kommt vom Server, nicht vom Client.
