<!-- Reality Block
last_update: 2026-01-17
status: draft
scope:
  summary: "High-Level Architektur – ReST Data Platform (Makerkit + Supabase) schlank, erweiterbar."
  in_scope:
    - components
    - deployment options
  out_of_scope:
    - detailed schemas
notes: []
-->

# Architektur (High Level)

## Ziel
Mit **minimalem Aufwand** eine robuste Basis schaffen, die **Reporting/Monitoring** und **Datenorganisation** trägt, und später optional um KI/Agenten erweitert werden kann.

## Bausteine (minimal)
- **Portal (Next.js)**: Login/Rollen, Upload‑Flows, “ReST‑Bereiche”.
- **Backend (Supabase Cloud, separat je Projekt)**:
  - Postgres (Daten)
  - Auth (Nutzer)
  - Storage (Dokumente/Uploads)
  - RLS (Zugriffsschutz)
- **Kernmodule (WP 2.1)**:
  - Offshore‑Asset‑Register (Standorte, Lebenszyklen, Grunddaten)
  - Dokumenten‑Erschliessung (RAG light)
  - Low‑Complexity Zeitachsen/Mengenschaetzungen
  - DPP‑Light Demonstrator (ein Beispielobjekt)
- **Analytics (optional, separater Dienst)**:
  - Superset **separat** (eigene URL) für Self‑Service Exploration.

## Optionale Bausteine (nur bei Bedarf)
- **RAG/Agent‑Service**: separater Worker/Service (z. B. lokal/Spark), schreibt Ergebnisse als Text/Metadaten zurück.
- **ETL/Jobs**: schlanker Job‑Runner (Cron/Worker) statt “grossem” Orchestrator.
- **MCP‑Interface**: standardisierte Tool‑Aufrufe (Upload, Query, Report).

## Detaillierte Stack-Skizze (WP 2.1, textlich)
### Kern (jetzt, 1 FTE realistisch)
1) **Portal-Schicht (Next.js Web-App)**
   - Login/Rollen, Upload-Wizard, Asset-Register UI, Dokumentenbereich
2) **App-Layer (API/Business-Logik)**
   - API Routes/Server Actions, Validierung, Mapping-Logik, Zugriffskontrolle
3) **Supabase-Layer (Managed Backend)**
   - Postgres, Storage, Auth, RLS, Migrationen/Versionierung
4) **Analytics (Superset, separat)**
   - Read-only Zugriff auf Postgres, 1-2 Standardreports

### Optional (spaeter, wenn Nutzen klar)
5) **AI Processing (Spark Worker)**
   - RAG/Embeddings, Extraktion aus PDFs, Batch-Anreicherung
6) **Agentic Layer (AG2, intern)**
   - CE-Agent (BOM light), Datenqualitaet, Auto-Drafts
7) **MCP-Interface**
   - Standardisierte Tool-Aufrufe fuer externe KI-Tools
8) **DPP-Light**
   - Beispielkomponente, QR, Lifecycle-Events, Verknuepfung mit Asset-Register

## Deployment (low ops)
- App: Coolify/Hetzner
- Supabase: managed (wenig Ops) – pro Projekt getrennt, um Risiken/Trennung zu vereinfachen.


