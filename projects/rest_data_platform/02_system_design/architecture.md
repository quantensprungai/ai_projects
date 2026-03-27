<!-- Reality Block
last_update: 2026-03-27
status: draft
scope:
  summary: "High-Level Architektur – WP 5.2 ReST Data Platform (Next.js + Supabase); Pilot WP 2.1."
  in_scope:
    - components
    - deployment options
    - code repo boundary vs Inner Compass
  out_of_scope:
    - detailed schemas
notes:
  - "IMC-Domain-Schema liegt in reference/imc/IMC_Schema_v1.sql (public, eigenes Code-Repo geplant)."
-->

# Architektur (High Level)

## Zielbild (Stage A)
Mit minimalem Team eine **nutzbare Vertical-Slice-Plattform** in **WP 5.2** (ReST Data Platform) bauen — **Pilotfokus WP 2.1** (*Incubator for Maritime Circularity 2050* / Offshore):
- konsolidiertes Offshore-Asset-Register (Alpha Ventus als Pilot),
- reproduzierbare Datenpipelines (Import, Version, Source/Stand),
- erste API- und UI-Flaechen fuer nachgelagerte Module (Simulation, LCA, DPP-Light).

Die Plattform ist bewusst **Backbone zuerst**: robust, erweiterbar, aber ohne Produktversprechen fuer Stage B/C.

## Positionierung: Was ReST jetzt ist (und nicht ist)
ReST ist in Stage A:
- Integrations- und Datenbasis (Supabase + Next.js),
- gemeinsamer Einstiegspunkt fuer Module mit klaren Interfaces,
- Demonstrator fuer Entscheidungsunterstuetzung (Kosten/Zeit/CO2 auf Proxy-Niveau).

ReST ist in Stage A nicht:
- vollwertige Betriebsplattform fuer alle Stakeholder,
- Ersatz fuer AnyLogic/SimaPro,
- Industrie-Datenbeschaffer (OEM/NDA),
- "eierlegende Wollmilchsau" mit Echtzeit und Vollautomatisierung.

## Architekturprinzipien
1. **Infrastruktur ungleich Fachinhalt**  
   Plattform liefert Schema, Import, Verknuepfung, API, Rollen. Modul-Owner liefern fachliche Inhalte und Datenqualitaet.
2. **Data Ampel steuert Scope**  
   Gruen zuerst (Stage A), Gelb gezielt als Proxy, Rot nur mit Partner/NDA in Stage C.
3. **Interface Agreements vor Implementierung**  
   Keine Modulintegration ohne gemeinsames Feldset, Keys, Lieferformat und Beispieldaten.
4. **Vertical Slice vor Breite**  
   Erst Alpha Ventus + Emden + definierte Outputs, danach kontrollierte Erweiterung.

## Technische Basis (2-Layer-Modell)
### Layer 1: Rohdaten-Mirror
- Quelltreue Ablage (z. B. MaStR/BSH/4C Exporte)
- Keine semantische Umdeutung
- Zweck: Reproduzierbarkeit, Auditierbarkeit, Nachvollziehbarkeit

### Layer 2: Angereichertes Register
- kuratierte Entitaeten fuer Produkte/Services (Assets, Komponenten, Events, LCA/Sim-Outputs, Dokumentmetadaten)
- versionierte Anreicherung mit klarer Provenienz
- Grundlage fuer API, UI, Reports

## Andockmodi fuer Module
- **Modus A (im ReST-Stack):** Next.js + Supabase, gemeinsames Deployment (z. B. DPP-Light, BOM-UI).
- **Modus B (eigener Service + API):** Externes Tool liest/schreibt ueber API (z. B. AnyLogic, LCA).
- **Modus C (eigene Plattform):** ReST liefert Daten, keine Rueckschreibung zwingend (spaetere Produkte/Marktplatz).

## Kernbausteine (Stage A, realistisch mit kleinem Team)
- **Portal (Next.js):** Login/Rollen, Upload/Import, Asset-Register, Basis-Dashboard.
- **Supabase:** Postgres + PostGIS, Auth, Storage, RLS, Migrations.
- **Daten-Governance light:** Source/Stand, Pflichtfelder, Import-Checks, Qualitaetsreport.
- **OpenAPI/REST:** stabile Basisschnittstellen fuer Modul-Owner.
- **Analytics:** minimale KPI-Ansichten im Portal oder separater Self-Service-Read-Only-Zugang.

## Optionale Bausteine (nur bei klarem Nutzen)
- DPP/AAS-Vertiefung ueber DPP-Light hinaus
- RAG/Agent-Service (Spark/Worker)
- BPM/Orchestrierung (Camunda oder AG2) als Connector-Service
- Echtzeitnahe AIS-/Wetterintegration mit laufenden Betriebskosten

## Code-Repository (Abgrenzung)
- **Eigene App, eigenes Repo:** `quantensprungai/astra-imc-platform` (lizenzierte Next.js/Supabase-Turbo-Basis), **kein** Bestandteil von `code/hd_saas_app` (Inner Compass).
- **Gemeinsam** mit Inner Compass: nur **Muster** (Migrations, RLS, Client-Patterns) — keine gemeinsame Produkt-Datenbank.
- **Kanonisches SQL (Domain v1):** [`reference/imc/IMC_Schema_v1.sql`](../reference/imc/IMC_Schema_v1.sql) — alles in **`public`** für PostgREST/RLS wie in der Anwendungsbasis üblich. Nach den **Baseline-Migrationen** der Vorlage als **eigene Migration** einspielen; RLS/Policies setzen.

## Dokumentation: was wohin (kein Doppelpflege-Chaos)
| Ebene | Inhalt |
|--------|--------|
| `projects/rest_data_platform/` (Overview, Spec, Architektur, Roadmap, Comms) | **Projekt-SoT:** Ziele, Scope, Ablauf, Schnittstellenprozess, Stakeholder. Kurz und stabil. |
| `reference/imc/` | **IMC-/ASTRA-Arbeitsartefakte:** Mapping-Excel, Workshops, Vorgehensplan-Word, Samples-Hinweise, SQL-Entwurf. Fachliche Tiefe bleibt in den **Originaldateien**. |
| Synchronisation | Aenderungen zuerst in der **führenden Quelle** (xlsx/docx), dann bei Bedarf **eine Zeile** in Architektur oder `reference/imc/README.md` (Link/Version/Status). **Nicht** komplette Excel-Inhalte nach Markdown spiegeln. |

## Deployment (low ops)
- **App:** Next.js auf schlanker Hosting-Umgebung (z. B. Coolify/Hetzner).
- **Datenebene:** Supabase managed (Postgres/PostGIS/Auth/Storage).
- **Prinzip:** pro Projekt getrennte Supabase-Umgebung fuer Risiko- und Zugriffsgrenzen.
