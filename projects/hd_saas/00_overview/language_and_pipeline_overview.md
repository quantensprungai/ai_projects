# Sprache, Gesamtprozess und nächste Schritte (HD-SaaS)

<!-- last_update: 2026-02-10 -->

## 0) Sprachmodell (verbindlich) – wie Sprache intern und extern funktioniert

Dieses Modell ist die **einzige verbindliche** Referenz für Backend, Worker und App.

### Intern (Backend / Worker / Datenmodell)

| Schicht | Rolle der Sprache | Regel |
|--------|--------------------|--------|
| **hd_interpretations** | **Quellenbasiert** | Interpretationen extrahieren wir aus dem **Originaltext** – in der **Sprache der Quelle**. DE-Buch → DE-Interpretationen; EN-PDF → EN. Interpretationen sind **keine** globale, mehrsprachig duplizierte Wahrheit; sie sind fachlich präzise, terminologieabhängig. **Nicht** in allen Sprachen speichern – das wäre falsch und ineffizient. |
| **hd_kg_nodes / hd_kg_edges** | **Sprachneutral** | KG speichert Struktur: node_key, node_type, dimensions, interactions. Dimensions-Werte sind inhaltlich strukturierter Content; die Sprache des gespeicherten Strings ist zweitrangig, weil die **Synthesis** daraus die nutzerorientierte Sprache erzeugt. KG = neutral, schulübergreifend. |
| **hd_synthesis_wordings** | **Sprachschicht (multilingual)** | Einzige Schicht, die bewusst **mehrsprachig** ist. Pro (node_id, language, version) eine Zeile. Beispiel: (node 39), language= en → EN-Synthesis; language= de → DE-Synthesis; language= fr → FR-Synthesis. **Multilingualität entsteht ausschließlich hier**, nicht über Interpretationen. |

**Fazit:**  
- **Interpretationen** = Originalsprache der Quelle (DEPENDS ON SOURCE).  
- **KG** = sprachunabhängig.  
- **Synthesis** = mehrere Sprachen, je eigene Zeile; Speichern ist Standard, **on-the-fly** nur für fehlende Sprachen oder exotische Locales (optional).

### Extern (UI / API / Nutzer)

- **UI-Sprache** ist unabhängig vom Knowledge-Content: Makerkit i18n (DE, EN, FR, …). UI-Sprache ≠ Content-Sprache.  
- **Content-Anzeige:** API fragt `hd_synthesis_wordings` mit `language = Nutzer-Locale`. Wenn die Sprache fehlt → Worker-Job `synthesize_node` mit `debug.language=xyz` nachziehen oder LLM-Übersetzung/Translation-Layer (on-the-fly erzeugen und speichern).

### Zentrale Antworten

- **„Müssen Interpretationen in allen Sprachen vorhanden sein?“** → **Nein.** Sie bleiben quellenbasiert.  
- **„Multilingualität on-the-fly bei der Output-Generierung?“** → **Optional.** Optimal: vorhandene Sprachen **speichern**; fehlende Sprachen **on-the-fly erzeugen und danach speichern** (schnell für User, versionierbar, befragbar).

### Schema `hd_synthesis_wordings` (multilingual)

Das aktuelle Schema ist bereits das empfohlene für Mehrsprachigkeit: Spalte **language**, Unique pro (account_id, node_id, language, version) bzw. (account_id, canonical_id, language, version). **Keine Schema-Erweiterung nötig** – nur weitere Zeilen pro Sprache anlegen.

---

## 1) Sprache: Speicherung vs. App vs. LLM-Extraktion

**Ziel:** HD (und später BaZi, Astro, …) strukturiert speichern und abrufen; App für Nutzer; Kopplung mehrerer Schulen/Systeme.

### Empfehlung

| Ebene | Empfehlung | Begründung |
|-------|------------|------------|
| **Interpretations (verbindlich)** | **Quellsprache** (siehe Abschnitt 0) | Pro Quelle/Asset: Extraktion in der **Sprache des Originaltexts**. Kein Duplizieren in viele Sprachen. |
| **LLM-Extraktion** | **Ausgabe in Quellsprache** (oder konfigurierbar) | Default: **Englisch** (`HD_LLM_EXTRACTION_LANG=en`) für internationale Basis; bei erkannter Quellsprache (z. B. `metadata.detected_language`) kann in dieser Sprache extrahiert werden. |
| **App (Anzeige)** | **i18n / Übersetzung in der App** | Nutzer wählt Sprache (DE/EN/…); Anzeige kommt aus Übersetzungs-Layer: entweder (a) vorgehaltene Übersetzungen (z. B. für kanonische Texte), (b) on-the-fly via LLM/Translation-API beim Abruf, oder (c) nur Speichersprache anzeigen wenn keine Übersetzung. Keine Änderung der Speicherlogik nötig. |

