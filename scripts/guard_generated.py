#!/usr/bin/env python3
"""Claude Code PostToolUse hook: warn when a generated file is edited directly.

phases/, capstones/ and the generated docs/ files are rebuilt from CURRICULUM.md,
so direct edits are overwritten on the next build. Exit code 2 sends the warning
back to Claude so it moves the change into CURRICULUM.md instead.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GENERATED_DOCS = {"market-research.md", "interview-prep.md", "rubric.md", "sources.md"}


def is_generated(path: Path) -> bool:
    try:
        rel = path.resolve().relative_to(ROOT)
    except ValueError:
        return False
    parts = rel.parts
    if parts and parts[0] in ("phases", "capstones") and rel.name == "README.md":
        return True
    return len(parts) == 2 and parts[0] == "docs" and rel.name in GENERATED_DOCS


def main() -> int:
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        return 0
    file_path = (payload.get("tool_input") or {}).get("file_path")
    if file_path and is_generated(Path(file_path)):
        print(
            f"{file_path} is generated from CURRICULUM.md and will be overwritten. "
            "Make this change in CURRICULUM.md instead, then run `python scripts/build.py`.",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
