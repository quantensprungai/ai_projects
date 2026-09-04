---
last_update: 2026-09-03
status: active
scope:
  summary: "Canon-first Synthesis-Policy + Chat-Playbook. Mechanik-Wahrheit vor Literatur-Reichtum; Verify-before-write; Sanierung risikobasiert. Delta 2026-09-03: dünne Auth + Mix-Demote + Interpret-vor-text2kg."
  in_scope:
    - synthesis_status Enum + Placeholder
    - Evidence-Admission (binär) vs Score nur Sortierung
    - link_role primary|contrast|mention und Abgrenzung zu Edges/Interactions
    - Canon-Card Rollout + Sanierungs-Queue
    - Chat-Anleitung ohne Vorwissen
    - Dünne Authority-Nodes und Multi-Topic-Interps
  out_of_scope:
    - Full-Wipe / Full-Re-Synth aller Systeme
    - Implementierungsdetails jedes Workers (steht im Code)
notes:
  - "Decision: reference/decisions.md → 2026-08-13 Canon-first Synthesis; 2026-09-03 dünne Auth"
  - "Canon Auth/Def: reference/canon/hd_auth_def_canon_v1.yaml"
  - "Quality-Ist: cursor/reference/literature_content_wave_2026-07-18.md § Quality"
---

# Synthesis Canon-First — Policy & Playbook

> **Für jeden neuen Chat:** diesen File lesen + `reference/canon/hd_auth_def_canon_v1.yaml` wenn Auth/Def/Synth angefasst wird.  
> **Nicht** Coverage („viele Links“) mit Korrektheit verwechseln.

## 0) Chat-Anleitung (Copy für Agent)

```
Aufgabe betrifft synthesize_node / Wordings / Relink / Auth|Def Qualität:
1) Lies projects/inner_compass/cursor/reference/synthesis_canon_first.md (dieses Doc)
2) Lies projects/inner_compass/reference/decisions.md Eintrag 2026-08-13 Canon-first + 2026-09-03 dünne Auth
3) Bei Auth/Def: reference/canon/hd_auth_def_canon_v1.yaml als SoT für Mechanik
4) Regeln:
   - Canon-first; Evidence nur stützen
   - Kein Write bei blocked; Placeholder statt erfundener Prosa
   - Verify-before-write (Regeln zuerst; Check-LLM nur wenn nötig)
   - Kein Full-Wipe; Sanierung nur Risiko-Queue
   - contrast/mention nicht default in Synth-Context; Edges/Interactions sind anderer Pfad
   - Default-Synth nur jovian; Schulen (Blue I Ching, Cosmic Way) nicht in denselben Wording-Topf
   - Dünne Auth (ego_*/self_projected): Mix demoten, nicht re-synthen; Interpret prüfen vor text2kg (synthesis_canon_first.md §3.4)
5) Pipeline-Kontext: cursor/pipeline.md § synthesize_node + code/.../scripts/ic_worker.py
   Schulen-Mapping: cursor/engines.md §6.7b + decisions.md 2026-08-13 HD-Schulen
```

## 1) Entscheidung in einem Satz

**Mechanik-Wahrheit kommt aus Canon-Cards; Literatur-Interps dürfen nur belegen/ausschmücken; nichts UI-Taugliches ohne Verify-Gate; dünne Evidenz = blocked/canon_fallback, nie Halluzination.**

## 2) Status-Enum (Steuerung, nicht „Confidence-Gefühl“)

| `synthesis_status` | Bedeutung | UI / Chart? |
| --- | --- | --- |
| `blocked` | Zu wenig clean Evidence **und** kein nutzbarer Canon-Fallback gewählt | **nein** |
| `canon_fallback` | Kurzer Canon-Text, Literatur dünn/giftig | ja, mit Flag / Review-Hinweis |
| `synth_draft` | LLM gelaufen, Verify noch nicht grün | **nein** (intern) |
| `verified` | must_cover erfüllt, forbidden nicht verletzt, kein `hd.…` im Text | **ja** |

Placeholder (immer gleiches Muster, maschinenfindbar):

```text
[UNSYNTHESIZED:{canonical_id}] Insufficient clean evidence; awaiting review.
```

- Bei `blocked`: `canonical_description` = Placeholder (oder leer + Status); **keine** Styles als echte Prosa.
- `confidence` / weiche Scores **steuern nicht** den Write — höchstens Telemetrie.
- `dropped_claims[]` = Audit (welche Excerpt-Claims verworfen), optional.

## 3) Pipeline-Logik (Soll)

```
Links am Node
  → Admission (binär: rein / raus)
  → Sortierung (optional Score nur unter Admitted)
  → Synth(Canon + admitted primary excerpts)
  → Verify (Regeln; ggf. Check-LLM)
  → Write nur bei verified | bewusst canon_fallback
  → sonst blocked + Placeholder
```

