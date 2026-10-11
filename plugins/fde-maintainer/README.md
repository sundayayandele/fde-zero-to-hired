# fde-maintainer (Claude Code plugin)

Keeps the Zero-to-Hired curriculum current. It packages the repo's maintenance workflow so any Claude Code session follows the same rules.

## What's inside

| Component | Name | Purpose |
| --- | --- | --- |
| Command | `/fde-maintainer:monthly-refresh [focus]` | Runs the whole monthly refresh in order |
| Skill | `refresh-fde-market` | Updates the market table and sources with verified postings |
| Skill | `update-curriculum` | Safe edits: CURRICULUM.md → build → check → changelog |
| Skill | `audit-resources` | Dead links, retired resources, renamed tools |
| Skill | `release-update` | Changelog, version, dates, commit message for GitHub Desktop |
| Agent | `fde-market-researcher` | Searches and verifies postings; returns cited rows |
| Agent | `curriculum-reviewer` | Fresh-eyes review of a diff before commit |
| Hook | PostToolUse | Warns when a generated file is edited directly |
| Hook | Stop | Blocks finishing while generated files are stale or links are broken |

The hooks call `scripts/guard_generated.py` and `scripts/check_repo.py` in the repo, so the plugin is meant to be used inside this repository.

## Install

**Automatic (recommended).** `.claude/settings.json` in the repo registers this marketplace and enables the plugin. Open the repo in Claude Code, trust the folder, and accept the prompt to install. Before publishing, replace `YOUR-GITHUB-USERNAME` in `.claude/settings.json` with your GitHub username.

**Manual, from your local clone:**

```
/plugin marketplace add ./
/plugin install fde-maintainer@fde-zero-to-hired
```

**Manual, from GitHub (after publishing):**

```
/plugin marketplace add YOUR-GITHUB-USERNAME/fde-zero-to-hired
/plugin install fde-maintainer@fde-zero-to-hired
```

Check it loaded with `/plugin` (installed tab) and `/hooks`.

## Monthly routine

1. A GitHub Action opens a **Monthly refresh** issue on the 1st of each month with the external link report.
2. Open the repo in Claude Code and run `/fde-maintainer:monthly-refresh`.
3. Review the summary, then commit and push in GitHub Desktop with the suggested message.
