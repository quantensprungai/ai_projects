INNER COMPASS
Steuerungs- & Konzeptdokument  |  VERSION 5.0  |  25. Februar 2026
Living Document — Single Source of Truth  |  VERTRAULICH

"Jeder Mensch kommt mit einer einzigartigen Signatur zur Welt. Darunter liegen Schichten. Das Schälen lässt nichts verschwinden — es lässt sichtbar werden, was von Anfang an da war."
 
CHANGE-LOG
Version	Datum	Wesentliche Änderungen
v1	25.02.26	Erstkonsolidierung PRD v3 + Master v2 + Strang 0. E-01–E-13.
v2	25.02.26	E-14–E-24, OE-01–OE-11. Zeitmodell 4 Dimensionen.
v3	25.02.26	E-25–E-30. Quellenstrategie, KG-Qualitäts-Layer, OE-12. Phasen-Ton + App-Trigger. Domäne×Phase Matrix. inner_strategy factor_scores. Story/Release-Architektur. Drei-Sprachebenen-Tabelle.
v4	25.02.26	E-31–E-40. OE-13/14/15 geschlossen. System×Ebenen-Architekturprinzip (E-36). HD-Enneagramm-Brücke (E-31). Zeitmodell-Hierarchie (E-40). Widerspruchs-Protokoll (E-39). Graduation (Kap. XIV). Karte≠Territorium (E-34). 7-Ebenen-Modell (E-35). System-Kernfragen (E-37). 3-Gruppen-Taxonomie (E-38).
v5	25.02.26	MERGE: v4-Struktur (E-01–E-40) + 5 wiederhergestellte operative Blöcke aus v3:
1. Phasen-Ton + App-Trigger (Kap. XI.1)
2. Domäne × Phase Matrix (Kap. XI.2)
3. inner_strategy factor_scores Schema (Kap. VI.1 → E-27)
4. Story/Release-Architektur + KI-Qualitätsprinzipien (Kap. XIX + E-30)
5. Drei-Sprachebenen-Tabelle + Lens-Switcher kombiniert (Kap. XVII)
6. NEU: System×Ebenen×Phase Mapping Table (Kap. V.5)
Alle OEs konsolidiert.

I. PROJEKT-IDENTITÄT & MISSION
I.1 Kern-Vision
Inner Compass integriert mehrere Weisheitssysteme (HD, BaZi, Westl. Astrologie, Maya/Tzolkin, Gene Keys u.a.) durch einen Knowledge-Graph zu einer personalisierten, entwicklungsorientierten Sprache für den Menschen. Kein System ist das „beste" — jedes beleuchtet präzise eine andere Ebene des Menschen.
I.2 Drei Stränge (E-01 — NICHT ÄNDERBAR)
Strang	Fokus	Leitdokument
Strang 0	Fundament / Philosophie / Genese	IC_Fundament (Living Doc) — ehem. „Strang0_Inner_Compass"
Strang 1	App & Produkt	IC_App (aus diesem Dok. abzuleiten) — ehem. „App-Leitdokument"
Strang 2	Buch / Vermittlung	IC_Vermittlung (geplant) — ehem. „Vermittlungs-Leitdokument"
Strang 3	Forschung	IC_Forschung (OE-12 → Forschungsdesign) — ehem. „Forschungs-Backlog"
I.3 Dokument-Hierarchie (korrigiert v4)
Ebene	Dokument	Beziehung
KERN (gleichrangig)	IC_Fundament ↔ IC_Leitdokument (dieses Dok.)	Gegenseitig informierend — beide bindend
PRODUKT	IC_App	Abgeleitet aus KERN
SPECS	PRD	Unterdokument von IC_App
VERMITTLUNG	IC_Vermittlung	Abgeleitet aus KERN (geplant)
FORSCHUNG	IC_Forschung	Abgeleitet aus KERN (geplant)
II. ETHIK & DESIGN-PRINZIPIEN
•	Kein Guru-Prinzip: IC schafft keine Abhängigkeit. Ziel: Empowerment zur Selbstnavigation.
•	Graduation: Es gibt ein explizites Konzept des "Fertig-Seins" (→ Kap. XIV).
•	Hypothesen-Sprache: IC sagt nie "Du bist X." Es sagt: "Dein Chart deutet auf X — erkennst du das?"
•	Invitational Language: Alle Reflexionsfragen sind einladend, nie direktiv.
•	Karte ≠ Territorium: IC zeigt explizit, was es sieht und was nicht (→ III.3 + E-34).
•	Wissenschaftliche Redlichkeit: IC liegt zwischen Esoterik und Wissenschaft — und hält diese Spannung aus.
•	Keine Diskriminierung: Kein System-Output darf für Ausgrenzung oder Pathologisierung verwendet werden.
•	KEIN Sucht-Design: Ziel ist Empowerment und letztlich Unabhängigkeit vom Tool.
•	Datensparsamkeit: Geburtsdaten lokal, Affect-Daten opt-in, Biografie löschbar.
•	Kulturelle Bescheidenheit: Kein System wird als "wahrer" dargestellt als andere.
III. PHILOSOPHISCHES FUNDAMENT
III.1 Die Vier Thesen
1. Zwiebel-These
Jeder Mensch hat eine Anlage/Signatur, die von Prägung/Konditionierung überlagert wird und durch bewusstes Erkennen zugänglich wird. Formulierung: "Drei beschreibbare Schichten + offener Kern." Die drei Schichten (Anlage → Prägung → Bewusstsein) sind beschreibbar. Der Kern (das Wesen selbst) bleibt offen, nicht definiert, nicht gemessen.
2. Multi-Spiegel-These
Multiple, kulturell unabhängige Geburtssysteme erzeugen reichhaltigere Selbstbilder als jedes Einzelsystem. Die Differenz zwischen Systemen ist ebenso wertvoll wie die Konvergenz.
3. Spiral-These
Selbsterkenntnis ist ein Prozess mit natürlichen Phasen und Spannungen, kein einmaliger Moment. Das System bildet diesen Prozess ab, beschleunigt ihn aber nicht künstlich.
4. Resonanz-These
Wenn unabhängige Kulturen für denselben Geburtsmoment ähnliche Qualitäten beschreiben, ist das ein Phänomen, das ernst genommen werden sollte. Systeme wirken nicht durch Wahrheit, sondern durch Resonanz. Die Frage ist nicht: "Stimmt das?" Sondern: "Klingt das wahr genug, um hinzuschauen?"
III.2 Zwiebel-Modell (vereinfachte Kommunikationsversion des 7-Ebenen-Modells)
•	Prägung (außen): Familie, Kultur, Erziehung, Trauma, Epigenetik.
•	Anlage / Signatur: Was Geburtssysteme beschreiben — die Karte.
•	Bewusstsein: Fähigkeit, Prägung und Anlage zu sehen und trotzdem zu wählen.
•	Offener Kern: Das Unbenennbare — wird von IC bewusst NICHT abgedeckt.
III.3 Zwillings-Problem — Grenzen geburtsbasierter Systeme
Zwei Menschen mit identischem Chart leben fundamental verschieden. Geburts-Disposition (Ebene 4) ist notwendig, aber nicht hinreichend. Fehlende Schichten (Epigenetik, Trauma, Bindung, freier Wille) werden von IC transparent kommuniziert.
III.4 Karte ≠ Territorium (E-34 — NEU v4 — Pflicht-Kapitel im IC_Fundament, früh, 3-teilig)
•	WAS IC SIEHT: Anlage/Disposition (Ebene 4), psychodynamische Muster (Ebene 3/5), Entwicklungsrichtung (Ebene 2–6).
•	WAS IC NICHT SIEHT: Freier Wille, Trauma-Überlagerungen, transgenerationale Muster, Bewusstsein jenseits der Geburt.
•	WARUM DAS KEIN FEHLER IST: Ein Spiegel, der einen Aspekt klar zeigt, ist wertvoller als einer, der alles zeigen will und nichts klar zeigt.

