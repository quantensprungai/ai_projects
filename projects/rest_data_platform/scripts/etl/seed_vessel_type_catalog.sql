-- ============================================================================
-- Seed: 8 vessel TYPE catalog rows (placeholders for Marc)
-- Idempotent via unique index idx_imc_vessels_one_catalog_per_type (vessel_type)
-- Weather/crane = documented placeholders — override later in DB/UI/AnyLogic
-- Requires migration 20260826140000_imc_vessel_type_catalog.sql
-- ============================================================================

insert into public.imc_vessels (
  vessel_name,
  ext_vessel_key,
  vessel_type,
  vessel_sub_type,
  is_type_catalog,
  max_wind_speed_ms,
  max_wave_height_m,
  transit_speed_kn,
  crane_capacity_t,
  constraint_note,
  source_id
)
values
  (
    'TYPE_CTV',
    'type:ctv',
    'ctv',
    'catalog',
    true,
    12.0,
    1.5,
    20.0,
    6.0,
    'placeholder_pending_marc — aligned with platform ERA5 defaults (12 m/s, 1.5 m Hs)',
    'a1000001-0001-4001-8001-000000000003'
  ),
  (
    'TYPE_SOV',
    'type:sov',
    'sov',
    'catalog_w2w',
    true,
    15.0,
    2.5,
    12.0,
    20.0,
    'placeholder_pending_marc — W2W/SOV family; looser weather than CTV',
    'a1000001-0001-4001-8001-000000000003'
  ),
  (
    'TYPE_JACK_UP_BARGE',
    'type:jack_up_barge',
    'jack_up_barge',
    'catalog',
    true,
    15.0,
    2.0,
    8.0,
    400.0,
    'placeholder_pending_marc — work jack-up; crane capacity indicative',
    'a1000001-0001-4001-8001-000000000003'
  ),
  (
    'TYPE_WTIV',
    'type:wtiv',
    'wtiv',
    'catalog',
    true,
    15.0,
    2.0,
    10.0,
    1500.0,
    'placeholder_pending_marc — installation jack-up; crane indicative',
    'a1000001-0001-4001-8001-000000000003'
  ),
  (
    'TYPE_HEAVY_LIFT',
    'type:heavy_lift',
    'heavy_lift',
    'catalog',
    true,
    12.0,
    1.5,
    12.0,
    3000.0,
    'placeholder_pending_marc — HLV; crane indicative for foundation/OSS',
    'a1000001-0001-4001-8001-000000000003'
  ),
  (
    'TYPE_CABLE_LAYER',
    'type:cable_layer',
    'cable_layer',
    'catalog',
    true,
    12.0,
    1.5,
    12.0,
    null,
    'placeholder_pending_marc — CLV weather conservative',
    'a1000001-0001-4001-8001-000000000003'
  ),
  (
    'TYPE_TUG',
    'type:tug',
    'tug',
    'catalog',
    true,
    15.0,
    2.0,
    14.0,
    null,
    'placeholder_pending_marc — tug/AHTS-like assist',
    'a1000001-0001-4001-8001-000000000003'
  ),
  (
    'TYPE_SURVEY',
    'type:survey',
    'survey',
    'catalog',
    true,
    12.0,
    1.5,
    12.0,
    null,
    'placeholder_pending_marc — survey/ROV support',
    'a1000001-0001-4001-8001-000000000003'
  )
on conflict (vessel_type) where (is_type_catalog)
do update set
  vessel_name = excluded.vessel_name,
  ext_vessel_key = excluded.ext_vessel_key,
  vessel_sub_type = excluded.vessel_sub_type,
  max_wind_speed_ms = excluded.max_wind_speed_ms,
  max_wave_height_m = excluded.max_wave_height_m,
  transit_speed_kn = excluded.transit_speed_kn,
  crane_capacity_t = excluded.crane_capacity_t,
  constraint_note = excluded.constraint_note,
  source_id = excluded.source_id,
  updated_at = now();

-- Marc catalog placeholders (requires 20260827114145_imc_vessel_catalog_marc_fields.sql)
update public.imc_vessels
set
  fuel_consumption_t_d = coalesce(fuel_consumption_t_d, case vessel_type
    when 'ctv' then 2.0
    when 'sov' then 8.0
    when 'jack_up_barge' then 12.0
    when 'wtiv' then 25.0
    when 'heavy_lift' then 20.0
    when 'cable_layer' then 15.0
    when 'survey' then 4.0
    when 'tug' then 6.0
    else null
  end),
  mobilisation_days = coalesce(mobilisation_days, case vessel_type
    when 'ctv' then 1
    when 'sov' then 3
    when 'jack_up_barge' then 7
    when 'wtiv' then 14
    when 'heavy_lift' then 10
    when 'cable_layer' then 7
    when 'survey' then 2
    when 'tug' then 1
    else null
  end),
  jacking_time_h = coalesce(jacking_time_h, case vessel_type
    when 'jack_up_barge' then 4.0
    when 'wtiv' then 6.0
    else null
  end),
  availability_note = coalesce(
    availability_note,
    'assumed year-round; override in AnyLogic'
  ),
  updated_at = now()
where is_type_catalog;
