# Inner Compass — Design-Entscheidungen

> Lebendes Dokument. Neue Entscheidungen oben anfügen. Format: Decision → Rationale → Consequences.

---

## 2026-05-07: Ur-Systeme — `kabbalah`-Split, `chakra` ein Pfad, I-Ging-AA-Auswahl (Wilhelm/Baynes + Legge)

**Decision:**

1. **`kabbalah`:** Zwei **`system_id`s**: **`kabbalah_jewish`** (klassisch / Sefer Yetzirah-Linie, Scholem/Idel, ggf. Zohar-Auszüge) und **`kabbalah_hermetic`** (Golden Dawn, Fortune, Regardie u. ä.). Crosswalk-Kanten nur explizit (`has_analogue`, …).

2. **`chakra`:** **Ein** `system_id` **`chakra`**; Trennung klassisch vs. westlich über **`tradition`** + **`model`** (z. B. `tantra_classical`, `western_synthesis`), kein zweites `system_id` bis sich ein Pilot gegen beweist.

3. **I Ging — welche AA-Treffer für IC `text_line: wilhelm_baynes` (engl. P0):**  
   - **Primär (vollständige Bollingen-Ausgabe, Text + Material + Kommentare / Ten Wings je nach Auflage):** Princeton UP, **Wilhelm → Baynes** (Cary F.), **3rd ed. ca. 1967–1971**, **eine** große PDF-Datei mit bibliographisch klarem Umfang (ca. **700+ Seiten**). In der Trefferliste: z. B. **`The I ching; or, Book of changes_123862961`** oder **`_123768270`** (zlib, Princeton, lxii+740 S.) **oder** **`nexusstc/.../f53e2237935cf72214e6a2bcb0ad5b95.pdf`** (~23 MB) — **vor Download** Dateigröße/Beschreibung mit „3 books“, „commentaries“, „Ten Wings“ abgleichen.  
   - **Alternativ robust:** `ia/ichingorbookofc00wilh.pdf` (Routledge & Kegan Paul **1950**, sehr ausführliches Inhaltsverzeichnis im Snippet) — wenn die Datei vollständig und gut OCR-tauglich ist.  
   - **E-Book statt PDF:** Princeton-**EPUB** 1967/1971 (z. B. `069109750X_The.epub` oder `nexusstc/.../29ee70af8c8770cd40a81c385d1c85df.epub`) — für Lesen ok; **MinerU/Pipeline** bevorzugt oft **PDF**.  
   - **Nicht** als K2-Primäranker: **Pocket**-Ausgaben, **stark gekürzte** Scans, **„Gary F. Baynes“**-Tippfehler-Metadaten (unsauber), Dateien **unter 1 MB** mit vollem Titel (meist Fragment), **chenjin5**/fragliche **MOBI/EPUB** mit ❌-Hinweis, **DJVU** (nur wenn ihr bewusst konvertiert).

4. **I Ging — Zusatzwerk (K3, nicht Ersatz des Orakeltexts):** **`Understanding the I Ching: The Wilhelm Lectures on the Book of Changes`** (Hellmut + Richard, Princeton **1995** o. ä.) — z. B. zlib **`119130701`** oder **`119118554`** oder **`d7ccdfc52e41f03909ad6b37e83ee89a`**; **getrennt** speichern und mit `component: secondary_commentary` taggen.

5. **I Ging — `text_line: legge` (P1):** **Dover**-Reprint *Sacred Books of the East* XVI, z. B. **`The I ching_123761840.pdf`** (1963, ~27 MB) **oder** die Chai-ed. **University Books 1964** (`I ching; Book of changes_121162061`) — **nicht** Treffer, bei denen der Metadatenblock eindeutig **Tao Te Ching** / falsches Werk ist.

6. **Spanisch** (`Yi king : libro de las mutaciones`, Mexico 1999): **optional** zweite Datei für **`language: es`** + `text_line: wilhelm_spanish` — nur wenn ihr spanische K3/K4 im KG wollt; **nicht** statt der englischen Bollingen-Basis.

**Rationale:** K2-Anker muss **eindeutig reproduzierbar** und **vollständig** (Hexagramme + traditionelle Schichten) sein; Dubletten und Schrott-Treffer verwässern Provenance. Split Kabbalah war in `ontology_policy.md` begründet; Chakra bleibt ein Graph bis zur Evidenz des Gegenteils.

