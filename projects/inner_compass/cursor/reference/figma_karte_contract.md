---
title: Figma × KARTE — Arbeitsvertrag und Dateistruktur
status: aktiv
in_scope:
  - Rollenteilung Figma vs. Engine/Code
  - Figma-Dateistruktur und Namenskonvention
  - Geometrie-Export-Format für den Bodygraph
  - Quota-Regeln der Figma-Anbindung
out_of_scope:
  - Chart-Berechnung (siehe reference/hd_state_contract.md)
  - Content-Admission (siehe cursor/contracts.md)
last_update: 2026-08-26
---

# Figma × KARTE

## 1. Rollenteilung

> Figma entwirft die Wahrnehmung der Zustände. Die Engine berechnet die Zustände.
> Der Packer entscheidet, welcher Ausschnitt sichtbar wird.

**Figma besitzt:** visuelle Sprache, Layout und Informationshierarchie,
Bodygraph-Geometrie, Komponenten samt Zustandsvarianten, Interaktionsprototypen,
responsives Verhalten.

**Code und Verträge besitzen:** Chart-State, Gate-/Kanal-/Center-Berechnung,
planetare Aktivierungen, Line-Fixing, `defined | undefined`,
`conscious | unconscious`, retrograde, Facet-Admission, Content-Provenienz,
konkrete Chartdaten.

Figma darf Koordinatenquelle sein, aber **keine zweite State-Engine**.

## 2. Quota — drei Konten, nicht eines

Drei Budgets, die **nichts miteinander zu tun haben**:

| Konto | Was zählt | Was nicht zählt |
|-------|-----------|-----------------|
| **1. Figma Starter Reads** | `get_design_context`, `get_metadata`, `get_variable_defs`, `get_screenshot`, `whoami` — **20/Monat** | `use_figma` (Writes), `generate_figma_design`. Contract- und Token-Seiten schreiben **verbrauchen keine Reads**. |
| **2. Langdock Overlay-Tokens** | Overlay-LLM (`gpt-5-mini`) beim Chart-Lesen | Figma-Arbeit berührt sie nicht. Overlay-Länge ist **Admission**, nicht Mini-Quota (siehe Overlay-Vertrag §5.0). |
| **3. Cursor-Kontext** | Chat-Fenster dieser Session | Irrelevant für Overlay-Länge und für Figma-Reads. |

Daraus folgt die Reihenfolge:

1. Laufende KARTE per `generate_figma_design` in die Datei drücken — kostet keine
   Lesequote und liefert ein pixelgenaues Referenz-Frame.
2. In Figma **daneben** gestalten (Menschenarbeit oder `use_figma`).
   Live-Datei: https://www.figma.com/design/6KCXRVzu39tqEjpr66hGwc
3. **Ein** gebündelter Lesezugriff, wenn die Richtung steht — nicht pro Iteration.
   Gemeint: erst gestalten, dann **einmal** `get_design_context` auf dem
   freigegebenen Frame (Koordinaten/Komponenten), nicht zwanzig Zwischenstände.
4. Geometrie am Ende **einmal** als Tabelle exportieren (§5), nicht laufend.

Nicht: pro Designfrage ein `get_design_context`. Zwanzig Fragen sind der Monat.

## 2a. Capture-Frames (Dump = Referenz)

Zwei Top-Level-Frames auf der Capture-Seite, beide ursprünglich `"Human Design"`:

| Node | Höhe | Layer | Urteil |
|------|------|-------|--------|
| `6:2` | 645 | **oben** in Ebenen | **Referenz aktuell** (Capture 2) |
| `2:2` | 1080 | unten in Ebenen | **Referenz älter** (Capture 1) |

Beide sitzen bei y=0. Der Dump bleibt Referenz. Gestalt **daneben**, HTML-Layer
**nicht** aufräumen, Captures **nicht** löschen.

