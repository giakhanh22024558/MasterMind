"""
Scaffold a new skill in `skills/` by copying the `template/v1/` starter
and renaming placeholders.

USE CASE:
  - You want to create a new skill (e.g. `business_analysis`, `code_review`,
    `data_modeling`) following the uniform structure
  - Manually copying + renaming is error-prone and tedious

WHAT IT DOES:
  1. Copies `template/v1/` to `skills/<new-skill-name>/`
  2. Renames placeholder strings (`<skill-name>`, `<SKILL_NAME>`) in all files
  3. Reports the structure created · next steps

CONFIGURATION:
  Edit CONFIG block below for your new skill.
"""
import shutil
from pathlib import Path

# ─── CONFIG ────────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parents[3]   # MasterMind/
SKILLS_ROOT = REPO_ROOT / "skills"
TEMPLATE_DIR = REPO_ROOT / "template" / "v1"

NEW_SKILL_NAME = "business_analysis"           # ← change to your skill name (snake_case)
NEW_SKILL_DESCRIPTION = (
    "Capture, analyze, and document business requirements and stakeholder needs. "
    "Use when eliciting requirements, mapping stakeholders, modeling business "
    "processes, or producing BA artifacts."
)


# ─── EXECUTION ────────────────────────────────────────────────────────────────

def main():
    template_dir = TEMPLATE_DIR
    new_skill_dir = SKILLS_ROOT / NEW_SKILL_NAME

    if not template_dir.exists():
        raise SystemExit(f"Template not found at {template_dir}")

    if new_skill_dir.exists():
        raise SystemExit(f"Skill {NEW_SKILL_NAME!r} already exists at {new_skill_dir}")

    # 1. Copy template
    shutil.copytree(template_dir, new_skill_dir)
    print(f"✅ Copied template → {new_skill_dir}")

    # 2. Rename placeholders in all .md files
    replacements = {
        "<skill-name>": NEW_SKILL_NAME,
        "<SKILL_NAME>": NEW_SKILL_NAME.upper().replace("_", " "),
        "<skill description here>": NEW_SKILL_DESCRIPTION,
    }

    updated = 0
    for md_file in new_skill_dir.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        new_content = content
        for placeholder, value in replacements.items():
            new_content = new_content.replace(placeholder, value)
        if new_content != content:
            md_file.write_text(new_content, encoding="utf-8")
            updated += 1

    print(f"✅ Updated {updated} files with skill name {NEW_SKILL_NAME!r}")

    # 3. Report next steps
    print()
    print("━" * 60)
    print(f"NEXT STEPS for completing {NEW_SKILL_NAME!r}:")
    print("━" * 60)
    print(f"1. Read {new_skill_dir / 'SKILL.md'} and fill in the workflow templates")
    print(f"2. Define your skill's conventions in {new_skill_dir / 'conventions-schema' / 'v1'}")
    print(f"3. Provide sensible defaults in {new_skill_dir / 'conventions-defaults' / 'v1'}")
    print(f"4. Add at least one pattern in {new_skill_dir / 'patterns' / 'v1'}")
    print(f"5. Add at least one worked walkthrough in {new_skill_dir / 'examples' / 'v1'}")
    print(f"6. Update {SKILLS_ROOT / 'README.md'} 'Currently implemented' table")
    print(f"7. (Optional) Add scripts in {new_skill_dir / 'scripts' / 'v1'}")
    print()
    print("Reference meta-patterns from `meta/` (at repo root) for:")
    print("  - Versioning model: meta/versioning-pattern/")
    print("  - Conventions as data: meta/conventions-as-data-pattern/")
    print("  - Defer-then-promote: meta/defer-then-promote-pattern/")
    print("  - Atomic edits: meta/atomic-edits-pattern/")


if __name__ == "__main__":
    main()
