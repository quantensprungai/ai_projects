<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "MVP-Definition für HD-SaaS."
  in_scope:
    - MVP scope
    - cut lines
  out_of_scope:
    - full roadmap
notes: []
-->

# MVP – HD‑SaaS

## MVP‑Ziel (v0): **HD‑Ingestion Slice (intern / Curator‑Workflow)**

Der MVP startet bewusst **nicht** bei “perfektem KG/Chat”, sondern bei einem **kleinsten ausführbaren End‑to‑End Pfad**, der die technische Grundlage für alle späteren Layer schafft.

Wichtig: Das ist primär ein **interner Curator/Admin‑Workflow** (Vorarbeit/Korpus‑Aufbau). End‑User laden in v0 nicht “ihre PDFs” hoch – sie konsumieren später das daraus abgeleitete System (Readings/Chat).

- **Input**: PDF und/oder Transkript (Text) je Tenant/Account (Tenant = Makerkit `public.accounts`)
- **Ablauf**: Upload → DB‑Record → Job → Text‑Extraction → gespeicherter Text (mit Referenzen)
- **Output**: Eine **durchsuch-/anzeigbare Textbasis** pro Dokument als Grundlage für spätere Chunking/Extraction/KG/Dynamics

Warum: Das ist der “Plumbing”-Teil, den alle weiteren Layer brauchen (KG, Dynamics, RAG, Synthesis).

## In Scope (MVP)

- **Storage Buckets** für:
  - `hd_uploads_raw` (PDFs)
  - `hd_transcripts_raw` (Transkripte als `.txt/.md/.json`)
- **DB Tabellen (minimal)** – tenant‑fähig über `account_id` (Makerkit `public.accounts`):
  - `hd_documents`
  - `hd_document_files`
  - `hd_ingestion_jobs`
  - optional: `hd_document_texts` (oder Text direkt an `hd_documents`, falls klein)
- **RLS**: Zugriff ausschließlich über Membership/Account (kein Cross‑Tenant Leaking)
- **UI (Makerkit)**:
  - Upload‑Form (pro Account; **intern** für Curator/Admin)
  - Dokumentliste + Status (pending/running/succeeded/failed)
  - “Extracted Text” Ansicht (read‑only)
- **Job Runner (MVP)**:
  - Minimaler Worker (Script/Service) der Jobs abarbeitet (zunächst “manuell/CLI”-fähig)

## Out of Scope (MVP Cut Lines)

- Vollständige KG Extraktion (Nodes/Edges)
- Embeddings/RAG
- Whisper/OCR als Produktfeature (nur als “Job‑Type” vorgesehen)
- Automatisches Importieren/Downloaden externer Libraries (Anna Toolkit bleibt Upstream; `assets.jsonl` ist ein separater Track)
- Billing/Payments (Makerkit‑Feature, aber nicht MVP‑kritisch)
- **User‑Uploads für persönliche Dokumente** (z.B. Lebenslauf, Journaling/Notizen, “Life Docs”) – **Future Option**, separater Track (Privacy/Consent/Retention/UX)

## Klarstellung: Zwei “Ingestion”-Ebenen (damit es später nicht vermischt wird)

- **Korpus‑Ingestion (intern)**: Quellen/Schulen (Bücher, Transkripte, PDFs) → unser Strukturmodell (JSONB) → später KG/Dynamics/Synthesis.  
  Das ist das, was wir hier als MVP‑Slice vorbereiten.
- **User‑Kontext (produktseitig)**: Geburtsdaten + Präferenzen + ggf. Notizen/Feedback.  
  Das ist ein separater Track und kann später dazukommen, muss aber nicht mit PDF‑Uploads starten.

## Erfolgskriterien (MVP)

- **Operabel**: Ein Dokument kann pro Account ingestiert werden, inkl. Job‑Status, Logs/Error‑Trace.
- **Traceability**: Jeder extrahierte Text ist eindeutig einem `document_id` + `file_id` zuordenbar.
- **Security**: RLS verhindert Zugriff auf fremde Accounts.



