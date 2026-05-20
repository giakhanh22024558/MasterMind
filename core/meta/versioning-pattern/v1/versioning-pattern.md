# Versioning pattern (general)

Every skill in this repo versions its content at the **leaf-folder grain**. AI sessions and human readers default to the **latest version** unless explicitly pinned to an older one.

## Goals

1. **Iterate freely** — improve one module without fearing breakage in unrelated modules
2. **Default to latest** — agents always pick the newest unless told otherwise
3. **Backward compatibility** — older versions stay available for projects pinned to them
4. **Minimal coupling** — modules version independently · bumping one doesn't force others to bump

## What is versioned, what isn't

| Category | Versioned? | Examples |
|---|---|---|
| **Content modules** (patterns, scripts, schemas, examples, type-specific docs) | ✅ Yes — `vN/` subfolders | `<skill>/patterns/v1/`, `<skill>/scripts/v1/` |
| **Navigation docs** (`SKILL.md`, `README.md`, `VERSIONING.md`) | ❌ No — always current | `<skill>/SKILL.md`, `models/model_NNN/README.md` |

Rule of thumb: if it describes **what to do**, version it. If it describes **how to navigate**, don't.

## Folder shape

Every content module — whether multi-file or single-doc — uses `vN/` subfolders:

### Multi-file modules

```
<skill>/patterns/
├── v1/
│   ├── pattern-a.md
│   └── pattern-b.md
└── v2/                              ← future bump
    ├── pattern-a.md                 (revised)
    └── pattern-b.md                 (unchanged copy or revised)
```

### Single-doc modules

```
<skill>/conventions-schema/
├── v1/
│   └── conventions-schema.md
└── v2/                              ← future bump
    └── conventions-schema.md        (revised)
```

The single doc is wrapped in a folder of the same name so the versioning shape stays uniform.

## Default version resolution

**Convention:** latest = highest `vN/` subfolder.

```
<skill>/scripts/
├── v1/
├── v2/
└── v3/                              ← LATEST · used by default
```

Agent following a cross-reference like `<skill>/scripts/` should:

1. List subfolders matching pattern `v\d+`
2. Pick the one with the highest number
3. Read content from that subfolder

No pointer file (`LATEST`) needed — convention is self-documenting via filesystem.

## How to pin to a specific version

### Project-wide pin (preferred)

In project's `<skill>-conventions.md`, add a Pinning section:

```markdown
## Skill version pinning

- `<skill>/<module>`: **v1** (we depend on v1 behavior)
- `<skill>/<other-module>`: default (latest)
```

The skill reads this section before applying defaults.

### One-off pin (conversation)

User says: "Use v1 of `<skill>/<module>` for this session" → agent reads from `v1/` instead of latest.

### Cross-reference pin (within content)

A versioned doc can explicitly pin:

```markdown
For the legacy form, see [`v1/foo.md`](../v1/foo.md).
```

Otherwise, references default to leaf-folder paths (latest):

```markdown
See [`foo`](../<module>/) for the foo pattern.
```

## Cross-reference convention

**Inside versioned content**, when linking to another versioned module:

| Goal | Link style | Example |
|---|---|---|
| Always latest of the referenced module (default) | leaf-folder path (no `vN`) | `[patterns/](../../patterns/)` |
| Specific version of the referenced module | explicit `vN/file.md` | `[pattern v1](../../patterns/v1/foo.md)` |

## How to bump a version

### Step 1 · Copy current to next

```bash
cp -r <skill>/<module>/v1 <skill>/<module>/v2
```

### Step 2 · Modify v2 only

Apply changes inside `v2/`. Leave `v1/` untouched.

### Step 3 · Update changelog

Add or update `<skill>/<module>/CHANGELOG.md` at the module's leaf level:

```markdown
# <module> — changelog

## v2 (YYYY-MM-DD)
- Added: <thing>
- Changed: <thing>
- Breaking: <thing>

## v1 (YYYY-MM-DD)
- Initial release
```

### Step 4 · Decide downstream pin status

For each consumer of this module (cross-references in other content):

- **Backward-compatible** → leave links to leaf folder (auto-latest pickup)
- **Breaking** → consumers needing old behavior pin to `v1/` explicitly

### Step 5 · No deletion of old versions

Old versions remain available indefinitely. Don't delete `v1/` even when "everyone uses v2".

Deletion is only acceptable when **no projects use the old version anymore** and you've confirmed externally. Document the deletion in CHANGELOG.

## Bumping a multi-file module · what counts as a "version"

**Recommended approach: each `vN/` is a complete snapshot** of the module at that version. If only one file in a 4-file module changes, copy all 4 into `v2/` and modify just the one.

- Pros: self-contained, easy to navigate
- Cons: duplication in storage (negligible for text files)

The alternative (selective: only changed files in `v2/`, others remain in `v1/`) has complex resolution semantics and breaks the "version = snapshot" mental model. Avoid unless you have a strong reason.

## Why per-leaf-folder grain (not coarser)?

Coarser grain (per-skill versioning, e.g. `skill/v1/<all-content>`) would force every file in the skill to bump when one tiny script changes. Per-leaf-folder grain avoids that — each module evolves on its own cadence.

## Why not finer grain (per-file)?

Per-file versioning (`module/<file-name>/v1/<file>.md`) would give maximum flexibility but adds:

- More folder nesting (worse readability)
- Files within a module usually evolve together (related concepts)
- Filesystem becomes harder to navigate visually

Per-leaf-folder is the right compromise.

## Summary

| Question | Answer |
|---|---|
| Where do versions live? | Every leaf content folder has `vN/` subfolders |
| Which version is default? | Highest `vN/` (convention) |
| Can projects pin to older versions? | Yes · via project's conventions file or one-off |
| What's NOT versioned? | Navigation docs (`SKILL.md`, `README.md`, `VERSIONING.md`) |
| How do I bump? | Copy `vN/` to `v(N+1)/`, modify, CHANGELOG · don't delete old |
| Cross-reference default | Leaf folder path (latest) · pin explicitly when needed |
