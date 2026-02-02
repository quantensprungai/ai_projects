<!-- Reality Block
last_update: 2026-01-30
status: stable
scope:
  summary: "Kompletter Workflow-Guide: Von Topics zu Knowledge Graph (HD-SaaS Ingestion, Duplikat-Prävention, Topic-Unterscheidung)."
  in_scope:
    - end-to-end workflow (topics → metadata → assets → ingestion → KG)
    - duplicate prevention in HD-SaaS
    - topic/profile differentiation in database
    - downstream processing control
  out_of_scope:
    - technical implementation details (siehe code/docs/)
    - setup instructions (siehe code/docs/setup/)
notes: []
-->

# Kompletter Workflow-Guide: Von Topics zu Knowledge Graph

## Übersicht

Dieser Guide erklärt den **kompletten Workflow** von der Topic-Sammlung bis zur Knowledge-Graph-Erstellung in HD-SaaS, inklusive Duplikat-Prävention und Topic-Unterscheidung.

## Workflow-Übersicht

```
1. Topics definieren (topics.txt)
   ↓
2. Metadaten sammeln (libgen_metadata_collector.py)
   ↓
3. Assets exportieren (export_assets.py) → assets.jsonl
   ↓
4. Downloads (fast_download_acquire.py) → PDFs lokal
   ↓
5. Upload zu HD-SaaS (assets.jsonl hochladen)
   ↓
6. Ingestion (automatisch) → hd_assets Tabelle
   ↓
7. Weiterverarbeitung (Worker) → Chunks → Classification → KG
```

## 1. Topics definieren und erweitern

### Aktuelle Topics-Liste

**Datei:** `code/annas-archive-toolkit/projects/hd_content/topics.txt`

**Aktuell:** 107 Topics (Human Design fokussiert)

### Weitere Inhalte hinzufügen (z.B. BaZi)

**Auf VM105 (Windows):**
```powershell
# Öffne topics.txt
code code\annas-archive-toolkit\projects\hd_content\topics.txt

# Füge neue Topics hinzu:
# BaZi / Four Pillars
bazi
four pillars
八字
四柱
stem branch
heavenly stem
earthly branch
pillar
```

**Übertragen:**
```powershell
powershell -ExecutionPolicy Bypass -File code\annas-archive-toolkit\transfer_to_vm102.ps1
```

**Hinweis:** Topics können gemischt sein (HD + BaZi). Die Relevanz-Filterung findet alle relevanten Items.

## 2. Metadaten sammeln

**Auf VM102 (Linux):**
```bash
export AAT_CONFIG=projects/hd_content/config.json
export AAT_TOPICS=projects/hd_content/topics.txt
python3 src/libgen_metadata_collector.py
```

**Output:** `output/hd_content/metadata.json`

**Wichtig:** Alle gefundenen Items werden gesammelt, unabhängig vom Topic.

## 3. Assets exportieren (HD-SaaS Contract)

**Auf VM102 (Linux):**
```bash
export AAT_CONFIG=projects/hd_content/config.json
python3 src/export_assets.py
```

**Output:** `output/hd_content/assets.jsonl`

**Format:**
```json
{
  "title": "Human Design System",
  "source_type": "book",
  "source_ref": "4688baa6786530ab2b9f155594a5f359",
  "metadata": {
    "profile_id": "hd_content",
    "topic": "human design",
    "authors": ["Ra Uru Hu"],
    "md5": "4688baa6786530ab2b9f155594a5f359",
    "collected_at": "2026-01-30T10:00:00.000Z"
  }
}
```

**Wichtig:** 
- `source_ref` = MD5 (eindeutiger Identifier)
- `metadata.profile_id` = "hd_content" (kann später erweitert werden)
- `metadata.topic` = Topic aus Collection (z.B. "human design", "bazi")

## 4. Downloads (Fast-Download)

