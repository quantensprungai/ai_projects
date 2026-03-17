# HD: 13 Ebenen, Strukturbaum vs. KG, Engines & Lizenz

> Klarstellung nach externer Analyse. Quelle: IC_KG_Node_Edge_Schema v1.1 + structure_descriptor_seed.md.

---

## 1. HD hat 13 Ebenen in die Tiefe — das ist korrekt

Unser Schema (**IC_KG_Node_Edge_Schema v1.1**) definiert **hd_ontological_layer 1–13**. Das sind die **13 Ebenen** (Tiefen) des Human-Design-Systems:

| Layer | Ebene | Anzahl | Kurz |
|-------|--------|--------|------|
| 1 | Basis (Hexagramm-Basis) | 5 | Basis-Typen |
| 2 | Ton | 6 | Ton (1–6) |
| 3 | Farbe | 6 | Farbe |
| 4 | Linie | 6 | Line (1–6 pro Gate) |
| 5 | Tor (Gate) | 64 | Gate |
| 6 | Kanal (Channel) | 36 | Channel |
| 7 | Zentrum (Center) | 9 | Center |
| 8 | Profil | 12 | Profile (1/1 … 6/2) |
| 9 | Variable/Pfeile | 4 | Pfeile |
| 10 | Autorität | 7 | Authority |
| 11 | Typ | 5 | Type |
| 12 | Definition | 4 | Single, Split, … |
| 13 | Inkarnationskreuz | 192 | Incarnation Cross |

Eine andere Analyse sprach von „6 berechenbaren Schichten“ — das war eine **andere Gruppierung** (z. B. Topologie → Gates → Channels → Lines/Colors/Tones/Bases als globale Typen), **nicht** eine Abweichung von den 13 Ebenen. Für den **Strukturbaum** und den **KG** gilt: **13 Ebenen** sind die verbindliche Tiefe; alle müssen beim Parsen/Seeden berücksichtigt werden.

---

## 2. Strukturbaum ≠ Knowledge Graph (KG)

| | Strukturbaum | Knowledge Graph |
|---|--------------|------------------|
| **Was** | Einmaliges, statisches Konstrukt (die „Karte“ des Systems). | Dynamisches, wachsendes Netz (Inhalte + Verbindungen). |
| **Inhalt** | Nur **Struktur**: welche Knoten und Kanten existieren (Centers, Gates, Channels, Lines, Colors, Tones, Bases, Types, Profiles, …). **Keine** Bedeutungs-Texte. | Struktur **plus** Interpretationen, canonical_descriptions, Quellen, Cross-System-Edges. |
| **Wann** | Einmalig seeden (Phase 0), danach stabil. | Wächst durch PDF-Extraktion, Synthesis, Cross-System-Mapping. |

**Strukturbaum-Knoten:** Wir legen **Element-Typen und ihre Instanzen** als Nodes an (z. B. hd.gate.1 … hd.gate.64, hd.line.1 … hd.line.6, hd.color.1 … hd.color.6). **Nicht** jede berechnete Position (z. B. „Gate 34 Line 3 Color 2“) als eigener Node — das ist das **Ergebnis** einer Chart-Berechnung und gehört als Property auf die Chart-Entität, nicht in den statischen Strukturbaum. Der Strukturbaum enthält also z. B. die 64 Gates, die 6 Lines, die 6 Colors, die 5 Bases usw. als **globale** Knoten; die konkrete Kombination „Gate 34 / Line 3“ ist Teil der **berechneten Chart**, nicht ein zusätzlicher Struktur-Node.

**KG:** Derselbe Knoten (z. B. hd.gate.34) wird später mit **Bedeutungen** angereichert (canonical_description, Interpretationen aus Quellen, Shadow/Gift, Line-Keynotes usw.). Das ist Schicht B und darüber — der Strukturbaum ist Schicht A.

---

## 3. Was aus einem Engine-Repo extrahierbar ist (Strukturbaum)

**Einmalig aus einem HD-Repo (z. B. hdkit oder MicFell) ziehen:**

