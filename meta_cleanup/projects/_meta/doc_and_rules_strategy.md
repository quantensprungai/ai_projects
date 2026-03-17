# Doku & Rules Strategie

<!-- Reality Block
last_update: 2026-02-16
status: living
scope:
  summary: "Wie Docs und Cursor-Rules organisiert werden. Rules First, Docs Lean, cursor/ + reference/ Pattern."
  in_scope:
    - Prinzipien
    - Limits und Konventionen
    - Pro-Projekt-Struktur
  out_of_scope:
    - Inhalte einzelner Docs
notes: []
-->

## Kernprinzip: Rules First, Docs Lean

Rules werden automatisch geladen (globs, alwaysApply) — KI hat sie im Kontext ohne @-Mention. Docs sind Referenz für Vertiefung, nicht Einstieg.

## Projekt-Struktur-Muster (cursor/ + reference/)

Jedes aktive Projekt folgt diesem Muster (Inner Compass als Referenz-Implementierung):

```
projects/<projekt>/
├── cursor/                 ← KI liest primär hier
│   ├── README.md           ← Index + Kernzahlen (< 80 Zeilen)
│   ├── status.md           ← Was existiert, was fehlt (< 300 Zeilen)
│   ├── handover.md         ← Copy-Paste für neue Sessions (< 100 Zeilen)
│   └── [contracts, architecture, pipeline, ...]  ← Projektspezifisch
│
├── reference/              ← Mensch-Kontext (KI liest nur bei Bedarf)
│   ├── prd.md / vision.md  ← Produktvision
│   ├── decisions.md        ← Design-Entscheidungen (ADR-lite, laufend)
│   └── [ideas, inspirations, ...]  ← Projektspezifisch
│
├── 99_archive/             ← Altes, nicht referenzieren
└── README.md               ← Projekt-Index
```

Nicht jedes Projekt braucht alle Dateien. Ein kleines Projekt kommt mit cursor/README.md + cursor/status.md + reference/decisions.md aus.

## Limits

| Bereich | Limit | Begründung |
|---------|-------|------------|
| Aktive Docs in cursor/ | 6-8 | Token-Effizienz |
| Zeilen pro Doc | < 300 | KI liest gezielt |
| Rules pro Code-Repo | 10-15 | Fokussiert |
| Rules: Zeilen pro Datei | < 50 | Cursor Best Practice |

## Wann neue Docs — wann nicht

**Ja:** Neuer Vertrag (Contract), operatives Runbook, eigenständiges Thema.
**Nein:** "Könnte nützlich sein" (→ scratch/inbox), passt in bestehende Doc (→ Abschnitt ergänzen), nur für einen Chat (→ handover/status).

## Rules-Architektur

```
.cursor/rules/
├── ai-projects-global.mdc      ← alwaysApply: true (Repo-Intent, Sprache, Konventionen)
├── inner-compass-context.mdc   ← globs: projects/inner_compass/**,code/hd_saas_app/**
├── spark-serving.mdc           ← globs: infrastructure/spark/**
└── [weitere-projekt-context.mdc]  ← Pro aktivem Projekt eine Rule

code/<repo>/.cursor/rules/
├── [framework-rules]            ← Makerkit, DB, Security etc. (Code-spezifisch)
└── [projekt]-docs.mdc           ← Verbindung zu ../../projects/<name>/cursor/
```

## Chat-Handover (vereinfacht)

Beim Chat-Wechsel: cursor/handover.md öffnen → Block kopieren → in neuen Chat einfügen. Der Block enthält Kontext, Links, nächste Schritte — keine Specs. KI liest dann gezielt die verlinkten Docs.

## Wartung

- Nach jedem Meilenstein: status.md aktualisieren
- Bei neuer Entscheidung: decisions.md ergänzen
- Vierteljährlich: "Haben wir Docs die niemand liest?" → archivieren
