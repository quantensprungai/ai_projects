# Inner Compass

> Geburtsbasiertes Meta-System — kulturell diverse Wissenssysteme über gemeinsamen Knowledge Graph vereint.

## Schnelleinstieg

| Frage | Datei |
|-------|-------|
| Was ist der aktuelle Stand? | `cursor/status.md` |
| Wie übergebe ich an neue KI-Session? | `cursor/handover.md` |
| Wie sieht das Schema aus? | `cursor/architecture.md` + `cursor/contracts.md` |
| Wie funktioniert die Pipeline? | `cursor/pipeline.md` |
| Welche Engines berechnen Charts? | `cursor/engines.md` |
| Was ist die Vision? | `reference/prd_v3.md` |
| Warum haben wir X so entschieden? | `reference/decisions.md` |
| Was sind offene Ideen? | `reference/ideas.md` |
| Welche Theorien stecken dahinter? | `reference/inspirations.md` |
| Story, UX, Zukunftsvision? | `reference/vision_and_story.md` |
| Layer-Schemas, Descriptor-Spec? | `reference/schema_and_descriptor_specs.md` |
| Phase 1 Engine-Integration pro System? | `reference/engine_integration_playbook.md` |
| Struktur vs. Deskriptor vs. Seed, Kit-first, Ebenen? | `reference/structure_descriptor_seed.md` |
| HD-Kit: Was steht in bodygraph-data/constants/hdkit? | `reference/hd_kit_structure_extraction.md` |
| S5 E2E-Runbook (PDF → MinerU → LLM)? | `reference/s5_runbook.md` |
| Reference nach Phasen gruppiert (Struktur/Pipeline/Produkt)? | `reference/README.md` |

## Verwandte Orte

- **Code:** `code/inner_compass_app/` (Makerkit 3.1.3)
- **Infrastruktur:** `infrastructure/spark/` (Worker, MinerU, LLM)
- **Globale Meta:** `projects/_meta/`

## Ordnerstruktur

```
projects/inner_compass/
├── cursor/                 ← Cursor liest primär hier (max. 6–8 aktive Docs, siehe Doku-Regel)
├── reference/              ← Kontext: PRD, Entscheidungen, Ideen, Runbooks, Struktur-Specs
├── system_descriptors/     ← JSON-Deskriptoren pro System (u. a. HD, BaZi, Ziwei, Astro, …)
├── system_structure/       ← Kataloge / Strukturbäume (z. B. ziwei_catalog_v0.json)
├── transfer/               ← Schema, Prompts (Import/Export-Specs)
├── 99_archive/             ← Alles aus hd_saas/ (nicht löschen, nicht referenzieren)
└── README.md               ← Diese Datei
```

## Doku-Regel & Phasierung (Workspace-Regel)

- **cursor/:** max. **6–8 aktive Docs**. Neue Dateien nur, wenn Inhalt in keine bestehende passt **und** aktiv referenziert wird. (Globale Rule: ai-projects-global.mdc.)
- **reference/:** für Kontext, Runbooks, tiefere Specs — hier dürfen mehr Dateien liegen; klare Benennung, kein Durchnummerieren.
- **Phasierung:** Projekt in **Phasen** gedanklich unterteilen (z. B. Struktur & Engines → Pipeline & Content → Cross-System → Handbuch), aber **keine neuen cursor-Dateien pro Phase**. Phasen stehen als Abschnitte/Checklisten in **cursor/status.md** (S1, S2, …) und ggf. in **reference/** (Runbooks, Pläne). So bleiben die Docs klar ohne Datei-Wildwuchs.

## Status

Pre-Launch. Engines: Ziwei (iztro), BaZi (@yhjs), Jyotish (PyJHora), HD (dturkuler — 13-Layer-Tiefe + Composite/Transit). Schema-Migration (`hd_*` → `sys_*`) steht an. Details: `cursor/status.md`.
