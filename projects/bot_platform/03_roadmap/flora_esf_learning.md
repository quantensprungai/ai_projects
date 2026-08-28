<!-- Reality Block
last_update: 2026-06-08
status: active
scope:
  summary: "Flora ESF (Empirische Sozialforschung): PDF-Pipeline, 14-Tage-Curriculum, Hermes-Tutor — ohne OpenClaw/HD-Worker."
  in_scope:
    - Architektur Spark (Batch) + Hermes (Tutor)
    - 14-Tage-Plan
    - Dateipfade und Deploy
  out_of_scope:
    - Clawdbot-Produktions-Cutover
    - Supabase/RAG-Pipeline
-->

# Flora – ESF Lernprogramm (2 Wochen)

**Lernende:** Flora, duales Studium Physiotherapie (Hochschule Osnabrück / Prof.-Grewe-Schule).

**Tutor-Agent:** **Hermes**, Profil `pilot` auf VM102 — **nicht** OpenClaw/Clawdbot (Produktion bleibt parallel). Persona **Sage** aus [`infrastructure/docker/workspace-flora/`](../../../infrastructure/docker/workspace-flora/).

**Quellen (lokal):**

| Deck | Seiten | PyMuPDF-Zeichen | Strategie |
|------|--------|-----------------|-----------|
| ESF_EINFÜHRUNG_EPDUAL | 88 | ~32k | PyMuPDF reicht oft |
| QUALITATIVE_METHODEN_ESF_EPDUAL | 57 | ~20k | MinerU (Diagramme) |
| QUANTITATIVE_METHODEN_ESF_EPDUAL | 183 | ~58k | MinerU (Formeln/Grafiken) |

PDFs liegen unter `Downloads/` (Windows) → einmalig nach Spark kopieren.

---

## Architektur

```
PDFs (3 Decks)
    → Spark: MinerU/PyMuPDF Batch (einmalig)
        → Markdown (3 Dateien)
            → Spark: LLM-Strukturierung (Outline, Module, Karten, Übungen) + menschliches Review
                → workspace-flora/learning/esf/ (Hermes-Kontext)
                    → Flora: 14-Tage-Plan (offline/lightweight)
                        → Hermes/Sage: Tutor on-demand (Telegram Pilot)
```

| Phase | Wo | GPU? |
|-------|-----|------|
| PDF → Markdown | Spark | Ja (MinerU) |
| Markdown → Module | Spark (SGLang) oder Anthropic | Optional |
| Tägliches Lernen | Floras Gerät | Nein |
| Fragen / Erklären | Hermes `pilot` | Nein (API) |

**Parsing ist Vorbereitung, nicht das Lernsystem.** Kein HD-Worker, keine Supabase-Pipeline nötig.

---

## Schritt 1 — Extraktion (Spark)

Skript: [`infrastructure/spark/scripts/esf/mineru_batch_esf.sh`](../../../infrastructure/spark/scripts/esf/mineru_batch_esf.sh)

```bash
# PDFs hochladen
scp ~/Downloads/*ESF* user@spark:~/batch/esf/input/

# Auf Spark (ggf. SGLang stoppen für VRAM)
bash ~/ai_projects/infrastructure/spark/scripts/esf/mineru_batch_esf.sh \
  ~/batch/esf/input ~/batch/esf/output

# Markdown zurück
scp user@spark:~/batch/esf/output/*.md \
  infrastructure/docker/workspace-flora/learning/esf/source/
```

Qualitätsprobe: **5 Folien pro Deck** manuell gegen PDF (Formeln, Tabellen).

---

## Schritt 2 — Strukturierung (LLM + Review)

Prompt-Vorlagen: [`infrastructure/spark/scripts/esf/llm_curriculum_prompts.md`](../../../infrastructure/spark/scripts/esf/llm_curriculum_prompts.md)

Reihenfolge: Outline → Module (MUST only) → Karteikarten → Übungen → Glossar.

**Pflicht-Review** bei Statistik und p-Werten — LLM-Fehler sind hier teuer.

---

## Schritt 3 — Hermes-Kontext deployen