**Consequences:** `entity_registry_iching_v01.json` (o. ä.) mit `known_works`-Einträgen inkl. **AA-MD5** nach verifiziertem Download; `literature_canon_by_scope.md` §6.1 um **„gewählte Referenzdatei“** ergänzen sobald MD5 feststeht; Toolkit/VM-Profil `iching_content` später analog HD.

---

**Decision:** Der Rechenmodus `hybrid_design_tropical_personality_sidereal` (`compute_profile.hd`, `cursor/contracts.md` §13) heißt in **UI und Doku** **EarthStar Human Design**. Technische Keys und `system_id: 'hd'` unverändert; Anzeigename in §13-Tabelle.

**Rationale:** Verständlicher, markenfähiger Name innerhalb von IC; klare Abgrenzung zu Jovian-„offiziell“; API bleibt stabil über Enum.

**Consequences:** Copy, Consent-Banner für Erstnutzung, Hilfetexte; Side-by-Side- und Dropdown-Spezifikation in `reference/hd_compute_profiles_kg_and_roadmap.md` §6.1.

---

## 2026-05-06: Human Design — Rechenmodi ohne neues `system_id` (`compute_profile`)

**Decision:** Unterschiedliche astronomische Konventionen für HD (**tropical Ra/Jovian-Standard**, **sidereal**, **Hybrid Design/Persönlichkeit**) werden **nicht** als extra `system_id` modelliert. Stattdessen bleibt **`system_id: 'hd'`**; der Modus steckt in **`compute_profile.hd`** (siehe **`cursor/contracts.md` §13**): `zodiac_mode`, optional `sidereal.ayanamsha`, `backend` (Swiss Ephemeris + Engine-Paket/Version).

**Rationale:** Canonical IDs (`hd.gate.N`, …) sind **eine** Ontologie; mehrere Modi ändern **aktivierte Teilmengen**, nicht die Bedeutungs-Adressierung. So bleiben KG-Seed und Literatur an **denselben** Knoten hängbar; Vergleichbarkeit von Charts ist über **`compute_profile`** explizit und API-neutral.

**Consequences:** Chart-Snapshots und Engine-Requests müssen **`compute_profile`** persistieren; UI und Vergleiche (Composite etc.) nur **innerhalb desselben Profils**. Detailplan und K1–K4-Einordnung: **`reference/hd_compute_profiles_kg_and_roadmap.md`**.

---

## 2026-04-16: Nine Star Ki — K1/K2 v1 (Tabellen, Sonnenmonate, energetischer Stern)

**Decision:** `@ic/engines` **Nine Star Ki** auf **v1** gehoben: **Honmei** weiter aus **Ki-Jahr** (lokaler **4. Feb.**-Grenze) mit **Jahres-Stern-Overrides** wo die einfache Ziffernregel von Standardtabellen abweicht; **Sonderfall** Geburt **Gregorianisch 1986** mit **Ki-Jahr 1985** → Honmei-Basisjahr **1984** (übliche Sonoda/Tabellenkorrektur). **Getsumei** nicht mehr über `wrap9(Honmei − Monatsindex)`, sondern über **12×9-Monatsmuster** (inkl. Anomalie Hauptstern 5 Okt–Dez). **Dritter Stern (energetic / 81er-Tabelle)** aus **(Honmei, Getsumei)**. **Sonnenmonate** als **12 feste Monat/Tag-Schnitte** (Li Chun 4. Feb. … Kleine Kälte 6. Jan.), **ohne** exakte Solar-Term-Uhrzeit.

**Rationale:** Die alte Differenzformel für den Monatsstern ist **fachlich nicht** deckungsgleich mit gängigen japanischen NSK-Tabellen (z. B. Hauptstern 5); K1/K2 sollen **stabil** und **gegen Lehrmittel prüfbar** sein. Tabellen sind klein und deterministisch.

