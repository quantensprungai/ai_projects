<!-- Reality Block

last_update: 2026-06-24

status: draft

scope:

  summary: "MVP-Fortschritt vs Master-Plan."

  in_scope:

    - completion estimate

  out_of_scope:

    - phase A research

notes: []

-->



# MVP-Fortschritt (~75 % von Phase B + Ops)



> Stand: 2026-06-24 · Monitor-only, kein Auto-Trading



## Gesamt



| Bereich | Fertig | Kommentar |

|---------|--------|-----------|

| **Phase 0** Setup | **100 %** | Doku + Repo + Config |

| **Stufe 1** IBKR Sync | **100 %** | Read-only → `positions.json` |

| **Layer 1** Valuation | **100 %** | yfinance, Greeks, Snapshots, SQLite |

| **Layer 2** Analytics | **100 %** | Allocation, IV-Rank, Flags |

| **Layer 3** Macro + News | **95 %** | Macro ✅ · News ✅ (GPT-5.5 Langdock) |

| **Layer 4** Alerts + UI | **~90 %** | Alerts ✅ · Monitor + Greeks + Screener Tabs ✅ |

| **Phase C** Ops | **~85 %** | Task Scheduler ✅ · Paper-Switch-Scripts ✅ |

| **Phase A** Research | **~15 %** | S0 strategy_brief + S1 universe.json (2026-06-24) |



**Phase B (Build) ≈ 90 %** · **Gesamtprojekt inkl. A ≈ 75 %**



---



## Layer 4 Dashboard — Spec vs. Ist



| Panel (Spec) | Status |

|--------------|--------|

| Status Strip | ✅ |

| Active Alerts (farbcodiert) | ✅ (new_strike gelb teilweise) |

| Positions Grid + DTE + Progress | ✅ |

| Strike Ladder ±6 | ✅ (HELD/NEW + orange styling) |

| Allocation Bars | ✅ |

| News Feed | ✅ (Material +/- + Headlines) |

| Theta Decay (BS-Kurve bis Expiry) | ✅ |

| Bloomberg-Polish | ✅ Basis (orange/dark/monospace) |

| Greeks Tab (per contract + exposure bars) | ✅ |

| Universe Screener Tab | ✅ UI-Stub — wartet auf `research/universe.json` aus Phase A |



---



## Paper Trading (DUR097452)

Siehe [paper_trading_setup.md](../reference/paper_trading_setup.md) · `scripts/use_paper.ps1` / `use_live.ps1`



---



## Noch offen (Post-MVP)



- Phase A: echtes Book / Targets aus Strategie

- Notifier aktivieren (Telegram)

- IBKR Marktdaten statt yfinance (optional)

- `positions.json` aus Live-Account pflegen


