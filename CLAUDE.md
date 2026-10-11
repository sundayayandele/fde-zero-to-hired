# CLAUDE.md

@AGENTS.md

## Claude Code specifics

This repo ships its own Claude Code plugin, **fde-maintainer**, in `plugins/fde-maintainer/`. It is listed in the repo's marketplace (`.claude-plugin/marketplace.json`) and enabled for this project in `.claude/settings.json`.

| Use | When |
| --- | --- |
| `/fde-maintainer:monthly-refresh` | Once a month, or when the GitHub "Monthly refresh" issue opens. Runs market, resources, build, checks and changelog in order |
| `refresh-fde-market` skill | Updating the job-posting table and sources |
| `update-curriculum` skill | Any edit to phases, weeks, capstones, resources or the rubric |
| `audit-resources` skill | Checking links, resources and tool names are still current |
| `release-update` skill | Writing the changelog, bumping the version, preparing the commit |
| `fde-market-researcher` agent | Delegated research on new postings; returns verified rows only |
| `curriculum-reviewer` agent | Fresh-eyes review of a diff before it is committed |

Hooks in the plugin:

- **PostToolUse** (`Edit|Write|MultiEdit`): `scripts/guard_generated.py` warns if you edit a generated file. Move the change into `CURRICULUM.md`.
- **Stop**: `scripts/check_repo.py` blocks finishing if generated files are stale or a relative link is broken. Run `python scripts/build.py` and fix links.

## Working style here

- Research before editing market facts: open each posting with WebFetch and cite it.
- After a content change, show the owner a short summary of what changed and the suggested commit message. Don't commit or push; he uses GitHub Desktop.
- For anything larger than a few lines, propose the change first, then edit.
