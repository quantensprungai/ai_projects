# Z2 — Inner Compass: Die User-Journey

<!-- Reality Block
last_update: 2026-04-01
status: Entwurf v0.1 — UPDATE NÖTIG (siehe unten)
scope: Die 7 Phasen aus UX/Produkt-Perspektive — wie der User den IC erlebt
depends_on: ergebnis_modelle.md v0.9 (§6 Mapping), z1_gesamtwerk.md v0.5, z3_modell_referenz.md v0.4, ic_gesamtinventur.md v0.5
sources_kern:
  - kern/IC_Fundament_v06.md (Original 7 Phasen, Staffel-Logik)
  - kern/IC_Leitdokument_v5.1.md (E-20, Domäne×Phase-Matrix, UX-Triggers, Handbuch-Schichten)
  - kern/IC_Gesamtwerk_Skeleton_v02.1.md (Campbell-Heldenreise-Variante)
  - kern/IC_BRIDGE_v1.0.md (MVP-Scope, phase_tag)
purpose: Das Dokument, das jemand liest, der verstehen will wie ein User den IC erlebt
perspective: UX/Produkt — progressive Enthuellung, nicht philosophische Vollstaendigkeit
supersedes: Modell B (7 Phasen) aus IC_Fundament, Kap. XI aus IC_Leitdokument
-->

> **Z2 vs. Z1:** Z1 beschreibt den *universellen menschlichen Erkenntnisprozess* (9 Schritte, philosophisch). Z2 beschreibt, *wie ein User die App erlebt* (7 Phasen, UX). Es sind zwei Sichten auf denselben Prozess — Z2 ist die UX-Übersetzung von Z1.

> ---
> 
> **⚠️ UPDATE-VERMERK (1. April 2026)**
> 
> Dieses Dokument (v0.1) ist **veraltet** in folgenden Bereichen. Update geplant nach Engine-Phase (cursor/status.md Phase 1):
> 
> 1. **App-Spaces fehlen:** Die Navigation wurde von "5 Navigationsachsen" zu **4 App-Spaces** (JETZT, KARTE, WERKSTATT, ZEIT) überarbeitet. Dokumentiert in `ic_gesamtinventur.md` §XIII + `cursor/architecture.md` §14.
> 2. **Anker v2 fehlt:** Der Anker wurde von 3 auf 5 Komponenten erweitert (+ Handle finden, + Resonanz-Check aus Focusing). Vorschlag in `ic_gesamtinventur.md` §XIX.4. Z3 A4 hat Verweis.
> 3. **Praxis-Empfehlungs-Engine:** Externe Praktiken (IFS, Somatic, Breathwork) als phasenbasierte Empfehlungen. Konzipiert in `ic_gesamtinventur.md` §XVII.
> 4. **Engine-abhängige Entscheidungen:** Welche Chart-Visualisierungen möglich sind, hängt von den integrierten Engines ab (Phase 1). Deshalb kein Z2-Update vor Phase 1.
> 
> ---

---

# Teil 0 — Orientierung

## 0.1 Die Grundidee

Der IC enthüllt nicht alles auf einmal. Er folgt einer **progressiven Enthüllungslogik**: Erst Sicherheit, dann Muster, dann Körper, dann Schatten, dann Transformation. Der User bestimmt das Tempo. Der IC bestimmt die Reihenfolge — aber nur als Empfehlung, nie als Zwang.

## 0.2 Zwei Perspektiven, ein Prozess

| Perspektive | Dokument | Frage | Einheiten |
|---|---|---|---|
| **Universell** | Z1 (Gesamtwerk) | Was durchlebt ein Mensch bei der Selbsterkennung? | 9 Schritte |
| **UX/Produkt** | Z2 (dieses Dok.) | Wie erlebt ein User die App? | 7 Phasen |

Die 9 Schritte sind der Kompass. Die 7 Phasen sind die Straße.

## 0.3 Drei Eingänge

