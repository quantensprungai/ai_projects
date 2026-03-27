<!-- Reality Block
last_update: 2026-03-28
status: draft
scope:
  summary: "Festlegung Namen & Marken (GitHub, App, Kurzformen) plus ASTRA-WP-Zuordnung; optionaler lokaler Klon unter code/."
  in_scope:
    - product naming
    - repository naming
    - ASTRA work package alignment
  out_of_scope:
    - rechtliche Markenprüfung
    - finale CI/CD-Hostnamen
notes:
  - "Quelle WP-Struktur: 00_overview/gesamtantrag_astra.md (Antragstext)."
-->

# Naming-Kanon & ASTRA-Einordnung

## ASTRA: Arbeitspakete (offiziell)

| WP | Bedeutung (Kurz) | Bezug zu dieser Doku |
|----|------------------|----------------------|
| **WP 5.2** | **ReST Data Platform** — zentrale Daten-/Analyseplattform im Antrag („Driving Regional Innovation Through Advanced Digital Technology“) | **Diese Plattform** (Next.js/Supabase-App, IMC-Schema) wird **in WP 5.2** umgesetzt. |
| **WP 2.1** | **Incubator for Maritime Circularity 2050** — maritime Kreislaufwirtschaft, u. a. Offshore-Wind, LCA, DPP-Kontext | **Fachlicher Pilot-Fokus** und Use-Case für Stage A (Offshore-Asset-Register, IMC-Datenmodell). |

**Kurzform für Folien:** *WP 5.2 liefert die Plattform; WP 2.1 liefert den maritimen Offshore-/Kreislauf-Kontext.*

**Hinweis „AP 5.2“:** In älteren internen Texten wurde dieselbe Einheit mitunter **AP 5.2** bezeichnet. Im Antrag heißt die Einheit **WP 5.2**. Neue Texte verwenden **WP 5.2**; in historischen Mails/PDFs kann „AP 5.2“ weiter vorkommen.

**IMC** (*Integrated Maritime Circularity*): Fachbezeichnung für den **Offshore-Wind / EoL / Kreislauf**-Zweig; **kein** Ersatz für die offiziellen WP-Nummern.

---

## Produkt- und Langtitel

| Kontext | Formulierung |
|---------|----------------|
| **Lang (EN, Antrag/Folien)** | Integrated Maritime Circularity — End-of-Life Planning Platform for Offshore Wind Assets |
| **Lang (DE)** | Integrated Maritime Circularity — Planungsplattform für Offshore-Windanlagen (End-of-Life / Rückbau) |
| **Kurz (UI / Tab)** | **ASTRA IMC** |
| **Untertitel UI (DE)** | End-of-Life & Kreislaufwirtschaft · Offshore-Wind |
| **Technischer Projektname** | ReST Data Platform (bleibt der **Antrags-/Dokuname** für WP 5.2) |

---

## GitHub & Code

| Artefakt | Festlegung |
|----------|------------|
| **Repository** | `quantensprungai/astra-imc-platform` |
| **SSH-Klon** | `git@github.com:quantensprungai/astra-imc-platform.git` |
| **HTTPS** | `https://github.com/quantensprungai/astra-imc-platform` |
| **Monorepo-Paket / Ordner** | wie von der geklonten Turbo-Vorlage vorgegeben (`apps/web` o. ä.); interner Codename optional `imc` |

**Doku-Ordner vs. Code-Repo:** Die Projekt-Doku liegt absichtlich unter **`projects/rest_data_platform/`** (Antragsname *ReST Data Platform*). Das **GitHub-Repo** heißt **`astra-imc-platform`**. Für die KI reicht der Verweis auf diese Datei — ein Umbenennen des gesamten Doku-Zweigs wäre viel Pflegeaufwand und **nicht nötig**.

Im Code-Repo: „Docs live here“ → `../../projects/rest_data_platform/` (je nach Workspace) bzw. Link auf das `ai-projects`-Repo.

**Lokaler Klon (optional):** `ai-projects/code/astra-imc-platform/` — gleiche Remote-URL; erster Commit nach Befüllen mit der Vorlage.

---

## Was wo verwenden

- **Öffentlich / fachlich:** WP 5.2 + WP 2.1 + bei Bedarf Langtitel IMC (EN/DE).
- **Login-Seite / Browser-Tab:** „ASTRA IMC“ + kurzer Untertitel.
- **README / technische Doku:** „ReST Data Platform“ + Verweis auf dieses Dokument.
- **Datenbank / APIs:** IMC-Domain-Objekte in `public` mit Präfix **`imc_`** (z. B. `imc_wind_farms`, Views `imc_v_*`, ENUMs `imc_*`); Organisationen kurz **`imc_orgs`**. Makerkit-Tabellen (`accounts`, …) bleiben ohne dieses Präfix.

## Verweise

- ASTRA-Gesamtrahmen: [`gesamtantrag_astra.md`](gesamtantrag_astra.md)
- Scope-Schutz: [`scope_shield.md`](scope_shield.md)
- WP 2.1-Kurzfassung: [`wp2_1_offshore_ce_summary.md`](wp2_1_offshore_ce_summary.md)
