---

last_update: 2026-08-13
status: draft
scope:
  summary: "K3/K4-Quellen nach Vollständigkeitsstufe; Gene Keys vs Registry; Ur-Systeme mit Start-Kanon-Tabellen (K2_ref/K3_deutung); Abgleich manueller Downloads; Architektur separate KG vs. Tradition-Tags."
  in_scope:
    - Gene Keys Must-cover vs entity_registry_hd_v02 + gk_catalog_v0
    - Ur-Systeme — konkrete Startliste (extern kuratiert, hier eingebettet)
    - K2_ref vs K3_deutung; getrennte Textlinien / Kabbalah-Tracks
    - Scope-Stufen (core / extended); Verweise literature_acquisition_ic_aa.md, status.md
  out_of_scope:
    - Illegale Beschaffung
    - Engine-Implementierungsdetails (→ engines.md / Code)
notes:

- "Tabellen unten: Anker aus externer Recherche (fremde KI); mit IC-Prinzipien abgeglichen — Editionen/Jahre verifizieren."
- "Manuelle Downloads unter C:UsersAdmin105DownloadsLiteratur entsprechen inhaltlich diesem Sammelziel; Bestand: literature_local_inventory_2026-05-06.csv."

---

# Literatur-Kanon nach Scope (HD, Gene Keys, Ur-Systeme)

## 0. Manueller Download = frühe Realisierung dieses Kanons

Die **Werkliste**, die ihr für AA/IC ohnehin einsammeln wolltet, hast du **teilweise schon manuell** unter `Downloads\Literatur` abgelegt. Die **saubere Bestandsdatei** dazu liegt im Repo: `reference/literature_local_inventory_2026-05-06.csv` (+ `.meta.json`).

**Abgleich:** dieselben Titel/MD5s später gegen die Tabellen in **§6** (Ur-Systeme) und gegen `entity_registry_hd_v02` / künftige `entity_registry_*_v01.json` — Lücken = fehlende Zeilen oder falsche `rolle`/`priority`.

---

## 1. Drei Vollständigkeitsstufen (festhalten)


| Stufe             | Ziel                                                        | Typische Quellen                                                                                                                    |
| ----------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Core**          | K2-konforme Struktur + wenige K3-Definitionen für UI/Engine | Kataloge `system_structure/*_catalog_v0.json`, Deskriptoren `system_descriptors/*.json`, plus **1–3 Primärwerke** pro Schule/System |
| **Concept graph** | Begriffe, Kanten, Provenance (`source_work`, Kapitel)       | Wie Core + **Kanon-Werke** aus `entity_registry_*` → `known_works` (high priority)                                                  |
| **Extended**      | Praxis, Kurs-Sprache, Rand-Schulen, Übersetzungen           | Zusatzwerke, Website-Glossare — **nach** Core stabil                                                                                |


So explodiert der Umfang nicht: erst **Core/Concept**, dann **Extended** pro `system_id`.

---

## 2. K2_ref vs K3_deutung — und: ein KG oder mehrere?


| Rolle          | Bedeutung                                                                                                             | Beispiel                                                                             |
| -------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **K2_ref**     | Primär-/Standardtexte oder wissenschaftliche Überblicke, die **Begriffe und Struktur** einer **Textlinie** definieren | Wilhelm/Baynes I Ging; Kaplan *Sefer Yetzirah*; *Huangdi Neijing* (Auswahl)          |
| **K3_deutung** | Interpretations-, Popularisierungs- oder **Brücken**werke (Richtung HD, Gene Keys, westliche Psychologie)             | Parkyn *Book of Lines*; Rudd *Gene Keys* als I-Ching-Brücke; Judith *Wheels of Life* |


**Separate Knowledge Graphs vs. ein Graph mit Tags?**

