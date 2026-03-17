# Migration-Prompt: _meta + Globale Ebene aufräumen

> Diesen Prompt NACH der Inner-Compass-Migration an Cursor geben.
> Setzt voraus, dass projects/inner_compass/ bereits existiert.

---

## Prompt (kopieren):

```
Ich räume die globale Meta-Ebene auf. Bitte führe folgende Schritte durch:

### 1. _meta/ — Dateien archivieren

Verschiebe diese Dateien nach projects/_meta/99_archive/:
- governance.md
- stakeholders.md
- project_template.md
- naming_conventions.md
- architecture_overview.md
- tech_stack.md
- chat_handover_template.md
- rules.md
- doc_migration_plan.md
- git_commit_blocks_separat.md

Füge in jede verschobene Datei ganz oben ein:
```markdown
> **ARCHIVIERT** (2026-02-16). Inhalt wurde in Cursor Rules (.cursor/rules/) oder doc_and_rules_strategy.md überführt.
```

### 2. _meta/ — Aktualisierte Dateien ersetzen

Ersetze diese Dateien mit den neuen Versionen (liegen in [PFAD]):
- README.md (vereinfacht: nur 3 aktive Dateien referenziert)
- master_map.md (aktualisiert: inner_compass statt hd_saas, vereinfachte Projektliste)
- doc_and_rules_strategy.md (aktualisiert: cursor/+reference/ Pattern, vereinfachte Limits)
- glossary.md (erweitert: Inner Compass Begriffe + Repository-Begriffe)

### 3. Root README.md ersetzen

Ersetze die Root README.md mit der neuen Version (liegt bei den vorbereiteten Dateien).

### 4. .cursor/rules/ aktualisieren

Die Rules sollten bereits durch die Inner-Compass-Migration aktualisiert sein. Prüfe:
- .cursor/rules/ai-projects-global.mdc → Referenziert inner_compass, nicht hd_saas
- .cursor/rules/inner-compass-context.mdc → Existiert und zeigt auf projects/inner_compass/cursor/
- .cursor/rules/hd-saas-context.mdc → Sollte NICHT mehr existieren (gelöscht oder durch inner-compass-context.mdc ersetzt)

### 5. Alte hd-saas Rule entfernen

Falls .cursor/rules/hd-saas-context.mdc noch existiert:
- Lösche sie (der Inhalt ist in inner-compass-context.mdc)

### 6. Validierung

Prüfe:
- projects/_meta/ enthält genau 4 aktive Dateien: README.md, master_map.md, doc_and_rules_strategy.md, glossary.md
- projects/_meta/99_archive/ enthält die archivierten Dateien
- Root README.md referenziert inner_compass, nicht hd_saas
- .cursor/rules/ enthält: ai-projects-global.mdc, inner-compass-context.mdc, spark-serving.mdc
- Keine Datei außerhalb von 99_archive/ referenziert "hd_saas" als aktives Projekt (Code-Pfade ausgenommen)

Zeige mir eine Zusammenfassung.
```

---

## Nach der Meta-Migration

Die Struktur sollte dann so aussehen:

```
ai_projects/
├── .cursor/rules/
│   ├── ai-projects-global.mdc      ← Immer geladen
│   ├── inner-compass-context.mdc   ← Bei Inner Compass Dateien
│   └── spark-serving.mdc           ← Bei Spark Dateien
│
├── projects/
│   ├── _meta/
│   │   ├── README.md               ← Index (3 Dateien)
│   │   ├── master_map.md           ← Projektlandkarte
│   │   ├── doc_and_rules_strategy.md ← Wie Docs organisiert werden
│   │   ├── glossary.md             ← Begriffe
│   │   └── 99_archive/             ← Archivierte Meta-Docs
│   │
│   ├── inner_compass/              ← NEU (ehemals hd_saas)
│   │   ├── cursor/                 ← 7 Lean-Docs
│   │   ├── reference/              ← 4 Kontext-Docs
│   │   ├── system_descriptors/     ← 10 JSON
│   │   ├── 99_archive/             ← Alle alten hd_saas Docs
│   │   └── README.md
│   │
│   ├── trading_bot/                ← Nächster Kandidat für cursor/+reference/
│   ├── rest_data_platform/
│   └── [weitere]/
│
├── infrastructure/                 ← Unverändert
├── code/                           ← Unverändert (Umbenennung separat)
├── scratch/                        ← Unverändert
└── README.md                       ← Aktualisiert
```

## Für andere Projekte (Trading Bot, etc.)

Wenn du ein anderes Projekt aktivierst:
1. cursor/ + reference/ Ordner anlegen
2. Mindestens cursor/README.md + cursor/status.md
3. Rule in .cursor/rules/<projekt>-context.mdc
4. Eintrag in _meta/master_map.md aktualisieren
