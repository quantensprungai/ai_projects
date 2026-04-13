# IC Konsolidierung — Status & Abhängigkeiten

<!-- Reality Block
last_update: 2026-04-01
status: Phase 3 abgeschlossen, Übergang zu technischer Phase
scope: Cockpit für den gesamten Konsolidierungsprozess (Phase 2+)
purpose: Trackt Entscheidungen, Abhängigkeiten, offene Punkte über alle Themen
depends_on: 00_thematisches_register.md (Index der Fundstellen)
major_shift: 2026-03-29 — Ordnungsprinzip gewechselt von Modell-Taxonomie (WAS/WIE/WOMIT)
  zu Prozess-Architektur (9 Schritte des menschlichen Erkenntnisprozesses).
major_update: 2026-03-30 — 9-Schritte gegen alle consolidation/-Dateien validiert.
major_update: 2026-03-31 — Phase 3 substanziell: Z1 v0.5, Z3 v0.4, Glossar v1.2.
  Neue Konzepte: Lernmoment, Gabel, P1-Sonderrolle, Schwelle, Wahl.
  Ra-Integration: 6 Beiträge, Ra-7-vs-IC-9-Mapping, 3-vs-4-Erkenntniswege geklärt.
  Ra/Aaron-Abgleich + Wording-Audit abgeschlossen. Begriffs-Fixes eingearbeitet.
  3 rote Lücken operationalisiert (Anker, Diagnose-Erweiterung, Leiter-Methodik).
major_update: 2026-04-01 — Phase 3 als abgeschlossen markiert. Z4 = cursor/ Dateien (kein eigenes Dok).
  ic_gesamtinventur.md v0.5 als Brücke Philosophie→Technik anerkannt.
  Weiterarbeit geht in Engine Evaluation Sprint (cursor/status.md Phase 1).
  Z2 + Z3 A4 mit Update-Vermerken versehen.
-->

> Dieses Dokument ist das Cockpit. Es zeigt: was entschieden ist, was offen, was wovon abhängt.
> Ergebnis-Dokumente pro Thema liegen als eigene Dateien in `consolidation/ergebnis_*.md`.

---

## 1. Gesamtstand

| Phase | Was | Status |
|---|---|---|
| Phase 1 | Extraktion + Thematisches Register | ✅ Abgeschlossen (00_thematisches_register.md) |
| Phase 2 | Best-of-Sichtung pro Thema | ✅ Abgeschlossen (30. März 2026) |
| Phase 3 | Enddokumente füllen (Z1–Z6) | ✅ **Abgeschlossen** (1. April). Z1 v0.5 + Z2 v0.1 + Z3 v0.4 + Glossar v1.2. ic_gesamtinventur.md v0.5 als Inventur+Scope-Brücke. |
| Phase 4 | Prozess-Werkzeuge + Ra-informierte Ergänzungen | 🟡 Teilweise erledigt (Anker v1 operationalisiert, Diagnose-Erweiterung, Leiter-Methodik). Rest = in Z3 dokumentiert, Umsetzung in App-Phase. |

### Wichtige Entscheidungen (1. April 2026)

1. **Z4 (Architecture) = cursor/ Dateien.** Kein separates Z4-Enddokument. Die technische Dokumentation lebt in `cursor/{architecture, pipeline, contracts, engines, status}.md`. Begründung: Vermeidet Duplizierung; cursor/-Dateien sind direkt actionable; handover.md ist der Einstiegspunkt.

2. **ic_gesamtinventur.md ist Referenz-Dokument**, keine lebende Planungsdatei. §I–XIX = Inventar (stabil). §XX–XXI (Scope-Cut, Architecture-Delta) = Brücke, die ihren Job getan hat — Input für cursor/-Updates geliefert.

3. **Weiterarbeit geht in cursor/status.md** (Engine Evaluation Sprint = Phase 1). Die Konsolidierung philosophischer Inhalte ist abgeschlossen.

---

## 2. Themen-Status (Phase 2)

### Kern-Erkenntnis: Prozess statt Taxonomie (29. März 2026, validiert 30. März)

~~Die Modelle sind die größte Baustelle.~~ → **Korrektur:** Das Ordnungsprinzip war das Problem, nicht die Modelle. 

Bisherige Versuche (6 Modelle flach → 3-Schichten WAS/WIE/WOMIT) sortierten nach der *logischen Natur* der Bausteine. Das erzeugte unscharfe Grenzen und ein Henne-Ei-Problem.

