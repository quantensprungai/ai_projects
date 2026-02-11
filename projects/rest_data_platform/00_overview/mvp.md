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
Ein funktionsfaehiges „ReST Portal“ + Supabase‑Backend, das **Offshore‑Daten und Dokumente** sauber organisiert und **standardisierte Sichtbarkeit** erzeugt – ohne Service‑Falle.

## MVP‑Module (4 Bausteine)

1) **Portal & Rollen**
- Login, Rollen (Admin/Editor/Viewer) für AP 5.2 (intern)
- Fokus: WP 2.1 Offshore‑CE, keine WP‑Sonderportale

2) **Offshore‑Asset‑Register + Upload**
- Upload von **PDFs** und **Tabellen** (CSV/XLSX)
- Minimal: Metadaten (Titel, Quelle, Version, Verantwortliche, Datum)
- Strukturierte Asset‑Basis (Standort, Typ, Leistung, Lebenszyklus)

3) **Transparente Outputs (ohne große Dashboard-Commitments)**
- Entweder:
  - a) sehr schlanke „KPI/Status Cards“ im Portal (Uploads, letzte Aktualisierung, Datensatzanzahl), oder
  - b) Superset separat (Self‑Service) – nur Templates, kein Custom‑Build
- Erste Rueckbau‑Zeitachsen (low‑complexity)

4) **Optionale KI‑Funktion (nur wenn wirklich gewollt)**
- Dokumenten‑Q&A (RAG) **für Offshore‑Docs**
- Ergebnis: Quellenzitierung + einfache Zusammenfassungen
- Optional: DPP‑Light Demonstrator (1 Beispielkomponente)

## Erfolgskriterien (einfach, messbar)
- Upload/Versionierung funktioniert reproduzierbar (keine “Dateichaos”-Ablage)
- Klare Rollen/Policies (niemand sieht, was er nicht sehen soll)
- Offshore‑Asset‑Register mit belastbaren Grunddaten steht
- Optional: RAG beantwortet 10 typische Fragen zuverlässig mit Quellen


