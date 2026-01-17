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
- **Portal (Makerkit / Next.js)**: Login/Rollen, Upload‑Flows, “ReST‑Bereiche”.
- **Backend (Supabase Cloud, separat je Projekt)**:
  - Postgres (Daten)
  - Auth (Nutzer)
  - Storage (Dokumente/Uploads)
  - RLS (Zugriffsschutz)
- **Analytics (optional, separater Dienst)**:
  - Superset **separat** (eigene URL) für Self‑Service Exploration.

## Optionale Bausteine (nur bei Bedarf)
- **RAG/Agent‑Service**: separater Worker/Service (z. B. lokal/Spark), schreibt Ergebnisse als Text/Metadaten zurück.
- **ETL/Jobs**: schlanker Job‑Runner (Cron/Worker) statt “großem” Orchestrator.

## Deployment (low ops)
- App: Coolify/Hetzner
- Supabase: managed (wenig Ops) – pro Projekt getrennt, um Risiken/Trennung zu vereinfachen.


