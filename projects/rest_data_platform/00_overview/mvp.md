<!-- Reality Block
last_update: 2026-01-17
status: draft
scope:
  summary: "MVP Definition – ReST Data Platform (schlank, wenig Ops, hoher Nutzen)."
  in_scope:
    - mvp modules
    - what success looks like
  out_of_scope:
    - detailed implementation
notes: []
-->

# MVP – ReST Data Platform (schlank)

## Ziel (6–8 Wochen, realistisch)
Ein funktionsfähiges „ReST Portal“ (Makerkit) + Supabase‑Backend, das **Daten/Dokumente sauber organisiert** und **standardisierte Sichtbarkeit** erzeugt – ohne Service‑Falle.

## MVP‑Module (4 Bausteine)

1) **Portal & Rollen (Makerkit)**
- Login, Rollen (Admin/Editor/Viewer) für AP 5.2 (intern)
- Keine WP‑spezifischen Bereiche

2) **Upload & Datenorganisation (Supabase)**
- Upload von **PDFs** und **Tabellen** (CSV/XLSX)
- Minimal: Metadaten (Titel, Quelle, Version, Verantwortliche, Datum)

3) **Transparente Outputs (ohne große Dashboard-Commitments)**
- Entweder:
  - a) sehr schlanke „KPI/Status Cards“ im Portal (Uploads, letzte Aktualisierung, Datensatzanzahl), oder
  - b) Superset separat (Self‑Service) – nur Templates, kein Custom‑Build

4) **Optionale KI‑Funktion (nur wenn wirklich gewollt)**
- Dokumenten‑Q&A (RAG) **für AP 5.2 Dokumente**
- Ergebnis: Quellenzitierung + einfache Zusammenfassungen

## Erfolgskriterien (einfach, messbar)
- Upload/Versionierung funktioniert reproduzierbar (keine “Dateichaos”-Ablage)
- Klare Rollen/Policies (niemand sieht, was er nicht sehen soll)
- Mindestens 1 “offizieller” Daten-/Dokumenten-Katalog (für Abstimmungen/Reporting)
- Optional: RAG beantwortet 10 typische Projektfragen zuverlässig mit Quellen


