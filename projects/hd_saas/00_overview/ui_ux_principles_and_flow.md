# UI/UX-Prinzipien und Flow – Human-first, Muster statt Systeme

<!-- last_update: 2026-02-10 -->

Wie das Interface aussehen und sich anfühlen soll: **Muster in Menschensprache**, keine Expertensprache im Default; optional „Mechanik anzeigen“ für Profis. Abgestimmt auf vision_2026_2027 und story_and_mythology.

---

## 1) Grundprinzip: Human-first, nicht System-first

**User sagt nicht:**  
„Bitte analysiere Mars über Gate 21 und kombiniere mit meinem BaZi Luck Pillar.“

**User sagt:**  
„Warum fühle ich mich heute so gedrückt?“ / „Warum wiederholt sich das immer?“ / „Was steht bei mir gerade an?“ / „Was soll ich tun?“ / „Was blockiert mich?“

**Der Agent übersetzt intern:**  
Alle Systeme in menschliche Sprache; der User muss die Systeme nicht kennen. **Muster erklären – nicht die Mechanik benennen** (außer User will es).

---

## 2) Expertensprache: versteckt, dann erforschbar

| Phase | Für normale User | Für Deep Divers / Profis |
|-------|-------------------|---------------------------|
| **Default** | Nur Muster, Zyklen, Kräfte – **keine** Gates, Nakshatras, Jia/Geng, Rave Mandala. | – |
| **Optional** | – | Tab „Mechanik anzeigen“: Gates, Lines, BaZi Elements, Nakshatras, Houses, Definition Types, Ten Gods usw. |

Komplexität erscheint, **wenn der Nutzer bereit dafür ist**. So bleibt es massentauglich und tief zugleich.

---

## 3) UI-Flow (konkret)

| Schritt | Inhalt |
|--------|--------|
| **1 – Arrival** | Ruhige, organische Muster (z. B. Flowfields). Ein Satz: „Jeder Mensch folgt Mustern. Hier beginnt deine Karte.“ → **Beginnen**. |
| **2 – Gesprächsbeginn** | Agent (Voice + Text optional): „Was beschäftigt dich im Moment am meisten?“ User kann sprechen, schreiben oder Thema wählen (Klarheit, Beziehung, Energie, Entscheidung, Selbstbild). |
| **3 – Muster sichtbar** | Nach Eingabe: Analyse aus Chart, BaZi, Astro, KG, Dimensions. **Nicht** komplizierte Diagramme. Stattdessen: subtil leuchtender **archetypischer Kreis** mit 3–5 hervorgehobenen Kräften + Text (z. B. „Innere Spannung zwischen Rückzug und Ausdruck“, „Phase des Sammelns statt Handelns“). |
| **4 – Deep Insight** | Optional „mehr sehen“: **Der Kern** (ein Satz), **Die Dynamik**, **Der Schatten**, **Die Gabe**, **Der Weg**, **Der Kontext**, **Der nächste Schritt** (1 Satz Empfehlung). Keine Fachbegriffe. |
| **5 – Mechanik anzeigen** | Schmaler Button → für Nerds: HD Gate/Line, BaZi Element, Astro-Position, KG-Verbindung, Dimensions, Interactions, Transite. |
| **6 – Timeline** | Heute → 3 Tage → Woche → Monat → Jahresphase. Visuell. |
| **7 – Relationship Mode** | Zwei Profile → Spannungsfelder, Ergänzungen, Muster-Kollisionen, harmonische Flüsse – wieder nur Muster, keine Systembegriffe. |
| **8 – Exploring** | Archetypen kennenlernen, Energiespektrum, Schatten und Gaben, Zyklen – digitale Selbst-Mythologie. |

---

## 4) Agent-Haltung

- **Nicht:** allwissend, autoritär, prophezeiend, Orakel.
- **Sondern:** Begleiter, Spiegel, Navigator – **nicht** Entscheider.  
  Sanfter Übersetzer für das, was im Menschen selbst liegt.

---

## 5) Ästhetik

- Modern, archäologisch, futuristisch, mystisch aber klar.
- Kein Sternchen-Esoterik; Gold, Ocker, Schwarz, Sand.
- Diagramme, nicht Mandalas; Codes, nicht Horoskope; Energie-Flüsse, nicht Tarot.

---

## 6) Bezug zur Implementierung

- **Aktuell:** Pipeline + KG + Synthesis; keine Voice-UI, kein voller Agent-Flow, keine MCP.
- **Insight-Engine-UI** (next_steps) = erster sichtbarer Schritt (nach Backend-Phase, Option B) zu „Inhalte/Muster sichtbar“ (Listen, Detail, optional erste Visualisierungen).
- **Später:** Voice-first, visuelle Dynamik (KG → Diagramme), MCP, episode-based Unlock – wie in vision_2026_2027 beschrieben.

---

**Referenzen:** vision_2026_2027.md, story_and_mythology.md, interface_and_vision.md, next_steps_was_fehlt_noch.md.
