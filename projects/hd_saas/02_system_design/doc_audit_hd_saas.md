# HD-SaaS Doku-Audit – Inhalt, Referenzen, Einstiegspunkte

<!--
last_update: 2026-02-10
status: audit
scope:
  summary: "Prüfung aller MD-Dateien: Inhalt stimmt, Referenzen korrekt, Einstiegspunkte passen."
-->

Ergebnis einer systematischen Prüfung der 58 MD-Dateien in `projects/hd_saas/`.

---

## 1) Einstiegspunkte

### README.md – zu knapp

**Aktuell:** Nur grobe Ordner-Struktur (00_overview, 01_spec, …), current_status genannt.

**Fehlt:** Keine Verweise auf die wichtigsten Docs für neue Chats/Implementierung:
- `next_steps_was_fehlt_noch.md` (Priorität, Reihenfolge)
- `plan_option_b_roadmap.md` (Option B Roadmap)
- `chat_handover_hd_saas.md` (Copy-Paste für Chat-Wechsel)
- `02_system_design/` – welche Dateien sind zentral? (interpretations_contract, text2kg_spec, dimensions_contract, layer_implementation_abgleich)
- Worker-Contracts, system_descriptor_spec

**Empfehlung:** README um einen Abschnitt „Einstieg für KI/neue Chats“ ergänzen mit Links zu next_steps, plan_option_b, chat_handover, current_status.

---

### Gut vernetzt

- **next_steps_was_fehlt_noch.md** – verlinkt auf nahezu alle relevanten Specs (text2kg, interpretations, dimensions, layer_abgleich, process_batch, Vision/Story/UI-Docs).
- **plan_option_b_roadmap.md** – verlinkt auf next_steps, erkenntnisse, text2kg, interpretations.
- **chat_handover_hd_saas.md** – enthält die wichtigsten Links für Chat-Wechsel.
- **current_status_local_dev.md** – verweist auf interpretations_contract, worker_contract_extract_interpretations, text2kg_spec, export_supabase.

---

## 2) Inhaltliche Inkonsistenzen

### interface_and_vision.md – veraltete Reihenfolge

**Zeile 29:** „Zuerst **Insight-Engine-UI** … umsetzen“

**Problem:** Das entspricht **Option A**. Aktuell gilt **Option B** (next_steps, plan_option_b): Edges → Dynamics → Interactions → danach Insight Engine.

**Empfehlung:** Anpassen, z. B.: „Die **Reihenfolge** (Option B) steht in next_steps_was_fehlt_noch.md: zuerst Edges, Dynamics, Interactions; danach Insight-Engine-UI.“

---

### ui_ux_principles_and_flow.md

**Zeile 67:** „Insight-Engine-UI (next_steps) = erster Schritt zu …“

**Problem:** Bei Option B ist Insight Engine nicht der erste Schritt, sondern kommt nach dem Backend.

**Empfehlung:** Klarstellen: „Erster sichtbarer Schritt (nach Backend-Phase) = Insight-Engine-UI (next_steps).“

---

## 3) Referenzen – geprüft

| Referenz | Von | Zu | Pfad korrekt? |
|----------|-----|-----|---------------|
| next_steps_was_fehlt_noch.md | platform_and_story_master, interface_and_vision, ui_ux, vision_2026, app_picture | 02_system_design/next_steps_was_fehlt_noch.md | ⚠️ Teilweise ohne Pfad (funktioniert mit Suche) |
| interpretations_contract.md | dimensions, text2kg, erkenntnisse, layer_abgleich, current_status | 02_system_design/interpretations_contract.md | ⚠️ current_status: fehlender Pfad |
| text2kg_spec.md | next_steps, plan_option_b, dimensions, erkenntnisse, process_batch | 02_system_design/text2kg_spec.md | OK |
| dimensions_contract.md | interpretations, text2kg, erkenntnisse | 02_system_design/dimensions_contract.md | OK |
| erkenntnisse_und_fuer_spaeter.md | next_steps, plan_option_b | 02_system_design/erkenntnisse_und_fuer_spaeter.md | OK |
| layer_implementation_abgleich.md | next_steps, erkenntnisse, text2kg | 02_system_design/layer_implementation_abgleich.md | OK |
| worker_contract_* | layer_abgleich, text2kg, current_status | 02_system_design/worker_contract_*.md | OK |

