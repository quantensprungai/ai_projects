# K2 Foundation — Sanierung & Abschluss-Gate (2026-07-12)

last_update: 2026-07-12
scope: Gesamtsanierung BaZi/HD/GK nach Re-Seed-Bug; Abschluss-Gate vor nächster Content-Welle
in_scope: Metadata-Wipe, Relink, Restore, Cleanup, Audit, Werk-Reihenfolge, Synthese-Cap
out_of_scope: App-Implementierung, Cross-System (Phase 3)

## Auslöser

Re-Seed (`ic_seed_structure.py`) lief **vor** dem Metadata-Erhalt-Fix und überschrieb bei jedem Upsert:
- `metadata.interpretation_ids` / `chunk_ids` (K3-Links)
- `canonical_description` (K4 auf dem Node)

**Betroffen:** BaZi (entdeckt 2026-07-11, repariert) und HD (entdeckt 2026-07-12, repariert). GK nicht betroffen (kein Re-Seed nach Content).

## Sanierungs-Ablauf (wiederholbar)

```
1. ic_k2_state_audit.py              → Ist-Zustand messen
2. ic_relink_strict.py --system X    → interpretation_ids aus sys_interpretations zurück
3. ic_restore_desc_from_wordings.py → canonical_description aus sys_synthesis_wordings (ohne LLM)
4. ic_*_alias_remap.py / wildwuchs   → Duplikate remappen + löschen
5. ic_k2_synth_batch.py              → fehlende Synthese (nur Nodes ohne Description)
6. ic_k2_state_audit.py              → Abschluss-Gate: 0 Jobs, 0 Wildwuchs, Interp→Synth vollständig
```

## Ergebnis 2026-07-12

| System | Nodes | Interp-Nodes | Synthese | Wildwuchs | Jobs |
|--------|-------|--------------|----------|-----------|------|
| BaZi | 97 | 34 | 37 ✅ | 0 | 0 |
| HD | 777 | 114 | 114 ✅ | 0 | 0 |
| Gene Keys | 64 | 64 | 64 ✅ | 0 | 0 |

**Durchgeführte Aktionen:**
- HD Re-Link: 136 + 542 Links (Rave I'Ching + Life Force)
- Description-Restore: 32 BaZi + 105 HD (aus `sys_synthesis_wordings`)
- HD Alias-Remap: 8 remapped, 10 gelöscht (`g_center`→`g`, `outer`→`mental`, …)
- HD Wildwuchs: 260 Extras (2026-07-11) + 10 Alias-Junk (2026-07-12)
- GK Wildwuchs: 167 `genekeys.asset_chunk.*`
- 3 Zombie-`synthesize_node`-Jobs geschlossen

## Neue Pflicht-Regeln (ab sofort)

1. **Nach jedem Seed:** `python ic_k2_state_audit.py` — Interp-Count darf nicht sinken
2. **Seed ist idempotent** (Metadata-Erhalt in `ic_seed_structure.py` seit 2026-07-11)
3. **Abschluss einer Welle** = Audit grün, nicht „Skripte existieren“
4. **Kein Content ohne strict text2kg** für das Zielsystem

## Werk-Reihenfolge (empirisch)

| Typ | Beispiel | Synthese-Qualität |
|-----|----------|-------------------|
| Referenz/Lexikon | Rave I'Ching (1 Gate = 1 Kapitel) | Hoch — wenige, präzise Interps |
| Überblick | Destiny Code (BaZi quer) | Mittel — Cap + Relevanz nötig |
| Spezialwerk | Da Yun, Jiazi-Nayin | Hoch auf wenigen Nodes — Re-Synth `--only-id` |

**Empfehlung:** Referenz → Überblick → Spezial. Nicht umgekehrt.

## Synthese-Cap — wann welcher Wert

| Situation | `IC_SYNTHESIS_MAX_INTERPS` | Aktion |
|-----------|---------------------------|--------|
| Erstes Referenzwerk | irrelevant (1–3 Interps/Node) | Normal synthetisieren |
| Überblickswerk | **8** (Default) | Relevanz-Score aktiv |
| Nach Spezialwerk | 10–12 | `--only-id` Re-Synth |
| Node mit >50 Interps, generischer Text | 5–6 | Stichprobe lesen, ggf. `--force` |

Cap **dynamisch per Werk-Typ steuern** (Env/Job-Debug), kein Automatismus nötig solange wenige PDFs.

## Best-Practice-Abgleich

Unser Ansatz entspricht **ontology-guided KG construction** (Stand Forschung/Industrie 2024–2026):
- Schema/Seed vor Extraktion ✅
- Post-hoc Validation gegen Whitelist ✅
- Entity Resolution via Alias-Registry ✅
- Iterative Schema-Erweiterung (Wellen) ✅
- Hierarchisches Clustering für Synthese → Backlog (erst bei Mehrquellen)

**Was bei uns anders ist (bewusst):**
- Kein Embedding-Matching für Entity Resolution (geschlossene Kataloge mit Slugs reichen)
- Chunks nicht als Graph-Nodes (`chunk_ids` in Metadata statt `asset_chunk`-Nodes — letztere sind Wildwuchs)
- LLM-Synthese statt regelbasiertem Merge (flexibler, aber Qualitäts-Gate nötig)

**Nicht falsch, nicht Trial-and-Error pur** — aber domain-spezifisch: Esoterische Systeme mit festen Katalogen + Literatur-Pipeline haben wenig 1:1-Vorbilder in der Literatur. Der ontology-first-Ansatz ist der richtige Rahmen; Details (Cap, Werk-Reihenfolge, Alias-Listen) sind empirisch aus S5b/S5d/S6.

## Skript-Referenz

| Skript | Zweck |
|--------|--------|
| `ic_k2_state_audit.py` | **Abschluss-Gate** — Nodes/Interps/Synth/Jobs |
| `ic_relink_strict.py` | Generisches Re-Link nach Metadata-Wipe |
| `ic_restore_desc_from_wordings.py` | Synthese-Text aus wordings-Tabelle (ohne LLM) |
| `ic_k2_synth_batch.py` | Re-Synthese mit Cap/Priorität |
| `ic_hd_alias_remap.py` | HD Legacy-Slugs → Katalog |
| `ic_gk_wildwuchs_cleanup.py` | GK asset_chunk löschen |

→ Playbook: `k2_foundation_wave_playbook.md` · Scope: `k2_seed_scope_and_strict_text2kg.md`
