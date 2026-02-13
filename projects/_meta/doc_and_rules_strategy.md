# Doku & Rules Strategie – AI-freundliche Projektstruktur

<!-- Reality Block
last_update: 2026-02-13
status: living
scope:
  summary: "Gesamtplan: Wie Doku und Cursor-Rules organisiert werden, damit kein Wildwuchs entsteht und KI/Entwickler Kontext behalten."
  in_scope:
    - Prinzipien (Rules First, Docs Lean)
    - Limits und Konventionen
    - Pro-Projekt-Struktur
    - Wartung
  out_of_scope:
    - Inhalte einzelner Docs
notes:
  - "Cursor/Community: Rules unter 50 Zeilen, modular, globs für Kontext. Dateien unter 300 Zeilen für Token-Effizienz."
  - "Referenz: .cursor/skills-cursor/create-rule/SKILL.md, Lambda Curry Cursor Rules Best Practices"
-->

## 1. Das Problem

- **Viele Docs** → KI kann nicht alles lesen (Context-Window)
- **Neue Chats** → Kontext geht verloren
- **Wildwuchs** → Unübersichtlich, Duplikate, veraltete Referenzen
- **Code + Docs getrennt** → hd_saas_app hat eigene Docs, projects haben eigene – wo ist die Wahrheit?

**Ziel:** Eine lebende Struktur, die skaliert und KI/Entwickler schnell auf den richtigen Kontext bringt.

---

## 2. Kernprinzip: Rules First, Docs Lean

### Rules übernehmen, was Docs oft tun

| Regel | Warum |
|-------|-------|
| **Rules werden automatisch geladen** (globs, alwaysApply) | KI hat sie im Kontext, ohne @-Mention |
| **Rules sind kurz** (< 50 Zeilen pro Datei) | Token-effizient, fokussiert |
| **Rules sind actionable** | "So machst du X" statt "X ist dokumentiert in …" |
| **Docs sind Referenz** | Vertiefung, wenn nötig – nicht als Einstieg |

### Docs werden schlank gehalten

- **Max. 15–20 aktive Docs pro Projekt** (ohne 99_archive)
- **Ein Einstieg pro Projekt:** README + current_status + next_steps
- **Keine neuen Docs** ohne Prüfung: "Kann das in eine Rule? Oder in bestehende Doc?"

---

## 3. Die lebende Struktur

### Root (ai_projects)

```
.cursor/rules/
  ai-projects-global.mdc    # Immer: Repo-Intent, Doku-Konventionen, Sprache
  spark-serving.mdc         # Wenn infrastructure/spark relevant

projects/_meta/
  master_map.md            # Projektlandkarte
  doc_and_rules_strategy.md  # Dieser Plan
  chat_handover_template.md  # Schablone für Chat-Wechsel
```

### Pro Projekt (z.B. hd_saas)

```
projects/hd_saas/
  README.md                 # Einstieg + Links (nicht Spez)
  00_overview/
    current_status_local_dev.md   # Single Source of Truth: Status
    chat_handover_hd_saas.md      # Copy-Paste für Chat-Wechsel
  02_system_design/
    next_steps_was_fehlt_noch.md  # Priorität, Reihenfolge
    <contracts>                   # interpretations, dimensions, text2kg_spec
    <3–5 weitere Specs>           # Nur die, die aktiv referenziert werden
  99_archive/               # Deprecated, alte Versionen

  # NICHT: 50+ Dateien in 00/01/02/03/04
```

### Code-Repo (hd_saas_app)

```
code/hd_saas_app/
  .cursor/rules/            # Code-spezifisch (Makerkit, DB, etc.)
  docs/                     # Nur: Ingestion, Setup, Troubleshooting
  AGENTS.md / CLAUDE.md     # Kurz, auf Rules verweisen
```

**Konvention:** Docs für "wie starte ich, wie deploye ich" – nicht für Architektur (die liegt in projects/).

---

## 4. Konkrete Limits

| Bereich | Limit | Begründung |
|---------|-------|------------|
| **Aktive Docs pro Projekt** | 15–20 | KI kann ~20–30 Dateien sinnvoll im Kontext halten |
| **Zeilen pro Doc** | < 300 | Token-Effizienz (Community-Empfehlung) |
| **Rules pro Code-Repo** | 10–15 | Fokussiert, nicht überladen |
| **Rules: Zeilen pro Datei** | < 50 | Cursor Best Practice |
| **Neue Doc anlegen** | Nur wenn: "Passt in keine bestehende" UND "wird aktiv referenziert" | Verhindert Wildwuchs |

