<!--
Reality Block
last_update: 2026-04-11
major_update: 2026-04-11 — Ziwei K1+ (heavenlyStems/earthlyBranches, Struktur-Kanten); BaZi shensha_aux; §7.5 Hanzi/UTF-8
major_update: 2026-04-11 — BaZi-Katalog-Extraktion @yhjs/bagua (§7.2/7.4 angepasst)
major_update: 2026-04-10 — Policy K1+K2 (Kit, möglichst voll) vs. K3+K4 (Literatur); §7.4 Kit-Code-Audit
status: Aktiv — Phase-1-Vorgehen pro Chart-System
scope: Wiederholbare Schritte Katalog → Struktur → Validierung → KG-Seed; Artefakt-Pfade; Referenz Ziwei; Extraktionsgrenze Kit vs. Ontologie
in_scope: Prozess, Konventionen, Dateiorte, Checkliste, Grenzziehung Phase 1 (inkl. Ziwei/BaZi)
out_of_scope: Kit-spezifische Fach-Tiefe (stehen in engines.md §6 / §15–16)
depends_on: cursor/engines.md, cursor/contracts.md, structure_descriptor_seed.md, schema_and_descriptor_specs.md
-->

# Engine-Integration — Playbook (Phase 1)

> **Ziel:** Jedes neue Chart-System (HD, BaZi, Ziwei, …) durchläuft **dieselbe Schichtung**: erst **Bausteine und Struktur** aus dem Kit dokumentieren und testen, dann **KG-Materialisierung** — ohne jedes Mal neu zu erfinden.

**Referenzimplementierungen:** **Ziwei** (iztro) — `cursor/engines.md` §15; **BaZi** (@yhjs/bazi) — §16. Code: `code/inner_compass_app/packages/engines/`.

**Policy — welche „Tiefe“ wann:**

| Schicht | Quelle | Anspruch in Phase 1 |
|---------|--------|---------------------|
| **K1 + K2** | Open-Source-Kit (Listen, Konstanten, exportierbare Tabellen, deterministische Struktur) | **Möglichst vollständig** aus dem Kit ziehen, sobald es technisch extrahierbar ist — stabile Canonical IDs, wenig Duplikat-Handpflege, keine künstliche Dünne. Details und Lücken: §7, §7.4. |
| **K3 + K4** | Literatur, Lehrtexte, Pipeline (MinerU+LLM) | **Nicht** aus Kits erwarten; **nicht** Ziel von „Phase‑1‑Kit‑Extraktion“. |

→ Kategorien und Tabellen: `cursor/engines.md` §2.

---

## 1. Pro System vs. gemeinsamer Ablauf

| Ebene | Vorgehen |
|-------|----------|
| **Artefakte** | Pro `system_id` **eigene** Dateien (Deskriptor, Katalog, Struktur, Tests). |
| **Konvention** | **Eine** gemeinsame Namens- und Schrittlogik (dieses Playbook). |
| **KG-Seed / DB** | **Ein** späterer Import-Mechanismus (`sys_kg_*`), der **nacheinander** alle „ready“-Systeme einliest — nicht zwangsläufig ein Big-Bang für alle Systeme am selben Tag. |

Cross-System-Kanten (Schicht D) kommen **nach** tragfähigen Einzelsystem-Graphen.

---

## 2. Artefakt-Orte (Konvention)

| Artefakt | Pfad | Zweck |
|----------|------|--------|
| **Deskriptor** | `projects/inner_compass/system_descriptors/{system_id}.json` | Regeln, `element_types`, `canonical_id_rules`, KG-Hinweise |
| **Katalog (Schritt 1)** | `projects/inner_compass/system_structure/{system_id}_catalog_v0.json` | Vollständiger **Baustein-Inventar** aus Kit (Labels, Konstanten, ggf. Regelblöcke) |
| **Struktur (Schritt 2)** | `projects/inner_compass/system_structure/{system_id}_structure_v0.json` | **Ebenen** (`levels`), statische **Kanten**, optional Mapping zu IC (`life_domain`, …) |
| **Engine-Code** | `code/inner_compass_app/packages/engines/` (oder `services/…` bei isoliertem Service) | Wrapper, Typen, `compute*` + Tests |

Namensmuster `{system_id}_catalog_v0.json` / `{system_id}_structure_v0.json` beibehalten; Version im JSON-`meta` hochziehen bei größeren Änderungen.

---

## 3. Schritte (wiederholbar)

### Schritt 0 — Spike (Proof)

- Kit einbinden, minimaler Input → Output.
- Entscheidung: Keep / Replace / ergänzen (`cursor/engines.md`, Kit-Tabelle).