**Kurz:**  
- **Interpretations:** quellenbasiert (eine Sprache pro Quelle), **nicht** multilingual duplizieren.  
- **Kanonische technische Basis:** Englisch (KG, canonical_ids, Default für LLM/Synthesis).  
- **Synthesis:** multilingual (eine Zeile pro Sprache in `hd_synthesis_wordings`); speichern, fehlende Sprachen optional on-the-fly erzeugen.  
- **App:** Makerkit i18n für UI; Content aus DB (Synthesis in Nutzer-Sprache) oder nachziehen/Translation.

### Internationale App: viele Sprachen

**Ziel:** App soll international nutzbar sein; DE + EN reichen nicht für weltweiten Einsatz – Mehrsprachigkeit ist ein Kernvorteil.

| Ebene | Umsetzung |
|-------|-----------|
| **UI (Makerkit i18n)** | Einfach erweiterbar: in `i18n.settings.ts` weitere Sprachen in `languages` eintragen, unter `public/locales/<code>/` JSON-Dateien anlegen (common, auth, account, …). Keine Backend-Änderung nötig. |
| **Content (Interpretations, Synthesis)** | **Intern:** `hd_interpretations.payload` und `hd_synthesis_wordings` haben bzw. nutzen **Sprache** (Payload-Metadaten, Zeile pro Sprache). **Strategie:** (1) **Kanonisch EN** – Extraktion/Synthesis standardmäßig auf Englisch; (2) **Mehrsprachige Speicherung** – pro gewünschter Sprache Job mit `debug.language=fr` (etc.) ausführen oder Nutzer-Locale beim ersten Pipeline-Lauf übergeben → eine Zeile pro (node_id, language) in `hd_synthesis_wordings`; (3) **Alternativ:** nur EN speichern, bei Abruf per Translation-API oder Batch-Übersetzungs-Job weitere Sprachen erzeugen und ablegen. So können möglichst viele Sprachen abgebildet werden, ohne die Architektur zu sprengen. |
| **Default für Worker** | **Englisch** (`en`) als Default für `HD_LLM_EXTRACTION_LANG` und `debug.language`, sofern nicht User-Locale/Account-Einstellung übergeben wird. |

**Deutsch differenzierter:** Wenn ihr bewusst **Deutsch** als Speichersprache wollt (z. B. für HD-Fachbegriffe), dann: `HD_LLM_EXTRACTION_LANG=de`, Speicherung auf Deutsch, App zeigt DE direkt oder übersetzt für andere Locales. Cross-school (BaZi, …) kann trotzdem über `system` + canonical_ids laufen; Begriffe pro System können unterschiedliche Sprachen haben, solange `payload.language` gesetzt ist.

### Spracherkennung für MinerU (Chinesisch etc.)

- **Manuell:** `HD_MINERU_LANG=ch` (oder `en`, `latin`, `chinese_cht`) in der Worker-.env – alle PDFs werden mit dieser Sprache extrahiert.
- **Automatisch:** **HD_MINERU_AUTO_LANG=true** (und `HD_MINERU_LANG` leer): Worker extrahiert mit PyMuPDF die ersten Seiten als Stichprobe, erkennt die Sprache per **fast_langdetect** (mit MinerU bereits installiert) und übergibt das Ergebnis an MinerU (z. B. `ch` für Chinesisch, `en` für Englisch, `latin` für DE/FR/ES/…). Die erkannte Sprache wird in **asset.metadata.detected_language** und im Job-`debug` gespeichert; downstream (LLM, Anzeige) kann darauf zugreifen. **Metadaten:** Vor der Extraktion haben wir die Sprache nicht; nach extract_text steht sie in `metadata.detected_language`, wenn Auto-Lang aktiv war.

---

## 2) Wo stehen wir im Gesamtprozess?