Nicht jeder User betritt den IC an derselben Stelle. Der Eingang bestimmt die Startphase.

| Eingang | User-Frage | Startphase | Motivation |
|---|---|---|---|
| **Chart-Signal** | "Zeig mir wer ich bin" | Phase 1 → linear | Neugier, explorativ |
| **Lebensbereich** | "Ich struggle mit meiner Beziehung" | Phase 2 → direkt in Domäne | Problem-orientiert |
| **Zeitlinie** | "Was passiert gerade mit mir?" | Phase 5 → rückwärts verlinkt | Krise, Transit-getrieben |

Der IC empfiehlt eine Reihenfolge, erzwingt keine. Aber er warnt, wenn ein User in Phase 5 (Konfrontation) einsteigt, ohne Phase 1 (Sicherheit) durchlaufen zu haben.

---

# Teil 1 — Die 7 Phasen

## Übersicht

```
Phase 1: ANKOMMEN                    ← Sicherheit + Staunen
Phase 2: ERKENNEN                    ← Muster sehen
Phase 3: VERKÖRPERN                  ← Vom Kopf in den Körper
    ┌── Konvergenz-Moment ──┐        ← (kein Phase, ein Erlebnis)
Phase 4: KONFRONTATION               ← Schatten + Falle
Phase 5: WANDLUNG                    ← Transformation
Phase 6: HORIZONT                    ← Zeitkontext + Sinn
Phase 7: GRADUATION                  ← Loslassen
```

**Jede Phase ist pro Domäne eigenständig.** Ein User kann in "Beruf" in Phase 5 sein und in "Beziehung" in Phase 2. Der IC trackt das pro Domäne.

---

## Phase 1 — ANKOMMEN: "Du bist richtig hier"

| Feld | Inhalt |
|---|---|
| **User-Frage** | "Wer bin ich?" / "Was sagen die Systeme über mich?" |
| **Ton** | Warm, bestätigend, staunend. Kein Fachjargon. |
| **9-Schritte-Mapping** | Schritt 1 (Eintritt) + Schritt 2 (Wiedererkennung) |
| **Tiefe** | Spiegel (Tiefe 1) |
| **Erkenntnisweg** | A (Konzeptuell) |

### Was passiert

Der User gibt seine Geburtsdaten ein. IC berechnet das Chart aus allen verfügbaren Systemen (Staffel-abhängig). Der User sieht zum ersten Mal seine "Signatur" — nicht als Diagnose, sondern als Spiegel.

### IC-Werkzeuge aktiv

| Werkzeug | Rolle in dieser Phase |
|---|---|
| **10 Quellsysteme** | Rohdaten → einheitliche Darstellung |
| **Stimme** (Register: Mechanik) | "Dein HD-Typ ist Generator. Das bedeutet..." |

### UX-Triggers für Phasenübergang → Phase 2

- User hat Chart gesehen und mindestens 3 Elemente angeklickt
- User sagt: "Das stimmt" / "Das kenne ich" (Wiedererkennung)
- Zeitbasiert: nach 2–3 Sessions in Phase 1

### Designprinzipien

- **Kein Overwhelm:** Nicht alle 10 Systeme auf einmal. Staffel-Logik bestimmt, was sichtbar ist.
- **Resonanz-Check:** "Erkennst du das?" — immer als Frage, nie als Behauptung.
- **Barnum-Schutz:** Transparenz: "Das ist, was die Systeme sehen. Es ist ein Angebot, kein Urteil." (Prinzip 1)

---

## Phase 2 — ERKENNEN: "Deine Muster"

| Feld | Inhalt |
|---|---|
| **User-Frage** | "Wo zeigt sich das in meinem Leben?" |
| **Ton** | Neugierig, kartographierend. "Schauen wir mal..." |
| **9-Schritte-Mapping** | Schritt 3 (Verortung) |
| **Tiefe** | Spiegel → Muster (Tiefe 1–2) |
| **Erkenntnisweg** | A → B (Konzeptuell beginnt, Erfahrungsbasiert keimt) |

