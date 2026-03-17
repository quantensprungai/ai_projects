# Inner Compass — Ideen & Backlog

> Parkplatz für Ideen die noch nicht entschieden sind. Wenn entschieden → nach decisions.md verschieben.

## Produkt-Ideen

### Relationship Mode (Partnervergleich)
Zwei Profile → Spannungsfelder, Ergänzungen, Muster-Kollisionen. Composite-Charts (HD) + Synastry (Astro) + Day-Branch-Vergleich (BaZi). Könnte eigener Bereich oder eigenes Produkt werden.

### Voice-Agent
KI als gesprochener Begleiter statt nur Text. Kontextualisiert: weiß welches Element in welchem Lebensbereich. Technisch: RAG auf KG + Embeddings + TTS.

### Community-Experimente
User können eigene Experimente vorschlagen und teilen. Voting/Bewertung. Füllt Handbuch-Schicht 4 bottom-up.

### Daily Compass
Tägliche Push-Notification: "Heute ist Maya Kin X, dein Transit ist Y, dein BaZi Tageseinfluss ist Z. Fokus: [Lebensbereich]." Retention-Mechanismus.

### Compatibility-API
Relationship Mode als API für Dating-Apps oder Team-Building-Tools.

## Technische Ideen

### Lokale Embedding-Modelle statt OpenAI
text-embedding-3-large kostet. Alternative: Lokales Modell auf Spark (z.B. BGE, Instructor). Gleiche Qualität? Testen.

### Strukturbaum-Visualisierung
Den KG als interaktiven Graphen visualisieren (für Entwickler/Power-User). D3.js oder ähnlich.

### Multilingual Pipeline
Aktuell: KG in Englisch, Wording-Schicht in Deutsch/Englisch. Langfristig: Chinesisch (BaZi-Quellen), Sanskrit (Jyotish-Quellen), Maya-Sprachen direkt extrahieren.

### Progressive Web App
Statt native App: PWA mit Offline-Fähigkeit. Handbuch offline lesbar. Charts berechnen braucht online.

## Story-Ideen

### "Die Bibliothek"
Metapher für den KG: Eine Bibliothek, in der jedes Wissenssystem ein Bücherregal ist. Cross-System-Mappings sind Querverweise zwischen Büchern. Meta-Knoten sind die Themen, unter denen mehrere Bücher stehen.

### Staffel-basiertes Unlock als Erlebnis
Nicht nur Feature-Unlock, sondern narratives Erlebnis: "Staffel 2: Die östlichen Meister" mit Intro-Story, visuellem Reveal, Animations.

### Astrologische Events als Community-Momente
Saturn Return, Mondfinsternis, etc. als App-weite Events: "Heute erleben 2.4 Mio Menschen ihren Saturn Return. Du bist einer davon."

## Architektur-Ideen (aus hd_saas-Erkenntnissen)

### Priority Rules / Emergent Logic / Conflict Resolution
- Wenn Dimensionen oder Interpretationen kollidieren (z.B. Type vs. Authority), welche hat Vorrang? HD: Authority > Type > Profile. Als Regelwerk später modellierbar.
- Emergent Logic: Wenn mehrere Elemente zusammenwirken (offenes Solarplexus + Generator), entstehen neue Muster. Braucht Reasoning-Layer.
- Conflict Resolution: Bei widersprüchlichen Quellen → Interpretationen bleiben getrennt; Synthesis konsolidiert oder zeigt quellenspezifisch. Explizite Regeln für später.

### Concept Nodes (expresses_as Edges)
Optional: `node_type=concept` für Shadow, Gift, Archetype; Kanten `expresses_as` von Element-Node zu Concept-Node. Aktuell: Dimensions nur in node.metadata.

### hd_documents vs. hd_assets Konsolidierung
Analyse schlägt vor: konsolidieren. Aktuell: hd_assets = Knowledge Pipeline, hd_documents = Upload. Klären wenn Schema-Migration.

## Offene Fragen

- Wie tief geht die Granularität der Experimente? Bis hin zu "sag diesen Satz" oder eher "beobachte diese Woche"?
- Brauchen wir ein User-Profil-System jenseits von Geburtsdaten? (z.B. "ich bin introvertiert" als manueller Input)
- Wie handhaben wir System-Updates? (z.B. neue Gene-Keys-Bücher, neue HD-Erkenntnisse)
- Soll der KI-Chat die Wording-Ebene automatisch wählen oder der User manuell?