| Schritt | Status | Beschreibung |
|---------|--------|---------------|
| A | ✅ | **Upload:** PDF → Storage (direkt), Server Action legt Asset, Document, Document_File, **extract_text**-Job an. |
| B1 | ✅ | **Textbasis:** extract_text (PDF) → PyMuPDF oder **MinerU** (bei HD_USE_MINERU) → Markdown/Text. **Sprache:** HD_MINERU_LANG fest oder **HD_MINERU_AUTO_LANG=true** (fast_langdetect auf ersten Seiten → ch/en/latin); Ergebnis in **asset.metadata.detected_language**. |
| B2 | ✅ | **Scan-Pfad:** extract_text_ocr (EasyOCR/GPU) oder MinerU hybrid. |
| B3 | ✅ | **Chunking:** heading-aware (MinerU) oder paragraph_accumulate → **hd_asset_chunks**. |
| B4 | ✅ | **classify_domain:** system_id (hd/bazi/astro/jyotish/…) → Asset-Metadaten. |
| B5 | ✅ | **extract_term_mapping:** Seed-Term-Mapping für **HD und BaZi** (canonical_ids); astro/jyotish erweiterbar. |
| B6 | ✅ | **extract_interpretations:** Bei **HD_LLM_EXTRACTION_URL** echte LLM-Extraktion (OpenAI-kompatibel); sonst Stub. |
| C | – | Extraction → KG (kg_nodes, kg_edges), Dynamics (später). |
| D | – | Synthesis (kanonische Formulierungen, Versionen). |
| E | – | Query/Chat (App/API, LLM-Antwort mit Quellen). |

**Aktueller Stand:** End-to-End **PDF → Chunks → classify_domain → extract_term_mapping (HD/BaZi) → extract_interpretations (LLM oder Stub)** läuft. LLM-Extraktion auf Spark (SGLang/Qwen 32B) getestet; Interpretations-Payload in `hd_interpretations` geprüft.

**Nach LLM-Prüfung – Reihenfolge C → D → E:** (1) **text2kg:** Interpretations (+ Term-Mapping) → `hd_kg_nodes`, `hd_kg_edges`. Ausarbeitung: `02_system_design/text2kg_spec.md`. (2) **extract_dynamics:** Dimensions + challenges/growth → Phasen/Traps/Growth (hd_dynamics). (3) **Synthesis:** KG + Interpretations + Dynamics → kanonische Formulierungen (hd_syntheses). (4) **Query/Chat:** App/API fragt KG + Interpretations ab, LLM antwortet mit Quellen.

**Nächste Schritte:** (1) text2kg im Worker implementieren (Spec liegt vor). (2) Später: extract_dynamics, Synthesis, astro/jyotish Term-Seeds.

---

## 3) Der eigentliche End-to-End-Prozess (Zielbild)

```
[App] PDF-Upload
    → Storage (Supabase)
    → Server Action: Asset, Document, Document_File, Job extract_text

[Worker]
  extract_text (PDF)     → MinerU oder PyMuPDF → Markdown/Text
                        → Chunking (heading-aware / paragraph) → hd_asset_chunks

  classify_domain        → system_id (hd | bazi | astro | …) → Asset.metadata

  extract_term_mapping   → (für HD empfohlen) Seed canonical_ids → hd_term_mapping

  extract_interpretations → pro Chunk:
                              → LLM (Chunk-Text, system_id) → strukturierter Payload
                              → Insert hd_interpretations (payload, chunk_id, system, element_type, element_id)

[Später]
  KG / Dynamics / Synthesis  → aus Interpretations + Term-Mapping
  App: Abruf, Anzeige, i18n  → Nutzer sieht HD (ggf. übersetzt)
  Multi-School               → gleiche Pipeline, system_id trennt HD/BaZi/…
```

**Kopplung mit weiteren Schulen (BaZi, etc.):**  
- Gleiche Tabelle `hd_interpretations`; `system` = `hd` | `bazi` | `astro` | …  
- Gleicher Contract (essence, mechanics, expression, dimensions, …); pro System eigene element_types/element_ids.  
- classify_domain setzt `system_id`; LLM-Extraktion bekommt system_id im Prompt und füllt payload systemspezifisch.

---

## 4) LLM-Extraktion (umgesetzt)

- **Wo:** Worker `extract_interpretations`: Bei gesetztem **HD_LLM_EXTRACTION_URL** wird ein OpenAI-kompatibles LLM (vLLM/SGLang) aufgerufen; sonst Stub.  
- **Env:** `HD_LLM_EXTRACTION_URL` (z. B. `http://spark:8000/v1/chat/completions`), `HD_LLM_EXTRACTION_LANG` (z. B. `en`), optional `HD_LLM_EXTRACTION_MODEL`, `HD_LLM_API_KEY`.  
- **Input:** Chunk-Text, system_id, lang → Prompt mit JSON-Schema; **Output:** Payload (essence, mechanics, expression, dimensions, interactions, evidence) gemäß Interpretations-Contract.  

Damit ist der Kernprozess **PDF → strukturierte HD (und andere Systeme) speichern und abrufen** geschlossen; App und Übersetzung bauen darauf auf.

---

## 5) Warum „extract_term_mapping“ optional? (HD + BaZi)

**„Optional“ heißt hier dreierlei:**

