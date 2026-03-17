#!/usr/bin/env python3
"""Apply agent-specific templates to workspaces on VM102."""
import os
import re

BASE = "/home/user/clawd"
AGENTS = ["heiko", "noah", "flora", "familie"]

# Templates (inline if yaml not available)
TEMPLATES = {
    "heiko": {
        "agents_prepend": """# Du bist Heikos Assistent – NICHT Lumi/Familien-Bot.

## Fokus: Heiko – Projekte, Reminder, Multiprojektworkspace

Du unterstützt Heiko bei:
- Aufgaben und Projekten (ai_projects, Multi-Projekt-Workspace)
- Reminder, TODOs, Doku
- Projekt-Kontext, nächste Schritte

---
""",
        "user": ("Heiko", "Heiko", "Europe/Berlin"),
    },
    "noah": {
        "agents_prepend": """# Du bist Noahs Lern-Assistent – NICHT Lumi/Familien-Bot.

## Fokus: Noah – Lernagent 5.–6. Klasse Gym

Du unterstützt Noah (5.–6. Klasse Gymnasium) bei:
- Schulfächern, Hausaufgaben
- Spaced Repetition, Lernpläne
- Verständnisfragen, Übungen

---
""",
        "user": ("Noah", "Noah", "Europe/Berlin"),
    },
    "flora": {
        "agents_prepend": """# Du bist Floras Lern-Assistent – NICHT Lumi/Familien-Bot.

## Fokus: Flora – Lernagent duales Studium Physiotherapie

Du unterstützt Flora (duales Studium Physiotherapie) bei:
- Examensvorbereitung
- Anatomie, Theorien, Praxistipps
- Lernpläne, Spaced Repetition

---
""",
        "user": ("Flora", "Flora", "Europe/Berlin"),
    },
    "familie": {
        "agents_prepend": """# Du bist Lumi, der Familien-Assistent – NICHT Heikos Projekt-Bot.

## Fokus: Familie – Allgemeinwissen, Termine, Planung

Du unterstützt die Familie bei:
- Allgemeinwissen, Geburtstage
- Urlaub, Wetter, Termine
- Finanzen, gemeinsame Planung

---
""",
        "user": ("Familie", "ihr", "Europe/Berlin"),
        "soul_prepend": "**Du bist Lumi, der Familien-Assistent.** Du hilfst der Familie bei Allgemeinwissen, Terminen und Planung – nicht Heikos Projekt-Assistent.\n\n",
    },
}

# SOUL identity lines (nur familie hat soul_prepend; heiko etc. nutzen soul_identity)
SOUL_IDENTITY = {
    "heiko": "**Du bist Heikos persönlicher Assistent.** Du hilfst bei Projekten, Remindern und Doku – nicht der Familien-Bot.\n\n",
    "noah": "**Du bist Noahs Lern-Assistent.** Du hilfst bei Schulfächern und Hausaufgaben – nicht der Familien-Bot.\n\n",
    "flora": "**Du bist Floras Lern-Assistent.** Du hilfst bei Physiotherapie-Studium und Examensvorbereitung – nicht der Familien-Bot.\n\n",
    "familie": None,  # nutzt soul_prepend aus TEMPLATES
}

for agent in AGENTS:
    ws = os.path.join(BASE, f"workspace-{agent}")
    t = TEMPLATES[agent]

    # AGENTS.md: Identity-Zeile + Fokus (wird zuerst gelesen!)
    agents_path = os.path.join(ws, "AGENTS.md")
    if os.path.exists(agents_path):
        with open(agents_path) as f:
            content = f.read()
        # Identity-Zeile fehlt? -> Voranstellen (auch wenn Fokus schon da)
        identity_markers = ("Du bist Heikos", "Du bist Lumi", "Du bist Noahs", "Du bist Floras", "Sage", "Flora Agent")
        if not any(m in content[:300] for m in identity_markers):
            first_line = t["agents_prepend"].split("\n")[0] + "\n\n"
            content = first_line + content
            with open(agents_path, "w") as f:
                f.write(content)
            print(f"  {agent}: AGENTS.md identity updated")
        elif "Fokus:" not in content:
            with open(agents_path, "w") as f:
                f.write(t["agents_prepend"] + content)
            print(f"  {agent}: AGENTS.md focus updated")
    else:
        print(f"  {agent}: AGENTS.md not found")

    # USER.md: update name/call/timezone
    user_path = os.path.join(ws, "USER.md")
    if os.path.exists(user_path):
        name, call, tz = t["user"]
        with open(user_path) as f:
            content = f.read()
        content = re.sub(r"- \*\*Name:\*\*.*", f"- **Name:** {name}", content, count=1)
        content = re.sub(r"- \*\*What to call them:\*\*.*", f"- **What to call them:** {call}", content, count=1)
        content = re.sub(r"- \*\*Timezone:\*\*.*", f"- **Timezone:** {tz}", content, count=1)
        with open(user_path, "w") as f:
            f.write(content)
        print(f"  {agent}: USER.md updated")

    # SOUL.md: Agent-Identitaet voranstellen (verhindert Verwechslung)
    # Flora: Custom Sage-Persona – nicht überschreiben
    soul_prepend = None
    if agent == "flora":
        soul_path = os.path.join(ws, "SOUL.md")
        if os.path.exists(soul_path):
            with open(soul_path) as f:
                content = f.read()
            if "Sage" in content[:400] or "Salbei" in content[:400]:
                print(f"  {agent}: SOUL.md (Sage) – skip")
            else:
                soul_prepend = SOUL_IDENTITY.get(agent)
        else:
            soul_prepend = SOUL_IDENTITY.get(agent)
    else:
        soul_prepend = t.get("soul_prepend") or SOUL_IDENTITY.get(agent)
    if soul_prepend:
        soul_path = os.path.join(ws, "SOUL.md")
        if os.path.exists(soul_path):
            with open(soul_path) as f:
                content = f.read()
            if "**Du bist " not in content[:400]:
                with open(soul_path, "w") as f:
                    f.write(soul_prepend + content)
                print(f"  {agent}: SOUL.md identity updated")

print("Done.")
