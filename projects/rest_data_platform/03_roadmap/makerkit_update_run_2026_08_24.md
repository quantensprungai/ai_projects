<!-- Reality Block
last_update: 2026-08-24
status: draft
scope:
  summary: "Konkreter Update-Run gegen Makerkit-Upstream (Triage + erste Backports)."
  in_scope:
    - upstream divergence snapshot
    - now/later decision
    - first applied backport
  out_of_scope:
    - full upstream merge
notes: []
-->

# Makerkit Update Run — 2026-08-24

## Snapshot

- Branch: `main`
- Remotes: `origin` (astra-imc-platform), `upstream` (makerkit)
- Divergenz `main...upstream/main`: **12 / 1103** (lokal / upstream; Stand nach Push `a0592b93`)

## Heute direkt übernommen

### Security Hardening (Backport)

- Quelle upstream: `d58f6b27` (`#517`)
- Lokal übernommen als Migration:
  - `apps/web/supabase/migrations/20260824100000_revoke_residual_privileges.sql`
- Zweck:
  - residuale Rechte auf `public`-Tabellen/Sequenzen reduzieren
  - `TRUNCATE/REFERENCES/TRIGGER` für API-Rollen sauber entziehen
  - Sequenz-`UPDATE` restriktiver behandeln

### Welle A (teilweise übernommen)

- Quelle upstream: `f85ce120` (`#519`)
  - `packages/email-templates/src/lib/i18n.ts`
  - `apps/web/app/[locale]/home/(user)/_components/home-page-header.tsx`
  - `apps/web/app/[locale]/home/[account]/_components/team-account-layout-page-header.tsx`
  - `packages/features/team-accounts/src/components/members/account-members-table.tsx`
  - `package.json` (`test:unit`)
  - `turbo.json` (`tasks.test:unit`)
  - `apps/e2e/tests/team-accounts/team-accounts.po.ts`
  - `apps/e2e/tests/team-accounts/team-accounts.spec.ts`
  - `apps/e2e/tests/utils/mailbox.ts`
- Zweck:
  - E-Mail-Lokalisierung fällt auf `NEXT_PUBLIC_DEFAULT_LOCALE`, dann `en`, zurück
  - Seitentitel im `PageHeader` werden wieder korrekt angezeigt
  - lokalisierte Datumsanzeige in der Mitgliederliste
  - Unit-Test-Task einheitlich im Root verfügbar
  - stabilere Team-Account-E2E-Selektoren (`:visible`) bei Client-Navigation
  - flexibler OTP-Mail-Subject-Match (lokalisierte Betreffzeilen)
  - robustere OTP-Code-Erkennung aus HTML

- Quelle upstream: `48233d9d` (`#520`)
  - `packages/mcp-server/src/lib/process-utils.ts`
  - `packages/mcp-server/src/tools/emails/kit-emails.service.ts`
  - `packages/mcp-server/src/tools/emails/__tests__/kit-emails.service.test.ts`
  - `packages/mcp-server/src/tools/run-checks/__tests__/run-checks.service.test.ts`
- Zweck:
  - robustere Windows-Command-Resolution
  - saubereres Handling von `.cmd`/`.bat` vs. nativen Binaries
  - stabilere PowerShell-basierte Prozesssuche
  - plattformstabile Pfadnormalisierung in MCP-Email-Service und Tests
  - Run-Checks-Testfixtures decken reale Default-Skripte (`lint:fix`, `format:fix`) ab

- Quelle upstream: `9cffa706` (`#516`) — selektiv, ohne Upstream-Signatur-Flow
  - `apps/web/app/[locale]/join/accept/route.ts`
  - `apps/web/app/[locale]/join/page.tsx`
  - `packages/features/team-accounts/src/schema/invite-members.schema.ts`
  - `packages/features/team-accounts/src/server/services/account-invitations.service.ts`
  - `packages/features/team-accounts/src/components/invitations/accept-invitation-container.tsx`
  - `apps/web/i18n/messages/en/teams.json`
  - `apps/web/i18n/messages/de/teams.json`
- Zweck:
  - Invitation-E-Mails werden case-insensitive normalisiert (`trim` + `toLowerCase`)
  - Join-Fehler kommen als stabile Codes statt Klartext in der URL
  - Accept-Fehler werden im UI sichtbar angezeigt

## E2E-Stabilisierung (ASTRA-Anpassung)

