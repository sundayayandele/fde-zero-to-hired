#!/usr/bin/env python3
"""Regenerate phases/, capstones/ and docs/ from CURRICULUM.md.

CURRICULUM.md is the single source of truth. Every file this script writes
starts with a GENERATED banner; never edit those files by hand.

Usage:
    python scripts/build.py           # rewrite generated files
    python scripts/build.py --check   # exit 1 if generated files are out of date
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "CURRICULUM.md"
BANNER = (
    "<!-- GENERATED from CURRICULUM.md by scripts/build.py. "
    "Do not edit by hand: edit CURRICULUM.md, then run `python scripts/build.py`. -->\n\n"
)

# Stable folder names. Keep these so links from README and learners' forks keep working.
PHASE_SLUGS = {
    0: "00-programming-and-tooling",
    1: "01-swe-and-ml-foundations",
    2: "02-llm-application-engineering",
    3: "03-evaluation-and-reliability",
    4: "04-model-customization",
    5: "05-inference-and-sovereign-ai",
    6: "06-forward-deployed-practice",
    7: "07-getting-hired",
}
CAPSTONE_SLUGS = {
    1: "01-enterprise-document-assistant",
    2: "02-eval-harness-and-red-team",
    3: "03-domain-fine-tune",
    4: "04-sovereign-deployment",
    5: "05-flagship-pilot",
}
CAPSTONE_TEMPLATES = {
    1: ["capstone-README.md", "customer-brief.md"],
    2: ["capstone-README.md", "customer-brief.md", "eval-report.md"],
    3: ["capstone-README.md", "decision-memo.md", "data-card.md", "model-card.md"],
    4: ["capstone-README.md", "customer-brief.md"],
    5: ["capstone-README.md", "customer-brief.md", "decision-memo.md", "case-study.md"],
}
DECOMPOSITION_FRAMEWORK = """## Decomposition case framework

Work through these out loud, asking the interviewer (the "customer") at each step:

1. **Goal:** what business outcome changes if this works? How is it measured today?
2. **Users:** who uses it, how often, and what do they do now instead?
3. **Data:** what exists, where, in what shape, who owns it, what is sensitive?
4. **Constraints:** latency, cost, privacy, regulation, deployment environment, timeline.
5. **Options:** at least two approaches (for example prompting vs RAG vs fine-tuning) with trade-offs.
6. **MVP:** the smallest pilot that proves value in 2–6 weeks.
7. **Metric:** the success bar agreed before building, and how you will measure it.
8. **Risks:** what could fail, and the fallback for each.

## Practice prompts

