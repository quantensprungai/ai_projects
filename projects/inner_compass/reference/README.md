# Inner Compass — Reference-Index

> Kontext-Docs, Runbooks, Pläne. Gruppiert nach **Phasen**, damit neue Docs sich zuordnen lassen ohne Datei-Chaos. Dateien werden **nicht** in Phasen-Ordner verschoben; dieser Index ist die Struktur.

## Phasen (thematisch)


| Phase                  | Thema                                                          | Docs in reference/                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Struktur & Engines** | System-Struktur, Deskriptoren, Seed, Kits parsen, Ebenen       | **engine_integration_playbook.md** (Phase 1 pro System: Katalog, Struktur, Validierung), structure_descriptor_seed.md, **hd_kit_structure_extraction.md** (HD-Kit Auswertung), **hd_structure_13_layers_and_engines.md** (13 Ebenen, Strukturbaum vs. KG, Engines, Lizenz), **hd_ebenen_recherche_und_strukturbaum_vollstaendigkeit.md** (Ebenen-Recherche, Vollständigkeit, Gene Keys separat), schema_and_descriptor_specs.md, deep_structure_plan.md, deep_structure_seed_*.plan.md |
| **Pipeline & Content** | E2E-Pipeline, MinerU, LLM, Runbooks, K3-Kanon, Ontologie-Split | s5_runbook.md, **unlimited_ocr_spike_runbook.md**, **literature_canon_by_scope.md**, **ontology_policy.md**                                                                                                                                                                                                                                                                                                                                                                            |
| **Produkt & Vision**   | PRD, Entscheidungen, Ideen, Inspirationen                      | prd_v3.md, decisions.md, ideas.md, inspirations.md, vision_and_story.md                                                                                                                                                                                                                                                                                                                                                                                                                |


**Neue Docs:** Beim Anlegen in reference/ hier in die passende Phase eintragen (oder neue Phase Zeile ergänzen). Kein Durchnummerieren von Dateinamen nötig.

## Schnellzugriff (nach Thema)

- **Phase 1 Engine-Integration (alle Systeme gleicher Ablauf):** engine_integration_playbook.md  
- **Struktur/Deskriptor/Seed, Kit-first, Ebenen:** structure_descriptor_seed.md  
- **HD 13 Ebenen, Strukturbaum vs. KG, Engines, Lizenz:** hd_structure_13_layers_and_engines.md  
- **HD Ebenen-Recherche, Vollständigkeit Strukturbaum, Gene Keys pro Schule:** hd_ebenen_recherche_und_strukturbaum_vollstaendigkeit.md  
- **S5 E2E (PDF → MinerU → LLM):** s5_runbook.md
- **Nächstes Element / Facetten-Lesen:** `../cursor/pipeline.md` §12a + `../cursor/contracts.md` §1a/§1b  
- **HD State-Vertrag (defined/undefined, Träger, Display-Policy):** hd_state_contract.md  
- **Layer-Ist + Delta 2026-08-17:** hd_layer_master_checklist_2026-08-11.md
- **Unlimited-OCR Spike (Spark, Vergleich gegen MinerU):** unlimited_ocr_spike_runbook.md  
- **K3-Kanon / Ur-Systeme / Scope:** literature_canon_by_scope.md  
- **Split vs. Tags (Entscheidungs-Matrix):** ontology_policy.md  
- **Layer-Schemas, Descriptor-Spec:** schema_and_descriptor_specs.md  
- **Warum-Entscheidungen:** decisions.md  
- **Vollständiges PRD:** prd_v3.md

Haupt-Schnelleinstieg fürs Projekt: `../README.md` und `../cursor/status.md`.