---

## 5. Wann neue Dokumente – wann nicht

### ✅ Neue Doc anlegen, wenn

- Operatives Runbook (z.B. Spark Worker Recovery) – eigenes Thema
- Neuer Vertrag (z.B. interpretations_contract) – zentraler Referenzpunkt
- Projekt-übergreifendes Thema (z.B. Anna's Archive → HD-SaaS Flow)

### ❌ Keine neue Doc, wenn

- "Das könnte mal nützlich sein" → Scratch/Inbox, später promoten
- Inhalt passt in bestehende Doc → Abschnitt ergänzen
- Nur für einen Chat → In Chat-Handover oder current_status
- Spezifikation für etwas, das noch nicht implementiert ist → Backlog, nicht eigenes Doc

---

## 6. Rules-Strategie

### Global (ai_projects Root)

- **ai-projects-global:** Repo-Intent, Doku-Konventionen, Sprache, Projects↔Code↔Infra Crosslinks
- **spark-serving:** Wenn an Spark/LLM/Infra gearbeitet wird

### Pro Code-Repo (hd_saas_app)

- **Bereits vorhanden:** 19 Rules (project-structure, database, security, etc.)
- **Ergänzen:** Eine Rule `hd-saas-context.mdc` – verweist auf projects/hd_saas für Architektur, Contracts, Pipeline

### Pro Projekt (optional)

- **Projekt-spezifische Rules** im Root: `projects/hd_saas/.cursor/rules/` – Cursor unterstützt das, wenn das Projekt als Root geöffnet wird
- **Alternativ:** Im Root `.cursor/rules/` eine `hd-saas-context.mdc` mit globs `projects/hd_saas/**`, `code/hd_saas_app/**`

---

## 7. Konsolidierung: HD-SaaS als Beispiel

**Aktuell:** 61 MD-Dateien in projects/hd_saas, 14 in code/hd_saas_app/docs

**Empfohlene Aktionen:**

1. **99_archive nutzen:** Wenig referenzierte Docs (doc_audit) → prüfen, ob archivieren
2. **README als Einstieg:** Links zu current_status, next_steps, chat_handover, plan_option_b – wie doc_audit vorschlägt
3. **Contracts bleiben:** interpretations, dimensions, text2kg_spec – zentral, aktiv
4. **Vision/Story/UI:** 4–5 Overview-Docs → ggf. in 1–2 zusammenfassen (z.B. vision_and_flow.md)
5. **code/hd_saas_app/docs:** SQL-Skripte bleiben; MD-Docs auf hd_ingestion_local_dev, cloud_db_push, troubleshooting reduzieren

**Nicht:** Alles auf einmal umbauen. Schrittweise: Neue Docs erst nach Prüfung; alte bei Bedarf archivieren.

---

## 8. Chat-Handover als zentraler Anker

**Beim Chat-Wechsel:**

1. current_status lesen
2. next_steps abgleichen
3. Handover-Block aus chat_handover_hd_saas.md kopieren
4. In neuen Chat einfügen

**Der Block enthält:** Kontext, Status, nächste Schritte, Links – keine Spez. Die Spez liegt in den verlinkten Docs.

**Prinzip:** Ein Copy-Paste bringt 80% Kontext. Die KI liest dann gezielt die verlinkten Docs.

---

## 9. Wartung (lebend)

- **Nach jedem größeren Schritt:** current_status prüfen, last_update setzen
- **Vierteljährlich:** doc_audit (Referenzen, Waisen, Konsolidierung)
- **Bei neuem Projekt:** Diese Struktur von Anfang an anwenden
- **Rules:** Bei Framework-Update prüfen; veraltete Patterns entfernen

---

## 10. Referenzen

- **Cursor Rules:** `.cursor/skills-cursor/create-rule/SKILL.md`
- **Chat Handover:** `projects/_meta/chat_handover_template.md`
- **Doc Audit HD-SaaS:** `projects/hd_saas/02_system_design/doc_audit_hd_saas.md`
- **Master Map:** `projects/_meta/master_map.md`
- **Community:** Lambda Curry Cursor Rules Best Practices, Cursor Rules Framework