### 3.1 Evidence-Admission (binär)

**Rein nur wenn:**
- nicht Stub/TOC/Meta-Müll
- Target klar Hauptthema (`link_role=primary` sobald vorhanden; sonst Heuristik „primary-like“)
- kein forbidden-Hit als *Mechanik dieses Nodes*
- bei Definition/Authority: Layer passt (kein Strategy-Overview als einziger Beleg)

**Raus:** contrast, mention (für Synth), Gift-Nachbar-Mechanik, leere Essences.

Score höchstens: Reihenfolge der admitted Excerpts (max ~6–8). **Nie** „0.73 → darf rein“.

### 3.2 Vergleichs-Chunks — Empfehlung

| Option | Empfehlung |
| --- | --- |
| Gar nicht in Synth-Context | ✅ **default**, solange `link_role` fehlt: Vergleich/Multi-Topic **nicht** synth’en |
| Sätze auf Target trimmen | später optional (Aufwand); nicht MVP |
| `link_role=contrast` | ✅ **Soll-Zustand**: Link behalten, Synth ignoriert default |

**Empfehlung:** Sofort Synth-seitig Vergleichs-/Multi-Topic ausschließen; parallel Relink auf `link_role` umstellen. Nicht zuerst teures Sentence-Splitting.

### 3.3 `link_role` vs Edges / Interactions

Das sind **zwei Pfade**:

| Pfad | Nutzt | Ziel |
| --- | --- | --- |
| **Node-Wording-Synth** | nur `primary` (+ Canon) | korrekter Text *für diesen Node* |
| **Beziehungen** | auch `contrast` / `mention` + `payload.interactions` + `sys_kg_edges` (`amplifies`, `depends_on`, `clashes_with`, …) | wie Elemente zueinander stehen |

- `contrast` / `mention` sind **nicht wertlos** — sie sind oft die besten Inputs für **K3/Edges/Overlay**, nur **schlechte** Inputs für Single-Node-Prosa (Vermischungsrisiko, siehe ego_projected ← G/25-51).
- Bestehende Edge-Backfill-Policy: `reference/decisions.md` → „2026-08-05: Element-Verbindungen“.

| role | Synth-Wording | Edges / Interactions |
| --- | --- | --- |
| `primary` | ja | ja |
| `contrast` | **nein** (default) | **ja** (Abgrenzung, clashes, „unlike X“) |
| `mention` | **nein** (default) | **ja** (schwache Ko-Erwähnung; vorsichtig gewichten) |

### 3.4 Dünne Nodes + Interpret-vor-text2kg (2026-09-03)

**Dünn ist ein Literatur-Limit, kein Relink-Bug.** `ego_manifested` / `ego_projected` / `self_projected` haben Primaries (Four Views + kurze Canon-Atome 13.08.). Mehr Links oder ein Re-Synth machen sie nicht reich. KARTE zeigt das Atom; der Mix lag in einem `primary`, das den nächsten Synth vergiften würde.

| Schritt | Tun | Nicht |
| --- | --- | --- |
| Mix-Interp (zwei Authorities in einer Essence) | `primary` → `mention` (oder `contrast` zum Geschwister-Node) | Chunk/Interp umschreiben; Satz splitten (MVP) |
| Neues Buch | TOC, dann Interpret mit `enqueue_text2kg: false`, Essence der dünnen Nodes gegenlesen | Worker-Continuation ungeprüft text2kg enqueuen (`ic_worker.py` setzt `true`) |
| Relink | dry-run → apply **ohne** `--synth` | `--apply --synth` auf Auth/Def |
| Synth | nur `--only-id`, nur wenn Primaries **besser** als das Atom | dünne Atome `--force` „aufkochen“ |
| `text2kg_unmatched` Cap 200 | Whitelist/unresolved-Rauschen | nicht mit „dünnen Nodes“ gleichsetzen |

Self-Projected ≠ Mental Projector / Outer Authority. Canon-`forbidden` + Relink `_essence_about` (Mental Projector in der **vollen** Essence, nicht nur im Lead). Ist-Beispiel: Definitive `10829c13` demoted 2026-09-03.

Restbücher (Black Book, Book of Letters, Resonance Mapping): **nicht** für diese drei Nodes. Park-Liste: `literature_hd_toc_coverage_2026-08-11.md` Delta 2026-09-03.

## 4) Verify-before-write

### 4.1 Regel-Verifier (default, Auth/Def zuerst)

Vor jedem Write:
1. kein `hd.` / Canonical-ID in Prosa  
2. alle `must_cover`-Gruppen getroffen (Regex/Any-of aus Canon-YAML)  
3. kein `forbidden`-Hit  
4. bei leerem/Placeholder-Output → Status `blocked`, kein Fake-Fließtext  

