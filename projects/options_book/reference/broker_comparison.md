<!-- Reality Block
last_update: 2026-06-23
status: draft
scope:
  summary: "Robinhood vs. IBKR für AlgoBot — Entscheidungsgrundlage."
  in_scope:
    - comparison
    - recommendation
    - integration paths
  out_of_scope:
    - implementation
notes:
  - "Referenz: Claude Portfolio.pdf (Robinhood + yfinance Monitor)"
  - "Referenz: humbledtrader.com/blog/ai-trading-bot-claude-ibkr/ (IBKR Auto-Bot)"
-->

# Broker-Vergleich: Robinhood vs. IBKR

## Drei verschiedene Ansätze (nicht verwechseln)

| Ansatz | Quelle | Broker | Auto-Execution? |
|--------|--------|--------|-----------------|
| **A — Morning Monitor** | Claude Portfolio.pdf | Robinhood (manuell) | ❌ Nur Fakten/Alerts |
| **B — Auto Day-Trading Bot** | Humbled Trader + IBKR | IBKR API (`ib_async`) | ✅ Vollautomatisch (Paper) |
| **C — IBKR × Claude (offiziell)** | IBKR AI Integrations | IBKR MCP Connector | ❌ Draft Orders, du bestätigst |

**Unser Projekt = Ansatz A** (Monitor, Human-in-the-Loop).  
IBKR ist trotzdem der **bessere Broker** für uns — weil du Zugang hast und er die Daten-/Positions-Sync-Schicht verbessert, ohne dass wir sofort Ansatz B bauen müssen.

---

## Vergleich

| Kriterium | Robinhood | IBKR |
|-----------|-----------|------|
| **API für Retail** | ❌ Keine offizielle API | ✅ TWS / Gateway + `ib_async` |
| **Options-Daten** | Nur über Drittanbieter (yfinance) | ✅ Echte Chains, Greeks, OI vom Broker |
| **Positionen syncen** | ❌ Manuell → `positions.json` | ✅ Automatisch aus Account lesen |
| **Paper Trading** | Eingeschränkt | ✅ Separates Paper-Sub-Account |
| **Claude-Integration** | Nur manuell (Web) | ✅ Offizieller MCP-Connector (Research) |
| **Kosten Daten** | $0 (yfinance) | Marktdaten-Abos je nach Börse (US oft günstig) |
| **Setup-Aufwand** | Minimal | TWS/Gateway muss laufen |
| **PDF-Referenz** | ✅ So gemacht | — |
| **Humbled-Trader-Referenz** | — | ✅ So gemacht |

---

## Empfehlung: **IBKR als Primary Broker**

### Warum IBKR für dich passt

1. **Du hast bereits Zugang** — kein neuer Broker nötig
2. **Positionen-Sync** — `positions.json` muss nicht jedes Mal per Hand gepflegt werden (Phase B+)
3. **Bessere Options-Qualität** — Greeks/IV direkt vom Broker statt yfinance-Näherung
4. **Paper Account** — Monitor + spätere Features sicher testen
5. **Claude MCP** — Phase A Research direkt mit echten Portfolio-Daten (offiziell, Human-in-the-Loop)
6. **Erweiterbar** — falls du später Execution willst (Humbled-Trader-Pfad), ist die Infrastruktur da

### Was wir **nicht** aus Humbled Trader übernehmen

Der [Humbled-Trader-Artikel](https://www.humbledtrader.com/blog/ai-trading-bot-claude-ibkr/) baut einen **vollautomatischen Day-Trading-Bot** (S&P-500-Gapper-Scanner, Orders ohne Mensch). Das widerspricht unserem Design-Prinzip **„Facts, not advice"** und dem PDF-Monitor.

| Humbled Trader | Unser AlgoBot |
|----------------|---------------|
| Auto-Orders via IBKR API | Keine Orders — nur Alerts |
| Premarket Scanner alle 30 min | 1× Daily Run nach Close |
| Stock Day-Trading | Options + Shares, LEAPS-Fokus |
| Strategie in JSON, Bot entscheidet | Du entscheidest |

---

## Integrations-Stufen (Roadmap)

```text
Stufe 0 (MVP)     yfinance + manuelle positions.json     ← Layer 1–4 lauffähig, broker-agnostisch
Stufe 1 (empfohlen) IBKR Position-Sync → positions.json  ← nach Layer 1
Stufe 2 (optional)  IBKR Marktdaten statt yfinance         ← bessere Greeks/Chains
Stufe 3 (optional)  IBKR MCP für Phase A Research          ← Claude + echtes Portfolio
Stufe 4 (out of scope) Auto-Execution                      ← nur bei expliziter Entscheidung
```

**Entscheidung Phase 0:** IBKR als Broker, MVP startet trotzdem mit yfinance (Layer 1 Spec). IBKR-Sync kommt in Stufe 1.

---

## IBKR Setup (für Stufe 1+, Vorbereitung)

Aus Humbled Trader / IBKR-Doku:

1. **TWS oder IB Gateway** installieren
2. API aktivieren: *Enable ActiveX and Socket Clients*, localhost only
3. **Read-Only API** für Monitor-Phase (Stufe 1) — sicherer als Write
4. Paper-Sub-Account nutzen zum Testen
5. Python: `ib_async` (Nachfolger von `ib_insync`)
6. Test: `connect('127.0.0.1', 7497, clientId=99)` → Paper TWS Port

| Port | Umgebung |
|------|----------|
| 7497 | TWS Paper |
| 7496 | TWS Live |
| 4002 | IB Gateway Paper |
| 4001 | IB Gateway Live |

---

## Offene Entscheidung

- [ ] Paper vs. Live für ersten Sync-Test
- [ ] TWS vs. IB Gateway (Gateway leichter für headless/Cron)
- [ ] US-Options-Marktdaten-Abonnement bei IBKR prüfen