### Was passiert

Die Signatur wird konkret. Nicht mehr "Du bist ein Generator" — sondern "In deinen Beziehungen zeigt sich das so. In deinem Beruf so." Das Mandala (10 Domänen) gibt dem User eine Landkarte. Die Wurzeln (9 Bedürfnisse) zeigen den Antrieb.

### IC-Werkzeuge aktiv

| Werkzeug | Rolle in dieser Phase |
|---|---|
| **Mandala** (10 Domänen) | WO im Leben zeigt sich das Muster? |
| **Wurzeln** (9 Bedürfnisse) | WAS treibt dich — was fehlt dir? |
| **Prisma** (7 Perspektiven) | Durch welche Linse schaust du gerade? |
| **Grammatik** (4 Fragen) | BEING/HAVING/DOING/INTERACTING |

### UX-Triggers für Phasenübergang → Phase 3

- User hat mindestens 2 Domänen exploriert
- User beginnt, Alltagsmuster zu erkennen ("Das mache ich auch!")
- User meldet Körper-Reaktion ("Das fühlt sich komisch an")

### Konvergenz-Moment (kann hier oder später auftreten)

Wenn 3+ Systeme gleichzeitig auf dasselbe Thema zeigen, hebt IC das hervor: "Drei unabhängige Systeme zeigen auf dasselbe Muster. Das ist kein Zufall — es ist ein Signal." Der Konvergenz-Moment ist kein Phase — er ist ein markiertes Erlebnis, das zwischen Phase 2 und Phase 5 auftreten kann.

---

## Phase 3 — VERKÖRPERN: "Dein Körper weiß"

| Feld | Inhalt |
|---|---|
| **User-Frage** | "Was sagt mein Körper dazu?" |
| **Ton** | Ruhig, einladend, verlangsamend. "Spür mal hin." |
| **9-Schritte-Mapping** | Schritt 4 (Verkörperung) — **hier liegt die Gabel** |
| **Tiefe** | Muster → Prozess (Tiefe 2–3) |
| **Erkenntnisweg** | A → **B** (Übergang vom Kopf in den Körper) |

### Was passiert

Der Modus wechselt. Phase 1–2 waren konzeptuell (lesen, verstehen, einordnen). Phase 3 wechselt in den Körper. Der Anker wird aktiviert: "Wo in deinem Körper spürst du dieses Thema?"

**Die Gabel:** Genau hier entscheidet sich der Verarbeitungsweg. Jeder **Lernmoment** (eine Lebenserfahrung, die eine Einladung enthält) kommt am Körper an. Wenn der User hinschaut → weiter zu Phase 4–5 (Transformation). Wenn er ausweicht → das Material sinkt ab, wiederholt sich lauter.

### IC-Werkzeuge aktiv

| Werkzeug | Rolle in dieser Phase |
|---|---|
| **Der Anker** | Energiezentren-Scan + Sitting With + Nervensystem-Check |
| **Stimme** (Register: Praxis) | "Schließ die Augen. Wo spürst du etwas?" |

### Nervensystem-Check als Gate

**Vor jeder Vertiefung:** IC fragt nach dem körperlichen Zustand.
- **Ventral vagal (Sicherheit):** → Vertiefung möglich
- **Sympathisch (Kampf/Flucht):** → Stabilisierung anbieten, dann Vertiefung
- **Dorsal vagal (Erstarren):** → **STOP.** Keine Tiefenarbeit. Stabilisierung + ggf. externer Verweis (Therapie)

Das ist Spannungsfeld 5 (Tiefe vs. Zugänglichkeit) in der Praxis.

### UX-Triggers für Phasenübergang → Phase 4

- User hat Anker-Übung mindestens 1× durchgeführt
- User meldet Körper-Wahrnehmung ("Ich spüre Enge in der Brust")
- Nervensystem-Check: ventral vagal (sicher genug für Vertiefung)

---

