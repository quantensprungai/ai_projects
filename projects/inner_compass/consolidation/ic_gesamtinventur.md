# IC Gesamtinventur — Alle Bausteine auf einen Blick

<!-- Reality Block
last_update: 2026-03-31
status: v0.5 (+Scope-Cut v1/v2/v3, +Architecture-Delta 8 Lücken + 3 Updates)
scope: Vollständiges Inventar + Scope-Cut + Architecture-Delta-Analyse
depends_on: z3_modell_referenz.md v0.4, ergebnis_modelle.md v0.9, z1_gesamtwerk.md v0.5, z2_user_journey.md v0.1, cursor/architecture.md, cursor/pipeline.md, cursor/engines.md, cursor/contracts.md
purpose: Grüne-Wiese-Referenz + Produktplanung + Architektur-Brücke
phase: Phase 3→4 (Inventur abgeschlossen, Scope definiert, Architektur-Delta identifiziert)
-->

> **Dieses Dokument ist die Inventur.** Kein Konzept, keine Architektur-Entscheidung — nur: was existiert.
> Es dient als Grundlage für die App-View-Entscheidungen (→ Z4).

---

## Inhaltsverzeichnis

- [I. Philosophische Grundlagen](#i-philosophische-grundlagen)
- [II. Der Prozess (Ordnungsprinzip)](#ii-der-prozess)
- [III. Schritt-gebundene Bausteine (11)](#iii-schritt-gebundene-bausteine)
- [IV. Querschnitt-Werkzeuge (4)](#iv-querschnitt-werkzeuge)
- [V. Meta-Strukturen (8)](#v-meta-strukturen)
- [VI. Content-Dimensionen (7D-Inhaltsraum)](#vi-content-dimensionen)
- [VII. 16er-Matrix (Content-Produktionsprinzip)](#vii-16er-matrix)
- [VIII. Content-Typen und Erzählprinzipien](#viii-content-typen-und-erzaehlprinzipien)
- [IX. Navigations-Achsen (aus kern-Docs)](#ix-navigations-achsen)
- [X. Infrastruktur-Bausteine](#x-infrastruktur-bausteine)
- [XI. Verwechslungsschutz](#xi-verwechslungsschutz)
- [XII. Zahlen auf einen Blick](#xii-zahlen-auf-einen-blick)
- [XIII. App-Spaces (Erster Entwurf)](#xiii-app-spaces)
- [XIV. Abgleich: Externe System-Diskussion](#xiv-abgleich-externe-system-diskussion)
- [XV. Phasen-Vergleich](#xv-phasen-vergleich)
- [XVI. Was bereits existiert](#xvi-was-bereits-existiert)
- [XVII. Neue Feature-Ideen](#xvii-neue-feature-ideen)
- [XVIII. Gesamtbild: 5-Schichten-Modell](#xviii-gesamtbild)
- [XIX. Abgleich: Voice Dialogue, Focusing, Prozessarbeit, Tesla](#xix-abgleich-voice-dialogue)
- [**XX. Scope-Cut: v1 / v2 / v3**](#xx-scope-cut)
- [**XXI. Architecture-Delta: Was sich ändern muss**](#xxi-architecture-delta)

---

## I. Philosophische Grundlagen

### 7 Thesen

| # | Name | Kernaussage |
|---|---|---|
| T1 | Quell-These | Unter allen Schichten liegt etwas Unbeschreibbares. IC zeigt darauf, benennt es nicht. |
| T2 | Bewusstseins-These | Bewusstsein ist nicht verursacht durch Anlage/Prägung — es kann beides SEHEN. |
| T3 | Schichten-These | Selbsterkenntnis ist ein Schälprozess: Verhalten → Muster → Überzeugungen → Kernverletzung. |
| T4 | Konvergenz-These | Wenn mehrere Systeme auf dasselbe zeigen = Signal (nicht Beweis). |
| T5 | Resonanz-These | Der User spürt Wahrheit am "Ding"-Moment — das System liefert nur Sprache dafür. |
| T6 | Temporal-These | Selbsterkenntnis hat Zeitfenster. Systeme zeigen nicht nur WAS, sondern WANN. |
| T7 | Praxis-These | Erkenntnis ohne Praxis verändert nichts. IC muss ins Leben wirken. |

### 5 Prinzipien

| # | Name | Leitplanke |
|---|---|---|
| P1 | Kein neuer Guru | IC sagt "Dein Chart deutet auf X", nie "Du bist X". |
| P2 | Graduation | Der User soll die App nicht mehr brauchen. Das ist Erfolg. |
| P3 | Karte ≠ Territorium | Alle Systeme sind Modelle, keines ist die Wahrheit. |
| P4 | Keine Position des Guten | IC bewertet nicht. "Offenes Emotionalzentrum" ist weder gut noch schlecht. |
| P5 | Körper hat Vorrang | Wenn der Körper Nein sagt, wiegt das schwerer als jeder Chart. |

### 4 Spannungsfelder (produktiv, nicht aufzulösen)

| Spannung | Warum produktiv |
|---|---|
| Freiheit vs. Determination | Chart zeigt Anlage, Bewusstsein wählt frei |
| Synthese vs. Vereinnahmung | Kulturelles Wissen nutzen ohne anzueignen |
| Spiegel vs. Autorität | IC spiegelt, kuratiert aber den Spiegel |
| Graduation vs. Geschäftsmodell | Sich-überflüssig-machen = Feature |

---

## II. Der Prozess

### 9 Schritte (universelles Ordnungsprinzip)

| # | Schritt | User-Moment | User-Frage | Cross-Framework |
|---|---|---|---|---|
| 1 | **Eintritt** | "Zeig mir wer ich bin" | Chart aus 10 Systemen | Ra: Pre-incarnative choices. Jung: Archetypen |
| 2 | **Wiedererkennung** | "Das bin ja ich!" | Resonanz-Erlebnis | Ra: Katalysator bemerkt. Jung: Animus/Anima |
| 3 | **Verortung** | "Wo zeigt sich das?" | Domänen + Bedürfnisse | Ra: Inkarnation in 3D. IFS: System erkunden |
| 4 | **Verkörperung** | "Was sagt mein Körper?" | ⚡ Gabel-Punkt | Ra: Körper als Katalysator-Speicher. Aaron: Körper-Gewahrsein |
| 5 | **Diagnose** | "Wo stecke ich fest?" | Pattern Traps | Ra: Unverarbeiteter Katalysator. Jung: Schatten |
| 6 | **Vertiefung** | "Warum dieses Muster?" | Brunnen + Wunde-Kette | Ra: Erfahrung→Verstehen. IFS: Teile bezeugen |
| 7 | **Transformation** | "Was kann ich tun?" | Leiter (5 Stufen) | Ra: Akzeptanz. GK: Shadow→Gift→Siddhi |
| 8 | **Zeitkontext** | "Ist jetzt der Moment?" | Pfad + Gezeiten | Ra: Zyklische Katalysator-Wellen |
| 9 | **Graduation** | "Ich brauch das nicht mehr" | Feier, nicht Verlust | Ra: Harvest. IFS: Harmonie |

### 7 User-Phasen (UX-Perspektive, → Z2)

| # | Phase | Ton | 9-Schritte-Mapping |
|---|---|---|---|
| 1 | Ankommen | Warm, bestätigend | Schritte 1–2 |
| 2 | Erkennen | Neugierig, kartographierend | Schritte 2–3 |
| 3 | Verkörpern | Ruhig, verlangsamend | Schritt 4 (Gabel) |
| 4 | Konfrontation | Ehrlich, mitfühlend | Schritte 5–6 |
| 5 | Wandlung | Ermutigend, praktisch | Schritt 7 |
| 6 | Horizont | Weitsichtig, zyklisch | Schritt 8 |
| 7 | Graduation | Feierlich, loslassend | Schritt 9 |

### 3 Einstiegskanäle

| Kanal | User-Frage | Einstiegs-Schritt |
|---|---|---|
| **Chart-Signal** | "Zeig mir wer ich bin" | Schritt 1 → linear |
| **Lebensbereich** | "Hier brennt es" | Schritt 3 (Domäne) → dann 5–7 |
| **Zeitlinie** | "Was ist gerade los?" | Schritt 8 → dann betroffene Domäne |

### 2 Einstiegs-Typen

| Typ | Weg |
|---|---|
| **Neugier** | Schritt 1 → 2 → 3 → ... (linear, explorativ) |
| **Schmerz** | Schritt 5 direkt → 6 → 7 → dann 1–4 (Diagnose zuerst) |

---

## III. Schritt-gebundene Bausteine

### III.1 — 10 Quellsysteme (Schritt 1: Eintritt)

| System | Kulturkreis | Perspektive | Kernfrage | Klasse |
|---|---|---|---|---|
| Human Design | Synthese | Mechanik/Energietyp | WIE bin ich gebaut? | A (Vollständig) |
| BaZi | Chinesisch | Elementezyklen/Timing | WAS sind meine Zyklen? | A |
| Westliche Astrologie | Europäisch | Archetypen/Häuser | WO sind meine Themen? | A |
| Maya/Tzolkin | Mesoamerikanisch | Kosmischer Rhythmus | WELCHE WELLE trägt mich? | A |
| Jyotish | Indisch | Dharma/Karma | WOZU bin ich hier? | B (Teilweise) |
| Gene Keys | Synthese | Frequenz-Spektrum | WOHIN kann ich mich entwickeln? | B (Lizenzthema) |
| Enneagramm | Psychodynamisch | Psychodynamik/Wunde | WARUM reagiere ich so? | C (Via HD abgeleitet) |
| Numerologie | Westlich | Zahlenmuster | WELCHE MUSTER trage ich? | B |
| Spiral Dynamics | Entwicklungspsych. | Werte-Ebenen | AUF WELCHER EBENE stehe ich? | D (Sekundär) |
| I Ging / Ur-Systeme | Diverse | Historische Wurzeln | WOHER kommt das Wissen? | Referenz |

### III.2 — Mandala: 12 Domänen, 3 Ringe (Schritt 3: Verortung)

> **Revidiert 2026-03-31:** Von 10→12 Domänen erweitert. Begründung: ergebnis_modelle.md §20d-rev.

**Ring-Struktur:**

| Ring | Domänen |
|---|---|
| **Kern** | 10 Sinn & Spiritualität |
| **Nah** | 1 Selbst, 2 Liebe, 3 Sexualität, 7 Gesundheit, 12 Wandlung & Erneuerung 🆕 |
| **Feld** | 4 Community, 5 Beruf, 6 Familie, 8 Geld, 9 Kreativität, 11 Austausch & Lernen 🆕 |

**Domänen:**

| # | Domäne | Kernfrage | Ring |
|---|---|---|---|
| 1 | Selbst & Identität | Wer bin ich im Kern? | Nah |
| 2 | Liebe & Partnerschaft | Wie liebe ich? | Nah |
| 3 | Sexualität & Intimität | Wie verbinde ich mich körperlich? | Nah |
| 4 | Beziehungen & Community | Wie gestalte ich Zugehörigkeit? | Feld |
| 5 | Beruf & Berufung | Was ist meine Arbeit in der Welt? | Feld |
| 6 | Familie & Zuhause | Wie gestalte ich Heimat? | Feld |
| 7 | Gesundheit & Körper | Was braucht mein Körper? | Nah |
| 8 | Geld & Ressourcen | Wie verdiene und verwalte ich? | Feld |
| 9 | Kreativität & Ausdruck | Was will durch mich in die Welt? | Feld |
| 10 | Sinn & Spiritualität | Was ist das größere Bild? | Kern |
| 11 | Austausch & Lernen 🆕 | Wie teile und verstehe ich? | Feld |
| 12 | Wandlung & Erneuerung 🆕 | Was muss loslassen, damit Neues kommt? | Nah |

### III.3 — Wurzeln: 9 Bedürfnisse (Schritt 3: Verortung)

Basierend auf Max-Neef. Antrieb hinter dem Verhalten — was treibt, was fehlt.

| # | Bedürfnis | Kernfrage |
|---|---|---|
| 1 | Subsistence | Was brauche ich zum Überleben? |
| 2 | Protection | Wo fühle ich mich sicher? |
| 3 | Affection | Wo werde ich geliebt? |
| 4 | Understanding | Was will ich verstehen? |
| 5 | Participation | Wo gehöre ich dazu? |
| 6 | Idleness | Wo kann ich ruhen? |
| 7 | Creation | Was will durch mich entstehen? |
| 8 | Identity | Wer bin ich wirklich? |
| 9 | Freedom | Wo bin ich frei? |

### III.4 — Der Anker: Verkörperung (Schritt 4: Verkörperung) 🔴

3 Komponenten:

| Komponente | Was | Praxis |
|---|---|---|
| **Energiezentren-Scan** | "Wo im Körper spürst du etwas?" (4 Zonen) | User markiert Körperzonen |
| **Sitting With** | "Bleib beim Gefühl. Nicht ändern." | Timer-basierte Körper-Meditation (2–5 min) |
| **Nervensystem-Check** | "Kampf/Flucht, Erstarren oder Sicherheit?" | 3-Optionen-Selbsteinschätzung |

**Architekturelle Rolle:** Der Anker steht am **Gabel-Punkt**. Er hilft, Lernmomente im Körper zu BEMERKEN, bevor sie unbewusst absinken.

### III.5 — EG-Brücke: HD→Enneagramm (Schritt 5: Diagnose)

3-Schritt-Ableitung: HD offene Zentren → EG-Triade → EG-Typ-Hypothese (nicht Assessment, sondern Chart-basiert).

| HD-Zentrumsstatus | EG-Triade | Grundemotion | Typen |
|---|---|---|---|
| Offenes Emotional/Sakral | Bauch (8-9-1) | Zorn | Instinkt-zentriert |
| Offenes Ajna/Krone | Kopf (5-6-7) | Angst | Mental-zentriert |
| Offenes Herz/G | Herz (2-3-4) | Scham | Gefühl-zentriert |

### III.6 — Pattern Traps: Konfigurationsfallen (Schritt 5: Diagnose)

Kombinatorische Fallen aus mehreren Systemen gleichzeitig:

```
HD offenes Zentrum × EG-Fixierung × BaZi-Element-Clash × Domäne = spezifische Falle
```

**Abgrenzung zum Lernmoment:** Pattern Traps = strukturelle Verwundbarkeit (das trockene Holz). Lernmoment = die neutrale Lern-Einladung (der Funke). Beides unabhängig, aber sie treffen aufeinander.

### III.7 — Brunnen: 4 Tiefenschichten (Schritt 6: Vertiefung)

| Schicht | Name | Was | User-Frage |
|---|---|---|---|
| 1 | **Verhalten** | Oberfläche, sichtbar | "Was tue ich?" |
| 2 | **Muster** | Wiederkehrende Dynamiken | "Was wiederhole ich?" |
| 3 | **Überzeugungen** | Filter, Glaubenssätze | "Was glaube ich?" |
| 4 | **Kernverletzung** | Ursprüngliche Erfahrung | "Was liegt darunter?" |
| — | *(Quelle)* | Das Unbeschreibbare (These 1) | *(IC zeigt darauf, benennt es nicht)* |

**16er-Matrix:** Brunnen × Grammatik = 4 Schichten × 4 Fragen = 16 Content-Zellen (→ §VII).

### III.8 — Wunde-Bedürfnis-Falle-Kette (Schritt 6: Vertiefung)

Kausalkette der tiefen Muster:

```
Kernverletzung (Brunnen S4) → blockiertes Bedürfnis (Wurzeln) → Kompensation (Brunnen S3) → Pattern Trap → Symptom (Brunnen S1-2)
```

Trianguliert durch die **EG-HD-Neef Kehrseiten-Brücke**:

| EG-Typ | Leidenschaft | Bedrohtes Bedürfnis | Kompensation |
|---|---|---|---|
| 1 Perfektionist | Zorn | Freedom | Kontrolle |
| 2 Helfer | Stolz | Affection | Unentbehrlichkeit |
| 3 Performer | Täuschung | Identity | Leistung/Image |
| 4 Individualist | Neid | Identity + Participation | Einzigartigkeit |
| 5 Beobachter | Geiz | Understanding + Protection | Rückzug |
| 6 Loyalist | Angst | Protection | Orientierungssuche |
| 7 Enthusiast | Völlerei | Freedom + Idleness | Vermeidung |
| 8 Herausforderer | Wollust | Freedom + Subsistence | Dominanz |
| 9 Vermittler | Trägheit | Participation + Idleness | Selbstvergessenheit |

**Status:** Forschungshypothese (Evidenzklasse C–D).

### III.9 — Leiter: 5 Transformationsstufen (Schritt 7: Transformation)

| Stufe | Name | Was | Erkenntnisweg | Quelle |
|---|---|---|---|---|
| 1 | **SEHEN** | Muster erkennen | A (Konzeptuell) | HD/Astro/BaZi |
| 2 | **FÜHLEN** | Im Körper ankommen | B (Erfahrung) | Anker, Polyvagal |
| 3 | **VERSTEHEN** | Beide Pole halten (Balancing) | B (Erfahrung) | Ra, IFS |
| 4 | **HANDELN** | Konkretes Experiment | B + C (Relational) | Quellsysteme + Aaron |
| 5 | **ERNTEN** | Wunde → Gabe | A + B + C (alle) | GK, Max-Neef |

**Spiegelung:** Stufe 1↔Schicht 1, Stufe 2↔Schicht 2, Stufe 3↔Schicht 3, Stufe 4↔Schicht 4. Stufe 5 (Ernten) hat kein Brunnen-Gegenstück — Transformation geht über die Wunde hinaus.

### III.10 — Pfad: Innere Uhr (Schritt 8: Zeitkontext)

Die 7 User-Phasen als persönlicher Entwicklungspfad — pro Domäne eigenständig. Kein globaler User-Status.

### III.11 — Gezeiten: Äußere Uhr (Schritt 8: Zeitkontext)

| Zeitquelle | Was sie zeigt | Zykluslänge | System |
|---|---|---|---|
| HD Transit | Aktivierte Tore/Kanäle | Stunden – Monate | HD |
| BaZi Luck Pillar | 10-Jahres-Phasen | 10 Jahre | BaZi |
| Astro Transit | Planetentransite | Tage – Jahre | Westl. Astro |
| Jyotish Dasha | Planetenperioden | 6–20 Jahre | Jyotish |
| Maya Wavespell | 13-Tages-Zyklen | 13 Tage | Maya |

**4 Dynamik-Dimensionen (Priorität):**

| Prio | Dimension | Quellen |
|---|---|---|
| 1 | Biographisch | User-Selbstauskunft |
| 2 | Konvergenz | KG-Kreuzabgleich (mehrere Systeme gleichzeitig) |
| 3 | Astronomisch | Transite, Luck Pillars, Dashas |
| 4 | Psychologisch | Not-Self-Muster, Trigger |

---

## IV. Querschnitt-Werkzeuge

### IV.1 — Prisma: 7 Perspektiven

| # | Perspektive | Frage | System-Beiträge |
|---|---|---|---|
| P1 | **Körper / Soma** | Was spürt mein Körper? | HD: PHS, Astro: ASC, BaZi: Element-Balance |
| P2 | **Energie / Vitalität** | Wie fließt meine Energie? | HD: Typ+Zentren, BaZi: Qi-Fluss |
| P3 | **Disposition / Identität** | Wer bin ich von Natur aus? | HD: Profil, BaZi: Day Master, Astro: Sonne |
| P4 | **Verbindung / Beziehung** | Wie beziehe ich mich? | HD: Composite, EG: Beziehungsstil, Astro: Venus |
| P5 | **Psychodynamik** | Was treibt mich unbewusst? | EG: Fixierung, HD: Offene Zentren, Astro: Pluto/Chiron |
| P6 | **Bewusstsein** | Was kann ich sehen/wählen? | GK: Shadow→Gift→Siddhi, Spiral Dynamics |
| P7 | **Transzendenz / Sinn** | Was ist das größere Bild? | HD: Inkarnationskreuz, Jyotish: Dharma, Maya: Kin |

**Sonderrolle P1:** Körper ist nicht nur Linse — er ist der primäre Auffangort für unbewusst verarbeitete Lernmomente (→ Gabel).

### IV.2 — Grammatik: 4 Fragen (Max-Neef)

| Frage | Was sie öffnet | Beispiel (Domäne 2: Liebe) |
|---|---|---|
| **BEING** | Was BIN ich hier? | "Wie zeige ich mich in Beziehungen?" |
| **HAVING** | Was HABE ich / fehlt mir? | "Welche Ressourcen/Defizite bringe ich mit?" |
| **DOING** | Was TUE ich? | "Was tue ich automatisch wenn es eng wird?" |
| **INTERACTING** | Wie INTERAGIERE ich? | "Wie gestalte ich Nähe/Distanz?" |

### IV.3 — Stimme: 3 Register + 5-Schritt-Mikro-Erzählprinzip

**3 Register:**

| Register | Ton | Wann primär |
|---|---|---|
| **Mechanik** | Sachlich, neutral | Schritt 1–3 |
| **Transformation** | Warm, einladend | Schritt 4–7 |
| **Praxis** | Direkt, handlungsorientiert | Schritt 7–9 |

**5-Schritt-Mikro-Erzählprinzip** (pro Content-Baustein):

1. **BENENNEN** — Was zeigt das System? (Systemsprache)
2. **ÜBERSETZEN** — Was heißt das in Alltagssprache?
3. **VERORTEN** — Wo zeigt sich das? (Tiefe, Domäne, Zeit)
4. **REFLEXION** — Was löst das in dir aus? (Offene Frage)
5. **EINLADUNG** — Was könntest du damit tun? (Möglichkeit, kein Urteil)

### IV.4 — Zeitgeist-Fallen: 8 kulturelle Verzerrungen

| # | Falle | Verzerrung | Antidot |
|---|---|---|---|
| 1 | Optimierungs-Falle | "Ich muss mich verbessern" | P4 (Keine Position des Guten) |
| 2 | Identifikations-Falle | "Ich BIN mein Typ" | P3 (Karte ≠ Territorium) |
| 3 | Guru-Falle | "Das System weiß es besser" | P1 (Kein neuer Guru) |
| 4 | Konsum-Falle | "Mehr Systeme = mehr Erkenntnis" | P2 (Graduation) |
| 5 | Bypassing-Falle | "Spirituelle Erklärung statt Gefühl" | P5 (Körper hat Vorrang) |
| 6 | Einzigartigkeits-Falle | "Ich bin so besonders/komplex" | T4 (Konvergenz = Signal) |
| 7 | Zukunfts-Falle | "Wenn ich erst X bin, dann..." | T7 (Praxis-These) |
| 8 | Determinismus-Falle | "Es steht in den Sternen" | Spannungsfeld 1 |

---

## V. Meta-Strukturen

### V.1 — Zentralspindel (Brunnen ↔ Leiter)

```
LEITER (Aufstieg)                        BRUNNEN (Abstieg)
Stufe 5: ERNTEN (Gabe)                  
    ↑                                    
Stufe 4: HANDELN (Experiment)            Schicht 1: VERHALTEN (Oberfläche)
    ↑                                        ↓
Stufe 3: VERSTEHEN (Balancing)           Schicht 2: MUSTER (Dynamiken)
    ↑                                        ↓
Stufe 2: FÜHLEN (Körper)                 Schicht 3: ÜBERZEUGUNGEN (Filter)
    ↑                                        ↓
Stufe 1: SEHEN (Muster)                 Schicht 4: KERNVERLETZUNG (Wunde)
                                             ↓
                                    ─── QUELLE (These 1) ───
```

**Kern-Mechanik:** Brunnen geht RUNTER (Diagnose: Was liegt darunter?). Leiter geht RAUF (Transformation: Was wird möglich?). Zusammen bilden sie den U-Bogen der Schritte 5–7.

### V.2 — Die Gabel (Schritt 4)

```
LERNMOMENT (Lebenserfahrung)
       │
       ├── BEWUSST verarbeitet ──→ Leiter (Schritt 6→7)
       │
       └── UNBEWUSST ──→ sinkt in den Körper (P1) ──→ Brunnen füllt sich (Schritt 5)
```

Am Gabel-Punkt entscheidet sich: Leiter-Pfad oder Brunnen-Füllung. Der **Anker** ist das IC-Werkzeug, das hier ansetzt.

### V.3 — EG-HD-Neef Kehrseiten-Brücke

```
HD offene Zentren → EG-Triade → EG-Typ → Leidenschaft → blockiertes Bedürfnis → Falle
```

Trianguliert drei Modelle zur Kausalkette der Wunde (→ III.8).

### V.4 — Zwei-Richtungen-Prinzip

| Richtung | Wer | Von → Nach |
|---|---|---|
| **Analyse** | System / Pipeline | Außen → Innen: P1→P7, Schritt 1→6 |
| **Vermittlung** | App / User | Innen → Außen: Sicherheit zuerst, Tiefe bei Bereitschaft |

### V.5 — 3 Erkenntniswege

| Weg | Was | IC-Status |
|---|---|---|
| **A: Konzeptuell** | Systeme lesen, Muster verstehen | ✅ Kernstärke |
| **B: Erfahrungsbasiert** | Körper spüren, Meditation, Praxis | 🔴 Noch auszubauen |
| **C: Relational** | Im Spiegel anderer, Beziehungsarbeit | 🔴 Fehlt weitgehend |

**Klärung:** 3 praktische Lernmodi, nicht 3 ontologische Dimensionen. Die 4. Dimension (Transpersonal/Spirit) wird von IC anerkannt, aber nicht operationalisiert (→ V.6: Die Schwelle).

### V.6 — Die Schwelle

Wo IC's Werkzeuge enden und Stille beginnt. IC sagt: *"Hier enden die Systeme. Was du in der Stille findest, ist deins."*

Wo sie erscheint: Brunnen unter Schicht 4 (Quelle), Leiter Stufe 5 (Ernten), Anker: Sitting With, Konvergenz-Moment.

### V.7 — Die Wahl (Meta-Qualität)

Ra's 22. Archetyp ("Der Narr / Die Wahl") als pervasierende Meta-Qualität: An jedem IC-Schritt steht eine Wahl (hinschauen oder ausweichen). Nicht ein Schritt, sondern die Qualität, die den Prozess überhaupt möglich macht.

### V.8 — IC's Quadrantenstruktur

| | DIAGNOSTISCH | TRANSFORMATIV |
|---|---|---|
| **INDIVIDUELL** | Brunnen × Prisma | Leiter × Experiment |
| **RELATIONAL** | Mandala × P4 | Experiment im Feld (Weg C) |

---

## VI. Content-Dimensionen (7D-Inhaltsraum)

Jeder IC-Inhalt hat eine Adresse in 7 Dimensionen:

| # | Dimension | Frage | Werte | Quelle |
|---|---|---|---|---|
| 1 | **Schritt** | WELCHES THEMA im Prozess? | 1–9 | 9-Schritte-Prozess |
| 2 | **Domäne** | WO im Leben? | 12 Domänen | Mandala |
| 3 | **Tiefe** | WIE TIEF engagiert? | 1–4 (Spiegel→Experiment) | Handbuch-Schichten |
| 4 | **Perspektive** | DURCH WELCHE LINSE? | 1–7 | Prisma |
| 5 | **Frage** | WELCHE ART Frage? | B/H/D/I | Grammatik |
| 6 | **Register** | IN WELCHER SPRACHE? | M/T/P | Stimme |
| 7 | **Zeitkontext** | WANN? | statisch / transit / overlay | Gezeiten |

**Adressierungsbeispiel:**
> Schritt 5 (Diagnose) × Domäne 2 (Liebe) × Tiefe 3 (Prozess) × P4 (Verbindung) × INTERACTING × Transformation × Transit-aktiv
> = *"Saturn transitiert dein 7. Haus. Dein offenes Emotionalzentrum verstärkt die Gefühle deines Partners. Dein EG-Typ 2 kompensiert mit Helfen. Diese Woche: Beobachte, wann du hilfst ohne gefragt zu werden."*

**Theoretisches Maximum:** 9 × 10 × 4 × 7 × 4 × 3 × 3 = 90.720 Inhaltspunkte.
In der Praxis: nur sinnvolle Kombinationen. Die meisten Zellen bleiben leer.

### Tiefe ↔ Erkenntnisweg

| Tiefe | Name | Erkenntnisweg | Was der User tut |
|---|---|---|---|
| 1 | Spiegel | Weg A (Konzeptuell) | Liest, was die Systeme sagen |
| 2 | Muster | Weg A → B | Erkennt Alltagsmuster, beginnt zu spüren |
| 3 | Prozess | Weg B (Erfahrungsbasiert) | Arbeitet körperlich/emotional |
| 4 | Experiment | Weg B + C (Relational) | Probiert Verhalten im Beziehungsfeld |

---

## VII. 16er-Matrix (Content-Produktionsprinzip)

**Was:** 4 Brunnen-Schichten × 4 Grammatik-Fragen = 16 Content-Zellen.
**Wo:** Primär für Brunnen-Content (Schritt 6). Grundsätzlich anwendbar auf jede Domäne.
**Herkunft:** Chat 7 (26.–27. Feb), operationalisiert These 3.

```
                  BEING          HAVING         DOING          INTERACTING
                  Was bin ich?   Was habe ich?  Was tue ich?   Wie interagiere ich?
    ┌────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
 S1 │ Verhalten  │  Wie zeige   │  Welche      │  Was tue ich │  Wie wirke   │
    │            │  ich mich?   │  Gewohnheiten│  automatisch?│  ich auf     │
    │            │              │  habe ich?   │              │  andere?     │
    ├────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
 S2 │ Muster     │  Welches     │  Was fehlt   │  Welche      │  Welches     │
    │            │  Selbstbild  │  immer       │  Schleifen   │  Beziehungs- │
    │            │  steckt      │  wieder?     │  drehe ich?  │  muster?     │
    │            │  dahinter?   │              │              │              │
    ├────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
 S3 │ Überzeu-   │  Was glaube  │  Was glaube  │  Was glaube  │  Was glaube  │
    │ gungen     │  ich über    │  ich zu      │  ich tun     │  ich über    │
    │            │  mich?       │  brauchen?   │  zu müssen?  │  Beziehungen?│
    ├────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
 S4 │ Kern-      │  Wer bin ich │  Was wurde   │  Was durfte  │  Wie wurde   │
    │ verletzung │  wenn alles  │  mir früh    │  ich nicht?  │  Nähe für    │
    │            │  wegfällt?   │  genommen?   │              │  mich?       │
    └────────────┴──────────────┴──────────────┴──────────────┴──────────────┘

    Diagonaler Makro-Pfad: Oben-links (leicht) ──→ Unten-rechts (intim)
```

**Sicherheitsregel:** Progressive Enthüllung. S4 × INTERACTING (unten-rechts) erst bei nachgewiesener Bereitschaft (Nervensystem-Check).

---

## VIII. Content-Typen und Erzählprinzipien

### Content-Typen (traversieren Schritte)

| Typ | Was | Schritte |
|---|---|---|
| **Beschreibung** | Standard-Interpretation eines Elements | 1–3 primär |
| **Pattern Trap** | Kombinatorische Konfigurationsfalle | 5–6 |
| **Transformation Arc** | Vollständiger Bogen Wunde→Falle→Gabe | 5–7 |
| **Konvergenz-Insight** | Mehrere Systeme zeigen auf dasselbe | 2–5 (Konvergenz-Moment) |
| **Experiment** | Konkrete Verhaltensänderung zum Ausprobieren | 7 (Leiter S4) |
| **Transit-Kontext** | Zeitliche Aktivierung eines Musters | 8 |

### Makro-Erzählpfad

Diagonal durch die 16er-Matrix: Von oben-links (Verhalten × BEING — leicht, zugänglich) nach unten-rechts (Kernverletzung × INTERACTING — intim, verletzlich). Das ist der narrative Gesamtbogen des IC.

### Mikro-Erzählprinzip (pro Content-Zelle)

5 Schritte: BENENNEN → ÜBERSETZEN → VERORTEN → REFLEXION → EINLADUNG (→ IV.3)

---

## IX. Navigations-Achsen (aus kern-Docs: IC_Fundament Modell A)

Die 5 Achsen aus den Originaldokumenten — wie der User durch IC navigiert:

| Achse | Frage | Metapher | Verortung | Möglicher View |
|---|---|---|---|---|
| **Mandala / Landkarte** | WO in meinem Leben? | Räumlich | App-UI Startbildschirm | ✅ Eigener View (Home) |
| **Handbuch** | WAS bedeutet das? | Vertikal (Tiefe) | Content-Schichten 1–4 | Tiefenachse in jedem View + eigenständiger Browse |
| **Zeitlinie** | WANN ist das aktiv? | Temporal | Transite, Zyklen | ✅ Eigener View |
| **Flussdiagramm** | WIE hängt das zusammen? | Relational (Bridges) | KG-Graph | Eigener View (Power-User) |
| **Heldenreise** | WOHIN gehe ich? | Narrativ (geführt) | 7 Phasen × Domäne | Eigener View ODER im Mandala integriert |

**Beziehung Handbuch ↔ Mandala:** Das Handbuch ist KEIN separater Tab neben dem Mandala. Es ist die Tiefendimension (1–4), die in JEDEM View existiert. Man klickt eine Domäne im Mandala → sieht Tiefe 1 (Spiegel) → kann tiefer gehen. Das Handbuch KANN zusätzlich als eigenständiger Browse-Modus existieren (Nachschlagewerk ohne Domänen-Kontext).

---

## X. Infrastruktur-Bausteine

| Baustein | Funktion | Wo |
|---|---|---|
| **Knowledge Graph** | Verbindet alle Inhalte (Nodes, Edges, 5 Schichten A–E) | Backend |
| **Pipeline** | Extraktion: Quellen → KG-Nodes (extract_entities → meanings → relationships → processes) | Backend |
| **State Detection** | Erkennt aktuelle User-Phase automatisch | Backend → UX |
| **15 Backend-Dimensionen** | Technische Persönlichkeits-Grammatik (mapped auf 7 Prisma-Perspektiven) | Pipeline |
| **Lens-Switcher** | Synthese-Meta-View (Default) vs. Original-Modus (Opt-in) | Frontend |
| **Staffel-Logik** | System-Freischaltung über Staffeln (S1: Klasse A, S2: +B, S3: +C/D) | Content-Management |

### KG 5 Schichten

| Schicht | Name | Inhalt |
|---|---|---|
| A | Rohsignal | Planetenpositionen, Säulen, Ephemeriden |
| B | System-Konzepte | HD-Typ, BaZi-Element, Astro-Aspekt |
| C | Cross-System-Muster | Innere Strategie, Brücken-Insights |
| D | Handbuch-Text | Sprachliche Übersetzung für den User |
| E | User-Aktion | Impuls, Experiment, Reflexionsfrage |

### KG Edge-Typen

| Edge | Bedeutung |
|---|---|
| maps_to | Gleiche Bedeutung, anderes System |
| extends | Tiefere Frequenz (HD→GK) |
| contradicts | Echter Widerspruch → Reflexion |
| triggers | Zeitliche Aktivierung |
| correlates | Statistische Assoziation |
| deepens | Vertiefung A→B→C |
| influences | Kausaler Einfluss |

---

## XI. Verwechslungsschutz

| Begriff | Was es IST | Was es NICHT ist | Anzahl |
|---|---|---|---|
| **Schritte** | WELCHES THEMA im Erkenntnisprozess | ≠ Phasen, ≠ Tiefe | 9 |
| **Phasen** | WIE der User die App erlebt | ≠ Schritte, ≠ Perspektiven | 7 |
| **Perspektiven** (Prisma) | DURCH WELCHE LINSE (horizontal) | ≠ Tiefe, ≠ Dimensionen | 7 |
| **Tiefe** (Handbuch) | WIE TIEF der User einsteigt | ≠ Schritte, ≠ Perspektiven | 4 |
| **Dimensionen** (Backend) | TECHNISCHE Grammatik für Pipeline | ≠ Perspektiven | 15 |
| **Domänen** (Mandala) | WO im Leben | ≠ Dimensionen, ≠ Perspektiven | 10 |
| **Fragen** (Grammatik) | WELCHE ART Frage (B/H/D/I) | ≠ Perspektiven, ≠ Tiefe | 4 |
| **Register** (Stimme) | IN WELCHER SPRACHE (M/T/P) | ≠ Tiefe, ≠ Perspektiven | 3 |
| **Schichten** (Brunnen) | WIE TIEF im Brunnen | ≠ Tiefe (Handbuch), ≠ KG-Schichten | 4 |

---

## XII. Zahlen auf einen Blick

| Was | Anzahl |
|---|---|
| Thesen | 7 |
| Prinzipien | 5 |
| Spannungsfelder | 4 |
| Schritte (Prozess) | 9 |
| Phasen (User Journey) | 7 |
| Einstiegskanäle | 3 |
| Quellsysteme | 10 |
| Domänen (Mandala) | 12 |
| Mandala-Ringe | 3 |
| Bedürfnisse (Wurzeln) | 9 |
| Anker-Komponenten | 3 |
| Brunnen-Schichten | 4 |
| Leiter-Stufen | 5 |
| Prisma-Perspektiven | 7 |
| Grammatik-Fragen | 4 |
| Stimme-Register | 3 |
| Zeitgeist-Fallen | 8 |
| 16er-Matrix-Zellen | 16 (4 Schichten × 4 Fragen) |
| Mikro-Erzählschritte | 5 |
| Content-Dimensionen | 7 |
| Backend-Dimensionen | 15 |
| KG-Schichten | 5 (A–E) |
| KG-Edge-Typen | 7 |
| EG-Typen | 9 |
| Handbuch-Tiefen | 4 |
| Erkenntniswege | 3 |
| Navigations-Achsen | 5 |
| Meta-Strukturen | 8 |

**Schritt-gebundene Bausteine:** 11
**Querschnitt-Werkzeuge:** 4
**Meta-Strukturen:** 8
**Infrastruktur-Bausteine:** 6+

---

## XIII. App-Spaces (Erster Entwurf)

### Grundprinzip: Vom Moment, nicht vom Modell

Die 5 Navigationsachsen (kern-Docs) beschreiben, wie man auf Daten ZUGREIFEN kann. Aber der User denkt nicht in Achsen — er denkt in Momenten: "Wer bin ich?", "Wo tut es weh?", "Was ist gerade los?"

Das Zwei-Richtungen-Prinzip (V.4) bestätigt: Vermittlung geht innen→außen (Sicherheit zuerst), nicht außen→innen (Architektur-Logik).

### 3+1 Spaces statt 5 Tabs

| Space | User-Frage | Primäre IC-Modelle | Metapher |
|---|---|---|---|
| **JETZT** (Home) | Was ist gerade relevant für mich? | State Detection, Konvergenz, Transite | Dein persönlicher Radar |
| **KARTE** (Erkunden) | Wer bin ich, wo zeigt sich das? | Mandala, Prisma, Handbuch, Chart | Deine Landkarte |
| **WERKSTATT** (Vertiefen) | Woran arbeite ich, wie komme ich raus? | Brunnen, Leiter, Anker, Pattern Traps | Deine Werkstatt |
| **ZEIT** (Timing) | Was kommt, was wirkt gerade? | Gezeiten, Pfad, Konvergenz | Dein Kalender |

### JETZT (Startbildschirm)

Personalisierte Oberfläche: "Was ist gerade relevant?"

- Aktive Transite (Top 1–3 Konvergenzen)
- Offene Arbeit (wenn User ein Thema hat)
- Phase-Fortschritt pro Domäne
- Einladung zum Stöbern

Dahinter: State Detection + Konvergenz-Engine + Biografie-Layer.

### KARTE (Erkunden)

Hauptansicht = **Mandala** (12 Domänen, 3 Ringe, Phase-Indikator pro Domäne).

Klick auf Domäne → Domänen-Detail mit **Handbuch-Tiefe** als Gleiter:
- Tiefe 1 (Spiegel): Was die Systeme sagen
- Tiefe 2 (Muster): Cross-System-Bridges, Alltagsmuster
- Tiefe 3 (Prozess): Hier beginnt Arbeit → leitet zu WERKSTATT über
- Tiefe 4 (Experiment): Konkreter Versuch → leitet zu WERKSTATT über

Zusätzlich:
- **Lens-Switcher**: Synthese (Default) / Original-Modus (Opt-in)
- **Mein Chart**: Referenz-Ansicht (Rohdaten aller 10+ Systeme)
- **Flussdiagramm**: Optionaler Layer für Cross-System-Bridges (Power-User)

### WERKSTATT (Vertiefen + Transformieren)

Das **Herzstück** der App. Geführter Brunnen→Leiter-Flow:

1. **Thema wählen** (aus Mandala, JETZT, oder direkt)
2. **Brunnen-Abstieg**: Schicht 1→2→(Nervensystem-Check)→3→4→Schwelle
3. **Gabel-Bewusstsein**: Anker-Werkzeug am Übergang
4. **Leiter-Aufstieg**: Sehen→Fühlen→Verstehen→Handeln→Ernten
5. **Experiment**: Konkretes Verhalten für die nächsten Tage

Nervensystem-Check als Gate vor jeder Tiefenschicht ≥3.
Zeitgeist-Fallen als Kontext-Hinweise wenn relevant.

### ZEIT (Timing)

Timeline mit allen Systemen:
- Aktive Transite (HD, Astro, BaZi Luck Pillar, Jyotish Dasha, Maya Wavespell)
- Konvergenz-Highlights: "3+ Systeme zeigen auf Domäne X"
- Klick → springt in KARTE (Domäne) oder WERKSTATT (wenn Trap aktiv)

### Was KEIN eigener View wird

| IC-Element | Stattdessen |
|---|---|
| Heldenreise (7 Phasen) | Impliziter roter Faden: Phase-Indikator im Mandala, Empfehlungen in JETZT |
| Handbuch | Tiefendimension INNERHALB jedes Views + eigenständiger Browse in KARTE |
| Flussdiagramm | Optionaler Layer in KARTE |
| Grammatik (B/H/D/I) | Backend: Content-Produktion, User sieht es nicht |
| Stimme (3 Register) | Backend: IC wechselt automatisch |
| 16er-Matrix | Backend: Content-Raster |

### Baustein → Space Mapping

| IC-Baustein | Space | Als was |
|---|---|---|
| Mandala | KARTE | Visuelles Navigations-Element |
| Handbuch (4 Tiefen) | KARTE (Gleiter pro Domäne) | Tiefe 1→4 |
| Zeitlinie | ZEIT | Kalender mit Konvergenz |
| Flussdiagramm | KARTE (opt. Layer) | Power-User-Modus |
| Heldenreise | ÜBERALL (implizit) | Phase-Indikator |
| Brunnen | WERKSTATT (erste Hälfte) | Geführter Abstieg |
| Leiter | WERKSTATT (zweite Hälfte) | Geführter Aufstieg |
| Anker | WERKSTATT (Gabel-Punkt) | Pop-up/Overlay |
| Pattern Traps | KARTE → WERKSTATT | Trigger für Arbeits-Flow |
| Prisma | KARTE (Filter) | Lens-Switcher |
| Wurzeln | KARTE + WERKSTATT | Wunde-Kette + Domänen-Detail |
| EG-Brücke | WERKSTATT (Diagnose) | Teil des Pattern-Trap-Flows |
| Zeitgeist-Fallen | WERKSTATT (Kontext) | Warnung wenn relevant |
| State Detection | JETZT | Personalisierung |
| Konvergenz-Engine | JETZT + ZEIT | Highlights |

### 5 User-Momente → Spaces

| Moment | Was der User fühlt | Space |
|---|---|---|
| **Erster Kontakt** | "Zeig mir wer ich bin" | Onboarding → KARTE |
| **Stöbern** | "Erzähl mir mehr" | KARTE (Mandala + Tiefe) |
| **Etwas brennt** | "Hier tut es weh" | JETZT → WERKSTATT |
| **Was ist los?** | "Was ist gerade aktiv?" | ZEIT → KARTE/WERKSTATT |
| **Dranbleiben** | "Ich arbeite an meinem Thema" | WERKSTATT (laufend) |

---

## XIV. Abgleich: Externe System-Diskussion (31. März 2026)

### XIV.1 Was die externe Diskussion vorschlägt

Ein phasenbasiertes Modell mit 4 Schichten:

| Schicht | Was | Individuell? | IC-Entsprechung |
|---|---|---|---|
| **Signatur** | Wer bin ich? (Geburtsdaten) | ✅ Voll individuell | Quellsysteme (Schritt 1) |
| **Signatur×Zeit** | Wann ist was dran? | ✅ Individuell | Gezeiten + Pfad (Schritt 8) |
| **Phase/Praxis** | Wie arbeite ich damit? | ⚡ Werkzeug allgemein, Inhalt individuell | Leiter + Anker (Schritt 4+7) |
| **Rahmen** | Wohin das alles führt | Allgemein | Thesen + Ra-Integration |

**Phasen-Mapping der Diskussion:**

| Phase | System/Konzept | IC-Entsprechung |
|---|---|---|
| 1 Schwelle | Logotherapie, Stoizismus, Polyvagal, Mythologie | Schritt 5 (Diagnose), Anker (Nervensystem-Check) |
| 2 Orientierung | HD, Gene Keys, I Ging, Big Five, Narrationspsychologie | Schritt 1–3 (Eintritt→Verortung) |
| 3 Schälen | Enneagramm, Voice Dialogue, Focusing, Shadow Work, Aufstellungsarbeit | Schritt 5–6 (Diagnose→Vertiefung), EG-Brücke |
| 4 Integration | IFS, Somatic Experiencing, Breathwork, Ra-Katalysator, Musik/Kunst | Schritt 6–7 (Vertiefung→Transformation), Brunnen→Leiter |
| 5 Ausdruck | GfK, Ikigai, Max-Neef, HD-Praxis | Schritt 7–8 (Transformation→Zeitkontext), Experiment |
| 6 Transzendenz | GdE, Advaita, Zen, Sufismus | Schritt 9 (Graduation), Schwelle, Wahl |

### XIV.2 Was IC bereits abdeckt ✅

| Konzept aus Diskussion | IC-Baustein | Status |
|---|---|---|
| HD als Struktur-Signatur | Quellsystem #1, Klasse A | ✅ Kernstück |
| BaZi als Ressourcen-/Zeitkarte | Quellsystem, Klasse A + Gezeiten | ✅ Vollständig |
| Jyotish inkl. Dashas | Quellsystem, Klasse B + Gezeiten | ✅ Inkl. individuelle Zeitphasen |
| Enneagramm als Motivationsstruktur | Via EG-Brücke (HD→EG) + Wunde-Kette | ✅ Integriert |
| Gene Keys (I Ging × HD) | Quellsystem, Klasse B | ✅ Lizenzthema offen |
| Numerologie | Quellsystem | ✅ Inkl. Jahreszyklen |
| Konvergenz-These | These 4 | ✅ Kern-These |
| Schichten-These | These 3, Brunnen | ✅ Operationalisiert |
| IFS-Prinzip | Leiter Stufe 3 (Teile-Arbeit) | ✅ Als Prinzip übernommen |
| Polyvagal / Nervensystem | Anker, Nervensystem-Check | ✅ Operationalisiert |
| Max-Neef Bedürfnisse | Wurzeln (9 Bedürfnisse) | ✅ Vollständig |
| Ra/GdE (Ethische Ausrichtung) | Z1 §5 (Ra-Beiträge), Z3 C6–C8 | ✅ Extensiv integriert |
| Körper-zuerst-Prinzip | Prinzip 5, Anker, Gabel | ✅ Architekturprinzip |
| Phase×System Zuordnung | Z2 (7 Phasen mit Werkzeug-Zuordnung) | ✅ Existiert |
| Bindungstheorie als P4-Quelle | Prisma P4 (Verbindung/Beziehung) | ✅ Eigenständigkeitstest bestanden |
| "Kein System alleine reicht" | Architekturprinzip: Multi-System | ✅ Kernidee des IC |

### XIV.3 Was IC NICHT hat / wo Lücken sind 🔴

| Konzept aus Diskussion | Was es bieten würde | IC-Status | Empfehlung |
|---|---|---|---|
| **Kabbala operationalisiert** (Tikun, Gematria, Baum des Lebens) | Individuelle Seelen-Aufgabe aus Name+Datum, Bewusstseins-Karte | Nur als "Ur-System" erwähnt, nicht operationalisiert | 🟡 **Prüfen:** Gematria/Tikun aus Name ableitbar → könnte Quellsystem-Ergänzung sein |
| **I Ging als eigenständiges Weisheitssystem** (nicht nur via HD/GK) | 64 Zustände + Übergänge als Wandlungskarte | Implizit via HD-Tore, nicht eigenständig | 🟡 **Prüfen:** "Jetzt-Moment-Reading" (aktuelles Hexagramm × persönliches Chart) |
| **Hermetik (7 Prinzipien)** | Universalgesetze als philosophischer Rahmen | Nicht vorhanden | 🔵 **Niedrig:** Thesen+Prinzipien+Ra decken den Rahmen ab |
| **Sufismus / Nafs-Modell** | 7 Stufen der Seele als Entwicklungspfad | Nicht vorhanden | 🔵 **Niedrig:** Parallele zu Leiter, aber anderes Framework |
| **Reich / Bioenergetik** | Charakterpanzer, Körper-gespeichertes Trauma | Implizit in P5+Anker, nicht explizit | 🟡 **Bestätigt P5:** Validiert Anker-Konzept, könnte Leiter Stufe 2 stärken |
| **Schamanismus / Soul Retrieval** | Seelenteile zurückholen | Nicht vorhanden | 🔵 **Extern:** IC kann darauf VERWEISEN, nicht implementieren |
| **Narrationspsychologie** | Lebensnarrativ-Analyse aus Text | Nicht vorhanden | 🟢 **Hohe Relevanz:** KI kann Narrativ-Muster aus User-Text ableiten |
| **Focusing (Gendlin)** | Felt Sense, Körperbotschaft vor dem Wort | Teilweise in Anker (Sitting With) | 🟡 **Stärkt Anker:** Könnte Sitting-With-Komponente verfeinern |
| **Aufstellungsarbeit** | Familiensystem-Muster | Nicht vorhanden | 🔵 **Extern:** IC kann auf Familien-Muster HINWEISEN (Epigenetik-Layer) |
| **Astrokartographie** | Geografische Dimension aus Geburtsdaten | Nicht vorhanden | 🟡 **Prüfen:** Vollautomatisch ableitbar, einzigartig |
| **Praxis-Empfehlungs-Engine** | "In deiner Phase empfehle ich: IFS / Breathwork / ..." | IC empfiehlt keine externen Praktiken | 🟢 **Hohe Relevanz:** IC-Alleinstellung: Phase×Signatur→Praxis-Empfehlung |
| **NLP/Voice-Analyse** | EG-Typ + Bindungsstil aus Text/Stimme | Nicht vorhanden | 🟢 **Hohe Relevanz:** Ergänzt Chart-basierte Ableitung |
| **"Jetzt-Uhrzeit" als Datenpunkt** | I-Ging-Moment-Reading × persönliches Chart | Nicht vorhanden | 🟢 **Hohe Relevanz:** Macht App situativ statt nur statisch |
| **Epigenetik / Familienmuster** | Transgenerationale Trauma-Layer | Nicht vorhanden | 🟡 **Prüfen:** Passt zu Brunnen Schicht 4, braucht Narrativ-Input |

### XIV.4 Die wichtigsten Impulse (sortiert nach Relevanz)

**🟢 HOCH — Sollte in IC aufgenommen werden:**

1. **Praxis-Empfehlungs-Engine:** IC sagt nicht nur "Das ist dein Muster" (Diagnose), sondern "In deiner Phase wäre XY hilfreich" (Praxis). Leiter-Stufen könnten externe Methoden EMPFEHLEN (nicht implementieren): IFS für Stufe 3, Somatic für Stufe 2, Breathwork für Integration.

2. **"Jetzt-Moment" als Datenpunkt:** Jedes Mal wenn der User die App öffnet: aktuelle Uhrzeit × aktuelle Transite × persönliches Chart = situativer Snapshot. Das macht IC LEBENDIG statt statisch. Entspricht dem I-Ging-Prinzip: Der Moment des Fragens ist selbst Information.

3. **Narrativ-Analyse (NLP):** Eine offene Narrativ-Frage im Onboarding ("Was beschäftigt dich gerade am meisten?") → KI leitet daraus ab: EG-Cluster, aktuelle Phase, emotionalen Zustand, Einstiegspunkt. Später: fortlaufende Text-Analyse aus Reflexions-Eingaben.

**🟡 MITTEL — Prüfen und ggf. integrieren:**

4. **Kabbala/Gematria als Quellsystem:** Name → Zahlencode → Tikun (Seelen-Aufgabe). Vollautomatisch ableitbar. Würde IC ein weiteres System geben, das KEINEN anderen Input braucht.

5. **Astrokartographie:** "Wo auf der Erde bist du am stärksten?" — vollständig aus Geburtsdaten ableitbar. Eigene Domäne oder Zusatz zu Domäne 5 (Beruf)/6 (Zuhause).

6. **Epigenetik-Layer:** Narrative Fragen zu Familienmustern ("Welche Muster kennst du aus deiner Familie?") → automatisches Flagging von Brunnen-Schicht-4-Themen.

**🔵 NIEDRIG — Bewusst extern lassen:**

7. Hermetik, Sufismus, Schamanismus, Bioenergetik: Wertvolle Rahmen/Praktiken, aber IC implementiert sie nicht. IC kann darauf VERWEISEN in der Praxis-Empfehlungs-Engine.

### XIV.5 Das 4-Schichten-Modell — Vergleich mit IC

Die externe Diskussion schlägt vor:

```
SIGNATUR (individuell, geburtsbasiert)
    HD + BaZi + Jyotish + Numerologie + Gene Keys + [Kabbala?]
        ↓
SIGNATUR×ZEIT (individuell-dynamisch)
    Jyotish Dashas + BaZi Luck Pillars + HD Transite + [Jetzt-Moment?]
        ↓
PRAXIS (universell, individuell befüllt)
    Je nach Phase: IFS / Somatic / Breathwork / Aufstellung / ...
        ↓
RAHMEN (universell)
    GdE / Hermetik / Sufismus → Gibt Richtung und Sinn
```

**IC hat das bereits — unter anderen Namen:**

| Externe Schicht | IC-Entsprechung | Vollständigkeit |
|---|---|---|
| Signatur | 10 Quellsysteme → Schritt 1 | ✅ (Kabbala/Gematria offen) |
| Signatur×Zeit | Gezeiten + Pfad → Schritt 8 | ✅ (Jetzt-Moment fehlt) |
| Praxis | Leiter → Schritt 7, Anker → Schritt 4 | 🟡 (Externe Empfehlungen fehlen) |
| Rahmen | 7 Thesen + 5 Prinzipien + Ra-Integration | ✅ |

### XIV.6 Datenpunkte — Was IC nutzt vs. nutzen könnte

| Datenpunkt | Aktuell in IC | Könnte liefern | Aufwand |
|---|---|---|---|
| **Geburtsdatum** | ✅ | HD, BaZi, Astro, Maya, Jyotish, Numerologie, GK | Basis |
| **Geburtszeit** | ✅ | Präzise Charts, Dashas, ASC, Häuser | Basis |
| **Geburtsort** | ✅ | HD, Jyotish, Astrokartographie | Basis |
| **Name** | 🟡 (Numerologie) | + Kabbala/Gematria/Tikun | Gering |
| **Offene Narrativ-Frage** | 🔴 Fehlt | EG-Cluster, Phase, Emotionszustand, Einstieg | Gering |
| **Jetzt-Uhrzeit** | 🔴 Fehlt | Situativer Snapshot, I-Ging-Moment × Chart | Minimal |
| **Reflexions-Texte** | 🔴 Fehlt | Fortlaufende NLP-Analyse, EG-Validierung | Mittel |
| **Familienmuster-Fragen** | 🔴 Fehlt | Epigenetik-Layer, Brunnen S4 Flagging | Gering |
| **Stimme** (optional) | 🔴 Fehlt | Voice-Persönlichkeitsprofil | Hoch |
| **HRV/Wearable** (optional) | 🔴 Fehlt | Nervensystem-Validierung, Chronotyp | Hoch |

**Minimal-Set** (vollautomatisch): Datum + Zeit + Ort + Name = alles Geburts-basierte
**Optimal-Set** (+wenig Aufwand): + Narrativ-Frage + Jetzt-Uhrzeit + Familienmuster
**Erweiterung** (später): Stimme, HRV, Reflexions-Texte

---

## XV. Phasen-Vergleich: 6 externe Phasen vs. IC

### Die 6 externen Phasen (aus Diskussion)

| # | Extern | Was | IC-Entsprechung | Unterschied |
|---|---|---|---|---|
| 1 | **Schwelle** | Krise, alter Rahmen bricht | Einstiegstyp "Schmerz" (→ Schritt 5 direkt) | IC behandelt Krise als Einstiegsmodus, nicht als eigene Phase |
| 2 | **Orientierung** | Wer bin ich? Erste Landkarten | Schritte 1–3 (Eintritt→Wiedererkennung→Verortung) | IC differenziert STÄRKER: 3 Schritte statt 1 Phase |
| 3 | **Schälen** | Was bin ich NICHT? Dekonditionierung | Schritte 5–6 (Diagnose→Vertiefung) | IC hat Pattern Traps + Brunnen — granularer |
| 4 | **Integration** | Schatten+Wunde+Körper zusammen | Schritte 6–7 (Vertiefung→Transformation) | IC hat Brunnen→Leiter als Paar |
| 5 | **Ausdruck** | Authentisch leben und geben | Schritte 7–8 (Transformation→Zeitkontext) | IC verbindet mit Timing (Gezeiten) |
| 6 | **Transzendenz** | Jenseits des Selbst | Schritt 9 (Graduation) + Schwelle | IC hat "Die Schwelle" als architekturelles Konzept |

### Was IC hat, das die externe Version NICHT hat

| IC-Alleinstellung | Warum wichtig |
|---|---|
| **Schritt 4: Verkörperung** als eigener Schritt | Kein externes System hat einen dedizierten "Körper-Checkpoint" VOR der Diagnose. IC: Prinzip 5 (Körper hat Vorrang). |
| **Gabel-Punkt** | Die bewusst/unbewusst-Weiche am Verkörperungs-Moment. In keiner der externen Phasen vorhanden. |
| **Konvergenz-Moment** | Kein eigener Schritt, aber markiertes Erlebnis (3+ Systeme zeigen auf dasselbe). Extern nicht vorhanden. |
| **Nicht-lineare Domänen** | User kann in Beruf bei Phase 5 und Liebe bei Phase 2 sein. Extern: linear gedacht. |

### Was die externe Version hat, das IC überdenken könnte

| Extern | Was es bietet | IC-Implikation |
|---|---|---|
| **"Schwelle" als explizite Phase** | Der Krisenmoment wird würdevoll benannt, nicht nur als "Einstiegskanal" | IC könnte die Krise als eigenständigen Moment stärker würdigen (UX in JETZT-Space) |
| **"Ausdruck/Service" als Phase** | Expliziter Übergang von "an mir arbeiten" zu "in die Welt geben" | IC hat das in Graduation, aber der Übergang "jetzt gebe ich zurück" könnte expliziter sein |

### Bewertung

IC's 9 Schritte + 7 Phasen sind **differenzierter und besser** als die 6 externen Phasen. Die externe Version bestätigt den Grundbogen, hat aber weniger Auflösung. IC's Alleinstellung (Verkörperung, Gabel, Konvergenz, nicht-lineare Domänen) bleibt bestehen.

---

## XVI. Was bereits existiert (gefundene Konzepte)

Viele der in der externen Diskussion genannten Ideen existieren BEREITS in den kern-Dokumenten:

### XVI.1 Dynamische Texte / Transit-Overlay ✅

**Fundstelle:** IC_Gesamtwerk_Kap2 v1.1 (Kap. 14):
> *"Transit-Overlay: Die Zeitqualität wird als dritte Verortungsdimension integriert — 'Dein Chart zeigt X. Gerade jetzt, in der aktuellen Zeitqualität, zeigt sich das besonders in…'"*

**Drei Text-Modi im Leitdokument (E-21):**

| Modus | Was | Beispiel |
|---|---|---|
| **Statisch** | Geburts-Chart (unveränderlich) | "Dein Tor 34 ist definiert" |
| **Dynamisch (Transit)** | Aktuelle Zeitqualität | "Die Sonne steht heute in Tor 41" |
| **Overlay** | Statisch × Dynamisch | "Tor 41 aktiviert DEINEN Kanal 41–30 — das Thema Neuanfang ist für DICH gerade besonders lebendig" |

→ Der "Jetzt-Moment" war also **bereits konzipiert**. Er muss nur implementiert werden (JETZT-Space).

### XVI.2 IFS (Internal Family Systems) ✅

**Umfangreich integriert!** Fundstellen:

- **Z3 Leiter Stufe 3:** "Welcher Teil schützt die Wunde?" — operationalisiert als Format B ("Der innere Dialog", 10–20 Min Reflexion)
- **Z3 Brunnen Cross-Framework:** IFS-Teile-Schichtung (Manager→Firefighter→Exile→Self) parallel zu Brunnen-Schichten
- **Fundament Ebene 5:** "Psychodynamik / Innere Struktur: Enneagramm (Kernwunde), IFS-Konzepte"
- **Z3 offene Frage #3 (🔴 HOCH):** "IFS-Prinzip operationalisieren. Angeleiteter Dialog, keine vollständige IFS-Sitzung."

**Abgrenzung bewusst dokumentiert:** IC führt NICHT IFS-Unburdening/Reparenting durch. IC nutzt die Frage-Logik als Reflexions-Tool. Bei schweren Wunden: Verweis auf professionelle Begleitung.

### XVI.3 EG-Situativfragen / Selbsteinschätzung ✅

**Fundstelle:** IC_Fundament v06, Kap. III.5b:

| Schritt | Was | Methode |
|---|---|---|
| 1 | HD→EG Triade (automatisch) | Chart-Ableitung (offene Zentren → Triade) |
| 2 | Triade→Subtyp (situativ) | Reflexionsfrage: "Erkennst du dich eher in 5, 6 oder 7?" |
| 3 | Hypothese-Verfeinerung | Hängende Tore im Chart als zweiter Datenpunkt |

> "Das ist sogar besser als ein reines Self-Assessment, weil der User zwei unabhängige Datenpunkte hat: den Chart und die eigene Erfahrung."

### XVI.4 Reflexionsfragen als Kern-Prinzip ✅

**Überall vorhanden:**
- KG Schicht E = "Impuls, Experiment, Reflexionsfrage"
- 5-Schritt-Mikro-Erzählprinzip: Schritt 4 = REFLEXION ("Was löst das in dir aus?")
- Leitdokument: "Invitational Language: Alle Reflexionsfragen sind einladend, nie direktiv"

### XVI.5 Jyotish-Mantras / Upayas ✅

**Fundstelle:** Z3 Leiter Cross-Framework:
> "Jyotish: Upayas: Mantras, Edelsteine, Fasten" — Stufe 4 (Handeln)

→ Mantras als personalisierte Praxis sind **bereits konzipiert**, nur nicht als Audio-Feature.

### XVI.6 Ur-Systeme als eigenständige KG-Systeme ✅

**Fundstelle:** Chat 9 (01mar_chat9_chunk3), Entscheidung A-WL9-19:

| System | system_id | Knoten |
|---|---|---|
| **I Ching** | `iching` | 64 Hexagramme + 8 Trigramme + 6 Linien |
| **Kabbala** | `kabbalah` | 10 Sephiroth + 22 Pfade + 4 Welten + 3 Säulen |
| **Chakra** | `chakra` | 7 Hauptchakren + 3 Nadis |

→ Diese sind als **eigenständige Systeme** im KG modelliert, nicht nur als HD-Quellen.

### XVI.7 Bilder wirken tiefer als Begriffe

**Fundstelle:** Ra Batch 17 (Session 76):
> "Ein Begriff erklärt. Ein Bild öffnet. Ihr könnt einen Begriff verstehen und unverändert bleiben. Aber ein Bild kann euch treffen — in einer Weise, die ihr nicht vorhergesehen habt."

→ Ra bestätigt: **Visuelle Elemente** (Symbole, Bilder, Karten) sind keine Dekoration, sondern sprechen den "Potentiator" (das Unterbewusste) an.

### XVI.8 Traumarbeit

**Fundstellen:**
- Ra concepts: "Unverarbeiteter Katalysator: Wo landet er? (Körper, Emotion, Traum)"
- Ra Batch 17: "Matrix-Potentiator-Struktur: Welche IC-Interventionen sprechen den Potentiator an (Imagination, Traumarbeit, Symbol)?"
- Ra Batch 16: "Exponierte Offenheit ohne Verankerung ist vulnerabel" (Sicherheitsregel für Tiefenarbeit)

→ Traumarbeit ist **konzeptionell angedacht**, aber nicht operationalisiert.

### XVI.9 Voice-first Agent

**Fundstelle:** reference/vision_and_story.md:
> "Drei Modi (langfristig): 1. Voice-first Agent — User spricht, Agent antwortet visuell + sprechend"

---

## XVII. Neue Feature-Ideen (Erweitertes Inventar)

### XVII.1 Praxis-Empfehlungs-Engine

IC empfiehlt nicht nur "Das ist dein Muster", sondern "In deiner Phase wäre XY hilfreich":

| Leiter-Stufe | IC-internes Werkzeug | Externe Empfehlung |
|---|---|---|
| 1 SEHEN | System-Erzählung + Resonanz-Check | Gene Keys Contemplation |
| 2 FÜHLEN | Anker (Energiezentren-Scan, Sitting With) | Breathwork, Somatic Experiencing, Focusing |
| 3 VERSTEHEN | Balancing + IFS-Prinzip ("Welcher Teil?") | Aufstellungsarbeit, Voice Dialogue, Journaling |
| 4 HANDELN | System-spezifische Praxis + Experiment | HD-Experiment, BaZi-Element-Balance, Jyotish Upayas |
| 5 ERNTEN | Reflexion + Bedürfnis-Check | Dankbarkeitspraxis, Narrativ-Reflexion |

**Somatic Experiencing** (kurz erklärt): Körperorientierte Traumatherapie (Peter Levine). Grundidee: Trauma sitzt im Nervensystem, nicht im Verstand. Durch langsames, kontrolliertes Spüren von Körperempfindungen wird eingefrorene Energie (Freeze-Response) schrittweise aufgelöst. Verwandt mit IC's Anker (Sitting With), aber therapeutisch tiefer.

### XVII.2 KI-generierte personalisierte Mantras / Sound

| Feature | Was | Input | Output |
|---|---|---|---|
| **Jyotish-Mantras** | Traditionelle Mantras basierend auf Dasha-Periode + schwachen Planeten | Chart + aktuelle Dasha | Audio (KI-generiert), Text, Anleitung |
| **Frequenz-Meditation** | Personalisierte Klang-Meditation basierend auf Gene Key Shadow→Gift | Aktuelles Gene Key × Phase | Audio (KI-generiert), 5–15 Min |
| **Tages-Mantra** | Kurzer Satz aus aktuellem Transit × persönlichem Chart | Jetzt-Moment-Daten | Text + optional Audio |
| **BaZi-Element-Sound** | Klanglandschaft für das fehlende/schwache Element | BaZi-Chart | Ambient Audio (Wasser, Feuer, Erde, Metall, Holz) |

→ Downloadbar, Spotify-kompatibel, oder in-App abspielbarer Player.

### XVII.3 KI-generierte visuelle Symbole / Krafttiere

| Feature | Was | Input | Output |
|---|---|---|---|
| **Persönliches IC-Glyph** | Einzigartiges visuelles Symbol aus Chart-Daten | HD-Typ + BaZi-Element + Maya-Kin + EG-Typ | KI-generiertes Bild (Mandala-artig) |
| **Krafttier / Archetyp** | Symbolische Figur basierend auf Inkarnationskreuz + Profil | HD-Chart | KI-generiertes Bild + Beschreibung |
| **Transit-Karte** | Visuelles "Tarot" für den aktuellen Moment | Jetzt-Uhrzeit × Transit × Chart | KI-generiertes Bild + Weisheitstext |
| **Domänen-Symbole** | 12 personalisierte Symbole für das Mandala | Chart-Daten × Domäne | KI-generiert, wiedererkennbar |
| **Leiter-Visualisierung** | Visueller Fortschritt der Transformation | Aktueller Brunnen-Stand × Leiter-Stufe | Animiertes Bild |

→ Ra bestätigt: Bilder sprechen den Potentiator (Unterbewusstes) an, wo Begriffe nur die Matrix (Bewusstes) erreichen.

### XVII.4 Weisheitskarten / Sprüche

| Feature | Was | Format |
|---|---|---|
| **Tägliche Weisheitskarte** | Personalisierter Spruch aus Transit × Chart × Phase | In-App-Karte, druckbar, teilbar |
| **7 Hermetische Karten** | Die 7 universalen Prinzipien als visuelle Karten | Set zum Durchblättern |
| **IC-Prinzipien-Deck** | 7 Thesen + 5 Prinzipien + 8 Fallen als Karten-Set | Physisch druckbar / in-App |
| **Gene Key Contemplation Cards** | Shadow→Gift→Siddhi pro aktivem Gate | Tages-/Wochen-Karten |
| **I-Ging-Tages-Hexagramm** | Aktuelles Hexagramm × persönlicher Kontext | Morgenritual-Karte |

### XVII.5 KI-gestützte Traumdeutung

| Feature | Was | Mechanik |
|---|---|---|
| **Traum-Journal** | User loggt Traum als Text (oder Sprache) | Freie Eingabe |
| **Symbol-Analyse** | KI extrahiert Symbole und mappt auf Chart-Daten | NLP → KG-Abgleich |
| **Transit-Kontext** | Welcher Transit war in der Nacht aktiv? | Automatisch berechnet |
| **Brunnen-Verbindung** | Traum-Themen × Brunnen-Schichten × offene Pattern Traps | KG-Cross-Reference |
| **Reflexions-Einladung** | "Dein Traum zeigt X. Dein Chart deutet auf Y. Was resoniert?" | Hypothesen-Sprache (P1) |

→ Ra sagt explizit: Unverarbeiteter Katalysator zeigt sich in Träumen. IC könnte das als Diagnose-Kanal nutzen.

### XVII.6 I-Ging als Navigationsstruktur

| Konzept | Was es bietet | IC-Integration |
|---|---|---|
| **64 Zustände + Übergänge** | Jedes Hexagramm beschreibt einen Zustand UND seinen natürlichen nächsten Schritt | Transit-View: "Du bist in Zustand X (Hexagramm Y). Der natürliche Übergang führt zu Z." |
| **Wandlungslinien** | Die sich ändernden Linien zeigen den aktiven Transformationspunkt | Könnte die Gabel-Mechanik verfeinern: WO genau im Hexagramm findet die Wandlung statt? |
| **HD-Tore als I-Ging-Tore** | 64 Tore = 64 Hexagramme (bereits im System) | Das I Ging liefert die WANDLUNGS-LOGIK, die HD nicht hat: welcher Zustand folgt natürlich? |

### XVII.7 Kabbala-Baum als alternative Karte

| Konzept | Was es bietet | IC-Integration |
|---|---|---|
| **10 Sephiroth ↔ 12 Domänen** | ~~Auffällige 1:1-Parallele~~ Seit 12 Domänen nicht mehr 1:1, bleibt als alternativer View denkbar | Kabbala-Kenner sehen ihre Sprache; 10 Sephiroth mappen auf Teilmenge |
| **22 Pfade ↔ Cross-System-Bridges** | Pfade verbinden Sephiroth wie Edges Nodes im KG | Flussdiagramm-View in Kabbala-Ästhetik |
| **Tiferet (Herz) als Zentrum** | Integrationspunkt aller anderen Sephiroth | Parallele zu P4 (Verbindung/Beziehung) als Scharnier-Perspektive |
| **Tikun (Seelen-Aufgabe)** | Aus Name + Datum ableitbar | Zusätzliche individuelle Dimension für Schritt 1 |

### XVII.8 Alltags-Experimente (Erweiterung Leiter Stufe 4)

| Feature | Was | Personalisierung |
|---|---|---|
| **HD-Strategie-Experiment** | "Diese Woche: Folge deiner Sakral-Reaktion bei X" | HD-Typ + aktuelle Domäne |
| **BaZi-Element-Ausgleich** | "Dein Chart fehlt Wasser. Diese Woche: abends 10 Min am Wasser sitzen" | BaZi-Chart × fehlendes Element |
| **EG-Gegenbewegung** | "Du kompensierst mit Helfen. Experiment: Einen Tag NICHT helfen, beobachten" | EG-Typ × Pattern Trap |
| **Breathwork-Einladung** | "Vor dem Schlafen: 4-7-8 Atemrhythmus (beruhigt dein aktiviertes Nervensystem)" | Nervensystem-Check-Ergebnis |
| **Mantra-Experiment** | "Diese Woche: Dein Jyotish-Mantra 108× morgens" | Jyotish Dasha + schwacher Planet |
| **Stille-Einladung** | "10 Min Stille. Keine Frage. Nur dasein." (→ Schwelle) | Phase-abhängig (erst ab Phase 4+) |

---

## XVIII. Gesamtbild: Signatur → Phase → Praxis → Rahmen (aktualisiert)

```
SCHICHT 1 — SIGNATUR (individuell, geburtsbasiert, automatisch)
    HD + BaZi + Jyotish + Westl. Astro + Maya + Numerologie
    + Gene Keys + Kabbala/Gematria + I Ging (als eigenständige Systeme im KG)
    → Input: Datum + Zeit + Ort + Name
    → IC-Schritte: 1–3

SCHICHT 2 — SIGNATUR × ZEIT (individuell-dynamisch, automatisch)
    Jyotish Dashas + BaZi Luck Pillars + HD Transite + Numerologie-Jahreswelle
    + I-Ging-Wandlungslogik + Jetzt-Moment (Uhrzeit × Transit × Chart)
    → IC-Schritte: 8 + JETZT-Space
    → NEU: Dynamische Texte (Overlay-Modus)

SCHICHT 3 — DIAGNOSE × TIEFE (individuell, Chart + Reflexion)
    EG-Brücke (HD→EG) + Pattern Traps + Brunnen (4 Schichten)
    + Wunde-Kette + Narrativ-Analyse (NLP aus User-Text)
    + Situativ-Fragen (EG-Verfeinerung, Nervensystem-Check)
    + Traumdeutung (KI-gestützt, optional)
    → IC-Schritte: 4–6

SCHICHT 4 — PRAXIS (Werkzeug universell, Inhalt individuell)
    IC-intern: Anker, Leiter (5 Stufen), Balancing, IFS-Prinzip
    IC-empfohlen: Breathwork, Somatic Experiencing, Aufstellung, Focusing
    IC-generiert: Mantras, Sound-Meditationen, Experimente, Weisheitskarten
    IC-visuell: Krafttier/Glyph, Transit-Karten, Domänen-Symbole
    → IC-Schritte: 4 + 7

SCHICHT 5 — RAHMEN (universell, gibt Richtung)
    7 Thesen + 5 Prinzipien + Ra-Integration (6 Beiträge)
    + Hermetik (als Weisheitskarten, nicht als System)
    + Die Schwelle + Die Wahl (Meta-Qualitäten)
    → IC-Schritte: 9 + durchdringend
```

---

## XIX. Abgleich: Voice Dialogue, Focusing, Prozessarbeit, Tesla 3-6-9

### XIX.1 Was in IC bereits existiert

| Externes Konzept | IC hat bereits | Wo |
|---|---|---|
| Voice Dialogue: "Welche Stimme spricht?" | IFS-Prinzip: "Welcher Teil schützt die Wunde?" | Z3 Leiter Stufe 3, Format B ("Der innere Dialog") |
| Voice Dialogue: HD → Teilpersönlichkeit | HD offene Zentren → Konditionierungsmuster | Pattern Traps (Schritt 5) |
| Focusing: "Wo spürst du das im Körper?" | Anker: Energiezentren-Scan (4 Zonen) | Z3 A4 (Schritt 4) |
| Focusing: Körper weiß mehr als Verstand | Prinzip 5: Körper hat Vorrang | Kern-Prinzip, durchdringend |
| Focusing: Innehalten/Verweilen | Anker: Sitting With | Z3 A4 |
| Prozessarbeit: Symptom = Botschaft | Brunnen: Verhalten (S1) → Muster (S2) → Überzeugung (S3) → Wunde (S4) | Z3 A7, Z1 Schritt 6 |
| Prozessarbeit: Primär/Sekundär | Prisma: Was sichtbar ist (P1-P3) vs. was darunter liegt (P5-P7) | Zwei-Richtungen-Prinzip |
| Numerologie: Lebenszahl, Zyklen | Quellsystem: Numerologie | Z3 III.1, Gezeiten |

### XIX.2 Was NEU ist und IC stärken kann

**A. Focusing: 6-Schritt-Prozess → Anker-Verfeinerung**

IC's Anker hat 3 Komponenten (Scan, Sitting With, Nervensystem-Check). Gendlins Focusing ist **strukturierter** — und die fehlenden Schritte könnten den Anker verbessern:

| Focusing-Schritt | IC-Entsprechung | Lücke? |
|---|---|---|
| 1. Raum schaffen | Nervensystem-Check (bin ich sicher?) | ✅ Vorhanden |
| 2. Thema wählen | User wählt Domäne/Pattern Trap | ✅ Vorhanden |
| 3. Felt Sense erspüren | Energiezentren-Scan ("Wo spürst du?") | ✅ Vorhanden |
| 4. **Handle finden** | — | 🔴 **FEHLT:** "Welches Wort oder Bild passt zu dem, was du spürst?" |
| 5. **Resonieren** | — | 🔴 **FEHLT:** "Stimmt das? Verändert sich etwas, wenn du das Wort sagst?" |
| 6. Empfangen | Sitting With ("Bleib dabei, was kommt?") | ✅ Teilweise |

→ **Empfehlung:** Anker von 3 auf 5 Komponenten erweitern:
1. Nervensystem-Check (Sicherheit)
2. Energiezentren-Scan (Wo?)
3. **Handle finden** (Welches Wort/Bild?)
4. **Resonanz-Check** (Stimmt das?)
5. Sitting With (Bleib dabei)

Das würde den Anker vom reinen "Spür-Werkzeug" zum vollständigen **Körper-Erkenntnis-Werkzeug** machen. HD-Sacral-Response und Emotional Wave funktionieren nach demselben Prinzip: der Körper "antwortet" — man muss nur lernen, die Antwort zu lesen.

**B. Voice Dialogue: "Welche Stimme schreibt gerade?" → KI-Feature**

Nicht als eigenständiges System, sondern als **NLP-Analyse-Layer** in der App:

| Was die KI erkennt | Wie | Was IC sagt |
|---|---|---|
| Kritische Selbstbeschreibung | Textanalyse: Tonfall, Wortwahl | "Du schreibst gerade sehr streng über dich. Kennst du diese Stimme?" |
| Leistungsdruck | Sprache des "Machers" | "Hier spricht der Teil, der immer fertig werden will. Was braucht er?" |
| Rückzug/Intellektualisierung | Analyse statt Fühlen | "Du beschreibst viel — aber wie fühlt es sich an?" (→ Focusing) |
| EG-typische Fixierung | EG-Typ × Sprachmuster | "Dein Typ-2-Muster zeigt sich gerade: Helfen statt Fühlen." |

→ Das verbindet Voice Dialogue + IFS + Narrativ-Analyse zu einem **einheitlichen KI-Feature**: Die App erkennt nicht nur WAS der User schreibt, sondern aus WELCHEM inneren Teil heraus.

**C. Prozessarbeit: "Was nervt dich?" → Projektions-Reflexionsfrage**

Zwei neue Reflexionsfragen für IC:

| Frage | Was sie öffnet | Wo in IC |
|---|---|---|
| "Was nervt dich gerade am meisten an einer anderen Person?" | Projektion → Sekundärer Prozess → eigener Schatten | WERKSTATT (Brunnen Schritt 6, Schicht 2–3) |
| "Welches Körpersymptom hast du gerade, das du normalerweise ignorierst?" | Randsignal → Körper-Speicher → Gabel-Material | WERKSTATT (Anker, Gabel-Punkt) |

Mindells Prinzip "Das Symptom will wahrgenommen werden, nicht bekämpft" **bestätigt** IC's Brunnen-Logik: Das Muster IST die Botschaft, nicht der Fehler.

**D. Tesla 3-6-9 → Numerologische Tiefe + Strukturprinzip**

| Aspekt | IC-Integration | Priorität |
|---|---|---|
| **Lebenszahl 3, 6, 9 als Sonder-Interpretation** | Numerologie-Content vertiefen: "Achsen-Qualitäten" mit besonderer Entwicklungslogik | 🟡 Mittel |
| **3er-6er-9er Rhythmus als Phasen-Struktur** | 3er: Anfang→Mitte→Ende (jede Phase). 6er: Polarität→Integration. 9er: Abschluss→Neustart. Passt zur 9-Schritte-Struktur (9 = Graduation/Neustart) | 🟡 Prüfen |
| **Vortex-Geometrie als Mandala-Visualisierung** | Die Rodin-Coil-Geometrie als ästhetisches Rahmenmodell für das Mandala (12 Domänen auf einem Torus?) | 🔵 Niedrig (spekulativ) |
| **3-6-9 × Numerologie-Jahreswelle** | Jahre 3, 6, 9 im persönlichen Zyklus als besondere Übergangspunkte | 🟡 Mittel |
| **3 Säulen (Kabbala) × 3-6-9** | 3 Säulen = Strenge (3), Milde (6), Mitte (9) — Strukturparallele zum Baum des Lebens | 🟡 Wenn Kabbala integriert wird |

**Ehrliche Einschätzung:** 3-6-9 ist faszinierend, konvergiert an vielen Stellen, aber IC sollte es als **numerologische Vertiefung** behandeln, nicht als eigenes Rahmenmodell. Die Konvergenz-These (T4) greift: das Muster ist real, die Interpretation muss hypothetisch bleiben.

### XIX.3 Aktualisiertes Inventar: Externe Methoden → IC-Mapping

| Externe Methode | IC-Integration | Typ |
|---|---|---|
| **IFS** | Leiter Stufe 3 ("Welcher Teil?") | ✅ Bereits integriert |
| **Focusing** | Anker-Erweiterung (Handle + Resonanz-Check) | 🟢 Aufnehmen → Anker v2 |
| **Voice Dialogue** | KI-Stimmen-Erkennung (NLP-Layer) | 🟢 Aufnehmen → Feature |
| **Prozessarbeit** | Projektions-Frage + Randsignal-Eingabe | 🟢 Aufnehmen → Reflexionsfragen |
| **Somatic Experiencing** | Empfehlung in Praxis-Engine (Leiter Stufe 2) | ⚡ Extern empfehlen |
| **Breathwork** | Empfehlung + ggf. einfache In-App-Anleitung | ⚡ Extern + einfache Anleitung |
| **Aufstellungsarbeit** | Empfehlung in Praxis-Engine (Leiter Stufe 3) | ⚡ Extern empfehlen |
| **GfK** | Empfehlung für Leiter Stufe 4 (Relational) | ⚡ Extern empfehlen |
| **Numerologie 3-6-9** | Content-Vertiefung für Lebenszahlen 3/6/9 | 🟡 Prüfen |
| **Kabbala Klipoth** | Schatten der Sephiroth als Content-Layer | 🟡 Wenn Kabbala integriert |

### XIX.4 Aktualisierter Anker (v2-Vorschlag)

| # | Komponente | Was | Dauer | Quelle |
|---|---|---|---|---|
| 1 | **Nervensystem-Check** | "Kampf/Flucht, Erstarren oder Sicherheit?" | 30 Sek | Polyvagal |
| 2 | **Energiezentren-Scan** | "Wo im Körper spürst du etwas?" (4 Zonen) | 1–2 Min | Ra + Chakra |
| 3 | **Handle finden** | "Welches Wort oder Bild passt zu dem, was du spürst?" | 1–2 Min | Focusing (Gendlin) |
| 4 | **Resonanz-Check** | "Sag das Wort leise. Stimmt es? Verändert sich etwas?" | 1 Min | Focusing |
| 5 | **Sitting With** | "Bleib dabei. Nicht ändern. Was kommt?" | 2–5 Min | Aaron + Buddhismus |

→ Vorher: 3 Komponenten (Diagnose-Tool).
→ Nachher: 5 Komponenten (Körper-Erkenntnis-Werkzeug). Der Anker wird zum **Micro-Focusing für die App**.

---

## XX. Scope-Cut: v1 / v2 / v3

### Grundprinzip

Alle 10 Systeme sind von Anfang an in der Architektur (Pipeline, KG, Engines existieren für alle).
Die Staffeln (HD zuerst → BaZi/Astro/Maya → Jyotish/Gene Keys → Rest) betreffen die **Content-Tiefe** — wann genug extrahierte Interpretationen pro System vorhanden sind.

v1/v2/v3 unterscheiden sich durch **UI-Features und Interaktionstiefe**, nicht durch Systeme.

### v1 — Vollständiger Bogen, wachsende Content-Tiefe

**Navigation:** 4 Spaces (Arbeitstitel: JETZT / KARTE / WERKSTATT / ZEIT)

| Feature | Was | Abhängig von |
|---|---|---|
| **Onboarding** | Geburtsdaten → Chart aller verfügbaren Systeme | Chart-Engine-Service |
| **JETZT** (Home) | Aktive Transite (Top 1–3), offene Arbeit, Phase-Fortschritt | Transit-Service (einfach) |
| **KARTE** (Erkunden) | Mandala (12 Domänen, 3 Ringe, Phase-Indikator) | user_charts + sys_kg_nodes |
| **KARTE: Handbuch** | Tiefe 1 (Spiegel) + Tiefe 2 (Muster) pro Domäne | KG Schicht B + D |
| **KARTE: System-Charts** | BodyGraph (HD), Geburtsrad (Astro), 4-Säulen (BaZi), Kin (Maya) | Chart-Renderer-Komponenten |
| **KARTE: Rohdaten** | Tabellarische Ansicht aller Chart-Elemente | user_charts |
| **KARTE: Lens-Switcher** | Synthese (Default) / Original-Modus (einzelnes System) | Frontend-Filter |
| **WERKSTATT** (Vertiefen) | Brunnen→Leiter Flow (vereinfacht), Pattern Traps | Flow-Engine (einfach) |
| **WERKSTATT: Anker v1** | 3 Komponenten (Nervensystem-Check, Scan, Sitting With) | Frontend-Komponenten |
| **ZEIT** (Timing) | Einfache Timeline (HD-Transite + Astro-Transite) | Transit-Service |
| **Content** | Wächst mit Staffel-Pipeline (HD zuerst, dann BaZi/Astro/Maya) | PDF-Pipeline + KG |

**Backend-Voraussetzungen v1:**
- User Data Model: user_charts, user_progress (Basis)
- Chart-Engine-Service (alle Engines parallel)
- Transit-Service (einfach, HD + Astro)
- KG Schichten A–D (D = Cross-System-Mappings, mindestens Starter-Set)
- Handbuch-Generator (Tiefe 1–2)

### v2 — Tiefe + Praxis + Dynamik + Beziehung

| Feature | Was | Neu gegenüber v1 |
|---|---|---|
| **Handbuch Tiefe 3–4** | Prozess + Experiment mit Nervensystem-Gates | Safety-Gating, KG Schicht C |
| **Anker v2** | 5 Komponenten (+ Handle finden, + Resonanz-Check) | Focusing-Erweiterung |
| **Praxis-Empfehlungs-Engine** | Phase × Signatur → externe Praxis-Empfehlung | Recommendation-Service |
| **Volle Konvergenz-Engine** | 3+ Systeme zeigen auf selbe Domäne → Highlight | Cross-System-Edge-Analyse |
| **State Detection** | Automatische Phase-Erkennung pro Domäne | State Machine |
| **Dynamische Texte** | Transit-Overlay (statisch × transit × KG = personalisiert) | Overlay-Service |
| **Narrativ-Frage** | Offene Frage im Onboarding → KI-Ableitung (EG, Phase, Emotion) | NLP-Service |
| **Weisheitskarten** | Tägliche personalisierte Karte (Transit × Chart × Phase) | Content-Generator |
| **Alltags-Experimente** | Personalisiert pro System und Phase | KG Schicht E |
| **Jyotish Dashas + BaZi Luck Pillars** | Langfrist-Zyklen im ZEIT-Space | PyJHora + alvamind |
| **Partner-/Familien-Charts** | WIR-Modus: Composite, Synastry, Beziehungs-Pattern-Traps | Multi-Person user_charts |
| **WIR-Umschalter** | In KARTE + WERKSTATT: ICH / WIR mit Personenauswahl | Frontend + Relationship-Charts |
| **Jyotish/Gene Keys Chart-Views** | Rasi, Navamsa, Hologenetic Profile | Weitere Chart-Renderer |

### v3+ — KI-Kreativität + Alternative Karten

| Feature | Was |
|---|---|
| **KI-generierte Mantras/Sound** | Jyotish-Mantras, Frequenz-Meditationen, BaZi-Element-Sound |
| **Krafttiere/Glyphen** | Persönliches IC-Glyph, Archetyp-Bild (KI-generiert) |
| **Traumdeutung** | Traum-Journal → Symbol-Analyse × Chart × Transite |
| **NLP-Layer** | Stimmen-Erkennung aus Text (Voice Dialogue), fortlaufende Narrativ-Analyse |
| **I-Ging als Navigation** | 64 Zustände + Wandlungslogik als alternativer Weg |
| **Kabbala-Baum als Karte** | 10 Sephiroth ↔ 12 Domänen als alternativer KARTE-View |
| **Voice-first Agent** | Gesprochener Begleiter mit RAG auf KG |
| **Astrokartographie** | Geografische Dimension aus Geburtsdaten |

### Was bewusst NICHT geplant ist

| Feature | Warum nicht |
|---|---|
| Wearable-Integration (HRV, Schlaf) | Zu hohe Abhängigkeit, zu wenig validiert |
| Voice-Analyse (Stimmfrequenz → Persönlichkeit) | User-Entscheidung: eher nicht |
| Aufstellungsarbeit in-App | Zu komplex für App-Automatisierung |
| Schamanismus-Features | IC verweist darauf, implementiert es nicht |
| Vortex-Geometrie als App-Visualisierung | Zu spekulativ |

### Pipeline-Abhängigkeiten

| Version | Pipeline-Phase | Was bereit sein muss |
|---|---|---|
| v1 | S5–S7 + P1 + P3 | HD E2E validiert, Staffel-1-PDFs verarbeitet, Chart-Engines integriert |
| v1 | P4 (Starter) | Mindestens 50 Cross-System-Mappings (approved) für Konvergenz-Erlebnis |
| v2 | P4 (voll) | Cross-System + Meta-Knoten, NLP-Pipeline, Relationship-Chart-Engine |
| v3 | Neue Pipeline | Content-Generation (Mantras, Sound, Bilder), Traum-NLP |

---

## XXI. Architecture-Delta: Was sich ändern muss

### Bestehende Architektur (Stand S4)

| Dokument | Was es abdeckt | Status |
|---|---|---|
| `cursor/architecture.md` | 5 Datenschichten, 10 sys_*-Tabellen, Tech Stack, Infra-Topologie | ✅ Aktuell |
| `cursor/pipeline.md` | PDF-Pipeline (extract → KG), Worker, Anna's Archive, LLM-Steuerung | ✅ Aktuell |
| `cursor/engines.md` | Chart-Engines (hdkit, alvamind, pyswisseph, etc.), Staffeln, Kit-Parsing | ✅ Aktuell |
| `cursor/contracts.md` | 15 Dimensionen, 12 Lebensbereiche, Payloads, Enums | ✅ Aktuell |
| `cursor/status.md` | S1–S4 erledigt, S5 nächster Schritt | ✅ Aktuell |

### 8 Lücken (was FEHLT)

**L1 — User Data Model (komplett fehlend)**

Aktuelle Architektur kennt nur sys_* (KG-Wissen). Kein Schema für User-Daten:

| Tabelle | Was | Wann nötig |
|---|---|---|
| `user_profiles` | Geburtsdaten, Name, Onboarding-Status | v1 |
| `user_charts` | Berechnete Chart-Daten pro Person pro System (JSONB) | v1 |
| `user_persons` | Mehrere Personen pro Account (ICH + Partner + Familie) | v1 (Schema), v2 (WIR-Modus) |
| `user_relationships` | Beziehung zwischen Personen (Partner, Kind, Elternteil, Freund) | v2 |
| `user_relationship_charts` | Composite/Synastry als abgeleitete Charts | v2 |
| `user_progress` | Phase pro Domäne (1–7), Brunnen/Leiter-Stand pro Thema | v1 |
| `user_sessions` | Anker-Sessions, Brunnen→Leiter-Flows (Zustand, Fortschritt) | v1 |
| `user_reflections` | Text-Input für NLP-Analyse (Narrativ-Frage, Reflexionen) | v2 |
| `user_dreams` | Traum-Journal-Einträge | v3 |

**L2 — Jetzt-Moment / Transit-Engine (nicht designed)**

Engines.md beschreibt Chart-Berechnung (einmalig, Onboarding). Aber: Transit-Overlay (Echtzeit) fehlt:

| Aspekt | Was | Wie |
|---|---|---|
| Transit-Berechnung | Aktuelle Planetenpositionen → aktive Tore/Aspekte | pyswisseph Echtzeit oder 15-Min-Cache |
| Overlay-Logik | Statischer Chart × aktueller Transit × KG-Interpretation | Overlay-Service |
| Konvergenz-Detection | 3+ Systeme zeigen auf selbe Domäne → Highlight | Cross-System-Edge-Analyse |
| Jetzt-Moment | Uhrzeit × Transit × Chart = situativer Snapshot | Jedes App-Öffnen |

**L3 — Derived Data Layer (neues Konzept)**

Nicht im KG, nicht in der Pipeline — BERECHNET aus User-Chart + KG zur Laufzeit:

| Ableitung | Input | Output | Wann |
|---|---|---|---|
| EG-Bridge | HD offene Zentren | EG-Triade → EG-Typ-Hypothese | v1 |
| Pattern Trap Detection | HD × EG × BaZi × Domäne | Spezifische Falle + Beschreibung | v1 |
| Wunde-Kette | EG-Typ × Brunnen-Schicht × Max-Neef | Kernverletzung → blockiertes Bedürfnis → Kompensation | v1 |
| Beziehungs-Traps | Chart A × Chart B × KG | Verstärkungs-/Clash-Dynamiken | v2 |

**L4 — Content Delivery / Handbuch-Generator (nur Stichworte in P5)**

Wie wird aus KG-Daten personalisierter Handbuch-Text?

| Aspekt | Was fehlt |
|---|---|
| 7D-Adressierung | Schritt × Domäne × Tiefe × Perspektive × Frage × Register × Zeit |
| 3 Text-Modi | Statisch / Transit / Overlay (→ XVI.1 bereits konzipiert) |
| Progressive Disclosure | Tiefe 1→4 mit Nervensystem-Check als Gate vor Tiefe 3+ |
| Mikro-Erzählung | 5-Schritt-Prinzip: BENENNEN → ÜBERSETZEN → VERORTEN → REFLEXION → EINLADUNG |
| Personalisierung | User-Chart-Elemente → KG-Lookup → Wording-Style → fertiger Text |

**L5 — State Machine / Flow Engine (nicht in Architektur)**

| Element | Was | Komplexität |
|---|---|---|
| 7 Phasen × 12 Domänen | Pro User, pro Domäne eigenständig (nicht-linear) | Mittel |
| Brunnen→Leiter Flow | Multi-Step, unterbrechbar, mit Anker als Sub-Flow | Hoch |
| Anker v1/v2 | 3 bzw. 5 Schritte, eingebettet in WERKSTATT | Niedrig |
| Nervensystem-Check als Gate | Bedingung vor Tiefe 3+, Ergebnis beeinflusst Flow | Niedrig |
| Phase-Erkennung | Automatisch aus User-Verhalten + Reflexionen (v2) | Hoch |

**L6 — AI/NLP Layer (nicht in Architektur)**

| Feature | Wann | Wie |
|---|---|---|
| Narrativ-Analyse | v2 | User-Text → EG-Cluster, Phase, Emotion (LLM-basiert) |
| Stimmen-Erkennung | v3 | Text-Analyse → "Welcher innere Teil schreibt gerade?" |
| Praxis-Empfehlung | v2 | Phase × Signatur × Leiter-Stufe → externe Praxis |
| Traumdeutung | v3 | Traum-Text → Symbole → Chart × Transite × KG |
| Content-Generation | v3 | KI-generierte Mantras, Sound, Bilder |

**L7 — Chart-Visualisierungen (komplett fehlend)**

Engines berechnen, KG interpretiert — aber KEIN Frontend-Konzept für traditionelle Chart-Ansichten:

| Chart | Komplexität | Open-Source-Optionen | Version |
|---|---|---|---|
| **HD BodyGraph** | Hoch (SVG: 9 Center, 36 Channels, 64 Gates, definiert/offen) | hdkit Sample-App, bodygraph-chart (npm) | v1 |
| **Astro Geburtsrad** | Hoch (SVG: Planeten, Häuser, Aspekte, Zeichen) | astrochart.js, Kerykeion (Python→SVG) | v1 |
| **BaZi 4-Säulen** | Niedrig (Tabelle: Stems, Branches, Hidden Stems, Ten Gods) | Kein spezielles Paket nötig | v1 |
| **Maya Kin/Wavespell** | Niedrig (Tabelle/Karte: Seal, Ton, Wavespell) | Kein spezielles Paket nötig | v1 |
| **Jyotish Rasi/Navamsa** | Mittel (Quadrat-Chart mit Planeten, Häusern) | PyJHora hat Chart-Rendering | v2 |
| **Gene Keys Hologenetic** | Mittel (Sphären-Diagramm) | Kein Open Source bekannt | v2 |
| **IC Mandala** | Hoch (Eigenes Design: 12 Segmente, 3 Ringe, Farben, Animationen) | Eigenentwicklung | v1 |

**L8 — Multi-Person / Relationship Charts (nicht im Datenmodell)**

| Aspekt | Was nötig ist | Wann |
|---|---|---|
| Personen-Management | User kann Partner/Kind/Elternteil/Freund hinzufügen (eigene Geburtsdaten) | v1 (Schema), v2 (UI) |
| Relationship-Engine | 2 Einzel-Charts → Composite (HD), Synastry (Astro), Day-Branch-Vergleich (BaZi) | v2 |
| Beziehungs-Pattern-Traps | Verstärkungs-/Clash-Dynamiken zwischen zwei Charts | v2 |
| WIR-Modus | Umschalter in KARTE + WERKSTATT: ICH / WIR mit Personenauswahl | v2 |

### 3 Updates (was sich ÄNDERT)

**U1 — contracts.md erweitern**

Neue Tags im Interpretations-Payload:

| Tag | Werte | Wozu |
|---|---|---|
| `ic_step` | 1–9 | Zuordnung zum 9-Schritte-Prozess |
| `ic_depth` | 1–4 (Spiegel/Muster/Prozess/Experiment) | Handbuch-Tiefe |
| `ic_brunnen_layer` | 1–4 (Verhalten/Muster/Überzeugung/Kernverletzung) | Brunnen-Schicht |
| `ic_leiter_stufe` | 1–5 (Sehen/Fühlen/Verstehen/Handeln/Ernten) | Leiter-Stufe |
| `ic_grammatik` | BEING / HAVING / DOING / INTERACTING | Grammatik-Frage |
| `ic_register` | mechanik / transformation / praxis | Stimme-Register |
| `ic_safety_gate` | boolean + min_depth | Progressive Disclosure |
| `ic_reflexion_frage` | string | Reflexionsfrage für dieses Element |
| `ic_experiment_seed` | string | Experiment-Ansatz (bereits in process.experiment_seed, erweitern) |

**U2 — pipeline.md erweitern**

Neue Pipeline-Jobs (Batch):

| Job | Input | Output | Prio |
|---|---|---|---|
| `extract_pattern_traps` | Interpretationen aus 2+ Systemen × Domäne | sys_dynamics (trap-Typ, kombinatorisch) | Hoch |
| `extract_reflexion_questions` | sys_interpretations | KG Schicht E: Reflexionsfragen pro Element | Hoch |
| `extract_experiments` | sys_interpretations × process-Feld | KG Schicht E: Experiment-Seeds | Mittel |
| `tag_ic_metadata` | sys_interpretations | ic_step, ic_depth, ic_brunnen_layer, etc. | Hoch |

Neuer Pipeline-Typ (Echtzeit, nicht Batch):

| Service | Was | Cache |
|---|---|---|
| Transit-Berechnung | pyswisseph → aktuelle Positionen → aktive Tore/Aspekte | 15 Min |
| Overlay-Text | Statisch × Transit × KG → personalisierter Satz | On-demand, LLM-basiert |
| Konvergenz-Check | Cross-System-Edges + aktive Transite → Highlights | 15 Min |

**U3 — architecture.md erweitern**

| Erweiterung | Was | Wo |
|---|---|---|
| User-Schema | user_* Tabellen neben sys_* | Neuer Abschnitt "User Data Model" |
| Echtzeit-Layer | Transit-Service, Overlay-Service | Neuer Abschnitt "Real-time Services" |
| Frontend-Architektur | 4 Spaces, Datenfluss, Komponenten | Neuer Abschnitt "App Architecture" |
| Chart-Visualisierungen | Pro System: Renderer, Datenformat, Open-Source-Optionen | Neuer Abschnitt "Chart Views" |
| Multi-Person | Personen-Management, Relationship-Charts | Im User Data Model |

---

<!-- Footer
ic_gesamtinventur.md v0.5 | 2026-03-31
-->
