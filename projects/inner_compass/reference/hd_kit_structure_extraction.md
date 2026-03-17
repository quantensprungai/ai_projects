# HD-Kit (hdkit) — Struktur-Extraktion & Zum-Laufen-bringen

> Auswertung von `bodygraph-data.js`, `constants.js`, `hdkit.js` unter `code/hd_saas_app/packages/engines/hd/`. Basis für system_structure/hd.json (Kit-first).

---

## 0. Ist das Kit nutzbar? Berechnung läuft nur mit Ephemeris

**Wichtig:** Das Kit **berechnet keine Planetenpositionen selbst**. Die eigentliche Chart-Berechnung (Geburtsdatum → Type, Profile, Channels, …) passiert in der **Sample-App** (`sample-apps/hdblacklist-client/src/hd-utils/get-bodygraph-json.js`). Dort:

1. **Ephemeris wird von außen geladen:** `fetch(https://...netlify.app/ephemeris-annual-{year}-1s-accuracy.json)` — vorkomputierte Aktivations pro Zeitstempel (Sun, Moon, … mit Gate/Line/Color/Tone/Base).
2. Zum Geburtszeitpunkt wird der passende Eintrag gesucht; daraus werden Personality- und Design-Aktivations abgeleitet (Design = ~88° Solar Arc zurück).
3. Aus den Aktivations leitet die gleiche Datei ab: **Profile, Channels, Type, Authority, Definition, Variable, Circuitry** — mit den Lookup-Tabellen **definedCentersByChannel**, **harmonicGates**, **motorToThroat** usw.

**Fazit:** Wenn die externe Ephemeris-URL erreichbar ist und das Schlüsselformat passt, **lässt sich alles berechnen** (Type, Profile, Channels, Authority, Definition, Variable). Die fehlenden Struktur-Infos (Tone, Color, Base, Profile-Liste, Cross-Namen) in `constants.js`/`bodygraph-data.js` betreffen **Metadaten für Anzeige**, nicht die Berechnung — die Berechnung nutzt g/l/c/t/b aus der Ephemeris. Für **Produktion** solltet ihr Ephemeris **lokal** berechnen (z.B. pyswisseph in `packages/engines/astro`) und die gleiche Ableitungslogik (get-bodygraph-json) mit euren Daten füttern.

**Test-Skript:** `code/hd_saas_app/scripts/test-hdkit.mjs` — prüft, ob die Ephemeris-URL lädt und ob ein Zeitstempel einen Aktivations-Eintrag findet. Aufruf: `node scripts/test-hdkit.mjs 2024-06-15 12:00:00`. Wenn die URL funktioniert, siehst du Personality Sun (Gate, Line, Color, Tone, Base); dann kannst du prüfen, ob das Kit für euch passt.

### Brauchen wir ein anderes Kit? Und: Ist hdkit eine Oberfläche?

- **hdkit ist keine Oberfläche.** Es ist eine **Bibliothek + Strukturdaten** (Centers, Channels, Gates, Lines, Lookups) plus **Ableitungslogik** in der Sample-App (Type, Profile, Authority aus Aktivations). Die "Oberfläche" sind die Sample-Apps (z. B. hdblacklist-client = React) — Beispiele, keine fertige Produkt-UI. Für Inner Compass baut ihr eure eigene UI (Next.js); hdkit liefert nur **Berechnungslogik und Daten**, nicht die Ansicht.

- **Können wir ein Kit nutzen, das wir eh brauchen (Swiss)?** **Ja.** Wir brauchen **kein zweites HD-Kit**. Die Rollen sind:
  - **pyswisseph** (habt ihr in `packages/engines/astro`): berechnet **Planetenpositionen** (Länge in Grad, z. B. Sonne bei 236,5°). Nichts HD-spezifisch.
  - **hdkit**: liefert die **HD-Logik** — aus Positionen (oder aus vorkomputierten Aktivations) werden **Gate/Line/Color/Tone/Base** und daraus **Type, Channels, Authority, Definition** abgeleitet. Die Umrechnung **Grad → Gate/Line/…** steckt in der Sample-App (`getActivationFromDegrees`); die Lookups (definedCentersByChannel, harmonicGates, motorToThroat) ebenda.

