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

**Code:** start with [fde-03-evaluation-starter](https://github.com/sundayayandele/fde-03-evaluation-starter) and complete the exercises in `labs/` week by week. The reference solution, [fde-03-evaluation](https://github.com/sundayayandele/fde-03-evaluation), is an evaluation harness with golden sets, a calibrated judge, a red team and a CI release gate. Open it only after you have tried each exercise.

## Capstone 2

This phase ends with **[Capstone 2: Eval harness and red-team report for Capstone 1](../../capstones/02-eval-harness-and-red-team/README.md)**. Read the brief before week 1 of the phase so you build towards it.

## Watch

Optional short videos for each week, all in English with English captions. Moodle learners get them embedded on a Watch page per week.

### Week 16: Eval design

- [Why Everyone Should Know About AI Evals: The Fundamentals Explained](https://www.youtube.com/watch?v=EN8jVkv0kiw) · ByteByteAI · 9 min. Why evals matter and the fundamentals every AI system needs.
- [How To Approach Your AI Evals](https://www.youtube.com/watch?v=DZxaPNYi_k0) · Hamel Husain · 4 min. How to approach evals: start from real errors, not generic metrics.
- [The Most Important Skill for AI Engineers: Evals Explained](https://www.youtube.com/watch?v=MltkRz94SWA) · Aish Reganti · 18 min. Evals explained end to end, the skill hiring teams test for.
- [6.1 How to evaluate a RAG system: methods and metrics](https://www.youtube.com/watch?v=qI2qQfOG0Js) · Evidently AI · 7 min. How to evaluate a RAG system: retrieval and answer metrics.
- [What are Golden Datasets? (And Why You Need One for AI Testing)](https://www.youtube.com/watch?v=u12MxA-LPSY) · TestinGil  - Gil Zilberfeld · 4 min. Golden datasets: the fixed test set every change is measured against.

### Week 17: LLM-as-judge and guardrails

- [LLM as a Judge: Scaling AI Evaluation Strategies](https://www.youtube.com/watch?v=trfUBIDeI1Y) · IBM Technology · 6 min. LLM as a judge: scaling evaluation, and where it goes wrong.
- [How to Automate AI Evals (Correctly)](https://www.youtube.com/watch?v=tqUDjc1HzO4) · Hamel Husain · 27 min. Automating evals correctly: judges you have checked against human labels.
- [Prompt Injection, Clearly Explained](https://www.youtube.com/watch?v=KDcayRssGbw) · ByteByteAI · 6 min. Prompt injection, clearly explained, including attacks hidden in documents.
- [Episode 3: Direct Prompt Injection Explained | AI Red Teaming 101](https://www.youtube.com/watch?v=8i95orzUrY0) · Microsoft Developer · 6 min. Direct prompt injection, from Microsoft's AI Red Teaming 101 series.
- [OWASP's Top 10 Ways to Attack LLMs: AI Vulnerabilities Exposed](https://www.youtube.com/watch?v=gUNXZMcd2jU) · IBM Technology · 25 min. The OWASP Top 10 ways LLM applications get attacked.
- [Advanced Guardrails for AI Agents | Full Tutorial](https://www.youtube.com/watch?v=rMUycP_cp9g) · James Briggs · 22 min. Building guardrails for AI agents: input, output and tool checks.

### Week 18: Observability and regression

- [OpenTelemetry: Simplifying Hybrid Cloud Monitoring](https://www.youtube.com/watch?v=hLvwoow3XTk) · IBM Technology · 6 min. OpenTelemetry: the open standard for traces, metrics and logs.
- [Langfuse Walkthrough - Full Demo of Agent Tracing, Evals, Experiments and Prompt Management](https://www.youtube.com/watch?v=THfB4p2xCFY) · Langfuse · 15 min. Langfuse walkthrough: tracing, evals, experiments and prompt management (official).
- [How to use GitHub Actions | GitHub for Beginners](https://www.youtube.com/watch?v=BQrohJ3PT7I) · GitHub · 8 min. GitHub Actions: running your tests and eval suite on every change (official GitHub).

### Want more depth? (longer, optional)

- [How to Systematically Setup LLM Evals (Metrics, Unit Tests, LLM-as-a-Judge)](https://www.youtube.com/watch?v=a3SMraZWNNs) · Dave Ebbelaar · 55 min. Setting up LLM evals systematically: metrics, unit tests and LLM judges, with code.
- [AI Evaluations Clearly Explained in 50 Minutes (Real Example) | Hamel Husain](https://www.youtube.com/watch?v=uiza7wp1KrE) · Peter Yang · 53 min. Hamel Husain walks through AI evaluations on a real product example.

---

← [Phase 2: LLM application engineering](../02-llm-application-engineering/README.md) · [Home](../../README.md) · [Phase 4: Model customization](../04-model-customization/README.md) →