Seite in Figma: `06 — Referenz Captures` (`0:1`, umbenannt aus Page 1).
Seiten `00 — Readme & Contract` (`10:2`) und `01 — Design Tokens` (`11:2`)
sind in diesem Slice angelegt. Gestalt **daneben** den Captures, nicht im Dump.

## 3. Dateistruktur

**Starter = 3 Seiten.** `figma.createPage()` wirft darüber.
Geplante 00–07 sind Abschnitte, keine Figma-Pages. Live:

```
00 — Readme & Contract           Designregeln (§4)
01 — Tokens & Geometry           Tokens links; Bodygraph Geometry v0 rechts
06 — Referenz Captures           HTML-Dump; nicht putzen; Gestalt daneben
```

Abschnitte 02 Components, 04 Screens, 05 Szenarien, 07 Handoff = Plan,
bis Professional oder bis sie als Frames **auf 01** daneben liegen.

Geometry-Frame (2026-08-19): `Bodygraph Geometry v0` auf Seite 01, x=1600.
9 Zentren (HD-Formen) + 64 Tore + 36 Kanäle, je `visible` / `label` / `hit_area`.
IDs = `hd.center.*` · `hd.gate.N` · `hd.channel.A_B` (Katalog aus
`HD_CHANNEL_CENTERS`). Zentren-Layout skaliert aus `hd-bodygraph.tsx`
(`CENTER_POS`); Gate-Offsets = erste Passung entlang der Kanten, **kein**
Jovian-/Anbieter-Trace. Feinschliff visuell gegen Capture 6:2, ohne Read-Tools.

`06` war im Entwurf „Developer Handoff“. Captures brauchen eine eigene Seite
(sonst Namenskollision). Handoff bleibt **Plan**.

## 3a. Palette (Tokens)

Hex als COLOR-Variablen in `01 — Design Tokens` (`KARTE / Color`):

| Token | Hex | Rolle |
|-------|-----|-------|
| Canvas | `#E9EFEC` | Seitenhintergrund |
| Surface | `#F8FBF8` | Karten / Paneele |
| Ink | `#14242B` | Text **und** Persönlichkeit (klassisch Schwarz, als Shade) |
| Personality | Ink (nicht mehr `#315CCB`) | Bewusst — Rails + Kanäle. Dark Mode: invertiertes Ink |
| Design | `#C75B45` | Unbewusst — Rails + Kanäle (Vermilion) |
| Defined | `#168574` | Zentrum definiert (Token; Jovian-Füllung ist Konvention) |
| Undefined | `#82918E` | Zentrum undefined |
| Signal | `#C9A24A` | Hover/Selection (Gold, Tint von Kopf/G) |

Personality und Design brauchen **zusätzlich** Nicht-Farbe (Muster und/oder Label).
Farbe allein reicht für a11y nicht (zwei Rot/Blau-Kanäle, Rails links/rechts).

## 3b. Rails-Komposition (Layout-Pilot, 2026-08-19)

Rails gehören **neben** den Graph, nicht in die Overlay-Zusammenschau.
Frame `KARTE / Rails+Graph` auf Seite 01: Design links · Graph · Persönlichkeit rechts.

Spiegel (nicht 64keys-Kopie; gleiche Idee „Zahlen am Körper“):

```
Design:     Name  ▲▼  Tor.Linie  R  | Graph |
Persönlichkeit:                 | Graph |  ▲▼  Tor.Linie  R  Glyphe
```

Color/Tone ist eine **eigene Spalte**, Default **aus**. Toggle „Color/Tone an Rails“ blendet `C/T` ein, ohne dass ▲/▼/R/Tor.Linie verrutschen (feste Slots). Mini-L/R nur an den vier Kopf-Pfeilen.

