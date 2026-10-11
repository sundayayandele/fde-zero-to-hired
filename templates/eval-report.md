# Eval and release-readiness report: <system name>

**Verdict:** ready / ready with conditions / not ready. **Date:** <date> · **Version tested:** <git sha>

## Golden set

- **Size:** <n> items (easy / hard / adversarial split)
- **Built from:** <source>; labelled by <who>
- **Version:** <tag or hash>

## Results

| Variant | Retrieval recall@k | Faithfulness | Correctness | Refusal accuracy | p95 latency |
| --- | --- | --- | --- | --- | --- |
| Prompt-only | | | | | |
| Basic RAG | | | | | |
| Advanced RAG | | | | | |

**Judge calibration:** LLM judge agreed with human labels on <x>% of <n> items.

## Red-team results

| Attack category | Cases | Passed | Failed | Notes |
| --- | --- | --- | --- | --- |
| Prompt injection via documents | | | | |
| Out-of-scope questions | | | | |
| PII leakage | | | | |
| Jailbreak attempts | | | | |

## Regression gate

Metrics checked in CI, thresholds, and what happens when one drops.

## For the risk owner (plain language)

Three or four sentences: what the system gets right, where it fails, what safeguards exist, and the conditions for going live.
