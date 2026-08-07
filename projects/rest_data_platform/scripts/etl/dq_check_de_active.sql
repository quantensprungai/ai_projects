-- ============================================================================
-- IMC Slice-1 — leichter DQ-Check (DE aktiv, ohne cancelled)
-- Stand: 2026-08-07
-- ============================================================================

WITH de_active AS (
  SELECT
    wf.farm_id,
    wf.name,
    wf.country,
    wf.lifecycle_phase,
    wf.location IS NOT NULL AS has_location,
    fd.rated_capacity_mw_max AS capacity_mw,
    fd.foundation_type,
    wf.source_id
  FROM public.imc_wind_farms wf
  LEFT JOIN public.imc_farm_design fd ON fd.farm_id = wf.farm_id
  WHERE wf.country = 'Germany'
    AND wf.lifecycle_phase <> 'cancelled'
)
SELECT 'de_active_count' AS check_id, count(*)::text AS value FROM de_active
UNION ALL SELECT 'missing_name', count(*)::text FROM de_active WHERE name IS NULL OR btrim(name) = ''
UNION ALL SELECT 'missing_status', count(*)::text FROM de_active WHERE lifecycle_phase IS NULL
UNION ALL SELECT 'missing_capacity', count(*)::text FROM de_active WHERE capacity_mw IS NULL
UNION ALL SELECT 'missing_foundation', count(*)::text
  FROM de_active
  WHERE foundation_type IS NULL OR foundation_type::text IN ('unknown')
UNION ALL SELECT 'missing_location', count(*)::text FROM de_active WHERE NOT has_location
UNION ALL SELECT 'missing_source', count(*)::text FROM de_active WHERE source_id IS NULL
UNION ALL SELECT 'duplicate_name_country', count(*)::text FROM (
  SELECT name, country
  FROM public.imc_wind_farms
  WHERE country = 'Germany' AND lifecycle_phase <> 'cancelled'
  GROUP BY name, country
  HAVING count(*) > 1
) d
UNION ALL
SELECT 'status_' || lifecycle_phase, count(*)::text
FROM de_active
GROUP BY lifecycle_phase
ORDER BY 1;