- **Empfehlung IC (ein Pfad):** **ein** zusammenhängender Graph (Meta-Ziel), aber **strikte Trennung über `system_id` + Provenance**: jede Aussage hat `source_system_id`, `source_work`, optional `**tradition`** / `**text_line`** (z. B. `wilhelm_baynes`, `legge`, `tantra_sanskrit`, `western_seven_chakra`).
- **Zweiter Pfad nur bei Kollision der *Ontologie*** — Kabbala war nur das **deutlichste** Beispiel, weil derselbe Baum/hebräische Begriffe in **jüdisch-mystischer** vs. **hermetisch-astrologischer** Linie **anders definiert** sind; eine gemischte Suche würde Knoten semantisch vergiften. **Nicht** „nur Kabbala“: dasselbe Prüfkriterium gilt überall.
- **Weitere Kandidaten für Split oder strikte Teilbäume** (nur wenn ihr beim Modellieren merkt, dass Tags nicht reichen):
  - `**chakra`:** klassisch-tantrik / Āyurveda‑nahe Linie vs. **westliches 7‑Chakra‑Psychologisieren** (andere Zählungen, andere „Energien“-Stories) — oft reicht `**tradition` + `evidence_class`**; Split nur wenn ihr getrennte **Knotentypologien** wollt.
  - `**wu_xing` / TCM:** strikt **medizinisch-kosmologisch** vs. rein **philosophische** Lesart der 五行 — Kanten zu Organen/Jahreszeiten vs. „reine“ Korrespondenz; meist **ein** `wu_xing` mit `lens: tcm | philosophy`.
  - `**pancha_bhuta`:** Sāṃkhya-/Yoga‑Kontext vs. **Ayurveda‑Doṣa‑Netz** — oft **ein** Graph mit zwei **Teilgraphen** und klaren `maps_to` zwischen Bhūta und Doṣa, statt zwei Welten.
- **Wann wirklich zwei `system_id`s?** Wenn zwei Linien **keine** gemeinsame, stabile K2-Knotenbasis teilen sollen (oder ihr **bewusst** getrennte Curricula/AA-Profile/MinerU-Pipelines wollt). Kabbala jüdisch vs. hermetisch ist der häufigste Fall; alles andere **erst** splitten, wenn der **eine-Pfad-mit-Tags**-Ansatz in Queries oder UI bricht.
- **I Ging:** unterschiedliche Übersetzungs-/Kommentarlinien (Wilhelm vs. Legge vs. Shaughnessy) = **parallele K3-Schichten** über **derselben** K2-Struktur (64 Hexagramme) — **gleiche** `i_ching.hex.*`, verschiedene Glossen/Properties mit `text_line` — **kein** zweiter `system_id` nötig. **Nicht** in dieses KG: *Blue I Ching* (`hd` / `tradition: 64keys`) und *Oracle of the Cosmic Way* (`hd` / `tradition: cosmic_sidereal` — 64-Gate-Prosa sideral). Siehe `decisions.md` 2026-08-13 HD-Schulen.

**Kurz:** Für eure Zwecke macht **ein Graph + `tradition`/`text_line`/`source_work`** fast immer Sinn; ein **zweiter Pfad** (`system_id` oder physisch getrennter Teilgraph) nur dort, wo **Begriffe gleich heißen, die Sache aber nicht dieselbe ist** — Kabbala ist das Paradebeispiel, nicht die einzige mögliche Ausnahme.

**Vollständige Entscheidungs-Matrix + Policy-Tabelle:** → `**reference/ontology_policy.md`**

---

## 3. Gene Keys — externe Minimal-Analyse vs. IC

**Kern: ja — inhaltlich stimmig** für einen **Minimal-Kanon** (Codebook + Golden-Path-Logik + optional Kontemplation).

### A. Codebook

- Extern: *Unlocking the Higher Purpose…* — Registry: *Embracing Your Higher Purpose* (Watkins / Auflage).
- `gk_catalog_v0.json`: Shadow/Gift/Siddhi-**Namen** = K3/K4 aus Pipeline/Büchern.

### B. Golden Path (Activation / Venus / Pearl)

- In `entity_registry_hd_v02` (`auth_richard_rudd`): *Genius* … vorhanden; **Venus-** und **Pearl-/Prosperity**-Bände als eigene `known_works` **nachziehen**.

### C. *The Art of Contemplation*

- Bei Praxis-Knoten: Priorität ggf. von `low` auf `medium`/`high` anheben.

### D. „4 Bücher ≈ 80–90 %“

- Heuristik für **offizielles Narrativ**; für **Extended** (Web/Kurse) reicht das nicht.

---

## 4. Ur-Systeme: Vorgehen (status.md-kompatibel)

- **Eigene** `system_id`, **eigene** `entity_registry_<system>_v01.json` (o. ä.) — **nicht** in `entity_registry_hd_v02` mischen.
- **Ziel:** **Core-Kanon** (Ankerwerke), nicht Vollbibliografie.
- **Jahre/Editionen:** nur Anker; beim Import **Verlag/ISBN/Übersetzer** verifizieren.