Fail → **kein Patch** der Wordings (`synth_rejected` / Status bleibt draft/blocked).

### 4.2 Check-LLM — wann und wie

**Nicht** als Ersatz für Canon. **Nur** wenn:

- Layer/Node in Canon `verify: semantic` (Sprache zu variabel für Regex), **oder**
- Regel-Verifier **inconclusive** (z. B. must_cover semantisch da, Regex blind), **oder**
- Human/Job explizit `force_semantic_verify=true`

**Wie:**
- Input: `canonical_id`, Canon-Card (must/forbidden/is), Draft-Text  
- Output strikt: `{ "pass": bool, "violations": string[], "missing_must": string[] }`  
- Temperature 0; kein Umschreiben im Check-Call — nur Urteil  
- Fail → kein Write (gleich wie Regel-Fail)

Auth/Def v1: **nur Regel-Verifier**. Check-LLM erst wenn wir sehen, dass Regex echte False-Fails erzeugt.

## 5) Synth-Prompt (Soll-Vertrag, nicht der alte Worker-Text)

Global hart:
1. Nur Canon + admitted Excerpts; sonst `blocked`  
2. Nur dieser Node  
3. Nie Canonical-IDs im Output  
4. Nicht erfinden (Channels, Zentren, Prozentsätze außerhalb Canon/Excerpts)  
5. Konflikt → Canon gewinnt; Claim nach `dropped_claims`  
6. Thin → `canon_fallback` oder `blocked`, **nie** aufblasen  

Node dem LLM als **Human-Label** geben (`Ego-Projected Authority`), nicht als `hd.authority.ego_projected`-Prosa-Seed.

Vollständiger Prompt-Text wird bei Implementierung in `ic_worker.py` gezogen; **Policy hier ist SoT**.

## 6) Canon-Cards — Rollout (nicht alles sofort)

| Priorität | Layer / Systeme | Form |
| --- | --- | --- |
| P0 | HD `authority`, `definition` | YAML pro Node — **liegt vor** (`hd_auth_def_canon_v1.yaml`) |
| P1 | HD `type`, `strategy`, `signature`, `not_self*` | YAML pro Node |
| P2 | HD `center`, `circuit` | kompakt |
| P3 | HD Gates/Channels/Lines/Crosses | **Template** + Instanz-Felder (Zahl, Keynote, Paar) |
| Px | BaZi / Gene Keys / … | gleiches Muster **wenn** das System angefasst wird |

Muster für alle Systeme: ja. Sofort alle Nodes handschreiben: nein.

## 7) Bestand — was nacharbeiten?

**Kein Full-Wipe / kein Full-Re-Synth.**

| Klasse | Aktion |
| --- | --- |
| Forensic **BAD** (falsche Mechanik) | sofort: Admission + Canon + Verify + Re-Synth |
| **WARN** (`hd.…` Artefakt, weiche Formulierung) | Re-Synth oder Strip + Verify |
| Layer mit stabilem Sign-off (viele Gates/Channels/…) | **nicht** anfassen; Stichproben-Audit wenn UI ausspielt |
| Dünne Nodes | `blocked` / `canon_fallback` ehrlich |
| Neue Wellen | ab Umstellung nur neuer Pfad |

Aktuelle BAD-Queue (2026-08-12/13 Forensic):
- `hd.authority.ego_projected` (G/25-51)
- `hd.authority.self_projected` (splenic-Klang, fehlt Throat/talk)
- `hd.definition.none` (Authority/Strategy-Vermischung; 2 irrelevante Links)
- WARN: `hd.authority.ego_manifested` (+ andere) mit `hd.…`-Prefix

## 8) Doku-Landschaft — reicht’s?

| Doc | Rolle |
| --- | --- |
| **Dieses File** | Policy + Chat-Playbook (SoT Qualität Synth) |
| `reference/decisions.md` | verbindliche Decision |
| `reference/canon/*.yaml` | Maschinen-Canon |
| `cursor/pipeline.md` | Job-Überblick + Pointer hierher |
| `cursor/handover.md` | Kontext-Block Pointer |
| Quality-Ist Wave-Doc | Befund/Historie, nicht Policy |

**Separater „Doku-Umbauplan“: Overkill.** Fehlt war diese Schicht — nicht die ganze Landkarte.  
Schulen/Linsen: `engines.md` §6.7b + `decisions.md` 2026-08-13 — **nicht** in Default-Synth mischen.

## 8b) Default-Tradition

Synth-Write auf `canonical_wording` / Default-Linse = **`jovian`**. Andere `tradition`s erst wenn das Feld am Interp existiert und die Linse es anfordert. Blue I Ching und Cosmic Way **nicht** in denselben Topf wie S0-Gates.

