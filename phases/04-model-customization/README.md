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

## Watch

Optional short videos for each week, all in English with English captions. Moodle learners get them embedded on a Watch page per week.

### Week 19: PyTorch for LLMs

- [Write your training loop in PyTorch](https://www.youtube.com/watch?v=Dh9CL8fyG80) · Hugging Face · 5 min. Writing your own PyTorch training loop (official Hugging Face course).
- [PyTorch Tutorial 09 - Dataset and DataLoader - Batch Training](https://www.youtube.com/watch?v=PXOzkkB5eH0) · Patrick Loeber · 15 min. Datasets and DataLoaders: feeding batches to the training loop.
- [Mixed Precision Training - Explained](https://www.youtube.com/watch?v=87GhCIQudEA) · DataMListic · 11 min. Mixed precision: training faster and with less GPU memory.
- [Nvidia CUDA in 100 Seconds](https://www.youtube.com/watch?v=pPStdjuYzSI) · Fireship · 3 min. CUDA in 100 seconds: why GPUs make deep learning practical.

### Week 20: Transformer internals

- [Transformers Step-by-Step Explained (Attention Is All You Need)](https://www.youtube.com/watch?v=avjX3QrYkls) · ByteByteGo · 10 min. The transformer step by step, as in 'Attention Is All You Need'.
- [I Visualised Attention in Transformers](https://www.youtube.com/watch?v=RNF0FvRjGZk) · Gal Lahat · 13 min. Attention visualised: how each token decides what to look at.
- [Tokenization and Byte Pair Encoding](https://www.youtube.com/watch?v=gstdcCDqdlc) · Luis Serrano Academy · 8 min. Tokenization and byte-pair encoding, worked through by hand.
- [Positional Encodings: Why RoPE Rotates Instead of Adds](https://www.youtube.com/watch?v=EA24K07lH0Y) · DataMListic · 5 min. Positional encodings, and why RoPE rotates instead of adds.
- [How KV Cache Speeds Up LLMs for Faster AI Models on GPUs](https://www.youtube.com/watch?v=o0gkdZBtwEg) · IBM Technology · 11 min. The KV cache: why generation gets faster, and why it costs memory (IBM and Red Hat).
- [Mixture of Experts: Explained & Implemented](https://www.youtube.com/watch?v=vHF7gGvAqu8) · NeuralNine · 24 min. Mixture of experts explained and implemented, the idea behind Mixtral.

### Week 21: Data for fine-tuning

- [Is Fine-Tuning Still Needed? LLMs, RAG, & LoRA](https://www.youtube.com/watch?v=-W2JdSl1v48) · IBM Technology · 11 min. Is fine-tuning still needed? Where it beats prompting and RAG, and where it does not.
- [Fine Tuning LLM Explained Simply](https://www.youtube.com/watch?v=ezdIOLbUSWg) · codebasics · 7 min. Fine-tuning explained simply: what changes in the model and why data matters most.
- [How to Create Synthetic Datasets for Fine-Tuning Llama](https://www.youtube.com/watch?v=Cb8DZraP9n0) · Meta Developers · 3 min. Creating synthetic datasets for fine-tuning (official Meta).
- [Get Started with Unsloth Studio: Generate Data & Fine-Tune LLMs Locally on any NVIDIA GPU](https://www.youtube.com/watch?v=mmbkP8NARH4) · NVIDIA Developer · 8 min. Generating training data and fine-tuning locally with Unsloth Studio (official NVIDIA).

### Week 22: Supervised fine-tuning

- [Parameter-Efficient Fine-Tuning for LLMs: LoRA, QLoRA, rsLoRA & LoRA-FA](https://www.youtube.com/watch?v=722yHNfei7k) · Ryan Rad · 13 min. Parameter-efficient fine-tuning: LoRA, QLoRA and their variants.
- [Fast Fine Tuning with Unsloth](https://www.youtube.com/watch?v=dMY3dBLojTk) · Matt Williams · 17 min. Fast LoRA fine-tuning with Unsloth, start to finish.
- [How to Fine-Tune an AI Model Locally with Unsloth - Method That Actually Works!](https://www.youtube.com/watch?v=Yr0G1QbAsEE) · Gary Explains · 18 min. Fine-tuning a model locally with Unsloth, a method that works on modest hardware.

### Week 23: Preference tuning

- [Reinforcement Learning with Human Feedback (RLHF) in 4 minutes](https://www.youtube.com/watch?v=vJ4SsfmeQlk) · Sebastian Raschka · 4 min. RLHF in four minutes, from Sebastian Raschka.
- [Reinforcement Learning with Human Feedback (RLHF), Clearly Explained!!!](https://www.youtube.com/watch?v=qPN_XZcJf_s) · StatQuest with Josh Starmer · 18 min. RLHF clearly explained: rewards, preferences and why they matter.
- [Direct Preference Optimization (DPO) | Paper Explained](https://www.youtube.com/watch?v=TfybkCFQufc) · Outlier · 17 min. Direct Preference Optimization: preference tuning without a reward model.
- [Group Relative Policy Optimization(GRPO) Visualized](https://www.youtube.com/watch?v=EX8-ucKOBbA) · AGI Lambda · 7 min. GRPO visualised: the reinforcement learning method behind reasoning models.
- [DeepSeek's GRPO (Group Relative Policy Optimization) | Reinforcement Learning for LLMs](https://www.youtube.com/watch?v=xT4jxQUl0X8) · Julia Turc · 23 min. GRPO in depth, and when reinforcement learning fine-tuning pays off.

### Week 24: Decision and Capstone 3

- [RAG vs Fine-Tuning vs Prompt Engineering: Optimizing AI Models](https://www.youtube.com/watch?v=zYGDpG-pTho) · IBM Technology · 13 min. RAG vs fine-tuning vs prompt engineering: choosing with evidence.
- [RAG vs Fine Tuning vs Prompt Engineering](https://www.youtube.com/watch?v=Q-_D_2NWECE) · codebasics · 9 min. The same decision with concrete examples and trade-offs.

### Want more depth? (longer, optional)

- [Positional Encodings and Group Theory | 3Blue1Brown and Alok Puranik](https://www.youtube.com/watch?v=k86eUj4hgdc) · Jane Street · 77 min. 3Blue1Brown and Jane Street on positional encodings: the maths behind RoPE.
- [How to Fine-Tune any AI Model Locally (FULL Tutorial)](https://www.youtube.com/watch?v=4JofSJIrjwU) · Tech With Tim · 41 min. A full local fine-tuning tutorial, from dataset to running model.
- [How to Fine Tune your own LLM using LoRA (on a CUSTOM dataset!)](https://www.youtube.com/watch?v=D3pXSkGceY0) · Nicholas Renotte · 61 min. Fine-tuning your own LLM with LoRA on a custom dataset, end to end.

---

← [Phase 3: Evaluation and reliability](../03-evaluation-and-reliability/README.md) · [Home](../../README.md) · [Phase 5: Inference, deployment and sovereign AI](../05-inference-and-sovereign-ai/README.md) →
