#!/usr/bin/env python3
"""Check links in every Markdown file.

Usage:
    python scripts/check_links.py              # relative links only (fast, offline)
    python scripts/check_links.py --external   # also request every http(s) link

Exit code 1 if a relative link is broken or an external link returns 404/410.
Job boards often block bots (403/429) or close postings; those are reported as
warnings for a human or agent to review, not failures.
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\]\(([^)\s]+)\)")
SKIP_DIRS = {".git", "node_modules", ".venv", "venv"}
USER_AGENT = "Mozilla/5.0 (compatible; fde-zero-to-hired-linkcheck/1.0)"


def markdown_files() -> list[Path]:
    return [p for p in ROOT.rglob("*.md") if not SKIP_DIRS & set(p.relative_to(ROOT).parts)]


def links_in(path: Path) -> list[str]:
    text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)  # inline code holds examples, not real links
    return LINK.findall(text)


def check_external(url: str) -> tuple[str, int | None, str]:
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=15) as resp:
                return url, resp.status, ""
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 501):
                continue  # some servers reject HEAD; retry with GET
            return url, e.code, e.reason
        except Exception as e:  # network error, timeout, TLS
            if method == "HEAD":
                continue
            return url, None, str(e)
    return url, None, "unreachable"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--external", action="store_true", help="also check http(s) links")
    args = parser.parse_args()

    broken: list[str] = []
    external: dict[str, list[str]] = {}
    count = 0
    for md in markdown_files():
        rel_md = md.relative_to(ROOT)
        for link in links_in(md):
            if link.startswith(("http://", "https://")):
                external.setdefault(link, []).append(str(rel_md))
                continue
            if link.startswith(("#", "mailto:")) or "<" in link:
                continue
            count += 1
            target = (md.parent / urllib.parse.unquote(link.split("#")[0])).resolve()
            if not target.exists():
                broken.append(f"{rel_md}: {link}")

    print(f"relative links: {count} checked, {len(broken)} broken")
    for b in broken:
        print(f"  BROKEN {b}", file=sys.stderr)

    dead: list[str] = []
    if args.external:
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(check_external, external))
        warn = []
        for url, status, reason in results:
            where = ", ".join(sorted(set(external[url])))
            if status in (404, 410):
                dead.append(f"{status} {url}  (in {where})")
            elif status is None or status >= 400:
                warn.append(f"{status or 'ERR'} {url}  {reason}  (in {where})")
        print(f"external links: {len(external)} checked, {len(dead)} dead, {len(warn)} to review")
        for d in dead:
            print(f"  DEAD   {d}", file=sys.stderr)
        for w in warn:
            print(f"  REVIEW {w}")

    return 1 if broken or dead else 0


if __name__ == "__main__":
    sys.exit(main())