**Klarstellung — HD-Minuten vs. NSK-Sonnenterme:** Human Design nutzt den Geburts**moment** (Ephemeris, Minuten-relevant für Gates/Profil usw.) — dafür ist **präzise lokale Wandzeit + Zone** nötig. Die **Jieqi**-Grenzen (Li Chun, Jing Zhe, …) für Nine Star Ki fallen astronomisch jedes Jahr auf eine **andere Uhrzeit** (nicht automatisch Mitternacht lokaler Zivilzeit). NSK **v1** arbeitet deshalb mit **festen Kalender-Schnitten** (4. Feb., 6. Mrz., …) — eine dokumentierte **K1-Approximation**. Das ist **kein** „einfach dieselbe Swiss-Ephemeris wie HD aufmachen“: man müsste explizit **Solar-Term-Module** (oder Ephemeris-Queries) pro Jahr/Zone fahren → **v2+** / `tradition`. HD-Zeitfelder **kann** die App überall sammeln; sie **ersetzen** ohne diese Zusatzlogik **nicht** die NSK-Term-Uhren.

**Consequences:** Chart-Nodes inkl. `nsk.energetic_star.{1–9}`; Vitest **Step 3** (`nine-star-ki-catalog-validation.test.ts`); Katalog-Meta `schema_version` 1.0.1. Optional später: exakte Li-Chun-Zeit pro Zeitzone → v2 / `tradition`.

---

## 2026-04-16: Maya Tzolkin — v1 (lokales Zivildatum aus aufgelöstem Instant)

**Decision:** Engine **`ic_maya_tzolkin_v1`**: Der **Tzolkin-Tag (Kin)** bezieht sich auf das **lokale Zivilkalenderdatum** in `birth.timezone`, abgeleitet aus dem mit **`utcMillisForWallTimeInZone`** aufgelösten UTC-Instant (gleiche Pipeline wie HD/BaZi). **Ein Kin pro lokalem Ziviltag**; kein Haab/Long Count in v1.

**Rationale:** Konsistente Nutzung von Datum, Uhrzeit und IANA-Zone; vermeidet stillschweigende Abweichungen, falls Eingaben und Zone formal zusammenpassen sollen; für typische Geburtsurkunden-Eingaben identisch zum bisherigen reinen `YYYY-MM-DD`-Parse.

**Consequences:** `raw.gregorian_date` = aufgelöstes `YYYY-MM-DD`; Vitest **Step 3** `maya-tzolkin-catalog-validation.test.ts` (Nodes + Konsistenz zur `kins`-Zeile im Katalog); `mayan_tzolkin_catalog_v0.json` Meta `schema_version` 1.0.1.

---

## 2026-04-20: Phase-1 „triviale“ Systeme — v0-Schulwahl (Maya, NSK, Numerologie, Akan)

**Decision:**

| `system_id` | v0 Berechnungsbasis (K1/K2) | K3/K4 / später |
|-------------|------------------------------|----------------|
| **mayan_tzolkin** | **260-Tage-Tzolkʼin** mit **GMT-Korrelation** (JDN-Anker **584283** = klassischer „0.0.0.0.0“-Tag); Siegel-**Slugs** wie im Deskriptor (**Dreamspell-/Arguelles-Namen**: `red_dragon` … `yellow_sun`), weil `canonical_id` darauf ausgelegt ist — explizit **nicht** identisch mit rein akademischer „Imix/Ik“-Benennung in der UI. Wellen/Castle: **Dreamspell-Raster** (13er-Wavespell, 5×52 Burgen). | „traditional_mayan“ / andere Correlations nur als **zweiter Pfad** / `tradition`. |
| **nine_star_ki** | **Japanisches Nine Star Ki** (Sonoda-Linie). **Ausführung K1/K2:** siehe **2026-04-16** (Engine `ic_nine_star_ki_v1`: Overrides + ggf. 1986→1984, **Monatsmuster**, **energetischer Stern**, feste **Sonnenmonats-Schnitte**). Die Zeile unten beschrieb die **frühere v0-Näherung** (nur noch historisch). | Exakte Li-Chun-Uhrzeit / weitere Schulen → v2+ / `tradition`. |
| **numerology** | **Pythagoreische** Buchstaben-Zuordnung (1–9-Zyklus); **Life Path** aus Geburtsdatum; optional **Destiny / Soul Urge / Personality**, wenn `full_name` mitgegeben wird. **Chaldeisch / Kabbalah** → später / andere `tradition`. | Meisterzahlen 11/22/33 wie üblich; Karmic Debt aus Teilstrings → v0 minimal oder v1. |
| **akan** | **Ghanaische Krada-Namenslogik** nach **Wochentag der Geburt** (Wandzeit in `birth.timezone`); Zuordnung **Sonntag=Kwasi/Akosua** … **Samstag=Kwame/Amma** (weit verbreitete Standardtabelle). **Obosom / Adaduanan** → v1 (Literatur-K2). | Varianten `akan_calendar` / `adaduanan` später. |

