# Literatur Content-Wellen — Stand 2026-07-18

last_update: 2026-07-18
scope: Alle kuratierten Werke bleiben im Scope; Wellen = Verarbeitungsreihenfolge, kein Aussortieren
in_scope: Inventar-Refresh, Queue, Wave-Definition
out_of_scope: PDF-Upload/Pipeline-Ausführung (nächster Schritt)

## Klärung: Warum Wellen, wenn alles rausgesucht wurde?

Die Werke wurden bewusst kuratiert (`entity_registry_*`, Ordner `K2`/`K3`/`K4`, Download-Matrix).  
**Nichts wird gestrichen.** Wellen bedeuten nur:

> Wir verarbeiten **alle** `status=ok`-Werke — aber **nacheinander**, in einer Reihenfolge, die Synthese-Qualität maximiert (Referenz vor Überblick vor Spezial).

Das ist kein „nur einen Teil nutzen“, sondern **Queue-Management** gegen den BaZi-Fehler (Überblickswerk ohne Cap → generische Synthese).

## Inventar-Refresh (dieser Rechner)

| | Juni (anderer PC) | Juli (dieser PC) |
|--|-------------------|------------------|
| Quelle | `he5013\Nextcloud\…\Literatur` | `C:\Users\Admin105\Downloads\Literatur` |
| Dateien | 216 | **219** |
| `status=ok` | 208 | **208** |
| P0 (K2+K3+K4 yes) | 81 | **74** |

CSVs: `projects/inner_compass/reference/literature_*_2026-07-18.csv`  
Queue: `literature_content_wave_queue_2026-07-18.csv`  
Skript: `scripts/build_literature_inventory.py`, `scripts/build_content_wave_queue.py`

## Queue-Überblick (208 ok-Werke)

| Wave | Bedeutung | Anzahl | Status |
|------|-----------|--------|--------|
| **0** | Bereits in S5/S6 verarbeitet | **5** | done |
| **1** | `K2_ref` / Struktur-Referenz | **141** | queued |
| **3** | `K3_deutung` (Deutung/Regeln) | **36** | queued |
| **4** | `K4_deutung` (Bedeutungstiefe) | **26** | queued |

Wave 2 (`K2+K3`-Ordner) ist auf Disk in die Rollen K2_ref/K3 eingeflossen — keine eigene Restmenge.

### Wave 0 — done (nicht nochmal Full-Pipeline)

- HD: Complete Rave I'Ching · Life Force (Channels)
- Gene Keys: 64 Ways · Opening Doors
- BaZi: Destiny Code Combined (Joey Yap)

### Wave 1 zuerst — aktive Systeme (Auszug der Logik)

System-Priorität in der Queue: `hd → bazi → genekeys → ziwei → astro → jyotish → …`

Pro Werk unverändert: Seed/strict ok → Upload → Pipeline → `ic_k2_state_audit.py` → nächstes Werk.

## AA-Lücken (14, unverändert)

Siehe `literature_aa_need_2026-07-18.csv` (u. a. Rave Cosmology IV–VII). Das blockiert die Content-Welle nicht — nur die betroffenen Curriculum-IDs.

## Nächster Schritt

1. Queue ab Wave 1 abarbeiten (alle 203 queued — kein Cherry-Pick außer Reihenfolge).
2. Optional: pro System Batch von 5–10 parallel vorbereiten, aber Audit-Gate nach jedem Werk/Batch.
3. Branches pushen (siehe Chat).