## Phase 4 — KONFRONTATION: "Dein Filter"

| Feld | Inhalt |
|---|---|
| **User-Frage** | "Wo stecke ich fest? Warum dieses Muster?" |
| **Ton** | Ehrlich, mitfühlend, konfrontativ. "Das tut weh — und es ist wichtig." |
| **9-Schritte-Mapping** | Schritt 5 (Diagnose) + Schritt 6 (Vertiefung) |
| **Tiefe** | Prozess → Experiment (Tiefe 3–4) |
| **Erkenntnisweg** | **B** (Erfahrungsbasiert, voll aktiv) |

### Was passiert

Jetzt wird es unbequem. IC benennt die Falle — das spezifische Muster, das den User gefangen hält. Dann gräbt der Brunnen: Unter dem Verhalten liegt ein Muster. Unter dem Muster eine Überzeugung. Unter der Überzeugung eine Kernverletzung. Unter der Kernverletzung: die Quelle (These 1) — die **Schwelle**, wo IC aufhört und die Stille beginnt.

### IC-Werkzeuge aktiv

| Werkzeug | Rolle in dieser Phase |
|---|---|
| **EG-Brücke** | HD-Konditionierung → EG-Fixierung (spezifisch) |
| **Pattern Traps** | Cross-System-Kombinationsfallen (kombinatorisch) |
| **Brunnen** (4 Schichten) | WIE TIEF reicht das Muster? |
| **Wunde-Kette** | WARUM dieses Muster? (Kausalkette) |
| **Stimme** (Register: Transformation) | "Die Wunde dahinter: 'Ich bin nicht liebenswert ohne Leistung.'" |

### Die Wahl

An jedem Punkt dieser Phase steht eine Wahl: Hinschauen oder ausweichen. IC respektiert beides. Es gibt immer eine Tür zum Innehalten, zum Nicht-Tun, zum Zurückkehren zu Phase 2. Konfrontation ohne Sicherheit ist Retraumatisierung — nicht Heilung.

### UX-Triggers für Phasenübergang → Phase 5

- User hat mindestens einen Pattern Trap vollständig exploriert
- User hat Brunnen-Schicht 3+ erreicht (Überzeugungen oder Kernverletzung)
- User äußert Transformationswunsch ("Was kann ich tun?")

---

## Phase 5 — WANDLUNG: "Dein Aufstieg"

| Feld | Inhalt |
|---|---|
| **User-Frage** | "Was kann ich tun? Wie komme ich da raus?" |
| **Ton** | Ermutigend, praktisch, experimentell. "Probier das diese Woche." |
| **9-Schritte-Mapping** | Schritt 7 (Transformation) |
| **Tiefe** | Experiment (Tiefe 4) |
| **Erkenntnisweg** | **B + C** (Erfahrungsbasiert + Relational) |

### Was passiert

Die Leiter wird beschritten. Fünf Stufen führen aus dem Brunnen heraus:

| Stufe | Was | Format |
|---|---|---|
| **SEHEN** | Muster erkennen, benennen | System-Erzählung + Resonanz-Check |
| **FÜHLEN** | Im Körper spüren, annehmen | Anker: Sitting With |
| **VERSTEHEN** | Beide Pole halten, Teile befragen | Balancing + IFS-Prinzip |
| **HANDELN** | Konkretes Experiment im Alltag | System-spezifische Praxis + relationales Experiment |
| **ERNTEN** | Integration: Wunde wird zur Gabe | Reflexion + Bedürfnis-Check |

**Stufe 5 (Ernten) ist die Schwelle:** Die Wunde wird zur Gabe — das ist ein transpersonaler Moment. IC sagt hier nicht "Hier ist deine Seele." IC sagt: "Hier ist Stille. Was du darin findest, ist deins."

### IC-Werkzeuge aktiv

