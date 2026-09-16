<!--
Reality Block
last_update: 2026-09-16
scope: Was darf Handbuch-Prosa sein
in_scope: UI-Tauglichkeit, Gate in domain-assemble
out_of_scope: System-Chart-Inspector (bleibt wie er ist)
-->

# Vertrag: Status

Policy (Soll): `blocked` | `canon_fallback` | `synth_draft` | `verified` — siehe `synthesis_canon_first.md`.

**Ist:** `sys_synthesis_wordings` hat **keine** Status-Spalte. Worker schreibt `account_id, node_id, canonical_id, language, version, canonical_description, canonical_wording, styles`.

**Gate im Slice (Phase 2):** nur `lib/ic/domain-assemble.ts`. System-Charts unverändert.
- UI-tauglich: `language='de'` **oder** explizite Allowlist (HD-Keil) **oder** vorgeschriebene Färbungskarte in `handbook-voice.ts` (Decision 2026-09-16: Identität + Liebe, inkl. HD/BaZi-OS auf Liebe).
- `synth_draft` EN: Lage-Satz + sichtbarer Entwurfs-Hinweis, nie Handbuch-Absatz.
- Nichts da: Leerfall — ein Satz, welches System hier schweigt und warum. Keine erfundene Prosa.

**Schuld:** Spalte `synthesis_status` als spätere Migration. Nicht im Slice erfinden.

**Ist (Plan 04 Todo 3, 2026-09-15):** Gate hält EN-Absätze. Tiefe 2 liest Familie 4, nicht `uiReady`-Zählung. Lage-Sätze dürfen ins Treffen. `synthesis_status`-Spalte nicht angelegt.
