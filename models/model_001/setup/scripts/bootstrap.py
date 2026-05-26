#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bootstrap.py — scaffold BA workspace từ model_001 templates.

Usage:
  python bootstrap.py [--force] [--workdir PATH]

Hành vi:
- Detect working folder (folder cha của MasterMind/)
- Tạo input/, context/, output/, docs/, conventions/
- Copy CLAUDE.md + templates/docs/* + templates/conventions/* vào working folder
- Idempotent: không overwrite trừ khi --force
"""
import argparse
import os
import shutil
import sys


def find_working_folder(start=None):
    """Working folder = folder chứa subfolder MasterMind/.
    Search up từ cwd hoặc start."""
    p = os.path.abspath(start or os.getcwd())
    for _ in range(20):
        if os.path.isdir(os.path.join(p, "MasterMind")):
            return p
        if os.path.basename(p) == "MasterMind":
            return os.path.dirname(p)
        if os.path.isdir(os.path.join(p, "skills", "MasterMind")):
            return p
        parent = os.path.dirname(p)
        if parent == p:
            break
        p = parent
    return os.path.abspath(os.getcwd())


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--force", action="store_true",
                        help="Overwrite existing files")
    parser.add_argument("--workdir",
                        help="Override working folder detection")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    templates_root = os.path.normpath(os.path.join(script_dir, "..", "templates"))
    if not os.path.isdir(templates_root):
        print(f"❌ Templates folder không tồn tại: {templates_root}", file=sys.stderr)
        sys.exit(1)

    workdir = args.workdir or find_working_folder()
    print(f"📂 Working folder: {workdir}\n")

    created, skipped = [], []

    # ── Create base directories ──
    for d in ["input", "context", "output", "docs", "conventions"]:
        path = os.path.join(workdir, d)
        if not os.path.isdir(path):
            os.makedirs(path)
            created.append(("dir", d + "/"))
        else:
            skipped.append(("dir", d + "/", "exists"))

    # ── Copy template files ──
    for root, _, files in os.walk(templates_root):
        for f in sorted(files):
            src = os.path.join(root, f)
            rel = os.path.relpath(src, templates_root).replace(os.sep, "/")
            dst = os.path.join(workdir, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            if os.path.exists(dst) and not args.force:
                skipped.append(("file", rel, "exists"))
                continue
            shutil.copy2(src, dst)
            created.append(("file", rel))

    # ── Report ──
    print(f"✓ Created {len(created)} items:")
    for kind, *rest in created:
        icon = "📁" if kind == "dir" else "📄"
        print(f"  {icon} {rest[0]}")
    if skipped:
        print(f"\n○ Skipped {len(skipped)}:")
        for kind, name, reason in skipped:
            icon = "📁" if kind == "dir" else "📄"
            print(f"  {icon} {name} ({reason})")
    print()
    print("📖 Next steps:")
    print(f"  1. Read {os.path.join(workdir, 'CLAUDE.md')}")
    print(f"  2. Drop raw input materials into {os.path.join(workdir, 'input/')}")
    print(f"  3. Open docs/*.md → ask Claude to fill (agent picks model_001 skill)")
    print(f"  4. Optional: fill conventions/<skill>-conventions.md để override defaults")


if __name__ == "__main__":
    main()