### Schritt 1 — Katalog

- Alle **benannten Entitäten** und relevanten **Konstanten** aus dem Kit extrahieren (Script, manuell oder gemischt).
- Ausgabe: `{system_id}_catalog_v0.json` unter `system_structure/`.
- **Ziwei-Referenz:** Script `extract:ziwei-catalog` im Paket `@ic/engines`.

### Schritt 2 — Struktur

- **Ebenen** (`levels`): fachliche Schichtung (nicht an HD-Ton/Base koppeln — pro System eigen).
- **Kanten**: nur was **deterministisch** aus dem Kit folgt (Reihenfolgen, Regeln wie 五虎遁 — wenn im Kit).
- Optional: **Mapping** zu IC-Lebensbereichen (`contracts.md` §2), wo sinnvoll.
- **Ziwei-Referenz:** `build:ziwei-structure` → `ziwei_structure_v0.json`.

### Schritt 3 — Abgleich Engine ↔ Katalog

- Jede vom Engine gelieferte **canonical_id** / `nodes[]`-Liste muss auf den Katalog abbildbar sein (oder dokumentierte Fallback-Muster, z. B. Hash für ungemappte Labels).
- **Tests** im Code-Repo (Vitest o. ä.).
- **Ziwei-Referenz:** `validateZiweiNodesAgainstCatalog`, `ziwei-catalog-validation.test.ts`.

### Schritt 4 — KG-Seed (später, oft zentral)

- Ein **gemeinsamer** Import in `sys_kg_nodes` / `sys_kg_edges` aus Deskriptor + Katalog + Struktur + Validierung.
- Pro System nachziehen, sobald Schritt 1–3 grün sind — **nicht** alle Systeme zwinglich in einem Sprint.

---

## 4. Contracts & `system_id`

- Neues System: `system_id` in `cursor/contracts.md` (§4) ergänzen.
- Canonical-Format: `{system}.{element_type}.{element_id}` (`contracts.md` §9).

---

## 5. Checkliste (Copy-Paste pro System)

- [ ] `system_id` in `contracts.md`
- [ ] `system_descriptors/{system_id}.json` angelegt oder erweitert
- [ ] Schritt 1: `{system_id}_catalog_v0.json`
- [ ] Schritt 2: `{system_id}_structure_v0.json`
- [ ] Schritt 3: Tests: Engine-Output ⊆ Katalog (+ dokumentierte Ausnahmen)
- [ ] `cursor/engines.md` um Bewertung/Contract/Kurzreferenz ergänzt
- [ ] `cursor/status.md` aktualisiert
- [ ] (später) Schritt 4: Seed/DB dokumentiert in `architecture.md` / Pipeline

---

## 6. Verwandte Dokumente

| Datei | Inhalt |
|-------|--------|
| `cursor/engines.md` | K1–K4, Kit-Wahl, Ziwei §15, BaZi §16 |
| `structure_descriptor_seed.md` | Idee Deskriptor vs. Structure-Datei |
| `schema_and_descriptor_specs.md` | Descriptor-Schema |
| `system_structure/README.md` | Kurzindex der generierten JSONs |

---

## 7. Kit-Analyse: wo die Grenze liegt (Phase 1)

### 7.1 Ziel vs. Abgrenzung

**Ziel:** Alles, was im Kit als **stabile, benannte Bausteine** (Listen, Locales, Konstanten, exportierte Typen) vorliegt und für **Canonical IDs** + **Validierung** gebraucht wird, soll **in Katalog und Struktur** fließen — damit Literatur (K3/K4) später **pro Element/Kante** andocken kann.

**Phase-1-Grenze (bewusst):** Nicht „die gesamte traditionelle Ontologie eines Systems in einem Rutsch“, sondern:

| Mitgenommen (typisch) | Bewusst zurückgestellt / später |
|------------------------|----------------------------------|
| Benannte Entitäten aus Kit-Exports, Locales, `STARS_INFO` o. Ä. | Vollständige **Kombinatorik** (z. B. alle 60 甲子 als eigener Katalog-Eintrag), wenn sie nicht Schritt 1 braucht |
| Deterministische **statische** Struktur (Reihenfolgen, Ringe, dokumentierte Regel-Kanten wie 五虎遁/五鼠遁) | **Instanz-Daten** pro Geburt (Stern→Palast, konkrete 大运-Schritte) — das ist **Laufzeit-Engine**, kein statischer Vollgraph |
| Alles, was der Spike-Output als `nodes[]` referenziert und gegen den Katalog geprüft werden soll | Regeln, die nur **imperativ im Code** stecken und **nicht** als Tabelle exportiert sind → Extra-Spike: parsen oder aus Literatur ergänzen |
| Dokumentierte Fallbacks (z. B. Hash/Index-IDs bei fehlendem Locale-Mapping) | Schul-spezifische Feinheiten, die nur in K3/K4-Literatur konsistent sind |