| Werkzeug | Rolle in dieser Phase |
|---|---|
| **Leiter** (5 Stufen) | Der Transformationspfad |
| **Anker** | Körper-Arbeit in Stufe 2 (Fühlen) |
| **Prisma** | Durch welche Linse transformierst du? |
| **Stimme** (Register: Praxis) | "Diese Woche: Beobachte, wann du hilfst ohne gefragt zu werden." |

### UX-Triggers für Phasenübergang → Phase 6

- User hat mindestens ein Experiment durchgeführt und reflektiert
- Bedürfnis-Check zeigt Verschiebung (blockiertes Bedürfnis weniger blockiert)
- User berichtet von Veränderung im Alltag

---

## Phase 6 — HORIZONT: "Dein Timing"

| Feld | Inhalt |
|---|---|
| **User-Frage** | "Was passiert gerade zeitlich? Ist jetzt der richtige Moment?" |
| **Ton** | Weitsichtig, kontextualisierend, zyklisch. "Sieh es im größeren Bild." |
| **9-Schritte-Mapping** | Schritt 8 (Zeitkontext) |
| **Tiefe** | Alle Tiefen, Meta-Perspektive |
| **Erkenntnisweg** | A + B + C (alle drei) |

### Was passiert

Der User sieht sein Thema im zeitlichen Kontext. Zwei Uhren laufen:
- **Der Pfad** (innere Uhr): Wo bin ich in meinem Prozess? In welchem Schritt, in welcher Domäne?
- **Die Gezeiten** (äußere Uhr): Welche Zeitqualität wirkt? Saturn Return, BaZi Luck Pillar, HD Transit — gleichzeitig.

IC's Alleinstellung hier: **Cross-System-Timing.** Nicht "Saturn steht in deinem 7. Haus" — sondern "Saturn + BaZi Metal-Phase + HD Tor 28 zeigen alle auf Beziehung. Die Systeme konvergieren zeitlich."

### IC-Werkzeuge aktiv

| Werkzeug | Rolle in dieser Phase |
|---|---|
| **Pfad** | Innere Uhr: wo im Prozess, pro Domäne |
| **Gezeiten** | Äußere Uhr: Cross-System-Timing |
| **Mandala** | Welche Domänen sind gerade aktiv? |

### UX-Triggers für Phasenübergang → Phase 7

- User hat Timing-Kontext gesehen und integriert
- User äußert Zufriedenheit/Abschluss für diese Domäne
- Zeitbasiert: wenn User über mehrere Wochen kein neues Thema öffnet

---

## Phase 7 — GRADUATION: "Du brauchst mich nicht mehr"

| Feld | Inhalt |
|---|---|
| **User-Frage** | "Bin ich fertig?" / (keine Frage — nur Stille) |
| **Ton** | Feierlich, loslassend. "Du hast deine Sprache gefunden." |
| **9-Schritte-Mapping** | Schritt 9 (Graduation) |
| **Tiefe** | Jenseits der Tiefen — Integration |
| **Erkenntnisweg** | Jenseits der Wege — die Schwelle |

### Was passiert

Der User braucht den Spiegel nicht mehr — zumindest für dieses Thema, in dieser Domäne. Das ist kein Verlust. Das ist Erfolg (Prinzip 2: Sich überflüssig machen).

Graduation ist:
- **Pro Domäne:** Man kann in Beziehung graduieren und gleichzeitig in Beruf Phase 3 sein
- **Zyklisch:** Wenn ein neues Lebensthema auftaucht, beginnt der Zyklus neu — aber tiefer
- **Freiwillig:** IC drängt nicht zu Graduation und verhindert sie nicht

### IC-Werkzeuge aktiv

| Werkzeug | Rolle in dieser Phase |
|---|---|
| **Rückblick** | Was hast du durchlaufen? Zusammenfassung der Reise in dieser Domäne |
| **Die Wahl** | Loslassen oder vertiefen — beides ist okay |

### Die Tür bleibt offen

Saturn Return, Lebenskrisen, neue Beziehungen — es gibt immer Gründe, zurückzukehren. IC feiert die Rückkehr genauso wie die Graduation.