---

## 5. Welche `system_id`s sind bei IC „Ur-Systeme“ — und was ist davon getrennt?

**Als Ur-Systeme / Struktur-first** (Deskriptor + Katalog v0, Literatur-Pipeline wie in `cursor/status.md`): u. a. `**i_ching`**, `**kabbalah_jewish`** / `**kabbalah_hermetic**`, `**chakra**`, `**pancha_bhuta**`, `**wu_xing**`, `**western_elements**` (plus Element-Verwandte wie in `system_descriptors/`).

**Eigene Chart-Engines + eigene `entity_registry_*`, aber nicht dieselbe „Ur-Literatur“-Kategorie:** `**jyotish`**, `**bazi`**, `**ziwei**`, `**astro**`, `**mayan_tzolkin**`, `**nine_star_ki**`, … — dort geht es primär um **Berechnung + Schule**, nicht um „klassisches I Ging ohne HD“.

`**genekeys` / `hd`:** gebunden an Ephemeris/Kit; Literatur teils über HD-Registry (`auth_richard_rudd`) und künftig eigenes Profil — siehe `literature_acquisition_ic_aa.md`.

---

## 6. Start-Kanon-Tabellen (K2_ref / K3_deutung, P0–P3)

*Hinweis: Jahreszahlen/Editionen variieren; für den KG entscheidend ist die **festgelegte Referenzlinie** (Übersetzung/Schule).*

### 6.1 `i_ching`

**Stichworte:** Judgements, Image, Lines, Ten Wings, Trigramme, Hexagrammstruktur; Brücke: lines, gates, hexagrams↔gates.

**Festgelegte AA-/Dateiauswahl (Wilhelm/Baynes EN, Legge, Zusatz):** siehe `**reference/decisions.md`** Eintrag **2026-05-07** (konkrete Treffer-IDs und Ausschlüsse).


| system_id | autor                                            | titel                                                                   | jahr                 | sprache | rolle                                                | priority |
| --------- | ------------------------------------------------ | ----------------------------------------------------------------------- | -------------------- | ------- | ---------------------------------------------------- | -------- |
| i_ching   | Richard Wilhelm (Übers.); Cary F. Baynes (Engl.) | I Ging / Book of Changes (Wilhelm/Baynes-Linie)                         | 1924 (DE), 1950 (EN) | DE/EN   | K2_ref                                               | P0       |
| i_ching   | James Legge (Übers.)                             | I Ching (Sacred Books of the East / Chinese Classics)                   | 1882                 | EN      | K2_ref (Alternative Textlinie)                       | P1       |
| i_ching   | Edward L. Shaughnessy (Übers./Komm.)             | I Ching: The Classic of Changes                                         | 1996                 | EN      | K2_ref (moderne textkritische Linie)                 | P1       |
| i_ching   | Stephen Karcher                                  | Total I Ching (o. vergleichbares Werk)                                  | 2003                 | EN      | K3_deutung (popular/interpretativ)                   | P2       |
| i_ching   | Richard Rudd                                     | The Gene Keys (Brücke: 64 Archetypen, Shadow/Gift/Siddhi)               | 2009 ff.             | EN      | K3_deutung (GK↔I Ching)                              | P0       |
| i_ching   | Chetan Parkyn                                    | The Book of Lines                                                       | 2007                 | EN      | K3_deutung (HD-Brücke „Lines“) — IC: `hd` / `parkyn`, nicht I-Ging-KG | P0       |
| **hd**    | Hanna Moog; Carol K. Anthony                     | I Ching: The Oracle of the Cosmic Way                                   | 2002/2011            | EN      | **64-Gate-Prosa sideral** (`tradition: cosmic_sidereal`); nicht `i_ching.*` | P1 (Linse) |


> Zeile Cosmic Way sitzt in der I-Ging-Tabelle nur inventarisch (Datei oft im I-Ging-Ordner). **Produktziel:** `hd.gate.*`. Blue I Ching analog: Datei im I-Ging-Ordner, `tradition: 64keys`. Volltext: `decisions.md` 2026-08-13.


### 6.2 Kabbalah — `kabbalah_jewish` vs. `kabbalah_hermetic`

**Stichworte (jüdisch-klassisch):** Sefirot, Ein Sof, Olamot, Zimzum, Shekhinah … **Stichworte (hermetisch):** Tree of Life, Paths, hebräische Buchstaben als Korrespondenz-Raster, Golden-Dawn-Material.

