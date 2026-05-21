# business_analysis — README

A skill that turns any raw project input into a structured business analysis: a **consolidated requirements table**, an **ERD**, and a **feature list**.

Philosophy: whatever the input, everything reduces to **one requirements table** — and the ERD and feature list both derive from it.

## Quick start

| If you want to… | Read |
|---|---|
| Understand the skill in one page | [`SKILL.md`](SKILL.md) |
| Know the requirements table structure | [`requirements-table/`](requirements-table/) |
| Know the feature list structure | [`feature-list/`](feature-list/) |
| Know the ERD conventions | [`erd-conventions/`](erd-conventions/) |
| Know what a project must declare | [`conventions-schema/`](conventions-schema/) |
| See a worked example | [`examples/`](examples/) |
| Generate the pilot `.xlsx` | [`scripts/`](scripts/) |

## The three artifacts

| Artifact | Form | Where |
|---|---|---|
| Requirements table | `.md` (timestamp-batched table) + `.xlsx` | `context/` + `output/` |
| ERD | Mermaid in `.md`; `.drawio` on request | `context/` + (on request) `output/` |
| Feature list | `.md` table + `.xlsx` | `context/` + `output/` |

## Workflow in three steps

1. **Consolidate** — ingest the input, write the requirements table (grouped by analysis-run timestamp).
2. **In parallel** — derive the ERD (entities + relationships) and the feature list from the requirements.
3. **Render** — save each table as `.md` (context) + `.xlsx` (pilot); render the ERD `.drawio` only on request.

## Folder layout

```
business_analysis/
├── SKILL.md                     ← agent-facing entry
├── README.md                    ← this file
├── conventions-schema/          ← what a project must declare
├── conventions-defaults/        ← defaults
├── requirements-table/          ← requirements table spec
├── feature-list/                ← feature list spec
├── erd-conventions/             ← ERD crow's-foot conventions
├── patterns/                    ← requirements-as-single-source pattern
├── examples/                    ← worked walkthrough
└── scripts/                     ← ba_md_to_xlsx.py + README
```

## Stack

- **Markdown** for content + the `.md` context tables
- **Mermaid** (`erDiagram`) for the ERD
- **Python** (`openpyxl`) for the `.xlsx` generator — install: `pip install openpyxl`

## License

Internal. Adapt freely. No warranty.
