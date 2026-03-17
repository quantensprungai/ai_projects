# kern/ — Single Source of Truth

> ⚠️ **ACHTUNG: Read-Only Bereich**
> Diese Dokumente werden NICHT im Repo editiert.
> Änderungen entstehen ausschließlich im KERN-Prozess (extern) und werden als neue Version eingecheckt.

---

## Was liegt hier?

| Datei | Inhalt | Version |
|---|---|---|
| `IC_Fundament_v06.md` | Konzeptionelles Fundament: Systeme, Taxonomie, Analyse-Pipeline, Kanal-Dualität, HD↔EG-Brücke | v06 |
| `IC_Leitdokument_v5.1.md` | Steuerungsdokument: 40 Entscheidungen (E-01–E-40), OEs, Phasen, Domänen, UX-Regeln | v5.1 |


---

## Regeln für die Cursor-KI

### 1. Leserecht — ja. Schreibrecht — nein.
- Du darfst diese Dateien **lesen und referenzieren**.
- Du darfst sie **NICHT editieren, überschreiben oder löschen**.
- Wenn du einen Fehler oder Widerspruch findest, **dokumentiere ihn** in `bridge/IC_BRIDGE.md` als neuen Patch-Vorschlag (P-XX) — ändere NICHT die Quelldatei.

### 2. Vorrang-Regel (Konflikthierarchie)
Bei Widersprüchen zwischen Dokumenten gilt:

```
kern/IC_Fundament     >  kern/IC_Leitdokument  >  bridge/  >  cursor/  >  reference/
```

- `kern/` schlägt immer alles andere.
- `IC_Fundament` schlägt `IC_Leitdokument` (Fundament = WARUM, Leitdokument = WIE).
- Wenn `cursor/`-Dateien (architecture.md, contracts.md etc.) etwas anderes sagen als `kern/`, gilt `kern/`.

### 3. Referenzierung
Wenn du in `cursor/`-Dateien auf KERN-Inhalte verweist, nutze dieses Format:

```
<!-- KERN-REF: IC_Fundament_v06 § Abschnitt X.Y -->
<!-- KERN-REF: IC_Leitdokument_v5.1 § E-31 -->
```

So bleibt nachvollziehbar, woher eine technische Entscheidung kommt.

### 4. Versions-Awareness
- Prüfe vor jedem größeren Task: Stimmt die Version in diesem Ordner noch mit der BRIDGE überein?
- Die BRIDGE (`bridge/IC_BRIDGE_v1.0.md`) listet die erwarteten Versionen.
- Wenn eine neue Version eingecheckt wird, erstelle einen Diff-Report in `bridge/`.

---

## Regeln für menschliche Contributors

1. **Keine direkten Edits im Repo.** Änderungen am Fundament oder Leitdokument entstehen im externen KERN-Prozess (Autor).
2. **Neue Versionen** werden als Ganzes eingecheckt (z.B. `IC_Fundament_v07.md`), die alte Version wird nach `99_archive/` verschoben.
3. **Commit-Message-Format** für KERN-Updates:

```
kern: update IC_Fundament v06 → v07

- Änderungen: [kurze Liste]
- Auslöser: [OE-XX / Patch P-XX / externe Entscheidung]
- BRIDGE-Update erforderlich: ja/nein
```

4. Nach jedem KERN-Update: Prüfe ob `bridge/IC_BRIDGE.md` aktualisiert werden muss.

---

## Warum dieser Ordner existiert

Die Cursor-KI braucht Zugriff auf die konzeptionellen Grundlagen, um:
- Konsistenz-, Logik- und Vollständigkeits-Checks durchzuführen (Briefing §3)
- Patches (P-01 bis P-25) korrekt gegen KERN-Entscheidungen zu validieren
- Technische Entscheidungen in `cursor/` auf ihre fachliche Grundlage zurückzuführen

Ohne `kern/` im Repo wäre die BRIDGE ein Verweis ins Leere.


