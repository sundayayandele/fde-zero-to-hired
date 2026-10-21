<!-- GENERATED from CURRICULUM.md by scripts/build.py. Do not edit by hand: edit CURRICULUM.md, then run `python scripts/build.py`. -->

# Capstone 2: Eval harness and red-team report for Capstone 1

← [Capstone 1](../01-enterprise-document-assistant/README.md) · [Home](../../README.md) · [Capstone 3](../03-domain-fine-tune/README.md) →

Built during [Phase 3: Evaluation and reliability](../../phases/03-evaluation-and-reliability/README.md).

**Brief:** the customer's risk team will not approve Capstone 1 without evidence. Produce that evidence.

**Must include**

- A versioned golden set and an eval harness that scores prompt-only, basic RAG and advanced RAG side by side.
- An LLM judge with its agreement rate against human labels reported.
- A red-team suite (prompt injection through documents, out-of-scope questions, PII leakage) with pass/fail results.
- A CI job that fails the build if a key metric drops.

**Definition of done:** a results table in the README, a dashboard screenshot, and a one-page "release readiness" memo written for a non-technical risk owner.

**Worked example:** [fde-03-evaluation](https://github.com/sundayayandele/fde-03-evaluation) builds this capstone against the fde-02 document assistant. Use it to check your scope, not as your submission.

**Proves:** the evaluation depth named in the Anthropic, Databricks, DeepMind and Reflection postings, and the strongest single answer in an FDE interview.

## Templates to use

- [capstone-README.md](../../templates/capstone-README.md)
- [customer-brief.md](../../templates/customer-brief.md)
- [eval-report.md](../../templates/eval-report.md)

## Submit

1. Publish your capstone in its own public repo, using the [capstone README template](../../templates/capstone-README.md).
2. Score it against the [rubric](../../docs/rubric.md): pass at 14/20 with no criterion below 2.
3. Open a **Capstone submission** issue in your fork of this repo with the links.

---

← [Capstone 1](../01-enterprise-document-assistant/README.md) · [Home](../../README.md) · [Capstone 3](../03-domain-fine-tune/README.md) →