Leitspruch: "Die Systeme geben dir die SPRACHE — aber das Gelebte bist du."
IV. DAS 7-EBENEN-PERSPEKTIV-MODELL (E-35 — OE-15 GESCHLOSSEN)
Orientierungswerkzeug im IC_Fundament. Beantwortet: "Welche Systeme schauen auf welche Seite des Menschen?" KERNREGEL: Ein Mensch ist immer auf ALLEN Ebenen gleichzeitig. Die Ebenen sind Perspektiven, KEINE Entwicklungsstufen.
Ebene	Bezeichnung	Frage	Primäre Systeme in IC
7	Transzendent / Seelenpfad	Wozu bin ich hier?	Jyotish, Maya (Galakt. Ton), HD-Inkarnationskreuz
6	Bewusstseinsentwicklung	Auf welcher Stufe?	Spiral Dynamics, Gene Keys (Siddhi)
5	Psychodynamik / Innere Struktur	Welche Wunde formt meinen Filter?	Enneagramm (Kernwunde), IFS-Konzepte
4	Geburts-Disposition	Was ist mein Design?	HD (Gates/Typ), Westl. Astro, BaZi (Day Master), Maya (Kin)
3	Körper / Konstitution	Wie funktioniert mein Körper?	HD (PHS/Variables), Ayurveda, TCM
2	Kognition / Funktion	Wie denke ich?	MBTI, Big Five, BaZi-Elemente (Klasse C)
1	Verhalten / Oberfläche	Was ist außen sichtbar?	DISC, Stärken-Tools (Randständig)
IV.1 Abgrenzung zu anderen Modellen
Modell	Kernfrage	Richtung	Verortung
A — 5 Navigationsachsen	Wie navigiert der User?	Raum	App-UI
B — 7 Phasen / Heldenreise	Wann ist der User wo?	Zeit (vorwärts)	App-Journey + Fundament
C — 4 Handbuch-Schichten	Wie tief geht ein Element?	Vertikal	Handbuch/Inhalte
D — KG-Pipeline A→E	Wie denkt IC intern?	Außen → Innen	Technisch/KG
E — 7-Ebenen-Modell (dieses)	Was zeigt welches System?	Keine (Perspektive)	Fundament/Konzept
Querverweis: Die vollständige Architektur-Grammatik aller 5 Modelle — inklusive Eigenschafts-Tabellen, Detailtabellen pro Modell und Verwechslungsschutz (7 Phasen ≠ 7 Ebenen) — ist in IC_Fundament Kap. IV-A dokumentiert. Das Leitdokument enthält die operative Entscheidung (E-35); das Fundament enthält die philosophische Herleitung und den Verwechslungsschutz.
V. SYSTEM × EBENEN-MAPPING — Das Architekturprinzip (E-36 — NEU v4)
KERNPRINZIP: Kein System wird monolithisch einer Ebene zugeordnet. Jedes System hat Elemente auf mehreren Ebenen. KG-Regel: Jeder Knoten trägt ein verpflichtendes level_tag (1–7) zusätzlich zum system_tag.
V.1 Human Design
HD-Element	Ebene	Begründung
Inkarnationskreuz	7 (Transzendent)	Seelenpfad, Dharma
Gates & Kanäle (bew./unbew.)	4 (Disposition)	Kern-Charakteristik aus Geburt
Typ (MG/G/M/P/R)	4 (Disposition)	Energie-Strategie
Offene Zentren	3 + 5 (Körper + Psychodyn.)	Konditionierungsort — körperlich UND psychodynamisch
Definierte Zentren	4 (Disposition)	Stabile Charaktereigenschaften
PHS / Variables	3 (Körper/Konstitution)	Ernährungs- und Wahrnehmungsstrategie
Autorität	4 (Disposition)	Entscheidungsmodus
Profil (Linie)	4 + 7	Rolle (4) + Lebensthema (7)
Nicht-Selbst-Thema	5 (Psychodynamik)	Konditionierungsmuster im Alltag
V.2 Westliche Astrologie
Astro-Element	Ebene	Begründung
Nordknoten / Südknoten	7 (Transzendent)	Seelenpfad, karmische Richtung
Sonnenzeichen	4 (Disposition)	Kern-Identität
Mondzeichen	5 (Psychodynamik)	Emotionale Muster, innere Reaktionen
Aszendent	1 (Oberfläche)	Äußere Wirkung
Chiron	5 + 3 (Wunde/Körper)	Verwundung und Heilungspotenzial
Saturn	5 (Psychodynamik)	Struktur, Grenze, Konditionierungsmuster
V.3 BaZi
BaZi-Element	Ebene	Begründung
Day Master	4 (Disposition)	Kern-Charakter
Luck Pillars	4 + Zeitlich	Disposition in Zeitphasen
Clashing Pillars	5 (Psychodynamik)	Konfliktmuster
Nützliche Götter	7 (Transzendent)	Idealer Entwicklungspfad
Jahrespfeiler	1 (Verhalten)	Timing, sichtbares Verhalten
Element-Konstitution	3 (Körper)	Elementare Gesundheit
V.4 Gene Keys / Enneagramm / Maya
Element	System	Ebene	Begründung
Schatten (Shadow)	Gene Keys	5 (Psychodynamik)	Unbewusstes Muster
Geschenk (Gift)	Gene Keys	2–4	Gelebte Stärke
Siddhi	Gene Keys	6–7 (Bewuss. + Transzend.)	Höchstes Potenzial
Triade (Kopf/Herz/Körper)	Enneagramm	3 + 5	Konditionierungszentrum — aus HD ableitbar
Typ (1–9)	Enneagramm	5 (Psychodynamik)	Überlebensstrategie, Kernwunde
Galaktischer Ton	Maya	7 (Transzendent)	Kosmischer Auftrag
Geburts-Kin	Maya	4 (Disposition)	Kern-Signatur
V.5 System × Ebenen × Phase Mapping Table (NEU v5)
Diese Tabelle verknüpft erstmals System-Elemente, Ebenen (E-36) und Phasen (E-20) in einer einzigen Referenz. Sie dient als Import-Vorlage für das KG-Schema.
System	Element	level_tag	phase_tag (primär)	dynamic_type	domain_tag (Beispiel)
HD	Typ (MG/G/M/P/R)	4	1	static	1 Identität
HD	Offene Zentren	3+5	4	trap	2 Emotionen
HD	Inkarnationskreuz	7	7	static	9 Spiritualität
HD	PHS / Variables	3	3	static	3 Körper
HD	Autorität	4	5	static	1 Identität
HD	Profil	4+7	1–2	static	1 Identität
HD	Not-Self-Thema	5	4	trap	2 Emotionen
BaZi	Day Master	4	1	static	1 Identität
BaZi	Luck Pillars	4	5	phase_cycle	7 Arbeit
BaZi	Clashing Pillars	5	4	trap	4 Familie
BaZi	Nützliche Götter	7	7	growth_path	9 Spiritualität
BaZi	Element-Konstitution	3	3	spectrum	3 Körper
Astro	Sonnenzeichen	4	1	static	1 Identität
Astro	Mondzeichen	5	2–4	spectrum	2 Emotionen
Astro	Nordknoten	7	7	growth_path	9 Spiritualität
Astro	Saturn	5	4–5	phase_cycle	7 Arbeit
Astro	Chiron	5+3	4	trap	3 Körper
Astro	Aszendent	1	1	static	1 Identität
Maya	Geburts-Kin	4	1	static	1 Identität
Maya	Galaktischer Ton	7	7	static	9 Spiritualität
Gene Keys	Shadow	5	4–6	growth_path	11 Wachstum
Gene Keys	Gift	2–4	6	growth_path	11 Wachstum
Gene Keys	Siddhi	6–7	6–7	growth_path	9 Spiritualität
Enneagramm	Triade	3+5	4	static	2 Emotionen
Enneagramm	Typ (1–9)	5	4	trap	1 Identität
Jyotish	Nakshatras	4+7	7	static	9 Spiritualität
Jyotish	Dashas	4	5–7	phase_cycle	7 Arbeit
VI. SYSTEM-KLASSIFIKATION & KERN-FRAGEN (E-04 + E-37 + E-38)
VI.1 Klassen
Klasse	Systeme	Merkmal
A — Kernsysteme	HD, BaZi, Westl. Astrologie, Maya/Tzolkin	Geburtsdaten-basiert, Chart-Element, primäre KG-Knoten
B — Erweiterungssysteme	Jyotish, Gene Keys (Staffel 2), Quantum HD	Tief komplementär; Staffel-Planung
C — Brücken-Systeme	Enneagramm (Pflicht-Brücke via HD), Spiral Dynamics, MBTI	Kein eigenständiger Geburts-Chart; via HD-Ableitung oder Selbstreflexion
D — Ausgeschlossen	Numerologie als Einzelsystem	Kein ausreichender Mehrwert
VI.2 System-Kernfragen — Dramaturgie der Staffeln (E-37)
System	Kernfrage	Staffel / Phase
HD	WIE — Wie bin ich gebaut? Wie entscheide ich?	Staffel 1, Phase 1–3
BaZi	WAS / WANN — Was sind meine Zyklen? Wann ist die richtige Zeit?	Staffel 1, Phase 2–3
Westl. Astrologie	WO — Wo sind meine Themen? Welche Häuser brennen?	Staffel 1, Phase 1–3
Maya/Tzolkin	WELCHE WELLE — In welchem kosmischen Rhythmus bin ich?	Staffel 1, Phase 1
Gene Keys	WOHIN — Wohin kann ich mich entwickeln?	Staffel 2, Phase 6
Jyotish	WOZU — Was ist mein Dharma?	Staffel 2, Phase 7
Enneagramm	WARUM — Warum reagiere ich so? Was ist meine Grundwunde?	Staffel 1, Phase 4
VI.3 3-Gruppen-Taxonomie (E-38)
Gruppe	Systeme	Beziehungstyp	KG-Implikation
Gleiche Linse / anderer Code	Westl. Astro ↔ Jyotish	~70–80% Überlappung	Viele maps_to-Edges
Echte Komplementarität	HD ↔ BaZi	~20–30% Überlappung, andere Linse	Mehr contradicts/extends-Edges
Vertikale Erweiterung	HD → Gene Keys (64er-Basis)	Gleiche Nummern, andere Frequenzebene	extends-Edges, unterschiedl. level_tag
VII. ENNEAGRAMM-INTEGRATION — HD-BRÜCKE (E-31 — OE-13 GESCHLOSSEN)
VII.1 Entscheidung E-31
Das Enneagramm bleibt technisch Klasse C (kein eigenständiger Geburts-Chart). Es wird durch den HD-Chart als Triade automatisch abgeleitet und erhält dadurch eine Pflicht-Position im Fundament. Der Self-Assessment-Einstieg entfällt — Konzept und Inhalte bleiben vollständig.
HD-Zentrumsstatus	Enneagramm-Triade	Grundemotion	Typen
Offenes Ajna	Kopf-Zentrum (Mental)	Angst	5, 6, 7
Def. Ajna + offene Milz	Körper-Zentrum	Wut / Instinkt	8, 9, 1
Def. Ajna & Milz + off. Solar Plexus	Herz-Zentrum (Emotional)	Scham	2, 3, 4
VII.2 3-Schritte-Prozess in IC
•	SCHRITT 1 — Triade automatisch: HD-Chart → Konditionierungstriade. Kein User-Input nötig.
•	SCHRITT 2 — Subtyp durch Resonanz: IC zeigt 3 Typ-Beschreibungen; User wählt oder sagt "weiß nicht".
•	SCHRITT 3 — Subtyp-Hypothese via hängende Tore: Im Hintergrund berechnet, als zweite Hypothese angeboten (Forschungs-Backlog).

