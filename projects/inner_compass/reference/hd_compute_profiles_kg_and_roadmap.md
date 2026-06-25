# Human Design — Compute-Profile, KG-Auswirkungen und Gesamt-Roadmap

> Festhalten der Diskussion: **tropical (Standard)** vs. **sidereal** vs. **EarthStar Human Design** (Hybrid: Design tropisch / Persönlichkeit sidereal), Einordnung in **Inner Compass** (App, KG, Literatur).

---

## 1. Kurzantworten


| Frage                                       | Antwort                                                                                                                                                                                                          |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ändert sich der **KG** (Ontologie)?         | **Nein** in dem Sinne: `hd.gate.`*, `hd.channel.*`, `hd.type.*` bleiben **dieselben Canonical IDs**. Literatur und Regeln beziehen sich weiterhin auf dieselben Bausteine.                                       |
| Ändert sich das **Nutzerergebnis**?         | **Ja:** Welche Knoten für eine Person **aktiviert** sind (und ggf. Typ/Profil/Kreuz), hängt von den **berechneten Gates** ab — die können zwischen Modi stark divergieren.                                       |
| Ist das nur eine **andere Berechnung**?     | **Größtenteils ja:** Gleiche Pipeline „ecliptic longitude → Rave-I-Ging-Kreis → Gate/Zeile/Farbe/Ton/Base“, andere **Eingabelangen** oder **getrennte Läufe** beim Hybrid.                                       |
| **Swiss Ephemeris** = offizieller HD-Stack? | Swiss ist die **Astronomie-Bibliothek**. „Offiziell“ im Jovian-Sinn ist v. a. **tropical + etablierte Gate-Zuordnung**. Sidereal ist **andere Konvention**, kein anderes `system_id` — siehe `contracts.md` §13. |


---

## 2. Produktname: **EarthStar Human Design**

**Hybrid** im Sinne von „Design-Kristall / Erde = tropical, Persönlichkeits-Kristall / Kosmos = sidereal“ heißt in der **Inner-Compass-Oberfläche und Doku** → **EarthStar Human Design**.


| Ebene                                        | Wert                                                        |
| -------------------------------------------- | ----------------------------------------------------------- |
| Technisch (`compute_profile.hd.zodiac_mode`) | `hybrid_design_tropical_personality_sidereal` (unverändert) |
| Menschlich / Marketing-kompatibel            | **EarthStar Human Design**                                  |
| Kurzlink / Tooltip                           | „Erde (tropical) · Sterne (sidereal)“ o. ä.                 |


**Abgrenzung:** Kein Anspruch auf „offizielles“ Jovian-/IHDS-Branding; EarthStar ist die **IC-benannte Konvention** für genau diesen Hybrid. Andere Apps nennen ähnliche Ideen anders — **Persistenz und API** nutzen immer den Enum-Wert, nicht den Marketingstring allein.

---

## 3. Contracts — Einordnung (authoritative: `cursor/contracts.md` §13)

- `**system_id`:** immer `**hd`**.
- **Unterscheidung der Modi:** Feld `**compute_profile.hd`** (JSON), mit mindestens `zodiac_mode`, optional `sidereal.ayanamsha`, `backend.`*.
- **Keine** neuen Enums in §4 nur für Sidereal — das vermeidet Duplikat-Ontologien und duplizierte `hd.gate.`*-Knoten.
- **Anzeigenamen** pro Modus (inkl. EarthStar) → `**contracts.md` §13** Tabelle.

---

## 4. Schichten K1–K4: Was Literatur (K3+K4) berührt — und was nicht


