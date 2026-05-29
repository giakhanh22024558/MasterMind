# model_001

Skill cluster number 001.

## Skills

| Category | Skill | Purpose |
|---|---|---|
| diagram | [`diagram/architecture/`](diagram/architecture/) | Draw / audit master architecture diagrams (C4-style) |
| diagram | [`diagram/erd/`](diagram/erd/) | Build Entity-Relationship Diagrams (crow's-foot notation) |
| diagram | [`diagram/wireframe/`](diagram/wireframe/) | Draw low-fi UI wireframes (annotated HTML) for new/changed screens, with a Design Assumptions table for client sign-off |
| document | [`document/srs/`](document/srs/) | Generate IEEE SRS documents in `.docx` format from Markdown |
| document | [`document/requirements/`](document/requirements/) | Consolidate any input into one requirements table |
| document | [`document/features/`](document/features/) | Derive a feature list / backlog from a requirements table (Epic → Feature → US) |
| document | [`document/foundation-sprint/`](document/foundation-sprint/) | Plan the Sprint 0 / cross-cutting foundation (Topic → Concern → Task → ACs) + gate-buffer scheduling |
| document | [`document/analysis/`](document/analysis/) | Gap Analysis & Impact Analysis for change requests (`.xlsx` sheets) |
| integration | [`integration/jira/`](integration/jira/) | Generate Jira issues + sub-tasks (BA / FE / BE) from approved CRs |
| integration | [`integration/google_sheets/`](integration/google_sheets/) | CRUD Google Sheets via API — cell-level edits preserve comments/history/dropdowns |
| pipeline | [`business_analysis/`](business_analysis/) | Orchestrate requirements → ERD + features into one end-to-end analysis |
| utility | [`setup/`](setup/) | `/set-up` command — bootstrap a BA workspace (folder layout + CLAUDE.md + artifact templates) for a new project |

Each skill follows the uniform structure — its entry point is its own `SKILL.md` — and follows the [Core Rule](../../core/core-rule/).