SPRACH-REGEL: IC sagt NIE "Du bist Typ 6." Es sagt: "Dein offenes Ajna deutet auf mentale Konditionierung — Typen 5, 6 oder 7. Welcher davon klingt wahr für dich?"
Positionierung: Das Enneagramm verbindet Ebene 3 (Konditionierungszentrum körperlich) und Ebene 5 (Psychodynamik/Kernwunde) — es liegt tiefer als die Geburtsdisposition.
Querverweis: Die vollständige HD→EG 3-Schritt-Methodik — inklusive Zuordnungsmatrix (offene Zentren → Triaden), UX-Kommunikationsmuster und Hypothesis-Flag-Definition — ist in IC_Fundament Kap. IV-B dokumentiert. Die dort beschriebene Methodik bildet die Grundlage für OE-13a.
VII.3 Forschungs-Backlog
•	Subtyp via hängende Tore (innen/außen/unterdrückt) — Prüfbasis klein.
•	Alle 3 Zentren definiert → trotzdem Mentaltyp? Hypothese prüfen.
•	Wing-Typen und Korrelation zum HD-Chart.
•	Kanal-Dualität (korrekt/inkorrekt × positiv/negativ) als Phase-3-Feature.
VIII. GENE KEYS & QUANTUM HD — LIZENZ & INTEGRATION (OE-04)
System	Kernfrage	Ebene	Was es liefert
HD	WAS bin ich?	4	Struktur, Typ, Energie — die Karte
Quantum HD	WIE konditioniert mich das?	3 + 5	Konditionierungsarbeit, Experiment-Protokolle
Gene Keys	WOHIN kann ich mich entwickeln?	2–7	Schatten → Geschenk → Siddhi — Entwicklungsachse

