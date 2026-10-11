---
description: Run the monthly curriculum refresh - job market, resources, rebuild, checks and changelog
argument-hint: "[optional focus, e.g. 'market only' or 'Phase 5']"
---

Run the monthly refresh of the Forward Deployed ML Engineer curriculum in this repository.

Focus from the user (may be empty): $ARGUMENTS

Work through these steps in order, tracking them in a task list. If a focus is given, do only the steps it covers plus steps 4–6.

1. **Baseline.** Run `python scripts/check_repo.py` and read the `Last reviewed` date and the `## [Unreleased]` section of `CHANGELOG.md`, so you know where things stand.
2. **Market.** Follow the `refresh-fde-market` skill. Delegate searching and page verification to the `fde-market-researcher` agent.
3. **Resources.** Follow the `audit-resources` skill, starting with `python scripts/check_links.py --external`.
4. **Gaps.** If steps 2–3 surfaced curriculum gaps, propose specific edits (phase, week, wording) and ask the owner before making changes larger than a few lines. Small, clearly evidenced fixes can go ahead via the `update-curriculum` skill.
5. **Review.** Ask the `curriculum-reviewer` agent to review the full diff. Fix what it flags.
6. **Release prep.** Follow the `release-update` skill: rebuild, check, finalise the changelog, update dates, and hand over the commit message.

End with a short report: what changed, what was left as "watch", open questions for the owner, and the commit message.
