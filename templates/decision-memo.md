# Decision memo: <prompt vs RAG vs fine-tune for TASK>

**Decision:** deploy <variant>. **Date:** <date>

## Context

The task, the user, the success bar, and why prompting alone was not enough (or was).

## Options compared

All variants scored on the same versioned golden set (<n> items) with the same harness.

| Variant | Quality metric | Secondary metric | p95 latency | Cost / 1k requests | Effort to maintain |
| --- | --- | --- | --- | --- | --- |
| Prompt-only | | | | | Low |
| RAG | | | | | Medium |
| SFT (LoRA) | | | | | High |
| SFT + DPO | | | | | High |

## Why this option

- The deciding numbers.
- What we give up.
- Conditions under which we would revisit (data volume, new base model, cost change).

## Error analysis

Top three failure types for the chosen variant, with an example of each and the planned fix.

## Risks

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| | | | |