**Rationale:** Eine klare v0-Linie pro System für **stabile** `canonical_id`s und Konvergenz; transparenzfreundlich für Nutzer:innen; Literatur- und Schulbreite bleibt an K3/K4 und Linsen.

**Consequences:** `@ic/engines` + minimale `*_catalog_v0.json`; UI-Copy „IC v0 rechnet …“; Tests gegen feste Referenzdaten wo möglich.

---

## 2026-04-19: Konvergenz (Person vs. strukturell); v0 „modern“ vs. „traditionell“; Einzel-Linsen

**Decision:**

1. **Zwei gleichberechtigte Wege zu „Klumpen“ / Meta-Einheit im KG:**  
   - **Personengebunden:** Dieselbe Person liefert für mehrere `system_id` aktivierte Teilgraphen; Konvergenz entsteht aus **Überschneidung und Kanten** zwischen den **personbezogenen** Chart-Knoten (starker App-Anker, intuitive UX).  
   - **Personen-unabhängig (strukturell):** Ur-/Grundsysteme und Element-Raster (I Ging, Kabbalah, Chakren, Wu Xing, Pancha Bhuta, westliche Elemente, …) bilden **ohne Geburtsereignis** eigene **Struktur-KGs**; **Klumpen** entstehen über **Cross-System-Kanten** (`maps_to`, `cross_system`), **Embeddings + LLM-Review** und später Meta-Knoten (Datenschicht E) — also **Ontologie-Konvergenz**, nicht nur „gleicher Geburtstag“.

2. **Beides zusammen:** Strukturelle Klumpen **können und sollen** schon in v0 vorbereitet werden (Deskriptoren, Kataloge, erste Kanten); **personengebundene** Konvergenz nutzt dieselbe Kanten-Infrastruktur, sobald Charts existieren.

3. **v0 bei rechenbaren „kleineren“ Systemen (Maya Tzolkin, Nine Star Ki, Numerologie, Akan, …):** Pro `system_id` **genau eine** K1/K2-Berechnungskonvention (eine Correlation / eine Tabellenlogik), damit **Knoten stabil** und **Vergleiche** zwischen Systemen **interpretierbar** bleiben. **Priorität v0:** **gut dokumentierbar + implementierbar + für die erwartete App-Zielgruppe nachvollziehbar** — das tendiert bei **Tzolkin** oft zur **modernen, explizit benannten Linie** (z. B. **Dreamspell / Arguelles**), bei **NSK/Numerologie** zu **einer** klar benannten Schul- bzw. Tabellenvariante (jeweils in Doku/Copy genannt). **„Traditionell“** in v0 primär über **K3/K4** (Literatur, `tradition`, `werk_kategorie`) und **Linsen**, **nicht** als zweiter paralleler Rechenmotor ohne UI-Klarstellung.

4. **Nutzer:innen, die ein System einzeln sehen wollen:** **System-Linsen** bleiben zentral; die v0-Rechenwahl ist **transparenter technischer Default** („IC rechnet v0 so und so“), **kein** Anspruch auf die einzig gültige spirituelle Linie. Roadmap: zweite Rechenvariante / zweite Correlation nur mit **eigenem Scope** (Lens oder `tradition`-Parameter), nicht als stiller Mix.

**Rationale:** Schnittmengen- und Meta-Analysen brauchen **stabile** strukturelle Identitäten; parallele Schulen ohne Modell würden den Graphen **zersplittern**. Strukturelle Klumpen liefern **Wissen über Muster** unabhängig von Geburtsdaten. Modern-vs-traditionell ist bei **K1/K2** eine **Produkt- und Lieferentscheidung**; bei **K3/K4** bleibt Raum für **traditionelle** Tiefe und Mehrstimmigkeit.

