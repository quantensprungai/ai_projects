<!-- Reality Block
last_update: 2026-08-24
status: draft
scope:
  summary: "Stückweiser Update-Prozess für Makerkit-Upstream bei stark divergentem ASTRA-IMC-Fork."
  in_scope:
    - triage workflow
    - release cadence
    - risk controls
    - V4/Cache-PPR upgrade window and rollback
  out_of_scope:
    - full rebase playbook
notes:
  - "Ausgelegt auf Stage A: Stabilität vor Feature-Hype."
-->

# Makerkit Update Process (Stage A)

## Prinzip

Kein „alles neu aufsetzen und zurückkopieren“ auf `main`.  
Stattdessen: **kontinuierliche Triage + gezielte Backports**.

## Cadence

- **Täglich (10–15 Min):** upstream fetchen, relevante Releases/PRs markieren.
- **Wöchentlich (30–60 Min):** shortlist „jetzt übernehmen / beobachten / ignorieren“.
- **Monatlich (0.5–1 Tag):** ein gebündeltes Update-Fenster mit Tests.

## Priorisierung

1. **Security / Rechtehärtung**  
2. **Runtime-Stabilität** (Next/React/Theme/Auth-Regressionen)  
3. **Supabase/Auth-Kompatibilität**  
4. **Developer Experience** (Lint/Build/Tooling)  
5. **UI-/Marketing-Verbesserungen** nur falls konfliktarm

## Arbeitsmodus

1. Upstream-Änderung identifizieren (Release oder PR).
2. Lokalen Impact prüfen:
   - Routen/Layouts
   - Auth/Session
   - i18n/Locale
   - Supabase-Migrationen/Policies
3. In Feature-Branch übernehmen (cherry-pick oder selektiver Patch).
4. Smoke-Test:
   - `/` (de default, locale switch)
   - `/home/[account]/assets`
   - Sign-in/Sign-out
   - zentrale DB-Views
5. Bei sauberem Ergebnis mergen, sonst zurückstellen.

## Guardrails

- **Kein** Full-Rebase im laufenden Stage-A-Sprint.
- **Keine** Upgrades mit API-Break ohne Zeitfenster + Rollback-Plan.
- **Keine** Vermischung mit fachlichem Scope-Change im gleichen PR.
- Immer changeloggen: was kam von Upstream, was blieb bewusst draußen.

## Upgrade-Fenster bis „aktuellster Makerkit-Stand“ (`#512` + Deps)

Ziel irgendwann: Next/Cache-Components/PPR (`#512`) plus Dependency-Bumps. Das ist **kein** Nebenbei-Backport.

### Brauchen wir einen neuen Branch?

**Ja — immer einen eigenen Git-Branch** (z. B. `chore/makerkit-v4-cache`), nie direkt auf `main` experimentieren.

| Ebene | Rollback | Verliert IMC-Tabellen? |
|---|---|---|
| **Git-Branch** | `main` bleibt unberührt; Branch verwerfen = App-Code zurück | Nein |
| **Lokale Supabase-DB** | Volume/Backup / `db dump` vor Migrationen | Nur bei `db reset` oder destruktiven Migrationen |
| **Cloud/Staging-DB** | Supabase Branch-DB oder Snapshot/Backup vor Apply | Nur wenn Migrationen DROP/REWRITE machen |

Kurz: **App-Upgrade allein löscht keine Tabellen.** Risiko entsteht erst durch **SQL-Migrationen** (Makerkit-Kit-Schema oder versehentliches `reset`).

### Was kann Daten gefährden?

1. `supabase db reset` / Volume löschen → lokal alles weg (IMC inkl.).
2. Upstream-Migration mit `DROP TABLE` / aggressivem Rewrite auf Kit-Tabellen (`accounts`, …) — IMC-`imc_*` meist unberührt, aber Auth/Memberships kritisch.
3. Blindes `migration up` auf Prod ohne Review der SQL-Diffs.

IMC-Rohdaten (`imc_wind_farms`, ERA5, …) liegen in **eigenen Migrationen**; Makerkit-UI/Next-Upgrades touchieren die nicht.

### Pflicht-Checkliste vor dem Fenster

1. **Git:** Branch von aktuellem `main`; Tag/Notiz `pre-makerkit-v4`.
2. **DB-Backup lokal:** `supabase db dump` (Schema+Data) oder Docker-Volume-Kopie.
3. **Cloud:** Snapshot oder Supabase Preview-Branch — Migrationen zuerst dort.
4. **Migration-Diff:** alle neuen Upstream-`.sql` lesen; alles mit `DROP`/`TRUNCATE`/`ALTER … TYPE` einzeln freigeben.
5. **ASTRA-Regressionen absichern:** Assets-Home-Redirect, Proxy-Matcher **ohne** `assets`-Exclude, Locale `de`, Workspace-Switcher, E2E `--workers=1`.
6. **Rollback-Probe:** wissen, wie Code (`git checkout main`) und DB (Dump restore / Branch löschen) getrennt zurückgesetzt werden.

### Empfohlene Reihenfolge im Fenster

1. Dependency-Bump in isoliertem Branch (Next 16.3 etc.), Build+Typecheck.
2. Dann `#512` Cache/PPR schichtweise (Layouts/Provider zuerst, Marketing zuletzt).
3. ASTRA-Patches erneut anwenden (Assets, Proxy, i18n).
4. E2E Smoke; erst dann Merge nach `main`.

## Entscheidung „Neu aufsetzen vs. Stückweise“

Neu aufsetzen nur dann, wenn mindestens zwei Kriterien erfüllt sind:

- Build-/Security-Blocker lässt sich nicht mehr selektiv patchen.
- Divergenz erzeugt wiederholt kritische Integrationsfehler.
- Geplantes Refactor-Fenster mit Puffer ist bereits freigegeben.

Sonst gilt: **stückweise aktualisieren**.