**Auf VM102 (Linux):**
```bash
# Limit prüfen
python3 src/check_daily_limit.py

# Downloads starten
set -a; source /etc/annas-archive-toolkit/member.env; set +a
python3 src/fast_download_acquire.py --max-items 50
```

**Output:** PDFs in `output/hd_content/downloads/fast_download/`

**Status:** `acquire_queue.json` wird aktualisiert (`completed` / `failed`)

**Technische Details:** Siehe `../../code/annas-archive-toolkit/docs/FAST_DOWNLOAD_SETUP.md`

## 5. Upload zu HD-SaaS

### assets.jsonl hochladen

**Via HD-SaaS UI oder API:**
- Upload `assets.jsonl` zu HD-SaaS
- Wird in `hd_assets` Tabelle gespeichert

### Duplikat-Prävention ✅

**Wie funktioniert es:**
- **Unique Constraint:** `(account_id, source_ref)` in `hd_assets` Tabelle
- **Upsert-Logik:** Bei Upload wird `upsert` mit `onConflict: 'account_id,source_ref'` verwendet
- **Ergebnis:** Gleiche MD5 = Update statt Duplikat

**Beispiel:**
```sql
-- Erster Upload
INSERT INTO hd_assets (account_id, source_ref, title, metadata)
VALUES ('account-123', 'md5-abc', 'Human Design', '{"topic": "human design"}');

-- Zweiter Upload (gleiche MD5)
UPSERT INTO hd_assets (account_id, source_ref, title, metadata)
VALUES ('account-123', 'md5-abc', 'Human Design Updated', '{"topic": "human design", "year": 2024}');
-- → Update statt Duplikat!
```

**Praktisch:**
- ✅ Mehrfaches Hochladen von `assets.jsonl` erzeugt keine Duplikate
- ✅ Updates werden automatisch angewendet
- ✅ Gleiche MD5 = gleiches Asset (unabhängig von Topic)

## 6. Topic/Profile-Unterscheidung in der DB

### Wie unterscheidet man Assets nach Topics?

**In Supabase/PostgreSQL:**
```sql
-- Alle Human Design Assets
SELECT * FROM hd_assets 
WHERE metadata->>'topic' = 'human design';

-- Alle BaZi Assets
SELECT * FROM hd_assets 
WHERE metadata->>'topic' = 'bazi';

-- Nach Profile-ID filtern
SELECT * FROM hd_assets 
WHERE metadata->>'profile_id' = 'hd_content';

-- Kombiniert: HD Assets aus hd_content Profile
SELECT * FROM hd_assets 
WHERE metadata->>'profile_id' = 'hd_content'
  AND metadata->>'topic' = 'human design';
```

### Index für Performance

**Empfohlen (falls noch nicht vorhanden):**
```sql
-- Index für Topic-Filterung
CREATE INDEX IF NOT EXISTS ix_hd_assets_metadata_topic 
ON hd_assets USING GIN ((metadata->>'topic'));

-- Index für Profile-ID-Filterung
CREATE INDEX IF NOT EXISTS ix_hd_assets_metadata_profile_id 
ON hd_assets USING GIN ((metadata->>'profile_id'));
```

## 7. Entscheidung: Was wird weiterverarbeitet?

### Status-Felder in hd_assets

- `status`: `queued` | `processed` | `failed`
- Assets mit `status: 'queued'` werden vom Worker verarbeitet

### Filterung nach Topics/Profiles

**Option 1: In der DB filtern (empfohlen)**
```sql
-- Nur Human Design Assets verarbeiten
UPDATE hd_assets 
SET status = 'queued'
WHERE metadata->>'topic' = 'human design'
  AND status = 'processed';  -- Falls bereits verarbeitet, zurücksetzen
```

**Option 2: Im Worker filtern**
- Worker kann `metadata->>'topic'` prüfen
- Nur bestimmte Topics verarbeiten

