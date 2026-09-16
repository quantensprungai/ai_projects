<!--
Reality Block
last_update: 2026-09-16
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

**Ist (Plan 02 Todo 5, 2026-09-04):** `lib/ic/domain-assemble.ts` liest `belongs_to_domain`, schneidet gegen Chart-Knoten, eine Karte pro Quelle (`approved` vor `candidate`). Route `karte/bereich/[domain]`, nur `self_identity` frei.

**Ist (Review 2, 2026-09-11):** Eine Domäne liest sich als Handbuchkapitel. Schwelle v0 der inhaltlichen Kanten bleibt (Decision 2026-09-11). Zwölf Seiten und Mandala weiter Phase 6. BaZi als nächste Welle, weil Ziwei die Konvergenz-These nicht testet.

**Ist (Plan 03, 2026-09-13):** Auf `self_identity` vier Quellen. BaZi spricht am Tagstamm (eine Rolle, zehn Färbungen), nicht am 12-Rad. Review 3 bestanden. Phase 4 = Cross-Kanten in dieser einen Domäne, nicht zwölf.

**Ist (Phase 5, Review 5, 2026-09-15):** Vertikal auf `self_identity` geschlossen (Spiegel, Treffen, Werkstatt). Zwölf Bereichs-*Routen* existieren; außer Identität: Kernfrage + „noch nicht“. Hub zeigt einen Link plus Quellen-Linsen, Mandala-Platzhalter. BaZi-Routing bleibt Tagstamm → Identität; HD-OS bleibt Identität — ohne Nachzug werden andere Bereichsseiten dünn.

**Ist (Phase 7, Review 7, 2026-09-16):** `love_partnership` ist zweites Handbuch. Strukturell Haus 7 + Spouse; HD/BaZi still (Seed). Assemble injiziert `astro.house.7` auf dieser Seite, weil Natal-Nodes keine Häuser führen (wie Haus 1 auf Identität). Occupancy-Regel unverändert. Candidate-418 unangetastet. Plan: [../plans/07_love_partnership.md](../plans/07_love_partnership.md).

**Ziwei** passt auf die Domänen-Achse. Es testet die Konvergenz-These nicht (Häuser-Stamm). Deshalb BaZi als nächste Content-Welle, nicht gegen Ziwei.
