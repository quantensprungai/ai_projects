<!-- Reality Block
last_update: 2026-06-23
status: draft
scope:
  summary: "Langdock GPT-5.5 in Cursor + options-book."
  in_scope:
    - cursor openai override
    - options-book .env
  out_of_scope:
    - proxy deployment
notes: []
-->

# Langdock GPT-5.5 — Cursor + options-book

## options-book (Layer 3 News)

Datei: `code/options-book/.env`

```env
OPENAI_API_KEY=dein_langdock_key
OPENAI_BASE_URL=https://api.langdock.com/openai/eu/v1
```

`config.yaml`:

```yaml
llm:
  provider: openai
  model: gpt-5.5
  reasoning_effort: low
```

Dein bestehender Langdock-Key aus `ANTHROPIC_API_KEY` funktioniert auch — der Loader liest
`OPENAI_API_KEY` → `LANGDOCK_API_KEY` → `ANTHROPIC_API_KEY`.

Modell-ID prüfen: `GET https://api.langdock.com/openai/eu/v1/models`

---

## GPT-5.5 in Cursor (Chat/Agent)

Langdock OpenAI ist **Cursor-kompatibel** — anders als der Anthropic-Endpoint.

1. **Cursor → Settings → Models**
2. **OpenAI API Key:** dein Langdock-Key
3. **Override OpenAI Base URL:** `https://api.langdock.com/openai/eu/v1`
4. **Add Custom Model:** `gpt-5.5` (exakte ID aus Models-Endpoint)
5. Modell in der Chat-Auswahl wählen

**Wichtig:** Wenn Override aktiv ist, können Cursor-eigene OpenAI-Modelle (GPT-5.x Subscription) auf deine Base-URL umgeleitet werden. Override nur nutzen, wenn du bewusst Langdock für OpenAI-Modelle willst — sonst für Coden Cursor-Standard lassen.

Dedicated Deployment: `<deployment-url>/api/public/openai/eu/v1`

---

## Referenz

- [Langdock OpenAI Chat](https://docs.langdock.com/en/developer/completion-api/openai)
- [Langdock Anthropic](https://docs.langdock.com/en/developer/completion-api/anthropic) (weiterhin für `provider: anthropic`)
