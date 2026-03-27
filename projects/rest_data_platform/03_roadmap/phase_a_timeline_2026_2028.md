<!-- Reality Block
last_update: 2026-03-27
status: draft
scope:
  summary: "Phase A Plan bis 31.08.2028 (100% Stelle) – bewusst in Etappen, nicht zu schnell/nicht zu langsam."
  in_scope:
    - milestone cadence
    - external/internal communication rhythm
    - handover-ready outputs within Phase A
  out_of_scope:
    - Phase B (nach 31.08.2028) – da du dann nicht mehr da bist
notes:
  - "Mittel laufen bis 31.08.2030, aber Plan wird so geschrieben, dass Ende Phase A ein sauberer Übergabepunkt entsteht."
-->

# Phase A (28.01.2026 → 31.08.2028) – Zeitplan & Meilensteine

## Prinzipien
- **Nicht zu schnell**: erst “Basis + Nutzen” beweisen, dann skalieren.
- **Nicht zu langsam**: alle 6–10 Wochen ein sichtbares Artefakt (Demo, Report, Flow).
- **Handover by design**: bis 31.08.2028 sind Betrieb/Docs/Ownership so klar, dass jemand übernehmen kann.

## Stakeholder-Fokus (intern)
- Projektleitung: Kotzur, Hanfeld (ggf. Schleuter) + Schwesterprojekte (bei Relevanz).

## Cadence (Vorschlag)
- **Monatlich**: 1‑seitiges Status Update (Template siehe `04_communication/status_update_template.md`)
- **Pro Meilenstein**: kurze Demo + 3 Bullet “was ist jetzt möglich?”

## Roadmap – Etappen

### Etappe 0: Setup & Klarheit (Jetzt → +4 Wochen)
- **Output**:
  - Scope Shield final (`00_overview/scope_shield.md`)
  - MVP als “Minimum Useful Product” präzisiert (`00_overview/mvp.md`)
  - 1 Pilotdomäne **WP 2.1** Offshore‑CE + Datenzugriff geklärt (Plattform **WP 5.2**; wer darf was, wo liegt was?)
- **Kommunikation**:
  - Kickoff-Update: “Was ist es / was ist es nicht?”

### Etappe 1: MVP-Vertical Slice (ca. +5 bis +12 Wochen)
- **Output**:
  - 1 Upload-/Erfassungsflow + 1 Offshore‑Asset‑View + 1 Export/Report
  - Rollen/RLS minimal (wer sieht was)
- **Success Kriterien**:
  - 1–2 Nutzer können es ohne dich bedienen (Onboarding-Notiz/Video optional)

### Etappe 2: Datenqualität & Reporting (Q3–Q4 2026)
- **Output**:
  - Offshore‑Daten sauber strukturiert (Definitionen, Versionierung, “Quelle/Stand”)
  - 1–2 Standardreports (Superset o.ä.) als Single Source of Truth
- **Kommunikation**:
  - “Ab jetzt ist das der Ort, wo Zahlen/Status herkommen”

### Etappe 3: KI als Assist (lightweight, wenn wirklich nützlich) (2027 H1)
- **Output (optional, nur bei Bedarf)**:
  - RAG light (Q&A + Quellen) fuer Offshore‑Docs
  - DPP‑Light Demonstrator (1 Beispielkomponente)
  - Evaluation: Genauigkeit/Quellen/Fehlerfälle
- **Guardrails**:
  - klare Datenklassifizierung + keine sensiblen Inhalte unkontrolliert

### Etappe 4: Stabilisierung + Übergabepunkt (2027 H2 – 2028 H1)
- **Output**:
  - Betriebsdoku (Runbook), Rollen/Ownership, Backup/Restore-Test
  - “Definition of Done” für neue Domänen/Reports (Checkliste)
- **Kommunikation**:
  - Übergabeplan: wer übernimmt was, ab wann, mit welchem Zugriff

### Etappe 5: Finalisierung Phase A (2028 H2 bis 31.08.2028)
- **Output**:
  - Abschlussbericht/Deck (intern) + ggf. externe Kurzfassung
  - Übergabe-Session + “last known good” Release/Tag

## Offene Entscheidungen (halten wir bewusst offen)
- Monatlicher Rhythmus vs. rein Meilenstein-basiert (wir können in Q2 2026 entscheiden).
- Wie stark KI integriert wird (nur “Assist”, nicht Kernabhängigkeit).

