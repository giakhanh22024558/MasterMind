# Core Rule — the invariant 3-layer rule

The foundational rule that **every model** in MasterMind must follow — no matter how different the input context or the output document format may be. This belongs to the core (`core/`): it does not change when a new project or model is added.

## The three layers

| Layer | Role | Where it lives |
|---|---|---|
| **1 · Input → Context** | Analyze any raw input (requirements, source documents, images...) into structured Markdown. This `.md` file is the **context** — the source of truth for *content*. | `.md` file |
| **2 · Agent layer** | Normalize the *format / presentation* into Python code. Machine-managed: content in `.md`, format in Python. | `.md` file + Python code |
| **3 · User layer** | The deliverable handed to the user — `.docx`, `.drawio` files. The "rendered" layer, **not** the source of truth. | `.docx`, `.drawio` |

```
[raw input] ──analyze──▶  .md (context)  ─┐
                                           ├──▶  AGENT LAYER  (source of truth)
          format ──normalize──▶  Python   ─┘          │
                                                render │
                                                       ▼
                                          USER LAYER  (.docx / .drawio)
```

## Mandatory rule when editing the User layer

When an agent is asked to edit a `.docx` or `.drawio` file:

1. **Always grep the content from the Agent layer first** — read the `.md` file (and the Python format code) to obtain the authoritative content and context.
2. **Only then edit** the `.docx` / `.drawio`, using the **cross-reference technique** — see [`cross-reference`](../../cross-reference/).
3. **Never** edit the `.docx` / `.drawio` directly and expect the change to sync back into `.md`. The source of truth is always the Agent layer.

## Why

- Separating **content** (`.md`) from **presentation** (Python) means changing one never disturbs the other.
- The User layer is derived output — it can be regenerated and holds no unique state.
- Every model, however different its domain (SRS, architecture diagram...), reduces to the same flow → the `core/` layer stays reusable.

## How to apply

Every skill under `models/model_NNN/` — diagram, document, or a new type — must state in its `SKILL.md`: what the `.md` context is, what the Python format code is, what the User-layer file is, and must follow the 3-layer flow above.
