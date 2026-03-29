# IC Extraktion — 25. Feb 2026 Chat — Gesamtzusammenfassung

> **Quelle:** Konsolidierungs-Chat vom 25. Feb 2026 (inkl. 4 eingebettete Docs + Leitdokument v2.0 Artefakt)
> **Extrahiert:** 28. März 2026 | 4 Chunks | 6 Schichten (A–F)

---

## Zählung

| Schicht | Einträge | Beschreibung |
|---------|----------|-------------|
| A — Substanz | 46 | Konzepte, Entscheidungen, Modelle, Schemata |
| B — End-of-Answer | 7 | Steuerungssignale am Ende von KI-Antworten |
| C — KI-Korrekturen | 4 | Revisionen früherer KI-Aussagen |
| D — Nutzer-Klärungen | 9 | User-Impulse die Erkenntnissprünge auslösten |
| E — Synthese-Überschuss | 10 | Artefakt-Inhalte die nie besprochen wurden |
| F — Delta Artefakt↔Referenz | 8 | Abweichungen zwischen Artefakt und Input-Docs |
| **Gesamt** | **84** | |

---

## Top-10 Erkenntnisse (priorisiert nach Auswirkung)

### 1. Variante D — Zwei-Ebenen-Architektur (A-03)
KERN (Fundament + Leitdokument als bidirektionales Paar) + AUSSPIELUNG (Produkt, Vermittlung, Forschung). Supersedes alle früheren Hierarchie-Modelle. **Heute im Repo umgesetzt** als `kern/` + `bridge/` + `cursor/`.

### 2. 7-Phasen-Modell als verbindliche vertikale Architektur (A-09, F-07)
Phasen ≠ Stufen. Ankommen→Erkennen→Verkörpern→Disposition→Konfrontation→Integration→Horizont. Phase 4 = Kernmoment (Meta-System wird erlebbar). **Fehlte komplett in Master v2** — nur durch diesen Chat ins Leitdokument gekommen.

### 3. Dynamik = 4 Dimensionen (A-20)
Astronomisch + Psychologisch + Biographisch + Prozessual. Schärft den vagen "Zeitlinie"-Begriff zu einer vollständigen Dynamik-Architektur. **User-getrieben** ("da steckt mehr drin als Transite").

### 4. Innere Strategie = 4 Faktoren + offener Kern (A-16, C-03)
f(Signatur, Konditionierung, Bewusstsein, Zyklus). Abgeleitet aus der Zwiebel-These, aber "Zyklus" als neuer Faktor aus der Dynamik-Diskussion (F-05). **User-Nachfrage korrigierte 3→4**.

### 5. 5 Navigationsachsen (A-21)
Landkarte (räumlich) / Handbuch (inhaltlich) / Fluss-Diagramm (relational) / Zeitlinie (dynamisch) / Heldenreise (narrativ). Löst die Begriffsverwirrung Landkarte≠Handbuch≠Heldenreise auf. **Fundamentale UX-Architektur.**

### 6. 3-Schicht-Release-Modell (A-26)
Serie (viral, 5 Botschafter) → Global Unlock (Community-Moment) → Personal (Chart-basiert individuell). Netflix+Spotify-Metapher. **Differenzierungsmerkmal im Release.**

### 7. 11 statt 10 Lebensbereiche (A-17, C-04)
"Emotionen & Innenwelt" als eigener Bereich #2 — dichteste System-Abdeckung, höchstes Retention-Potenzial, Enneagramm-Brücke. **User-Nachfrage korrigierte 10→11.**

### 8. Hypothesenregister — Migrations-Verlust (A-31)
7 testbare Hypothesen (alter Master) gingen bei Gen-1→Gen-2 komplett verloren. Für Strang 3 (Forschung) kritisch. **Im Leitdokument v2 auf 10 erweitert (E-04).**

### 9. Synthese-Schemata im Artefakt (E-01, E-02)
inner_strategy JSON-Schema und Affect-Tracking Felder (Valence/Arousal) — nie besprochen, aber implementierungsrelevant. **Prüfungsbedarf ob in v5.1 angekommen.**

### 10. True Core Story ≠ 7 Phasen (A-38)
Die öffentliche Projekt-Story (7 Kapitel) und die User-Heldenreise (7 Phasen) sind zwei verschiedene 7er-Strukturen. **Diese Unterscheidung fehlt in den aktuellen Docs.**

