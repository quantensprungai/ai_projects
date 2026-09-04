<!-- Reality Block
last_update: 2026-09-04
status: active
scope:
  summary: "Cloud IMC: Coolify-App plus curated data on Supabase, how to re-seed without MCP."
  in_scope:
    - cloud schema
    - curated IMC data on team astra-imc
    - demo login
    - Coolify app
    - re-seed path (CLI, not MCP)
  out_of_scope:
    - imc_source_raw_rows (Excel staging, local only)
    - MCP execute_sql bulk seed
    - Docker psql to db.*.supabase.co (IPv6-only)
notes:
  - "Demo password is for Stage-A only — rotate before any external share."
  - "Invite mail needs EMAIL_SENDER; without it, copy the accept link from Offene Einladungen."
-->

# Cloud Bootstrap — ASTRA IMC

| | |
|---|---|
| App | https://imc.ostfriesland.ai (Coolify / Hetzner) |
| Supabase | `pfprwudrfkugvzpjyrvj` (eu-west-1) |
| API | https://pfprwudrfkugvzpjyrvj.supabase.co |
| Team | Slug **`astra-imc`**, Name ASTRA IMC (`d0000001-0001-4001-8001-000000000010`) |
| Branch | `feat/assets-ia-restructure` |

## Was in Cloud liegt (2026-09-04)

Curated Working-Board-Daten, **derselbe Stand wie lokal**, gemappt auf Team `astra-imc`. **Nicht** die Excel-Staging-Tabelle `imc_source_raw_rows` (~151k Zellen).

| Inhalt | Stand |
|---|---|
| Schema (Makerkit + IMC + MaStR + Natura + ERA5 + Vessels …) | ja (`db push`) |
| Windparks | **3606** |
| Farm Design / Grid | **3606** / ~1423 |
| Häfen / Farm-Häfen | **118** / **677** |
| Schutzgebiete BfN marin | **205** |
| Turbinen (MaStR-Einheiten) / 4C-Typen | **1651** / **369** |
| ERA5 Stunden (Alpha Ventus CDS) | **23 232** |
| Vessels / VPI-Contracts | ~2218 / ~1185 |
| Demo-User + Team `astra-imc` | ja |

## Demo-Login (Stage-A)

- E-Mail: `demo@astra-imc.local`
- Passwort: `AstraDemo2026!`
- Team-Slug: **`astra-imc`** (nicht mehr `makerkit`)

**Vor externem Teilen Passwort drehen.**

## Einladungen

Einladungen werden in der DB angelegt, auch ohne SMTP. `EMAIL_SENDER` fehlt in Coolify → keine Mail. Link unter **Mitglieder → Offene Einladungen** kopieren (`/join/accept?invite_token=…`). Gültig **7 Tage**, bis angenommen. Der Accept-Link legt neue User **ohne Passwort** an — Passwort vor dem Logout setzen, sonst ist nach dem Annehmen kein erneuter Login möglich (Reset-Mails brauchen ebenfalls `EMAIL_SENDER`).

## Marketing / Docs

Öffentliche Landing ist intern (Anmelden + Kontakt). `/docs` ist aus Nav/Footer entfernt und leitet auf `/` um. Makerkit-Dokumentation ist kein Produktinhalt.

## Daten nachladen (ohne MCP)

**Nicht** Bulk-Seed über MCP `execute_sql` — das hat das Kontingent verbraucht.

1. Schema: `projects/rest_data_platform/scripts/push_supabase_cloud.ps1` (`supabase db push`, kein Reset).
2. Curated Daten: lokal `pg_dump`/`COPY` der `imc_*`-Tabellen **ohne** `imc_source_raw_rows`, `account_id` auf Cloud-Team `astra-imc` umschreiben, einspielen über `pnpm --filter web supabase db query --linked` (HTTPS). Direktes `psql` auf `db.<ref>.supabase.co` aus Docker scheitert (Host nur IPv6).
3. Roh-Excel bleibt lokal; bei Bedarf neu ingestieren aus `scripts/etl/`.

## Präsentieren

Eingeloggt: Team **ASTRA IMC** → Sidebar **Assets**. Partner ohne Laptop: https://imc.ostfriesland.ai
