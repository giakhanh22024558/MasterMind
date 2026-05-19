# Versioning model

Every **content module** in this skill is versioned at the lowest folder granularity. AI sessions and human readers default to the **latest version** unless explicitly pinned to an older one.

## Goals

1. **Iterate freely** — improve a module without fearing breakage in unrelated modules
2. **Default to latest** — agents always pick the newest unless told otherwise
3. **Backward compatibility** — older versions stay available for projects that pin to them
4. **Minimal coupling** — each module versions independently · bumping one doesn't force others to bump

## What is "versioned"?

The two categories:

| Category | Versioned? | Examples |
|---|---|---|
| **Content modules** (concepts, patterns, scripts, schemas, examples) | ✅ Yes — each gets its own `vN/` subfolder | `architecture/scripts/v1/`, `architecture/patterns/v1/`, `_shared/spec-driven-audit/v1/` |
| **Navigation docs** (dispatchers, indexes, READMEs, this VERSIONING.md) | ❌ No — always reflect current design | `SKILL.md`, `README.md`, `VERSIONING.md`, `architecture/SKILL.md` |

Rule of thumb: if it describes **what to do**, version it. If it describes **how to navigate**, don't.

## Folder shape

Every content module — whether it holds multiple files or a single doc — lives inside its own folder with `vN/` subfolders:

### Multi-file modules (folders that hold related files)

```
architecture/patterns/
├── v1/
│   ├── storage-exception.md
│   ├── cross-layer-reads-tracking.md
│   └── hardware-gaps-tracking.md
└── v2/                                  ← future, after improvements
    ├── storage-exception.md             (revised)
    ├── cross-layer-reads-tracking.md    (unchanged copy from v1, optional)
    └── hardware-gaps-tracking.md
```

### Single-doc modules (one concept = one doc)

```
architecture/conventions-schema/
├── v1/
│   └── conventions-schema.md
└── v2/                                  ← future
    └── conventions-schema.md            (revised)
```

The single doc is wrapped in a folder of the same name so the versioning shape stays uniform.

### Top-level (unversioned)

```
skills/diagram/
├── SKILL.md                             ← unversioned (dispatcher)
├── README.md                            ← unversioned (overview)
├── VERSIONING.md                        ← unversioned (this file)
├── _shared/
├── architecture/
└── _project-template/
```

Sub-skill entries (e.g. `architecture/SKILL.md`) are also **unversioned** because they describe how to navigate the sub-skill's versioned content.

## Default version: latest = highest `vN`

**Convention:** the latest version is the subfolder with the highest `vN` number.

```
architecture/scripts/
├── v1/
├── v2/
└── v3/             ← LATEST · used by default
```

An agent following a cross-reference like `architecture/scripts/` should:

1. List subfolders matching pattern `v\d+`
2. Pick the one with the **highest number**
3. Read content from that subfolder

No `LATEST` pointer file needed — convention is self-documenting via filesystem.

## How to pin to a specific version

