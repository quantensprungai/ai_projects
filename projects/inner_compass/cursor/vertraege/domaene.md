<!--
Reality Block
last_update: 2026-09-04
scope: 12 Lebensbereiche — Herleitung, Routing, Code-Ort
in_scope: Enums, Ringe, zwei Wege belongs_to_domain
out_of_scope: Mandala-Geometrie, Content-Füllung
-->

# Vertrag: Domäne

**SoT-Enums:** [contracts.md §2](../contracts.md). 12 Werte, Labels, Kernfragen, Ringe. Einziger Code-Ort nach Phase 2: `apps/web/lib/ic/life-domains.ts`.

**Herleitung:** Cross-Framework der Zwölfteilung (Häuser, Bhavas, Paläste), Ringe Kern(1) / Nah(5) / Feld(6). Nicht Max-Neef (das sind die Wurzeln).

**Jedes System spricht in jeden Bereich**, nur nicht jedes als Strukturkonzept. HD hat kein 12-Rad, ist aber inhaltlich in allen 12 erfahrbar (`payload.life_domain` an Interpretations ~99 %). „HD nur `self_identity`“ war ein Seed-Artefakt.

**Zwei Wege für `belongs_to_domain`:**

| Weg | Quelle | Status | Beispiel |
|---|---|---|---|
| Strukturell | Katalog-`life_domain_map` (Häuser, Paläste, HD-OS) | `approved`, Evidence = Datei+Zeile | Haus 1 → `self_identity`; Haus 8 → zwei Kanten |
| Inhaltlich | Aggregation `payload.life_domain` pro Node | `candidate`, Evidence = Interp-IDs | HD-Tor mit Geld-Essays → `money_resources` |

Zielknoten: `ic.life_domain.{enum}`, `system='meta'`, 12 Stück. Abruf über Kanten, nicht über `payload.life_domain`. Node-Metadata darf stehen bleiben.

**Ist (Plan 02 Todo 1, 2026-09-04):** 12 Zielknoten liegen. Strukturelle Kanten `approved` aus den Maps (HD-OS, Ziwei 10/12, Astro inkl. Haus 8 zwei Kanten). `sexuality_intimacy` strukturell nur Astro Haus 8. Inhaltliche HD-Kanten `candidate`, Schwelle v0 ≥3 Interps und ≥30 %. Node-Metadata bleibt.

**Ziwei** passt auf die Domänen-Achse. Es testet die Konvergenz-These nicht (Häuser-Stamm). Deshalb BaZi als nächste Content-Welle, nicht gegen Ziwei.