| Schicht | Inhalt                                       | Wirkung von Literatur-Download / PDF-Pipeline                                                                                                                                                                                            |
| ------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **K1**  | Numerisches: Grad→Gate, Ephemeris, Zeitzonen | **Unabhängig** von PDF-Literatur; kommt aus **Kit/Engine**. Neue Literatur **ändert K1 nicht**, außer ihr **beschließt bewusst**, eine Quelle sei „wahrer“ als das Kit und **revised** Struktur-Samen (Governance-Entscheidung, selten). |
| **K2**  | Struktur: Kanäle, Zentren, Typlogik im Code  | Wie K1: aus **open-source Kit + Seeds**. Literatur kann **K3-Regeln** liefern („wenn Gate X dann …“), aber **ersetzt** nicht automatisch K2-Tabellen.                                                                                    |
| **K3**  | Gewichtungen, Wenn-Dann aus Lehrtexten       | **Hier** landet extrahierte Literatur: `sys_kg_edges`, `sys_interactions`, Bedingungen.                                                                                                                                                  |
| **K4**  | Bedeutungen, Narrative                       | `**sys_interpretations`**, Embeddings, Handbuchtexte.                                                                                                                                                                                    |


**Antwort auf die typische Arbeitsunterbrechung:** Wenn du **jetzt** Literatur für **K3+K4** ziehst, sind **K1+K2** dadurch **nicht automatisch „falsch“ oder veraltet**. Sie können **unverändert parallel** bleiben. Konflikte (Literatur vs. Kit) werden beim Review sichtbar — dann **Explizit entscheiden**, nicht still überschreiben.

---

## 5. Swiss Ephemeris als „Übersetzungsadapter“

Mentalmodell:

```
Swiss Ephemeris (Flags: tropical | sidereal + Ayanamsha)
        → ecliptic longitude pro Planet, JD
        → bestehende HD-Logik (IGING_offset, 64 Gates, …)
        → Aktivierungen / Channels / Typ
```

- **Zwei weitere Versionen** (full sidereal; hybrid) sind **kein zweites Lexikon**, sondern **andere Eingaben** in dieselbe (oder explizit gemergte) Mechanik.
- **Hybrid** braucht **zwei Laufkonventionen** und **Merge-Regeln** im Engine-Layer — siehe Roadmap §7.

---

## 6. Auswirkungen auf die **App**


| Bereich               | Auswirkung                                                                                                                       |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Chart-Speicherung** | Pro gespeichertem Chart: `**compute_profile`** mitschreiben; bei mehreren Modi pro Nutzer: mehrere Snapshots oder Versionierung. |
| **UI**                | Labels gemäß `**contracts.md` §13** (Klassisches HD, Sidereal HD, **EarthStar Human Design**).                                   |
| **Vergleiche**        | Composite, Partner-Charts, Zeit-Muster: **nur gleicher Modus**.                                                                  |
| **Evidenz**           | Standard-tropical → A/B; sidereal / EarthStar → oft **C/D** mit kurzem Erklärbanner (eigene IC-Policy).                          |


### 6.1 UI — Moduswahl und Umschalten (Phasen)

**Ziel:** Einheitliche Rechenkonvention pro Ansicht, keine stillen Wechsel; Nutzer:innen verstehen, *welches* HD sie sehen.

**Stufe 1 (empfohlen zuerst — für alle):**

- **Eine zentrale Rechen-Präferenz** pro Nutzer/Kontext (z. B. Einstellungen „Standard-HD-Modus“), Default:** `tropical_ra_standard`**.
- **Dropdown oder Segment-Control** dort, wo der Modus das Ergebnis ändert: Chart-Hauptansicht, relevante **Text-/Interpretations**-Widgets (Landkarte, Handbuch-Snippets, die aus Chart-Knoten gespeist werden). Gleiche Auswahl **logisch gekoppelt**: wer den Modus am Chart ändert, soll dieselbe Session-Ansicht für zugehörige Texte sehen (oder explizit „Texte folgen Chart-Modus“ als Toggle).
- **Sidereal:** wenn angeboten, **Ayanamsha** wählen oder „Empfohlen (IC-Default)“ mit Link zu Kurzerklärung.
- **EarthStar:** kurzer **Consent-/Info-Hinweis** beim ersten Mal (experimentelle Konvention, nicht Jovian-Standard).

**Stufe 2 (später — „Profis“ / Power-User):**

