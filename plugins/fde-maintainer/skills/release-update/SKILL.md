---
name: release-update
description: Close out a batch of curriculum changes - finalise CHANGELOG.md, choose the version number, update Last reviewed dates, run all checks and write the commit message for GitHub Desktop. Use when asked to release, publish, wrap up or prepare a commit for this repo.
---

# Release an update

The owner commits and publishes with GitHub Desktop. Your job is to leave the working tree ready and hand over a commit message. Do not commit or push unless asked.

## 1. Check the tree is consistent

```bash
python scripts/build.py
python scripts/check_repo.py
```

Both must pass. If phases or weeks changed, confirm the README phase table matches `CURRICULUM.md` and flag if `assets/roadmap.png` needs regenerating.

## 2. Pick the version (semantic versioning for content)

| Bump | When |
| --- | --- |
| **Major** (2.0.0) | Phases or capstones added, removed or renumbered; total duration changes |
| **Minor** (1.1.0) | New weeks, labs, resources or market rows; a capstone's requirements change |
| **Patch** (1.0.1) | Fixed links, typos, wording, dates |

Read the last version from `CHANGELOG.md`.

## 3. Finalise the changelog

Move the `## [Unreleased]` lines into a new section `## [x.y.z] - YYYY-MM-DD`, grouped under `### Market`, `### Curriculum`, `### Resources`, `### Repo` (omit empty groups). Leave an empty `## [Unreleased]` at the top.

## 4. Update dates and versions

- `Last reviewed: YYYY-MM-DD` at the top of `CURRICULUM.md` (then rebuild).
- `Last reviewed` line in `README.md`.
- `version` in `plugins/fde-maintainer/.claude-plugin/plugin.json` only if the plugin itself changed.

## 5. Hand over

Give the owner:

1. A two-line summary of the release.
2. The commit message, summary line under 72 characters, for example:

   ```
   v1.1.0: Oct 2026 market refresh and Phase 5 serving update

   - Market: +3 postings, 2 marked closed
   - Phase 5: SGLang lab, quantization resources refreshed
   ```

3. A reminder: in GitHub Desktop, review the changed files, paste the message, **Commit to main**, then **Push origin**. Optionally create a GitHub release named `vx.y.z` with the changelog section as its notes.