**current_status Zeile 71:** „Doku: interpretations_contract.md“ – Pfad fehlt. Besser: `02_system_design/interpretations_contract.md`.

---

## 4) Wenig referenzierte Dateien (potenzielle Waisen)

Diese Dateien werden selten oder gar nicht verlinkt:

| Datei | Verweise von | Einschätzung |
|-------|--------------|--------------|
| architecture.md | (keine gefunden) | README nennt „Architektur“; evtl. von architecture.md aus referenzieren |
| data_flows.md | (keine gefunden) | Ergänzung zu architecture; README |
| agents.md | (keine gefunden) | Vision/Agent-Thema; in next_steps/vision erwähnt |
| tools_integrations.md | (keine gefunden) | Infrastruktur |
| prompts_and_personas.md | (keine gefunden) | Prompts |
| makerkit_bootstrap_and_orientation.md | README | OK |
| vision_and_scope_frame.md | interface_and_vision, app_picture, user_journeys | OK |
| market_context.md | (keine gefunden) | Overview |
| value_proposition.md | (keine gefunden) | Overview |
| problem_statement.md | (keine gefunden) | Overview |
| requirements.md | (keine gefunden) | Spec |
| functional_spec.md | (keine gefunden) | Spec |
| prd.md | (keine gefunden) | Spec |
| edge_cases.md | (keine gefunden) | Spec |
| parking_lot_backlog.md | (keine gefunden) | Backlog |
| hd_ingestion_slice_spec.md | (keine gefunden) | Roadmap |
| milestones.md | interface_and_vision | OK |
| mvp.md | app_picture, interface_and_vision, user_journeys | OK |
| v1_v2_v3.md | (keine gefunden) | Roadmap |
| risks_assumptions.md | (keine gefunden) | Roadmap |
| 04_assets/* (prompts, diagrams, datasets, branding) | (keine gefunden) | README nennt Ordner |
| 99_archive/* | (keine gefunden) | Archiv, bewusst isoliert |

**Empfehlung:** README oder next_steps um einen Abschnitt „Weitere Docs“ ergänzen, der architecture, data_flows, requirements, mvp, milestones etc. erwähnt. So finden KI und Menschen auch wenig referenzierte Dateien.

---

## 5) Zusammenfassung – To-dos

| Priorität | Was | Aktion |
|-----------|-----|--------|
| 1 | README | Abschnitt „Einstieg für KI/neue Chats“ mit next_steps, plan_option_b, chat_handover, current_status |
| 2 | interface_and_vision | Option B als autoritative Reihenfolge nennen, Verweis auf next_steps |
| 3 | ui_ux_principles_and_flow | Klarstellen: Insight Engine kommt nach Backend (Option B) |
| 4 | current_status | Pfad zu interpretations_contract ergänzen: `02_system_design/interpretations_contract.md` |
| 5 | README | Optional: „Weitere Docs“ (architecture, requirements, mvp, …) |

---

## 6) Referenz-Graph (Kern)

```
README → current_status
README → (fehlt: next_steps, plan_option_b, chat_handover)

next_steps ← plan_option_b, chat_handover, interface_and_vision, app_picture, ui_ux, vision_2026, platform_and_story_master
next_steps → text2kg_spec, interpretations_contract, dimensions_contract, layer_implementation_abgleich,
             erkenntnisse_und_fuer_spaeter, process_batch, language_and_pipeline_overview,
             vision_2026_2027, story_and_mythology, ui_ux_principles_and_flow, app_picture_and_user_journey,
             platform_and_story_master, interface_and_vision

interpretations_contract ← dimensions_contract, text2kg_spec, erkenntnisse, layer_abgleich, current_status
text2kg_spec ← next_steps, plan_option_b, dimensions, erkenntnisse, layer_abgleich, process_batch
dimensions_contract ← interpretations_contract, text2kg_spec, erkenntnisse
```

---

## Referenzen

- **Template für Audits:** projects/_meta/chat_handover_template.md (Prinzip: Index + aktuelle Lage + Links)
- **Autoritative Reihenfolge:** next_steps_was_fehlt_noch.md, plan_option_b_roadmap.md