**„Versteckt“** meint hier **nicht** „absichtlich weggelassen“, sondern: **nicht als fertige Liste im Repo**, obwohl das Kit sie intern berechnet — weil Extraktion Aufwand ist (Parser, zweiter Export-Pfad) oder weil es **Chart-Instanz** ist und in `*_structure_v0.json` nicht materialisiert wird.

### 7.2 Ziwei (iztro) und BaZi (@yhjs/bazi) — Stand der Grundstruktur

Beide Systeme sind **über Kit-Analyse** angebunden: Scripts lesen **sichtbare** Quellen im npm-Paket (Locales, Konstanten, Metadaten), der Spike liefert **Chart-Rohdaten**; Katalog + Struktur + Tests sind die **Phase-1-Anteile**. Es **kann** mehr werden (z. B. zusätzliche Tabellen aus dem Quellcode), ohne das Konzept zu ändern — das ist **iterative** K1/K2-Verdichtung.

| System | Grobe Einordnung K1/K2 aus Kit (gesamt) | Was Phase 1 im Artefakt **abdeckt** | Was überwiegend „im Kit, aber nicht voll in v0-JSON“ liegt |
|--------|----------------------------------------|-------------------------------------|------------------------------------------------------------|
| **Ziwei** | ~**75** % (siehe `engines.md` Gesamtübersicht) | Vollständiges **Baustein-Inventar** (Paläste, Sterne über Locales + `STARS_INFO` wo vorhanden); **statische** Kanten (Palast-Ring, 五虎遁/五鼠遁); Validierung Engine ⊆ Katalog | **Stern→Palast-Placements** und Zeitreihen pro Chart = Laufzeit; nicht alle Sterne mit gleicher Meta-Tiefe im Kit; Schul-Plugins können Randfälle haben |
| **BaZi** | ~**65** % (siehe `engines.md` Gesamtübersicht) | **十天干 / 十二地支 / 十神** + **六十甲子 / 纳音 / 旬空 / 十二长生 / 旬首** (`schema_version` ≥ 1.1) aus `@yhjs/bagua`; Säulen-Kette 年→月→日→时; **Beispielhafte** 大运 in `nodes` | **流年/流月** als Zeitreihen (kein endlicher Katalog); **神煞**-Hilfstabellen optional noch aus `@yhjs/bazi`-Quellcode nachziehbar |

Die **Prozentzahlen** sind **Schätzungen zur Einordnung** (Anteil „strukturell aus Kit ableitbar“ vs. „Interpretation/Literatur/Schul-spezifisch“), keine gemessenen Metriken. Feinere Prozentangaben pro Teilgraph wären möglich, lohnen sich erst bei konkreter Nacharbeits-Priorität.

### 7.3 Aufwand „noch aus dem Kit zu holen“

| Aspekt | Ziwei | BaZi |
|--------|-------|------|
| **Komplexität** | Mittel–hoch: viele Sterne, Locales, optionale Schul-Konfiguration — Katalog-Script ist schon der Hauptpfad | Mittel: Vokabular ist klein, aber **60 甲子** + vollständige Luck-/Flow-Auflösung als **statischer** Katalog ist extra Arbeit |
| **Typischer nächste Schritt** | Locale-Abdeckung für Nicht-zh-CN verbreitern; fehlende Meta-Felder aus Kit nachziehen | 甲子-Generierung oder -Export; Struktur um 流年 erweitern, wenn Produkt das braucht |

### 7.4 Konkrete Code-Sicht (Audit — was im Upstream liegt, was unsere Scripts tun)

> Stand der Analyse: Quellcode der Kits auf GitHub (nicht nur Schätzung). Unser `extract:*-catalog` im Code-Repo: `code/inner_compass_app/packages/engines/scripts/`.

