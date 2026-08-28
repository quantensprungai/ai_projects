# ESF — Einmal-Setup (Heiko)

## Deploy-Status

**Ja — alles liegt auf VM102** (`~/clawd/workspace-flora/learning/esf/`) und **Hermes pilot** (`~/.hermes/profiles/pilot/learning/esf/`).

Sage kann alle Dateien nutzen. Flora muss die **Reader-Dateien** zusätzlich fürs Lesen auf iPad/PC haben.

---

## Einmal für Flora (15 Min)

### Option A — Obsidian (empfohlen, beste Lesbarkeit)

1. Obsidian auf iPad und PC installieren (kostenlos)
2. Ordner anlegen, z. B. `iCloud/Obsidian/ESF/`
3. Von diesem PC kopieren:

```
infrastructure/docker/workspace-flora/learning/esf/reader/
  FLORA_ESF_WOCHE1.md
  FLORA_ESF_WOCHE2.md

+ optional:
  reader/PHYSIOPRAXIS_ESF_2TEILER.md
  PICO_PICOT_SPIDER.md
  source/Altfragen_Klausur_Natalie.md
  FLORA_START_HIER.md
```

### Option B — PDF auf iPad (ohne Obsidian)

```powershell
cd C:\Users\Admin105\ai_projects
python infrastructure\spark\scripts\esf\build_flora_pdf.py --zip
```

Erzeugt `learning/esf/flora_esf_ipad.zip` (~450 KB) mit 5 PDFs + Start-Anleitung.

**An Flora senden:** AirDrop, iCloud Drive oder Mail → auf iPad in **Dateien** öffnen → ZIP antippen → entpacken.

PDFs liegen auch einzeln unter `learning/esf/reader/pdf/`:
- `00_Start_hier.pdf` — zuerst lesen
- `01_Woche1_...pdf`, `02_Woche2_...pdf`
- `03_PICO_...pdf`, `04_Altfragen_...pdf`

Seitenumbrüche: jedes **Kapitel** und jeder **Übungsblock** beginnt auf neuer Seite; Tabellen bleiben möglichst zusammen.

### 2. Flora Bescheid sagen

Sprachmemo oder Text — Kern:

> „Für ESF gibt's ein Lesepaket. In Obsidian öffnest du `FLORA_START_HIER.md` — da steht alles. Du fängst mit Woche 1 an: ein Stück lesen, Übung drunter machen. Wenn was hängt, frag Sage. Kein Zeitplan, kein Druck.“

### 3. Sage testen (optional)

Flora schreibt: *„Ich starte ESF Woche 1 — worauf soll ich achten?“*

---

## Wenn Material am Repo geändert wird

```powershell
cd C:\Users\Admin105\ai_projects
python infrastructure\spark\scripts\esf\ingest_esf_downloads.py  # neue PDFs aus Downloads
python infrastructure\spark\scripts\esf\esf_local_pipeline.py modules --only-reader --force
python infrastructure\spark\scripts\esf\esf_local_pipeline.py exercises --only-reader --force
python infrastructure\spark\scripts\esf\build_flora_reader.py
python infrastructure\spark\scripts\esf\build_flora_pdf.py --zip
python infrastructure\docker\deploy_flora_esf.py               # → VM102/Sage
```

Dann `reader/*.md` erneut in Floras Obsidian-Ordner kopieren — oder PDFs neu bauen (`build_flora_pdf.py --zip`).

---

## Datei-Landkarte

| Datei | Wer | Wofür |
|-------|-----|-------|
| `FLORA_START_HIER.md` | Flora | **Hauptanleitung** |
| `reader/FLORA_ESF_WOCHE1.md` | Flora | Lesen + Üben Woche 1 |
| `reader/FLORA_ESF_WOCHE2.md` | Flora | Lesen + Üben Woche 2 |
| `reader/PHYSIOPRAXIS_ESF_2TEILER.md` | Flora | PICOT + p-Wert (2 Artikel, ein RCT) |
| `PICO_PICOT_SPIDER.md` | Flora | PICO/PICOT Prüfung |
| `source/Altfragen_Klausur_Natalie.md` | Flora | Klausurtypen |
| `PRUEFUNGS_CANON.md` | du / Sage | Priorisierung |
| `modules/` (27) | Nachschlag | nicht alles lesen |
