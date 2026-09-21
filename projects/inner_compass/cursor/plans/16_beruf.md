<!--
Reality Block
last_update: 2026-09-21
scope: Phasen-Plan 16 — career_calling als erste Domäne im Kapitel-Modell (noch nicht gebaut)
in_scope: DOMAIN_RULES-Eintrag Beruf HD/Astro, Fixtures, Seed OS+Saturn → career, Route frei, Beweis
out_of_scope: Code-Umbau am Modell (Plan 15), Haus 6 verdrahten, BG5/Penta, Ziwei/BaZi formulieren, 418
-->

# Plan 16 — Beruf & Berufung im Kapitel-Modell

Folgt auf [Plan 15](15_hit_regel_tabelle.md). **Noch nicht gebaut.** Erster Test, ob eine neue Domäne ohne Code-Umbau trägt: Tabelleneintrag + Fixtures + Seed + Beweis.

## Methodik-Entwurf, Review vor Code

Highlight Sakral/Wille/Kehle = **oft zuerst** von „Was ist meine Arbeit?“ getroffen. Offenes Haupt, G, Milz, Solarplexus, Wurzel bedingen Arbeit genauso — Overlay (Plan 15), kein Ausschluss.

| System | Natal-Erstlage | Zusatzlage (Liste, leer erlaubt) | Highlight | Anderer Kontext | Schweigen |
|---|---|---|---|---|---|
| HD | Typ + Strategie in Arbeit | `21_45`, `26_44`, `32_54`, `16_48`, `20_34`, `10_20` + hängende Tore daraus | Sakral / Wille / Kehle | BG5, Penta | ja auf Zusatzlage |
| Astro | MC / Haus 10 (Planet H10 → MC-Konjunktion ≤3° → MC-Zeichen) | Saturn (Haus, Zeichen) | — | Transit; Haus 6 = Alltag, nicht mit MC vermischen | nein |
| Ziwei | 官禄宫 | Sterne im Palast (nicht 16) | — | 合盤 | nein |
| BaZi | Tagstamm in Arbeit | Officer-Stern später | — | Branch-Compare | ja |

Vor Code bestätigen: Kanal-Liste; Saturn vs Haus 6.

## Bau

1. `DOMAIN_RULES.career_calling` in `lib/ic/chapter-rules.ts` (HD + Astro aus Tabelle).
2. Fixtures: 5 HD (OS + 0/1/2 Arbeitskanäle, hängend 45, Reflektor), 4 Astro (Planet H10, MC-Konjunktion, nur MC-Zeichen, Saturn prominent).
3. `hd_structure_v0.json`: 9 OS-Zeilen → `career_calling`; `astro_structure_v0.json`: `astro.planet.saturn` → `career_calling`. Seed `--only-domain-routing`. 418 unangetastet.
4. Gating liest `DOMAIN_RULES` (Plan 15, **steht**) → Route frei ohne Code.
5. Beweis: `check_handbook_chapter.ts` um career erweitern; 1978 live HD/Astro; Jargon-Gate; UI-Sicht.
6. Docs: Ist, `domaene.md`, roadmap/handover; Commits.

Wenn Schritt 1–4 Code außerhalb Tabelle/Fixtures/JSON brauchen, ist das ein Befund gegen Plan 15 — zurück ins Modell, nicht Sonderfall.

## Nicht

Übrige Domänen, Overlay füllen, Haus 6, BG5/Penta, Ziwei/BaZi formulieren, 418, `db reset`, Merge `main`.