Curriculum-Dateien ins Flora-Workspace (Hermes liest `MESSAGING_CWD=~/clawd/workspace-flora`):

```bash
scp -r infrastructure/docker/workspace-flora/learning/esf \
  user@docker-apps:~/clawd/workspace-flora/learning/

# Hermes pilot: Workspace-Dateien synchron (falls noch nicht)
for f in SOUL.md USER.md AGENTS.md; do
  cp -a ~/clawd/workspace-flora/"$f" ~/.hermes/profiles/pilot/
done
```

Hermes Runbook: [`infrastructure/docker/HERMES_PILOT_VM102_RUNBOOK.md`](../../../infrastructure/docker/HERMES_PILOT_VM102_RUNBOOK.md)

Sage nutzt **kuratiertes** Modul + Glossar — **nicht** die rohen 328 Folien als RAG.

---

## 14-Tage-Curriculum

Detail: [`infrastructure/docker/workspace-flora/learning/esf/curriculum_14d.md`](../../../infrastructure/docker/workspace-flora/learning/esf/curriculum_14d.md)

**Rhythmus (Flora-spezifisch):**

- Max. **90 Min** pro Block, dann **Körperpause**
- **30 %** Lesen, **40 %** aktiv (Übungen, Kodieren, Datensätze), **20 %** Recall, **10 %** Hermes bei Fragen
- Kein Streak-Tracking, kein Druck — Tutor nur **on-demand**
- Lieber **Erklär-es-zurück** als ungefragte Quizze (außer Flora bittet explizit um Abfrage)

### Woche 1 — Forschungslogik + Qualitativ

| Tag | Fokus | Aktivität |
|-----|-------|-----------|
| 1–2 | Empirischer Forschungsprozess | Forschungsfrage formulieren, Gütekriterien |
| 3–4 | Qualitative Designs | Mini-Studienplan für fiktive Physio-Frage |
| 5–6 | Qualitative Auswertung | Transkript-Snippet kodieren |
| 7 | Review | „Erkläre den Forschungsprozess in 5 Minuten“ (laut sprechen) |

### Woche 2 — Quantitativ

| Tag | Fokus | Aktivität |
|-----|-------|-----------|
| 8–9 | Skalenniveaus, deskriptive Statistik | Datensatz beschreiben (M, SD) |
| 10–11 | Hypothesentest, p-Wert, Fehler 1./2. Art | Szenarien interpretieren |
| 12–13 | Studiendesigns | Studie kritisch lesen |
| 14 | Abschluss | Mixed-Methods-Frage + Selbsttest |

**Ziel:** Forschungsprozess verstehen + qualitative und quantitative Methoden **anwenden** können — nicht jede Folie auswendig.

---

## Prüfungsformat (geklärt)

Siehe [`pruefung_format.md`](../../../infrastructure/docker/workspace-flora/learning/esf/pruefung_format.md):

- **60–90 Min**, **~20–25 Aufgaben**
- **1–3 Kopfrechnen** ohne Taschenrechner (Mittelwert, einfache Prozente)
- Schwerpunkt: Begriffe, Zuordnung, Interpretation — kein SPSS/R

## Spark offline → lokale Pipeline

```powershell
pip install anthropic pypdf python-dotenv
python infrastructure\spark\scripts\esf\esf_local_pipeline.py extract
python infrastructure\spark\scripts\esf\esf_local_pipeline.py all
```

Doku: [`infrastructure/spark/scripts/esf/README.md`](../../../infrastructure/spark/scripts/esf/README.md) · Key in `learning/esf/.env` (nicht committen).

**Kosten `all`:** ca. 2–5 € (Haiku + Sonnet für Quant/Prüfung).

## Offen

- **Startdatum** für den 14-Tage-Plan

---

## Fallstricke

- LLM-Module ohne Review → Statistik-Fehler
- Zu viel Stoff → 60 % sicher schlägt 100 % oberflächlich
- Nur lesen → bei Quant bleibt wenig hängen
- Roh-PDF als Tutor-Kontext → schlecht; kuratiertes Modul ist besser
