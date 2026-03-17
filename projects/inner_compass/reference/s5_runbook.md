# S5 Runbook — Vollständiger E2E-Test (MinerU + LLM)

> **Ziel:** 1 HD-PDF durch die neue Pipeline (MinerU → LLM) validieren.
> **Voraussetzung:** Spark mit MinerU + LLM (nicht gleichzeitig auf GPU), Supabase (lokal oder Cloud), Worker mit service_role.

## Topologie (VM105 + Spark + Tailscale)

| Komponente | Host | Erreichbarkeit |
|-------------|------|----------------|
| Supabase | VM105 (lokal) | `http://127.0.0.1:54321` von VM105, `http://<VM105_TAILSCALE_IP>:54321` von Spark |
| Worker | Spark | Läuft auf Spark, verbindet zu Supabase via Tailscale |
| MinerU | Spark | Lokal auf Spark (CLI) |
| LLM | Spark | SGLang/vLLM auf Spark |

**Supabase-URL für Worker auf Spark:** `http://<VM105_TAILSCALE_IP>:54321` (IP via `tailscale status` auf VM105).

## Zwei-Phasen-Betrieb (GPU-Sharing)

MinerU und LLM teilen sich die GPU auf Spark. Deshalb:

| Phase | LLM | MinerU | Worker-Filter |
|-------|-----|--------|----------------|
| 1 — Text-Extraktion | **AUS** | **AN** | `IC_WORKER_JOB_TYPES=extract_text` |
| 2 — Wissens-Extraktion | **AN** | AUS | Filter entfernen (alle Jobs) |

---

## Phase 0: Vorbereitung

### 1. Supabase bereit
- Lokal: `pnpm run supabase:web:start` (von code/hd_saas_app)
- Windows Health-Check-Problem: `pnpm exec supabase start --ignore-health-check` (in apps/web)
- Oder: Cloud-Supabase mit Migration + Seed

### 2. Strukturgraph seeden (falls noch nicht)
```bash
cd code/hd_saas_app/apps/web
python scripts/ic_seed_structure.py
```

### 3. HD-PDF bereit
- Ein HD-PDF (z.B. aus scratch/hd_content-assets.jsonl oder manuell)
- Dateiname z.B. `test_hd.pdf`

### 4. PDF hochladen + Source + Job anlegen

**Option A — Anna's Archive Pipeline (VM102, empfohlen):**

Code-Sync (einmalig): `hd_saas_uploader.py` mit `--sys-mode` muss auf VM102 sein.
```bash
# Von VM105/Windows:
scp code/annas-archive-toolkit/src/hd_saas_uploader.py user@<VM102_IP>:~/annas-archive-toolkit/src/
```

```bash
# Auf VM102 (PDFs liegen in output/hd_content/downloads/fast_download)
cd ~/annas-archive-toolkit
set -a; source ~/.config/annas-archive-toolkit/member.env; set +a   # falls nötig

# .env.hd_saas: Cloud auskommentieren, lokale Werte nutzen:
# #SUPABASE_URL=https://...supabase.co
# #SUPABASE_SERVICE_ROLE_KEY=eyJ...
# #HD_ACCOUNT_ID=f9e10513-...
# SUPABASE_URL=http://100.70.238.41:54321
# SUPABASE_SERVICE_ROLE_KEY=sb_secret_...  (aus supabase status)
# HD_ACCOUNT_ID=5deaa894-2094-4da3-b4fd-1fada0809d1c

export AAT_CONFIG=projects/hd_content/config.json
python3 src/hd_saas_uploader.py --upload-pdfs output/hd_content/downloads/fast_download --max-pdfs 1 --sys-mode
```
→ PDF landet in sys_uploads_raw, sys_sources, sys_ingestion_jobs (extract_text queued).

**Option B — Supabase Studio (lokal):**
1. Studio öffnen: http://127.0.0.1:54323
2. Storage → sys_uploads_raw → Upload
   - Pfad: `accounts/5deaa894-2094-4da3-b4fd-1fada0809d1c/test_hd.pdf`
   - (Account-ID aus seed: Makerkit)
