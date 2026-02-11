<!-- Reality Block
last_update: 2026-02-02
status: draft
scope:
  summary: "Technische Schritte – ReST WP 2.1: erster Schritt und folgende."
  in_scope:
    - first step
    - sequence of technical actions
  out_of_scope:
    - detailed implementation
notes: []
-->

# Technisch: Erster Schritt und Folgende

## Erster Schritt (vor Code)
**Datenzugang und Minimalmodell klären.**
- **Quellenmap** anlegen: welche Quellen sind realistisch? (BNetzA, BSH, EU-Register, Open Data, Studien)
- **Lizenz/Recht** prüfen: darf gespeichert/weitergegeben werden?
- **Minimales Datenmodell** definieren: welche Felder braucht das Asset-Register? (Standort, Betreiber, Baujahr, Typ, Lebensdauer, Quelle)
- **Non-Scope** nochmal festhalten (keine Simulation, kein Voll-DPP)

Ohne das steht später alles auf wackeligen Beinen.

---

## Schritt 2: Backbone aufsetzen
**Portal + Supabase, kein WP-spezifischer Inhalt.**
- **Supabase-Projekt** anlegen (Auth, Postgres, Storage, RLS)
- **Next.js-App** (oder Makerkit-Basis) mit Login/Rollen und einem einfachen Upload-Flow
- **Erste Tabelle(n)** für das Asset-Register (Schema aus Schritt 1)
- **Upload-Pfad** für CSV/XLSX/PDF (Speicherung + Metadaten)

Ziel: Eine Person kann sich anmelden, etwas hochladen und einen Eintrag sehen.

---

## Schritt 3: Asset-Register sichtbar machen
**Erste echte Nutzung.**
- **Asset-Liste/-View** im Portal (Filter, Suche optional)
- **1 Export** (CSV/Excel) aus dem Register
- **Rollen/RLS** minimal: wer darf lesen/schreiben?

Ziel: „Das ist der Ort, wo die Anlagen stehen.“

---

## Schritt 4: Daten befüllen
**Erste Quellen anbinden.**
- **1–2 reale Datenquellen** integrieren (z. B. manueller Import aus BNetzA/BSH-Export oder API, wenn verfügbar)
- **Quelle und Stand** pro Datensatz pflegen (Versionierung/Governance)
- **Qualitätscheck**: Pflichtfelder, Duplikate, Plausibilität

Ziel: Register enthält echte, nachvollziehbare Daten.

---

## Schritt 5: Dokumente + RAG light
**Dokumente nutzbar machen.**
- **PDF-Ingest** (Upload → Speicherung → Metadaten)
- **RAG-Pipeline** (Embeddings, z. B. über Spark-Worker oder externen Service) – nur wenn Ressourcen da
- **Q&A mit Quellen** (10 Standardfragen definieren und testen)

Ziel: Fragen zu Dokumenten beantworten, ohne jedes PDF zu öffnen.

---

## Schritt 6: Reporting und Zeitachsen
**Low-Complexity Outputs.**
- **Superset** (oder Alternative) read-only an Postgres anbinden
- **1–2 Standardreports**: z. B. Bestandsübersicht, einfache Rückbau-Zeitachse („wann wird was rückbaupflichtig?“)
- **Export** für Anträge/Partner (z. B. PortCycle)

Ziel: Zahlen und Zeitachsen kommen aus dem System, nicht aus Excel.

---

## Schritt 7 (optional): DPP-Light + Agenten
**Nur wenn Kern steht und Nutzen klar.**
- **DPP-Light**: 1 Beispielkomponente, QR, Lifecycle-Events, Verknüpfung mit Register
- **Leichte Agenten** (z. B. Extraktion, Datenqualität) – wenn Spark/AG2 verfügbar und priorisiert

---

## Kurz: Reihenfolge
1. Datenzugang + Minimalmodell  
2. Backbone (Supabase + Next.js + Upload)  
3. Asset-Register-UI + Export + RLS  
4. Daten befüllen (Quellen, Qualität)  
5. RAG light (Dokumente, Q&A)  
6. Reporting + Zeitachsen  
7. Optional: DPP-Light, Agenten  

Die Schritte 1–4 sollten in 6–8 Wochen ein sichtbares, nutzbares System liefern.
