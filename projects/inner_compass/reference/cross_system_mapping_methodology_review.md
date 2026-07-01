---
last_update: 2026-07-01
status: review_open — vor Start Phase 3 zu entscheiden
scope:
  summary: "Kritische Prüfung der geplanten Cross-System-Mapping-Methodik (Phase 3): Warum Embedding-Cosine-Similarity auf synthetisiertem Text die falsche Vergleichsbasis ist, ob/wie LLM-Validierung das lösen kann, und Klärung der Reihenfolge canonical_description (Phase 2) vs. Meta-Knoten (Phase 4)."
  in_scope:
    - Mechanistische Erklärung, was Text-Embeddings tatsächlich messen (Sprachähnlichkeit vs. Bedeutung vs. Referenzidentität)
    - Warum die dokumentierte Pipeline (synthesize_node → embed → cosine >0.75 → LLM-Validierung → Human Review) das Problem verschärft statt löst
    - Klarstellung: zwei verschiedene Synthese-Schritte im Datenfluss (Phase 2 vs. Phase 4), die ähnlich klingen aber unterschiedliche Zwecke haben
    - Ob eine "wissende" separate LLM-Validierung das Problem lösen kann, und unter welchen Bedingungen
    - Konkrete Schema-Erweiterung für sys_kg_edges (correspondence_type, evidence_basis)
  out_of_scope:
    - Implementierung (Phase 3 hat Stand 2026-06 noch nicht begonnen, siehe status.md)
    - Alternative Embedding-Modelle / Kostenvergleich
    - Ontologie-Split-Fragen (→ reference/ontology_policy.md, anderes Thema)
notes:
  - "Entstanden aus Gesamtarchitektur-Review per Chat (2026-07-01), Anlass: Frage ob das Cross-System-Mapping-Konzept 'die ultimative App' tragen kann."
  - "Muss vor Beginn Phase 3 (Cross-System, aktuell 0%) gelesen und die Empfehlungen entweder übernommen oder bewusst verworfen werden — dann Eintrag in decisions.md."
  - "Bezug: cursor/architecture.md §4 (Datenfluss Phase 2-4) und §9; cursor/contracts.md §5 (maps_to Edge-Attribute: confidence, similarity_basis, human_reviewed); reference/ontology_policy.md (Split-Kriterien — komplementäres, aber anderes Thema: WANN zwei system_id, nicht WIE man Mapping-Qualität sichert)."
---

# Cross-System-Mapping: Methodik-Review (Phase 3)

> Kontext: Inner Compass' zentrales Alleinstellungsmerkmal ist die Aussage "wenn drei Traditionen dasselbe Muster sehen, ist das bedeutsam" (Datenschicht D+E, siehe `prd_v3.md` §3+5). Dieses Dokument prüft, ob die **aktuell dokumentierte** Methodik (siehe `architecture.md` §4) diesen Anspruch technisch einlösen kann.

## 1. Kurzfassung (TL;DR)

- Das **Grundkonzept** (KG pro System, Ähnlichkeiten suchen, Meta-Knoten destillieren) ist **nicht falsch**.
- Die **konkrete geplante Umsetzung** von Phase 3 (Embedding-Cosine-Similarity auf `canonical_description` als primäres Auswahlkriterium für `maps_to`-Kandidaten) ist **methodisch unzureichend** — nicht nur, weil Human Review fehlt/nicht skaliert, sondern weil die **Vergleichsgrundlage selbst** die entscheidenden Signale bereits verloren hat, bevor verglichen wird.
- Eine **zweite/separate LLM-Validierung kann das Problem lösen** — aber nur, wenn sie strukturell andere (reichhaltigere) Eingaben bekommt als die Embedding-Erzeugung. Ein zweiter LLM-Call auf denselben Text ist zirkulär (Rubber Stamp).
- Zusätzlicher, bisher nicht dokumentierter Punkt: Es gibt **zwei verschiedene Synthese-Schritte** (Phase 2 „synthesize_node“ pro System/Knoten, Phase 4 „Meta-Knoten“ cross-system), die leicht verwechselt werden. Das Problem sitzt in Phase 2, nicht in Phase 4.

---

## 2. Was Text-Embeddings tatsächlich messen

Embeddings (z. B. `text-embedding-3-large`) werden über kontrastives Training gelernt: Texte, die in ähnlichen Kontexten vorkommen oder als Paraphrasen gelten, landen im Vektorraum nah beieinander. Sie messen **distributionelle/thematische Verwandtschaft**, nicht **Referenzidentität**.

