<!-- Reality Block
last_update: 2026-01-16
status: draft
scope:
  summary: "Aktueller Stand (Snapshot) + nächste Schritte für Anna's Archive Toolkit (HD + Survival)."
  in_scope:
    - current status
    - next steps
    - run locations
  out_of_scope:
    - instructions for illegal acquisition of copyrighted works
    - secrets/credentials
notes: []
-->

# Status Snapshot – Anna’s Archive Toolkit

## Wo wir stehen (heute)

- **Profile vorhanden**:
  - **`hd_content`**: keyword/topic driven Collection (`code/annas-archive-toolkit/projects/hd_content/`)
  - **`survival`**: category-driven Collection (`code/annas-archive-toolkit/projects/survival/config.json`)
- **Metadaten‑Output**:
  - `hd_content` schreibt nach **`output/hd_content/`**:
    - `metadata.json` / `metadata.csv`
    - `assets.jsonl` (Ingest‑Contract, metadata‑only)
    - `acquire_queue.json` (Tracking/Selektion, metadata‑only)
  - `survival` schreibt analog in sein eigenes Output (im Repo ist `output/` ignoriert).
- **Detailseiten‑Stage (optional, resumable)**:
  - Collector kann zusätzlich `/md5/...` Detailseiten laden und strukturierte Zusatzinfos als `aa_detail` speichern.
  - Checkpoint: `output/<profile>/aa_detail_checkpoint.json` (mehrfach startbar; bereits bearbeitete MD5s werden übersprungen).
  - Default ist sicher: keine externen URLs werden gespeichert, außer explizit in Config erlaubt.
- **qBittorrent für HD ist live (VM102)**:
  - Kategorien & SavePaths sind sauber getrennt:
    - `HD_UNSORTED` → `/downloads_hd/_UNSORTED`
    - `HD_SORTED` → `/downloads_hd/_SORTED`
    - `HD_DUPLICATES` → `/downloads_hd/_DUPLICATES`
  - Credentials laufen über `/etc/annas-archive-toolkit/qbt.env` (env vars), nicht im Repo.
  - `--setup-categories` funktioniert und authentifiziert auf VM102.

## Pipeline‑Logik (wichtig: “Metadaten vs Download vs Ingestion”)

1. **Collect (Metadaten)**: Wir sammeln Metadaten (Titel/Autor/MD5/URL/Topic/Category) als **Katalog & Selektionsbasis**.
2. **Select (Priorisieren)**: Wir wählen gezielt Kandidaten aus (Heuristiken/Regeln/Manuell).
3. **Acquire (optional)**: Inhalte beschaffen (z. B. eigene Uploads/own library/licensed/free content).
4. **Ingest (Downstream Pipeline)**: Erst danach startet die eigentliche Verarbeitung (je nach Projekt, z. B. HD‑SaaS oder Survival‑Pipeline):
   - OCR/Whisper → Cleaning → Chunking → Extraction → **Text2KG** → Knowledge Graph + Dynamics.

> **Hinweis**: `assets.jsonl` ist ein **Ingest‑Contract**, der zunächst **metadata‑only** ist. Der “Acquire/Download”-Schritt ist davon getrennt.
>
> **Wichtig**: Automatisches Extrahieren von Magnet-/Torrent-Links aus beliebigen Webseiten ist nicht Teil des Toolkits. Für automatisierte Downloads werden Download-Hints (z. B. Magnet/.torrent) aus **zulässigen Quellen** separat an die Queue angehängt.

## Wo läuft was?

- **VM105**: Doku/Profiles pflegen, Code committen/pushen.
- **VM102**: Runtime (Runs ausführen). Standard: **pull‑only**.

## Nächste Schritte (empfohlen)

- **HD (`hd_content`)**:
  - Detailseiten‑Stage bei Bedarf aktivieren (`aa_detail_pages.enabled=true`) und laufen lassen, bis `aa_detail_checkpoint.json` “durch” ist.
  - `assets.jsonl` / `acquire_queue.json` als Ingest/Tracking‑Artefakte stabilisieren (Felder, Status, Resume).
  - Wenn Downloads gewünscht: legale Download-Hints an `acquire_queue.json` anhängen (`src/attach_download_links.py`) und dann enqueuen (`--add-from-acquire-queue`, mit Safety-Gates).
  - Danach: `assets.jsonl` als Ingest‑Contract in HD‑SaaS übernehmen (Supabase Tabellen + Pipeline).
- **Survival (`survival`)**:
  - Optional: gleiche Contract‑Kette nutzen (`metadata.*` → `assets.jsonl` → `acquire_queue.json`).
  - Danach: separate Acquire/Weiterverarbeitung (eigenes Projekt, nur gemeinsame Toolkit‑Infrastruktur).


