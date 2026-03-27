-- ============================================================================
-- IMC / ASTRA – PostgreSQL + PostGIS Schema v1 (public; Team-Accounts/RLS wie Anwendungsbasis)
-- Namenskonvention: Tabellen/Views/ENUMs Präfix imc_* (Organisationen: imc_orgs). Makerkit bleibt ohne Präfix.
-- Generiert: 2026-03-25 · Angepasst: 2026-03-27 (public, v1.1) · 2026-03-28 (imc_* Tabellen/ENUMs/Views, imc_orgs)
-- Basis: IMC_4C_to_AAS_Submodel_Mapping_v1.xlsx (93 Felder, 6 AAS-Submodels)
-- ============================================================================
-- Voraussetzungen:
--   • Baseline-Migrationen der App sind bereits angewendet (u. a. public.accounts).
--   • Hilfsfunktion public.has_role_on_account(uuid) existiert (Standard der Team-Account-Vorlage).
-- UUID: gen_random_uuid() (PostgreSQL integriert, kein uuid-ossp nötig).
-- Tenancy: imc_wind_farms.account_id → Team/Personal-Account; kinderlose Tabellen
--   nutzen Policies über farm_id → imc_wind_farms.
-- ============================================================================

-- ============================================================================
-- 0. EXTENSIONS
-- ============================================================================

CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS btree_gist;

-- ============================================================================
-- 1. ENUM-TYPEN
-- ============================================================================

CREATE TYPE public.imc_lifecycle_phase AS ENUM (
    'early_stage', 'planning', 'consented', 'pre_construction',
    'under_construction', 'operational', 'decommissioning', 'decommissioned',
    'cancelled', 'on_hold'
);

CREATE TYPE public.imc_foundation_type AS ENUM (
    'monopile', 'jacket', 'gravity_based', 'tripod', 'tripile',
    'suction_bucket', 'semi_submersible', 'spar', 'tension_leg',
    'barge', 'other', 'unknown'
);

CREATE TYPE public.imc_fixed_or_floating AS ENUM ('fixed', 'floating');

CREATE TYPE public.imc_vessel_type AS ENUM (
    'wtiv', 'clv', 'sov', 'ctv', 'jack_up_barge', 'heavy_lift',
    'cable_layer', 'survey', 'guard', 'tug', 'other'
);

CREATE TYPE public.imc_priority_level AS ENUM ('must', 'should', 'nice');

CREATE TYPE public.imc_data_source_type AS ENUM (
    '4c_windfarm', '4c_pop', '4c_transmission', '4c_vpi',
    '4c_interconnectors', 'bsh', 'era5', 'natura2000',
    'manual', 'lca_model', 'other'
);

CREATE TYPE public.imc_event_type AS ENUM (
    'site_exclusivity', 'submitted_for_consent', 'consent_granted',
    'offtake_secured', 'financial_close', 'construction_start',
    'offshore_construction_start', 'first_power', 'full_commissioning',
    'major_component_replacement', 'decom_start', 'decom_complete',
    'other'
);

CREATE TYPE public.imc_capex_category AS ENUM (
    'dev_to_fid', 'turbine_supply', 'turbine_installation',
    'foundation_supply', 'foundation_installation',
    'fa_ti_integration', 'floater_installation',
    'mooring_supply', 'mooring_installation',
    'array_cable_supply', 'array_cable_installation',
    'export_cable_supply', 'export_cable_installation',
    'offshore_substation_supply', 'offshore_substation_installation',
    'onshore_connection', 'contingency', 'other'
);

CREATE TYPE public.imc_opex_category AS ENUM (
    'transport', 'fuel', 'port_fees', 'large_component_replacement',
    'turbine_repairs', 'array_cable_repairs', 'export_cable_repairs',
    'substation_maintenance', 'moorings', 'lubricants', 'grid_power',
    'seabed_rental', 'insurance', 'training', 'staff',
    'onshore_logistics', 'offshore_logistics', 'hse_inspections',
    'environmental', 'other'
);

-- ============================================================================
-- 2. PROVENANCE & AUDIT (querschnittlich)
-- ============================================================================

