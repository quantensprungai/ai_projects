# Inner Compass — Product Requirements Document v3

> Stand: 2026-02-16 | Vollständiges PRD. Für Cursor: lies cursor/contracts.md statt dieses Dokument.

## 1. Was ist Inner Compass?

Ein personalisiertes, geburtsbasiertes Lebenshandbuch, das kulturell diverse Wissenssysteme über einen gemeinsamen Knowledge Graph verbindet. Der User gibt Geburtsdaten ein und erhält — statt einzelner Charts — eine einheitliche, interaktive Landkarte seines Designs, organisiert entlang der Lebensbereiche, die ihn tatsächlich beschäftigen.

**Was es NICHT ist:** Kein Chart-Rechner (davon gibt es genug), kein reiner Chatbot, kein esoterisches Unterhaltungsprodukt.

**Was es IST:** Ein Lebenshandbuch auf drei Säulen: Spiegel (geburtsbasierte Berechnung über mehrere Systeme), Prozess (Fallen erkennen, Geschenke aktivieren, Experimente durchführen), Zeitlinie (dynamische Aktualisierung basierend auf aktuellen Zyklen).

## 2. Zielgruppe

Millennial/Gen-Z, spiritual-curious, bereits mit mindestens einem System in Berührung (typischerweise Astrologie oder HD über Social Media). Sucht Tiefe jenseits von Horoskop-Apps, ist offen für kulturelle Breite, will nicht nur lesen sondern arbeiten.

## 3. Alleinstellungsmerkmale

- **Cross-System-Verbindung:** Wenn drei verschiedene Traditionen dasselbe Muster sehen, ist das ein anderer Moment als wenn ein System etwas behauptet.
- **Lebensbereich-Navigation:** User fragt nicht "Was sagt mein HD?" sondern "Warum klappt es in meiner Beziehung nicht?" und bekommt Antworten aus allen Systemen.
- **Vom Profil zum Prozess:** Nicht nur zeigen wer du bist, sondern wo du stehst und was du als Nächstes tun kannst.
- **Eigenes Wording:** Drei Sprachebenen machen Weisheit alter Traditionen zugänglich ohne zu verflachen.
- **Mandala als Signatur:** Visuell einzigartiger Fingerabdruck, sofort teilbar auf Social Media.

## 4. Die 12 Lebensbereiche

> Revidiert 2026-03-31: Von 10→12 erweitert (siehe ergebnis_modelle.md §20d-rev).

| # | Bereich | Kernfrage | Systemquellen |
|---|---------|-----------|---------------|
| 1 | Selbst & Identität | Wer bin ich im Kern? | HD: Typ+Autorität, BaZi: Day Stem, Astro: Sonne+ASC |
| 2 | Liebe & Partnerschaft | Wie liebe ich? | HD: Composite, BaZi: Spouse Palace, Astro: Venus+7.Haus |
| 3 | Sexualität & Intimität | Wie verbinde ich mich körperlich? | HD: Sakral+Intimität, BaZi: Peach Blossom, Astro: 8.Haus (Intimität) |
| 4 | Beziehungen & Community | Wie gestalte ich Zugehörigkeit? | HD: Profil+soziale Kanäle, BaZi: Friends, Astro: 11.Haus |
| 5 | Beruf & Berufung | Was ist meine Arbeit? | HD: Profil+Kreuz, BaZi: Month Pillar, Astro: MC+10.Haus |
| 6 | Familie & Zuhause | Wie gestalte ich Heimat? | HD: Environment, BaZi: Year Pillar, Astro: Mond+4.Haus |
| 7 | Gesundheit & Körper | Was braucht mein Körper? | HD: PHS+Zentren, BaZi: Element-Balance, Astro: 6.Haus |
| 8 | Geld & Ressourcen | Wie verdiene ich? | HD: Manifestation, BaZi: Wealth Element, Astro: 2.Haus |
| 9 | Kreativität & Ausdruck | Was will durch mich? | HD: Kehlzentrum, BaZi: Output, Astro: 5.Haus |
| 10 | Sinn & Spiritualität | Was ist das größere Bild? | HD: Kreuz, BaZi: Noblemen, Astro: 9.Haus, Maya: Kin |
| 11 | Austausch & Lernen 🆕 | Wie teile und verstehe ich? | Astro: 3.Haus, Jyotish: 3. Bhava, Ziwei: 兄弟宫 |
| 12 | Wandlung & Erneuerung 🆕 | Was muss loslassen, damit Neues kommt? | Astro: 8.+12.Haus, Jyotish: 8.+12. Bhava |

## 5. Die fünf Datenschichten