**Consequences:** Engines + Kataloge: ein Pfad, Tests, kurze Nutzer:innen-sichtbare Erklärung; KG- und Pipeline-Arbeit an Ur-/Element-Systemen parallel zu Chart-Engines; spätere Schul-Erweiterungen explizit scoped (Doku + Schema), nicht implizit.

---

## 2026-04-18: Gene Keys — Literatur wie alle anderen Systeme

**Decision:** Gene Keys erhält **keine** gesonderte Copyright-/Paraphrase-Policy in den technischen Projekt-Dokumenten. Literaturbeschaffung, Chunking und Extraktion (K3/K4) laufen über dieselbe Pipeline- und Profil-Logik wie bei allen anderen `system_id` (inkl. Quellenprofil / `entity_registry` nach Bedarf).

**Rationale:** Phase-1-Playbook und Datenmodell sind systemagnostisch; Sonder-Doku würde nur Verwirrung erzeugen und suggerieren, dass GK technisch anders behandelt wird — tut es nicht (`gk.*` bleibt eigenständiges Präfix, shared K1 mit HD).

**Consequences:** `cursor/status.md` und `cursor/engines.md` ohne GK-Sonder-Copyright-Abschnitte; rechtliche Fragen pro Verlag/Lizenz bleiben außerhalb der Engine-Doku, wie bei jedem System.

---

## 2026-02-16: Dokumentations-Architektur (Zweischicht)

**Decision:** Cursor-Docs (6 Dateien, < 300 Zeilen, rein technisch) getrennt von Reference-Docs (PRD, Entscheidungen, Ideen, Inspirationen).

**Rationale:** Cursor braucht technische Wahrheit ohne Vision-Ballast. Der Mensch braucht den größeren Kontext. Zwei verschiedene Leser = zwei verschiedene Doc-Sets.

**Consequences:** cursor/ Ordner wird in Cursor-Rule referenziert. reference/ wird nur bei explizitem Verweis gelesen. Alte Docs → 99_archive/.

---

## 2026-02-16: 10 statt 8 Lebensbereiche

**Decision:** Sexualität & Intimität und Beziehungen & Community als eigenständige Bereiche.

**Rationale:** Bei 8 waren Sexualität in "Partnerschaft" und Community in "Familie" versteckt. Jedes System hat zu beiden Themen eigenständige, substantielle Aussagen (HD Sakral/Intimität, BaZi Peach Blossom, Astro 8.Haus). 10 Segmente im Kreis = 36° pro Segment, visuell sauber.

**Consequences:** life_domain Enum hat 10 Werte statt 8. Mandala hat 10 Segmente. Kein Schema-Impact (Tag, nicht Constraint).

---

## 2026-02-16: Mandala als Signatur statt Radar-Chart mit Tiefe

**Decision:** Die persönliche Landkarte zeigt nicht "Beziehung ist wichtiger als Beruf" (Tiefe-Metapher), sondern den gesamten visuellen Abdruck als einzigartige Signatur.

**Rationale:** Tiefe impliziert Bewertung. Die Form des Kompass IST die Signatur — asymmetrisch, einzigartig, ohne Wertung. Äußere Silhouette = Dichte der Chart-Elemente. Farbe = Systemübereinstimmung. Leuchtende Akzente = zeitliche Aktivität.

**Consequences:** Kein "Score" pro Lebensbereich nötig. Stattdessen: Zählung der Chart-Elemente pro Bereich + Farbkodierung. SM-teilbar als Fingerabdruck.

---

## 2026-02-16: Fluss-Diagramm als separater Visualisierungsmodus

**Decision:** Neben dem Mandala (WAS habe ich) ein Fluss-Diagramm (WIE hängt es zusammen), inspiriert vom Gene Keys Hologenetic Profile.

**Rationale:** Mandala = räumlich, statisch, Exploration. Fluss-Diagramm = prozesshaft, dynamisch, Narrativ. Verschiedene Fragen → verschiedene Visualisierungen.

**Consequences:** Fluss-Diagramm ist Phase 2-3 (braucht Schicht D für Cross-System-Flüsse). Premium-Feature.

---

## 2026-02-16: 15 statt 12 Dimensionen

**Decision:** 3 neue Keys: elemental_quality, temporal_phase, destiny_pattern.

