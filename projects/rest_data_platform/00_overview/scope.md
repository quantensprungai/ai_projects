<!-- Reality Block
last_update: 2026-01-17
status: draft
scope:
  summary: "Scope/Non‑Scope zur bewussten Begrenzung von AP 5.2 (ReST Data Platform)."
  in_scope:
    - standard modules
    - boundaries
  out_of_scope:
    - bespoke development for other WPs
notes: []
-->

# Scope / Non‑Scope (AP 5.2 – ReST Data Platform)

## Scope (was wir liefern)
- **Backbone**: Makerkit‑Portal als “ReST Portal” (Login, Rollen, Basis‑UI).
- **Datenorganisation**: standardisierte Ablage/Metadaten für projektbezogene Daten & Dokumente.
- **Standard-Upload**: CSV/XLSX/PDF Upload + minimale Validierung/Versionierung (so schlank wie möglich).
- **Analytics**: Dashboards/Exploration als separater Self‑Service‑Bereich (z. B. Superset) *oder* minimale “KPI Cards” im Portal – abhängig vom Projektentscheid.
- **Optionale KI‑Bausteine** (nur wenn Aufwand/Nutzen passt): dokumentenbasiertes Q&A (RAG) und einfache Zusammenfassungen.

## Non‑Scope (was wir explizit NICHT liefern)
- Keine **WP‑spezifischen Portale** oder individuellen Fach‑UIs.
- Keine **individuellen Dashboards** “auf Zuruf” für andere WPs.
- Keine **Sonder‑ETLs** pro WP (nur Standard‑Schnittstellen/Upload; Fachmapping liegt beim WP).
- Kein “Rollout” als verpflichtender Regional‑Standard, kein Betrieb als Produkt – sofern nicht später entschieden.

## Prinzip
**Self‑Service first**: Wir stellen Standardbausteine bereit; WPs nutzen sie eigenverantwortlich oder nicht.


