-- ============================================================================
-- Alpha Ventus Pilot-Kuratierung (idempotent)
-- Zweck: Stage-A Vertical Slice — Foundation/Provenance für Demo
-- Ausführung: nach 4C Transform, lokal Team-Account-Account-IDs
-- ============================================================================

-- 1) Stammdaten: stabile 4C-ID, Aliase, Status operational
UPDATE public.imc_wind_farms wf
SET
  ext_windfarm_id = COALESCE(NULLIF(wf.ext_windfarm_id, ''), 'DE01'),
  lifecycle_phase = 'operational',
  region = COALESCE(wf.region, 'Niedersachsen'),
  sea_basin = COALESCE(wf.sea_basin, 'North Sea'),
  georegion = COALESCE(wf.georegion, 'Europe'),
  aliases = (
    SELECT ARRAY(
      SELECT DISTINCT a
      FROM unnest(
        COALESCE(wf.aliases, ARRAY[]::text[])
        || ARRAY['Borkum West I', 'ASTRA Pilot WP 2.1', '4C:DE01']
      ) AS a
      WHERE a IS NOT NULL AND btrim(a) <> ''
    )
  ),
  updated_at = now()
WHERE wf.name ILIKE 'Alpha Ventus';

-- 2) Design: Tripod (kuratiert), 4C-Rohtext behalten, Kommentar für Demo
UPDATE public.imc_farm_design fd
SET
  foundation_type = 'tripod',
  foundation_detail = COALESCE(
    NULLIF(fd.foundation_detail, ''),
    'Grounded: Various'
  ),
  foundation_comments = 'Kuratiert Stage A: Alpha Ventus - 12 Turbinen (historisch u.a. REpower 5M / AREVA M5000), Tripod-Fundamente. 4C lieferte Foundation Grounded: Various; Pilot-Override auf tripod. Quelle: 4C + manuelle Kuratierung (source ...032).',
  fixed_or_floating = 'fixed',
  rated_capacity_mw_max = COALESCE(fd.rated_capacity_mw_max, 60),
  num_turbines_max = COALESCE(fd.num_turbines_max, 12),
  source_id = COALESCE(fd.source_id, 'a1000001-0001-4001-8001-000000000001'),
  updated_at = now()
FROM public.imc_wind_farms wf
WHERE fd.farm_id = wf.farm_id
  AND wf.name ILIKE 'Alpha Ventus';

-- 3) Sicherstellen, dass Design-Zeile existiert (falls Transform fehlte)
INSERT INTO public.imc_farm_design (
  farm_id,
  rated_capacity_mw_max,
  num_turbines_max,
  foundation_type,
  foundation_detail,
  foundation_comments,
  fixed_or_floating,
  source_id
)
SELECT
  wf.farm_id,
  60,
  12,
  'tripod',
  'Grounded: Various',
  'Kuratiert Stage A: Alpha Ventus - Tripod-Fundamente (Pilot-Override).',
  'fixed',
  'a1000001-0001-4001-8001-000000000001'
FROM public.imc_wind_farms wf
WHERE wf.name ILIKE 'Alpha Ventus'
  AND NOT EXISTS (
    SELECT 1 FROM public.imc_farm_design d WHERE d.farm_id = wf.farm_id
  );
