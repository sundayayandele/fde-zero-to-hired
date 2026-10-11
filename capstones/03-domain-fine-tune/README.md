<!-- GENERATED from CURRICULUM.md by scripts/build.py. Do not edit by hand: edit CURRICULUM.md, then run `python scripts/build.py`. -->

# Capstone 3: Domain fine-tune with a defended decision

← [Capstone 2](../02-eval-harness-and-red-team/README.md) · [Home](../../README.md) · [Capstone 4](../04-sovereign-deployment/README.md) →

Built during [Phase 4: Model customization](../../phases/04-model-customization/README.md).

**Brief:** the customer's task (for example extracting fields from KYC documents, classifying claims, or answering in a strict house style) is not solved well enough by prompting. Decide whether fine-tuning is worth it and prove it.

**Must include**

- A curated SFT dataset and a preference dataset, both with data cards.
- A LoRA/QLoRA fine-tune of a small open Mistral model, then a DPO pass.
- The Capstone 2 harness re-used to score four variants: prompt-only, RAG, SFT, SFT+DPO.
- A decision memo: which variant you would deploy, with numbers for quality, latency and cost per 1,000 requests.

**Definition of done:** model adapter on the Hugging Face Hub with a model card, training code in the repo, and the memo. A fine-tune that does not win is still a pass if the memo explains why.

**Proves:** fine-tuning, PyTorch and the prompt-vs-RAG-vs-fine-tune judgement asked for by Mistral, Reflection and Databricks.

## Templates to use

- [capstone-README.md](../../templates/capstone-README.md)
- [decision-memo.md](../../templates/decision-memo.md)
- [data-card.md](../../templates/data-card.md)
- [model-card.md](../../templates/model-card.md)

## Submit

1. Publish your capstone in its own public repo, using the [capstone README template](../../templates/capstone-README.md).
2. Score it against the [rubric](../../docs/rubric.md): pass at 14/20 with no criterion below 2.
3. Open a **Capstone submission** issue in your fork of this repo with the links.

---

← [Capstone 2](../02-eval-harness-and-red-team/README.md) · [Home](../../README.md) · [Capstone 4](../04-sovereign-deployment/README.md) →
