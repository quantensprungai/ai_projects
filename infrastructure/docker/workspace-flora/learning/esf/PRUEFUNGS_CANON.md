# ESF — Prüfungs-Canon (priorisiert)

## Was zählt wirklich?

| Quelle | Gewicht | Inhalt |
|--------|---------|--------|
| **Dozentin S. 2–4** (`Wiederholung_EPdual.md`) | **Pflicht** | Themenvorlesung — das ist die Prüfungsbreite |
| **Altfragen Klausur** (`source/Altfragen_Klausur_Natalie.md`) | **Pflicht** | Konkrete Aufgabentypen |
| **Physiopraxis 2-teiler** (`reader/PHYSIOPRAXIS_ESF_2TEILER.md`) | **Pflicht-Leseergänzung** | Ein durchgängiges RCT: PICOT/Designs (Teil 1) + p-Wert/Auswertung (Teil 2) |
| **PICO/PICOT** (Flora-Notiz + Altfragen) | **Pflicht** | Schema + **eigene** Forschungsfrage formulieren |
| **PICO-Fälle S. 5–8** (Dozentin-PDF) | **Übung, nicht Pflichtstoff** | Nur Beispiele für Schülerfragen — **nicht** „kommt so dran“ |
| **27 LLM-Module** | Nachschlag | Canon filtert auf Kernkapitel |

---

## Altfragen → unsere Dateien

| Klausur-Thema | Lesen | Üben |
|---------------|-------|------|
| ESF-Definition + Bestandteile | `modules/02` | `exercises/02` |
| Induktion/Deduktion (5+5 Merkmale) | `modules/03` | `exercises/03` |
| Wiss. vs. statistische Hypothese | `modules/04` | `exercises/04` |
| Qual vs. Quant (Kernunterschiede) | `modules/06`, `07` | `exercises/06`, `07` |
| Gütekriterien qualitativ (4) | `modules/16` | `exercises/16` |
| Pearson r — wann? | `modules/22` + Dozentin S. 11 | `exercises/22` |
| Streuung, Korrelation aus Graph | `modules/21`, `22` | `exercises/21`, `22` |
| p-Werte / Outcomes | `modules/24` | `exercises/24` |
| Text „quantitativ“ schreiben | `modules/05`, `21` | `exercises/05` |
| **PICO / PICOT** | `source/Wiederholung_EPdual.md` (Rahmen) | **Eigene Physio-Frage** formulieren |
| **SPIDER** | ggf. Sage / erste Vorlesung | Eigene Frage (wie PICO) |
| Dichotom | `modules/20` (Skalen) | `exercises/20` |

**SPIDER:** Falls nicht im Modul — in Erstvorlesung/Folien nachschlagen; Sage kann Struktur erklären.

---

## Was heißt „27 → ~15 Kernkapitel“?

Die Pipeline hat aus **3 PDF-Decks** insgesamt **27 Modul-Dateien** erzeugt — inkl. Meta-Zeug und Doppelungen.

**Flora muss nicht alle 27 lesen.** Der **Reader** enthält **15 inhaltliche Kapitel**:

- **Woche 1:** 9 Abschnitte (Grundlagen + Qual)
- **Woche 2:** 6 Abschnitte (Quant)

**Überspringen (7 Meta-Dateien):** `01_`, `09_`, `10_`, `17_`, `26_`, `27_` usw.

→ Gleicher Stoff, weniger Datei-Chaos. **Lesen + Übungen** in `reader/FLORA_ESF_WOCHE1.md` und `WOCHE2.md`.

---

## PICO / PICOT (Flora-Notiz)

**P** Population · **I** Intervention · **C** Comparison · **O** Outcome · (**T** Time bei PICOT)

Prüfungstypisch: **Schema erklären** + **eigene Forschungsfrage** (Physio-Beispiel).

Die 4 langen Fälle in der Dozentin-PDF = Übungsmaterial, ein Fall reicht zum Üben.

---

## Apps (kostenlos, iPad + PC)

| Gerät | App | Warum |
|-------|-----|-------|
| **iPad** | **Obsidian** (kostenlos) | Markdown schön, Sync möglich (iCloud) |
| **iPad** | **Markor** (kostenlos) | Einfach, nur Lesen/Bearbeiten |
| **iPad** | **Apple Dateien** + Export | PDF aus Reader wenn du pandoc machst |
| **PC** | **Obsidian** | Gleiche Vault wie iPad |
| **PC** | **Cursor/VS Code** | Preview mit `Strg+Shift+V` |

**Empfehlung:** `reader/FLORA_ESF_WOCHE1.md` in **Obsidian-Vault** legen (iCloud) → iPad + PC gleicher Stand.

PDF nur optional: `pandoc reader/FLORA_ESF_WOCHE1.md -o Woche1.pdf`