- **Innen** (am Graph): `Tor.Linie` — das ist die Aktivierung.
- **Außen ungleich:** Design = Name (lesbar). Persönlichkeit = Glyphe (Marke). Nicht beides auf beiden Seiten.
- **▲ / ▼ / Stern** und **R** sitzen am Wert, nicht an der Glyphe. `neither` = leerer Slot, nicht ein drittes Symbol.
- **Color/Tone** = optionale Spalte (Toggle, Default aus). Hexagramm-Tiefe dieser Aktivierung, nicht die Variable-Bedeutung. Mini-L/R nur an den vier Kopf-Pfeilen.
- Pilotzahlen = Dachau, **Ra-direct** (Saturn 18.3 `neither`, auch wenn 64keys ▼ malt).
- Code (`hd-activation-rails.tsx`) ist **gespiegelt**: innen `Tor.Linie`, außen Glyphe; Name nur Inspector/`aria-label`. Figma ist der Entwurf.
- Rails in Figma = **Spaltenlayout** (innen Zahl, außen Glyphe, Zeilenabstand).
  Schrift- und Symbolgröße sind Zielbild, kein Export-Asset. Makerkit setzt
  Typo in CSS; die 13 Zeilen werden nicht als 26 Textlayer eingelesen.
- **R** und **Stern (Line-Juxtaposition / `both`)** sind Chart-State, keine Geometrie.
  Engine liefert `retrograde`. Stern auf der Zeile des Occupying (Dachau: Pluto 57.5),
  weil Fixing v2 beide Pole kennt (Pluto ▲ direct + Mond 10.1 ▼ harmonic) — nicht weil
  ein Planet beides ist. Rails v1 zeigt pro Planet nur den direkten Pol; der Stern ist
  die Zeilen-Variante, sobald `fixingSources` beide Pole tragen.
- Glyph vs. Name: **Design links Name, Persönlichkeit rechts Glyphe.** Zahlen `Tor.Linie` bleiben auf beiden Seiten — die sind IDs, keine Wörter.

## 3c. Was du in Figma schiebst vs. was die App malt

Die benannten Layer (`hd.gate.57 / visible` …) sind die **Koordinatenquelle**.
Nach dem Schieben: **ein** Export als Tabelle → `hd-bodygraph-geometry.ts`.
Die App (Makerkit/React-SVG) legt **State darüber**: defined-Fill, Kanal an/aus,
Persönlichkeit/Design an den Rails, ▲▼/R/Stern, Selection.

Du malst nicht „für immer“ in Figma. Figma = Zielbild + Geometrie. Runtime = Code.
Wenn du Farben/Striche in Figma änderst: Tokens und Varianten mitziehen, nicht zu
einem flachen Bild zusammenschmelzen — IDs müssen bleiben.

**Texte:**

| Auf der Fläche | Sprache | Woher |
|----------------|---------|--------|
| Tornummern 1–64 | keine | IDs |
| `29.5` auf der Schiene | keine | Chart-State |
| Glyphen ☉ ⊕ … | keine | `HD_PLANET_GLYPH` |
| „Kopf“, „Sonne“, „Design“ | ja | App-Locale (`next-intl`), nicht Figma, **nicht** `sys_term_mapping` |
| Atom-Essays im Inspector | ja | `sys_synthesis_wordings` Zeile je Sprache |
| Line-C Pol-Absätze (I’Ching) | en (Buch) | `sys_source_chunks` reconstructed, nicht Synth |

Figma-Labels auf dem Geometry-Frame sind Gerüst. Die App übersetzt; sie liest
keine deutschen Layer-Namen als Copy.

## 3d. Rave-Mandala (Rad) ≠ IC-Mandala (Domänen)

Zwei verschiedene Objekte. HD-KARTE bleibt Bodygraph + Rails
(`decisions.md` 2026-08-14). **IC-Mandala** = 12 Lebensdomänen, anderes Objekt.