- Team-Landing akzeptiert `/home/<slug>` und `/home/<slug>/assets`
- Workspace-Switcher: Hover/`ArrowRight`, Reload-Recovery, Escape-Close
- Create-Team: kein zweites unnötiges `createTeam()` in Validierungs-Specs
- Invite-Accept: Identities-Zwischenstopp abgefangen
- Validierung: `pnpm --filter web-e2e test -- tests/team-accounts/team-accounts.spec.ts --workers=1` → **11 passed**
- Hinweis: unter hoher Parallelität (`workers>=4`) bleibt der nested Dropdown noch empfindlich

## Welle B — Schema/Docs/Agent-Tooling (in Arbeit, uncommitted)

### Security-Schema-Sync (`#517` / `d58f6b27` Rest)

- `apps/web/supabase/schemas/00-privileges.sql` — Default-Privilege-Stripping
- Schema `02`–`11`: `anon` in `REVOKE ALL … FROM`
- `12-one-time-tokens.sql`: `REVOKE ALL ON public.nonces FROM anon, authenticated, service_role`
- `07-invitations.sql`: `GRANT USAGE ON SEQUENCE invitations_id_seq TO authenticated, service_role`
- `apps/web/supabase/AGENTS.md` — Privilege-Guidance (lokal: Migration `20260824100000`)
- `apps/web/supabase/tests/database/privileges.test.sql`
  - Katalog-Assertions + behavioral `TRUNCATE`-Denial
  - Anpassung: `SET ROLE authenticated` statt `makerkit.authenticate_as` (lokales Setup ohne dbdev-`tests`-Schema)
- Verifikation: `supabase db test` → **privileges.test.sql ok**
- Live-DB: `USAGE` auf `invitations_id_seq` an Schema angeglichen (`anon` revoked)

### `#519` / `#520` Rest

- `.github/workflows/unit-tests.yml`
- `packages/mcp-server/src/lib/__tests__/process-utils.test.ts` (zusätzliche Windows-Arg-Tests)
- Hinweis: MCP-Package hat vorbestehende Unit-/Typfehler; process-utils: 22/23 ok (1 Port-Listener-Flake unter Windows)

### Agent-Tooling (`dbfc8b82`)

- `.agents/` Skills + MCP-Config
- Docs: `docs/installation/ai-agents.mdoc`, `mcp.mdoc`
- `.claude/agents/code-quality-reviewer.md`

### Verifikation dieser Welle

- `pnpm --filter web typecheck` → ok
- `privileges.test.sql` → ok
- Commit/Push: **noch offen** (explizit anfordern)

## Welle C — Low-Risk Bugfixes (2026-08-24)

- Quelle:
  - `be16b27b` (`#488`) — Invitation-Daten via `next-intl` `useFormatter`
  - `1a60b782` — `not-found.tsx`: `lang={locale}`, Messages auf `common` begrenzt
  - `384ec381` (`#496`, selektiv) — `AuthHashStatusListener` + Callback-Pfad `personalAccountSettings`
- Bewusst **nicht** übernommen:
  - `be61b164` Proxy-Matcher mit `assets`-Exclude (würde `/home/[account]/assets` brechen)
  - `91abe428` (`#512`) Cache/PPR (siehe unten)
  - Expo-Ports (`#515`/`#518`), Passkeys, volle Dependency-Bumps (`#513`/`#514`)
- Verifikation: `pnpm --filter web typecheck` → ok

### Warum `#512` (Cache/PPR) weiter überspringen?

`91abe428` ist kein Fix, sondern ein **Framework-Cut** (Upstream als V4.0.0):

1. **Breite:** ~120 Dateien — Layouts, Marketing, Auth, Admin, Docs, E2E, Provider, Skeletons
2. **Runtime-Schalter:** `cacheComponents: true` + Dev-Turbopack-FS-Cache; verändert Caching/Rendering/Navigation grundlegend
3. **Versionssprung:** Upstream Next **16.3.0** vs. unser Catalog **16.2.1** — nicht isoliert cherry-pickbar
4. **Konflikt mit ASTRA:** Team-Home → Assets-Redirect, Workspace-Switcher, Locale-Default `de`, Proxy-Matcher ohne `assets`-Exclude — alles müsste parallel neu abgesichert werden
5. **Stage-A-Risiko:** hoher Regressionsschaden bei geringem unmittelbarem Produktnutzen; braucht eigenes Upgrade-Fenster mit Rollback

## Kandidaten Nächste Welle

### Niedriges Risiko (weiter selektiv)

