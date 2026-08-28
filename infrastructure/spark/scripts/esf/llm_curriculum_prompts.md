<!-- Reality Block
last_update: 2026-06-08
status: active
scope:
  summary: "LLM-Prompt-Vorlagen: ESF-Folien-Markdown → Lernmodule für Flora (Hermes-Tutor-Kontext)."
  in_scope:
    - Prompt-Kette Outline → Module → Karteikarten → Übungen
  out_of_scope:
    - Automatisierung / Skripte (manuell oder später)
-->

# ESF – LLM-Prompt-Vorlagen (Spark / SGLang)

Kontext für alle Prompts: **Duales Studium Physiotherapie**, Modul *Empirische Sozialforschung*. Zielgruppe lernt am besten durch **Erklären**, **Metaphern**, **kurze Phasen** — nicht durch Frontalunterricht. Output auf **Deutsch**, Fachbegriffe korrekt.

Input: eine extrahierte Markdown-Datei (MinerU/PyMuPDF). **Nicht** rohe PDFs.

---

## 1) Outline + Lernziele

```
Du erhältst extrahierte Folien (Markdown) aus einem ESF-Vorlesungsdeck.

Aufgabe:
1. Gliedere in 5–8 Kapitel (logische Lernsequenz, nicht Folienreihenfolge).
2. Pro Kapitel: 2–4 Lernziele (Verben: erklären, unterscheiden, anwenden, beurteilen).
3. Markiere jedes Kapitel: MUST (für 2-Wochen-Kompakt) oder NICE (vertiefend).
4. Nenne typische Prüfungsfallen / Missverständnisse.

Deck-Name: {{DECK_NAME}}
Markdown:
---
{{MARKDOWN_CHUNK}}
---

Format: Markdown mit ## Kapitel, ### Lernziele, Tags [MUST|NICE].
```

---

## 2) Lernmodul (pro Kapitel)

```
Erstelle ein Lernmodul aus dem Kapitel-Outline und den zugehörigen Folien.

Regeln:
- Max. 800 Wörter Fließtext + Bullet-Listen
- Jede Kernidee: 1 Alltags- oder Körper-/Therapie-Metapher (Physio-Bezug optional)
- Kein Motivations-Ton, kein Druck
- Statistik: Formeln nur wenn im Quelltext; Interpretation klar von Rechnung trennen
- Am Ende: "Erklär-es-zurück"-Frage (1 Satz)

Kapitel: {{KAPITEL_TITEL}}
Outline-Zeile: {{OUTLINE}}
Quell-Markdown:
---
{{MARKDOWN_CHUNK}}
---
```

---

## 3) Karteikarten (Anki/Mochi)

```
Erzeuge 8–12 Karteikarten für dieses Kapitel.

Format pro Karte (eine Zeile JSONL):
{"front":"...","back":"...","tags":["esf","{{KAPITEL}}"]}

Regeln:
- Front: präzise Frage, keine Fangfragen
- Back: max. 3 Sätze oder kurze Liste
- Bei Statistik: Interpretation > Formel auswendig
- Markiere unsichere Stellen mit [REVIEW]

Kapitel: {{KAPITEL_TITEL}}
Quelle:
---
{{MARKDOWN_CHUNK}}
---
```

---

## 4) Übungen + Musterlösung

```
Erstelle 3 Übungen (steigende Schwierigkeit) + Musterlösungen.

Typen (mix):
- Begriff zuordnen / Lückentext
- Mini-Fall (fiktive Physio-Fragestellung: Forschungsfrage formulieren)
- Interpretation (p-Wert, Gütekriterien, Stichprobe) — kein SPSS/R nötig

Pro Übung:
- Aufgabenstellung (klar)
- Hinweis (1 Satz)
- Musterlösung (mit Begründung)
- Häufiger Fehler

Kapitel: {{KAPITEL_TITEL}}
Quelle:
---
{{MARKDOWN_CHUNK}}
---
```

---

## 5) Glossar (kumulativ)

```
Extrahiere alle Fachbegriffe aus dem Modul. Pro Begriff:
- Definition (1–2 Sätze, prüfungsfest)
- Abgrenzung zu verwandten Begriffen (wenn relevant)
- Mini-Beispiel aus Therapieforschung

Bestehendes Glossar (ergänzen, nicht duplizieren):
{{GLOSSAR_BISHER}}

Neues Material:
---
{{MARKDOWN_CHUNK}}
---
```

---

## Review-Checkliste (menschlich, Pflicht)

- [ ] Statistik: p-Wert, Fehler 1./2. Art, Skalenniveaus korrekt?
- [ ] Qualitative Auswertung: Kodierung vs. Kategorisierung klar?
- [ ] Keine erfundenen Studien oder Zahlen
- [ ] MUST-Kapitel decken 2-Wochen-Ziel ab (~60 % Tiefe)