Sie können nicht unterscheiden zwischen:

1. „Diese zwei Texte beschreiben dasselbe zugrundeliegende Phänomen" (echte Entsprechung)
2. „Diese zwei Texte sind im selben Sprachregister geschrieben" (zufällige Ähnlichkeit)

**Warum das hier besonders riskant ist:** Moderne spirituelle/Coaching-Sprache im Englischen hat ein auffällig kleines, extrem häufiges Vokabular ("shadow", "transformation", "authentic", "power", "flow", "growth", "energy"). Fast jede archetypische Beschreibung — egal aus welcher Tradition — wird von einer LLM in dieses Vokabular übersetzt, weil es die Trainingsdaten-Dichte widerspiegelt (Blogs, Coaching-Content dominieren das Netz zu diesem Thema). Das ist in der NLP-Forschung als Phänomen bekannt (u. a. "hubness" in hochdimensionalen Embedding-Räumen; Grund, warum STS-Benchmarks nötig wurden, weil rohe Embedding-Similarity nur mäßig mit "gleiche Bedeutung" korreliert und noch schwächer mit "gleicher Referent").

**Fazit:** Es geht nicht um „sprachlich ODER thematisch ODER Bedeutung" — Embeddings vermischen alle drei. Das ist normalerweise ein akzeptabler Kompromiss. Im vorliegenden Anwendungsfall ist die Vermischung aber **maximiert statt minimiert** (siehe §3).

---

## 3. Warum die dokumentierte Pipeline das Problem verschärft

Dokumentierter Ablauf (`architecture.md` §4):

```
PHASE 2: SYNTHESIS + EMBEDDINGS
  Alle Interpretationen pro Node → synthesize_node
    → canonical_description + synthesis_wordings
    → embedding (pgvector)

PHASE 3: CROSS-SYSTEM-MAPPING
  Embedding Cosine Similarity zwischen Systemen
    → Kandidaten (>0.75) → LLM-Validierung
    → sys_kg_edges (maps_to, cross_system, candidate)
    → Human Review → approved/rejected
```

Das Problem sitzt bereits in Phase 2, nicht erst in Phase 3. `synthesize_node` nimmt heterogene Quellentexte (HD-Kommentar, BaZi-Klassiker, Jyotish-Sutra) und komprimiert sie **absichtlich** in eine einheitliche, allgemeinverständliche englische Beschreibung. Das ist für Mehrsprachigkeit/Zugänglichkeit richtig (siehe §7 Sprachstrategie in `architecture.md`) — für den Vergleichsschritt aber kontraproduktiv, weil es genau die Signale wegbügelt, die echte von zufälliger Entsprechung unterscheiden würden: Herkunft/Etymologie, kombinatorische Rolle (welche anderen Elemente stehen dazu in Beziehung, was ist der Gegenpol), Mechanismus (wie wirkt das Element strukturell im System).

Cosine-Similarity auf diesem bereits homogenisierten Material addiert eine zweite Kompressionsstufe (ein einzelner Vektor pro Node). Am Ende vergleicht die Pipeline zwei Dinge, die aus unterschiedlichen Systemen stammen, aber beide durchs selbe "beschreibe das archetypisch auf Englisch"-Nadelöhr gelaufen sind — sie landen zwangsläufig nah beieinander. Das ist kein Bug im Embedding-Modell, sondern ein Artefakt der Pipeline-Reihenfolge.

---

## 4. Klarstellung: zwei verschiedene Synthese-Schritte (leicht zu verwechseln)

Ein naheliegendes (und eigentlich richtiges) Mentalmodell für Cross-System-Arbeit ist: *„Jedes System-KG wird zuerst unabhängig fertig gebaut, dann übereinandergelegt, und erst daraus entsteht eine gemeinsame Sprache."* Das ist im Kern korrekt — beschreibt aber nur **Phase 4**, nicht Phase 2:

