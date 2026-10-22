#!/usr/bin/env python3
"""Fast consistency check: generated files match CURRICULUM.md and relative links resolve.

Run it yourself before committing:
    python scripts/check_repo.py

It is also the Claude Code Stop hook in the fde-maintainer plugin, run as
`check_repo.py --hook`. In hook mode it reads the hook JSON from stdin, exits 2
on failure so Claude sees the problem and fixes it before finishing, and steps
aside if it has already blocked once this turn.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    hook_mode = "--hook" in sys.argv[1:]
    if hook_mode:
        try:
            payload = json.loads(sys.stdin.read() or "{}")
        except json.JSONDecodeError:
            payload = {}
        if payload.get("stop_hook_active"):
            return 0  # already blocked once this turn; don't loop

    problems = []
    checks = (("scripts/build.py", ["--check"]), ("scripts/check_links.py", []),
              ("lms/check_videos.py", ["--schema"]))
    for script, args in checks:
        result = subprocess.run([sys.executable, str(ROOT / script), *args],
                                capture_output=True, text=True, cwd=ROOT)
        if result.returncode != 0:
            problems.append(f"[{script}]\n{result.stderr.strip() or result.stdout.strip()}")

    if not problems:
        if not hook_mode:
            print("check_repo: OK")
        return 0

    message = ("Repository is inconsistent. Fix before finishing:\n\n" + "\n\n".join(problems) +
               "\n\nGenerated files: edit CURRICULUM.md, then run `python scripts/build.py`.")
    print(message, file=sys.stderr)
    return 2 if hook_mode else 1


if __name__ == "__main__":
    sys.exit(main())