**Option 3: Separate Profile-IDs**
- Erweitere `profile_id` in `metadata`:
  - `"profile_id": "hd_content"` → HD Assets
  - `"profile_id": "bazi_content"` → BaZi Assets
- Filtere nach `profile_id` statt `topic`

### Classification-Stufe (L3)

**Automatisch im Worker:**
- Chunks werden klassifiziert: `HD|BaZi|Astro|GeneKeys|Mixed|Other`
- Gespeichert in `hd_classifications` (falls vorhanden)
- Kann manuell überprüft werden

**SQL-Abfrage:**
```sql
-- Zeige Classification-Verteilung
SELECT 
  metadata->>'topic' as topic,
  COUNT(*) as count,
  COUNT(*) FILTER (WHERE status = 'processed') as processed
FROM hd_assets
GROUP BY metadata->>'topic';
```

## 8. Weiterverarbeitung (Worker-Pipeline)

**Detaillierte Anleitung:** Siehe `hd_saas_processing.md`

### Automatischer Workflow (geplant)

1. **Upload assets.jsonl** → `hd_assets` (status: `queued`) ✅ **implementiert**
2. **Worker verarbeitet (🚧 geplant):**
   - PDF → Text (OCR/Extraction)
   - Text → Chunks (`hd_asset_chunks`)
   - Chunks → Classification (`hd_classifications`)
   - Classification → Knowledge Graph (`hd_kg_nodes`, `hd_kg_edges`)
3. **Status-Update:** `queued` → `processed`

### Manuelle Steuerung

**Nur bestimmte Topics verarbeiten:**
```sql
-- Setze nur HD Assets auf queued
UPDATE hd_assets 
SET status = 'queued'
WHERE metadata->>'topic' = 'human design'
  AND status != 'queued';
```

**Nur bestimmte Profile-IDs verarbeiten:**
```sql
-- Setze nur hd_content Assets auf queued
UPDATE hd_assets 
SET status = 'queued'
WHERE metadata->>'profile_id' = 'hd_content'
  AND status != 'queued';
```

## 9. Workflow für weitere Inhalte (BaZi, etc.)

### Schritt-für-Schritt

**1. Topics erweitern:**
```bash
# Auf VM105
code code/annas-archive-toolkit/projects/hd_content/topics.txt
# Füge hinzu: bazi, four pillars, 八字, etc.
```

**2. Metadaten neu sammeln (optional):**
```bash
# Auf VM102
python3 src/libgen_metadata_collector.py
# → Findet jetzt auch BaZi-Items
```

**3. Assets exportieren:**
```bash
python3 src/export_assets.py
# → assets.jsonl enthält jetzt HD + BaZi Items
# → metadata.topic unterscheidet: "human design" vs "bazi"
```

**4. Downloads:**
```bash
python3 src/fast_download_acquire.py
# → Lädt alle relevanten Items (HD + BaZi)
```

**5. Upload zu HD-SaaS:**
- Upload `assets.jsonl` (enthält HD + BaZi)
- Duplikate werden automatisch verhindert (MD5-basiert)

**6. Weiterverarbeitung steuern:**
```sql
-- Nur HD Assets verarbeiten
UPDATE hd_assets SET status = 'queued'
WHERE metadata->>'topic' = 'human design';

-- Oder: Nur BaZi Assets verarbeiten
UPDATE hd_assets SET status = 'queued'
WHERE metadata->>'topic' = 'bazi';
```

## 10. Best Practices

### Duplikat-Prävention

✅ **Funktioniert automatisch:**
- Gleiche MD5 = Update statt Duplikat
- Mehrfaches Hochladen von `assets.jsonl` ist sicher

✅ **Empfohlen:**
- Nutze immer `source_ref` = MD5
- Prüfe vor Upload: `SELECT COUNT(*) FROM hd_assets WHERE source_ref = 'md5-xyz'`

### Topic-Unterscheidung