- **A: Rohmechanik** — Bauteile jedes Systems (Gates, Stems, Planets, Kin)
- **B: Bedeutungen** — Was bedeutet jedes Element? (LLM-extrahiert aus Fachbüchern)
- **C: Dynamiken** — Zeitliche Zyklen UND inhaltliche Prozesse (Fallen, Auswege, Experimente)
- **D: Cross-System-Mappings** — Verbindungen zwischen Systemen (HD Gate 34 ↔ BaZi Yang Fire)
- **E: Meta-Knoten** — Systemübergreifende Archetypen + eigenes Wording

Ohne D+E = Multi-App. Mit D+E = Meta-System.

## 6. Visualisierung: Zwei Modi

### Mandala/Kompass (Hauptscreen)
10 Segmente (Lebensbereiche) × konzentrische Ringe (Dimensionen). Äußere Form = Signatur. Farbgebung = Systemübereinstimmung. Leuchtende Akzente = zeitlich aktiv. Jeder Kompass ist einzigartig — wie ein Fingerabdruck.

### Fluss-Diagramm (Phase 2-3)
Zeigt WIE Elemente zusammenhängen (prozesshaft, dynamisch). Inspiriert vom Gene Keys Hologenetic Profile. Braucht Schicht D für Cross-System-Flüsse.

## 7. Handbuch: 4 Tiefenschichten

Pro Lebensbereich, progressiv:
1. **Spiegel:** Was sagen die Systeme? (Schicht A+B+D)
2. **Muster:** Wo ist Falle, wo Geschenk? (Schicht B shadow/gift + D+E)
3. **Prozess:** Erkennen → In Beziehung treten → Verstehen → Integrieren (Schicht C + LLM)
4. **Experimente:** Was kann ich diese Woche tun? (Quellen + LLM + Community)

## 8. System-Filter (Linsen)

User kann zwischen Linsen umschalten: Alle Systeme (Standard), Nur HD, Nur BaZi, Nur Astro, Nur Maya. Bedient drei Zielgruppen: System-Kenner, kulturspezifische Nutzer, Einsteiger.

## 9. Wording-Strategie: Drei Ebenen

- **System-Ebene:** Original-Terminologie ("Offenes Emotionalzentrum")
- **Meta-Ebene (Schicht E):** Eigene Begriffe für übergreifende Konzepte ("Blindspot" statt Not-Self)
- **Handbuch-Ebene:** Alltagsnahe Sprache ("Wenn du in Stress gerätst...")

Zwischen Ebenen immer transparente Verbindung. Wording entsteht als Nebenprodukt der Cross-System-Arbeit.

## 10. User Journey: 5 Ebenen

1. **Spiegel (Profil):** Geburtsdaten → Charts → Landkarte. Viraler Hook.
2. **Handbuch (Vertiefung):** 4 Tiefenschichten. KI-Chat kontextualisiert.
3. **Zeitlinie (Wo bin ich gerade):** Zyklen, Transite. Wiederkehrende Nutzung.
4. **Prozess (Was kann ich tun):** Wochen-Experimente, Formulierungshilfen.
5. **Verbindung (Cross-System):** "Drei Traditionen sehen dasselbe." Emotionales ASP.

## 11. Staffel-Planung

- **Staffel 1 "Die Vier Spiegel" (Launch):** HD, BaZi, Westl. Astrologie, Maya Tzolkin
- **Staffel 2 "Die Tiefe" (3-6 Mo.):** Jyotish, Gene Keys, Numerologie
- **Staffel 3 "Die Wurzeln" (6-12 Mo.):** Nine Star Ki, Akan Day Name, Community

## 12. AQAL-Abgrenzung

Von Wilbers 5 AQAL-Elementen: Types ✅ (weit über AQAL hinaus), Lines ✅ (als Dimensionen), Quadrants ✅ (als interner Qualitätscheck), Levels ⚠️ (bewusst anders: Zeitlinie statt Stufen), States ❌ (nicht relevant für geburtsbasiertes System). Keine Entwicklungshierarchie — Inner Compass bewertet nicht, es spiegelt.

## 13. Monetarisierung

Freemium: Basis-Profil (Landkarte + Spiegel) kostenlos. Premium: Handbuch-Tiefe, Zeitlinie, Cross-System, Filter, Fluss-Diagramm. Staffel-Releases als Retention.

## 14. Fahrplan

- Phase 0 (Wo.1-2): Schema-Migration + Strukturbäume + Contract-Erweiterungen
- Phase 1 (Wo.3-6): 4 Systeme parallel durch Pipeline
- Phase 2 (Wo.5-8): Engines + Landkarte + Filter + Handbuch-Generator
- Phase 3 (Wo.7-14): Cross-System-Infra (50 Mappings + Jobs + Meta-Knoten)
- Phase 4 (Wo.12-16): Launch "Die Vier Spiegel"
- Phase 5 (ab Mo.4): Fluss-Diagramm + Staffel 2