**Festlegung (siehe `reference/decisions.md`, 2026-05-07):** Zwei `**system_id`s** — `**kabbalah_jewish`** und `**kabbalah_hermetic`**. Ein einziges `kabbalah` mit nur `tradition`-Tag war die Alternative; für IC gilt der **Split**, damit Registry, Literaturordner und KG-Knoten nicht vermischen. **Crosswalk** zwischen den Tracks im Graph nur **explizit** (z. B. `has_analogue`), nie stillschweigend gleiche IDs.


| system_id         | autor                                 | titel                                                       | jahr                           | sprache                    | rolle                                                          | priority |
| ----------------- | ------------------------------------- | ----------------------------------------------------------- | ------------------------------ | -------------------------- | -------------------------------------------------------------- | -------- |
| kabbalah_jewish   | (Tradition; anonym)                   | Sefer Yetzirah                                              | spätantik (Datierung variiert) | HE/DE/EN                   | K2_ref                                                         | P0       |
| kabbalah_jewish   | Aryeh Kaplan (Übers./Komm.)           | Sefer Yetzirah: The Book of Creation in Theory and Practice | 1990 (rev. u. a. 1997)         | EN (+ ggf. HE in Ausgaben) | K2_ref                                                         | P0       |
| kabbalah_jewish   | Gershom Scholem                       | Major Trends in Jewish Mysticism                            | 1941                           | EN/DE                      | K2_ref (wiss. Überblick)                                       | P1       |
| kabbalah_jewish   | Moshe Idel                            | Kabbalah: New Perspectives                                  | 1988                           | EN                         | K2_ref                                                         | P2       |
| kabbalah_jewish   | (Zohar; z. B. Pritzker Edition, Matt) | The Zohar (Auswahl/Bände)                                   | 2004–                          | EN                         | K2_ref (Auszüge)                                               | P2       |
| kabbalah_hermetic | Dion Fortune                          | The Mystical Qabalah                                        | 1935                           | EN                         | K3_deutung (westl. Esoterik-Standard; nicht jüdischer K2-Text) | P1       |
| kabbalah_hermetic | Israel Regardie                       | The Golden Dawn (Material)                                  | 1937/40                        | EN                         | K3_deutung (hermetische Praxis/Correspondences)                | P2       |


### 6.3 `chakra`

**Abgleich:** `system_structure/chakra_catalog_v0.json`. Stichworte: Ṣaṭ-cakra, nāḍī, kuṇḍalinī, granthi, bija mantra; Westen: 7-Chakren-Psychologisierung.


| system_id | autor                                         | titel                                              | jahr | sprache | rolle                           | priority |
| --------- | --------------------------------------------- | -------------------------------------------------- | ---- | ------- | ------------------------------- | -------- |
| chakra    | Sir John Woodroffe (Arthur Avalon)            | The Serpent Power (inkl. Ṣaṭ-cakra-nirūpaṇa u. a.) | 1919 | EN      | K2_ref                          | P0       |
| chakra    | (Upanishaden; kuratierte Auswahl)             | Yoga Upanishads / vergleichbar                     | alt  | EN/DE   | K2_ref                          | P2       |
| chakra    | B. K. S. Iyengar (o. Standardwerk eurer Wahl) | (konkretes Werk festlegen)                         | —    | EN/DE   | K2_ref                          | P2       |
| chakra    | Anodea Judith                                 | Wheels of Life                                     | 1987 | EN      | K3_deutung (westliche Synthese) | P1       |


### 6.4 `pancha_bhuta`

Stichworte: mahābhūta, tattva, ākāśa/vāyu/tejas/āpas/pṛthvī; Ayurveda: doṣa-Netz.

**Offene Entscheidung:** „Elemente“ **metaphysisch** vs. **ayurvedisch-medizinisch** modellieren — beeinflusst Kanten stark.


| system_id    | autor       | titel                                 | jahr       | sprache | rolle  | priority |
| ------------ | ----------- | ------------------------------------- | ---------- | ------- | ------ | -------- |
| pancha_bhuta | (Tradition) | Sāṃkhya Kārikā (mit Kommentar/Übers.) | ca. 4. Jh. | EN/DE   | K2_ref | P1       |
| pancha_bhuta | (Tradition) | Caraka Saṃhitā (Auswahl/Übers.)       | klassisch  | EN      | K2_ref | P2       |
| pancha_bhuta | (Tradition) | Suśruta Saṃhitā (Auswahl/Übers.)      | klassisch  | EN      | K2_ref | P3       |