**Rave-Mandala** (64 Hexagramme um den Graph): später erlaubt als zweite Lesart
oder Ring um denselben Chart. Keine neue Engine. Gate+Line (+ Color/Tone/Base,
die die Engine schon liefert) reichen, um einen Planeten auf dem Rad zu setzen
(`svgRaveMandalaGateOrder` im Kit). Längengrad wäre feiner, ist aber für die
Hexagramm-Position nicht Voraussetzung. **Nicht in diesem Slice bauen.**

## 4. Seite 00 — Regeln, die im Design nicht kippen dürfen

- `defined | undefined` ist der Kern-State. **`open` ist kein dritter Zustand**
  (Code nennt es `undefinedCenters`, die UI sagt „offen" nur als Wort).
- Mechanik steht vor Interpretation.
- Planeten sind Aktivierungsquellen, kein 14. Elementtyp.
- `juxtaposition` ist ein **Aggregat** aus Exaltation + Detriment, kein eigener
  Fixierungsmechanismus. Im Chart erscheint es als „both".
- Gift und Shadow sind zwei Frequenzen, keine Existenzbedingungen — und nicht
  automatisch an definiert/undefiniert gekoppelt.
- Exaltation/Detriment werden nicht in „gut/schlecht" übersetzt.
- Kein Text erzeugt Chart-Wahrheit.
- Keine UI-Kopie von 64keys, Gene Keys oder anderen Anbietern.
- PHS-Zahlen tragen **keine achsenlose** Bedeutung: dieselbe Colorzahl heißt je
  Pfeil etwas anderes (siehe `apps/web/lib/hd/hd-phs.ts`, `HD_PHS_AXES`).

### Formen vs. Farben

**Formen sind Grammatik**, keine Dekoration:

| Form | Zentren | Rolle im System |
|------|---------|-----------------|
| Dreieck oben/unten | Kopf, Ajna | Druck / mentale Awareness |
| Quadrat | Kehle, Sakral, Wurzel | Manifestation bzw. Motoren |
| Raute | G | Identität, kein Motor |
| Dreieck seitlich | Milz, Solar, Herz | Awareness-Motoren / Will |

Ein Kreis statt Raute wäre kein Bodygraph mehr.

**Farben sind Konvention**, zwei getrennte Systeme:

1. Jovian-Füllung wenn definiert (Kopf gelb, Ajna grün, Kehle braun, Motoren rot …) —
   schön und wiedererkennbar, aber **nicht** Chart-State. Dieselbe Information
   steckt schon in der Form.
2. Unsere Tokens: `Defined` / `Undefined` = State; `Personality` / `Design` =
   Aktivierungsseite (**Rails, Kanalhälften**), nicht auf das Zentrum gemalt.
   Ein Zentrum kann von gemischten Kanälen definiert sein — deshalb keine
   Streifenfüllung.

Freier für Schönheit: die konkreten Hues, Strichstärke, ob definiert = Füllung
oder nur Kontur, ob Kanäle geteilt (Design|Persönlichkeit) eingefärbt werden.
Nicht frei: Forminventar, `open` als dritte Form, Gift/Shadow als Center-Fill.

### 4b. Visuelle Regeln der laufenden KARTE (nicht kippen)

Geometrie (Koordinaten, Größen, Bézier) darf neu gezeichnet werden.
Diese Wahrnehmungsregeln bleiben, auch wenn Centers größer und Kanäle neu sind:

- Personality-Kanäle = Ink (`currentColor` / `#14242B`), nicht Blau.
  Design-Kanäle = `#C75B45` (Dark `#E08A7A`).
- Jovian-Füllung der definierten Zentren, **hell genug für einheitliche dunkle
  Schrift** (`#14242B`) auf jedem Zentrum: Kopf/G `#E0B84E`, Ajna `#6FB8A6`,
  Kehle/Milz/Solar/Wurzel `#C4A07C`, Sakral `#E85C4A`, Herz `#E07A72`.
  Undefined = opakes `fill-background`, damit Tubes unter der Form verschwinden.
- Definiert ohne Selection = **kein** Stroke. Selection = hellerer Tint derselben
  Hue, kein Gold-/Braunring.
- Tore: **keine Scheibe**. Definiert = Ink `#14242B`. Undefined =
  `fill-foreground` (Dark-Theme sichtbar). Aktiv = schwerere Ziffer; idle =
  Gewicht 500 und Opacity ~0.55. Hover/Selection = größer (14.5 → 16.5 → 19).
  Gate-Chips (hue-gematcht und Papier) ausprobiert und verworfen.
- Variable-Pfeile: dicker Chevron mit runden Kappen (kein gefülltes Spitzdreieck).
- Leere Tube `--hd-tube` kühles Schiefer `#5F6B72` (Dark `#6A7571`) — bewusst
  andere Helligkeit als Design-Orange und als Personality-Ink, sonst verschwimmen
  leere und volle Kanäle. Füllung Integration 10–20–34–57 `7.8` / betont `10.5`;
  alle anderen `9.4` / `12.4`. Beide Seiten aktiv = noch einen Tick dicker
  (`10.2`/`12` bzw. betont `13`/`15`), weil die zwei parallelen Hälften sonst
  dünner wirken als ein einseitiger Strich.
- Kanal-Ende = **Gate-Kreismitte**. Zentren liegen über den Tubes.
- `absent` = leere Tube; `partial` / hanging = aktives **hängendes** Tor bis
  zur Mitte *dieses* Pfads; `complete` = volle Tube. Beide Seiten = zwei
  parallele Strokes; die **Gesamtbreite** ist einen Tick dicker als einseitig.
- Integration 10–20–34–57: **sechs getrennte Pfade**, die sich kreuzen dürfen.
  Nicht zu einem Stern verschmelzen. Hanging an 10–57 ändert 20–57 nicht.
  Ein Tor, das schon in einem vollständigen Kanal sitzt, erzeugt keine
  Hanging-Stubs auf den anderen Integrationskanälen.
- Herz: scalenes Dreieck um Tore 21/26/40, nicht die Plugin-BBox.

- Variable: vier Marker **neben dem Kopf**, Abstand zur Form. Richtung = Chevron,
  Color große Ziffer, Tone Tiefzahl (kein Punkt). Design links (Pfeil dann Zahl,
  Hue `--hd-design`), Persönlichkeit rechts (Zahl dann Pfeil, Ink). Klick öffnet
  Register Körper.
Geometrie-Stand vor dem Neuzeichnen: `cursor/reference/geometry-backup-2026-08-24/`.

**Stand 2026-08-26:** Graph + Rails folgen §4b. Variable: vier Marker neben dem Kopf — Chevron + Color mit Tone als Tiefzahl. Rails: Color/Tone als zwei Mini-Ziffern je Planetenzeile. Design links, Persönlichkeit rechts. Klick öffnet Register Körper bzw. Tore.

## 5. Bodygraph-Geometrie — Exportformat

Kein großes SVG. Ein großes SVG kennt die Geometrie, aber nicht unsere Semantik.
Export ist eine normalisierte Tabelle mit stabilen IDs:

```json
{
  "canvas": { "width": 1200, "height": 820 },
  "centers": {
    "spleen": { "x": 420, "y": 350, "width": 120, "height": 150, "shape": "triangle_right" }
  },
  "gates": {
    "57": { "anchor": [365, 350], "side": "right", "center": "spleen" }
  },
  "channels": {
    "10_57": { "path": "M …", "hit_path": "M …" }
  },
  "hubs": {
    "integration": [246, 665.5],
    "26_44": [320, 720]
  }
}
```

Regeln:

- Jedes interaktive Objekt *darf* drei Ebenen haben: `visible`, `label`,
  `hit_area`. **Hitareas sind im Code nicht Pflicht.** React zeichnet die
  Trefferfläche als transparenten Stroke (18px) auf `path`. Eine Figma-Ebene
  namens `hitareas` wird nicht gelesen. Optional: `hd.channel.10_57 / hit_area`
  als dickere Kopie derselben Bézier — sonst `hit_path = path`.
- **Kurven sind erlaubt** wo gerade Linien sich kreuzen (Integration
  10–20–34–57; 26–44 über das G). `path` und `hit_path` = dieselbe Bézier,
  Hit nur dicker. Ein Kanal = ein Pfad; am gemeinsamen Tor treffen Endpunkte
  im Gate-Kreis. Klick = nächster Pfad, nicht das oberste Rechteck.
  Makerkit legt kein Figma-SVG darüber — React zeichnet Tube + State aus der Tabelle.
- Gate-Anker liegen an der Zentrumskante, mit `side` für die Labelrichtung.
- **Kanal-Enden** treffen den **Gate-Kreis**, nicht die große Zentrumskante.
  Pfad-Ende = Kreismitte; der Kreis liegt visuell darüber, die Tube wirkt
  am Rand. Eine Geometrie-Datei malt den vollen Pfad einmal — nicht halb,
  nicht längs geteilt. State kommt in React:
  `absent` = leere Tube; `partial` / hanging = Füllung vom aktiven Tor bis
  zur Pfadmitte *dieses* Kanals; `complete` = ganze Tube; Design vs.
  Persönlichkeit = Farbe; beide Seiten = Längsteilung derselben Kurve
  (zwei versetzte Strokes oder Maske), kein zweiter Figma-Pfad.
  Integration 10–20–34–57: sechs Pfade, die sich kreuzen dürfen. Nicht
  verschmelzen. Hanging an 10–57 ändert 20–57 nicht.
- Kanal-IDs in **Katalogordnung** (`hd.channel.10_57`), nicht in Engine-Reihenfolge —
  die Remap-Funktion ist `remapEngineChannelId`.
- **Linien haben keine Geometrie.** Die 384 `hd.line.<gate>_<line>` sind
  Inspector-Inhalt, keine Objekte im Graphen. Ein Figma-Layer `hd.line.57_5`
  würde Geometrie erfinden.
- Zielort im Repo: `apps/web/lib/hd/hd-bodygraph-geometry.ts` (Daten) +
  `hd-bodygraph.tsx` (Rendering). Der State-Layer wird programmatisch darüber
  gelegt, nicht in Figma eingefärbt.

### 5a. Neues Figma-File — Reihenfolge

1. **Backup:** aktuelle Figma-Seite duplizieren (nicht löschen). Code-Geometrie
   liegt unter `cursor/reference/geometry-backup-2026-08-24/`.
2. **Canvas zuerst, dann zeichnen.** Ein Frame `canvas / 800×1100` (Name darf
   mit `canvas` beginnen). Alles *innen* anlegen. Gruppen `centers` / `gates` /
   `channels` / `labels` / `hubs` sind nur Ordner — die **Layer-Namen** bleiben
   `hd.center.g`, `hd.gate.10`, `hd.channel.10_57`. Ein versehentlich zur
   Komponente gemachter Ordner (`gates / visible`) stört den Export nicht.
3. **Nicht** nachträglich lose Top-Level-Vektoren in Gruppen ziehen. Figma
   ändert dabei lokale Pfadkoordinaten. Wenn Layer schon lose liegen:
   markieren → Ausschneiden → Canvas-Frame anlegen → **Einfügen an
   Originalposition** (`Strg+Shift+V`).
4. **Sterne = Hanging-Mitte**, keine Geometrie. Namen:
   `hd.hub.integration` (Schnitt 10/20/34/57) und `hd.hub.26_44`.
   Der Plugin-Export schreibt `hubs`. Die sichtbaren Kanäle bleiben volle Pfade
   Tor→Tor; die Hälfte berechnet der Code am Hub.
5. Plugin neu laden. Es nimmt auch `Frame 1`, wenn darin `hd.*`-Layer liegen.
   Sauberer: den Frame in `canvas / 800×1100` umbenennen. Nicht „Manifest“
   als Ebene auswählen — das ist nur der Plugin-Start.
6. JSON hier einfügen. Ingest überschreibt **nicht** blind Herz-Vertices und
   Gate-`r`; Integration bleibt sechs Pfade.

## 6. Namen und Varianten

```
Bodygraph/Center      state = defined | undefined      selected = true | false
Bodygraph/Gate        activation = none | design | personality | both
                      channel = none | hanging | complete
Bodygraph/Channel     state = absent | partial | complete
Inspector/Field
Inspector/Section
Inspector/ProvenanceTrace
Activation/SourceRow  fixing = none | exalt | detriment | both
State/Badge
Facet/ContentBlock
```

Zwei Korrekturen gegenüber dem naheliegenden Entwurf:

- Gate-Zustand ist **zwei** Dimensionen. „hanging" ist eine Aussage über den
  Kanal, nicht über das Tor; `hangingGates` = aktiviertes Tor, dessen Gegentor
  fehlt.
- Fixierung ist **nicht** vierwertig. Exalt und Detriment sind unabhängig; das
  Aggregat („both" / juxtaposition) ist abgeleitet. Als vierter Enum-Wert würde
  daraus im Design ein eigener Mechanismus.

## 7. Fünf Pilotzustände statt zehn Screens

Der Dachau-Fall deckt fast die ganze Architektur ab (18.11.1980, 19:20,
48.26/11.43 — 3/5 Splenic Projector, Single, Right Angle Cross of Contagion):

1. **Center Milz, definiert** — Mechanik, Facetten nach State, kein leerer Slot.
2. **Tor 57** — Design-Aktivierung, Color/Tone/Base, Kanalkontext 10–57.
3. **Line 57.5** — Pluto exalt *direct*, Mond 10.1 detriment *harmonic via 10–57*,
   Aggregat „both". Keine Stärke- oder Balance-Sprache.
4. **Kanal 10–57 „Perfected Form"** — beide Tore aktiv, Endzentren definiert.
5. **Betriebssystem Projector** — Typ, Strategie, Autorität, Profil, Definition,
   Signature, Not-Self.

## 8. Provenienz-Faden als Signatur

Der Inspector zeigt nicht nur das Element, sondern wodurch der Zustand entsteht:

```
Quelle → Aktivierung → Gate → Line → Kanal → Center
```

Für 57.5 im Dachau-Chart:

```
Pluto · Design · Tor 57 · Linie 5
  Exaltation   Pluto 57.5          direct
  Detriment    Mond 10.1           harmonic via 10–57
  Aggregat     both (juxtaposition)
```

Das ist keine Dekoration, sondern macht die vorhandene Datenarchitektur
(`hd-line-fixing.ts`, `fixingSources`) sichtbar. Es ist der Teil, der die KARTE
von einer Chart-plus-Textspalte unterscheidet.

## 9. Mobile

Keine verkleinerte Sidebar-Ansicht, sondern: Kopf/Register → Bodygraph →
Detailbereich für das gewählte Element (Bottom Sheet oder nach unten laufend).
Die Karte bleibt sichtbar.

## 10. Was Figma nicht entscheidet

Nicht durch Ausprobieren im Design festlegen: ob `open` ein State ist, ob Gift
bei undefined fehlt, ob Shadow bei defined fehlt, ob eine planetare Aktivierung
mechanisch eine Fixierung erzeugt, ob eine Linie „stärker" ist, ob
`mind_when_open` ein Center-Slot oder ein allgemeines Mind-Konzept ist, ob
PHS-Labels achsenübergreifend gelten, ob ein Text `primary`, `contrast` oder
`mention` ist. Figma darf all das als Variante **darstellen**; die Wahrheit kommt
aus Vertrag, Engine und Content-Admission.