- "Our claims team takes 3 days to triage a claim. Can AI help?"
- "We want a chatbot over our internal policies, but legal is worried."
- "Our RAG pilot works in the demo but users say answers are wrong."
- "A bank wants our model but no data can leave their data centre."
- "Leadership wants to fine-tune our own model. Should we?"
"""


class BuildError(Exception):
    pass


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def sections(md: str, level: int) -> list[tuple[str, str]]:
    """Split markdown into (heading, body) pairs at exactly `level`, ignoring code fences."""
    lines = md.split("\n")
    out: list[tuple[str, list[str]]] = []
    in_code = False
    prefix = "#" * level + " "
    for line in lines:
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and line.startswith(prefix):
            out.append((line[len(prefix):].strip(), []))
        elif out:
            out[-1][1].append(line)
    return [(h, "\n".join(b).strip()) for h, b in out]


def intro_and_subsections(body: str) -> tuple[str, list[tuple[str, str]]]:
    match = re.search(r"^### ", body, re.M)
    intro = body[: match.start()].strip() if match else body.strip()
    return intro, sections(body, 3)


def find_h2(h2: list[tuple[str, str]], prefix: str) -> tuple[str, str]:
    for heading, body in h2:
        if heading.startswith(prefix):
            return heading, body
    raise BuildError(f'CURRICULUM.md has no "## {prefix}…" section')


def short(title: str) -> str:
    return title.split(" (")[0]


def phase_number(title: str) -> int:
    m = re.match(r"Phase (\d+)", title)
    if not m:
        raise BuildError(f"Cannot read phase number from heading: {title!r}")
    return int(m.group(1))


def capstone_number(title: str) -> int | None:
    m = re.match(r"Capstone (\d+)", title)
    return int(m.group(1)) if m else None


def nav(prev: tuple[str, str] | None, nxt: tuple[str, str] | None) -> str:
    parts = []
    if prev:
        parts.append(f"← [{prev[1]}](../{prev[0]}/README.md)")
    parts.append("[Home](../../README.md)")
    if nxt:
        parts.append(f"[{nxt[1]}](../{nxt[0]}/README.md) →")
    return " · ".join(parts)


def render(text: str) -> dict[Path, str]:
    """Return {relative path: content} for every generated file."""
    h2 = sections(text, 2)
    files: dict[Path, str] = {}

    # ---- Phases ---------------------------------------------------------
    phases: list[dict] = []
    for heading, body in h2:
        if heading.startswith("Phases "):  # grouped phases share one intro
            shared_intro, subs = intro_and_subsections(body)
            for sub_heading, sub_body in subs:
                if sub_heading.startswith("Phase "):
                    phases.append({"title": sub_heading, "intro": shared_intro + "\n\n" + sub_body, "subs": []})
        elif heading.startswith("Phase "):
            intro, subs = intro_and_subsections(body)
            phases.append({"title": heading, "intro": intro, "subs": subs})
    if not phases:
        raise BuildError("No phases found in CURRICULUM.md")

    for p in phases:
        n = phase_number(p["title"])
        p["num"] = n
        p["slug"] = PHASE_SLUGS.get(n) or f"{n:02d}-{slugify(short(p['title']).split(':', 1)[-1])}"
    phases.sort(key=lambda p: p["num"])

    capstones: list[dict] = []
    for i, p in enumerate(phases):
        prev = (phases[i - 1]["slug"], short(phases[i - 1]["title"])) if i else None
        nxt = (phases[i + 1]["slug"], short(phases[i + 1]["title"])) if i + 1 < len(phases) else None
        out = [f"# {p['title']}", "", nav(prev, nxt), "", p["intro"]]
        for sub_heading, sub_body in p["subs"]:
            cnum = capstone_number(sub_heading)
            if cnum is not None:
                cslug = CAPSTONE_SLUGS.get(cnum) or f"{cnum:02d}-{slugify(sub_heading.split(':', 1)[-1])}"
                capstones.append({"num": cnum, "title": sub_heading, "body": sub_body, "slug": cslug, "phase": p})
                out += ["", f"## Capstone {cnum}", "",
                        f"This phase ends with **[{sub_heading}](../../capstones/{cslug}/README.md)**. "
                        "Read the brief before week 1 of the phase so you build towards it."]
            else:
                out += ["", f"## {sub_heading}", "", sub_body]
        out += ["", "---", "", nav(prev, nxt), ""]
        files[Path("phases") / p["slug"] / "README.md"] = BANNER + "\n".join(out)

    # ---- Capstones ------------------------------------------------------
    capstones.sort(key=lambda c: c["num"])
    for j, c in enumerate(capstones):
        prev = (capstones[j - 1]["slug"], f"Capstone {capstones[j - 1]['num']}") if j else None
        nxt = (capstones[j + 1]["slug"], f"Capstone {capstones[j + 1]['num']}") if j + 1 < len(capstones) else None
        templates = CAPSTONE_TEMPLATES.get(c["num"], ["capstone-README.md", "customer-brief.md"])
        out = [
            f"# {c['title']}", "", nav(prev, nxt), "",
            f"Built during [{short(c['phase']['title'])}](../../phases/{c['phase']['slug']}/README.md).", "",
            c["body"], "",
            "## Templates to use", "",
            "\n".join(f"- [{t}](../../templates/{t})" for t in templates), "",
            "## Submit", "",
            "1. Publish your capstone in its own public repo, using the [capstone README template](../../templates/capstone-README.md).",
            "2. Score it against the [rubric](../../docs/rubric.md): pass at 14/20 with no criterion below 2.",
            "3. Open a **Capstone submission** issue in your fork of this repo with the links.",
            "", "---", "", nav(prev, nxt), "",
        ]
        files[Path("capstones") / c["slug"] / "README.md"] = BANNER + "\n".join(out)

    # ---- docs/ ----------------------------------------------------------
    def doc(name: str, title: str, body: str, lead: str = "") -> None:
        files[Path("docs") / name] = BANNER + f"# {title}\n\n[Home](../README.md)\n\n{lead}{body}\n"

    _, market = find_h2(h2, "What the market asks for")
    doc("market-research.md", "What the market asks for", market)

    hired = next((p for p in phases if p["num"] == 7), None)
    interview = next((b for h, b in (hired["subs"] if hired else []) if h.startswith("Interview loop")), None)
    if interview is None:
        raise BuildError('Phase 7 needs a "### Interview loop preparation" subsection')
    doc("interview-prep.md", "Interview loop preparation", interview + "\n\n" + DECOMPOSITION_FRAMEWORK,
        "FDE loops combine coding, a live decomposition case, a technical deep-dive, LLM system design "
        "and a values round. The decomposition round is usually the deciding one.\n\n")

    rubric_title, rubric = find_h2(h2, "Capstone rubric")
    doc("rubric.md", rubric_title, rubric)
    _, sources = find_h2(h2, "Sources")
    doc("sources.md", "Sources", sources)
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="only report files that are out of date")
    args = parser.parse_args()

    try:
        files = render(SOURCE.read_text(encoding="utf-8"))
    except BuildError as e:
        print(f"build: {e}", file=sys.stderr)
        return 1

    # Generated files that exist on disk but would no longer be produced (renamed/removed sections).
    existing = {p.relative_to(ROOT) for d in ("phases", "capstones") for p in (ROOT / d).rglob("README.md")}
    orphans = sorted(existing - set(files))

    stale = [rel for rel, content in files.items()
             if not (ROOT / rel).exists() or (ROOT / rel).read_text(encoding="utf-8") != content]

    if args.check:
        if stale or orphans:
            for rel in stale:
                print(f"out of date: {rel}", file=sys.stderr)
            for rel in orphans:
                print(f"orphaned (no longer in CURRICULUM.md): {rel}", file=sys.stderr)
            print("Run: python scripts/build.py", file=sys.stderr)
            return 1
        print(f"build: {len(files)} generated files are up to date")
        return 0

    for rel in stale:
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(files[rel], encoding="utf-8")
        print(f"wrote {rel}")
    for rel in orphans:
        print(f"warning: {rel} is no longer generated; delete it if the section was removed", file=sys.stderr)
    print(f"build: {len(stale)} updated, {len(files) - len(stale)} unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
