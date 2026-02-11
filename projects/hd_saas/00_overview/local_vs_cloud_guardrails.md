<!-- Reality Block
last_update: 2026-02-02
status: draft
scope:
  summary: "Verbindliche Guardrails: Was läuft lokal vs. Cloud, welche ENV wohin, wie vermeiden wir 'Worker sieht keine Jobs' und Key-Leaks."
  in_scope:
    - single-source-of-truth Regeln (Supabase Instanz, Tabellen, Jobs)
    - ENV-Matrix (Web vs Worker vs Uploader)
    - typische Failure Modes + schnelle Checks
  out_of_scope:
    - production hardening (WAF, secrets manager, multi-region)
notes: []
-->

# Local vs Cloud Guardrails (HD‑SaaS)

Diese Seite ist die **verbindliche** Orientierung, damit wir nicht wieder in den Zustand geraten:
„UI zeigt X, Worker sieht keine Jobs, Tabellen sind unterschiedlich, Keys sind im Terminal gelandet“.

## Grundregel (1 Satz)

**Control Plane ist genau eine Supabase‑Instanz pro Umgebung.**  
Alles, was Jobs erzeugt und alles, was Jobs verarbeitet, muss auf **dieselbe** Instanz zeigen.

## Quick Matrix: Was läuft wo?

| Komponente | Lokal (Dev) | Cloud (E2E/Prod‑ähnlich) | Muss auf welche Supabase zeigen? |
|---|---|---|---|
| Web UI (Makerkit) | ✅ ja | ✅ ja | die Instanz, in der du die Tabellen/JOBS sehen willst |
| Dev Runner (Import‑Job Button) | ✅ ja | optional | gleiche Instanz wie UI |
| Uploader (VM102/VM105 Scripts) | optional | ✅ ja (typisch) | **Cloud** (damit Worker Jobs sieht) |
| Worker (VM102/Spark/DGX) | optional | ✅ ja (typisch) | **Cloud** (Control Plane) |

## ENV‑Guardrails (Minimum)

### Web UI (Next.js)

- **Lokal‑Supabase**:
  - `NEXT_PUBLIC_SUPABASE_URL=http://127.0.0.1:54321`
  - `NEXT_PUBLIC_SUPABASE_ANON_KEY=...` (lokal)
- **Cloud‑Supabase**:
  - `NEXT_PUBLIC_SUPABASE_URL=https://<project-ref>.supabase.co`
  - `NEXT_PUBLIC_SUPABASE_ANON_KEY=...` (cloud)

Regel: Die UI kann nur das sehen, worauf sie zeigt. Wenn du Cloud‑Jobs debuggen willst, muss die UI **gegen Cloud** laufen.

### Worker (Python, Service Role)

- `SUPABASE_URL=https://<project-ref>.supabase.co`
- `SUPABASE_SERVICE_ROLE_KEY=...` (**niemals** in Client‑Code / niemals in Logs/Terminal tippen)

Regel: Worker nutzt **Service Role** und muss deshalb extra sauber mit Secrets umgehen (env‑file, systemd, keine Prints).

### Uploader (Scripts)

Regel: Der Uploader muss gegen **dieselbe Cloud** zeigen wie Worker, sonst erzeugt er Jobs „im falschen Universum“.

## Golden Path (Cloud E2E)

- **Schritt 1**: Migrationen/Schema in Cloud deployed (Supabase CLI `db push`).
- **Schritt 2**: Uploader schreibt `hd_documents`/`hd_document_files`/`hd_ingestion_jobs` in Cloud.
- **Schritt 3**: Worker pollt Cloud und schreibt Ergebnisse zurück (Chunks/Interpretations/etc.).

## Typische Failure Modes (und wie du sie in 30s findest)

### A) „Worker sieht keine Jobs“

- **Symptom**: UI zeigt Jobs lokal, Worker loggt „no queued jobs“.
- **Ursache**: UI/DevRunner schreibt lokal, Worker pollt Cloud (oder umgekehrt).
- **Check**:
  - In Worker‑Shell: `echo $SUPABASE_URL`
  - In UI‑Env: `NEXT_PUBLIC_SUPABASE_URL`
- **Fix**: Beide auf dieselbe Instanz stellen (typisch: Cloud).

### B) „In Cloud fehlen Tabellen“

- **Symptom**: Supabase Studio zeigt keine `hd_*` Tabellen oder RLS/Policies fehlen.
- **Ursache**: Migrationen wurden nicht gepusht.
- **Fix**: In `code/hd_saas_app/apps/web`: `supabase db push`.

### C) „Keys sind im Terminal/Logs gelandet“

- **Symptom**: Service Role Key wurde im Output/History sichtbar.
- **Fix**: **Keys rotieren**, künftig nur via env‑file laden, keine Debug‑Prints.

### D) „Jobs hängen ewig auf running“

- **Symptom**: `status=running`, `started_at` alt, keine `finished_at`.
- **Ursache**: Worker abgestürzt/neu gestartet ohne Cleanup; fehlendes Heartbeat‑Konzept.
- **Quick Fix**: Job auf `queued` zurückpatchen (siehe `infrastructure/spark/hd_worker_ops.md`).

## Minimal‑Checks (Copy/Paste)

### Worker: „bin ich auf Cloud?“

```bash
python3 - <<'PY'
import os
print("SUPABASE_URL =", os.environ.get("SUPABASE_URL"))
print("HAS_SERVICE_ROLE_KEY =", bool(os.environ.get("SUPABASE_SERVICE_ROLE_KEY")))
PY
```

### Worker: letzte Jobs lesen (Service Role)

Siehe `infrastructure/spark/hd_worker_ops.md` (Job Debug Abschnitt).

### Debug-Flags (Worker, nur zur Fehleranalyse)

- **Normalbetrieb:** `HD_DISABLE_OCR_FALLBACK` und `HD_MINERU_NO_FALLBACK` **nicht setzen** (oder explizit `false`). Fallbacks lassen die Pipeline robust laufen.
- **Kurzzeit-Debug:** `HD_DISABLE_OCR_FALLBACK=true` bzw. `HD_MINERU_NO_FALLBACK=true` setzen → dann schlägt der Job bei MinerU/OCR-Fallback fehl (Fehler sichtbar). Danach Flags wieder entfernen.
- **Worker-Signatur:** Bei Job-Updates schreibt der Worker `worker_host` und `worker_pid` ins `debug`-Objekt → erkennbar, welcher Host den Job verarbeitet hat (wichtig bei mehreren Workern).

