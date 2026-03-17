> **ARCHIVIERT** (2026-02-16). Inhalt wurde in Cursor Rules (.cursor/rules/) oder doc_and_rules_strategy.md überführt.

# Git Commit-Blocks – pro Projekt separat

<!--
last_update: 2026-02-10
scope: PowerShell-Befehle zum Committen und Pushen pro Projekt
-->

Führe die Blöcke nacheinander aus. Nach jedem Block: `git push` (falls gewünscht) oder am Ende einmal pushen.

---

## 1) HD-SaaS

```powershell
git add projects/hd_saas/
git add projects/_meta/chat_handover_template.md
git commit -m "hd_saas: Option B Plan, erkenntnisse_fuer_spaeter, interpretations Beispiele, Chat-Handover"
```

---

## 2) AI 2027

```powershell
git add projects/ai_2027/
git commit -m "ai_2027: Umstrukturierung – neue Overview-Docs, paper, strategy, opinions; alte Context/Spec archiviert"
```

---

## 3) ReST Data Platform

```powershell
git add projects/rest_data_platform/
git commit -m "rest_data_platform: MVP/Scope-Updates, wp2_1_offshore_ce_summary, technical_next_steps, 05_presentations"
```

---

## 4) Anna's Archive Toolkit

```powershell
git add projects/annas_archive_toolkit/
git commit -m "annas_archive_toolkit: status, topics_and_profiles, daily_workflow Updates"
```

---

## 5) LinkedIn Serie

```powershell
git add projects/linkedin_serie/
git commit -m "linkedin_serie: Umstrukturierung nach Jahren (2025/, 2026/); alte artikel/post entfernt"
```

---

## 6) Infrastructure Spark

```powershell
git add infrastructure/spark/
git commit -m "spark: hd_worker_ops, HD_WORKER_HANDOVER, Selbst-Checkliste, systemd-Service, MinerU-Patch"
```

---

## 7) Meta / Root (optional)

```powershell
git add projects/_meta/master_map.md
git add projects/_meta/git_commit_blocks_separat.md
git add README.md
git add .gitattributes
git commit -m "meta: master_map, README, git_commit_blocks, .gitattributes"
```

---

## Hinweis zu Code-Repos

- `code/hd_saas_app/` und `code/annas-archive-toolkit/` sind **eigene Git-Repos** (nicht im Root enthalten).
- Diese separat in ihrem jeweiligen Verzeichnis committen und pushen:
  - `cd code/hd_saas_app; git status; git add .; git commit -m "..."; git push`
  - `cd code/annas-archive-toolkit; ...`

---

## Push (einmal am Ende)

```powershell
git push
```
