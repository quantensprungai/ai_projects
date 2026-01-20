# Makerkit HD‑SaaS App – Bootstrap & Orientierung (ohne Start)

Ziel dieser Notiz: **Wir halten fest, dass der Makerkit‑Stack sauber geklont/installed ist** und wo welche Teile liegen – damit wir die nächsten Schritte (HD‑Ingestion Slice, Supabase‑Schema/Buckets, Upload→Job→Extraction) sauber darauf aufbauen können, **ohne** das Projekt jetzt schon laufen zu lassen.

## Status (lokal auf VM105 / Windows)

- **Repo-Pfad**: `code/hd_saas_app`
- **Branch**: `main`
- **Remotes**:
  - `origin`: `quantensprungai/hd-saas-app`
  - `upstream`: `makerkit/next-supabase-saas-kit-turbo`
- **Dependencies**: `pnpm install` wurde ausgeführt (`pnpm-lock.yaml` + `node_modules/` vorhanden).
- **Docker Desktop**: installiert (für lokales Supabase später relevant).

## Wichtige Repo-Struktur (Monorepo)

- **`apps/web/`**: Haupt‑App (Next.js App Router) – das ist später “das Produkt”.
  - **Routes**: `apps/web/app/` (Marketing/Auth/Home/Admin/API).
  - **Config**: `apps/web/config/*.ts`
  - **Supabase (lokal + SQL)**: `apps/web/supabase/`
    - `migrations/` (SQL Migrationen)
    - `schemas/` (SQL Schema-Dateien)
    - `seed.sql`
    - `config.toml`
- **`apps/dev-tool/`**: internes Dev‑Tool (u.a. für Env‑Variablen/Checks).
- **`packages/*`**: wiederverwendbare Module (Auth, Accounts, Team‑Accounts, Billing, UI, Supabase‑Helpers, …).

## Env‑Strategie (wichtig für “keine Secrets im Git”)

In `apps/web/` sind mehrere `.env*` Dateien vorhanden:

- **`apps/web/.env`**: *nur* public/shared Konfiguration (Kommentare warnen explizit: keine Secrets).
- **`apps/web/.env.production`**: soll nur public/nicht‑sensitive Werte enthalten (Kommentare warnen ebenfalls).
- **`apps/web/.env.development`** / **`apps/web/.env.test`**: enthalten auch sensitive Variablen‑Namen (z.B. Service Role Key) – **niemals echte Secrets committen**.

Für lokale Arbeit ist der Makerkit‑Standard:

- **`apps/web/.env.local`**: lokal, gitignored (hier gehören echte Secrets für lokale Dev rein).

## Local vs Cloud Dev (Reality Check für unseren Stack)

Makerkit ist **local-first** (Supabase lokal). Für unseren HD‑Ingestion E2E‑Pfad mit Spark Worker brauchen wir aber oft **Cloud**:

- **Local Mode** (Makerkit default):
  - UI + lokale Supabase (`http://127.0.0.1:54321`)
  - gut für schnelle UI‑Iteration
  - Spark Worker sieht diese Jobs **nicht**

- **Cloud Mode** (E2E: UI → Job → Spark Worker):
  - UI schreibt gegen Supabase Cloud
  - Spark Worker pollt Supabase Cloud und verarbeitet Jobs

Wichtig (Makerkit-Key-Priorität):
- Browser‑Client nutzt `NEXT_PUBLIC_SUPABASE_URL` und **primär** `NEXT_PUBLIC_SUPABASE_PUBLIC_KEY` (wenn gesetzt), sonst `NEXT_PUBLIC_SUPABASE_ANON_KEY`.
- Daher im Cloud Mode am besten **beide** Keys auf den Cloud Anon Key setzen, um “Invalid API key” durch Override/Mix zu vermeiden.

Hinweis: die Makerkit‑Doku im Repo referenziert den üblichen Schritt `cp apps/web/.env.example apps/web/.env.local` – je nach Kit‑Version kann statt `.env.example` auch eine andere Vorlage genutzt werden; entscheidend ist: **echte Secrets nur in `.env.local` oder im Hosting‑Secret‑Store**.

## Was wir bewusst NICHT gemacht haben

- Keine `pnpm dev`, kein `pnpm supabase:web:start`, kein lokales Supabase gestartet.
- Keine Supabase‑Projekte/Keys eingetragen.
- Kein Deployment.

## Makerkit Updates (Upstream → Unser Repo)

Makerkit empfiehlt “daily updates”. Praktisch heißt das:

- `upstream` regelmäßig fetchen
- Merge/Rebase in `main` (oder einem `upstream-sync/*` Branch) durchführen
- Konflikte lösen
- dann in unser `origin` pushen

Wichtig: Eigene HD‑SaaS‑Features so kapseln, dass Updates konfliktarm bleiben (z.B. eigene Feature‑Packages, klar benannte Routen/DB‑Objekte).

## Wie das in unseren HD‑Docs einsortiert ist

- **Vision/Frame (entscheidungsrelevant, ohne MVP zu sprengen)**: `projects/hd_saas/00_overview/vision_and_scope_frame.md`
- **MVP Definition (aktueller Fokus)**: `projects/hd_saas/03_roadmap/mvp.md`
- **MVP Spec (Buckets/Tabellen/Statusmodell)**: `projects/hd_saas/03_roadmap/hd_ingestion_slice_spec.md`
- **Ideen-Parkplatz (vNext)**: `projects/hd_saas/01_spec/parking_lot_backlog.md`

## Relevanz für den HD‑Ingestion Slice (nächster Schritt)

Wenn wir weitergehen, sind die wichtigsten “Andockpunkte”:

- **DB Schema/Migrations**: `apps/web/supabase/migrations/*` (+ RLS Policies)
- **Storage Buckets**: Supabase Storage (Konzept/Doku + später Provisioning)
- **App‑UI**: neue Routes/Views in `apps/web/app/home/...` (tenant‑konform)
- **Server‑Actions/Route Handlers**: `apps/web/app/api/...` oder server-side Loader/Actions in `_lib/server/`

Als nächstes definieren wir minimal:

- Buckets: `hd_uploads_raw` (PDF), `hd_transcripts_raw` (Text)
- Tabellen: `assets`, `asset_files`, `ingestion_jobs` (MVP)
- “Minimaler” Upload → Job anlegen → Extraction (später Worker/Queue)

