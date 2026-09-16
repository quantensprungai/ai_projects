<!--
Reality Block
last_update: 2026-09-16
scope: Ja/Teilweise/Nein an der Handbuch-Karte
in_scope: Tabelle, Granularität, Onboarding
out_of_scope: Trainingsdaten, KG-Knoten-Feedback
-->

# Vertrag: Resonanz

Signal hängt an der **Handbuch-Karte**, nicht am KG-Knoten. Wenige Dutzend `card_key`, nicht Tausende Tore.

**Antworten:** `yes` | `partly` | `no`. Anfangs qualitativ (welcher Satz trifft). Keine Trainingsdaten, keine Scores.

**Tabelle `ic_resonance` (Phase 2):**
- `account_id`, `card_key` (grob: `hd.type`, `hd.strategy`, `astro.asc_house1`, `astro.house7`, `ziwei.life_palace`, `ziwei.spouse_palace`, …), `domain`, `system`
- `canonical_ids[]` nur Referenz
- `answer`, `wording_version`, `created_at`
- RLS auf Account

Onboarding-Resonanz (`ic-onboarding-view.tsx`) schreibt in dieselbe Tabelle (`card_key=hd.type`, `domain=self_identity`). UI-Chip `partial` wird als `partly` gespeichert.

Plan 05: Werkstatt **liest** ob mindestens eine Resonanz auf `self_identity` existiert (Tür). Inhalt hängt nicht an der Anzahl. `no` öffnet genauso. Keine zweite Scoreschicht.

**Ist (2026-09-11):** Tabelle + RLS in `20260904130339_ic_resonance.sql`. Owner-Fix `20260911113000_ic_resonance_owner_rls.sql`. Action `karte/bereich/_lib/resonance-action.ts`. Append-only. Tags ohne CHECK; Validierung in `lib/ic/resonance.ts`. Browser: Insert `201` (`hd.type` / `yes`) nach dem Fix.

**Ist (2026-09-16):** Keys `astro.house7`, `ziwei.spouse_palace` für Liebe. Onboarding bleibt `hd.type` / `self_identity`.
