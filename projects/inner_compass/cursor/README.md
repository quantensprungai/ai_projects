# Inner Compass — Cursor Documentation Index

> **Projekt:** Geburtsbasiertes Meta-System — kulturell diverse Wissenssysteme über gemeinsamen Knowledge Graph vereint.
> **Status:** Pre-Launch (Pipeline funktioniert für HD, Schema-Migration auf sys_* steht an)
> **Stand:** 2026-02-16 (Index). **KARTE 2026-09-02:** Lesereihenfolge unten — Astro-Rad First Cut in `handover.md` + `reference/astro_natal_ingest_runbook.md`, nicht `status.md` zuerst.

## Was ist Inner Compass?

Eine App, die aus Geburtsdaten (Datum, Uhrzeit, Ort) das persönliche Profil aus mehreren Wissenssystemen gleichzeitig berechnet (Human Design, BaZi, westliche Astrologie, Maya Tzolkin u.a.) und dem User als einheitliche, navigierbare Landkarte präsentiert — organisiert entlang von 12 Lebensbereichen.

Das Alleinstellungsmerkmal ist die **Verbindungsschicht**: Ein Knowledge Graph, der Elemente über Systeme hinweg mappt (Schicht D: Cross-System-Mappings) und emergente Meta-Konzepte erzeugt (Schicht E: Meta-Knoten).

## KI-Lesereihenfolge (nicht die ganze reference/)

1. `handover.md` → 2. `contracts.md` **§1a + §1b** → 3. `reference/hd_state_contract.md` → 4. Overlay-Contract → 5. Layer-Checkliste (Delta 2026-08-17) → 6. `decisions.md` oben → 7. `pipeline.md` §12a bei neuem Element/PDF.

## Docs in diesem Ordner (Reihenfolge)

| Datei | Inhalt | Wann lesen |
|-------|--------|------------|
| **status.md** | Was existiert, was fehlt, nächste Schritte | Immer zuerst |
| **contracts.md** | Dimensions (15), Facetten-Vertrag §1a, Lebensbereiche (12), Payloads | Bei Schema/Pipeline/Overlay-Slots |
| **architecture.md** | 5 Datenschichten, sys_*-Schema (SQL), Tech Stack | Bei DB/Infra-Arbeit |
| **pipeline.md** | Jobs + **§1a Wörterbuch** (Chunk/Interp/Anhang/Synth/Relink) | Bei Worker/Pipeline; wenn die Wörter unklar sind |
| **engines.md** | Chart-Engines pro System, Integration, Was sie liefern | Bei Engine-Integration |
| **reference/synthesis_canon_first.md** | Canon-first Synth-Policy + Chat-Playbook (Verify, link_role, Sanierung) | Bei synthesize_node / Wording-Qualität / Relink |
| **reference/engine_integration_playbook.md** | Phase 1 wiederholbar: Katalog → Struktur → Tests → KG-Seed pro `system_id` | Bei neuem System / Engine-Integration |

**Doku-Regel:** cursor/ = max. 6–8 aktive Docs. Phasierung über **status.md** (S1–S7, …) und reference/ (Runbooks, Pläne), keine extra Dateien pro Phase.

## Verwandte Orte

- **Code-Repo:** `code/inner_compass_app/` (Makerkit 3.1.3 + Supabase)
- **Infra-Docs:** `infrastructure/spark/` (Worker, MinerU, LLM-Serving)
- **System-Deskriptoren:** `projects/inner_compass/system_descriptors/*.json`
- **Vollständiges PRD + Entscheidungen:** `projects/inner_compass/reference/`
- **Agents / MCP-Produkt / FLOP:** `projects/inner_compass/reference/agent_surface_and_monetization.md`

## Kernzahlen

- **15** Dimensionen (Backend-Schema, nullable)
- **12** Lebensbereiche (User-facing Navigation)
- **5** Datenschichten (A: Rohmechanik → E: Meta-Knoten)
- **4** Staffel-1-Systeme (HD, BaZi, Astro, Maya)
- **9** berechenbare Systeme total
- **4** Handbuch-Tiefenschichten (Spiegel → Muster → Prozess → Experiment)
