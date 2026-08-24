<!-- Reality Block
last_update: 2026-08-24
status: draft
scope:
  summary: "Stückweiser Update-Prozess für Makerkit-Upstream bei stark divergentem ASTRA-IMC-Fork."
  in_scope:
    - triage workflow
    - release cadence
    - risk controls
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

## Entscheidung „Neu aufsetzen vs. Stückweise“

Neu aufsetzen nur dann, wenn mindestens zwei Kriterien erfüllt sind:

- Build-/Security-Blocker lässt sich nicht mehr selektiv patchen.
- Divergenz erzeugt wiederholt kritische Integrationsfehler.
- Geplantes Refactor-Fenster mit Puffer ist bereits freigegeben.

Sonst gilt: **stückweise aktualisieren**.
