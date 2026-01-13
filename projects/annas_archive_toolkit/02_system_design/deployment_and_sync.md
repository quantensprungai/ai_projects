<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "Systemdesign: wo läuft was, und wie wird Code von VM105 nach VM102 synchronisiert."
  in_scope:
    - deployment model
    - sync options
    - operational guardrails
  out_of_scope:
    - credentials
    - CI implementation details
notes: []
-->

# Deployment & Sync (VM105 → VM102)

## Rollen

- **Laptop (lokal)**: aktueller Entwicklungsstand (bei dir derzeit die “neueste” Quelle)
- **VM105**: zentraler Sammel-Workspace (Cursor), soll alle Projekte lokal enthalten
- **VM102**: Runtime (Docker Host), führt Workloads aus (deployed copy)

## Sync‑Optionen

### Option A (empfohlen): Git Pull auf VM102

- Repo wird einmal auf VM102 geklont
- Updates: `git pull`
- Vorteil: reproduzierbar, sauber versioniert

## Empfohlenes Zielbild (Laptop → VM105 → VM102)

Du willst, dass VM105 “alles gesammelt” hat. Das ist kompatibel mit Git, ohne dass du manuell kopierst:

- **Laptop pusht** in ein zentrales Remote (GitHub/GitLab *oder* ein Bare‑Repo in deinem Homelab)
- **VM105 clont/pullt** dieses Remote → hier ist dein zentraler Workspace (alles lokal)
- **VM102 zieht Deployments** via `git pull` (oder bekommt Releases)

Wichtig: “VM105 hat alles lokal” heißt nicht zwingend, dass VM105 selbst der Git‑Server sein muss – nur dass VM105 die zentrale Working Copy ist.

#### Variante A1: Remote = GitHub/GitLab (einfach, wenn ok)

- VM105 pusht nach `origin`
- VM102 pullt von `origin`

#### Variante A2: Remote = “Bare Repo” auf VM102 (kein Cloud)

Das ist oft die sauberste Lösung im Homelab:

**Auf VM102 (einmalig):**

```bash
mkdir -p ~/repos
git init --bare ~/repos/annas-archive-toolkit.git
```

**Auf VM105 (Repo-Ordner, einmalig):**

```bash
cd <dein-projekt-ordner>
git init
git add .
git commit -m "initial import"
git branch -M main
git remote add origin ssh://<user>@docker-apps/~/repos/annas-archive-toolkit.git
git push -u origin main
```

> `<user>` ist dein Linux-User auf VM102. `docker-apps` ist der Tailscale/MagicDNS Name aus deinem Setup.

**Auf VM102 (Deployment-Working-Copy):**

```bash
git clone ~/repos/annas-archive-toolkit.git ~/libgen-survival-project
```

**Update-Zyklus:**
- VM105: `git push`
- VM102: `cd ~/libgen-survival-project && git pull`

### Option B: rsync/scp Deployment

- nur für schnelle “hotfix” Übertragung
- Vorteil: schnell
- Nachteil: kann drift erzeugen

## Guardrails

- VM102 führt aus, aber **Entscheidungen/Design** bleiben im Repo dokumentiert.
- Secrets nie ins Repo.

## Bereits nach VM102 deployed – wie gehen wir damit um?

Wenn `~/libgen-survival-project` auf VM102 schon existiert, gibt es zwei saubere Wege:

1) **Repo “drüberziehen” (empfohlen, wenn VM102 nur Kopie ist)**  
   - Backup/rename des Ordners
   - frischer `git clone` an die gleiche Stelle

2) **Bestehenden Ordner in Git überführen (wenn VM102 die aktuellste Version enthält)**  
   - auf VM102 `git init`, commit, remote setzen, push nach `origin`
   - danach ist VM105 die Source-of-Truth (pull/merge)

Sag mir kurz, welche Seite den “neueren” Stand hat (VM105 oder VM102), dann legen wir den sauberen Weg fest.

## Sonderfall: Laptop ist aktuellster Stand (dein Ist-Zustand)

Dann ist der nächste, saubere Schritt:

1. **Auf dem Laptop** sicherstellen: Projekt ist ein Git-Repo und hat ein Remote (z. B. GitHub oder Bare‑Repo im Homelab).
2. **Auf VM105**: `git clone` in `code/annas-archive-toolkit/` (damit alles lokal “gesammelt” ist).
3. **Auf VM102**: entweder weiter aus demselben Remote deployen oder (wenn schon deployed) den Ordner an das Remote “andocken”.