- **Pragmatisch:** Entweder (a) die **externe Ephemeris-URL** weiter nutzen (wie jetzt im Test) oder (b) **pyswisseph** verwenden, um Positionen zu berechnen, und die **gleiche hdkit-Logik** (oder eine Portierung davon) mit diesen Grad-Werten füttern. Dann habt ihr eine Berechnung ohne Abhängigkeit von der Netlify-URL; hdkit bleibt die Quelle für HD-Struktur und Ableitungsregeln, Swiss die Quelle für Positionen.

---

## 1. bodygraph-data.js

### centersByChannel (Channel → Centers)

Getter `centersByChannel`: Objekt `channel_id → [Center-Namen]`.  
Channel_id Format: `"g1-g2"` (z.B. `"7-31"`, `"19-49"`).  
Center-Namen (engl.): **Root**, **Sacral**, **Solar Plexus**, **Splenic**, **Heart**, **Throat**, **Ajna**, **G**. Aus der Logik (headToAjna, noCentersDefined) kommt zusätzlich **Head** → insgesamt **9 Centers**.

- Daraus ableitbar: **Channel-Liste** (unique Keys; Duplikate wie `35-36`, `64-47` mehrfach vorhanden, also dedupen) und für jeden Channel die **zwei Gates** (aus dem Key parsen) und die **Centers**, die der Channel verbindet.
- **Center → Gates:** Für jeden Center alle Channels durchgehen, die ihn enthalten; Gates aus diesen Channels sammeln → pro Center die Liste der Gate-Nummern.

### Logik (ergibt Typen, Autorität, Definition)

- **Types (5):** `auraType()` → Manifesting Generator, Generator, Manifestor, Reflector, Projector.
- **Authorities (7):** `innerAuthority()` → Solar Plexus, Sacral, Spleen, Ego, Self Projected, Outer Authority, Lunar.
- **Definitions (5):** `definition()` → Single, Split, Triple Split, Quad Split, None.
- **Inkarnationskreuz:** `incarnationCross()` nutzt `RIGHT_ANGLE_CROSSES_BY_SUN_GATE` und `JUXTAPOSITION_CROSSES_BY_SUN_GATE` — **in diesen Dateien nicht definiert** (evtl. fehlend oder in anderer Datei; im Repo suchen oder manuell ergänzen).

---

## 2. constants.js

### Gates (64)

- **gateOrder**, **harmonicOrder**, **svgRaveMandalaGateOrder** — Reihenfolge der Gates (für Mandala/Anzeige).
- **gateOf** — Gate 1–64 → "Gate of …" (z.B. "Gate of Self-Expression").
- **gateNames** — I-Ging-Namen (64).
- **gateShortDescriptions** — Kurzbeschreibung pro Gate (64).
- **iChingHexagramGlyphs** — Hexagramm-Symbol pro Gate (1–64).
- **aminoAcidByGate** — pro Gate: name, ring, gates (Array), oppositeGate → Gate-Metadaten und Hexagramm-Partner.
- **godheadsByGate** — Gate → Godhead (16 Godheads).
- **raveMandalaGateColors** — Gate → Farbe (Rave-Mandala).

### Lines (384 = 64×6)

- **fixings** — Keys `"gate.line.exaltingPlanet"` und `"gate.line.detrimentingPlanet"` (z.B. `"1.1.exaltingPlanet"`, `"1.1.detrimentingPlanet"` … `"64.6.*"`).  
  → **Alle 384 Lines** mit Exaltation/Detriment-Planet (hd_ontological_layer 4, Line-Ebene).

### Weitere

- **planetGlyphs** — 12 Planeten/Nodes (Sun, Earth, NorthNode, SouthNode, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto).
- **astrologicalSigns** (12), **godheads** (16), **nucleicAcidSequences** (64) — für Anzeige/Referenz.