**Rationale:** BaZi (Wuxing), Jyotish (Dashas), Maya (Farben) brauchen diese Dimensionen. Ohne sie sind 30%+ der System-spezifischen Bedeutungen nicht abbildbar.

**Consequences:** Nullable jsonb-Feld, keine Breaking Change. Alte Daten bleiben gültig. Pipeline-Prompts anpassen. 11 Kern-Dimensionen (user-facing), 4 ergänzende (system-spezifisch).

---

## 2026-02-16: Drei Sprachebenen (Wording-Strategie)

**Decision:** System-Ebene (Original-Terminologie), Meta-Ebene (eigenes Wording für übergreifende Konzepte), Handbuch-Ebene (Alltagssprache).

**Rationale:** Copyright-Schutz (Not-Self, Useful God sind geschützt). Verständlichkeit (Fachtermini unverständlich für Laien). Synthese-Mehrwert (wenn 3 Systeme dasselbe beschreiben, braucht es einen eigenen Begriff).

**Consequences:** Wording entsteht als Nebenprodukt von generate_meta_nodes. LLM schlägt vor, Mensch finalisiert.

---

## 2026-02-16: Keine Entwicklungsstufen (anti-AQAL)

**Decision:** Keine hierarchische Bewertung ("du bist auf Stufe X"). Stattdessen: Zeitlinie (Phasen statt Stufen).

**Rationale:** Keines der integrierten Systeme kennt Entwicklungshierarchie. Generator ≠ "höher" als Projektor. Stufen implizieren Bewertung. Inner Compass spiegelt, bewertet nicht.

**Consequences:** Zeitlinie-Layer (Schicht C) ersetzt Stufen. Dynamische Aktualisierung statt statische Einordnung. AQAL-Quadranten als interner Qualitätscheck nutzbar (decken unsere Dimensionen alle 4 Perspektiven ab?).

---

## 2026-02-16: System-Filter als Linsen-Metapher

**Decision:** User kann zwischen "Alle Systeme" (Standard) und Einzelsystem-Linsen umschalten.

**Rationale:** Bedient 3 Zielgruppen: System-Kenner, kulturspezifische Nutzer, Einsteiger. Strategischer Nebeneffekt: Erster Cross-System-Switch wird zum größeren Aha-Moment.

**Consequences:** Trivial (system_id-Filter auf allen Queries). Handbuch-Sprache wechselt von Meta auf System-Ebene.

---

## 2026-02-16: Prozess-Layer mit 4-Schritt-Struktur

**Decision:** Erkennen → In Beziehung treten → Verstehen → Integrieren (inspiriert von IFS, ohne dessen Terminologie).

**Rationale:** IFS ist therapeutisch validiert, gibt Chart-Elementen einen konkreten Arbeitspfad. HD sagt "lebe dein Design" (vage). Wir sagen "hier sind 4 Schritte" (konkret).

**Consequences:** Neues process-Feld im Interpretations-Contract (trap, gift_activation, experiment_seed). Neuer Pipeline-Job: extract_process_patterns. Handbuch-Schicht 3+4 werden damit gefüllt.

---

## 2026-02: Postgres+pgvector statt ArangoDB/Neo4j

**Decision:** Bleiben bei Supabase/Postgres. pgvector für Embeddings.

**Rationale:** Supabase bietet Auth, RLS, Storage, Realtime. Kein separater Graph-DB-Server nötig. Edges sind eine Tabelle, Nodes sind eine Tabelle — das reicht für unsere Größenordnung.

**Consequences:** Kein Graph-Traversal-Performance-Vorteil. Wenn jemals Millionen Nodes: exportieren. Für jetzt: Einfachheit > Performance.

---

## 2026-02: Strukturbäume aus Deskriptoren, NICHT aus PDFs

**Decision:** Systemstruktur (welches Gate in welchem Center) aus JSON-Deskriptoren + Engine-Code. NICHT aus PDF-Extraktion.

**Rationale:** Struktur ist deterministisch und fest. PDFs beschreiben Interpretationen, nicht Struktur. "Gate 34 ist im Sakral-Zentrum" ist eine Tatsache, keine Interpretation.

**Consequences:** Phase 0 = Seed-Script (Deskriptor → Nodes + Edges). PDFs reichern Nodes an, erzeugen sie nicht. Graph existiert BEVOR erste PDF verarbeitet wird.