CREATE TABLE public.imc_data_sources (
    source_id       UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    source_type     public.imc_data_source_type NOT NULL,
    source_name     TEXT NOT NULL,                     -- z.B. '4COffshore Wind Farm DB Q3/2024'
    source_version  TEXT,                              -- z.B. '2024-10-25'
    license_info    TEXT,
    snapshot_date   DATE NOT NULL,                     -- Datum des Exports/Downloads
    file_hash       TEXT,                              -- SHA-256 der Quelldatei
    notes           TEXT,
    created_at      TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE public.imc_audit_log (
    log_id          BIGSERIAL PRIMARY KEY,
    table_name      TEXT NOT NULL,
    record_id       UUID NOT NULL,
    operation       TEXT NOT NULL CHECK (operation IN ('INSERT','UPDATE','DELETE')),
    changed_by      TEXT NOT NULL DEFAULT current_user,
    changed_at      TIMESTAMPTZ DEFAULT now(),
    old_values      JSONB,
    new_values      JSONB
);

CREATE INDEX idx_audit_table_record ON public.imc_audit_log (table_name, record_id);
CREATE INDEX idx_audit_changed_at   ON public.imc_audit_log (changed_at);

-- ============================================================================
-- 3. NAMEPLATE (AAS Submodel: Identifikation & Standort)
-- ============================================================================

CREATE TABLE public.imc_wind_farms (
    farm_id             UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    account_id          UUID NOT NULL REFERENCES public.accounts(id) ON DELETE CASCADE,
    ext_windfarm_id     INTEGER UNIQUE,                     -- 4C WindfarmId
    name                TEXT NOT NULL,
    aliases             TEXT[],                              -- OtherNames
    country             TEXT NOT NULL,
    region              TEXT,
    georegion           TEXT,
    sea_basin           TEXT,                                -- SeaName
    lifecycle_phase     public.imc_lifecycle_phase NOT NULL,
    project_url         TEXT,
    location            GEOMETRY(Point, 4326),               -- Lat/Lon → PostGIS
    source_id           UUID REFERENCES public.imc_data_sources(source_id),
    created_at          TIMESTAMPTZ DEFAULT now(),
    updated_at          TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_farms_country   ON public.imc_wind_farms (country);
CREATE INDEX idx_farms_phase     ON public.imc_wind_farms (lifecycle_phase);
CREATE INDEX idx_farms_location  ON public.imc_wind_farms USING GIST (location);
CREATE INDEX idx_farms_account   ON public.imc_wind_farms (account_id);

-- ============================================================================
-- 4. TECHNICAL PROPERTIES (AAS Submodel: Technische Auslegung)
-- ============================================================================

-- 4a. Turbinen-Referenztabelle (normalisiert)
CREATE TABLE public.imc_turbine_models (
    turbine_model_id    UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    oem                 TEXT NOT NULL,                       -- z.B. 'Siemens Gamesa'
    model               TEXT NOT NULL,                       -- z.B. 'SG 14-236 DD'
    rated_power_mw      NUMERIC(6,2),
    rotor_diameter_m    NUMERIC(6,1),
    hub_height_m        NUMERIC(6,1),
    total_height_m      NUMERIC(6,1),
    is_reference        BOOLEAN DEFAULT false,               -- LCA-Referenztyp?
    source_id           UUID REFERENCES public.imc_data_sources(source_id),
    UNIQUE (oem, model)
);

-- 4b. Farm-Design (1:1 zu wind_farms, separiert wegen Größe)
CREATE TABLE public.imc_farm_design (
    farm_id                 UUID PRIMARY KEY REFERENCES public.imc_wind_farms(farm_id),
    rated_capacity_mw_min   NUMERIC(8,2),
    rated_capacity_mw_max   NUMERIC(8,2),
    turbine_model_id        UUID REFERENCES public.imc_turbine_models(turbine_model_id),
    is_estimated_turbine    BOOLEAN DEFAULT false,
    turbine_mw_min          NUMERIC(6,2),
    turbine_mw_max          NUMERIC(6,2),
    num_turbines_min        INTEGER,
    num_turbines_max        INTEGER,
    foundation_type         public.imc_foundation_type,
    foundation_detail       TEXT,                            -- FoundationsOnWindfarm
    foundation_comments     TEXT,
    fixed_or_floating       public.imc_fixed_or_floating,
    water_depth_min_m       NUMERIC(6,1),
    water_depth_max_m       NUMERIC(6,1),
    distance_from_shore_km  NUMERIC(7,2),
    dist_shore_auto_km      NUMERIC(7,2),
    site_area_km2           NUMERIC(8,2),
    power_density_mw_km2    NUMERIC(6,2),
    mean_wind_speed_100m    NUMERIC(5,2),
    mean_wind_speed_150m    NUMERIC(5,2),
    design_lifetime_years   INTEGER,
    -- Modelled Design (POP fallback)
    mod_capacity_mw         NUMERIC(8,2),
    mod_turbine_mw          NUMERIC(6,2),
    mod_num_turbines        INTEGER,
    source_id               UUID REFERENCES public.imc_data_sources(source_id),
    updated_at              TIMESTAMPTZ DEFAULT now()
);

-- 3c. Grid & Kabel
CREATE TABLE public.imc_farm_grid (
    farm_id                     UUID PRIMARY KEY REFERENCES public.imc_wind_farms(farm_id),
    num_export_cables           INTEGER,
    export_cable_length_km      NUMERIC(7,2),
    export_voltage_kv           NUMERIC(6,1),
    num_dc_cables               INTEGER,
    dc_cable_length_km          NUMERIC(7,2),
    dc_voltage_kv               NUMERIC(6,1),
    infield_cable_length_km     NUMERIC(7,2),
    infield_voltage_kv          NUMERIC(6,1),
    mod_array_cable_km          NUMERIC(7,2),           -- POP modelled
    mod_export_cable_km         NUMERIC(7,2),           -- POP modelled
    num_offshore_substations    INTEGER,
    mod_num_substations         INTEGER,
    grid_connection_point       TEXT,
    landing_point               TEXT,
    export_cable_comments       TEXT,
    infield_cable_comments      TEXT,
    source_id                   UUID REFERENCES public.imc_data_sources(source_id),
    updated_at                  TIMESTAMPTZ DEFAULT now()
);

-- ============================================================================
-- 5. ECONOMIC DATA (AAS Submodel: Kosten & Erlöse)
-- ============================================================================

-- 4a. Reported CAPEX (Originaldaten aus Projektquellen)
CREATE TABLE public.imc_farm_capex_reported (
    farm_id             UUID PRIMARY KEY REFERENCES public.imc_wind_farms(farm_id),
    reported_capex_text TEXT,                            -- Freitextfeld '4C CAPEX'
    project_cost_m      NUMERIC(10,2),
    project_cost_ccy    TEXT,                            -- ISO 4217
    project_cost_eur_m  NUMERIC(10,2),                  -- Umgerechnet
    capex_date          DATE,
    capex_source        TEXT,
    capex_comments      TEXT,
    source_id           UUID REFERENCES public.imc_data_sources(source_id),
    updated_at          TIMESTAMPTZ DEFAULT now()
);

-- 4b. Modelled CAPEX Breakdown (POP-Modell, 1:N pro Kategorie)
CREATE TABLE public.imc_farm_capex_modelled (
    capex_id            UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    farm_id             UUID NOT NULL REFERENCES public.imc_wind_farms(farm_id),
    category            public.imc_capex_category NOT NULL,
    amount_eur_m        NUMERIC(10,3),
    source_id           UUID REFERENCES public.imc_data_sources(source_id),
    updated_at          TIMESTAMPTZ DEFAULT now(),
    UNIQUE (farm_id, category)
);

-- 4c. Aggregierte CAPEX-Kennzahlen (POP)
CREATE TABLE public.imc_farm_capex_summary (
    farm_id             UUID PRIMARY KEY REFERENCES public.imc_wind_farms(farm_id),
    capex_per_mw_eur_m  NUMERIC(8,3),                   -- €m/MW
    total_capex_eur_m   NUMERIC(10,2),
    region_multiplier   NUMERIC(5,3),
    source_id           UUID REFERENCES public.imc_data_sources(source_id),
    updated_at          TIMESTAMPTZ DEFAULT now()
);

-- 4d. Revenue / Offtake
CREATE TABLE public.imc_farm_revenue (
    farm_id             UUID PRIMARY KEY REFERENCES public.imc_wind_farms(farm_id),
    revenue_mechanism   TEXT,                            -- CfD, FiT, PPA, Merchant
    revenue_details     TEXT,
    revenue_currency    TEXT,
    revenue_per_mwh     NUMERIC(8,2),
    revenue_eur_mwh     NUMERIC(8,2),                   -- Normalisiert
    subsidy_source      TEXT,
    source_id           UUID REFERENCES public.imc_data_sources(source_id),
    updated_at          TIMESTAMPTZ DEFAULT now()
);

-- 4e. Modelled OPEX Breakdown (POP-Modell, 1:N pro Kategorie)
CREATE TABLE public.imc_farm_opex_modelled (
    opex_id             UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    farm_id             UUID NOT NULL REFERENCES public.imc_wind_farms(farm_id),
    category            public.imc_opex_category NOT NULL,
    amount_keur_yr      NUMERIC(10,2),                  -- k€/Jahr
    source_id           UUID REFERENCES public.imc_data_sources(source_id),
    updated_at          TIMESTAMPTZ DEFAULT now(),
    UNIQUE (farm_id, category)
);

-- 4f. Aggregierte OPEX-Kennzahlen
CREATE TABLE public.imc_farm_opex_summary (
    farm_id             UUID PRIMARY KEY REFERENCES public.imc_wind_farms(farm_id),
    opex_total_eur_m_yr NUMERIC(8,3),                   -- €m/Jahr
    opex_per_mw_eur_m   NUMERIC(8,4),
    om_strategy         TEXT,                            -- Onshore/Offshore/Hybrid
    float_dist_to_port  NUMERIC(7,2),
    source_id           UUID REFERENCES public.imc_data_sources(source_id),
    updated_at          TIMESTAMPTZ DEFAULT now()
);

-- ============================================================================
-- 6. LIFECYCLE EVENTS (AAS Submodel: Lebenszyklus-Meilensteine)
-- ============================================================================

-- 5a. Schlüsseldaten (1:1, aus Wind Farm DB & POP)
CREATE TABLE public.imc_farm_milestones (
    farm_id                     UUID PRIMARY KEY REFERENCES public.imc_wind_farms(farm_id),
    site_exclusivity            DATE,
    submitted_for_consent       DATE,
    consent_granted             DATE,
    offtake_secured             DATE,
    financial_close             DATE,
    construction_start          DATE,
    offshore_construction_start DATE,
    first_power                 DATE,
    full_commissioning          DATE,
    -- POP-Ableitungen
    lease_to_first_power_yr     NUMERIC(5,1),
    fid_to_first_power_d_mw    NUMERIC(8,2),
    permit_process_months       NUMERIC(5,1),
    analyst_offshore_start_yr   INTEGER,
    analyst_confidence          TEXT,
    planned_decom_year          INTEGER,                 -- v1.1: DPP / Planung
    source_id                   UUID REFERENCES public.imc_data_sources(source_id),
    updated_at                  TIMESTAMPTZ DEFAULT now()
);

-- 5b. Event-Log (1:N, aus Events-Sheet)
CREATE TABLE public.imc_farm_events (
    event_id            UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    farm_id             UUID NOT NULL REFERENCES public.imc_wind_farms(farm_id),
    ext_event_id        INTEGER,                         -- 4C WindfarmEventId
    event_type          public.imc_event_type NOT NULL,
    event_date          DATE,
    description         TEXT,
    information_source  TEXT,
    certainty           TEXT,
    integrity           TEXT,
    event_code          TEXT,
    source_id           UUID REFERENCES public.imc_data_sources(source_id),
    created_at          TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_events_farm     ON public.imc_farm_events (farm_id);
CREATE INDEX idx_events_type     ON public.imc_farm_events (event_type);
CREATE INDEX idx_events_date     ON public.imc_farm_events (event_date);

-- ============================================================================
-- 7. LOGISTICS & DECOMMISSIONING (AAS Submodel: Logistik & Rückbau)
-- ============================================================================

-- 6a. Häfen
CREATE TABLE public.imc_ports (
    port_id             UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    port_name           TEXT NOT NULL,
    country             TEXT,
    location            GEOMETRY(Point, 4326),
    port_type           TEXT[],                          -- ['installation','o_and_m','decom']
    min_draft_m         NUMERIC(5,2),                    -- v1.1: Hafen-Matching / AnyLogic
    quay_length_m       NUMERIC(7,1),                    -- v1.1
    source_id           UUID REFERENCES public.imc_data_sources(source_id),
    created_at          TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_ports_location ON public.imc_ports USING GIST (location);

-- 6b. Farm ↔ Port Zuordnung
CREATE TABLE public.imc_farm_ports (
    farm_id             UUID NOT NULL REFERENCES public.imc_wind_farms(farm_id),
    port_id             UUID NOT NULL REFERENCES public.imc_ports(port_id),
    role                TEXT NOT NULL CHECK (role IN ('installation','o_and_m','decom','staging')),
    source_id           UUID REFERENCES public.imc_data_sources(source_id),
    PRIMARY KEY (farm_id, port_id, role)
);

-- 6c. Schiffe / Vessels (VPI)
CREATE TABLE public.imc_vessels (
    vessel_id           UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    vessel_name         TEXT NOT NULL,
    imo_number          TEXT UNIQUE,
    vessel_type         public.imc_vessel_type NOT NULL,
    vessel_sub_type     TEXT,
    -- Technische Constraints (AnyLogic-relevant)
    crane_capacity_t    NUMERIC(8,1),
    max_lift_height_m   NUMERIC(6,1),
    max_wave_height_m   NUMERIC(4,1),                   -- Weather-Window
    max_wind_speed_ms   NUMERIC(5,1),                   -- Weather-Window
    transit_speed_kn    NUMERIC(5,1),
    deck_load_t         NUMERIC(8,1),
    deck_area_m2        NUMERIC(8,1),
    fuel_consumption_t_d NUMERIC(6,2),                  -- LCA Scope 3
    day_rate_eur        NUMERIC(10,2),
    mobilisation_days   INTEGER,                        -- v1.1: Charter-Vorlauf
    source_id           UUID REFERENCES public.imc_data_sources(source_id),
    updated_at          TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_vessels_type ON public.imc_vessels (vessel_type);

-- 6d. Vessel ↔ Farm Zuordnung (Einsatzhistorie)
CREATE TABLE public.imc_vessel_assignments (
    assignment_id       UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    vessel_id           UUID NOT NULL REFERENCES public.imc_vessels(vessel_id),
    farm_id             UUID REFERENCES public.imc_wind_farms(farm_id),
    project_name        TEXT,                            -- Falls Farm nicht in DB
    contract_scope      TEXT,
    period_start        DATE,
    period_end          DATE,
    source_id           UUID REFERENCES public.imc_data_sources(source_id)
);

-- ============================================================================
-- 8. SUPPLY CHAIN (AAS Submodel: Lieferkette)
-- ============================================================================

CREATE TABLE public.imc_orgs (
    org_id              UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    org_name            TEXT NOT NULL,
    parent_org          TEXT,
    address             TEXT,
    city                TEXT,
    country             TEXT,
    website             TEXT,
    source_id           UUID REFERENCES public.imc_data_sources(source_id),
    UNIQUE (org_name, country)
);

CREATE TABLE public.imc_farm_stakeholders (
    stakeholder_id      UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    ext_id              INTEGER,                         -- 4C WindfarmStakeholderId
    farm_id             UUID NOT NULL REFERENCES public.imc_wind_farms(farm_id),
    org_id              UUID REFERENCES public.imc_orgs(org_id),
    stakeholder_type    TEXT NOT NULL,                   -- Owner, Developer, Contractor...
    sub_type_category   TEXT,
    sub_type            TEXT,
    client              TEXT,
    stake_description   TEXT,
    stake_value         NUMERIC(12,2),
    stake_currency      TEXT,
    cost_description    TEXT,
    is_expired          BOOLEAN DEFAULT false,
    source_id           UUID REFERENCES public.imc_data_sources(source_id),
    created_at          TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_stakeholders_farm ON public.imc_farm_stakeholders (farm_id);
CREATE INDEX idx_stakeholders_type ON public.imc_farm_stakeholders (stakeholder_type);

-- ============================================================================
-- 9. OFFSHORE-SUBSTATIONS / PLATTFORMEN
-- ============================================================================

CREATE TABLE public.imc_offshore_platforms (
    platform_id         UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    ext_platform_id     INTEGER,                         -- 4C PlatformID
    farm_id             UUID NOT NULL REFERENCES public.imc_wind_farms(farm_id),
    platform_name       TEXT,
    platform_group_type TEXT,
    platform_type       TEXT,
    platform_owner      TEXT,
    connecting_farms    TEXT,
    source_id           UUID REFERENCES public.imc_data_sources(source_id)
);

-- ============================================================================
-- 10. TRANSMISSION & CABLES (ergänzend, 4C Transmission DB)
-- ============================================================================

CREATE TABLE public.imc_transmission_assets (
    asset_id            UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    farm_id             UUID REFERENCES public.imc_wind_farms(farm_id),
    cable_name          TEXT,
    cable_type          TEXT,
    voltage_kv          NUMERIC(6,1),
    cable_length_km     NUMERIC(7,2),
    manufacturer        TEXT,
    installer           TEXT,
    source_id           UUID REFERENCES public.imc_data_sources(source_id)
);

-- ============================================================================
-- 11. VIEWS (Convenience, security_invoker = RLS der Basistabellen)
-- ============================================================================

DROP VIEW IF EXISTS public.imc_v_capex_breakdown;
DROP VIEW IF EXISTS public.imc_v_farm_overview;
DROP VIEW IF EXISTS public.imc_v_vessels_anylogic;

-- Vollständige Farm-Übersicht
CREATE VIEW public.imc_v_farm_overview
WITH (security_invoker = true) AS
SELECT
    wf.farm_id,
    wf.ext_windfarm_id,
    wf.name,
    wf.country,
    wf.region,
    wf.lifecycle_phase,
    ST_Y(wf.location) AS lat,
    ST_X(wf.location) AS lon,
    fd.rated_capacity_mw_max    AS capacity_mw,
    fd.num_turbines_max         AS num_turbines,
    tm.oem,
    tm.model                    AS turbine_model,
    fd.foundation_type,
    fd.fixed_or_floating,
    fd.water_depth_max_m,
    fd.distance_from_shore_km,
    fd.design_lifetime_years,
    cr.project_cost_eur_m       AS reported_cost_eur_m,
    cs.total_capex_eur_m        AS modelled_capex_eur_m,
    os.opex_total_eur_m_yr,
    rv.revenue_mechanism,
    rv.revenue_eur_mwh,
    ms.first_power,
    ms.full_commissioning
FROM public.imc_wind_farms wf
LEFT JOIN public.imc_farm_design fd    ON fd.farm_id = wf.farm_id
LEFT JOIN public.imc_turbine_models tm ON tm.turbine_model_id = fd.turbine_model_id
LEFT JOIN public.imc_farm_capex_reported cr ON cr.farm_id = wf.farm_id
LEFT JOIN public.imc_farm_capex_summary cs  ON cs.farm_id = wf.farm_id
LEFT JOIN public.imc_farm_opex_summary os   ON os.farm_id = wf.farm_id
LEFT JOIN public.imc_farm_revenue rv        ON rv.farm_id = wf.farm_id
LEFT JOIN public.imc_farm_milestones ms     ON ms.farm_id = wf.farm_id;

-- AnyLogic-relevante Vessel-Parameter
CREATE VIEW public.imc_v_vessels_anylogic
WITH (security_invoker = true) AS
SELECT
    v.vessel_id,
    v.vessel_name,
    v.imo_number,
    v.vessel_type,
    v.vessel_sub_type,
    v.crane_capacity_t,
    v.max_lift_height_m,
    v.max_wave_height_m,
    v.max_wind_speed_ms,
    v.transit_speed_kn,
    v.deck_load_t,
    v.deck_area_m2,
    v.fuel_consumption_t_d,
    v.day_rate_eur
FROM public.imc_vessels v;

-- CAPEX-Breakdown flach (für LCA-Proxy-Gewichtung)
CREATE VIEW public.imc_v_capex_breakdown
WITH (security_invoker = true) AS
SELECT
    wf.farm_id,
    wf.name,
    wf.country,
    cm.category,
    cm.amount_eur_m,
    cs.total_capex_eur_m,
    CASE WHEN cs.total_capex_eur_m > 0
         THEN ROUND((cm.amount_eur_m / cs.total_capex_eur_m * 100)::numeric, 1)
         ELSE NULL
    END AS pct_of_total
FROM public.imc_farm_capex_modelled cm
JOIN public.imc_wind_farms wf          ON wf.farm_id = cm.farm_id
LEFT JOIN public.imc_farm_capex_summary cs ON cs.farm_id = cm.farm_id;

-- ============================================================================
-- 12. ROW-LEVEL SECURITY + GRANTS (Muster wie Anwendungsbasis)
-- ============================================================================
-- Voraussetzung: public.has_role_on_account(account_uuid) aus der App-Baseline.
-- service_role umgeht RLS (Supabase) – ETL/Admin-Client.
-- Re-Apply: vor erneutem CREATE jeweils DROP POLICY … ON …; sonst Fehler.

-- --- imc_wind_farms (Tenant-Grenze: account_id) ---
ALTER TABLE public.imc_wind_farms ENABLE ROW LEVEL SECURITY;
CREATE POLICY imc_wind_farms_all
  ON public.imc_wind_farms
  FOR ALL
  TO authenticated
  USING (public.has_role_on_account(account_id))
  WITH CHECK (public.has_role_on_account(account_id));

-- --- Tabellen mit farm_id / PK farm_id: Zugriff nur wenn Farm im Account ---
DO $imc_rls$
DECLARE
  t text;
BEGIN
  FOREACH t IN ARRAY ARRAY[
    'farm_design',
    'farm_grid',
    'farm_capex_reported',
    'farm_capex_modelled',
    'farm_capex_summary',
    'farm_revenue',
    'farm_opex_modelled',
    'farm_opex_summary',
    'farm_milestones',
    'farm_events',
    'farm_ports',
    'farm_stakeholders',
    'offshore_platforms'
  ]
  LOOP
    EXECUTE format(
      'ALTER TABLE public.imc_%I ENABLE ROW LEVEL SECURITY',
      t
    );
    EXECUTE format(
      $p$
      CREATE POLICY %I ON public.imc_%I
        FOR ALL TO authenticated
        USING (
          EXISTS (
            SELECT 1 FROM public.imc_wind_farms wf
            WHERE wf.farm_id = farm_id
              AND public.has_role_on_account(wf.account_id)
          )
        )
        WITH CHECK (
          EXISTS (
            SELECT 1 FROM public.imc_wind_farms wf
            WHERE wf.farm_id = farm_id
              AND public.has_role_on_account(wf.account_id)
          )
        )
      $p$,
      'imc_' || t || '_all',
      t
    );
  END LOOP;
END
$imc_rls$;

-- --- transmission_assets: optional ohne farm_id (Katalog) ---
ALTER TABLE public.imc_transmission_assets ENABLE ROW LEVEL SECURITY;
CREATE POLICY imc_transmission_assets_select
  ON public.imc_transmission_assets
  FOR SELECT
  TO authenticated
  USING (
    farm_id IS NULL
    OR EXISTS (
      SELECT 1 FROM public.imc_wind_farms wf
      WHERE wf.farm_id = imc_transmission_assets.farm_id
        AND public.has_role_on_account(wf.account_id)
    )
  );
CREATE POLICY imc_transmission_assets_write
  ON public.imc_transmission_assets
  FOR ALL
  TO authenticated
  USING (
    farm_id IS NOT NULL
    AND EXISTS (
      SELECT 1 FROM public.imc_wind_farms wf
      WHERE wf.farm_id = imc_transmission_assets.farm_id
        AND public.has_role_on_account(wf.account_id)
    )
  )
  WITH CHECK (
    farm_id IS NOT NULL
    AND EXISTS (
      SELECT 1 FROM public.imc_wind_farms wf
      WHERE wf.farm_id = imc_transmission_assets.farm_id
        AND public.has_role_on_account(wf.account_id)
    )
  );

-- --- vessel_assignments: Zeilen ohne farm_id = gemeinsamer Flottenkatalog ---
ALTER TABLE public.imc_vessel_assignments ENABLE ROW LEVEL SECURITY;
CREATE POLICY imc_vessel_assignments_select
  ON public.imc_vessel_assignments
  FOR SELECT
  TO authenticated
  USING (
    farm_id IS NULL
    OR EXISTS (
      SELECT 1 FROM public.imc_wind_farms wf
      WHERE wf.farm_id = imc_vessel_assignments.farm_id
        AND public.has_role_on_account(wf.account_id)
    )
  );
CREATE POLICY imc_vessel_assignments_write
  ON public.imc_vessel_assignments
  FOR ALL
  TO authenticated
  USING (
    farm_id IS NOT NULL
    AND EXISTS (
      SELECT 1 FROM public.imc_wind_farms wf
      WHERE wf.farm_id = imc_vessel_assignments.farm_id
        AND public.has_role_on_account(wf.account_id)
    )
  )
  WITH CHECK (
    farm_id IS NOT NULL
    AND EXISTS (
      SELECT 1 FROM public.imc_wind_farms wf
      WHERE wf.farm_id = imc_vessel_assignments.farm_id
        AND public.has_role_on_account(wf.account_id)
    )
  );

-- --- Globale Stammdaten (lesbar für alle eingeloggten Nutzer; Schreiben nur service_role) ---
ALTER TABLE public.imc_data_sources ENABLE ROW LEVEL SECURITY;
CREATE POLICY imc_data_sources_select ON public.imc_data_sources FOR SELECT TO authenticated USING (true);

ALTER TABLE public.imc_turbine_models ENABLE ROW LEVEL SECURITY;
CREATE POLICY imc_turbine_models_select ON public.imc_turbine_models FOR SELECT TO authenticated USING (true);

ALTER TABLE public.imc_ports ENABLE ROW LEVEL SECURITY;
CREATE POLICY imc_ports_select ON public.imc_ports FOR SELECT TO authenticated USING (true);

ALTER TABLE public.imc_vessels ENABLE ROW LEVEL SECURITY;
CREATE POLICY imc_vessels_select ON public.imc_vessels FOR SELECT TO authenticated USING (true);

ALTER TABLE public.imc_orgs ENABLE ROW LEVEL SECURITY;
CREATE POLICY imc_orgs_select ON public.imc_orgs FOR SELECT TO authenticated USING (true);

-- --- Audit: nicht über Standard-Client ---
ALTER TABLE public.imc_audit_log ENABLE ROW LEVEL SECURITY;
-- Keine Policy für authenticated → kein Zugriff; service_role schreibt/liest bei Bedarf ohne RLS-Wirkung

-- ============================================================================
-- Grants (üblich: erst revoke, dann gezielt grant)
-- ============================================================================

REVOKE ALL ON public.imc_wind_farms FROM anon, authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_wind_farms TO authenticated;

REVOKE ALL ON public.imc_farm_design, public.imc_farm_grid, public.imc_farm_capex_reported,
  public.imc_farm_capex_modelled, public.imc_farm_capex_summary, public.imc_farm_revenue,
  public.imc_farm_opex_modelled, public.imc_farm_opex_summary, public.imc_farm_milestones,
  public.imc_farm_events, public.imc_farm_ports, public.imc_farm_stakeholders,
  public.imc_offshore_platforms, public.imc_transmission_assets, public.imc_vessel_assignments
  FROM anon, authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_farm_design TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_farm_grid TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_farm_capex_reported TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_farm_capex_modelled TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_farm_capex_summary TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_farm_revenue TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_farm_opex_modelled TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_farm_opex_summary TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_farm_milestones TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_farm_events TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_farm_ports TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_farm_stakeholders TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_offshore_platforms TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_transmission_assets TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.imc_vessel_assignments TO authenticated;

REVOKE ALL ON public.imc_data_sources, public.imc_turbine_models, public.imc_ports, public.imc_vessels, public.imc_orgs
  FROM anon, authenticated;
GRANT SELECT ON public.imc_data_sources TO authenticated;
GRANT SELECT ON public.imc_turbine_models TO authenticated;
GRANT SELECT ON public.imc_ports TO authenticated;
GRANT SELECT ON public.imc_vessels TO authenticated;
GRANT SELECT ON public.imc_orgs TO authenticated;

REVOKE ALL ON public.imc_audit_log FROM anon, authenticated;

GRANT SELECT ON public.imc_v_farm_overview, public.imc_v_vessels_anylogic, public.imc_v_capex_breakdown TO authenticated;

-- ============================================================================
-- 13. KOMMENTAR: TABELLEN-ÜBERSICHT
-- ============================================================================
-- Tabelle                      | AAS Submodel        | Zeilen (erwartet Stage A)
-- ----------------------------|---------------------|-------------------------
-- imc_wind_farms                | Nameplate           | ~2.000 (global 4C)
-- imc_turbine_models            | TechnicalProperties | ~150
-- imc_farm_design               | TechnicalProperties | ~2.000
-- imc_farm_grid                 | TechnicalProperties | ~2.000
-- imc_farm_capex_reported       | EconomicData        | ~1.500
-- imc_farm_capex_modelled       | EconomicData        | ~1.500 × 17 Kategorien
-- imc_farm_capex_summary        | EconomicData        | ~1.500
-- imc_farm_revenue              | EconomicData        | ~1.500
-- imc_farm_opex_modelled        | EconomicData        | ~1.000 × 20 Kategorien
-- imc_farm_opex_summary         | EconomicData        | ~1.000
-- imc_farm_milestones           | LifecycleEvents     | ~2.000
-- imc_farm_events               | LifecycleEvents     | ~20.000
-- imc_ports                     | LogisticsDecom      | ~500
-- imc_farm_ports                | LogisticsDecom      | ~4.000
-- imc_vessels                   | LogisticsDecom      | ~800
-- imc_vessel_assignments        | LogisticsDecom      | ~3.000
-- imc_orgs                      | SupplyChain         | ~2.000
-- imc_farm_stakeholders         | SupplyChain         | ~15.000
-- imc_offshore_platforms        | TechnicalProperties | ~500
-- imc_transmission_assets       | TechnicalProperties | ~1.000
-- imc_data_sources              | (Querschnitt)       | ~50
-- imc_audit_log                 | (Querschnitt)       | wachsend
-- ----------------------------|---------------------|-------------------------
-- GESAMT: 22 Tabellen + 3 Views + 12 ENUMs (Präfix imc_* / imc_orgs; ENUMs imc_*)
--
-- v1.1-Spalten (bereits im CREATE TABLE oben): imc_farm_milestones.planned_decom_year,
--   imc_ports.min_draft_m, imc_ports.quay_length_m, imc_vessels.mobilisation_days

-- ============================================================================
-- ANHANG: Upgrade v1 → v1.1 (nur wenn ältere v1-DDL schon deployed wurde)
-- ============================================================================
-- ALTER TABLE public.imc_farm_milestones ADD COLUMN IF NOT EXISTS planned_decom_year INTEGER;
-- ALTER TABLE public.imc_ports ADD COLUMN IF NOT EXISTS min_draft_m NUMERIC(5,2);
-- ALTER TABLE public.imc_ports ADD COLUMN IF NOT EXISTS quay_length_m NUMERIC(7,1);
-- ALTER TABLE public.imc_vessels ADD COLUMN IF NOT EXISTS mobilisation_days INTEGER;
