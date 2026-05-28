# input/

**User-managed** raw materials for the project. Drop files here in any format:

- `.docx` — SRS, requirement docs, contracts
- `.xlsx` — CR lists, issue trackers, feature lists
- `.pdf` — scanned specs
- `.png` / `.jpg` — wireframe screenshots, UI mockups
- `.drawio` / `.fig` — diagrams from designers
- `.csv` / `.txt` — data exports

## Core Rule

- ✅ User drops files
- ✅ Agent READS them (via python-docx / openpyxl / MCP read)
- ❌ Agent does NOT write into this folder (it is input from the user side)

Every file `input/<name>.<ext>` → the agent generates a `context/<name>.md` sidecar (cheap to read in later sessions).

## Workflow

1. User drops a file here
2. Asks the agent: `"read context of <file>"` or `"sync drive"` (for integration sync)
3. Agent creates `context/<file>.md` mirroring the file as markdown
4. Other skills then use `context/<file>.md` as input for artifacts (e.g. `docs/requirements.md`)
