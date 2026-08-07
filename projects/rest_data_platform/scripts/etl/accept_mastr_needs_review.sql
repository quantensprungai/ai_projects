-- Accept high-confidence MaStR matches → accepted
-- 1) needs_review (name hits)
-- 2) clean geo candidates (dist ≤ 1 km, capacity ≥ 0.95)

UPDATE public.imc_mastr_farm_matches
SET
  status = 'accepted',
  reviewed_by = COALESCE(reviewed_by, 'batch_accept_needs_review'),
  reviewed_at = COALESCE(reviewed_at, now()),
  updated_at = now()
WHERE status = 'needs_review';

UPDATE public.imc_mastr_farm_matches
SET
  status = 'accepted',
  reviewed_by = COALESCE(reviewed_by, 'batch_accept_clean_geo'),
  reviewed_at = COALESCE(reviewed_at, now()),
  updated_at = now()
WHERE status = 'candidate'
  AND method = 'geo'
  AND score >= 0.95
  AND COALESCE((evidence->>'dist_km')::numeric, 99) <= 1.0
  AND COALESCE((evidence->>'capacity_ratio')::numeric, 0) >= 0.95;

SELECT status, method, count(*)
FROM public.imc_mastr_farm_matches
GROUP BY 1, 2
ORDER BY 1, 2;