### 6.5 `wu_xing`

Stichworte: 五行, 生/克, Zang-Fu, Stämme/Zweige, Korrespondenzen.


| system_id | autor                                | titel                                       | jahr  | sprache | rolle                       | priority |
| --------- | ------------------------------------ | ------------------------------------------- | ----- | ------- | --------------------------- | -------- |
| wu_xing   | (Tradition)                          | Huangdi Neijing (Übers./Kommentar; Auswahl) | antik | EN/DE   | K2_ref                      | P0       |
| wu_xing   | Ted Kaptchuk                         | The Web That Has No Weaver                  | 1983  | EN/DE   | K3_deutung (TCM-Einführung) | P1       |
| wu_xing   | (Standardwerk 5 Elemente; festlegen) | …                                           | —     | DE/EN   | K3_deutung                  | P2       |


### 6.6 `western_elements`

Stichworte: four elements, aether, temperaments, hot/cold/dry/wet; Astro: triplicities.


| system_id        | autor                                              | titel                                         | jahr  | sprache | rolle                   | priority |
| ---------------- | -------------------------------------------------- | --------------------------------------------- | ----- | ------- | ----------------------- | -------- |
| western_elements | Aristoteles (Sekundärtext mit Zitaten)             | On Generation and Corruption / Elementenlehre | antik | EN/DE   | K2_ref                  | P1       |
| western_elements | Empedokles                                         | Fragmente (Vier-Elemente-Lehre)               | antik | EN/DE   | K2_ref                  | P2       |
| western_elements | (Hellenistische Astro; Valens/Dorotheus o. Übers.) | (Werk festlegen)                              | antik | EN      | K2_ref (Astro-Elemente) | P1       |


---

## 7. Schnellstart „Core-Kanon“ (P0/P1) pro Ur-System

Wenn ihr **schnell** einen arbeitsfähigen Concept-Graph wollt:

- **i_ching:** Wilhelm/Baynes + (Legge **oder** Shaughnessy) + Parkyn *Book of Lines* + Rudd *Gene Keys* (Brücke).
- **kabbalah_*:** *Sefer Yetzirah* + Kaplan (+ optional Scholem) unter `**kabbalah_jewish`**; Fortune/Regardie/Golden Dawn unter `**kabbalah_hermetic`** (kein gemeinsames `kabbalah` ohne Split).
- **chakra:** Woodroffe/Avalon *Serpent Power* + Judith *Wheels of Life*.
- **wu_xing:** *Neijing*-Auswahl + eine westliche TCM-Standard-Einführung (z. B. Kaptchuk).
- **western_elements:** ein antiker Elementen-Anker + ein hellenistisch-astrologischer Anker (konkret festlegen).

---

## 8. Nächste Schritte (kuratiert)

1. **Tradition wählen:** Kabbala (jüdisch vs. hermetisch); chinesische Quelle (medizinisch-kosmologisch vs. rein philosophisch).
2. **Listen auf je 2–5 Core-Werke** pro `system_id` kürzen (nach eurer Wahl).
3. `**entity_registry_iching_v01.json`** etc. im gleichen Schema wie HD anlegen (oder Tabellen erst in CSV, dann JSON).
4. **Manuellen Bestand** (`literature_local_inventory_*.csv`) den neuen Zeilen zuordnen (`system_id`, `rolle`, `priority`).

---

## 9. Verknüpfungen im Repo


| Artefakt                                              | Rolle                          |
| ----------------------------------------------------- | ------------------------------ |
| `reference/entity_registry_hd_v02.json`               | HD + Schulen inkl. Rudd/Parkyn |
| `reference/literature_local_inventory_2026-05-06.csv` | Manueller Download-Bestand     |
| `system_structure/gk_catalog_v0.json`                 | Gene Keys K2                   |
| `system_structure/i_ching_catalog_v0.json`            | I Ging K2                      |
| `system_structure/chakra_catalog_v0.json`             | Chakra K2                      |
| `cursor/status.md`                                    | Ur-Systeme vs. Chart-Engines   |
| `reference/literature_acquisition_ic_aa.md`           | AA-Pipeline                    |


**Registry-Pflege HD:** Rudd `known_works` um Venus + Pearl/Prosperity ergänzen; Gene-Keys-Haupttitel Verlag/AA abstimmen.