LIZENZ: Originaltexte lizenzpflichtig. Konzepte (Schatten/Geschenk/Siddhi als Idee) FREI. IC-Ansatz: Extraktion → eigene Sprache.
STATUS OE-04: Entscheidung + Alternativplan vor Extraktion — kritischer Gap.
Falls Lizenz nicht möglich → OE-18 (Ersatzstrategie definieren).
IX. KNOWLEDGE-GRAPH-ARCHITEKTUR (E-07–E-11, E-25–E-30, E-36)
IX.1 5 KG-Schichten A→E
Schicht	Name	Inhalt
A	Rohsignal	Planetenpositionen, Säulen, Gate-Aktivierungen
B	System-Konzepte	HD-Typ, BaZi Day Master, Astro-Zeichen
C	Cross-System-Muster	Bridges zwischen Systemen, Innere Strategie
D	Handbuch-Text	Sprachliche Übersetzung für User — human_review PFLICHT
E	User-Aktion	Impuls, Experiment, Reflexionsfrage — human_review PFLICHT
IX.2 Pflicht-Tags pro KG-Knoten (aktualisiert v4 + v5)
•	system_tag: hd | bazi | astro | maya | gene_keys | enneagram | …
•	level_tag: 1–7 — PFLICHT (per Element, nicht per System — das ist der Clou von E-36)
•	domain_tag: 1–11 | phase_tag: 1–7 | dynamic_type: static | transit | biographical | convergence
•	source_provenance: original_text | derived | synthesized | confidence: 0.0–1.0
•	human_review_required: true | false — Pflicht für Schicht D/E
IX.3 Node-Schema (aus v3 + v4 konsolidiert)
node: {
  id: uuid,
  type: node_type_enum,
  system: string,
  dimension_key: string,
  level_tag: int (1-7),                    ← PFLICHT (E-36)
  dynamic_type: enum {phase_cycle, trap, growth_path, spectrum} | null,
  phase: int | null,
  source_provenance: {
    source_id: string,
    page: int | null,
    chunk_id: string,
    text_snippet: string,
    language: string,
    confidence: float,
    human_reviewed: boolean
  }
}
IX.4 Edge-Typen
•	maps_to — gleiche Bedeutung, verschiedene Systeme
•	extends — tiefere Frequenz desselben Elements (HD Gate → GK Schatten)
•	contradicts — echte Widersprüche (→ Kap. XII)
•	correlates — statistische Assoziation (Forschungs-Backlog OE-12)
•	triggers — zeitliche Aktivierung (Transit → Element)
•	deepens — Vertiefungsbeziehung (Schicht A→B→C)
•	influences — kausaler/energetischer Einfluss
•	active_during — zeitliche Aktivierung (für temporal_phase)
•	belongs_to_domain — Zuordnung zu Lebensbereich
•	part_of_phase — Zuordnung zu Heldenreise-Phase
X. DIE 5 NAVIGATIONSACHSEN & HANDBUCH (E-12 ff.)
Achse	Name	Kernfrage	Modus
1	Landkarte / Mandala	WO bin ich? (räumlich, Domänen)	Explorer
2	Handbuch	WAS bedeutet dieses Element? (4 Schichten)	Leser
3	Zeitlinie	WANN ist was aktiv? (Transite)	Navigator
4	Flussdiagramm	WIE hängt alles zusammen? (Bridges)	Analytiker
5	Heldenreise	WOHIN gehe ich? (narrativ, geführt)	Reisende/r
X.1 Handbuch — 4 Inhalts-Schichten
Schicht	Name	Frage	Ton
1	Spiegel	"Das bist du"	Beschreibend, bestätigend
2	Synthese	"Das hängt so zusammen"	Erklärend, verknüpfend
3	Prozess	"Hier kannst du arbeiten"	Einladend, prozesshaft
4	Experiment	"Das kannst du ausprobieren"	Aktivierend, konkret
X.2 Lens-Switcher (E-32 — NEU v4)
•	Synthese-Meta-View (DEFAULT): IC-eigene Sprache, ebenen-übergreifend. UX-Richtung: innen→außen.
•	Original-Modus (OPT-IN): System-native Sprache — reduziertes Bild. User spürt die Grenzen selbst (pädagogisch wertvoll).
XI. DIE 7 PHASEN / HELDENREISE (E-20, OE-11)
v5-HINWEIS: Dieses Kapitel vereint die v4-Phasentabelle mit den in v3 definierten Ton- und App-Trigger-Angaben, die in v4 verloren gegangen waren. Beides ist für Strang 1 (App) und Strang 2 (Buch) operativ notwendig.
XI.1 Phasen-Tabelle mit Ton + App-Trigger (WIEDERHERGESTELLT aus v3)
Phase	Name	Kernfrage	Primäre Systeme	Ton (aus v3)	App-Trigger (aus v3)
1	ERKENNEN	"Wer bin ich?" — erste Orientierung	HD-Typ, BaZi Day Master, Astro Sonne, Maya Kin	Staunend, einladend, zugänglich	Onboarding → Erste Landkarte
2	VERSTEHEN	"Dein Terrain" — Muster, Cross-System-Bridges	HD-Profil, Astro Mond, BaZi Clashes	Analytisch, vernetzend	Handbuch-Tiefe ≥2 pro Bereich
3	VERKÖRPERN	"Dein Körper" — PHS, Somatik, Alltagsexperimente	HD PHS/Variables, Ayurveda-Brücke	Körpernah, experimentell	Erste Experimente abgeschlossen
4	SCHATTEN	"Deine Kante" — Not-Self, Konditionierung, Wunde	Offene Zentren, Enneagramm-Triade	Konfrontativ aber mitfühlend	User signalisiert Bereitschaft (kein automatisches Freischalten)
5	NAVIGATION	"Dein Kompass" — Autorität, Luck Pillars	HD-Autorität, BaZi Luck Pillars, Transite	Praktisch, handlungsorientiert	Zeitlinie aktiv genutzt
6	INTEGRATION	"Dein Standort" — Entwicklungsebene	Gene Keys, Spiral Dynamics	Reif, nicht wertend, perspektivisch	Staffel 2 + aktive Experimentphase
7	HORIZONT	"Dein Beitrag" — Sinn, Mission, Dharma	Inkarnationskreuz, Nordknoten, Jyotish	Öffnend, fragend, hypothetisch	Langzeit-User, abgeschlossene Experimentzyklen

•	Kein globaler User-Phasenstatus: User kann in "Beruf" Phase 5 und in "Beziehungen" Phase 2 sein. 7 Phasen gelten pro Domäne (E-19).
•	Einstiegslogik OE-11 — Empfehlung Hybrid: Standard Phase 1; Option "Krise" → Phase-4-Einstieg mit Rückverlinkung.
XI.2 Domäne × Phase Matrix (WIEDERHERGESTELLT aus v3 Kap. IV.1)
v5-HINWEIS: Diese Matrix war in v3 als strukturierendes Designkonzept definiert und fehlte in v4 vollständig. Sie ist die Basis für die Content-Architektur in Strang 1.
Jede Zelle (Domäne × Phase) ist ein potenzieller Inhaltsbaustein. Ein User kann in Domäne "Beruf" bei Phase 5 sein und gleichzeitig in Domäne "Beziehung" bei Phase 1. Das System ist nicht-linear.
•	11 Domänen × 7 Phasen = 77 Inhaltsbausteine (Potenzialraum)
•	Nicht jede Zelle muss ab MVP befüllt sein — Priorität: Phase 1 × alle Domänen + Domäne 1 × alle Phasen
•	Pro Zelle: System-Elemente + Handbuch-Schichten + Experimente
Domäne \ Phase	1 ERKENNEN	2 VERSTEHEN	3 VERKÖRPERN	4 SCHATTEN	5 NAVIGATION	6 INTEGRATION	7 HORIZONT
1 Identität	●	●	○	●	○	○	○
2 Emotionen	●	●	○	●	○	○	○
3 Körper	●	○	●	○	○	○	○
4 Geist	●	○	○	○	●	○	○
5 Beziehungen	●	●	○	●	○	○	○
6 Familie	●	○	○	●	○	○	○
7 Arbeit	●	●	○	○	●	○	●
8 Finanzen	○	○	○	○	●	○	○
9 Spiritualität	○	○	○	○	○	●	●
10 Gemeinschaft	○	○	○	○	○	○	●
11 Wachstum	○	○	○	●	○	●	●
● = MVP-Priorität  |  ○ = Post-MVP
XI.3 Verhältnis: 4-Schichten-Handbuch vs. 7 Phasen
•	Die 4 Handbuch-Schichten (Spiegel → Synthese → Prozess → Experiment) sind NICHT dasselbe wie die 7 Phasen.
•	Handbuch-Schichten = WIE TIEF gehe ich in ein einzelnes Thema?
•	7 Phasen = WO BIN ICH auf meiner Gesamtreise?
•	Beide Achsen koexistieren.
XII. WIDERSPRUCHS-PROTOKOLL (E-39 — NEU v4)
Multi-System-Widersprüche sind die Regel, nicht die Ausnahme. Widersprüche werden NICHT verborgen.
Schritt	Was IC tut	Muster-Sprache
1 — Zeigen	Widerspruch explizit sichtbar machen	"Diese zwei Systeme sehen dich hier unterschiedlich."
2 — Einordnen	Erklären: verschiedene Ebenen, kein Fehler	"BaZi schaut auf deine Zyklen — HD auf deine Energie-Architektur."
3 — Einladen	User zur Resonanz-Evaluation einladen	"Welches davon fühlt sich in deinem Alltag wahrer an?"
4 — Markieren	KG-Edge: contradicts + confidence-Wert	Intern: Forschungs-Signal für OE-12

