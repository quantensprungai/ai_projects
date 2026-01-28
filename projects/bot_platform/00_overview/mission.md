<!-- Reality Block
last_update: 2026-01-27
status: draft
scope:
  summary: "Mission/Zielbild für Bot Platform (Clawdbot) im Multi‑System."
  in_scope:
    - mission statement
    - success criteria
  out_of_scope:
    - implementation details
notes: []
-->

# Mission – Bot Platform (Clawdbot)

## Zweck
Wir betreiben eine **Bot Platform** (Clawdbot), die über Chat/GUI/CLI zugänglich ist und Aufgaben im Multi‑System sicher ausführen kann (mit Guardrails).

## Mission
- Ein Always‑On Assistant, der **Tool‑Using Workflows** zuverlässig ausführt (Ops, Home, Learning, Projekt‑Support).
- Klare **Trennung von Rollen/Trust** (ops vs. personal), damit “Bequemlichkeit” nicht zu Sicherheitsrisiko wird.

## Erfolgskriterien (v1)
- 2 getrennte Trust‑Zonen laufen stabil (Profile `ops` und `personal`).
- 4 Bots sind nutzbar: **Ops**, **Home Assistant**, **Learning**, **Project Bot (Test)**.
- Spark wird als LLM‑Backend genutzt (OpenAI‑kompatibel), ohne Cursor‑Modelle zu brechen.
- Keine Secrets im Repo; Backups der Bot‑State‑Ordner sind dokumentiert und getestet.

