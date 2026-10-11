<!-- GENERATED from CURRICULUM.md by scripts/build.py. Do not edit by hand: edit CURRICULUM.md, then run `python scripts/build.py`. -->

# Phase 4: Model customization (weeks 19–24)

← [Phase 3: Evaluation and reliability](../03-evaluation-and-reliability/README.md) · [Home](../../README.md) · [Phase 5: Inference, deployment and sovereign AI](../05-inference-and-sovereign-ai/README.md) →

The goal is to fine-tune an open-weight model, prove it beats prompting and RAG on a task a customer cares about, and know when it is not worth doing. This phase separates an ML-heavy FDE (Mistral, Reflection, Modal, Hugging Face) from an API-only one.

| Week | Topic | What you do |
| --- | --- | --- |
| 19 | PyTorch for LLMs | Tensors, autograd, training loop, mixed precision, data loaders, GPU memory basics. Write a training loop from scratch. |
| 20 | Transformer internals | Attention, positional encodings, KV cache, tokenizers, mixture-of-experts. Implement attention in a notebook; read the Mistral 7B and Mixtral papers. |
| 21 | Data for fine-tuning | Task framing, chat templates, cleaning and dedup, synthetic data generation and filtering, a data card. |
| 22 | Supervised fine-tuning | LoRA and QLoRA with Hugging Face TRL/PEFT or mistral-finetune; hyper-parameters, run tracking, error analysis. |
| 23 | Preference tuning | DPO (and ORPO as a variant) on top of SFT; awareness of RL fine-tuning and when it pays off. |
| 24 | Decision and Capstone 3 | Compare prompt vs RAG vs SFT vs SFT+DPO on quality, latency and cost. Ship Capstone 3. |

**Resources:** Karpathy *Let's build GPT* and *Let's build the GPT tokenizer*; the Hugging Face LLM Course fine-tuning chapters; TRL and PEFT docs; Sebastian Raschka *Build a Large Language Model (From Scratch)*.

**Compute:** a single rented 24–48 GB GPU is enough for a 7B-class model with QLoRA. Budget your GPU hours before you start and track spend per run.

## Capstone 3

This phase ends with **[Capstone 3: Domain fine-tune with a defended decision](../../capstones/03-domain-fine-tune/README.md)**. Read the brief before week 1 of the phase so you build towards it.

---

← [Phase 3: Evaluation and reliability](../03-evaluation-and-reliability/README.md) · [Home](../../README.md) · [Phase 5: Inference, deployment and sovereign AI](../05-inference-and-sovereign-ai/README.md) →