Kernprinzip: Widersprüche sind kein Produktfehler — sie sind Einladungen zur Selbstreflexion.
XIII. ZEITMODELL — 4 DIMENSIONEN + HIERARCHIE (E-21 + E-40)
Dim.	Name	Beschreibung	Quellen
1	Astronomische Dynamik	Transite, Luck Pillars, Dashas — berechnet	Alle Klasse-A-Systeme
2	Psychologische Dynamik	Not-Self-Muster, Trigger — abgeleitet	Chart + Reflexion
3	Biographische Dynamik	Aktuelle Lebenssituation — User-Input	User-Selbstauskunft
4	Konvergenzmarker	Mehrere Systeme aktivieren gleichzeitig — stärkstes Signal	KG-Kreuzabgleich
XIII.1 Prioritäts-Hierarchie (E-40 — NEU v4)
Priorität	Dimension	Warum
1 (höchste)	Biographisch	User weiß selbst, was gerade brennt — Einstiegspunkt
2	Konvergenz	Mehrere Systeme gleichzeitig → stärkstes strukturelles Signal
3	Astronomisch	Kontextualisiert das Biographische, gibt Zeitrahmen
4	Psychologisch	Dauerhaftes Hintergrundmuster — immer relevant, selten vordringlich
XIII.2 Dynamics-Taxonomie (E-25)
dynamic_type	Definition	Beispiel-Quellen	UI-Konsequenz
phase_cycle	Zeitlich begrenzte Zyklen mit Anfang/Ende	Luck Pillars, Dashas, Transite, Saturn Return	Timeline-Band mit Start/End-Datum
trap	Wiederkehrende Reaktionsmuster/Fallen	Not-Self, BaZi-Clashes, Shadow-Muster	Reflexions-Marker + Frage
growth_path	Entwicklungspfad mit Richtung	Gene Keys, HD-Dekonditionierung	Spektrum-Visualisierung
spectrum	Kontinuum ohne Richtung, situativ	Element-Balance, Center-Definiert/Offen	Radar/Mandala-Segment
XIV. GRADUATION & ABSCHLUSS-KONZEPT (NEU v4)
Es muss einen Punkt geben, an dem ein User "fertig" ist — und das als Erfolg erlebt, nicht als Verlust.
•	Phase 7 in mind. 3–4 Lebensbereichen abgeschlossen: eigene Sprache für das Selbst entwickelt.
•	Experimentierzyklen im Körper und Alltag verankert (nicht nur kognitiv).
•	Widersprüche integriert: User kann contradicts-Paare benennen und damit leben.
•	Graduation ≠ Account löschen: IC wird vom Guide zur Referenz.
•	Post-Graduation: optionale Rückkehr bei Life-Events (Saturn Return, Luck Pillar-Wechsel, Krise).
•	Graduation-Ritual: "Was hast du herausgefunden, das vorher nicht in Sprache war?"

STATUS: Konzept-Rahmen gesetzt — UX-Details offen (OE-16 → Strang 1).
XV. INNERE STRATEGIE — META-NODE-KONZEPT (E-19, E-27)
v5-HINWEIS: Das inner_strategy factor_scores Schema war in v3 Kap. VI definiert und fehlte in v4. Es wird hier vollständig wiederhergestellt, mit level_tag-Ergänzung aus E-36.
Die Kern-Formel: Signatur × Prägung × Bewusstsein × Zyklus = Innere Strategie
XV.1 Primär- und Ergänzungsfaktoren
•	Primärfaktoren (dokumentiert, berechenbar):
    • Signatur — Geburtsbasierte Disposition (HD/BaZi/Astro/Maya)
    • Prägung — Konditionierung (offene Zentren, Element-Mangel)
    • Zyklus — Aktuelle Zeitlinie/Transite
•	Ergänzende Faktoren (optional, abgeleitet/erfragt):
    • Bewusstsein — Metakognitionsfähigkeit, Beobachterposition
    • Affect — Psychologischer Zustand (current_affect, opt-in)
    • Soma — Somatischer Zustand (body_mechanics, PHS)
    • Kontext — Soziale Rolle, Lebensbereich, aktuelle Situation
    • Trigger — Kurzfristige situative Auslöser
XV.2 inner_strategy factor_scores Schema (E-27 — WIEDERHERGESTELLT aus v3)
inner_strategy: {
  contributing_nodes: [],
  factor_scores: {           ← ⚠️ EXPERIMENTAL
    signature:    0.4,       ← Hypothetisch, nicht validiert
    conditioning: 0.2,       ← Hypothetisch, nicht validiert
    transit:      0.1,       ← Hypothetisch, nicht validiert
    affect:       0.2,       ← Hypothetisch, nicht validiert
    consciousness: 0.1      ← Hypothetisch, nicht validiert
  },
  level_tags: [3, 4, 5],    ← NEU v5: Ebenen-Referenz (E-36)
  synthesis_text: "",        ← DEFAULT-Output (narrativ, nicht numerisch)
  recommended_experiments: [],
  human_review_required: true
}
Die factor_scores sind hypothesengetrieben (H-05). Sie dürfen NICHT für UX-Entscheidungen oder User-facing Anzeigen verwendet werden, bis:
•	N>30 qualitative Validierungen durchgeführt sind
•	A/B-Test zeigt, dass numerische Scores hilfreicher sind als narrative Synthese
•	Human Review durch Domänen-Experten stattgefunden hat