---

## 3. hdkit.js

- **harmonicGate(gate)**, **oppositeGate(gate)**, **nextGate(gate)**, **nextLine(line)** — Gate-/Line-Nachbarn (Mandala-Logik).
- **integrationGates** = [34, 20, 10, 57] — spezielle Gate-Gruppe.
- Keine expliziten Listen für Profile, Crosses, Tone, Color, Base.

---

## 4. Abgeleitete Struktur (für system_structure/hd.json)

| Ebene (hd_ontological_layer) | Quelle im Kit | Inhalt |
|------------------------------|----------------|--------|
| **Center (7)** | bodygraph-data: centersByChannel + Logik | 9 Centers: Head, Ajna, Throat, G, Heart, Sacral, Solar Plexus, Splenic, Root. Center→Gates aus Channel-Zuordnung ableiten. |
| **Channel (6)** | bodygraph-data: centersByChannel (Keys dedupen) | 36 Channels; jeder Channel = Gate-Paar (g1, g2) + zugehörige Centers. |
| **Gate (5)** | constants: gateOf, gateNames, gateShortDescriptions, aminoAcidByGate | 64 Gates mit Namen, Kurzbeschreibung, oppositeGate. |
| **Line (4)** | constants: fixings (Keys gate.line) | 384 Lines; pro Line exaltingPlanet + detrimentingPlanet. |
| **Type (11)** | bodygraph-data: auraType() | 5 Types. |
| **Authority (10)** | bodygraph-data: innerAuthority() | 7 Authorities. |
| **Definition (12)** | bodygraph-data: definition() | 5 Definitionen. |
| **Inkarnationskreuz (13)** | bodygraph-data: incarnationCross() | Referenz auf RIGHT_ANGLE_* / JUXTAPOSITION_* — **fehlt im Kit**, extern oder manuell. |

**Im Kit nicht gefunden (evtl. woanders oder manuell):**

- **Tone (2):** 6 Tones — keine explizite Tabelle in diesen drei Dateien.
- **Color (3):** 6 Colors — keine explizite Tabelle (nur raveMandalaGateColors pro Gate, nicht pro Color-Ebene).
- **Basis (1):** 5 Bases — nicht gefunden.
- **Profile (8):** 12 Profile (1/1 … 6/2) — nicht in diesen Dateien.
- **Variable/Pfeile (9):** 4 — nicht gefunden.
- **Cross-Namen (13):** RIGHT_ANGLE_CROSSES_BY_SUN_GATE, JUXTAPOSITION_CROSSES_BY_SUN_GATE — Referenz da, Definition fehlt.

---

## 5. Nächste Schritte

1. **Center→Gates aus centersByChannel ableiten:** Alle Keys parsen (g1-g2), pro Center alle Gates sammeln, die in Channels vorkommen, die diesen Center enthalten → `structure.centers` mit `gates: [1, 2, …]` pro Center.
2. **Channels deduplizieren:** Unique channel_ids, pro Channel `{ id: "7_31", gates: [7, 31], centers: ["Root"] }` → `structure.channels`.
3. **Gates/Lines aus constants.js exportieren:** Parser schreibt gateOf, gateNames, fixings (Lines + Exaltation/Detriment) in structure.
4. **Fehlende Ebenen:** Tone, Color, Base, Profile, Variable, Cross-Namen — entweder in anderen hdkit-Dateien suchen (sample-apps, weitere JS) oder aus reference (IC_KG_Schema, Leitdokument) übernehmen und in structure eintragen.
5. **Seed anbinden:** `system_structure/hd.json` aus dieser Extraktion befüllen; Seed liest diese Datei.

---

*Stand: Auswertung nach erstem Durchgang. Parser-Script kann die strukturierten Teile (centersByChannel, gateOf, fixings) automatisch auslesen; fehlende Ebenen manuell oder aus zweiter Quelle.*
