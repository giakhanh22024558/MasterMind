# context/

**Agent-managed** `.md` sidecars for every file in `input/` and `output/`.

## Purpose

Reading `.md` is much cheaper than reading `.docx` / `.xlsx` (~10x token savings). Every binary file must have one matching sidecar in this folder.

## Convention

```
input/SRS_v1.docx          → context/SRS_v1.md
input/Issues_MS1.xlsx      → context/Issues_MS1.md
output/<project>-SRS.docx  → context/<project>-SRS.md
```

The agent creates a sidecar automatically when:
- Reading a binary file for the first time (`"read context of <file>"`)
- Producing a binary output (`"render SRS"` → also creates the sidecar)
- The user triggers an explicit sync (`"sync drive"`, `"refresh context"`)

## Rules

- ❌ User does NOT edit these manually — they get overwritten on the next sync
- ✅ User only READS them for reference
- ✅ Agent overwrites when a new version of the source appears
- ❌ Do not commit this folder into the MasterMind git repo — it is per-project, not skill content