Default-Output bleibt: synthesis_text (narrativ). Siehe OE-09 für Forschungsplan.
XV.3 Affect-Tracking (E-22)
Emotionale Zustandsdaten (current_affect) werden als explizit opt-in behandelt. Default = aus.
Begründung: Emotionale Daten sind sensitiver als Geburtsdaten. DSGVO-konform, lokal berechnet, leicht löschbar. Kein Dark Pattern zur Aktivierung.
XVI. DIE 11 LEBENSBEREICHE / DOMÄNEN (E-18)
Nr	Domäne	Kernfrage
1	Identität & Selbstbild	Wer bin ich?
2	Emotionen & Innenwelt	Wie fühle ich?
3	Körper & Gesundheit	Wie ist mein Körper beschaffen?
4	Geist & Denken	Wie denke ich?
5	Beziehungen & Liebe	Wie liebe ich?
6	Familie & Herkunft	Woher komme ich?
7	Arbeit & Beruf	Was ist mein Beitrag?
8	Finanzen & Ressourcen	Wie gehe ich mit Ressourcen um?
9	Sinn & Spiritualität	Wozu bin ich hier?
10	Gesellschaft & Gemeinschaft	Wie lebe ich mit anderen?
11	Wachstum & Entwicklung	Wohin entwickle ich mich?
XVII. WORDING-STRATEGIE (E-23 + E-32 — v3 + v4 KOMBINIERT)
v5-HINWEIS: Dieses Kapitel kombiniert die v3-Drei-Sprachebenen-Tabelle mit konkreten Wording-Beispielen und die v4-Ergänzungen (Lens-Switcher, Zwei Richtungen). Beide fehlten isoliert in der jeweils anderen Version.
XVII.1 Drei Sprachebenen mit Beispielen (WIEDERHERGESTELLT aus v3)
Sprachebene	Wo sichtbar	Beispiel (aus v3)	Lens-Switcher (v4)
System-Ebene	System-Linse im UI	"Offenes Emotionalzentrum" | "Yin Water Day Master"	Original-Modus (opt-in)
Handbuch-Ebene	Handbuch, Default-Ansicht	"Du nimmst Emotionen anderer auf wie ein Schwamm"	Synthese-Meta-View (default)
Meta-Ebene	Cross-System-Synthese, Innere Strategie	"Dein Nervensystem ist auf Resonanz ausgelegt — du brauchst Stille, um dich zu sortieren"	Synthese-Meta-View (default)
XVII.2 Sprach-Regeln
•	VERBOTEN: "Du bist X." — IMMER: "Dein Chart deutet auf X — erkennst du das?"
•	Cross-System: "HD und BaZi zeigen hier dasselbe Thema — das ist ein starkes Signal."
•	Widerspruch: "Diese zwei Systeme sehen dich hier unterschiedlich. Welches fühlt sich wahrer an?"
XVII.3 Zwei Richtungen (NEU v4)
•	Analyse-Richtung (intern): außen → innen (A→E).
•	UX-Richtung (User): innen → außen (Bestätigung → Muster → Tiefe).
XVIII. DIMENSIONS-CONTRACT (15 Dimensionen — E-03)
mechanical, psychological, somatic, shadow, gift, archetype, role, social, relationship_pattern, projection_field, environment, body_mechanics, elemental_quality, temporal_phase, destiny_pattern.
Jede Interpretation im KG MUSS eine dimension_key tragen. Dimensionen sind erweiterbar, nie löschbar.
XIX. STORY- UND RELEASE-ARCHITEKTUR (E-23, E-30 — WIEDERHERGESTELLT aus v3)
v5-HINWEIS: Dieses Kapitel (v3 Kap. XI mit 4 Unterkapiteln) fehlte in v4 vollständig. Es wird hier vollständig wiederhergestellt, da es für Strang 2 (Buch/Vermittlung) und die Release-Strategie essentiell ist.
XIX.1 Schicht 1: DIE SERIE (öffentlich, viral)
KI-generierte Story mit 5 Botschafter-Figuren aus verschiedenen Kulturen (Aria, Jian, Priya, Kwame, Sofia). Sie durchlaufen die Journey, entwickeln sich, spiegeln echte Fragen. Format: KI-Video-Serie, kurze Episoden.
XIX.2 Schicht 2: DAS PRODUKT (App)
Jede Episode endet mit einem Hook: "Was würde DEIN Chart dazu sagen?" → App-Deeplink auf das relevante Feature/Element.
XIX.3 Schicht 3: DEINE GESCHICHTE (Personalisiert)
In der App erlebt der User seine eigene Version der Journey. Die Serie zeigt den Weg, die App macht ihn persönlich.
XIX.4 KI-Qualitätsprinzipien für kulturelle Darstellung (E-30 — WIEDERHERGESTELLT aus v3)
•	Respektvolle Recherche: Jede kulturelle Darstellung basiert auf Originalquellen des jeweiligen Kulturkreises, nicht auf vereinfachten Stereotypen.
•	Mehrdimensionale Figuren: Botschafter-Figuren sind keine "Vertreter ihrer Kultur", sondern individuelle Menschen MIT kulturellem Hintergrund.
•	Iterative Qualitätskontrolle: KI-generierte kulturelle Inhalte werden vor Veröffentlichung auf Stereotypen, Vereinfachungen und mögliche Verletzungen geprüft.
•	Transparenz: Es wird klar kommuniziert, dass die Serie KI-generiert ist.
•	Lernbereitschaft: Feedback aus betroffenen Communities wird aktiv eingeholt und ernst genommen.
•	Keine kulturelle Hierarchie: Kein System wird als "fortschrittlicher" oder "primitiver" dargestellt.
XX. BIOGRAFIE-LAYER (E-24)
Die Biografie sagt "und so hat sich das in meinem Leben gezeigt". Sie verknüpft Chart-Elemente mit realen Erfahrungen — aber NUR wenn der User das explizit möchte.
•	Opt-in: Kein Default-Feature, bewusst aktiviert
•	Granular: User entscheidet pro Lebensbereich, was er teilen will
•	Löschbar: Jederzeit vollständig löschbar (Recht auf Vergessen)
•	Lokal: Biografie-Daten werden lokal verarbeitet, nicht an Server gesendet
•	Kein Scoring: Biografie-Daten werden NICHT für Algorithmen verwendet
XXI. WISSENSEXTRAKTION & KG-QUALITÄT (E-28–E-30)
XXI.1 Quellenstrategie — Reihenfolge (E-28)
Schritt 1 — ORIGINALQUELLEN: PDFs → Chunking → LLM-Extraktion → KG Schicht A/B. Keine KI-Eigeninterpretation.
Schritt 2 — SYSTEM-MAPPING: Element-Konzepte auf 7-Ebenen-Modell mappen. level_tag setzen. Provenance tracken.
Schritt 3 — SYNTHESE-SPRACHE: Cross-System-Bridges in IC-eigener Sprache. Human Review für Schicht D/E.

