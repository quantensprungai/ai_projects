<!--
Reality Block
last_update: 2026-09-04
scope: Was darf Handbuch-Prosa sein
in_scope: UI-Tauglichkeit, Gate in domain-assemble
out_of_scope: System-Chart-Inspector (bleibt wie er ist)
-->

# Vertrag: Status

Policy (Soll): `blocked` | `canon_fallback` | `synth_draft` | `verified` — siehe `synthesis_canon_first.md`.

**Ist:** `sys_synthesis_wordings` hat **keine** Status-Spalte. Worker schreibt `account_id, node_id, canonical_id, language, version, canonical_description, canonical_wording, styles`.

**Gate im Slice (Phase 2):** nur `domain-assemble.ts`. System-Charts unverändert.
- UI-tauglich: `language='de'` **oder** explizite Allowlist der Canonical-IDs, die die Seite nutzt (HD-Keil aus `hd-handbook-gloss.ts` zählt als DE, unabhängig vom Atom).
- `synth_draft` EN: Lage-Satz + sichtbarer Entwurfs-Hinweis, nie Handbuch-Absatz.
- Nichts da: Leerfall — ein Satz, welches System hier schweigt und warum. Keine erfundene Prosa.

**Schuld:** Spalte `synthesis_status` als spätere Migration. Nicht im Slice erfinden.

**Tiefe 2** braucht zwei Quellen mit UI-tauglichem Status. Das ist eine Status-Frage, keine Sprach-Frage.
