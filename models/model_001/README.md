# model_001

Skill cluster number 001.

## Skills

| Category | Skill | Purpose |
|---|---|---|
| diagram | [`diagram/architecture/`](diagram/architecture/) | Draw / audit master architecture diagrams (C4-style) |
| diagram | [`diagram/erd/`](diagram/erd/) | Build Entity-Relationship Diagrams (crow's-foot notation) |
| document | [`document/srs/`](document/srs/) | Generate IEEE SRS documents in `.docx` format from Markdown |
| document | [`document/requirements/`](document/requirements/) | Consolidate any input into one requirements table |
| document | [`document/features/`](document/features/) | Derive a feature list / backlog from a requirements table |
| document | [`document/analysis/`](document/analysis/) | Gap Analysis & Impact Analysis for change requests (`.xlsx` sheets) |
| integration | [`integration/jira/`](integration/jira/) | Sinh Jira issue + sub-task (BA / FE / BE) từ CR đã approve |
| integration | [`integration/google_sheets/`](integration/google_sheets/) | CRUD trên Google Sheets via API — cell-level edit giữ comment/history/dropdown |
| pipeline | [`business_analysis/`](business_analysis/) | Orchestrate requirements → ERD + features into one end-to-end analysis |

Each skill follows the uniform structure — its entry point is its own `SKILL.md` — and follows the [Core Rule](../../core/core-rule/).
