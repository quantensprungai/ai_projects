<!-- Reality Block
last_update: 2026-03-28
status: draft
scope:
  summary: "Bootstrap: lizenzierte Next.js/Supabase-Turbo-Anwendungsbasis klonen, lokal verifizieren, IMC-Schema integrieren; Lokal/Cloud/Hosting."
  in_scope:
    - ordered bootstrap steps
    - stack integration (schemas, RLS, typegen)
    - dev vs supabase cloud vs app-hosting (high level)
  out_of_scope:
    - production deploy checklist (siehe going-to-production/supabase.md)
notes:
  - "Technische Tiefe: infrastructure/next-supabase-turbo/ (Spiegel der Vorlagen-Doku, ohne Produktnamen in der Projektdoku zu wiederholen)."
-->

# IMC-App: Start bei Null (Bootstrap)

## Kurzantwort: Nächster sinnvoller Schritt

1. **Code-Repo:** [`git@github.com:quantensprungai/astra-imc-platform.git`](https://github.com/quantensprungai/astra-imc-platform) — Stand 2026-03-26: **`main`** enthält einen **Import von** [`makerkit/next-supabase-saas-kit-turbo`](https://github.com/makerkit/next-supabase-saas-kit-turbo) (`main`, shallow). Remote **`upstream`** zeigt auf dasselbe öffentliche Repo (Updates: `git fetch upstream`). Lokal: `ai-projects/code/astra-imc-platform/`. Namenskonventionen: [`00_overview/naming_canon.md`](../00_overview/naming_canon.md).  
2. **Lokal verifizieren:** `pnpm supabase:web:start` (o. ä. laut Repo-README), dann **`pnpm supabase:web:reset`** einmal — bis Login und Datenbank-Baseline ohne Fehler laufen.  
3. **Erst danach** IMC-Domain-Schema einbinden (siehe unten) — nicht parallel zum ersten Start kämpfen.

So bleibt die **Anwendungsbasis = Referenz**, **IMC = kontrollierte Erweiterung**.

## Abgleich mit der Vorlagen-Struktur

Relevante interne Referenz (Spiegel unter `infrastructure/next-supabase-turbo/`):

- `development/database-schema.md` — Schema in **`apps/web/supabase/schemas/`** mit **Nummernpräfix**, Workflow **`supabase:db:diff`** oder neue Migration + Inhalt.
- `development/database-architecture.md` — Multi-Tenant über **`accounts` / `account_id`**; neue Features mit Ownership und RLS planen.
- Im geklonten Repo: **`apps/web/supabase/AGENTS.md`** — **RLS auf allen neuen Tabellen**, Grants/Policies nach dem dort beschriebenen Muster; Typegen nach Migration.

**Referenz-SQL** [`reference/imc/IMC_Schema_v1.sql`](../reference/imc/IMC_Schema_v1.sql); Policy-Muster: [`01_spec/imc_rls_policy_patterns.md`](../01_spec/imc_rls_policy_patterns.md).

| Thema | Stand (Referenz-SQL) | Im App-Repo noch zu tun |
|--------|----------------------|-------------------------|
| **RLS** | aktiv inkl. `has_role_on_account` / Farm-Join | Als **Migration** einspielen, mit Baseline-Migrationen testen |
| **Grants** | `revoke`/`grant` wie im SQL-Block | Ggf. an Vorlagen-Overrides angleichen |
| **UUID** | **`gen_random_uuid()`** (ohne uuid-ossp) | Unverändert oder an Vorlagen-Konvention |
| **Extensions** | `postgis`, `btree_gist` am Anfang | In erste nummerierte Schema-Datei / Migration |
| **Multi-Tenant** | **`imc_wind_farms.account_id`** | Beim Anlegen von Farms gültige `accounts`-ID setzen |

Ohne RLS auf neuen Tabellen sind **Supabase und die Anwendungsbasis** fachlich nicht abgesichert; hosted Supabase erwartet durchgängige Policies.

## Konkrete Integrationsvariante (empfohlen)

**A) Stand heute + weiterer Ausbau**

1. **IMC v1-Migration** liegt im Code-Repo: `apps/web/supabase/migrations/20260327120000_imc_astra_v1.sql` in [`quantensprungai/astra-imc-platform`](https://github.com/quantensprungai/astra-imc-platform) (Inhalt aus [`reference/imc/IMC_Schema_v1.sql`](../reference/imc/IMC_Schema_v1.sql) ab „1. ENUM-TYPEN“; Header + Extensions via [`../scripts/build_imc_migration.mjs`](../scripts/build_imc_migration.mjs). Tabellen/ENUMs/Views: Präfix **`imc_`**, Organisationen **`imc_orgs`**).
2. Nach Pull: **`pnpm supabase:web:reset`** + **`pnpm supabase:web:typegen`** — dann IMC-Tabellen in Studio sichtbar.
3. **Weitere Schema-Änderungen:** Kit-Workflow wie in `database-schema.md` (`schemas/*` + `supabase:db:diff`) **oder** Referenz anpassen und neue nummerierte Migration ergänzen; RLS-Muster: [`01_spec/imc_rls_policy_patterns.md`](../01_spec/imc_rls_policy_patterns.md).

**B) Nur historisch:** Monolith-Migration unter `migrations/` ohne `schemas/*`-Diff — v1 ist jetzt genau so umgesetzt.

## Wo entwickeln? Lokal · Supabase Cloud · App auf Hetzner/Coolify

1. **Lokal (Docker Supabase)** — `pnpm supabase:web:start`, Reset, typegen; Schema und RLS bis „grün“.
2. **Supabase Cloud (optional)** — Dev-Projekt **EU-Region**; verbinden, wenn lokaler Stand stabil oder Remote-Auth nötig.
3. **Next.js produktiv** — z. B. **Coolify auf Hetzner (Frankfurt)** für die App; DB oft **managed Supabase (EU)**.

## Supabase MCP (Cursor)

Verbindet typisch ein **Cloud-Projekt** (Dashboard-Token), **nicht** `127.0.0.1`. **Lokal:** Studio + CLI (`pnpm supabase:web:*`). **Cloud:** MCP für Inspektion/Migrationen gegen das verlinkte Projekt. Kanonische DDL bleibt [`reference/imc/IMC_Schema_v1.sql`](../reference/imc/IMC_Schema_v1.sql); ausgeführt wird die **Migration** im App-Repo.

## Remote-Supabase (später)

`going-to-production/supabase.md`: Auth-URLs, `db push`, Webhooks — **nach** lokalem grünem Stand.

## Referenzen im Workspace

- DB-Schema-Workflow: `infrastructure/next-supabase-turbo/development/database-schema.md`
- Tenancy: `infrastructure/next-supabase-turbo/development/database-architecture.md`
- Produktion: `infrastructure/next-supabase-turbo/going-to-production/supabase.md`
- IMC-DDL + RLS: `reference/imc/IMC_Schema_v1.sql`
- RLS-Muster: `01_spec/imc_rls_policy_patterns.md`
- Word vs. Repo: `imc_data_implementation_leitfaden.md`
- Namen / WP / Repo: `00_overview/naming_canon.md`

## Ein Satz für das Team

> Zuerst **nur Baseline** der Anwendungsbasis lokal grün, dann **eine** nummerierte Schema-Datei für IMC inkl. **Extensions + RLS**, dann **Diff/Migration + typegen**.