**Neues Ordnungsprinzip:** Der menschliche Erkenntnisprozess in **9 Schritten** (Eintritt → Wiedererkennung → Verortung → Verkörperung → Diagnose → Vertiefung → Transformation → Zeitkontext → Graduation). Validiert durch Cross-Framework-Vergleich (Ra, Aaron, Jung, IFS, Buddhismus) UND gegen alle 54 consolidation/-Dateien (30. März).

**Zwei Perspektiven (explizit getrennt):**
- **Extern (User-Journey):** Die 9 Schritte, die ein Mensch durchlebt
- **Intern (IC-System):** Die Werkzeuge, die IC braucht um für jeden Schritt den richtigen Inhalt zu erzeugen

Vollständige Dokumentation: `ergebnis_modelle.md` (v0.4)

### Themen-Übersicht

| # | Thema (Register-Ref) | Status | Ergebnis-Dok | Blockiert durch |
|---|---|---|---|---|
| **A1** | Thesen + Prinzipien + Spannungsfelder | 🟢 Final | `ergebnis_thesen_prinzipien.md` (v1.0) | — |
| **B** | **Modelle & Architektur** | 🟢 Validiert + dokumentiert | `ergebnis_modelle.md` (v0.9) + `z3_modell_referenz.md` (v0.4) | — |
| B-alt | ~~3-Schichten / WAS-WIE-WOMIT~~ | ~~Superseded~~ | — | — |
| B-neu | 9-Schritte-Prozess (Ordnungsprinzip) | 🟢 Validiert (30.03) | `ergebnis_modelle.md` §9 | — |
| B-detail | Einzelne Modelle (Mandala, Prisma, etc.) | 🟢 Dokumentiert + 3 Lücken operationalisiert | `z3_modell_referenz.md` A1–A11, B1–B4 | — |
| B-meta | Meta-Strukturen + neue Konzepte | 🟢 Dokumentiert (31.03) | `z3_modell_referenz.md` C1–C8 (Lernmoment, Gabel, Schwelle, Wahl, Ra-Mapping) | — |
| **A2** | Ethik (AL, Jesus, Kein Guru) | ⬜ Noch nicht begonnen | — | A1 |
| **A3** | Zeitgeist-Fallen | 🟡 In z3 B4 dokumentiert, eigenes Dok. offen | `z3_modell_referenz.md` B4 | A1, B |
| **A4** | Hypothesen-Sprache / Evidenzklassen | 🟡 In z1 §5.1 + z3 Template, eigenes Dok. offen | — | — |
| **C** | KG-Architektur & Pipeline | 🟢 **In cursor/ dokumentiert** | `cursor/{architecture,pipeline,contracts}.md` = Z4 | — |
| **D** | Quellenstrategie | 🟡 Teilweise (Anna's Archive Toolkit, pipeline.md §8) | `cursor/pipeline.md` | C |
| **E** | App / Produkt / Story | 🟡 **Scope+Architektur definiert** | `ic_gesamtinventur.md` §XX–XXI + `cursor/architecture.md` §12–14 | B, C |
| **F** | Ra/Q'uo/Aaron Integration | 🟢 Großteils erledigt (31.03) | z1 §5.6 + z3 C6–C8 + Glossar Ra-Sektion | — |
| **G** | **Gesamtinventur** (NEU, 31.03) | 🟢 v0.5 fertig | `ic_gesamtinventur.md` (Inventar §I–XIX + Scope §XX + Delta §XXI) | B, C, E |

---

## 3. Abhängigkeitsgraph

```
     ┌───────────────────────────────────────┐
     │  B: 9-SCHRITTE-PROZESS (Validiert)    │
     │  ✅ 3 Lücken operationalisiert        │
     │  ✅ Z1 v0.5 + Z3 v0.4 + Glossar v1.2 │
     └────────────────┬──────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
  ┌──────────┐  ┌──────────┐  ┌──────────┐
  │ A1:Thesen│  │ C: KG    │  │ E: App/  │
  │ ✅ Final │  │ &Pipeline│  │ Produkt  │
  └────┬─────┘  └────┬─────┘  └──────────┘
       │             │
       ▼             ▼
  ┌──────────┐ ┌──────────┐
  │ A2:Ethik │ │ D:Quellen│
  │ A3:Fallen│ └──────────┘
  │ ⬜ offen │
  └──────────┘

  F: Ra-Integration = ✅ großteils erledigt (Z1 §5.6 + Z3 C6–C8 + Glossar)
  Z5 (Ra/Aaron-Brücke): Eigenes Dok. evtl. nicht mehr nötig — Inhalt in Z1+Z3 verteilt
  → NÄCHSTER SCHRITT: Z2 (User-Journey)
```

### Erledigte Schritte

1. ~~**Gegencheck:** 8-Schritte-Modell gegen altes Material~~ → ✅ (29. März)
2. ~~**Zieldokumente definieren**~~ → ✅ (29. März, siehe §6)
3. ~~**9-Schritte gegen consolidation/ validieren**~~ → ✅ (30. März)
4. ~~**Einzelmodelle + Querschnittswerkzeuge klären**~~ → ✅ (30. März)
5. ~~**Prisma-Entscheidung**~~ → ✅ 7 Perspektiven (30. März)
6. ~~**3 Lücken füllen**~~ → ✅ Operationalisiert: Anker, Diagnose-Erweiterung, Leiter-Methodik (31. März)
7. ~~**Tiefe-Dimension formalisieren**~~ → ✅ z3 C3 (31. März)
8. ~~**Thesen+Prinzipien finalisieren**~~ → ✅ ergebnis_thesen_prinzipien.md v1.0
9. ~~**Z1 + Z3 erstellen**~~ → ✅ Z1 v0.5 + Z3 v0.4 (31. März)
10. ~~**Ra/Aaron-Abgleich + Wording-Audit**~~ → ✅ Begriffs-Fixes, 6 Ra-Beiträge, Mapping, Schwelle/Wahl (31. März)
11. ~~**Kanonisches Glossar**~~ → ✅ glossar.md v1.2 (31. März)

### Nächste Schritte

1. ~~**Z2 (User-Journey) erstellen**~~ → ✅ z2_user_journey.md v0.1 (31. März)
2. ~~**Z4 (Architecture)**~~ → ✅ **Entscheidung: cursor/ = Z4** (1. April). Kein eigenes Dok.
3. ~~**Z5 überprüfen**~~ → ✅ **Kein eigenes Dok. nötig.** Verteilt in Z1+Z3+Glossar. (1. April)
4. **Alte Chats extrahieren** — Pre-IC-Chats per Extraktions-Prompt sichern.
5. **A2 (Ethik)** — Eigenes Enddokument oder in Z1 Teil 5 integrieren?
6. **Z6 (Story & Serie)** — True Core Story, Botschafter, Staffel-Logik.
7. **Z2 aktualisieren** — App-Spaces (JETZT/KARTE/WERKSTATT/ZEIT), Anker v2. **Erst nach Engine-Phase** (cursor/status.md Phase 1), wenn technische Realität klar ist.

### Übergang zur technischen Phase

Die philosophische Konsolidierung (Phase 1–3) ist **abgeschlossen**. Die Weiterarbeit am IC-Projekt findet jetzt in `cursor/status.md` statt (Engine Evaluation Sprint = Phase 1). Diese consolidation/-Dateien werden nur noch aktualisiert, wenn sich an den philosophischen Grundlagen etwas ändert.

---

## 4. Methodik (aktualisiert 29. März 2026)

### Bisheriger Ansatz (superseded)

B1 (Architektur-Klassen prüfen) → B2 (Einzelmodelle) → B3 (Ra/Aaron-Overlay).
Problem: Die Architektur-Klassen (WAS/WIE/WOMIT) erwiesen sich als falsches Ordnungsprinzip.

### Aktueller Ansatz: Prozess-basiert

Statt Bausteine nach ihrer Natur zu sortieren, werden sie nach dem **Moment im menschlichen Erkenntnisprozess** zugeordnet, den sie bedienen. Dieser 9-Schritte-Prozess wurde durch Cross-Framework-Vergleich (Ra, Aaron, Jung, IFS, Buddhismus) validiert und am 30. März gegen alle consolidation/-Dateien gegengeprüft.

**Vollständige Dokumentation:** `ergebnis_modelle.md`

### Zwei-Spiegel-Ansatz (weiterhin gültig, erweitert)

**Spiegel 1: IC-eigene Entwicklung** → Organisch gewachsene Bausteine auf den Tisch gelegt
**Spiegel 2: Ra/Aaron-Eigenrahmen** → Strukturelle Gegenbilder, Lücken, Konvergenzen
**Spiegel 3 (NEU): Cross-Framework** → Allgemeiner menschlicher Erkenntnisprozess (Ra, Aaron, Jung, IFS, Buddhismus, Heldenreise)

### Nächste Methodische Schritte

1. ~~Gegencheck~~ → ✅ | 2. ~~Zieldokumente~~ → ✅ | 3. ~~Einzelmodelle~~ → ✅
4. ~~3 Lücken~~ → ✅ | 5. ~~Thesen~~ → ✅ | 6. ~~Z1+Z3+Glossar füllen~~ → ✅
7. 🔴 **Z2 erstellen** — User-Journey, 7 Phasen, UX-Perspektive
8. **Z4 erstellen** — Technische Architektur
9. **Validierung** — Z1+Z3 gegen alte kern/-Dateien auf Vollständigkeit prüfen

**Token-Fenster:** Normales Kontextfenster reicht. Gezielt 3–5 Dateien pro Aufgabe.

---

## 5. Vorläufige Ergebnisse

### A1: Thesen + Prinzipien + Spannungsfelder (vorläufig)

**Stand:** 7 Thesen v2.0 + 5 Prinzipien + 6 Spannungsfelder
**Ra-Validierung:** 10/12 stark, 2/12 mittel, 0 Widersprüche
**9-Schritte-Einfluss:** Option A (Spiral-These) möglicherweise aufgelöst — der 9-Schritte-Prozess IST die Spirale (wiederholter Durchlauf pro Thema).
**Details:** `ergebnis_thesen_prinzipien.md`

### B: Modelle & Architektur (validiert + dokumentiert)

**Stand:** 9-Schritte-Prozess als Ordnungsprinzip. Cross-Framework-validiert (30. März). Z3 v0.4 dokumentiert alle Modelle einzeln.
**Ehemalige Lücken:** ~~Verkörperung, Diagnose, Transformation~~ → ✅ Operationalisiert (31. März): Anker (A4), Energiefluss-Diagnose (A5b), Leiter-Methodik (A9).
**Neue Konzepte (31. März):** Lernmoment, Gabel, P1-Sonderrolle, Schwelle, Wahl (→ z3 C1, C6, C7).
**Ra-Integration:** 6 Ra-Beiträge, Ra-7-vs-IC-9-Mapping (→ z3 C8), 3-vs-4-Erkenntniswege geklärt.
**Querschnitt:** Prisma = **7 Perspektiven**, Grammatik = Querschnitt, Stimme = stabil.
**Gesamtbild:** 5D-Inhaltsraum + 3 Erkenntniswege (+ Schwelle als 4. Dimension, nicht operationalisiert).
**Details:** `ergebnis_modelle.md` (v0.9) + `z3_modell_referenz.md` (v0.4) + `glossar.md` (v1.2)

---

## 6. Zieldokumente (definiert 29. März 2026)

Die Konsolidierung mündet in diese Enddokumente. Jedes hat eine eigene Perspektive und ein eigenes Ordnungsprinzip.

| # | Dokument | Perspektive | Ordnung | Status |
|---|---|---|---|---|
| **Z1** | **IC Gesamtwerk** | Philosophisch | Universeller Erkenntnisprozess (9 Schritte) | 🟢 **v0.5** — stabil, kein Update nötig |
| **Z2** | **IC User-Journey** | UX/Produkt | 7 Phasen (progressive Enthüllung) | 🟡 **v0.1** — veraltet! App-Spaces (JETZT/KARTE/WERKSTATT/ZEIT) fehlen, Anker v2 fehlt. Update nach Engine-Phase. |
| **Z3** | **IC Modell-Referenz** | Konzeptuell | Jedes Modell einzeln | 🟢 **v0.4** — stabil. Einziger Nachtrag: A4 Anker hat v2-Verweis auf ic_gesamtinventur.md §XIX.4 |
| **Z4** | **= cursor/ Dateien** | Technisch | KG-Schema, Pipeline, Engines | 🟢 **Entscheidung (1. April): Kein eigenes Z4.** cursor/{architecture,pipeline,contracts,engines,status}.md = die technische Doku. |
| **Z5** | **IC Ra/Aaron-Brücke** | Tiefenvalidierung | Ra/Aaron → IC-Übersetzung | 🟢 **Erledigt** — verteilt in Z1 §5.6 + Z3 C6–C8 + Glossar. Kein eigenes Dok. nötig. |
| **Z6** | **IC Story & Serie** | Narrativ | True Core Story, Botschafter, Staffel×Episode | ⬜ Nicht begonnen. Aus vision_and_story.md + alte Chats. Nicht priorisiert. |
| **—** | **Glossar** | Terminologie | Kanonische Begriffe + Verwechslungsschutz | 🟢 **v1.2** — stabil |
| **—** | **Gesamtinventur** | Inventar + Scope | Alle Bausteine + Scope v1/v2/v3 + Delta | 🟢 **v0.5** — Referenzdokument (wird nicht weiter aufgebläht) |

### Z1 — IC Gesamtwerk (v0.5 — tatsächliche Struktur)

- Teil 0: Ouvertüre (Genese, 7 Thesen, 5 Prinzipien, 6 Spannungsfelder)
- Teil 1: Der Prozess (9 Schritte, U-Bogen, 3 Eingänge, 3 Erkenntniswege + Schwelle, Gabel-Mechanismus)
- Teil 2: Die Bausteine (Übersicht, Zentralspindel mit Lernmoment/Schwelle/Wahl, Kehrseiten-Brücke, Tiefenschichten)
- Teil 3: Die Werkzeuge (Prisma, Grammatik, Stimme, Zeitgeist-Fallen als Querschnitt)
- Teil 4: Die Quellen (10 Systeme, Staffel-Logik)
- Teil 5: Ethik & Grenzen (Evidenzklassen, Widerspruchs-Protokoll, 8 Limitation Layers, Körper als Grenze, Graduation, Ra/Aaron-Integration mit 6 Beiträgen + Mapping)

### Z2 — IC User-Journey (Struktur-Entwurf, noch nicht erstellt)

- 7 Phasen mit UX-Triggers, Systemzuordnung, Ton
- 3 Eingänge (Chart-Signal, Lebensbereich, Zeitlinie) → verschiedene Einstiegs-Phasen
- 4 Handbuch-Tiefenschichten (Spiegel → Muster → Prozess → Experiment)
- Staffel × Phase Matrix
- 7 Phasen ↔ 9 Schritte Mapping (existiert in §6 + z1 §1.3)
- Gabel-Moment als UX-Entscheidungspunkt (wann bietet IC Vertiefung an?)
- Nervensystem-Check als Gate vor Tiefenarbeit (Sicherheits-Feature)

### Z6 — IC Story & Serie (Struktur-Entwurf)

- True Core Story (7 Kapitel: Verluste → Fragmente → Verbindung → Plattform → Erwachen → Übergang → Loslassen)
- 5 Botschafter-Figuren (Aria, Jian, Priya, Luka, Amara)
- Plattform-Phasen synchron zur Story (6 Phasen, 24 Monate)
- Episode-based Feature-Unlocking (Story-Episode → App-Feature)
- Nicht-extrahierte alte Chats enthalten vermutlich weiteres Story-Material

### Beziehung 7 Phasen ↔ 8/9 Schritte

Die 7 Phasen (Master v0.1) und die 9 Schritte (Cross-Framework + Verkörperung) sind ZWEI Sichten auf denselben Prozess:

| 7 Phasen (User-Journey, Z2) | 9 Schritte (Universell, Z1) | Gemeinsam |
|---|---|---|
| 1. Ankommen | 1. Eintritt + 2. Wiedererkennung | Sicherheit + Resonanz |
| 2. Erkennen | 3. Verortung | Muster sehen |
| 3. Verkörpern | 4. Verkörperung | Körper-Wissen |
| 4. Disposition (KERNMOMENT) | Konvergenz-Moment (kein eigener Schritt) | Multi-System-Aha |
| 5. Konfrontation | 5. Diagnose + 6. Vertiefung | Wo steckst du fest + Warum |
| 6. Integration | 7. Transformation | Was tun |
| 7. Horizont | 8. Zeitkontext + 9. Graduation | Timing + Abschluss |

Die 7 Phasen gehen in Z2 (User-Journey). Die 9 Schritte gehen in Z1 (Gesamtwerk). Vollständiges Mapping: `ergebnis_modelle.md` §6.

---

## 7. Konventionen

### Status-Codes

| Code | Bedeutung |
|---|---|
| 🔴 | Nächster Schritt / Blockiert |
| 🟡 | Vorläufig (Ergebnis existiert, wartet auf Abhängigkeit) |
| 🟢 | Final entschieden |
| ⬜ | Noch nicht begonnen |

---

*Status-Dokument v3.2 · 1. April 2026 · Phase 3 abgeschlossen. Z4 = cursor/. Weiterarbeit: cursor/status.md (Engine Eval Sprint).*
