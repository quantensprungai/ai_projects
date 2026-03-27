<!-- Reality Block
last_update: 2026-03-27
status: draft
scope:
  summary: "ReST Data Platform ASTRA WP 5.2 – Doku: Zielbild, Scope, Naming, Stack (Next.js + Supabase); Code: quantensprungai/astra-imc-platform."
  in_scope:
    - project overview
    - scope / non-scope
    - architecture notes (high level)
    - IPW mapping / email templates
  out_of_scope:
    - any personal contact data / private emails / phone numbers
notes: []
-->

# ReST Data Platform (ASTRA) – Doku Index

- `00_overview/naming_canon.md`: **Namen** (GitHub, App „ASTRA IMC“) + **WP 5.2 / WP 2.1**-Zuordnung
- `00_overview/mission.md`: Zweck & Nutzen (schlank)
- `00_overview/wp2_1_offshore_ce_summary.md`: WP 2.1 Kurzfassung (Offshore Circular Economy)
- `00_overview/scope.md`: Scope/Non‑Scope (Schutz vor Feature‑Creep)
- `00_overview/mvp.md`: MVP (schlank, realistisch)
- `00_overview/scope_shield.md`: Kurztext für Meetings/Mails (Abgrenzung)
- `00_overview/options_landscape.md`: Optionen-Landkarte (Richtungen + Vergleich + Shortlist fürs Brainstorming)
- `00_overview/gesamtantrag_astra.md`: Referenz aus dem Gesamtantrag (Kontext)
- `00_overview/vorantrag_rest.md`: Vorantrag / historische Projektbasis
- `00_overview/project_crosslog.md`: Querverweise zu angrenzenden Projektideen
- `00_overview/project_digital_manufacturing_logistics_intelligence.md`: Referenzprojekt fuer Kontext/Abgrenzung
- `02_system_design/architecture.md`: High‑Level Architektur (Next.js + Supabase + optionale Services)
- `01_spec/ipw_email_templates.md`: sehr schlanke IPW‑Formulierungen + Mail‑Vorlagen
- `01_spec/idea_backlog.md`: offener Ideen-Backlog (Hypothesen/Experimente, noch nicht festgelegt)
- `01_spec/interface_agreement_template.md`: Template fuer Modul-Schnittstellen (Schema, Keys, Format, Abnahme)
- `01_spec/data_ampel_stage_a.md`: Stage-A Datenboard (Gruen/Gelb/Rot) fuer Meeting-Entscheidungen
- `01_spec/imc_rls_policy_patterns.md`: IMC RLS/Grant-Muster (Team-Accounts / `has_role_on_account`)
- `03_roadmap/phase_a_timeline_2026_2028.md`: Phase A Roadmap (bis 31.08.2028) + Übergabepunkt
- `03_roadmap/technical_next_steps.md`: Technisch: erster Schritt und folgende (Reihenfolge)
- `03_roadmap/imc_data_implementation_leitfaden.md`: IMC Word-Vorgehensplan einordnen + 4C-Sourcing-Strategie + Schema-Drift-Hinweise
- `03_roadmap/imc_app_bootstrap.md`: Start bei Null — Repo klonen, lokales Supabase, IMC-Schema + RLS einbinden
- `04_communication/stakeholders_and_comms.md`: Stakeholder + Kommunikationslogik
- `04_communication/status_update_template.md`: 1‑seitiges Status Update Template
- `04_communication/meeting_playbook_data_requirements.md`: Moderationsleitfaden fuer Daten-/Anforderungsmeeting
- `99_archive/keep2_sanitized_notes.md`: sanitisierte Langnotizen (ohne Kontaktdaten)
- `reference/imc/README.md`: IMC/ASTRA-Artefakte (Schema, Mapping, Ablage)
- `reference/imc/IMC_Schema_v1.sql`: Domain-Schema v1 (**public**), für `astra-imc-platform`
- `reference/imc/validation_handoff_one_pagers.md`: Validierungs-Checklisten (Thomas, Marc, Shubham) als Repo-Spiegel

**Code:** `git@github.com:quantensprungai/astra-imc-platform.git` — optionaler Klon im Meta-Repo: [`code/astra-imc-platform/`](../../code/astra-imc-platform/) (README dort). **Nicht** unter `code/hd_saas_app` (Inner Compass). Querverweis Doku ↔ Code: [`00_overview/naming_canon.md`](00_overview/naming_canon.md).


