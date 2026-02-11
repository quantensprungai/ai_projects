# HD Worker auf Spark – Was du jetzt selbst machen musst

<!-- last_update: 2026-02-05 -->

**Hinweis:** Der Worker auf Spark liegt unter **`~/srv/hd-worker`** (nicht `~/hd-worker`). Die systemd-Unit heißt `hd-worker.service` und muss einmalig installiert werden.

---

## 1) Von Windows aus: Dateien auf Spark kopieren

**Repo-Root:** `c:\Users\Admin105\ai_projects` (oder dein ai_projects-Pfad).

**PowerShell:**

```powershell
cd c:\Users\Admin105\ai_projects\code\hd_saas_app\apps\web\scripts
scp -P 2222 -o StrictHostKeyChecking=accept-new hd_worker_mvp.py requirements-hd-worker-mvp.txt requirements-hd-worker-spark.txt sparkuser@100.96.115.1:~/srv/hd-worker/
scp -P 2222 -o StrictHostKeyChecking=accept-new c:\Users\Admin105\ai_projects\infrastructure\spark\hd-worker-spark.service sparkuser@100.96.115.1:~/srv/hd-worker/hd-worker.service
```

**Spark-Host ersetzen**, falls anders: z. B. `sparkuser@<spark-ts-ip>` oder `sparkuser@spark-56d0` (MagicDNS).

---

## 2) Per SSH auf Spark einloggen

```bash
ssh -p 2222 sparkuser@100.96.115.1
```

(Oder: `ssh -p 2222 sparkuser@spark-56d0`)

---

## 3) Auf Spark: Verzeichnis prüfen und ggf. venv

**Wichtig:** Arbeitsverzeichnis ist **`~/srv/hd-worker`**.

```bash
cd ~/srv/hd-worker
ls -la
```

**Erwartung:** `hd_worker_mvp.py`, `requirements-hd-worker-mvp.txt`, `requirements-hd-worker-spark.txt`, `hd-worker.service`, `.env`, `.venv/` (falls schon eingerichtet).

**Falls noch kein venv:**

```bash
cd ~/srv/hd-worker
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements-hd-worker-spark.txt
```

**Falls venv schon da** (z. B. von früherem Setup): nur bei Code-Update nichts Nötiges; bei neuen Dependencies ggf. `.venv/bin/pip install -r requirements-hd-worker-spark.txt` erneut.

---

## 4) Auf Spark: .env prüfen

```bash
cd ~/srv/hd-worker
cat .env
```

**Mindestens vorhanden:**

- `SUPABASE_URL=https://...`
- `SUPABASE_SERVICE_ROLE_KEY=...`
- `HD_USE_MINERU=true`
- optional: `HD_MINERU_BACKEND=hybrid`, `HD_MINERU_DEVICE=cuda`, `HD_MINERU_LANG=latin` oder Auto: `HD_MINERU_AUTO_LANG=true`
- optional LLM (SGLang): siehe Block unten zum Eintragen in `~/srv/hd-worker/.env`.

Falls `.env` fehlt oder unvollständig: anlegen/ergänzen (z. B. `nano .env`). Siehe `infrastructure/spark/hd_worker_ops.md` (Abschnitt Secrets/ENV).

**SGLang für LLM-Extraktion eintragen (auf Spark in `~/srv/hd-worker/.env`):**

```bash
# LLM-Extraktion (SGLang auf Spark; Primary = 30001, Secondary = 30000)
HD_LLM_EXTRACTION_URL=http://127.0.0.1:30001/v1/chat/completions
HD_LLM_EXTRACTION_LANG=en
```

Falls SGLang auf Port **30000** läuft: `30000` statt `30001` in der URL. **Health prüfen:** Spark Model Switcher starten (`infrastructure/spark/tools/spark_model_switcher/` → `streamlit run app.py`) – dort werden Port 30001/30000 per SSH geprüft; wenn kein Dienst läuft, zuerst ein Modell starten (z. B. Qwen3 32B / DeepSeek R1).

---

## 5) Auf Spark: systemd-Service installieren und starten (einmalig)

**Die Unit-Datei muss zuerst auf Spark liegen** (siehe Schritt 1 als `hd-worker.service` in `~/srv/hd-worker/`).

```bash
cd ~/srv/hd-worker
ls -la hd-worker.service
```

Falls **hd-worker.service fehlt**: Schritt 1 (SCP der Service-Datei) ausführen.

Dann (sudo verlangt dein Passwort):

```bash
sudo cp ~/srv/hd-worker/hd-worker.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now hd-worker.service
sudo systemctl status hd-worker.service --no-pager
```

**Erwartung:** `active (running)`. Fehler: `journalctl -u hd-worker.service -n 100 --no-pager`.

---

## 6) Nach Code-Änderungen: nur Worker-Datei kopieren + Neustart

Wenn du nur den Python-Code erneuert hast (z. B. Auto-Lang, BaZi-Seeds):

**Von Windows:**

```powershell
cd c:\Users\Admin105\ai_projects\code\hd_saas_app\apps\web\scripts
scp -P 2222 hd_worker_mvp.py sparkuser@100.96.115.1:~/srv/hd-worker/
```

**Auf Spark:**

```bash
sudo systemctl restart hd-worker.service
sudo systemctl status hd-worker.service --no-pager
```

---

## 7) Kurzreferenz – Spark vs. VM102

| | Spark | VM102 / docker-apps |
|--|--------|----------------------|
| **Pfad** | `~/srv/hd-worker` | `~/hd-worker` |
| **Service-Datei** | `infrastructure/spark/hd-worker-spark.service` → als `hd-worker.service` kopieren | `apps/web/scripts/hd-worker.service` |
| **Requirements** | `requirements-hd-worker-spark.txt` (MVP + MinerU) | `requirements-hd-worker-mvp.txt` |
| **systemd** | `WorkingDirectory=/home/sparkuser/srv/hd-worker` | `WorkingDirectory=/home/user/hd-worker` |

Weitere Ops (Logs, Requeue, Fehlerbilder): **`infrastructure/spark/hd_worker_ops.md`**.
