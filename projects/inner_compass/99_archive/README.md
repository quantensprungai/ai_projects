# 99_archive — Archivierte Dokumentation

Dieser Ordner enthält Verweise auf archivierte Inhalte. Nicht als Source of Truth verwenden.

## Alte hd_saas-Dokumentation

Die vollständige alte Dokumentation liegt noch unter `projects/hd_saas/` (archiviert, README dort verweist auf Inner Compass).

**Was wurde übernommen:**

| Quelle (hd_saas) | Ziel (inner_compass) |
|-------------------|----------------------|
| 5× Vision/Story/UX Docs | `reference/vision_and_story.md` |
| 3× Layer-Schemas + Descriptor-Spec | `reference/schema_and_descriptor_specs.md` |
| Contracts (dimensions, interpretations) | `cursor/contracts.md` (erweitert: 15 Dims, process-Feld) |
| Pipeline + Worker-Contracts | `cursor/pipeline.md` (konsolidiert + batch ops) |
| Architektur + Guardrails | `cursor/architecture.md` (erweitert) |
| PRD + User Journeys | `reference/prd_v3.md` |
| Erkenntnisse + Meta-Analyse | `reference/decisions.md` + `reference/ideas.md` |

**Was NICHT übernommen wurde (bewusst):**
- Leere Skeleton-Dateien (17 Stück, gelöscht)
- Historische MVP/Milestone-Docs (überholt durch status.md)
- Redundante Contracts/Architektur-Docs (IC-Versionen sind aktueller)
- Code-nahe Implementierungs-Sketches (text2kg_implementation_sketch, text2kg_test_procedure → bleiben in hd_saas als Referenz)
