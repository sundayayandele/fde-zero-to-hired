<!-- GENERATED from CURRICULUM.md by scripts/build.py. Do not edit by hand: edit CURRICULUM.md, then run `python scripts/build.py`. -->

# Interview loop preparation

[Home](../README.md)

FDE loops combine coding, a live decomposition case, a technical deep-dive, LLM system design and a values round. The decomposition round is usually the deciding one.

| Round | What it tests | How to prepare |
| --- | --- | --- |
| Recruiter / hiring manager | Motivation, customer-facing history, travel and location fit | A 90-second story of why FDE, built around Capstone 5. |
| Coding | Practical Python: parse messy data, call an API, build a small LLM pipeline | Timed exercises building data + LLM pipelines from scratch; review LeetCode medium basics. |
| Decomposition / case | Turning a vague customer problem into a scoped, buildable plan, live | Practise 10 cases out loud with a partner playing an evasive stakeholder. Structure: clarify goal → users → data → constraints → options → MVP → metric → risks. |
| Technical deep-dive | Depth on one project: trade-offs, failures, numbers | Rehearse Capstone 3 and 5: why fine-tune or not, eval design, what broke. |
| LLM system design | RAG at scale, latency budgets, eval and guardrails, private deployment | Practise prompts like "cut a 1.5 s RAG pipeline to under 300 ms" and "deploy for a bank with no internet egress". |
| Values / behavioural | Ownership, ambiguity, low ego, honesty with customers | Five STAR stories: a failure, a pushback on a customer, an ambiguous win, a cross-team fix, a fast learn. |

## Decomposition case framework

Work through these out loud, asking the interviewer (the "customer") at each step:

1. **Goal:** what business outcome changes if this works? How is it measured today?
2. **Users:** who uses it, how often, and what do they do now instead?
3. **Data:** what exists, where, in what shape, who owns it, what is sensitive?
4. **Constraints:** latency, cost, privacy, regulation, deployment environment, timeline.
5. **Options:** at least two approaches (for example prompting vs RAG vs fine-tuning) with trade-offs.
6. **MVP:** the smallest pilot that proves value in 2–6 weeks.
7. **Metric:** the success bar agreed before building, and how you will measure it.
8. **Risks:** what could fail, and the fallback for each.

## Practice prompts

- "Our claims team takes 3 days to triage a claim. Can AI help?"
- "We want a chatbot over our internal policies, but legal is worried."
- "Our RAG pilot works in the demo but users say answers are wrong."
- "A bank wants our model but no data can leave their data centre."
- "Leadership wants to fine-tune our own model. Should we?"

