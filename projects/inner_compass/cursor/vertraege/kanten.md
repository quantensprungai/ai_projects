<!--
Reality Block
last_update: 2026-09-15
scope: Vier Kantenfamilien
in_scope: relation_type, intra vs. routing vs. cross
out_of_scope: extract_relationships neu bauen (Roadmap)
-->

# Vertrag: Kanten

Vier Familien. Enum in [contracts.md §5](../contracts.md).

| Familie | Typen | Zweck | Stand |
|---|---|---|---|
| 1 Struktur | `part_of` | Tor gehört zu Zentrum | existiert |
| 2 Wirkung intra-system | `amplifies`, `depends_on`, `modifies`, `clashes_with`, `produces`, `controls` | verstärken / schwächen / bedingen | HD Backfill liegt (`candidate`). Login-Person `self_identity`: 11 interne, 445 inzident, `modifies` 0. `extract_relationships` nie gebaut. |
| 3 Routing | `belongs_to_domain` | Element → Lebensbereich | Phase 2. Siehe [domaene.md](domaene.md). |
| 4 Cross-System | `converges` / `complements` / `contradicts` | Konvergenz-Skelett | Review 4: fünf Typen × Eingang/Lebensort; Tagstamm nur Ji/Yi. `maps_to` 143 unangetastet. |

**Cross-Arten (Phase 4):**
- `converges` — gleiche Aussage. Gewicht nach Genealogie: gleiche Wurzel (HD↔Astro über das Rad) niedrig, verschiedene Wurzel (BaZi↔Astro) hoch.
- `complements` — andere Facette derselben Domäne. Nicht als System-Stereotyp festnageln (jedes System hat Timing, Thema und Mechanik); nur Schwerpunkt und Auflösung differieren.
- `contradicts` — echter Widerspruch, als Reflexionsanlass ausgewiesen.

Antwort auf „Klumpen oder versetzt?“: beides, unterscheidbar per Kantenart.

**Phase 2:** Wirkungskanten der Login-Person für `self_identity` nur **lesen**, nichts extrahieren. Befund hier nachtragen.

## Bestand `self_identity` (Login-Person, 2026-09-04)

Person: `test@makerkit.dev`, Geburt 1980-11-18 19:20 Berlin. HD: Projektor, milzische Autorität, Profil 3/5, definierte Zentren G und Milz.

Fokus-Knoten: `hd.type.projector`, `hd.authority.splenic`, `hd.profile.3_5`, `hd.center.g`, `hd.center.spleen`.

| Schnitt | Zahl | Aufteilung |
|---|---|---|
| Zwischen den fünf Fokus-Knoten (beide Enden im Set) | **11** | `amplifies` 7, `depends_on` 3, `clashes_with` 1, `modifies` 0 |
| Mindestens ein Ende im Set (inzident) | 445 | `amplifies` 179, `depends_on` 170, `clashes_with` 96, `modifies` 0 |

Alle 11 bzw. 445: `review_status=candidate`, `edge_scope=intra_system` (Interactions-Backfill 2026-08-05). Keine `approved` Wirkungskante in diesem Cut. Hub ist die Milz (9 der 11 internen, 254 inzident). Typ nur 1 interne Kante.

Mehrere interne Kanten teilen dieselbe Interpretation (Fan-out). Beispiel: Interp „instantaneous splenic intuition“ speist `splenic amplifies spleen`, `splenic amplifies 3/5`, `3/5 amplifies spleen`, `spleen depends_on splenic`.

**Drei Beispiele (intern):**

1. `hd.authority.splenic` —`amplifies`→ `hd.center.spleen` — mechanisch plausibel (Autorität sitzt in dem Zentrum).
2. `hd.profile.3_5` —`depends_on`→ `hd.authority.splenic` — gleiches Interp wie (1), kein eigener Beleg.
3. `hd.center.spleen` —`clashes_with`→ `hd.center.g` — parallel existieren `amplifies` in beide Richtungen G↔Milz. Backfill-Widerspruch, nicht als Tiefe-2-Satz verwendbar.

**Folgerung fürs Handbuch:** Die 11 Kanten tragen in Phase 2 keinen Satz. OS-Paare sind dünn, oft Fan-out, nie `approved`; eine Kante widerspricht sich selbst. Inzidente 445 gehen vor allem auf Tore/Kanäle außerhalb dieses OS-Schnitts. Nichts extrahieren.

Einordnung: Familie 2 speist Muster *innerhalb* eines Systems und die Werkstatt — nicht Tiefe 2 „Wo sich die Quellen treffen“ auf der Bereichsseite; das ist Familie 4 (Phase 4). Bereichsseite Tiefe 2 hängt in Phase 2 nur an „zwei UI-taugliche Quellen“ (Status-Gate), nicht an Wirkungskanten. `domain-assemble.ts` liest Familie 2 nicht.

**Review 2 (2026-09-11):** Befund steht. Familie 2 bleibt stumm bis Phase 4/5 (Widerspruchsfilter + Fan-out darf nicht als mehrere Belege zählen). Inhaltliche `belongs_to_domain`-Schwelle v0 unverändert — die Bereichsseite liest für `self_identity` die strukturellen OS-/Lage-Karten, nicht die 418 `candidate`-Paare.