- **Side-by-Side:** bis zu **drei** Spalten oder Tabs — klassisch tropical · sidereal · EarthStar — **gleiche Person, gleiche Geburtseingabe**, nur `compute_profile` unterschiedlich.
- **Warum später:** Dreier-Vergleich ist kognitiv dicht (unterschiedlicher Typ/Profil möglich); für Ersteinsteiger eher **überfordert**. Stufe‑2 kann hinter „Erweitert“ / „Vergleichsmodus“ / Feature-Flag oder Rolle **„Berater:in“** liegen.
- **Performance:** Dreifach-Rechnung on-demand oder Cache der drei Ergebnisse nach erster Anforderung — Produktentscheidung (Speicher vs. CPU).

**Empfehlung:** Stufe 1 shippen, Stufe 2 sobald Stufe 1 stabil und Support-Texte für EarthStar/Sidereal stehen.

### 6.2 Bodygraph / Visualisierung

Der HD-Microservice liefert `**/bodygraph`** (Bitmap/SVG) aus derselben Engine wie `/calculate`. Jede neue Modus-Implementierung muss **dieselbe Modus-Logik** in den Renderer-Pfad füttern, sonst zeigt das Bild einen anderen Modus als die Zahlen — das ist eine **Checkliste bei Engine-Arbeit**, nicht ein separates Produkt.

---

## 7. Roadmap (nicht nur MVP)

### Phase A — Governance & Datenmodell (kurz)

- `compute_profile` in API + gespeichertem Chart-JSON **formal** abbilden (Align mit `contracts.md` §13).
- Produktregel: **Default** = `tropical_ra_standard` für Veröffentlichung/Vergleiche.

### Phase B — Engine-Erweiterungen (technisch)

- **Sidereal:** `pyswisseph` sidereal mode + **gewählter** Ayanamsha (Dokumentationspflicht); alle `calc_ut`-Pfade im vendored Pfad anpassen **oder** zentral parametrisieren.
- **Design-Datum:** Klar festlegen, ob bei rein sidereal auch die **Sonne−88°**-Suche sidereal sein soll (Konsequenz für Design-Zeitpunkt).
- **Hybrid:** Implementierung nur nach **fester Spezifikation** (welche Seite welcher Zodiac, welche JD für Merge); Tests gegen Referenzfälle.

### Phase C — KG & Pipeline

- Keine Duplikat-Nodes für Modi; ggf. **Tags** auf Interpretationsebene („gilt für Modus X“) nur wenn nötig — Standard ist: **gleiche Knoten**, andere Chart-Aktivierung.
- Optional: **Cross-Link**-Edges „entspricht ungefähr“ zwischen Modi → **nur** Evidenz D, Review-Pflicht.

### Phase D — Literatur & K3/K4 (parallel zu dir)

- PDF → Chunks → Extraktion gemäß `pipeline.md`; Ausrichtung auf bestehende `hd.gate.`*.
- Review-Prozess bei Widerspruch Literatur vs. K2.

### Phase E — Nutzerfunktionen (UI)

- Stufe 1: **Globale/sessionweise Moduswahl** + Dropdown an Chart + konsistente Text-Widgets; Default tropical.
- Stufe 2: **Side-by-Side** (3 Modi) unter „Erweitert“ / Profi-Modus; optional Cache der drei Berechnungen.
- Export mit `**compute_profile`**-Metadaten (immer).

---

## 8. Offene technische Punkte (Checkliste)

1. **Ayanamsha-Default** für IC-Sidereal (wenn nicht nutzerwählbar): Policy-Entscheidung (häufig Lahiri in „vedisch“-nahen Kontexten; Cosmic-HD-Web teils anders — dokumentieren).
2. **Hybrid:** Rechtliche/Community-Erwartung: als **experimentell** kennzeichnen.
3. **Ephemeris-Version:** Schweizer Ephemeris-Datei-Version bei Reproduzierbarkeit festhalten (`backend` in `compute_profile`).

---

## 9. Verweise

- **Payload-Konvention:** `cursor/contracts.md` §13  
- **Engine vs KG:** `cursor/engines.md` §1  
- **K-Kategorien:** `cursor/engines.md` §2  
- **Code-Pfad:** `code/inner_compass_app/services/hd/` — `vendored/humandesign_api/.../core.py` (`calc_ut`, Design-Datum)

