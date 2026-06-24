<!-- Reality Block

last_update: 2026-06-23

status: draft

scope:

  summary: "Ein IBKR Paper-Konto — zwei logische Profile (Standard / Micro)."

  in_scope:

    - single paper account

    - profile switch scripts

  out_of_scope:

    - live trading

notes:

  - "IBKR: nur ein Paper-Konto möglich — Micro virtuell oder manuell getaggt"

-->



# Paper Trading — Setup (ein Konto, zwei Profile)



IBKR: **nur ein Paper-Konto** (**DUR097452**, Port **4002**).  

Standard (€10K) und Micro (€1K) = **logische Books** in Software — siehe [`strategy_brief.md`](strategy_brief.md).



| Profil | NAV | positions-Datei | Script |

|--------|-----|-----------------|--------|

| **Standard** | €10.000 | `positions.json` | `use_paper_standard.ps1` |

| **Challenge** | €10.000 (Live-Ziel €30K+) | `positions.challenge.json` | `use_paper_challenge.ps1` |

| **Micro** | €1.000 | `positions.micro.json` | `use_paper_micro.ps1` |



Basiswährung Konto: **EUR**. US-Titel in **USD** (FX beachten).



---



## Wie zwei Profile mit **einem** Konto funktionieren



```text

IBKR Paper DUR097452 (physisch)

        │

        ├── Standard-Book  → positions.json      (~€8K deploy, 4 Namen)

        └── Micro-Book     → positions.micro.json (~€1K Regeln, 2–3 Namen)

```



**Empfohlene Reihenfolge:**



1. **Standard zuerst** — echte Paper-Trades, `sync_positions.py` → `positions.json`

2. **Micro parallel** — Option A: **nur simuliert** in `positions.micro.json` (Prozess üben, kein Broker-Chaos)  

   Option B: kleine echte Trades im **selben** Paper, aber nur Einträge in `positions.micro.json` pflegen (manuell, kein Auto-Sync-Mix)



**Nicht:** Standard + Micro blind per `sync_positions.py` mischen — das Script kennt aktuell ein Book.



---



## Gateway & Verbindung (gleich für beide)



1. **IB Gateway** → Paper, Port **4002**, Login **DUR097452**

2. Profil wählen:



```powershell

cd code\options-book

.\scripts\use_paper_standard.ps1   # oder use_paper_micro.ps1

python scripts\test_connect.py

```



3. Daily Run / Dashboard nutzt die **aktive** `BOOK_PROFILE` + positions-Datei aus `.env`



---



## Live (später)



```powershell

.\scripts\use_live.ps1

```



Micro kann auf Live mit **€1K echtes Konto** starten; Standard mit **€10K** — dann wieder **getrennte Konten** möglich.



---



## Scripts



| Script | BOOK_PROFILE | positions |

|--------|--------------|-----------|

| `use_paper_standard.ps1` | standard | positions.json (implizit) |

| `use_paper_micro.ps1` | micro | positions.micro.json (implizit) |

| `use_paper.ps1` | → Standard | Alias |

| `use_live.ps1` | live | positions.json |



---



## Fehler



| Symptom | Lösung |

|---------|--------|

| Micro und Standard vermischt | Nur eine positions-Datei pro Lauf aktiv; Micro simulieren bis klar |

| Buying Power „zu groß“ | Paper zeigt Gesamt-NAV — Micro-Regeln in **Software** durchsetzen |

| FX | EUR-Konto, USD-Underlyings — Reserve einplanen |

