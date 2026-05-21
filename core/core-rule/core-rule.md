# Core Rule — the invariant 3-layer rule

The foundational rule that **every model** in MasterMind must follow — no matter how different the input context or the output document format may be. This belongs to the core (`core/`): it does not change when a new project or model is added.

## The three layers

| Layer | Role | Where it lives |
|---|---|---|
| **1 · Input → Context** | Analyze any raw input (requirements, source documents, images...) into structured Markdown. The `context.md` files are the **context** — the source of truth for *content*. | `context/` folder |
| **2 · Agent layer** | Normalize the *format / presentation* into Python code. Machine-managed: content in `.md`, format in Python. | `context/` + the model's Python code |
| **3 · User layer** | The deliverable handed to the user — `.docx`, `.xlsx`, `.drawio` files. The "rendered" layer, **not** the source of truth. | `output/` folder |

```
[raw input] ──analyze──▶  .md (context)  ─┐
                                           ├──▶  AGENT LAYER  (source of truth)
          format ──normalize──▶  Python   ─┘          │
                                                render │
                                                       ▼
                                   USER LAYER  (.docx / .xlsx / .drawio)
```

## Working-folder layout

A user clones MasterMind into a **working folder**. Three sibling folders live **outside** MasterMind, in the working folder:

```
<working-folder>/
├── MasterMind/        ← this repo (the skills)
├── input/             ← user-managed · raw context files, any format
├── context/           ← the analyzed context.md mirror of input/ (built by the model)
└── output/            ← user-managed · finished deliverables (.docx, .xlsx, .drawio...)
```

- **`input/`** — the user drops in every file or folder they want used as context, in any format.
- **`context/`** — the model writes the analyzed `context.md` files here (Layer 1). It mirrors `input/`.
- **`output/`** — every deliverable the AI produces is written here.

None of these three folders are ever part of the MasterMind repo, and **nothing runtime is stored inside a model** — a model holds only its skill definition.

## Session start — required triggers

When an AI session begins in a working folder that contains MasterMind, the agent MUST, before doing any domain work:

1. **Ensure `input/` and `output/` exist** — create them as siblings of `MasterMind/` if they are missing.
2. **Select a model** — ask the user to choose one of `models/model_NNN/`. If the user prefers, create a **new model** instead, following this Core Rule.

## Context ingestion — the `context/` folder

The selected model **consumes the user's `input/`** and turns it into Layer 1:

- **Mirror the folder structure** of `input/` into the `context/` folder (a sibling of `input/` and `output/`, outside MasterMind).
- For **every file** in `input/` — whatever its format (`.docx`, `.xlsx`, `.drawio`, image, ...) — produce a `context.md` holding its analyzed content. Each input file maps to a same-named folder containing a single `context.md`, so the structure mirrors `input/` but every leaf file is a `context.md`.

```
input/                          context/
├── spec.docx           ──▶     ├── spec/context.md
├── data.xlsx           ──▶     ├── data/context.md
└── refs/                       └── refs/
    └── flow.drawio     ──▶         └── flow/context.md
```

`context/` is per-session, user/project-specific data. It lives in the working folder **outside** MasterMind — never inside a model, never committed to the repo.

## Output routing

Whenever the user asks to draw a `.drawio`, generate a `.docx` / `.xlsx`, or produce any other complex-format deliverable, the result is **always written to `output/`** — never inside MasterMind, never inside `input/`.

## Mandatory rule when editing the User layer

When an agent is asked to edit a `.docx`, `.xlsx`, or `.drawio` file in `output/`:

1. **Always grep the content from the Agent layer first** — read the `context.md` files (and the model's Python format code) to obtain the authoritative content and context.
2. **Only then edit** the deliverable, using the **cross-reference technique** — see [`cross-reference`](../cross-reference/).
3. **Never** edit the `output/` file directly and expect the change to sync back into the context. The source of truth is always the Agent layer.

## Why

- Separating **content** (`.md`) from **presentation** (Python) means changing one never disturbs the other.
- The User layer (`output/`) is derived output — it can be regenerated and holds no unique state.
- `input/`, `context/`, and `output/` all stay outside the repo and in the working folder, so MasterMind stays a clean, shareable skill library with no runtime data inside it.
- Every model, however different its domain (SRS, architecture diagram...), reduces to the same flow → the `core/` layer stays reusable.

## How to apply

Every skill under `models/model_NNN/` — diagram, document, or a new type — must:

- State in its `SKILL.md` what the `context.md` input is, what the Python format code is, and what the `output/` deliverable is.
- Follow the session flow above: ingest `input/` into the `context/` folder, work from the Agent layer, write every deliverable to `output/`.
- Follow the 3-layer flow without exception.
