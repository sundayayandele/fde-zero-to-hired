<!-- GENERATED from CURRICULUM.md by scripts/build.py. Do not edit by hand: edit CURRICULUM.md, then run `python scripts/build.py`. -->

# Phase 5: Inference, deployment and sovereign AI (weeks 25–28)

← [Phase 4: Model customization](../04-model-customization/README.md) · [Home](../../README.md) · [Phase 6: Forward-deployed practice](../06-forward-deployed-practice/README.md) →

The goal is to run your own model inside a customer-like environment at a known cost, latency and security posture. Mistral, Cohere, Reflection and Scale all ask for VPC or on-prem deployment, and Modal asks for vLLM/SGLang depth.

| Week | Topic | What you do |
| --- | --- | --- |
| 25 | LLM serving | vLLM (and a look at SGLang or TGI): continuous batching, KV cache, LoRA adapters at serve time, OpenAI-compatible endpoints. Benchmark throughput and p95 latency. |
| 26 | Quantization and sizing | AWQ, GPTQ and FP8; GPU memory maths; cost per 1,000 requests across GPU types. |
| 27 | Kubernetes for GPUs | Containers, Helm, GPU operator, autoscaling, rollout and rollback of model versions (Kubernetes or OpenShift). |
| 28 | Sovereign and enterprise deployment | Private networking, air-gapped installs, secrets, SSO, audit logging, data residency, GDPR and EU AI Act awareness. Ship Capstone 4. |

**Resources:** vLLM and SGLang docs; NVIDIA GPU Operator docs; Kubernetes official tutorials; Chip Huyen *AI Engineering*.

## Capstone 4

This phase ends with **[Capstone 4: Sovereign deployment of your fine-tuned model](../../capstones/04-sovereign-deployment/README.md)**. Read the brief before week 1 of the phase so you build towards it.

---

← [Phase 4: Model customization](../04-model-customization/README.md) · [Home](../../README.md) · [Phase 6: Forward-deployed practice](../06-forward-deployed-practice/README.md) →