✅ **In metadata speichern:**
- `metadata.topic` = Topic aus Collection
- `metadata.profile_id` = Profile-ID (z.B. "hd_content")

✅ **In DB filtern:**
- Nutze `metadata->>'topic'` für Filterung
- Nutze `metadata->>'profile_id'` für Profile-Filterung

### Weiterverarbeitung steuern

✅ **Status-basiert:**
- `status = 'queued'` → Wird verarbeitet
- `status = 'processed'` → Bereits verarbeitet
- `status = 'failed'` → Fehlgeschlagen

✅ **Topic-basiert:**
- Filtere nach `metadata->>'topic'` vor Verarbeitung
- Setze `status = 'queued'` nur für gewünschte Topics

## 11. Nächste Schritte (jetzt möglich)

### Bereit für Ingestion?

✅ **Ja, wenn:**
- `assets.jsonl` existiert
- Downloads erfolgreich (oder geplant)
- HD-SaaS Upload-Funktion verfügbar

### Workflow starten:

**1. assets.jsonl hochladen:**
- Via HD-SaaS UI oder API
- Wird in `hd_assets` gespeichert (ohne Duplikate)

**2. Weiterverarbeitung starten:**
```sql
-- Setze Assets auf queued für Verarbeitung
UPDATE hd_assets 
SET status = 'queued'
WHERE status != 'queued'
  AND metadata->>'profile_id' = 'hd_content';
```

**3. Worker verarbeitet automatisch:**
- PDF → Text → Chunks → Classification → KG

**4. Ergebnisse prüfen:**
```sql
-- Zeige verarbeitete Assets
SELECT title, metadata->>'topic', status 
FROM hd_assets 
WHERE status = 'processed';

-- Zeige Classification-Verteilung
SELECT 
  metadata->>'topic' as topic,
  COUNT(*) as count
FROM hd_assets
GROUP BY metadata->>'topic';
```

## 12. Erweiterung für BaZi (später)

### Separate Profile-ID (optional)

**Falls gewünscht:**
- Erstelle `code/annas-archive-toolkit/projects/bazi_content/topics.txt`
- Erstelle `code/annas-archive-toolkit/projects/bazi_content/config.json` mit `profile_id: "bazi_content"`
- Separate `assets.jsonl` für BaZi

**Oder: Gemischt (aktuell):**
- Nutze `metadata.topic` zur Unterscheidung
- Ein `assets.jsonl` für alle Topics
- Filtere in DB nach `metadata->>'topic'`

## Zusammenfassung

### Duplikat-Prävention ✅
- **Automatisch:** Unique Constraint auf `(account_id, source_ref)`
- **Upsert:** Gleiche MD5 = Update statt Duplikat
- **Sicher:** Mehrfaches Hochladen erzeugt keine Duplikate

### Topic-Unterscheidung ✅
- **In metadata:** `metadata.topic` und `metadata.profile_id`
- **In DB:** Filtere mit `metadata->>'topic'` oder `metadata->>'profile_id'`
- **Flexibel:** Ein `assets.jsonl` kann mehrere Topics enthalten

### Weiterverarbeitung steuern ✅
- **Status-basiert:** `status = 'queued'` → wird verarbeitet
- **Topic-basiert:** Filtere nach `metadata->>'topic'` vor Verarbeitung
- **Manuell:** Setze `status = 'queued'` nur für gewünschte Topics

### Bereit für nächsten Schritt ✅
- ✅ `assets.jsonl` kann hochgeladen werden
- ✅ Duplikate werden automatisch verhindert
- ✅ Topics können in DB unterschieden werden
- ✅ Weiterverarbeitung kann gesteuert werden

## Links

- **Technische Anleitungen:** `../../code/annas-archive-toolkit/docs/`
- **Täglicher Workflow:** `daily_workflow.md`
- **High-Level Workflow:** `workflow.md`
- **HD-SaaS Weiterverarbeitung:** `hd_saas_processing.md` ⭐