WICHTIG: Schritt 3 kommt erst, wenn Schritt 1+2 für die relevanten Systeme abgeschlossen und qualitätsgesichert sind.
XXI.2 Quellenklassen
Klasse	Definition	Verwendung
Primär	Originale/klassische Werke, Gründer-Texte	Mechaniken (Schicht A), Kern-Interpretationen (Schicht B)
Sekundär	Etablierte Lehrer, moderne Standardwerke	Erweiterte Interpretationen (Schicht B), Prozesse (Schicht C)
Tertiär	Blog-Artikel, Community-Wissen, populäre Darstellungen	Nur als Kontext/Validation, nicht als Primärquelle im KG
XXI.3 Chunking-Standards
•	Chunk-Größe: 500–1500 Tokens (semantische Einheiten, nicht mechanisches Splitting)
•	Overlap: 100 Tokens an Chunk-Grenzen
•	Metadaten pro Chunk: source_id, page_range, chapter, section, language
•	Strukturelle Marker: Tabellen, Listen, Diagramme als eigene Chunks mit Typ-Tag
XXI.4 Human-in-the-Loop
•	Nodes mit confidence < 0.7 werden automatisch für human_review geflaggt.
•	Cross-System-Mappings (Schicht D) erfordern IMMER human_review vor User-facing Verwendung.
•	Schicht D + E: human_review_required = true. Kein automatischer Output ohne Review.
XXII. AQAL-QUADRANTEN — Internes Qualitätsraster
Quadrant	Abdeckung	Was fehlt(e)	Lösung
OL (Innen-Individuell)	Stark	Bewusstseinsebenen	Phase 6 + Gene Keys
OR (Außen-Individuell)	Mittel	Somatik fehlte	Phase 3 + PHS + BaZi-Element
UL (Innen-Kollektiv)	Schwach	Kulturelle Resonanz	Multi-System-Ansatz + Strang 2
UR (Außen-Kollektiv)	Schwach	Soziale Systeme	Domäne 10 + Relationship Mode
XXIII. ENTSCHEIDUNGSREGISTER
XXIII.1 Getroffene Entscheidungen E-01 bis E-40
ID	Entscheidung	Status
E-01	Drei Stränge: App, Buch, Forschung	Nicht änderbar
E-02	Strang 0 als Fundament (gleichrangig mit Steuerung)	Nicht änderbar
E-03	Dimensions-Contract (15 Dim.)	Erweiterbar
E-04	HD, BaZi, Astro, Maya = Klasse A	Nicht änderbar
E-05	Gene Keys Staffel 2, Klasse B	Festgelegt
E-06	Enneagramm Klasse C → Pflicht-Brücke via HD (akt. E-31)	Aktualisiert v4
E-07	5 KG-Schichten A→E	Nicht änderbar
E-08	KG als Kern-Architektur	Nicht änderbar
E-09	Human-Review für Schicht D/E	Nicht änderbar
E-10	Confidence-Level pro Knoten	Nicht änderbar
E-11	Provenance-Tag pro Knoten	Nicht änderbar
E-12	5 Navigationsachsen	Nicht änderbar
E-13	Keine Psychologie-Systeme als Primärsystem	Festgelegt
E-14	Synthesis-Meta-View als Default + Lens-Switcher	Festgelegt
E-15	Hypothesen-Sprache für alle Ableitungen (Pflicht)	Nicht änderbar
E-16	Enneagramm-Einstieg via HD-Chart, kein sep. Assessment	Aktualisiert v4
E-17	Graduation-Konzept verpflichtend	Festgelegt (Details OE-16)
E-18	11 Lebensbereiche (einheitlich)	Nicht änderbar
E-19	Domänen × Phasen-Matrix (nicht-linear)	Nicht änderbar
E-20	7 Phasen / Heldenreise	Nicht änderbar
E-21	4 Zeitdynamik-Dimensionen	Aktualisiert: Hierarchie → E-40
E-22	Konvergenzmarker = stärkstes Signal	Bestätigt
E-23	Wording: Hypothesen-Sprache Pflicht	Nicht änderbar
E-24	Widersprüche sichtbar machen → Protokoll E-39	Festgelegt
E-25	Dimensions-Contract: erweiterbar, nie löschbar	Nicht änderbar
E-26	Rohmechaniken aus Originalwerken (kein KI-Wissen)	Nicht änderbar
E-27	KI-Eigeninterpretation verboten für Schicht A/B + factor_scores EXPERIMENTAL	Nicht änderbar / Änderbar nach Validierung
E-28	Quellenstrategie: Original → Mapping → Synthese	Nicht änderbar
E-29	Wissensquellen pro Dynamik-Typ = Research Required (OE-12)	Offen
E-30	KI-Kulturdarstellung mit Qualitätsprinzipien (Kap. XIX)	Erweiterbar
E-31	Enneagramm-Triade via HD-Chart ableitbar; Pflicht-Brücke — OE-13 geschlossen	NEU v4
E-32	Analyse: außen→innen / UX: innen→außen — explizit getrennt	NEU v4
E-33	3-Gruppen-Taxonomie der Systembeziehungen	NEU v4
E-34	Kapitel "Karte ≠ Territorium" im Fundament (früh, 3-teilig) — OE-14 geschlossen	NEU v4
E-35	7-Ebenen-Modell als eigenständiges Konzept — OE-15 geschlossen	NEU v4
E-36	System × Ebenen-Mapping: per-Element level_tag = KG-Pflicht-Feld	NEU v4
E-37	System-Kernfragen (WIE/WAS/WO/WELCHE WELLE/WOHIN/WOZU/WARUM)	NEU v4
E-38	3-Gruppen-Taxonomie der Systeme (Kap. VI.3)	NEU v4
E-39	Widerspruchs-Protokoll: zeigen → einordnen → einladen → markieren	NEU v4
E-40	Zeitmodell-Prioritäts-Hierarchie: biograph. > Konvergenz > astron. > psychol.	NEU v4
XXIII.2 Offene Entscheidungen (OE)
OE	Prio	Thema	Status / Nächster Schritt
OE-04	🔴 HOCH	Gene Keys Lizenzklärung	Entscheidung + Alternativplan vor Extraktion — kritischer Gap
OE-05	🔴 HOCH	Laurent-Material Policy	Klärung ausstehend
OE-06	🟡 MITTEL	Branding/Name "Inner Compass"	Vor Launch
OE-07	🟡 MITTEL	Free vs. Paid Modell	Vor Launch
OE-08	🟡 MITTEL	Exakte Staffel-Zuordnung	Vor Staffel 2
OE-09	🟡 MITTEL	Konzeptpapier "Innere Strategie"	Relevant ab Phase 5
OE-10	🟢 NIEDRIG	Fehlende Kulturkreise Staffel 4+	Nach Staffel 1
OE-11	🔴 HOCH	Heldenreise-Einstiegslogik	Empfehlung Hybrid. Endentscheidung ausstehend.
OE-12	🟡 HOCH	Forschungsdesign Strang 3	N, Datensätze, Consent — Triade, EG-Subtyp, hängende Tore
OE-13a	🟡 MITTEL	HD→EG Subtyp-Ableitung: 3-Schritt-Methodik	Detailierung in IC_Fundament Kap. IV-B. Schritt 1 (Triade, automatisch) = gesetzt. Schritt 2 (Subtyp via Resonanz) = gesetzt. Schritt 3 (Subtyp via hängende Tore) = Forschungshypothese → OE-12. Option C (Hybrid: zeigen + als Hypothese kennzeichnen) = EMPFOHLEN. UX-Flag: hypothesis_badge auf allen Schritt-3-Outputs. Testkriterien: N>30 qualitative Validierungen, A/B-Test narrative vs. numerische Darstellung.
OE-16	🟡 MITTEL	Graduation UX-Details	Konzept gesetzt (Kap. XIV), UX Strang 1
OE-17	🟡 MITTEL	Zielgruppen-Operationalisierung	Einsteiger/Fortgeschrittene/Experten in Onboarding & UI
OE-18	🟡 MITTEL	Gene Keys Ersatzstrategie	Falls Lizenz nicht möglich: Ebene-2–3-Gap schließen
OE-19	🟡 MITTEL	Domäne × Phase UX-Design	Wie zeigt die App nicht-linearen Phasenstatus?
XXIV. HYPOTHESENREGISTER
ID	Hypothese	Testbar durch
H-01	Konvergenz-These: Systeme konvergieren strukturell	Schicht D quantifizieren
H-02	Multi-System-Spiegel erzeugt stärkere Resonanz als Einzelsystem	A/B-Test
H-03	Progressive Enthüllung führt zu tieferer Integration	UX-Studie
H-04	Experiment-Tracking wirksamer als passive Informationsaufnahme	Längsschnitt
H-05	Innere Strategie ist ableitbar aus Geburtsdaten + Reflexion	Qualitative Studie
H-06	Enneagramm-Brücke erhöht Onboarding-Konversion	Conversion-Test
H-07	Emotionale Domäne fördert Engagement bei vorhandenen Usern	Feature-A/B
H-08	Kulturübergreifende Resonanz: Fremd-Systeme unterbrechen Bestätigungsfehler	Qualitativ
H-09	Selbst-Redundanz: Empowerment erzeugt stärkere Loyalität als Sucht-Design	Retention-Vergleich
H-10	Biografie-Konvergenz: Chart + Life-Event Overlap erzeugt stärkste Aha-Momente	Qualitativ
XXV. APP-FEATURE-MAP (Prinzipien-Referenz)
#	Feature	Leitdokument-Referenz	Staffel
1	Onboarding (Geburtsdaten)	E-04, Kap. VI	1
2	Landkarte/Mandala (11 Bereiche)	E-12, E-18, Kap. XVI	1
3	Handbuch (4 Schichten pro Element)	E-07, Kap. X	1
4	Zeitlinie (4 Dynamik-Dimensionen)	E-21, E-25, Kap. XIII	1
5	Fluss-Diagramm (Sequence Map)	Kap. X	1
6	System-Filter + Lens-Switcher	E-11, E-32	1
7	Cross-System-Insights (Schicht D)	E-10, Kap. IX	1
8	Drei Sprachebenen + Lens-Switcher	Kap. XVII	1
9	Agent/Begleiter (kontextuell)	PRD v3	1 (Phase 2)
10	Relationship Mode	PRD v3	1
11	Exploring/Archetypen-Bibliothek	PRD v3	1
12	Heldenreise (7 Phasen, geführt)	E-20, Kap. XI	1 (Phase 2)
13	Lebensskizze (Biografie, opt-in)	E-24, Kap. XX	1 (Phase 2)
14	Innere Strategie (Meta-Node)	E-17/E-19/E-27, Kap. XV	2
15	Affect Check-in (opt-in)	E-22, Kap. XV.3	2
16	Konvergenz-Marker (Zeitlinie)	Kap. XIII	2
17	Daily Compass (Push-Notification)	Vision-Doc	1 (Phase 2)
XXVI. CROSS-STRAND KOORDINATION
Bereich	Leitdokument (gilt überall)	Strang 1: App	Strang 2: Buch/Serie	Strang 3: Forschung
Philosophie	4 Thesen, Ethik-Prinzipien	UX-Konsequenzen	Narrative Rahmung	Positionality
Systeme	Inventar, Klassifizierung	Berechnung, Pipeline	System-Erklärungen	Untersuchte Sys.
Dimensionen	15 Dimensions-Contract	Schema, Mandala	Kapitelstruktur	Variablen-Op.
Lebensbereiche	11 Bereiche + Kernfragen	Navigation, Segmente	Kapitel-Gliederung	Interview-Leitf.
Wording	Drei-Ebenen-Prinzip + Lens-Switcher	UI-Texte, Meta-Nodes	Buchsprache	Wissenschaftsspr.
Innere Strategie	Multi-Faktor-Modell (E-19)	Schicht E, Prozess	Narrative Integr.	Forschungshyp.
7 Phasen	Referenz-Architektur (E-20)	UX-Journey	Kapitelfolge	Studien-Design
Dynamik	4 Dim. + Taxonomie (E-21/E-25)	Zeitlinie-Feature	Erzählstruktur	Längsschnitt
Biografie-Layer	Privacy-Prinzipien (E-24)	Opt-in Flow	Fallbeispiele	Qualitative Daten
Story/Release	3-Schicht-Modell + Kultur-QA (E-23/E-30)	Feature-Unlock	Content-Kalender	—
XXVII. NÄCHSTE SCHRITTE (Post v5)
Schritt	Deliverable	Inhalt	Prio
A — SOFORT	KG System×Ebenen Mapping-Tabelle (CSV)	Alle Systeme, alle Elemente, level_tag, phase_tag — Import-ready	🔴
B — PARALLEL	Gene Keys Lizenz-Entscheid + Alternativplan	Policy: was darf extrahiert, wie cite, Reformulierungsstufe	🔴
C — TECHNISCH	KG-Node-Schema: level_tag Pflicht + Extractor-Regeln	Provenance, confidence, human_review triggers	🔴
D — UX	Lens-Switcher UX + Widerspruchs-Karten-Sprache	Originalmodus vs. Meta-View; Triade-Hypothesis card language	🟡
E — FORSCHUNG	OE-12 Forschungsdesign	N, Datensätze, Consent für Triade-Validierung + EG-Subtyp	🟡
F — FUNDAMENT	IC_Fundament Kapitel schreiben	Karte≠Territorium + 7-Ebenen-Modell + Enneagramm als Texte
Kap. IV-A (5 Modelle) + IV-B (HD→EG) geschrieben.
Querverweise in Leitdokument v5.1 eingetragen.	🟡
G — CONTENT	Domäne × Phase Befüllung Staffel 1	Phase 1 × alle Domänen + Domäne 1 × alle Phasen	🔴
XXVIII. v5 CHANGE-DOKUMENTATION
Dieses Kapitel dokumentiert alle Änderungen von v4 → v5 gemäß der Delta-Analyse.
#	Aktion	Quelle	Kapitel in v5	Status
1	v4 als Basis behalten (E-01–E-40)	v4	Gesamt	✅ Pflicht
2	Phasen-Ton + App-Trigger wiederhergestellt	v3 Kap. IV	XI.1	✅ Erledigt
3	Domäne × Phase Matrix wiederhergestellt	v3 IV.1	XI.2	✅ Erledigt
4	inner_strategy Schema wiederhergestellt + level_tags (E-36)	v3 Kap. VI	XV.2	✅ Erledigt
5	Story/Release + E-30 Qualitätsprinzipien wiederhergestellt	v3 Kap. XI	XIX	✅ Erledigt
6	Drei-Sprachebenen + Lens-Switcher kombiniert	v3+v4	XVII	✅ Erledigt
7	System×Ebenen×Phase Mapping Table NEU eingebettet	Neu (v5)	V.5	✅ Erledigt
8	Enneagramm konsolidiert (v3 + v4)	v3+v4	VII	✅ Erledigt
9	OEs konsolidiert (v3 + v4)	v3+v4	XXIII.2	✅ Erledigt
10	Change-Log v5 dokumentiert	Standard	XXVIII	✅ Erledigt
11				

v5.1 25.02.2026 PATCH: Naming-Konvention durchgängig (IC_Fundament statt Strang0_Inner_Compass). Dokument-Hierarchie auf 5 Zeilen erweitert. Querverweise: IV.1 → IC_Fundament IV-A, VII.2 → IC_Fundament IV-B. OE-13a (HD→EG Subtyp-Methodik) als neuer offener Punkt. Punkt 8 (Naming) geschlossen: funktionale Naming-Konvention gilt ab v5.1.
IC_Leitdokument v5.1  |  25. Februar 2026  |  VERTRAULICH  |  Living Document
v5 = v4 (strukturelle Überlegenheit) + 5 wiederhergestellte operative Blöcke aus v3 + 1 neue Mapping Table