| | Phase 2 „synthesize_node" | Phase 4 „Meta-Knoten" |
|---|---|---|
| **Wann** | Vor dem Cross-System-Overlay | Nach dem Cross-System-Overlay (nach Phase 3) |
| **Scope** | Pro einzelnem Knoten, **innerhalb eines Systems** (z. B. alle HD-Interpretationen von Gate 34) | Pro Cluster, **über mehrere Systeme** (3+ Systeme zeigen auf dasselbe) |
| **Zweck laut Doku** | Sprachneutralität — Quellen kommen in DE/ZH/SA/etc., KG soll einheitlich sein (`architecture.md` §7) | IC-eigene Sprache/Archetypen destillieren (Datenschicht E, `prd_v3.md` §9) |
| **Wird hier kritisiert?** | **Ja** — weil sein Output (nicht dafür gedacht) als Vergleichsbasis für Phase 3 zweitverwendet wird | Nein — das ist der späte, korrekte Ort für eine gemeinsame Sprache |

**Kern des Problems:** Ein Artefakt, das für Ziel A (Mehrsprachigkeit/Zugänglichkeit) gebaut wurde, wird in Phase 3 für Ziel B (maximale Unterscheidbarkeit zwischen Systemen) wiederverwendet. Diese zwei Ziele stehen in Spannung: Ziel A will Texte möglichst einheitlich/zugänglich machen, Ziel B bräuchte möglichst diskriminierende, quellennahe Merkmale. Diese Spannung ist in der Doku nirgends benannt.

**Einordnung:** Das ist kein „Drift" (ursprünglich gut geplant, dann im Verlauf verschlechtert) — es steht so bereits in der frühen Architektur-Fassung. Eher ein **unreflektierter Doppel-Zweck**, dessen Kosten erst sichtbar werden, wenn man Phase 3 konkret durchdenkt. Da Phase 3 laut `status.md` noch bei 0 % steht, ist jetzt der richtige Zeitpunkt zur Korrektur — vor jeglichem Code.

---

## 5. Liegt es nur an fehlendem Human Review?

**Nein.** Der Fehler ist methodisch, nicht nur ein fehlender Prüfschritt:

- Wenn die validierende LLM in Phase 3 **dieselben** `canonical_description`-Texte sieht, die auch embedded wurden, prüft sie im Grunde nur, ob sie der eigenen (bzw. einer geschwisterlichen) Homogenisierung zustimmt. Das ist **zirkulär** — beide LLM-Aufrufe haben dieselbe Tendenz zum "alles klingt nach Transformation und Energie"-Register.
- Ein zweiter LLM-Call mit denselben Eingaben ist damit im Wesentlichen ein **Rubber Stamp**, kein unabhängiger Check.
- Human Review fängt das zwar auf (Menschen mit echtem Domänenwissen erkennen "klingt gleich, ist aber mechanistisch etwas anderes"), aber Human Review **skaliert nicht** auf 50+ Mappings × 14 Systeme, und im aktuellen Schema gibt es keine Unterscheidung zwischen "faktisch sicher" und "schwache Resonanz" (siehe §7) — beides landet gleich aussehend im UI (leuchtender Mandala-Akzent), was das zentrale emotionale Versprechen der App ("kein Zufall") angreifbar macht.

---

## 6. Kann eine separate, "wissende" LLM-Validierung das lösen?

**Ja — aber nur unter vier Bedingungen.** Ohne sie ist es Kosmetik:

| Fix | Warum nötig |
|---|---|
| **Validierung auf Rohmaterial, nicht auf `canonical_description`** — die LLM bekommt die ursprünglichen K3/K4-Extraktions-Chunks beider Seiten (oder Ausschnitte aus Primärquellen), nicht die bereits homogenisierten Synthesetexte | Nur so hat sie Zugriff auf Signale, die die Homogenisierung entfernt hat |
| **Strukturkontext mitgeben**: mit welchen anderen Knoten ist das Element intra-system verbunden, was ist sein Gegenpol, welche kombinatorische Rolle hat es | Echte Entsprechung zeigt sich oft in der **Relationstopologie** (z. B. Erzeugungs-/Kontrollzyklus bei Wu Xing), nicht in der isolierten Beschreibung |
| **Adversarial Prompting**: die LLM muss explizit das stärkste Gegenargument formulieren ("warum könnte das NUR zufällige Sprachähnlichkeit sein?") und darf nur bestätigen, wenn sie kein starkes Gegenargument findet | Bekannte Technik gegen sykophantisches Bestätigen — naive Prompts ("passt das zusammen?") erzeugen fast immer "ja" |
| **Nullhypothese umdrehen**: Prompt-Rahmung "gehe davon aus, dass KEINE Entsprechung besteht, außer es gibt konkrete Textbelege aus beiden Quellen, die dieselbe Aussage treffen" | LLMs (trainiert auf viel synkretistischem New-Age-Material) haben einen eingebauten Bias Richtung "alles hängt zusammen" — dagegen muss man aktiv gegensteuern |

