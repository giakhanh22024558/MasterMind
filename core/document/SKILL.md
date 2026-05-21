---
name: document
description: Core framework for document-generation skills — .docx and similar text formats. Defines the invariant part: content in .md, format in Python code, following the 3-layer Core Rule. Concrete document skills (srs...) live in models/model_NNN/document/.
---

# Document — core document-generation framework

`core/document/` holds the **invariant** part of every text-document generation skill (`.docx`...). **Concrete** document skills live inside a model at `models/model_NNN/document/<type>/` (for example: `srs`).

> **Status:** framework + stub. The core will be extracted incrementally (defer-then-promote) once there are two or more document skills.

## Invariant principles

Every document skill must follow:

1. **[Core Rule](../core-rule/)** — input → `.md` context → Python format (agent layer) → `.docx` (user layer). Editing the user layer requires grepping the agent layer first.
2. **Content / format separation** — content in `.md`, presentation in Python code; never mixed.
3. **[Cross-reference](../cross-reference/)** — the technique applied when editing an already-generated `.docx`.
4. **[Atomic edits](../meta/atomic-edits-pattern/)** — `.docx` is a sync-prone file: close Word before writing, read/write once.
5. **[Conventions as data](../meta/conventions-as-data-pattern/)** — project conventions live in `<project>/<skill>-conventions.md`.

## Existing document skills

| Model | Skill | Location |
|---|---|---|
| model_001 | `srs` — generates IEEE SRS `.docx` documents | [`models/model_001/document/srs/`](../../models/model_001/document/srs/) |
| model_001 | `requirements` — consolidates any input into a requirements table | [`models/model_001/document/requirements/`](../../models/model_001/document/requirements/) |
| model_001 | `features` — derives a feature list from a requirements table | [`models/model_001/document/features/`](../../models/model_001/document/features/) |

## Creating a new document skill

Create it inside a model at `models/model_NNN/document/<type>/`, following the uniform structure ([`uniform-skill-structure`](../meta/uniform-skill-structure/)) and all the invariant principles above.
