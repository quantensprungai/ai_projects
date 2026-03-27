<!-- Reality Block
last_update: 2026-03-28
status: draft
scope:
  summary: "Wiederkehrende RLS-/Grant-Muster für IMC-Tabellen (Next.js/Supabase, Team-Accounts; Template + Entscheidungslogik)."
  in_scope:
    - policy patterns
    - tenancy rules (account_id, farm_id)
    - Stammdaten vs. tenant-scoped writes
  out_of_scope:
    - vollständiges SQL (siehe reference/imc/IMC_Schema_v1.sql)
notes:
  - "Nach Umsetzung im Code-Repo: Migrationen sind Source of Truth; diese Datei bleibt Leitfaden."
-->

# IMC: RLS- und Policy-Muster (Supabase / Team-Accounts)

## Ziele

- **Multi-Tenant:** Zugriff nur auf Daten des **Accounts**, zu dem der Nutzer gehört — in der Anwendungsbasis typisch `public.has_role_on_account(account_uuid)`.
- **Farm als Untereinheit:** Tabellen mit `farm_id` (oder PK = `farm_id`) prüfen über **`EXISTS`-Join auf `imc_wind_farms`** dieselbe Account-Mitgliedschaft.
- **Stammdaten:** Global geteilte Kataloge (`imc_ports`, `imc_vessels`, `imc_turbine_models`, …) typischerweise **`SELECT` für `authenticated`**, **Schreiben** über **`service_role`** (Supabase-Client mit Service-Key) oder später Admin-Rolle — nicht jedem eingeloggten Nutzer.
- **Audit:** `imc_audit_log` ohne Policy für `authenticated` → **kein** direkter Zugriff; Schreiben/Lesen mit `service_role` oder Backend.

## Rollen (Kurz)

| Rolle | Typisch |
|--------|---------|
| `anon` | Keine Grants auf IMC-Tabellen (nur öffentliche Endpoints, die ihr explizit baut). |
| `authenticated` | JWT-Nutzer; alle IMC-Policies zielen hierauf. |
| `service_role` | Umgeht RLS; nur Server/ETL, niemals im Browser. |

## Muster A — Tenant-Wurzel (`imc_wind_farms`)

**Spalte:** `account_id NOT NULL` → `public.accounts(id)`.

```sql
ALTER TABLE public.imc_wind_farms ENABLE ROW LEVEL SECURITY;
CREATE POLICY imc_wind_farms_all ON public.imc_wind_farms
  FOR ALL TO authenticated
  USING (public.has_role_on_account(account_id))
  WITH CHECK (public.has_role_on_account(account_id));
```

## Muster B — Alles hängt an einer Farm (`farm_id` / PK `farm_id`)

**Bedingung:** `EXISTS (SELECT 1 FROM imc_wind_farms wf WHERE wf.farm_id = <tabelle>.farm_id AND has_role_on_account(wf.account_id))`.

In der Policy steht auf der Zeile der geschützten Tabelle schlicht `farm_id` (ohne Tabellenpräfix).

**Tabellen:** `imc_farm_design`, `imc_farm_grid`, `imc_farm_capex_*`, `imc_farm_revenue`, `imc_farm_opex_*`, `imc_farm_milestones`, `imc_farm_events`, `imc_farm_ports`, `imc_farm_stakeholders`, `imc_offshore_platforms`, …

## Muster C — Optional `farm_id` (Katalog + Zuordnung)

Wenn `farm_id IS NULL` **öffentlicher Katalog** innerhalb der App sein soll:

- **`SELECT`:** `farm_id IS NULL OR EXISTS(…imc_wind_farms…)`.
- **`INSERT`/`UPDATE`/`DELETE`:** nur Zeilen mit **`farm_id IS NOT NULL`** und Account-Match — Katalogzeilen nur per `service_role` pflegen.

**Tabellen:** `imc_transmission_assets`, `imc_vessel_assignments` (siehe kanonisches SQL).

Wenn ihr **keinen** gemeinsamen Katalog wollt: Muster B ohne `IS NULL`-Zweig; dann sind NULL-Zeilen nur für `service_role` sichtbar.

## Muster D — Globale Stammdaten (nur Lesen für Nutzer)

```sql
ALTER TABLE public.imc_ports ENABLE ROW LEVEL SECURITY;
CREATE POLICY imc_ports_select ON public.imc_ports
  FOR SELECT TO authenticated USING (true);
-- Kein INSERT/UPDATE/DELETE für authenticated → Schreiben nur service_role
```

## Views

Views mit `security_invoker = true` (PostgreSQL 15+), damit die **RLS der Basistabellen** gilt statt der View-Definiererrechte.

## Grants (Kurzcheck)

1. **`REVOKE ALL … FROM anon, authenticated`** auf neue Tabellen (nach Kit-Konvention).
2. **`GRANT`** nur das, was Policies erlauben sollen (z. B. `SELECT` auf Stammdaten, `SELECT, INSERT, UPDATE, DELETE` auf Farm-Tabellen).
3. Views: **`GRANT SELECT`** an `authenticated`, wenn die View für die App gedacht ist.

## Policy-Namen

Präfix z. B. `imc_`, pro Tabelle eindeutig (`imc_wind_farms_all`, `imc_farm_design_all`, …). Bei Migrationen: bei Änderungen **`DROP POLICY`** vor `CREATE POLICY`.

## Referenz

- Kanonische DDL inkl. RLS: [`../reference/imc/IMC_Schema_v1.sql`](../reference/imc/IMC_Schema_v1.sql)
- Bootstrap-Reihenfolge: [`../03_roadmap/imc_app_bootstrap.md`](../03_roadmap/imc_app_bootstrap.md)