1. Mobile-Sidebar-Refactor `#510` (`d8872c5b`) — nur nach Layout-Smoke (berührt Team-/User-Layouts)
2. Stripe/Billing-Fixes aus `#496` Rest — nur wenn Billing-Pfad aktiv getestet wird
3. MCP-Package-Hygiene separat (Types/`@types/node`/ESM), bevor weitere MCP-Backports

### Bewusst später

1. `91abe428` (`#512`) — V4 Cache/PPR/Instant Navigation (eigenes Fenster)
2. Größere Versionssprünge/Bundle-Änderungen in älteren Releases
3. Expo / Passkeys / Turnstile-managed — nur bei klarem Produktbedarf

## Nächste Schritte (konkret)

1. ~~Security-Migration lokal gegen Supabase laufen lassen.~~ **erledigt**
2. Smoke-Test remote/prod analog planen, wenn Staging existiert.
3. ~~Rest Welle A / Security-Schema + Agent-Tooling backporten.~~ **committed + pushed (`c657a30f`)**
4. ~~Welle C Low-Risk Bugfixes.~~ **lokal fertig → Commit/Push**
5. Team-Accounts-E2E bei CI/lokal mit `--workers=1` (oder serial) fahren, bis Dropdown robuster ist.
6. ~~Pending ältere IMC-Migrationen reparieren~~ **erledigt**
7. Nach Welle C: Produkt (ERA5 DE-Batch / AAS) **oder** `#510` Layout-Smoke.

## IMC-Migration History Repair (2026-08-24)

### Was los war

- `20260814140000_imc_era5_weather_windows.sql` und `20260817140000_imc_v_farm_era5_days.sql` waren **inhaltlich schon in der lokalen DB** (Tabellen/Views/Policies/Daten), aber **nicht** in `supabase_migrations.schema_migrations`.
- Dadurch scheiterte `supabase migration up` an `CREATE POLICY ... already exists` (Policies waren nicht idempotent).
- Wahrscheinliche Ursache: Objekte wurden früher manuell / per Script / per abgebrochenem Apply eingespielt, ohne History-Eintrag.

### Audit (vor Repair)

| Objekt | Status |
|---|---|
| `imc_era5_grid_points` | vorhanden, RLS + Select-Policy, 3 Rows |
| `imc_era5_weather_windows` | vorhanden, RLS + Select-Policy, 1858 Rows |
| `imc_v_farm_era5_context` | vorhanden |
| `imc_v_farm_era5_days` | vorhanden, 1858 Rows |
| History `20260814140000` / `20260817140000` | fehlte |

Zusätzlicher Befund: Views hatten breite Default-Privilegien (`anon`/`authenticated` inkl. INSERT/UPDATE/DELETE). Die Migrations-SQL hat nur `GRANT SELECT` gemacht, ohne vorher zu `REVOKE`.

### Was wir gemacht haben

1. Migrationsdateien härten:
   - `DROP POLICY IF EXISTS` vor `CREATE POLICY`
   - Views: `REVOKE ALL` dann `GRANT SELECT` für `authenticated`/`service_role`
2. Lokale View-Grants nachgezogen (gleicher Stand wie die gehärtete SQL)
3. History repariert: `supabase migration repair --local --status applied 20260814140000 20260817140000`

### Verifikation

- `supabase migration list --local`: alle Versionen inkl. `20260814140000`, `20260817140000`, `20260824100000` aligned
- `supabase migration up --local`: keine Pending-Migrationen mehr
- Daten unverändert (3 Grid Points / 1858 Windows / 1858 Days)
- View-Grants nur noch `SELECT` für `authenticated` + `service_role`

## Security-Migration lokal (2026-08-24)

- Status: **angewendet** auf lokaler DB (`supabase_migrations.schema_migrations`: `20260824100000`)
- Methode: SQL direkt via Docker-Postgres (`migration up` war durch ältere, teils bereits vorhandene IMC-Migrationen blockiert)
- Verifikation:
  - `TRUNCATE`/`REFERENCES` für `anon`/`authenticated` auf `accounts` und `imc_wind_farms` = false
  - `nonces`: keine Privilegien mehr für API-Rollen
  - normale Rechte bleiben: `SELECT/INSERT/UPDATE/DELETE` auf `accounts`; `authenticated` kann `imc_wind_farms` lesen (3606 Rows vorhanden)

## Smoke nach Migration

- App erreichbar: `http://localhost:3000` → 200
- E2E-Fokus (`workers=1`): **7 passed** (Healthcheck, Auth Sign-in, Invite-Pfad, Team-Update, Unauthorized-Team-Access)
- Browser: Session aktiv auf `/home`; Zugriff auf fremdes Team-Assets wird abgewiesen (erwartet)