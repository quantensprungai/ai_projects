-- Cleanup: Trianel II teilt sich denselben MaStR-Parknamen mit Phase I → reject
UPDATE public.imc_mastr_farm_matches m
SET
  status = 'rejected',
  reviewed_by = 'cleanup_trianel_phase_ambiguity',
  reviewed_at = now(),
  updated_at = now(),
  evidence = evidence || jsonb_build_object(
    'reject_reason',
    'Same MaStR NameWindpark as Trianel I; phases not separable in MaStR park name'
  )
FROM public.imc_wind_farms wf
WHERE m.farm_id = wf.farm_id
  AND m.status = 'accepted'
  AND wf.name = 'Trianel Windpark Borkum II';

-- Commissioning von Phase II zurücknehmen, wenn es vom MaStR-Doppelmatch kam
UPDATE public.imc_farm_milestones ms
SET full_commissioning = NULL, updated_at = now()
FROM public.imc_wind_farms wf
WHERE ms.farm_id = wf.farm_id
  AND wf.name = 'Trianel Windpark Borkum II'
  AND ms.full_commissioning = DATE '2015-07-16';

-- MaStR-Aliases an Phase II entfernen
UPDATE public.imc_wind_farms
SET
  aliases = ARRAY(
    SELECT a
    FROM unnest(aliases) AS a
    WHERE a NOT LIKE 'MaStR%'
  ),
  updated_at = now()
WHERE name = 'Trianel Windpark Borkum II';