---

## 2026-02: Embeddings für Cross-System-Mapping statt manuell

**Decision:** Cosine Similarity + LLM-Validierung statt manuelles Kuratieren.

**Rationale:** Skaliert auf beliebig viele Systeme. 50 manuelle Mappings als Startpunkt, dann automatisch. LLM + Embeddings ersetzen manuelles Kuratieren komplett.

**Consequences:** pgvector Pflicht. extract_cross_mappings Job. Review-Status-Feld auf Edges. Human Review bleibt Option (approved/rejected), aber nicht Pflicht.

---

## 2026-02: 4-stufige Extraktion statt ein LLM-Call

**Decision:** extract_entities + extract_meanings + extract_relationships + extract_processes statt alles in einem Prompt.

**Rationale:** Verschiedene Wissensebenen (Fakten vs. Bedeutungen vs. Beziehungen vs. Prozesse) brauchen verschiedene Prompt-Strategien. Ein Call vermischt diese Level.

**Consequences:** 4x so viele LLM-Calls. Aber: Bessere Qualität, sauberere Daten, leichter debuggbar.

---

## 2026-02-16: Zwei-Gate-Filtering für Content-Akquise

**Decision:** Breit scrapen, dann zweistufig filtern statt strenge Keyword-Filter.

**Rationale:** Anna's Archive Scraping produziert ~85% Noise (z.B. "UX Design" bei Suche nach "human design"). Einfache Keyword-Filter sind zu aggressiv — Nischen-Themen wie "Projector Empowerment", "Pfeile", "Liebe im HD" fallen raus. Stattdessen: Gate 1 = leichtgewichtige LLM-Vorklassifikation auf Titel+Metadaten (vor Download), Gate 2 = volle Inhaltsklassifikation nach MinerU-Extraktion (im Worker).

**Consequences:** Kein manuelles Kuratieren nötig. Noise wird automatisch erkannt. Nischen-Themen kommen durch. Admin-Review-Queue für Grenzfälle (Confidence 0.3–0.6). Kein Stub im Produktivbetrieb.

---

## 2026-02-16: Clean Data Restart (keine alten HD-Daten übernehmen)

**Decision:** Bestehende hd_assets/hd_asset_chunks/hd_interpretations in Cloud-DB NICHT migrieren. Sauberer Neustart mit sys_*-Schema.

**Rationale:** Bisherige Daten: 85% Noise in Assets, alle Interpretations sind Stubs ("mvp_stub", system: "other"), Ingestion-Jobs nur noch failed extract_interpretations. 113 PDFs sind schnell neu prozessiert — und diesmal richtig (mit echtem LLM, ohne Noise, mit Pre-Filtering). Schema ändert sich komplett (hd_* → sys_*).

**Consequences:** Lokale DB: supabase:web:reset löscht alles. Cloud: manuell bereinigen. Kein Datenverlust (alles war Stub/Noise). Anna's Archive Pipeline mit verbessertem Filtering neu durchlaufen.

---

## 2026-02-16: Verarbeitung pro System, in Wellen

**Decision:** Systeme nacheinander verarbeiten (HD → Gene Keys → Astro → BaZi → ...), nicht alle gleichzeitig.

**Rationale:** Pro-System ermöglicht Qualitätsvalidierung, Noise-Erkennung und Pipeline-Tuning. Kein Bias-Risiko, da jedes System eigene Wissensbasis aufbaut und Cross-System-Mappings erst in P4 kommen.

**Consequences:** HD als erstes System (größtes Corpus, am besten validierbar). Erkenntnisse aus HD-Verarbeitung fließen in Pipeline-Optimierung für Folgesysteme.

---

## 2026-02-16: Clean Inner Compass statt hd_*-Patch

**Decision:** Frischen Makerkit-Stand pullen, dann sauberen Inner Compass Teil (Schema, Worker, Scripts) neu aufsetzen. Kein String-Replace auf 2400 Zeilen altem Worker.

**Rationale:** 10 Migrations → 1-2 saubere (sys_* + pgvector + neue Felder von Tag 1). Worker referenziert direkt sys_*. Kein Legacy-Code. Wissen/Patterns aus altem Worker werden übernommen, aber Code neu geschrieben.