---

## Kritischste Verluste (existiert nur in dieser Quelle)

| # | Was | Wo im Chat | Im Ist-Stand (v5.1)? |
|---|-----|-----------|---------------------|
| 1 | Kongruenz-Matrix (6 kongruent, 5 divergent) mit Delta-Analyse | A-15, Chunk 1 | UNKLAR — Methodik, nicht Inhalt |
| 2 | Plattform-Phasen mit 24-Monats-Timing (A-39) | Chunk 3 | UNKLAR — vermutlich nicht migriert |
| 3 | MCP-Readiness Vision 2027 (A-41) | Chunk 3 | UNKLAR — nicht in cursor/architecture.md |
| 4 | Priority Rules / Emergent Logic (A-45) | Chunk 3 | UNKLAR — Reasoning-Layer nicht definiert |
| 5 | V-förmiger Einstieg als offene Frage OE-11 (A-28) | Chunk 2 | UNKLAR — Status in v5.1 prüfen |

---

## Naming-Evolutionen (chronologisch)

| Schritt | Vorher | Nachher | Auslöser |
|---------|--------|---------|----------|
| 1 | Master Document | Leitdokument / IC_Steuerung | Option B Naming (D-03) |
| 2 | Strang 0 | Fundament / IC_Fundament | Option B Naming |
| 3 | Strang 1/2/3 | Produkt / Vermittlung / Forschung | Option B Naming |
| 4 | 5 Kapitel | 7 Phasen | Delta 1 (A-09) |
| 5 | 10 Lebensbereiche | 11 Lebensbereiche | Delta 5 + User-Impuls (D-06) |
| 6 | 3 Faktoren | 4 Faktoren + offener Kern | User-Impuls (D-05) |
| 7 | Dynamik = Transite | Dynamik = 4 Dimensionen | User-Impuls (D-08) |
| 8 | Spiegel = Kernmetapher | Spiegel = Schritt 1 | User-Impuls (D-07) |
| 9 | E-01–E-14 (Master v2) | E-01–E-24 (Leitdokument) | Umnummerierung (F-03) |
| 10 | F-01–F-07 (Master v2) | OE-01–OE-11 (Leitdokument) | Umnummerierung (F-04) |

---

## Offene Prüfpunkte (gegen IC_Leitdokument v5.1 abgleichen)

- [ ] Sind alle 10 Hypothesen (H-01–H-10) in v5.1 angekommen?
- [ ] Ist das inner_strategy Schema (E-01) in v5.1 oder cursor/contracts.md?
- [ ] Sind die Affect-Tracking Felder (E-02) irgendwo spezifiziert?
- [ ] Existiert die Zwiebel→KG Mapping-Tabelle (E-05)?
- [ ] Ist die Feature-Map mit Priorisierung (E-03) aktuell?
- [ ] Ist die E-Nummern-Mapping-Tabelle (Master v2 → Leitdokument) erstellt worden?
- [ ] Status von OE-11 (V-Einstieg bei Phase 4)?
- [ ] Ist MCP-Readiness (A-41) irgendwo dokumentiert?
- [ ] True Core Story vs. 7 Phasen — ist die Unterscheidung in v5.1?

---

## Dateien dieser Extraktion

| Datei | Inhalt |
|-------|--------|
| `konsolidierungs-chat_25feb_klassifikation.md` | Klassifikation (Prompt 1) + Quellen-Inventar + Methodenerweiterung |
| `25feb_extraktion_chunk1.md` | Chunk 1: Architektur, Ist-Analyse, 5 Deltas |
| `25feb_extraktion_chunk2.md` | Chunk 2: Vertiefungen, Lebensbereiche, Dynamik, Navigationsachsen |
| `25feb_extraktion_chunk3.md` | Chunk 3: Eingebettete Docs (Migrations-Verluste, Vision, Inspirationen) |
| `25feb_extraktion_chunk4.md` | Chunk 4: Artefakt-Analyse (Synthese-Überschuss + Deltas) |
| `25feb_extraktion_zusammenfassung.md` | Diese Datei — Gesamtübersicht |
| `extraktions-prompt_v1.md` | Der Extraktions-Prompt (Werkzeug) |
