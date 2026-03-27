<!-- Reality Block
last_update: 2026-03-26
status: draft
scope:
  summary: "Markdown-Spiegel der 1-seitigen Validierungspakete (Thomas, Marc, Shubham) für Repo-Suche und Versionierung."
  in_scope:
    - checklist content
    - owner actions
  out_of_scope:
    - legal commitments
notes:
  - "Word-Originale bleiben führend, wenn sie abweichen."
-->

# Validierung – One-Pager (Repo-Spiegel)

Ziel: Jede Person weiß, **was schon da ist**, **was sie bestätigen soll**, **bis wann**, **in welchem Format**.

---

## Thomas – LCA & BOM

**Kontext (von Heiko vorab geladen / geplant):**

- BOM-Light aus `IMC_LCA_DPP_Data_Extraction_v1.xlsx` (z. B. V150; Alpha Ventus / REpower 5M als Proxy mit `is_proxy = true`).
- LCA-Impact-Kategorien als Lookup + Ergebniszeilen (Onshore-Proxy bis Offshore-Korrektur).
- EoL-Rates / Circularity / MCI wo vorhanden.

**Bitte bestätigen oder korrigieren (Checkliste):**

- [ ] Massen und Subsystem-Schnitt für **REpower 5M / Alpha Ventus** plausibel (oder Korrekturfaktoren nennen).
- [ ] **Offshore vs. Onshore** für GWP und relevante Kategorien: Faktor oder neu berechnen?
- [ ] **SimaPro vs. openLCA**, **ecoinvent-Version**, Methodik (CML / ReCiPe / …) festlegen.
- [ ] Reicht **BOM-Granularität** (~20 Zeilen Proxy) für eure Aussagen – oder Pflicht zu mehr Auflösung?
- [ ] MCI / Recyclability: Quelle und Aktualität ok für Publikation?

**Output von Thomas:** Kurzes schriftliches OK oder Liste Änderungsfelder + Priorität.  
**Aufwand:** ca. 30–90 Minuten nachdem CSV/Export vorliegt.

---

## Marc – Zerlegungssequenz & AnyLogic

**Kontext:**

- Literatur-/Matrix-basierte **Decom-Sequenz** ist Startwert; **Alpha Ventus = Tripod**, nicht Monopile-Standardsequenz – explizit gegenprüfen.
- VPI/Vessel-Felder aus 4C als Input für Constraints (Welle, Wind, Kran, Geschwindigkeit).

**Bitte bestätigen oder korrigieren:**

- [ ] Reihenfolge der Hauptschritte für **Tripod / Alpha Ventus** korrekt?
- [ ] **Parallele Pfade** (z. B. Kabel vs. Turm) markiert – nicht nur lineare Liste?
- [ ] **Vessel-Typ pro kritischem Schritt** oder Constraint-Logik plausibel?
- [ ] Fehlende Schritte (HSE, Vorarbeiten, Seeverlegung, Hafenlimits)?
- [ ] **Export aus AnyLogic** für DB: vorgeschlagenes CSV-Spaltenformat (Szenario, Dauer, Kosten, CO₂, Schiffe) akzeptiert?

**Output von Marc:** Annotierte Sequenz (eine Session) + ggf. Graph-Struktur; später Sim-CSV-Schema.  
**Aufwand:** ca. 2 h Session + Nacharbeit.

---

## Shubham – DPP / AAS

**Kontext:**

- Mapping-Excel: 4C → AAS-Submodelle; DB-Felder und Prioritäten (MUST/SHOULD/NICE).
- Geplant: Templates / Export-Pipeline (AASX, API).

**Bitte bestätigen oder ergänzen:**

- [ ] **IDTA / semanticId** pro Submodell (URNs) – welche Template-Version?
- [ ] Felder nach **ESPR-Analogie** oder interner Policy: essential / recommended / voluntary final zuordnen.
- [ ] **AASX-Package-Struktur:** pro Park, pro Turbine, pro Version?
- [ ] **Spez-Version** (AAS metamodel) und Toolchain (Validator).
- [ ] Referenz-AASX oder Beispiel aus Thesis (NDA beachten).

**Output von Shubham:** Finalisierte Submodell-Liste + IDs + Export-Regeln.  
**Aufwand:** ca. 1–1,5 h Session + Nachziehen IDs.

---

## Heiko – was du vorlegen solltest, bevor die Reviews starten

- Export oder Screenshot der **tatsächlich geladenen** Zeilen (Stichprobe) + `source_id`.
- **Ein** gemeinsames Beispielobjekt (z. B. Alpha Ventus) end-to-end: Standort, Modell, 4C-IDs.
- Klare Frage pro Person (oben als Checkboxen) – keine offenen „was meinst du?“-Mails.
