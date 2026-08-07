-- Review MaStR DE match candidates (after match_mastr_de.py)

SELECT
  m.status,
  m.score,
  m.method,
  wf.name AS farm_name,
  wf.ext_windfarm_id,
  p.name_windpark AS mastr_park,
  p.unit_count,
  p.capacity_mw_sum,
  p.commissioning_min,
  p.commissioning_max,
  m.evidence->>'dist_km' AS dist_km,
  m.evidence->>'capacity_ratio' AS capacity_ratio,
  m.match_id
FROM public.imc_mastr_farm_matches m
JOIN public.imc_wind_farms wf ON wf.farm_id = m.farm_id
JOIN public.imc_mastr_park_agg p ON p.park_key = m.park_key
ORDER BY m.score DESC, wf.name
LIMIT 40;

-- Accept example (replace UUID):
-- UPDATE public.imc_mastr_farm_matches
-- SET status = 'accepted', reviewed_by = current_user, reviewed_at = now()
-- WHERE match_id = '...';
