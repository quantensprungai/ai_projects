#!/usr/bin/env python3
"""Apply agent-specific templates to workspaces on VM102."""
import os
import re

BASE = "/home/user/clawd"
AGENTS = ["heiko", "noah", "flora", "familie"]

# Templates (inline if yaml not available)
TEMPLATES = {
    "heiko": {
        "agents_prepend": """# Fokus: Heiko – Projekte, Reminder, Multiprojektworkspace

Du unterstützt Heiko bei:
- Aufgaben und Projekten (ai_projects, Multi-Projekt-Workspace)
- Reminder, TODOs, Doku
- Projekt-Kontext, nächste Schritte

---
""",
        "user": ("Heiko", "Heiko", "Europe/Berlin"),
    },
    "noah": {
        "agents_prepend": """# Fokus: Noah – Lernagent 5.–6. Klasse Gym

Du unterstützt Noah (5.–6. Klasse Gymnasium) bei:
- Schulfächern, Hausaufgaben
- Spaced Repetition, Lernpläne
- Verständnisfragen, Übungen

---
""",
        "user": ("Noah", "Noah", "Europe/Berlin"),
    },
    "flora": {
        "agents_prepend": """# Fokus: Flora – Lernagent duales Studium Physiotherapie

Du unterstützt Flora (duales Studium Physiotherapie) bei:
- Examensvorbereitung
- Anatomie, Theorien, Praxistipps
- Lernpläne, Spaced Repetition

---
""",
        "user": ("Flora", "Flora", "Europe/Berlin"),
    },
    "familie": {
        "agents_prepend": """# Fokus: Familie – Allgemeinwissen, Termine, Planung

Du unterstützt die Familie bei:
- Allgemeinwissen, Geburtstage
- Urlaub, Wetter, Termine
- Finanzen, gemeinsame Planung

---
""",
        "user": ("Familie", "ihr", "Europe/Berlin"),
    },
}

for agent in AGENTS:
    ws = os.path.join(BASE, f"workspace-{agent}")
    t = TEMPLATES[agent]

    # AGENTS.md: prepend focus
    agents_path = os.path.join(ws, "AGENTS.md")
    if os.path.exists(agents_path):
        with open(agents_path) as f:
            content = f.read()
        if "Fokus:" not in content:
            with open(agents_path, "w") as f:
                f.write(t["agents_prepend"] + content)
            print(f"  {agent}: AGENTS.md updated")
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

print("Done.")