---

# Teil 2 — Querschnitt-Achsen

## 2.1 Die 4 Handbuch-Tiefenschichten

Jeder IC-Inhalt existiert auf einer von vier Tiefenstufen. Der User bestimmt die Tiefe. Nicht jeder muss Tiefe 4 erreichen.

| Tiefe | Name | Was der User tut | Erkenntnisweg | Phasen-Bezug |
|---|---|---|---|---|
| 1 | **Spiegel** | Liest, was die Systeme sagen | A (Konzeptuell) | Phase 1–2 primär |
| 2 | **Muster** | Erkennt Alltagsmuster, beginnt zu spüren | A → B | Phase 2–3 |
| 3 | **Prozess** | Arbeitet körperlich/emotional damit | B (Erfahrungsbasiert) | Phase 3–5 |
| 4 | **Experiment** | Probiert konkretes Verhalten im Beziehungsfeld | B + C (Relational) | Phase 5–6 |

**Die Tiefe ist keine Wertung.** Tiefe 1 für ein neues Thema ist völlig angemessen. Tiefe 4 für ein Thema, das nicht reif ist, kann schaden.

## 2.2 Domäne × Phase Matrix

Jede Zelle (Domäne × Phase) ist ein potenzieller Inhaltsbaustein. Der User befindet sich in verschiedenen Domänen in verschiedenen Phasen gleichzeitig.

| Domäne \ Phase | 1 Ankommen | 2 Erkennen | 3 Verkörpern | 4 Konfrontation | 5 Wandlung | 6 Horizont | 7 Graduation |
|---|---|---|---|---|---|---|---|
| 1 Selbst & Identität | ● | ● | ● | ● | ● | ○ | ○ |
| 2 Liebe & Partnerschaft | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| 3 Sexualität & Intimität | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| 4 Beziehungen & Community | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| 5 Beruf & Berufung | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| 6 Familie & Zuhause | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| 7 Gesundheit & Körper | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| 8 Geld & Ressourcen | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| 9 Kreativität & Ausdruck | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| 10 Sinn & Spiritualität | ○ | ○ | ○ | ○ | ○ | ○ | ● |

● = MVP-Priorität (Staffel 1) | ○ = Post-MVP

**MVP-Strategie:** Phase 1 × alle Domänen (breites Ankommen) + Domäne 1 (Identität) × alle Phasen (tiefe Durchdringung).

## 2.3 Staffel × Phase-Zuordnung

| Staffel | Systeme | Phasen-Fokus |
|---|---|---|
| **Staffel 1** | HD, BaZi, Westl. Astro, Maya | Phase 1–3 (Ankommen, Erkennen, Verkörpern) |
| **Staffel 2** | + Enneagramm, Gene Keys, Numerologie | Phase 3–5 (Verkörpern, Konfrontation, Wandlung) |
| **Staffel 3** | + Jyotish, Nine Star Ki, Kabbalah | Phase 5–7 (Wandlung, Horizont, Graduation) |

Jede Staffel fügt Systeme UND Tiefe hinzu. Ein User in Staffel 1 kann maximal Phase 3 erreichen — nicht weil es verboten ist, sondern weil die Werkzeuge für Phase 4+ (Pattern Traps, Leiter) die tieferen Systeme (EG, Gene Keys) brauchen.

---

# Teil 3 — Sicherheits-Architektur

## 3.1 Progressive Enthüllung als Schutz

IC zeigt nie alles auf einmal. Die Staffel-Logik und die Phasen-Reihenfolge SIND die Sicherheitsarchitektur. Begründung: Tiefenarbeit ohne Fundament (Phase 1–2) ist riskant.

## 3.2 Nervensystem-Check

Vor jeder Vertiefung ab Phase 3 (Verkörpern):

