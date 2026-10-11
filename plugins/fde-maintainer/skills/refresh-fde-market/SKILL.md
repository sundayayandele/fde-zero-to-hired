---
name: refresh-fde-market
description: Refresh the "What the market asks for" table and Sources in CURRICULUM.md with current, verified Forward Deployed Engineer job postings. Use when asked to update the job market, add new FDE roles, check which postings closed, or during the monthly refresh.
---

# Refresh the FDE job-market evidence

The market table in `CURRICULUM.md` is the curriculum's evidence base. Every row must point to a posting you actually opened.

## 1. Read what is there

- Read `## What the market asks for` and `## Sources` in `CURRICULUM.md`.
- Note the `Last reviewed` date at the top, the four families (ML-heavy, API / agent, Platform / private deploy, Classic data FDSE) and the companies already covered.

## 2. Find candidates

Delegate the search to the `fde-market-researcher` agent if it is available; otherwise search yourself. Search in one batch, for example:

- `"forward deployed engineer" AI job <current month> <current year>`
- `"forward deployed" machine learning engineer fine-tuning`
- `"applied AI engineer" forward deployed site:jobs.lever.co OR site:job-boards.greenhouse.io OR site:jobs.ashbyhq.com`
- Each company already in the table plus "forward deployed engineer" to see if the role changed or closed.
- New entrants: frontier labs, inference platforms, applied-AI startups, cloud providers.

## 3. Verify each posting

Open every candidate with WebFetch. Keep a posting only if the page itself shows:

- company, title, location, and either requirements or responsibilities;
- enough detail to fill the table's **Signature requirements** and **Experience** columns.

Record for each: company, role, URL, family, 3–6 signature requirements in the posting's own terms, experience asked, and whether it is open or closed.

## 4. Update the table

- Target 15–20 rows covering all four families; prefer the most recent and most specific postings.
- Replace a closed posting only when a current one from the same company exists. Otherwise keep it: closed postings still evidence requirements, and the Sources note already says so.
- Sort rows by family (ML-heavy, API / agent, Platform / private deploy, Classic data FDSE), then company.
- Update the opening sentence's count ("Across N public FDE postings reviewed in <Month YYYY>").
- Rewrite **What this means for the curriculum** only if the evidence changed: a requirement now common across families (for example a new protocol, framework or deployment pattern) that the curriculum does not teach.
- Mirror every added or replaced posting in `## Sources` using the existing `- [Company: Role](url)` format.

## 5. Flag curriculum gaps

If two or more new postings ask for something no phase covers, do not silently rewrite phases. List the gap and the phase it belongs in, and hand it to the `update-curriculum` skill (or ask the owner).

## 6. Finish

```bash
python scripts/build.py
python scripts/check_repo.py
```

Then add a `CHANGELOG.md` entry under `## [Unreleased]`, for example `- Market: added 3 postings (X, Y, Z); marked 2 closed; new gap noted: <gap>.`, and set `Last reviewed` to today.

Report back: rows added, removed, marked closed, and any gaps found.
