<!-- Reality Block
last_update: 2026-01-28
status: draft
scope:
  summary: "Offener Ideen-Backlog für ReST Data Platform (ASTRA) – bewusst noch nicht festgelegt."
  in_scope:
    - ideation
    - hypotheses and experiments
    - candidate deliverables
  out_of_scope:
    - secrets/tokens
notes:
  - "Diese Datei ist absichtlich offen/unscharf. Entscheidungen wandern später in Roadmap/MVP/Scope."
-->

# Ideen-Backlog (offen) – ReST Data Platform (ASTRA)

## Zweck
Diese Seite ist ein **ideation space**: mögliche Projektideen skizzieren, ohne zu früh “festzunageln”.
Alles hier ist **Hypothese**, bis es in `00_overview/mvp.md` + `00_overview/scope.md` überführt wurde.

## Leitfragen
- **Welches konkrete Problem** (bei ASTRA / Region / Stakeholdern) lösen wir als erstes?
- Was wäre ein **sichtbarer Nutzen in < 8 Wochen**?
- Welche Daten/Dokumente sind **wirklich verfügbar** und rechtlich/organisatorisch nutzbar?
- Wo hilft KI **real** (Zeit sparen, Qualität erhöhen) – und wo ist es “nice to have”?

## Kandidaten-Ideen (grobe Skizzen)

### A) “Single Source of Truth” für Indikatoren & Projekte
- **Hypothese**: Der größte Schmerz ist nicht “KI”, sondern **Struktur + Nachvollziehbarkeit**.
- **Outcome**: ein Portal, das Indikatoren/Projekte/Uploads konsistent ablegt + einfache Exporte/Reports ermöglicht.
- **Experiment**: 1 Datendomäne + 1 Reporting-View (Superset) + 1 Upload-Flow.

### B) Dokumentenbasierte Q&A (RAG light)
- **Hypothese**: Es gibt wiederkehrende Fragen zu Dokumenten/Reports; Q&A spart Zeit.
- **Outcome**: “Frage stellen → Quellen + Kurzantwort”.
- **Risiken**: Rechte/Vertraulichkeit; Halluzinationen; Erwartungsmanagement.
- **Experiment**: 20–50 Dokumente, 5–10 typische Fragen, Evaluations-Checkliste.

### C) “LLM-Assist” für Projektkommunikation (intern/extern)
- **Hypothese**: Regelmäßige Updates kosten viel Zeit; LLM kann Entwürfe liefern.
- **Outcome**: status update drafts, milestone summaries, stakeholder-specific versions.
- **Experiment**: Template + 3 Beispielupdates; Feedback-Schleife mit Projektleitung.

### D) Whiteboard/Collaboard als “Planungs-Frontend” (optional)
- **Hypothese**: Ideen/Strukturen entstehen im Whiteboard; automatisches “Strukturieren” wäre wertvoll.
- **Outcome**: LLM generiert Board-Struktur (Swimlanes, Sticky Notes, Roadmap-Karten).
- **Experiment**: Erst manuell definieren: gewünschtes JSON/Schema → dann API/Automation (siehe unten).

## Collaboard: “Von LLM → Board” (Skizze)

> Collaboard bietet API Keys zur Authentifizierung für die öffentliche API “im Namen des Key-Owners”.
> Diese Keys sind **hochprivilegiert** und sollten nur am Zielort gespeichert werden. Sie sind zudem zeitlich befristet.  
> Quelle: [Collaboard Help Center – API Keys](https://help.collaboard.app/api-key)

### Minimaler Ansatz (realistisch, ohne Magie)
- **Schritt 1**: LLM erzeugt einen **Board-Plan** als JSON (z. B. `columns`, `cards`, `text`, `links`).
- **Schritt 2**: Ein kleiner “Connector” sendet daraus **API Calls** an Collaboard.
- **Schritt 3**: Ergebnis wird im Board sichtbar; danach manuell verfeinern.

### Offene Punkte (müssen wir noch klären)
- Welche **API Endpoints** sind in der Academic Cloud Instanz verfügbar/erlaubt?
- Wie identifizieren wir das Ziel (Board/Project IDs) für z. B. `https://whiteboard.academiccloud.de/collaboard/13254`?
- Ist der Zugriff von deinem Arbeitsplatznetz **erlaubt** (Firewall/SSO/Tenant)?