- Gate-Reihenfolge im Zodiak (IGING_CIRCLE_LIST / gateOrder)
- Gate → Center (GATES_CHAKRA_DICT / centersByChannel ableiten)
- Channel-Paare (Gate A + Gate B = Channel)
- Circuit-Zuordnung
- Berechnungslogik: Longitude → Gate/Line/Color/Tone/Base (Offset 58°, Segmentgrößen)

**Nicht aus dem Repo:** Gate-Bedeutungen, Line-Beschreibungen, Channel-Namen, Color/Tone/Base-Bedeutungen, Incarnation-Cross-Texte — das kommt aus **Quellen** (PDFs, Rave I'Ching, Gene Keys) und landet im KG (Schicht B+).

---

## 4. Engines im Vergleich (für Struktur + Berechnung)

| Repo | Layer-Tiefe | Ephemeris | Lizenz | Für uns |
|------|--------------|-----------|--------|---------|
| **MicFell/human_design_engine** | Gate→Base komplett | pyswisseph | ⚠️ unklar (kein License-File) | Beste Basis: alle 13 Ebenen, Python, direkt pyswisseph. Autor vor kommerzieller Nutzung kontaktieren. |
| dturkuler/humandesign_api | Gate→Base | pyswisseph | ⚠️ unklar | Fertige FastAPI-API. |
| **hdkit (jdempcy)** | Gate/Line (Color/Tone/Base aus Ephemeris) | externe URL oder pyswisseph | MIT ✅ | Bereits geklont; Logik in Sample-App, Struktur in constants/bodygraph-data. |
| garys-primary/humanDesignEngine.js | Gate→Base (Port von MicFell) | WIP | ⚠️ unklar | JS-Port, noch unvollständig. |

**Empfehlung:** Für **Strukturextraktion** (alle 13 Ebenen): MicFell als Referenz nutzen oder klonen; für **Berechnung** entweder (a) hdkit-Logik + pyswisseph (Grad → Gate/Line/… portieren) oder (b) MicFell-Logik nutzen (nach Lizenzklärung). Eine **pyswisseph**-Installation deckt HD, westliche Astro und Jyotish (PyJHora) ab; BaZi braucht kein Ephemeris.

---

## 5. Swiss Ephemeris — Lizenz (CHF 750 vs. 1.550)

- **Erste Lizenz:** CHF 750 = **ein** Softwareprodukt / eine App.  
  → **Inner Compass als eine SaaS-Plattform** = CHF 750 reicht.
- **Zusätzliche Lizenz:** CHF 400 je weiteres **separates** Produkt (gleicher Lizenznehmer).
- **Unlimited:** CHF 1.550 = beliebig viele Produkte.  
  → Erst sinnvoll, wenn ihr **mehrere getrennte Produkte** (z. B. HD-Tool, Astro-Tool, Jyotish-Tool als eigene Apps) anbietet.

**Für den Start: CHF 750.** Unlimited wenn ihr skalierst und mehrere Produkte ausrollt.

---

## 6. Freie Ephemeris-Alternativen (Kurz)

- **Swiss Eph (Moshier-Modus):** Läuft ohne .se1-Dateien, Genauigkeit für HD ausreichend. Kommerzielle Nutzung trotzdem CHF 750.
- **Moshier-Ephemeris-JS:** MIT, keine externen Dateien — für HD grundsätzlich nutzbar; **swe_solcross** (Design-Datum 88° zurück) fehlt dort, müsste selbst implementiert werden.
- **astropy:** BSD, aber kein HD-spezifisches Design-Datum; Aufwand für HD höher.

Für eine saubere, eine Lizenz abdeckende Lösung bleiben **pyswisseph + professionelle Lizenz** die pragmatische Wahl für HD, Astro und Jyotish.

---

**Ebenen-Recherche, Vollständigkeit, Gene Keys separat:** [hd_ebenen_recherche_und_strukturbaum_vollstaendigkeit.md](hd_ebenen_recherche_und_strukturbaum_vollstaendigkeit.md).

*Referenz: IC_KG_Node_Edge_Schema v1.1 (hd_ontological_layer 1–13), structure_descriptor_seed.md, hd_kit_structure_extraction.md.*