## 9) Implementierungs-Backlog

1. [x] Canon YAML laden in Worker (`ic_synth_canon.py` + `IC_CANON_PATH`)  
2. [x] Admission + Prompt-Rewrite + Verify-before-write (`IC_SYNTHESIS_CANON_FIRST`)  
3. [x] `link_role` Auth/Def Relink (`interpretation_link_roles` + `--retag-roles`)  
4. [x] Re-Synth BAD/WARN Auth/Def (canon_fallback wo Evidence giftig)  
5. [x] `link_role` Type/Strategy Relink analog (`ic_hd_type_strategy_relink.py`)  
6. [ ] Canon P1 Type/Strategy/Signature  

**Nicht:** Full-Corpus-`link_role` auf Gates/Channels/Lines/Crosses, solange die KARTE nur das Atom zeigt. Relink = Schicht wo Inspector/Overlay Facetten braucht.  

## 11) Vorstufen — was ist Fehlerquelle, was jetzt prüfen?

| Step | Fehlerquelle für Wordings? | Jetzt tun? |
| --- | --- | --- |
| **MinerU / Chunking** | Mittel: Narrative Bücher = lange Multi-Topic-Chunks (Vergleichskapitel). **Nicht** Hauptbug für Gates (dort helfen Chunk-Profile). | **Kein** Re-Chunk Four Views/HA2 jetzt. Profile nur bei strukturierten Werken (Gates/Crosses) weiter pflegen. |
| **K1/K2 Seed** | Niedrig für Auth/Def (IDs existieren). | Nur wenn Canonical fehlt/falsch — nicht der Gift-Fall. |
| **Interps** | Mittel: LLM extrahiert treu aus **gemischtem** Chunk → Misch-Essence. | Kein Full-Re-Interpret. Mit `link_role`+Admission reicht für Wording. |
| **text2kg / Relink** | **Hoch:** Recall ohne Rolle = Gift in Synth. | **Jetzt:** `link_role` (dieses Update). |
| **Synth** | Hoch ohne Canon/Verify — **behoben**. | Canon-first anlassen. |
| **Edges/Overlay** | eigener Pfad; profitiert von `contrast`. | später Hygiene, nicht jetzt Full-Audit. |

**Historische Gesamt-QA aller Steps?** Nicht flächendeckend. **Risiko-Queue:** Auth/Def nach `retag-roles` (+ Stichprobe Strategy). Gates/Channels nur wenn UI/Anomalie. Full-Corpus-Reprocess = Overkill und Wipe-Risiko.

## 10) Content-Streams — was parallel läuft, was separat ist

| Stream | Zweck | Heute | Parallel zu Synth? |
| --- | --- | --- | --- |
| **A Struktur (K1/K2)** | Seed-Nodes/Edges aus Deskriptor | ✅ | vor Content |
| **B Bedeutung** | `extract_interpretations` → Interps | ✅ | vor Synth |
| **B→Node Link** | text2kg / Relink | ✅ | vor Synth |
| **B→Wording** | `synthesize_node` (dieses Doc) | ✅ Canon-first | **eigener** Job |
| **C Beziehungen pro Element** | `payload.interactions` (amplifies/depends_on/clashes_with) | ⚠️ im Interp-Prompt mitextrahiert; Backfill → `sys_kg_edges` | **Mit-Extraktion**, kein eigener Qualitäts-Stream |
| **C Prozesse pro Element** | `payload.process` (trap/gift/…) | ⚠️ befüllt, kaum genutzt | Mit-Extraktion |
| **C kombinatorisch** | `sys_dynamics` / Pattern-Traps | ❌ eigener Job geplant | separat, bewusst später |
| **D Cross-System maps_to** | Phase 3 | ❌ (Review offen) | separat nach Content-Reife |
| **E Meta-Knoten** | Clustering | ❌ | nach D |
| **Overlay (Read-time)** | Chart-Kombinationstexte | ❌ geplant | **nicht** Precompute-Synth |

**Antwort auf „Beziehungen parallel?“:**  
Teilweise **mit** im Interp-Payload (`interactions`), aber **nicht** als eigener sauberer Stream mit Canon/Verify. Node-Wording-Synth ist bewusst getrennt — richtig so.  
Beziehungen sollen **nicht** denselben Prompt wie Wordings füttern; sie brauchen später eigenen Admission/Review-Pfad (oder strengeren Backfill), besonders `contrast`-Links.

**Was noch fehlen sollte (Priorität):**  
1. Wording-Qualität (hier)  
2. `link_role` am Relink  
3. Beziehungs-Hygiene/Review auf Edges (nicht Full-Neu-Job sofort)  
4. Overlay read-time  
5. Phase 3/E nach Reviews
