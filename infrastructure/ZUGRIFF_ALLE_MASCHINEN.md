# Zugriff auf alle Maschinen – Quick Reference

**IPs prüfen:** `tailscale status` (auf VM105 oder in Git Bash)

---

## Terminal 1: VM105 (dein Windows-Rechner)

**Wo:** Cursor Terminal oder Git Bash – du bist bereits da.

```bash
cd ~/ai_projects
# oder
cd c:/Users/Admin105/ai_projects
```

**Typische Befehle:**
- `tailscale status` – IPs aller Maschinen
- `scp` – Dateien zu anderen Maschinen kopieren

---

## Terminal 2: VM102 (docker-apps) – Clawdbot, Anna's Archive, Docker

**SSH von VM105:**
```bash
ssh user@docker-apps
```
Falls nicht auflöst:
```bash
ssh user@100.83.17.106
```
*(IP aus `tailscale status` – docker-apps)*

**Wichtige Pfade auf VM102:**
| Pfad | Zweck |
|------|-------|
| `~/clawd/workspace-{heiko,noah,flora,familie}` | Clawdbot Agent-Workspaces |
| `~/.clawdbot-personal/clawdbot.json` | Clawdbot Config |
| `~/annas-archive-toolkit` | Anna's Archive Toolkit |
| `~/annas-archive-toolkit/output/hd_content/downloads/fast_download` | PDF-Downloads |

**Typische Befehle:**
```bash
# Clawdbot
systemctl --user status clawdbot-gateway-personal.service
systemctl --user restart clawdbot-gateway-personal.service

# Anna's Archive (nach Session-Start)
cd ~/annas-archive-toolkit
set -a; source ~/.config/annas-archive-toolkit/member.env; set +a
bash scripts/upload_hd_pdfs.sh
```

---

## Terminal 3: Spark (spark-56d0) – GPU, SGLang, LLM

**SSH von VM105:**
```bash
ssh -p 2222 sparkuser@spark-56d0
```
Falls nicht auflöst:
```bash
ssh -p 2222 sparkuser@100.96.115.1
```
*(IP aus `tailscale status` – spark-56d0)*

**Wichtige Pfade auf Spark:**
| Pfad | Zweck |
|------|-------|
| `~/ai/models/llama` | Modelle |
| `~/ai/scripts/serve/` | SGLang-Serve-Skripte |
| `~/srv/hd-worker/` | HD-Worker (MinerU, OCR) |

**Typische Befehle:**
```bash
# SGLang/LLM prüfen
curl -sf http://localhost:30001/v1/models

# Worker
systemctl --user status hd-worker
```

---

## SCP: Dateien von VM105 zu anderen Maschinen

**Wichtig:** SCP muss **auf VM105** (dein PC) laufen – nicht in einer SSH-Session auf VM102!
Öffne ein **neues Terminal** (ohne SSH), dann:

```bash
cd ~/ai_projects
scp infrastructure/docker/update_clawdbot_flora_config.py user@docker-apps:/tmp/
scp -r infrastructure/docker/workspace-flora user@docker-apps:/tmp/
```

**Zu Spark:**
```bash
scp -P 2222 infrastructure/spark/scripts/serve/sglang_switch_to_qwen.sh sparkuser@100.96.115.1:~/ai/scripts/serve/
```

---

## Übersicht: Maschinen & Rollen

| Maschine | Rolle | SSH |
|----------|-------|-----|
| **win11pro105** (VM105) | Dein Dev-PC, ai_projects | – (du bist hier) |
| **docker-apps** (VM102) | Clawdbot, Anna's Archive, Docker | `ssh user@docker-apps` |
| **spark-56d0** | GPU, SGLang, LLM, HD-Worker | `ssh -p 2222 sparkuser@spark-56d0` |
| **pve** | Proxmox Host | `ssh root@pve` |
| **management** | VM101 (Portainer, etc.) | `ssh user@management` |

---

## Clawdbot: Cron-Setup (flora) – kompletter Ablauf

```bash
# Terminal auf VM105 (ai_projects)
cd ~/ai_projects
scp infrastructure/docker/setup_flora_cron.py infrastructure/docker/update_clawdbot_flora_config.py user@docker-apps:/tmp/

# Terminal: SSH zu VM102
ssh user@docker-apps

# Auf VM102
python3 /tmp/update_clawdbot_flora_config.py
python3 /tmp/setup_flora_cron.py
systemctl --user restart clawdbot-gateway-personal.service
```

**Flora testen (deine Nummer umbiegen):**
```bash
scp infrastructure/docker/swap_flora_test_mode.py user@docker-apps:/tmp/
# Auf VM102:
python3 /tmp/swap_flora_test_mode.py          # Testmodus: deine Nummer → Flora
# Nach dem Test:
python3 /tmp/swap_flora_test_mode.py --restore # Zurück → Heiko
systemctl --user restart clawdbot-gateway-personal.service
```

**clawdbot-Pfad auf VM102:** Das Setup-Skript sucht automatisch in:
- `clawdbot` / `openclaw` / `moltbot` (PATH)
- `~/.clawdbot/bin/clawdbot` (offizieller Installer)

Prüfen: `ls -la ~/.clawdbot/bin/clawdbot` oder `which clawdbot`
