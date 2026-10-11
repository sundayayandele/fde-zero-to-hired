---
name: update-curriculum
description: Make any content change to the Zero-to-Hired curriculum (phases, weekly topics, resources, capstones, rubric, templates) the safe way, editing CURRICULUM.md and regenerating pages. Use whenever asked to add, change, reorder or remove curriculum content in this repo.
---

# Update the curriculum

## Where to edit

- **Phases, weeks, resources, capstones, rubric, market, sources:** `CURRICULUM.md` only. The pages in `phases/`, `capstones/` and the four generated `docs/` files are rebuilt from it.
- **Templates, README, CONTRIBUTING, tools/README:** edit directly.
- **Decomposition framework and practice prompts:** the `DECOMPOSITION_FRAMEWORK` constant in `scripts/build.py`.

## Steps

1. **Understand the request.** Which phase or capstone, and why (new market evidence, learner feedback, outdated tool)? If the change is larger than a few lines, propose it to the owner first.
2. **Keep the structure** described in `AGENTS.md` (headings `build.py` depends on). Phase and capstone headings keep their numbers.
3. **Write in house style:** point first, short sentences, British spelling, weekly plans as `| Week | Topic | What you do |` tables, capstones as Brief → Must include → Definition of done → Proves.
4. **Keep the arithmetic consistent.** If you change weeks in one phase, shift the following phases, the total in "How to use this curriculum" (36 weeks), the README phase table, and note that `assets/roadmap.png` needs regenerating.
5. **Keep the capstone chain intact.** Each capstone reuses the previous one; the flagship (Capstone 5) combines 1–4. Changing one capstone's outputs may require updating the next.
6. **Resources:** prefer free, current, widely used material. Check a resource exists and is current before adding it (open the page).
7. **Rebuild and check:**

   ```bash
   python scripts/build.py
   python scripts/check_repo.py
   ```

8. **Record it:** add a line under `## [Unreleased]` in `CHANGELOG.md` and set `Last reviewed: <today>` at the top of `CURRICULUM.md`.
9. **Review:** for non-trivial changes, ask the `curriculum-reviewer` agent to review the diff before handing back.

## New phase or capstone

Add its slug to `PHASE_SLUGS` or `CAPSTONE_SLUGS` in `scripts/build.py` (and templates to `CAPSTONE_TEMPLATES`), then add a row to the README phase table. Never rename existing slugs; learners' forks link to them.

## Hand back

A short summary of what changed and why, the files touched, and a suggested commit message, for example `Phase 4: add ORPO lab and update TRL resources`.