| Zustand | Signal | IC-Reaktion |
|---|---|---|
| **Ventral vagal** | "Ich bin präsent, neugierig" | → Vertiefung möglich |
| **Sympathisch** | "Ich bin aufgewühlt, unruhig" | → Stabilisierung anbieten, DANN Vertiefung |
| **Dorsal vagal** | "Ich bin taub, leer, nichts" | → **STOP.** Keine Tiefenarbeit. Stabilisierung + externer Verweis. |

## 3.3 Externer Verweis

IC weiß, was es NICHT kann (Z1 §5.4). An definierten Stellen verweist IC aktiv auf andere Werkzeuge:
- Bei dorsal vagal: Therapie, Krisenhotline
- Bei Trauma-Signalen: Traumatherapie (IC ≠ Therapeut)
- Bei Körper-Symptomen: Ärztliche Abklärung

---

# Teil 4 — 7 Phasen ↔ 9 Schritte Mapping

| 7 Phasen (Z2, UX) | 9 Schritte (Z1, universell) | Was verbindet sie |
|---|---|---|
| 1. Ankommen | 1. Eintritt + 2. Wiedererkennung | Sicherheit + Resonanz |
| 2. Erkennen | 3. Verortung | Muster im Leben sehen |
| 3. Verkörpern | 4. Verkörperung | Kopf → Körper. **Hier: Gabel** |
| (Konvergenz-Moment) | (kein eigener Schritt) | Multi-System-Aha |
| 4. Konfrontation | 5. Diagnose + 6. Vertiefung | Falle benennen + graben |
| 5. Wandlung | 7. Transformation | Leiter: Sehen→Ernten |
| 6. Horizont | 8. Zeitkontext | Timing, Kontext, Weitblick |
| 7. Graduation | 9. Graduation | Loslassen, Feier, Zyklus |

**Warum 7 statt 9?** Die UX komprimiert:
- Schritt 1+2 → Phase 1 (User erlebt Eintritt und Wiedererkennung als eins)
- Schritt 5+6 → Phase 4 (User erlebt Diagnose und Vertiefung als eins)
- Schritt 8+9 → Phasen 6+7 bleiben getrennt (Horizont und Graduation sind UX-seitig unterschiedlich)

---

# Teil 5 — Offene Fragen

| # | Frage | Kontext | Priorität |
|---|---|---|---|
| 1 | **Phasen-Detection:** Wie erkennt das System automatisch, in welcher Phase der User ist? | State Detection (AB-SaaS), skizziert nicht ausgearbeitet → Z4 | 🔴 HOCH |
| 2 | **Konvergenz-Moment UX:** Wie wird er visuell/interaktiv hervorgehoben? | Kein Phase, aber starkes Erlebnis. Braucht eigene UX-Behandlung. | 🔴 HOCH |
| 3 | **Phasen-Regressions-Logik:** Kann ein User von Phase 5 zu Phase 2 zurückkehren? | Ja — aber wie tracked das System das? Und wann warnt es? | 🟡 Mittel |
| 4 | **Tiefe × Phase × Domäne:** Wie navigiert der User in einem 3-achsigen Raum, ohne sich zu verlieren? | UX-Challenge: Einfachheit vs. Vollständigkeit | 🔴 HOCH |
| 5 | **Gabel-Moment als UX-Element:** Soll IC den Gabel-Moment explizit zeigen ("Du hast gerade die Wahl")? | Könnte mächtig sein — oder übergriffig. Spannungsfeld 3 (Spiegel vs. Autorität). | 🟡 Mittel |
| 6 | **Stille-Moment:** Soll IC an definierten Stellen (Schwelle) einen Stille-Moment anbieten? | "Hier enden die Systeme." — Konzept aus Z3 C6. Wie als UX-Feature? | 🟡 Mittel |
| 7 | **Phasen-Benennung:** Sind die aktuellen Namen (Ankommen, Erkennen...) die endgültigen? | Kern-Dokumente hatten verschiedene Benennungen. Noch nicht final. | 🟡 Mittel |

---

*Z2 v0.1 · 31. März 2026 · Die 7 Phasen aus UX/Produkt-Perspektive*
