## Makerkit – Next.js Supabase SaaS Kit Turbo (Doku & Rules)

Dieses Verzeichnis enthält **lokal importierte Referenz-Dokumentation** und **Cursor Rules** zur Makerkit-Boilerplate „Next.js Supabase SaaS Kit Turbo“.

### Wofür ist das hier?
- **Referenz/Onboarding**: Schnelles Nachschlagen zu Setup, Konfiguration, Security, Billing, RBAC, etc.
- **HD‑SaaS Planung**: Abgleich unserer HD‑SaaS Architektur/PRD mit dem Makerkit‑Stack.
- **Rules (Cursor)**: Hilft beim konsistenten Arbeiten im späteren SaaS‑Codebase.

### Wo gehört der eigentliche SaaS‑Code hin?
Der echte Makerkit‑Code (App/Packages) sollte als **separates Projekt** unter `code/` liegen, z. B.:
- `code/hd_saas_app/` (geklohntes Makerkit Repo, dort wird angepasst)

Wichtig: Das Root-Repo (`ai_projects`) ignoriert `/code/**` bewusst (Doku/Infra getrennt von Code-Repos).

### Cursor Rules
Die hier abgelegten Rules sind **Referenz**.
Damit sie automatisch auf dein SaaS‑Projekt wirken, kopiere sie in das jeweilige Projekt-Root:
- `code/hd_saas_app/.cursor/rules/*`


