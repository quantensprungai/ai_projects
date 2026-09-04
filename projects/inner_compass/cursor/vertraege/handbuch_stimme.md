<!--
Reality Block
last_update: 2026-09-04
scope: Wie ein Handbuch-Satz klingt
in_scope: Übersetzungsregel, Code-Ort, Meta-Begriffe der einen Domäne
out_of_scope: Glossar-Projekt, generate_meta_nodes
-->

# Vertrag: Handbuch-Stimme

**Regel:** Benennen ohne Systemjargon. Systemname erst im Verorten. Keine Canonical-IDs, keine Quelltitel, zweite Person, kein Urteil, keine Stufen (anti-AQAL).

Mikro-Erzählung Tiefe 1: **Benennen → Übersetzen → Verorten**. Reflexion und Einladung optional, Werkstatt später.

**Code:** `hd-handbook-gloss.ts` bleibt HD-Keil (Vorbild). Daneben `lib/ic/handbook-voice.ts`: Regel als Kommentar + Helfer. Sprache v0 ist **vorgegeben** und aus den Systemen abgeleitet. Version `handbook-voice-v0`.

**Handbuch-Text wird formuliert**, nicht aus Atomen übersetzt. Siehe [sprache.md](sprache.md).

**Meta-Begriffe** entstehen in der Menge, die eine Domäne braucht, und werden hier notiert, nicht in die DB geschrieben. `generate_meta_nodes` erst nach Cross-Kanten (Phase 4).

## Begriffe für `self_identity` (wachsen in Phase 2)

| Begriff | Statt (nicht im Benennen) | Herkunft |
|---|---|---|
| Einladung | HD-Strategie-Label | Alltagswort, wie jemand dich wirklich meint |
| Antwort | Wait to Respond | Bewegung, die wartet, bis etwas da ist |
| Eingang | Aszendent / Haus 1 | Wie du in einen Raum trittst |
| Lebensort | 命宫 / soulPalace | Ort, von dem aus du dich selbst liest |

**Ist (Plan 02 Todo 4, 2026-09-04):** Helfer in `handbook-voice.ts`. HD-Übersetzen kommt weiter aus `hd-handbook-gloss.ts`. Astro/Ziwei haben vorgegebene Lage-Sätze, keinen Handbuch-Absatz.