---

## 7. Konkrete Empfehlung: drei Korrespondenz-Klassen statt einer Confidence-Zahl

Aktuelles Schema (`contracts.md` §5, `IC_KG_Node_Edge_Schema_v1.1`): `maps_to`-Edges haben `confidence` (Float 0–1), `similarity_basis` (String), `human_reviewed` (Bool, Pflicht). Das ist gut, aber **eine einzige Zahl für drei kategorial verschiedene Arten von Entsprechung** reicht nicht — sie brauchen unterschiedliche Beweisstandards:

| Klasse | Beispiel | Evidenzbasis | Umgang |
|---|---|---|---|
| **`definitional`** (definitorisch/historisch belegt) | HD-Gate = I-Ging-Hexagramm-Nummer (Ra hat HD explizit aus dem I Ging abgeleitet) | Dokumentierte Herkunft, kein Fund | **Hartcodiert**, nicht durch Embedding-Pipeline "entdeckt". Konfidenz = faktisch sicher. |
| **`structural`** (strukturell/analog) | Fünf-Elemente-Systeme (Wu Xing, Ayurveda-Elemente) — Relationstopologie vergleichbar | Graph-Vergleich der intra-system-Kanten (erzeugt A wirklich B in beiden Systemen?) | Prüfbar, aber braucht Graph-Vergleich statt Cosine-Similarity auf Fließtext + LLM-Validierung mit Strukturkontext |
| **`thematic`** (thematisch/resonant) | Beide Systeme sprechen in ähnlichem Register über "Transformation" | Embedding-Similarity + adversariale LLM-Validierung auf Rohmaterial | **Schwächste Klasse**, höchste Fehlerrate — muss im UI sichtbar als "mögliche Resonanz" markiert werden, nicht wie ein Fakt |

**Schema-Erweiterung (additiv, kein Bruch):** `sys_kg_edges` um `correspondence_type` (`definitional | structural | thematic`) und `evidence_basis` (`documented_provenance | structural_analysis | embedding_similarity`) ergänzen.

---

## 8. Wo im Datenfluss ansetzen

- **Phase 2 (`synthesize_node`) bleibt bestehen** — Sprachneutralität ist weiterhin sinnvoll für UI/Mehrsprachigkeit.
- **Phase 3 darf sich nicht nur auf `canonical_description`-Embeddings stützen.** Zusätzlich heranziehen: Rohextraktion (`sys_interpretations` vor Synthese) + intra-system-Kantenkontext (`sys_kg_edges`, `edge_scope=intra_system`) für die LLM-Validierung.
- **`definitional`-Korrespondenzen** (z. B. HD↔I-Ging über Gate-Nummer) sollten **gar nicht** durch die Embedding-Pipeline laufen, sondern als deterministische Seed-Kanten direkt in Phase 0 (Strukturbäume) angelegt werden.

---

## 9. Status & nächster Schritt

Dies ist ein **offener Review**, keine `decisions.md`-Entscheidung. Vor Start Phase 3:

1. Entscheiden: Schema-Erweiterung (`correspondence_type`, `evidence_basis`) übernehmen oder bewusst ablehnen (Begründung).
2. Falls übernommen: Eintrag in `reference/decisions.md`, Verweis von `cursor/contracts.md` §5 und `cursor/architecture.md` §4 Phase 3.
3. Kleiner Validierungs-Spike vor Vollausbau: ~20 echte Cross-Mappings von einer Person mit Tradition-Kenntnis in beiden Systemen bewerten lassen ("trifft es wirklich" vs. "klingt nur ähnlich") — liefert eine Präzisionszahl, bevor die volle Pipeline gebaut wird.

## 10. Verweise

- `cursor/architecture.md` §4 (Datenfluss Phase 0–4), §7 (Sprachstrategie), §9 (Schlüsselentscheidungen)
- `cursor/contracts.md` §5 (Edge-Attribute: `maps_to`, `confidence`, `similarity_basis`)
- `reference/ontology_policy.md` (verwandtes, aber anderes Thema: WANN zwei `system_id` statt einer — nicht WIE Mapping-Qualität gesichert wird)
- `reference/decisions.md` 2026-04-19 (Konvergenz: personengebunden vs. strukturell — dieser Review vertieft den strukturellen Zweig)
- `reference/prd_v3.md` §3, §5 (USP-Anspruch, Datenschicht D+E)
