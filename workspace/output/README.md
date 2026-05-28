# output/

**Deliverables** — complex binary files generated from the artifact templates in `docs/`.

## Common file types

- `.docx` — SRS, reports
- `.xlsx` — rendered backlog, Gap/Impact Analysis, Jira CSV import
- `.drawio` — ERD / architecture diagrams (rendered from Mermaid)
- `.pdf` — exported reports
- `.json` — Jira REST API payloads
- `jira/*.md` — task descriptions to paste into the Jira UI

## Conventions

- ✅ Agent writes deliverable files
- ✅ Agent also creates a `.md` sidecar in `context/` (cheap to read)
- ✅ User can download / share files from here
- ❌ Do not edit binaries in this folder by hand — re-render from the source in `docs/` or the artifact md

## Common sub-folders

```
output/
├── <project>-SRS.docx
├── <project>-Backlog.xlsx
├── Gap_Analysis.xlsx
├── <project>-ERD.drawio
└── jira/
    ├── all-tasks.md
    ├── cr-01-task.json
    └── cr-01-task.md
```

The agent creates sub-folders as needed.