1. **Konfigurierbar:** Über `HD_ENABLE_TERM_MAPPING_SEED=false` kann der Schritt ausgeschaltet werden – dann: classify_domain → direkt extract_interpretations (ohne vorherigen Term-Seed).
2. **HD und BaZi:** Der Schritt wird bei `system_id in ("hd", "bazi")` gequeued; Seeds für HD und BaZi sind im Worker hinterlegt. Astro/Jyotish: Seeds ergänzbar, dann Enqueue analog erweitern.
3. **Pipeline läuft auch ohne:** extract_interpretations braucht die Term-Mapping-Tabelle nicht zwingend – der Stub/LLM schreibt Payloads; canonical_id kann später aus Term-Mapping nachgeschlagen werden.

**Empfohlen:** Der Seed füllt `hd_term_mapping` mit stabilen canonical_ids (HD: z. B. `hd.type.generator`, `hd.authority.sacral`; BaZi: z. B. `bazi.element.tian_gan`, `bazi.concept.yong_shen`). Das nutzt KG, Synthesis und konsistente Referenzen. **Fazit:** Für HD und BaZi nicht weglassen; „optional“ = technisch abschaltbar.

---

## 6) Local LLM vs. Cloud (GPT/Opus/Sonnet) für die Extraktion

**Frage:** Lokale LLMs auf Spark oder High-End-Cloud (GPT-5.2, Opus, Sonnet 4.5)? Qualität vs. Kosten bei vielen PDFs/Chunks?

### Qualität

- **Strukturierte Extraktion** (essence, mechanics, expression, dimensions) aus Chunk-Text ist ein **beschränktes Task**: Schema vorgeben, aus Text füllen. High-End-Cloud-Modelle (Claude Opus, GPT-4o, Sonnet) sind sehr stark bei Instruction Following und strukturiertem JSON; kleinere/lokale Modelle (z. B. Qwen3-32B, Llama4, DeepSeek) können das **ebenfalls**, wenn Prompt und Schema klar sind – ggf. mit etwas mehr Halluzination oder Lücken.
- **HD-Fachsprache:** Wenn das Modell HD-Begriffe (Type, Authority, Center, …) kaum kennt, hilft Cloud oft mehr (bessere Weltkenntnis). Lokale Modelle können mit **Few-Shot-Beispielen** oder **Feintuning** auf HD-Texte nachziehen.

### Kosten (grobe Orientierung)

| | Local (Spark) | Cloud (z. B. GPT-4o, Claude Sonnet) |
|--|----------------|-------------------------------------|
| **Kostenmodell** | Keine laufenden Kosten pro Token (Strom/Hardware fix) | $ pro 1M Input-/Output-Tokens (z. B. 2,50–10 $/1M output) |
| **Beispiel:** 100 PDFs, ~5000 Chunks, ~800 Token Input + ~400 Token Output pro Chunk | 0 € zusätzlich | 5000 × 400 output ≈ 2M output-Tokens → grob 5–20 € nur Output; plus Input |
| **Bei 10.000 Chunks/Monat** | 0 € | Deutlich höher (z. B. 50–200 €/Monat je nach Modell) |

Cloud wird bei **großer Chunk-Menge** schnell teuer; lokal ist bei euch durch Spark bereits vorhanden.

### Empfehlung

1. **Zuerst lokal (Spark):** vLLM/SGLang mit einem **fähigen Modell** (z. B. Qwen3-32B, Llama4-Scout, DeepSeek) nutzen – klarer Prompt, JSON-Schema, ggf. Few-Shot. Qualität auf einer **Stichprobe** (z. B. 50–100 Chunks) prüfen.
2. **Wenn Qualität reicht:** Bei lokal bleiben; Skalierung über Chunk-Menge kostet nichts extra.
3. **Wenn Qualität nicht reicht:** (a) Lokales Modell mit HD-Beispielen **feintunen**, (b) **Hybrid:** lokal für Bulk-Extraktion, Cloud nur für ausgewählte Assets oder Nachbearbeitung, (c) **Kritische Texte:** nur Cloud (Opus/Sonnet) für maximale Qualität.
4. **Cloud „zu teuer“?** Kommt auf Volumen an: Bei wenigen hundert PDFs/Monat ist Cloud machbar; bei tausenden Chunks/Monat ist lokal meist günstiger. Kosten pro Chunk vorher durchrechnen (Token-Schätzung × Cloud-Preis).

**Kurz:** Qualität kann ein lokales LLM liefern, wenn Prompt und ggf. Few-Shot/Feintuning stimmen. Mit Spark sinnvoll, **zuerst lokal** zu evaluieren; Cloud für Spitzenqualität oder gezielte Nachbearbeitung einplanen, wenn nötig.
