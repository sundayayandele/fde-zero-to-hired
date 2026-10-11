<!-- GENERATED from CURRICULUM.md by scripts/build.py. Do not edit by hand: edit CURRICULUM.md, then run `python scripts/build.py`. -->

# Capstone 4: Sovereign deployment of your fine-tuned model

← [Capstone 3](../03-domain-fine-tune/README.md) · [Home](../../README.md) · [Capstone 5](../05-flagship-pilot/README.md) →

Built during [Phase 5: Inference, deployment and sovereign AI](../../phases/05-inference-and-sovereign-ai/README.md).

**Brief:** a regulated customer (bank, hospital or public body) cannot send data to a public API. Deploy the Capstone 3 model and the Capstone 1 assistant inside a private environment.

**Must include**

- vLLM serving the base model plus your LoRA adapter, in full precision and one quantized variant.
- Kubernetes manifests or Helm chart, with no outbound internet needed at runtime.
- A benchmark table: tokens/second, p95 latency, GPU memory, cost per 1,000 requests.
- A reference architecture document covering networking, identity, logging and data residency.

**Definition of done:** reproducible deployment from the repo, benchmark notebook, and an architecture document a customer security team could review.

**Proves:** serving, quantization, Kubernetes and private deployment, the main gap between an application engineer and an FDE trusted with regulated customers.

## Templates to use

- [capstone-README.md](../../templates/capstone-README.md)
- [customer-brief.md](../../templates/customer-brief.md)

## Submit

1. Publish your capstone in its own public repo, using the [capstone README template](../../templates/capstone-README.md).
2. Score it against the [rubric](../../docs/rubric.md): pass at 14/20 with no criterion below 2.
3. Open a **Capstone submission** issue in your fork of this repo with the links.

---

← [Capstone 3](../03-domain-fine-tune/README.md) · [Home](../../README.md) · [Capstone 5](../05-flagship-pilot/README.md) →
