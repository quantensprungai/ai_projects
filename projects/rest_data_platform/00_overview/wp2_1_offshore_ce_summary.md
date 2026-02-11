<!-- Reality Block
last_update: 2026-02-02
status: draft
scope:
  summary: "Kurzfassung WP 2.1 Offshore Circular Economy – ReST Data Platform."
  in_scope:
    - problem framing
    - goals
    - non-scope
    - core modules
  out_of_scope:
    - detailed implementation
notes: []
-->

# WP 2.1 Offshore Circular Economy – Kurzfassung

## 1) Ausgangslage
Vor Ostfriesland steht eine der groessten Offshore‑Infrastruktur‑Konzentrationen Deutschlands (WEA, Konverter, Fundamente, Kabel, Logistik). Es fehlt eine konsolidierte Sicht auf Standorte, Alter, Komponenten, Rueckbaupflichten und Materialstroeme. Gleichzeitig kommen Ausbau und Rueckbau parallel – ein strategisch kritischer “Gegenverkehr”.

## 2) Ziel
Aufbau eines modularen, KI‑gestuetzten Informationssystems, das Offshore‑Infrastruktur sichtbar macht, Lebenszyklus/Rueckbau ableitet, Materialien/Komponenten zugreifbar macht und Dokumente per RAG erschliesst. ReST ist **keine** Modellierungsplattform, sondern Wissens‑ und Datenerschliessung.

## 3) Non‑Scope (klarer Rahmen)
- Keine Rueckbausimulationen
- Keine Hafenlogistikmodelle
- Kein vollwertiger Digitaler Produktpass
- Keine komplexen technischen Offshore‑Modelle
- Keine operativen CE‑Prozesse
- Keine Echtzeitdaten/SCADA/Sensorik

## 4) Kernmodule
1) **Offshore‑Asset‑Register** (Standorte, Lebenszyklen, Grunddaten, Quellen)  
2) **Dokumenten‑Erschliessung (RAG light)**  
3) **Leichte Agenten** (Extraktion/BOM‑light, Datenqualitaet, Harmonisierung)  
4) **DPP‑Light Demonstrator** (1 Beispielkomponente + QR + Credential + Event‑Kette)  
5) **Low‑Complexity Analysen** (Zeitachsen, Mengen, Cluster)  

## 5) Nutzen (kurz)
- Datengrundlage fuer Rueckbau/CE‑Planung  
- Anschlussfaehigkeit an Folgevorhaben (z. B. “PortCycle”)  
- Reduktion manueller Recherche durch RAG/Agenten  

## 6) Technischer Umfang (1 FTE realistisch)
Upload/Integration, Asset‑Register, RAG, Agenten, optionale Mini‑Dashboards (Superset), DPP‑Light, einfache Zeitachsen, Exportfunktionen.

## 7) KI vs. Modellierung (ehrlich, praxisnah)
**Primär ist es ein Modellierungs‑ und Datenintegrationsproblem.**  
Lebenszyklen, Rueckbauzeitpunkte, Mengen und Cluster sind klassisch modellierbar.

**KI ist der Beschleuniger**, nicht der Kern:
- Dokumente lesen (PDFs/Reports)
- Materiallisten extrahieren (BOM light)
- Luecken finden und klassifizieren
- Zusammenfassungen und Auto‑Drafts

**Agenten sind nicht zwingend, aber sinnvoll** (v. a. mit 1 FTE):  
Sie ersetzen manuelle Datenarbeit, nicht das Modell.

## 8) DPP‑Light: was realistisch ist
Kein vollwertiger Digitaler Produktpass.  
ReST liefert einen **DPP‑Light‑Demonstrator**:
- Produktseite + QR
- Materialliste (BOM light)
- Lifecycle‑Events (Herstellung → Betrieb → Rueckbau)
- Verknuepfung mit Asset‑Register & Dokumenten

## 9) Detaillierte Stack‑Skizze (textlich)
### Kern (jetzt, 1 FTE realistisch)
1) **Portal-Schicht (Next.js Web-App)**
   - Login/Rollen, Upload-Wizard, Asset-Register UI, Dokumentenbereich
2) **App-Layer (API/Business-Logik)**
   - API Routes/Server Actions, Validierung, Mapping-Logik, Zugriffskontrolle
3) **Supabase-Layer (Managed Backend)**
   - Postgres, Storage, Auth, RLS, Migrationen/Versionierung
4) **Analytics (Superset, separat)**
   - Read-only Zugriff auf Postgres, 1-2 Standardreports

### Optional (spaeter, wenn Nutzen klar)
5) **AI Processing (Spark Worker)**
   - RAG/Embeddings, Extraktion aus PDFs, Batch-Anreicherung
6) **Agentic Layer (AG2, intern)**
   - CE-Agent (BOM light), Datenqualitaet, Auto-Drafts
7) **MCP-Interface**
   - Standardisierte Tool-Aufrufe fuer externe KI-Tools
8) **DPP-Light**
   - Beispielkomponente, QR, Lifecycle-Events, Verknuepfung mit Asset-Register