**Consequences:** Alter Worker (hd_worker_mvp.py) bleibt als Referenz. Makerkit-Framework (Auth, Accounts, RLS, UI-Shell) bleibt wie es ist. Nur der projektspezifische Teil wird neu.

---

## 2026-02-16: Interpretation-zentrierter Ansatz statt NVIDIA-style Triple-Extraktion

**Decision:** Bedeutungs-Extraktion (15 Dimensionen pro Chunk, ~1000 Tokens) statt starre Triple-Extraktion (Subject-Predicate-Object per 512 Zeichen wie NVIDIA text2kg Playbook).

**Rationale:** NVIDIA text2kg ist NER+RE für faktische Domänen (News, Finance) mit festen Entity-Typen (ORG, PERSON) und 15 Relationsverben. Esoterische Texte brauchen Kontext für Bedeutung — 512-Zeichen-Chunks reißen das auseinander. Unsere Dimensions-Struktur (shadow, gift, archetype...) fängt mehr auf als flache Triples. Text2kg kommt danach deterministisch.

**Consequences:** Kein NVIDIA-Pipeline-Klon. Eigene Ontologie (Gate, Center, Stem, Archetype). Eigene Relationsverben (symbolisiert, korrespondiert_mit, aktiviert). Chunk-Größe bleibt ~1000 Tokens. Von NVIDIA übernehmen: Pipeline-Architektur, ggf. cuGraph für spätere Graph-Analytik, LoRA Fine-Tuning als Option.

---

## 2026-02-16: pgvector bestätigt als richtige Lösung

**Decision:** Postgres+pgvector für Embeddings und Cross-System-Mapping. Kein separater Vector-DB-Server.

**Rationale:** Supabase hat pgvector-Extension bereits. Für ~500-5000 Nodes mehr als ausreichend. Einziger Zweck: Cosine Similarity für Cross-System-Mapping-Kandidaten (Schicht D). Kein Pinecone/Weaviate/Qdrant nötig.

**Consequences:** `sys_kg_nodes.embedding vector(1536)` + ivfflat-Index kommt in Schema-Migration. text-embedding-3-large oder lokales Modell auf Spark.

---

## 2026-02: LLM-Wahl: Qwen3-32B als Default

**Decision:** Qwen3-32B als primäres Extraktions-/Synthesis-Modell auf Spark.

**Rationale:** Multilingual (100+ Sprachen), JSON/Structured Output, Apache-2.0 Lizenz, läuft bereits als NVFP4 auf Spark. BaZi-Quellen (Chinesisch) und Jyotish-Quellen (Sanskrit) profitieren von Mehrsprachigkeit.

**Consequences:** DeepSeek R1 8B als Alternative wenn Content zu stark gefiltert wird. A/B-Test mit 5-10 Chunks empfohlen bei Model-Wechsel. Model-Switcher erlaubt Wechsel ohne Code-Änderung.

---

## 2026-02: Deep Structure Seed = Backlog, nicht Sprint

**Decision:** Strukturvertiefung (832 → ~2000 Nodes) erfolgt demand-driven, nicht als Block vor S5.

**Rationale:** 832 Nodes (HD: 526, alle 10 Systeme) reichen vollständig für S5-Validierung. Wenn vor der Pipeline-Validierung 15-20h Daten kuratiert werden, blockiert das den kritischen Pfad. Falls S5 Contract-Anpassungen erfordert, müssten kuratierte Daten ggf. nochmal angefasst werden.

**Consequences:** S5 startet sofort mit bestehendem Graph. Fehlende Nodes werden erst nachgezogen wenn die Pipeline sie tatsächlich vermisst. Vollständiger Backlog in `reference/deep_structure_plan.md`. HD-Vertiefung (Crosses, PHS, Partners) nach S7 in P1.

---

## 2026-01: Schema hd_* → sys_* (Clean Restart)

**Decision:** EINE saubere Migration statt 10 Patches. 10 Tabellen mit sys_* Präfix.

**Rationale:** Kognitiver Overhead: hd_kg_nodes liest sich als "HD" statt "Meta-System". Technische Schuld: 10 Migrations-Dateien. pgvector von Anfang an.

**Consequences:** ~2-3 Tage Aufwand. Infra bleibt (Spark, Worker, MinerU). Nur Tabellennamen + neue Felder.
