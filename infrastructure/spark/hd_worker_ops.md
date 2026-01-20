<!-- Reality Block
last_update: 2026-01-20
status: draft
scope:
  summary: "Ops-Notizen für den HD Worker auf Spark: Debug/Retry, typische Fehler, Supabase Checks."
  in_scope:
    - job debugging
    - retry/requeue procedure
    - failure patterns
  out_of_scope:
    - worker code implementation (liegt auf Spark / separates Repo)
notes: []
-->

# HD Worker – Ops (Spark)

## Zweck

Kurze, praxisnahe Referenz: **Warum hängen Jobs? Wie debuggen wir das? Wie requeue’n wir sauber?**

## Grundannahmen (Architecture)

- **Supabase Cloud** = Control Plane (Auth, Storage, Tabellen, Jobs)
- **Spark Worker** = Data Plane (polling, processing, write-back)

Wichtig: Wenn die App lokal gegen `http://127.0.0.1:54321` schreibt, sieht Spark **keine** Jobs.

## Zugriff (robust)

- SSH Admin: `ssh -p 2222 sparkuser@<spark-ts-ip>`
- Worker Runtime Path (Spark): `~/srv/hd-worker/`

## Job Debug (schnell)

### 1) Letzte Jobs ansehen (Service Role)

Auf Spark (mit `.env` geladen):

```bash
cd ~/srv/hd-worker
set -a; source .env; set +a

python3 - <<'PY'
import os,requests
url=os.environ['SUPABASE_URL']
key=os.environ['SUPABASE_SERVICE_ROLE_KEY']
h={'apikey':key,'Authorization':f'Bearer {key}'}
params={'select':'id,account_id,job_type,status,attempts,error,debug,created_at,started_at,finished_at','order':'created_at.desc','limit':'10'}
r=requests.get(f"{url}/rest/v1/hd_ingestion_jobs", params=params, headers=h, timeout=30)
print(r.status_code)
print(r.text)
PY
```

### 2) Logs

```bash
tail -n 200 ~/srv/hd-worker/logs/worker.log
```

## Requeue / Retry (wenn Fix deployed ist)

```bash
cd ~/srv/hd-worker
set -a; source .env; set +a

python3 - <<'PY'
import os,requests
url=os.environ['SUPABASE_URL']
key=os.environ['SUPABASE_SERVICE_ROLE_KEY']
job_id="__JOB_ID__"
headers={'apikey':key,'Authorization':f'Bearer {key}','Content-Type':'application/json'}

patch={'status':'queued','error':None}
r=requests.patch(f"{url}/rest/v1/hd_ingestion_jobs?id=eq.{job_id}", headers=headers, json=patch, timeout=30)
print("patch", r.status_code)
PY
```

## Typische Fehlerbilder

### A) Jobs bleiben “queued/pending”, Worker zeigt keine Aktivität

- Ursache: App schreibt gegen **lokales Supabase**, Worker pollt **Cloud Supabase**.
- Fix: App‑Env auf Cloud stellen (URL + anon/public key) und Dev Server neu starten.

### B) `Circular reference detected` (import_assets_jsonl)

- Ursache: Worker schreibt zu große / nicht JSON‑serialisierbare Strukturen nach `metadata` (z. B. komplettes Objekt als `source_line`).
- Fix: `source_line` nur als **kleines Subset** speichern (flach, ohne Self‑Refs / ohne ganze Payloads).

