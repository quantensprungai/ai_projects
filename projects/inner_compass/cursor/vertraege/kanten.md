<!--
Reality Block
last_update: 2026-09-04
scope: Vier Kantenfamilien
in_scope: relation_type, intra vs. routing vs. cross
out_of_scope: extract_relationships neu bauen (Roadmap)
-->

# Vertrag: Kanten

Vier Familien. Enum in [contracts.md §5](../contracts.md).

| Familie | Typen | Zweck | Stand |
|---|---|---|---|
| 1 Struktur | `part_of` | Tor gehört zu Zentrum | existiert |
| 2 Wirkung intra-system | `amplifies`, `depends_on`, `modifies`, `clashes_with`, `produces`, `controls` | verstärken / schwächen / bedingen | HD teilweise (Interactions-Backfill). `extract_relationships` nie gebaut. Speist Tiefe 2 und Werkstatt. |
| 3 Routing | `belongs_to_domain` | Element → Lebensbereich | Phase 2. Siehe [domaene.md](domaene.md). |
| 4 Cross-System | heute `maps_to` (3 Ko-Erwähnungen, keine Methodik) | Konvergenz | Phase 4 ersetzt durch `converges` / `complements` / `contradicts` **pro Element-Paar in einer Domäne**, nicht pro System |

**Cross-Arten (Phase 4):**
- `converges` — gleiche Aussage. Gewicht nach Genealogie: gleiche Wurzel (HD↔Astro über das Rad) niedrig, verschiedene Wurzel (BaZi↔Astro) hoch.
- `complements` — andere Facette derselben Domäne. Nicht als System-Stereotyp festnageln (jedes System hat Timing, Thema und Mechanik); nur Schwerpunkt und Auflösung differieren.
- `contradicts` — echter Widerspruch, als Reflexionsanlass ausgewiesen.

Antwort auf „Klumpen oder versetzt?“: beides, unterscheidbar per Kantenart.

**Phase 2:** Wirkungskanten der Login-Person für `self_identity` nur **lesen**, nichts extrahieren. Befund hier nachtragen.

## Bestand `self_identity` (Phase 2, noch offen)

Noch nicht gesichtet.
