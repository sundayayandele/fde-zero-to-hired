<!-- GENERATED from CURRICULUM.md by scripts/build.py. Do not edit by hand: edit CURRICULUM.md, then run `python scripts/build.py`. -->

# Phase 3: Evaluation and reliability (weeks 16–18)

← [Phase 2: LLM application engineering](../02-llm-application-engineering/README.md) · [Home](../../README.md) · [Phase 4: Model customization](../04-model-customization/README.md) →

The goal is to prove with numbers whether an LLM system works, and to catch regressions before a customer does. Interviewers repeatedly ask how you know a system works beyond "it looks right"; this phase is your answer.

| Week | Topic | What you do |
| --- | --- | --- |
| 16 | Eval design | Define the business metric first. Build a 150–200 item golden set with easy, hard and adversarial cases. Retrieval metrics (recall@k, MRR) and answer metrics (faithfulness, correctness). |
| 17 | LLM-as-judge and guardrails | Write a rubric, calibrate the judge against about 50 hand labels, sample by stratum. Add input/output guardrails, prompt-injection tests and refusal behaviour. |
| 18 | Observability and regression | Tracing (Langfuse, LangSmith or OpenTelemetry), token cost and latency dashboards, eval suite in CI on every change. Ship Capstone 2. |

**Resources:** Hamel Husain's writing on LLM evals; RAGAS and DeepEval docs; OWASP Top 10 for LLM Applications.

## Capstone 2

This phase ends with **[Capstone 2: Eval harness and red-team report for Capstone 1](../../capstones/02-eval-harness-and-red-team/README.md)**. Read the brief before week 1 of the phase so you build towards it.

---

← [Phase 2: LLM application engineering](../02-llm-application-engineering/README.md) · [Home](../../README.md) · [Phase 4: Model customization](../04-model-customization/README.md) →