When a user needs an older version (e.g. their project was built on v1 of scripts and they don't want to migrate yet), they can:

### From outside the skill (project usage)

In their project's `diagram-conventions.md`, add a Pinning section:

```markdown
## Skill version pinning

This project uses the following pinned versions (override the skill's default "latest" behavior):

- `architecture/scripts`: **v1** (we depend on `compute-row-layout.py` v1 signature)
- `architecture/patterns`: default (latest)
- `_shared/spec-driven-audit`: **v2** (matches our spec audit workflow)
```

The skill reads this section before applying defaults.

### From inside a conversation (one-off request)

User says: "Use v1 of architecture/scripts for this session" → agent reads from `architecture/scripts/v1/` instead of the latest.

### In cross-references (within skill content)

A versioned doc can explicitly pin a reference:

```markdown
For the legacy pattern, see [`v1/storage-exception.md`](../patterns/v1/storage-exception.md).
```

Otherwise, references default to the leaf folder path (latest):

```markdown
See [`storage-exception`](../patterns/) for the storage exception pattern.
```

## Cross-reference convention

**Inside versioned content**, when linking to another versioned module:

| Goal | Link style |
|---|---|
| Always latest of the referenced module (default) | `path/to/leaf-folder/` (no `vN`) |
| Specific version of the referenced module | `path/to/leaf-folder/vN/file.md` |

Example — `architecture/conventions-schema/v1/conventions-schema.md` referring to patterns:

```markdown
✅ Latest: see [`architecture/patterns/`](../../patterns/)
✅ Pinned: see [`architecture/patterns/v1/storage-exception.md`](../../patterns/v1/storage-exception.md)
```

## How to bump a version

When you need to update a content module without losing the old version:

### Step 1 · Copy current to next

```bash
cp -r architecture/scripts/v1 architecture/scripts/v2
```

### Step 2 · Modify v2 only

Apply your changes inside `v2/`. Leave `v1/` untouched.

### Step 3 · Update changelog

Add a `CHANGELOG.md` at the leaf folder level (next to `vN/` subfolders) if not already present:

```markdown
# architecture/scripts — changelog

## v2 (YYYY-MM-DD)
- Added `align-cells-in-column.py` for vertical alignment
- `compute-row-layout.py`: now supports non-uniform gap arrays
- Breaking: `add-edge.py` parameter renamed `EDGE_STYLE` → `STYLE_PRESET`

## v1 (YYYY-MM-DD)
- Initial release
```

### Step 4 · Decide downstream pin

For each consumer of this module:

- **If v2 is backward-compatible** → leave their references to the leaf folder (auto-latest pickup)
- **If v2 breaks something** → consumers stay on v1 by pinning their reference: `path/v1/file.md`

The decision lives in the consumer's content, not in the bumped module.

### Step 5 · No DELETE of old versions

Old versions remain available indefinitely. Don't delete `v1/` even if "everyone uses v2 now" — projects pinned to v1 still need it.

Deletion is only acceptable when **no projects in the org use the old version anymore** and you've confirmed externally. Document the deletion in CHANGELOG.

## Bumping a multi-file module · what counts as a "version"

If `architecture/scripts/v1/` has 4 files and you only change 1:

**Option A — Full snapshot:** copy all 4 into `v2/`, modify the one. v2 has 4 files (3 identical to v1, 1 new).
- Pros: self-contained, easy to navigate
- Cons: duplication in storage (but text files are tiny)

**Option B — Selective:** put only the changed file in `v2/`, others still in `v1/`. Consumers reading `architecture/scripts/` get latest-of-each via per-file resolution.
- Cons: complex resolution logic, breaks "version = snapshot" semantic

**Default: Option A.** Each `vN/` is a complete snapshot of the module at that version. Disk cost is negligible.

## Why per-leaf-folder grain (not per-sub-skill grain)?

User-requested rationale: maximum flexibility. Bumping `architecture/scripts` shouldn't force `architecture/patterns` to also bump. Each module evolves on its own cadence.

Coarser-grain (per-sub-skill) would force every file in `architecture/` to bump when one tiny script changes. Per-leaf-folder grain avoids that.

## Why not per-FILE grain?

We could go even finer: `architecture/scripts/compute-row-layout/v1/compute-row-layout.py`. But:
- More folder nesting (worse readability)
- Files within a module usually evolve together (related concepts)
- Filesystem becomes harder to navigate visually

Per-leaf-folder is the right compromise.

## Summary

| Question | Answer |
|---|---|
| Where do versions live? | Every leaf content folder has `vN/` subfolders |
| Which version is used by default? | Highest `vN` (convention) |
| Can users pin to older versions? | Yes · via `diagram-conventions.md` Pinning section · or one-off in conversation |
| Are SKILL.md and READMEs versioned? | No · always reflect current design |
| How do I bump a version? | Copy `v(N)/` to `v(N+1)/`, modify, update CHANGELOG · don't delete old versions |
| Cross-reference default | Leaf folder path (latest) · pin explicitly when needed |
