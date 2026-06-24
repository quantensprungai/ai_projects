<!-- Reality Block
last_update: 2026-06-23
status: stable
scope:
  summary: "IBKR API-Wahl für options-book: TWS API vs Client Portal API."
  in_scope:
    - comparison
    - recommendation
  out_of_scope:
    - setup steps
notes: []
-->

# IBKR API-Wahl: Client Portal vs. TWS API

IBKR bietet **zwei verschiedene** Programmier-Schnittstellen. Das ist **nicht** dasselbe Gateway.

## Kurzantwort für options-book

| API | Empfehlung |
|-----|------------|
| **TWS API** (+ IB Gateway) | ✅ **Ja** — Positionen, Options Chains, Greeks, später Orders |
| **Client Portal API** (REST) | ❌ **Nein** als Haupt-API — REST-Gateway ist anderer Stack, Options-Lücken |

**IBKR Desktop** = Trading-UI (manuell). **Kein Ersatz** für TWS API oder Client Portal Gateway.

---

## Vergleich (IBKR-offiziell, verdichtet)

| | **Client Portal API** | **TWS API** |
|--|----------------------|-------------|
| Protokoll | REST + WebSocket | Socket (TCP), Open-Source API |
| Gateway | **Client Portal Gateway** (eigenes Programm) | **IB Gateway** oder **TWS** |
| Python-Lib | REST-Client / HTTP | **`ib_async`** (Humbled Trader, unser Plan) |
| Options Chains | Eingeschränkt | ✅ Voll |
| Komplexe Options (Spreads) | Oft lückenhaft | ✅ |
| Marktdaten Streaming | WebSocket | ✅ Echtzeit über Socket |
| OAuth / Setup | REST-OAuth, CP Gateway | TWS/Gateway API-Settings |
| Gut für | Web-Apps, einfache Konten-Ops | **Algo, Monitor, Automation** |

---

## Was ist was? (Verwechslungsgefahr)

```text
IBKR Desktop          →  UI zum manuellen Tradens (kein voller API-Ersatz)

Client Portal Gateway →  Für Client Portal REST API only
IB Gateway            →  Für TWS API only (ib_async, ib_insync)
TWS                   →  Volle UI + kann auch TWS API hosten
```

**Zwei Gateways, zwei APIs.** Client Portal Gateway ≠ IB Gateway.

---

## Empfehlung options-book

### Jetzt (Stufe 0–1)
- **IB Gateway** (Paper, Port **4002**) im Hintergrund
- Python: **`ib_async`** → TWS API
- MVP-Daten weiterhin **yfinance** (Layer 1), bis IBKR-Sync steht

### Später (Auto-Execution)
- Gleiche TWS API — Orders über `ib_async`
- Weiter **IB Gateway**, nicht Client Portal REST

### Optional parallel
- **IBKR Desktop** nur für manuelle Orders / Option Lattice
- **Claude × IBKR MCP** (offiziell) für Research — separates Feature, kein Ersatz für unser Python

---

## Ports (TWS API)

| Umgebung | IB Gateway | TWS |
|----------|------------|-----|
| Paper | 4002 | 7497 |
| Live | 4001 | 7496 |

---

## Client Portal API — wann sinnvoll?

- Reine Web-App ohne Options-Tiefe
- Nur Kontostand / einfache Orders per REST
- **Nicht** unser Pfad für Options-Book + spätere Automation