**BaZi — `@yhjs/bazi` / `@yhjs/bagua` ([yihai-js/yihai-bagua](https://github.com/yihai-js/yihai-bagua))**

| Befund | Detail |
|--------|--------|
| **Aktuelles Extrakt-Script** | `extract-bazi-catalog.mjs` importiert **`@yhjs/bagua`** (`GANS`, `ZHIS`, `JIA_ZI_TABLE`, `TEN_GOD_NAMES`, …) und schreibt u. a. **60 甲子**; Slug-Konventionen bleiben an `bazi-pinyin.ts` gekoppelt (Kommentar im Script). `@yhjs/bazi` nur für Versions-Metadaten. |
| **60 甲子 + 纳音 + 旬空** | Über `JIA_ZI_TABLE` im Katalog **exportiert** (Stand: `bazi_catalog_v0` schema 1.1). |
| **神煞-Hilfstabellen** | In `packages/bazi/src/shensha.ts`: kleine Konstanten (驿马, 天乙贵人, 旺相休囚死) — **wenige hundert Zeilen**, klar tabellarisch. |
| **流年 / 流月** | `getLiunian` / `getLiuyue` liefern **Zeitreihen pro Chart** — kein endlicher „Katalog aller Jahre“; hier geht es um **API/Dokumentation**, nicht um JSON-Enumeration. |

| Aufwand (grobe Einordnung) | Einschätzung |
|----------------------------|--------------|
| **60甲子 + 纳音 + 空亡** im Katalog | **Erledigt** (schema 1.1); Pflege über `extract:bazi-catalog` |
| **神煞-Tabellen** in den Katalog | **Erledigt** (`bazi_catalog` `shensha_aux`, schema ≥ 1.2) |
| **十二长生** u. a. aus `packages/bagua/src/twelve-state.ts` | **Niedrig bis mittel** — abhängig von gewünschter ID-Konvention |
| **Fazit** | Das „Fehlen“ im v0-Katalog ist **keine** technische Sperre im Kit, sondern **bewusst knappe** Phase‑1-Extraktion; der größte Fleiß ist **Konsistenz** (IDs, Tests), nicht Reverse-Engineering. |

**Ziwei — `iztro` ([SylarLong/iztro](https://github.com/SylarLong/iztro))**

| Befund | Detail |
|--------|--------|
| **Aktuelles Extrakt-Script** | `extract-ziwei-catalog.mjs` zieht bereits **Locales zh-CN**, `STARS_INFO`, `constants.js` (u. a. `PALACES`, 五虎遁/五鼠遁) — **breiter** als BaZi v0. |
| **earthlyBranches / heavenlyStems** | **Im Katalog** (schema ≥ 1.1) + **Kanten** in `ziwei_structure_v0`: 干冲/支冲, 命主/身主→`ziwei.star.*`, 天干四化 (`stem_mutagen_*`). Textfelder (Hanzi) aus iztro. |
| **Chart-Instanz** | Stern→Palast-Belegung bleibt **Laufzeit** (wie zuvor). |

| Aufwand (grobe Einordnung) | Einschätzung |
|----------------------------|--------------|
| **earthlyBranches / heavenlyStems** + Kanten | **Erledigt** (`extract:ziwei-catalog`, `build:ziwei-structure`) |
| **Weitere Locales** (en, ja, …) analog `zh-CN` | **Niedrig pro Sprache**, wenn Keys gleich bleiben |
| **Fazit** | Großteil der **Benennungen** ist schon extrahiert; die **reicheren** Stammtabellen sind **ein zusätzlicher Export-Schritt**, kein Monatsprojekt. |

**K3/K4 ersetzen keine K1-Lücken**, können aber **benannte** Kanten oder Aliase liefern, die das Kit nicht als Liste führt — dann werden Katalog/Struktur **erweitert**, nicht „flexibel übersprungen“.

### 7.5 Chinesische Schrift (Hanzi) in Katalogen & Pipeline

**Technisch:** JSON, Postgres und gängige Toolchains sind **UTF-8** — Hanzi in Feldern wie `label_zh`, Kit-Originalbegriffe oder `health_tip_zh` sind **unkritisch** und **erwünscht** für **Quelltreue** (K1/K2 aus dem Kit).

**Architektur:** Primärschlüssel für Maschinenpfade bleiben **lateinische Slugs** (`canonical_id`, `*.key` wo möglich). Chinesisch dient als **Anzeige- und Literatur-Anker**, nicht als einziger Identifier.

**Pipeline / LLM:** Für Chunking, Suche und Embeddings **gemischte** Texte (DE/EN + Hanzi) sind normal — auf **konsistente Normalisierung** (NFC), passende **Collation** in DB und **Schriftart** in der UI achten. Problematisch ist nicht Hanzi an sich, sondern **fehlende** UTF-8-Kette irgendwo in der Verarbeitung (heute selten, wenn durchgängig UTF-8).

**Fazit:** Hanzi in Artefakten ist **gut für den Gesamtprozess** (Authentizität, spätere Literatur-Zitate); technisches Risiko liegt nur bei **falscher Encoding-Annahme** — nicht bei der Verwendung chinesischer Zeichen als solche.