3. SQL Editor:
```sql
-- Source anlegen
insert into public.sys_sources (
  account_id, title, source_type, status, bucket, storage_path, mime_type
) values (
  '5deaa894-2094-4da3-b4fd-1fada0809d1c',
  'S5 Test HD PDF',
  'pdf',
  'queued',
  'sys_uploads_raw',
  'accounts/5deaa894-2094-4da3-b4fd-1fada0809d1c/test_hd.pdf',
  'application/pdf'
) returning id;

-- Job anlegen (source_id aus obigem RETURNING ersetzen)
insert into public.sys_ingestion_jobs (
  account_id, source_id, job_type, status
) values (
  '5deaa894-2094-4da3-b4fd-1fada0809d1c',
  '<SOURCE_ID_HIER>',
  'extract_text',
  'queued'
);
```

**Option C — ic_s5_upload.py (wenn PDF lokal vorhanden):**
```bash
cd code/hd_saas_app/apps/web/scripts
python ic_s5_upload.py C:\pfad\zu\hd_buch.pdf --title "Die lustigen Zweibeiner"
```

---

## Phase 1: MinerU (LLM pausieren)

### Auf Spark
1. **SGLang stoppen** (GPU freigeben): `docker stop sglang-r1-8b-josiefied` (oder welcher Container läuft)
2. MinerU prüfen: `.venv/bin/mineru --help` (muss im venv sein)

### Worker starten (nur extract_text)
**Wichtig:** Worker mit venv-Python starten, damit MinerU gefunden wird (PATH enthält sonst oft nicht venv/bin).

```bash
cd ~/srv/hd-worker
export SUPABASE_URL="https://xxx.supabase.co"   # oder http://100.70.238.41:54321 für lokal
export SUPABASE_SERVICE_ROLE_KEY="..."
export IC_USE_MINERU=true
export IC_MINERU_LANG=latin
export IC_MINERU_TIMEOUT=3600
export IC_WORKER_JOB_TYPES=extract_text

.venv/bin/python3 ic_worker.py --loop --sleep 5
```

- Worker pollt, findet extract_text Job
- MinerU extrahiert PDF → Chunks in sys_source_chunks
- Worker enqueued classify_domain
- Wenn "No queued jobs" für extract_text: Phase 1 fertig, Worker stoppen

---

## Phase 2: LLM (MinerU kann weg)

### Auf Spark
1. LLM starten (SGLang/vLLM mit Qwen3-32B o.ä.)
2. Worker neu starten (ohne Job-Filter):

```bash
cd ~/srv/hd-worker
export SUPABASE_URL="..."
export SUPABASE_SERVICE_ROLE_KEY="..."
export IC_LLM_URL="http://localhost:8000/v1"   # oder Spark-LLM-URL
export IC_LLM_MODEL="Qwen/Qwen3-32B"            # je nach Setup
# IC_USE_MINERU kann true bleiben, wird für folgende Jobs nicht genutzt

.venv/bin/python3 ic_worker.py --loop --sleep 5
```

- Worker verarbeitet: classify_domain → extract_term_mapping → extract_interpretations → text2kg → synthesize_node
- Jeder Job braucht LLM (außer text2kg, der ist deterministisch)

---

## Phase 3: Validierung

### Prüfen
1. **sys_sources:** status = `processed` (oder `text_extracted` wenn nur Phase 1)
2. **sys_source_chunks:** Einträge vorhanden
3. **sys_kg_nodes:** Neue/angereicherte Nodes mit canonical_description
4. **sys_synthesis_wordings:** Styles für verarbeitete Nodes

### SQL-Checks
```sql
-- Chunks
select count(*) from sys_source_chunks where source_id = '<SOURCE_ID>';

-- Neue Interpretationen / angereicherte Nodes
select node_key, canonical_id, canonical_description
from sys_kg_nodes
where updated_at > now() - interval '1 hour'
limit 20;
```

---

## Troubleshooting

| Problem | Lösung |
|--------|--------|
| MinerU nicht gefunden | Worker mit `.venv/bin/python3` starten (nicht system `python3`); MinerU liegt in venv |
| MinerU OOM / sehr langsam | SGLang stoppen: `docker stop sglang-r1-8b-josiefied` (oder `docker ps` → laufenden Container) |
| MinerU Timeout | `IC_MINERU_LANG=latin` setzen (DE-PDFs); `IC_MINERU_TIMEOUT=7200` für große Docs |
| Storage 403 | service_role Key prüfen, RLS-Policy sys_uploads_raw_service_role |
| LLM Timeout | IC_LLM_URL prüfen, Modell läuft? |
| classify_domain skipped | Confidence < 0.3 → PDF evtl. nicht HD-relevant |
| Kein account_id | Seed-Account 5deaa894-2094-4da3-b4fd-1fada0809d1c nutzen |
