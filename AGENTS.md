# AGENTS.md

Instructions for any AI coding agent (Claude Code, Codex, Cursor, Gemini CLI, Copilot) working in this repository. Humans: see [CONTRIBUTING.md](CONTRIBUTING.md).

## What this repo is

A public, 36-week curriculum that takes a learner from zero to a hireable **Forward Deployed ML Engineer (FDE)**. It is grounded in real FDE job postings and built around five capstones. Owner: Sunday Ayandele. Licence: CC BY-SA 4.0.

The repo is **content, not software**. The scripts exist only to keep the content consistent.

## The one rule: CURRICULUM.md is the source of truth

| Path | Who edits it | Notes |
| --- | --- | --- |
| `CURRICULUM.md` | **Edit here** | Every phase, capstone, market table, rubric and source |
| `phases/*/README.md` | Generated | Rebuilt by `scripts/build.py`; carries a GENERATED banner |
| `capstones/*/README.md` | Generated | Same |
| `docs/market-research.md`, `docs/interview-prep.md`, `docs/rubric.md`, `docs/sources.md` | Generated | Same; the decomposition framework text lives in `scripts/build.py` |
| `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `templates/`, `tools/README.md` | Edit directly | Hand-written |
| `tools/FDE_Skills_Matrix_90_Day_Plan.xlsx` | Edit with care | Formula-driven; keep formulas, don't paste values over them |
| `assets/roadmap.png` | Replace only if phases or weeks change | Must match the phase table in CURRICULUM.md |
| `lms/videos.json` | Edit directly | Curated weekly videos. Feeds the Watch section of each phase page (run the build) and the Moodle Watch pages. Check with `python lms/check_videos.py` before committing |

Never edit a generated file by hand. Change `CURRICULUM.md`, then run the build.

## Commands

```bash
python scripts/build.py              # regenerate phases/, capstones/, docs/
python scripts/check_repo.py         # build --check + relative links (run before every commit)
python scripts/check_links.py --external   # also test every external URL (slow, needs network)
```

Python 3.9+ standard library only. No dependencies to install.

## Structure CURRICULUM.md must keep

`scripts/build.py` parses headings, so keep this shape:

- `## Phases 0–1: Foundations (…)` containing `### Phase 0: …` and `### Phase 1: …`
- `## Phase N: <name> (weeks a–b)` for phases 2–7
- Inside a phase: `### Capstone N: <name>` (or `### Capstone N (flagship): …`)
- `## What the market asks for`, `## Capstone rubric and evidence checklist`, `## Sources`
- Phase 7 must contain `### Interview loop preparation`

Folder names for phases and capstones are fixed in `PHASE_SLUGS` and `CAPSTONE_SLUGS` in `scripts/build.py`, so renaming a heading never breaks links in learners' forks. Add a new slug there when adding a phase or capstone.

## Writing style

- Lead each section with its point; first sentence = the answer, with a number where possible.
- Short sentences (under 25 words), plain words, British spelling to match the existing text ("organisation", "behaviour").
- Weekly plans are tables: `| Week | Topic | What you do |`.
- Every capstone has **Brief**, **Must include**, **Definition of done**, **Proves** in that order. "Proves" names the postings that ask for it.
- Prefer free, current, widely used resources. Name the resource exactly; no affiliate links.
- No hype words ("revolutionary", "cutting-edge"), no emoji.

## Facts and sources

- Anything about the job market (who is hiring, requirements, salaries, interview loops) must come from a page you actually opened, cited in `## Sources`. A search snippet is not a source.
- Postings close. Keep closed postings only as evidence of requirements and say so; never present them as open roles.
- Update the `Last reviewed: YYYY-MM-DD` line at the top of `CURRICULUM.md` and add a `CHANGELOG.md` entry whenever content changes.
- Tool and library names drift (vLLM, TRL, PEFT, LangGraph, MCP). Check current docs before naming a version or API.

## Definition of done for any change

1. `CURRICULUM.md` edited (not generated files).
2. `python scripts/build.py` run.
3. `python scripts/check_repo.py` passes.
4. `CHANGELOG.md` has an entry under `## [Unreleased]` and `Last reviewed` is today if content changed.
5. If phases or weeks changed: README phase table and `assets/roadmap.png` still match.

## Don'ts

- Don't commit secrets, model weights or datasets (see `.gitignore`).
- Don't rename phase or capstone folders.
- Don't delete the GENERATED banner or hand-edit below it.
- Don't push or open PRs unless the owner asks; he commits with GitHub Desktop.
