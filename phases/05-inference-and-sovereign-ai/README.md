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

## Watch

Optional short videos for each week, all in English with English captions. Moodle learners get them embedded on a Watch page per week.

### Week 25: LLM serving

- [What is vLLM? Efficient AI Inference for Large Language Models](https://www.youtube.com/watch?v=McLdlg5Gc9s) · IBM Technology · 5 min. What vLLM is and why it serves models so much more efficiently.
- [Understanding vLLM with a Hands On Demo](https://www.youtube.com/watch?v=qdPkA5mxLhg) · KodeKloud · 15 min. vLLM hands on: serving a model behind an OpenAI-compatible endpoint.
- [vLLM: Easy, Fast, and Cheap LLM Serving for Everyone - Simon Mo, vLLM](https://www.youtube.com/watch?v=Tv71-g75OgU) · PyTorch · 25 min. vLLM from its maintainers: continuous batching, PagedAttention and what's next (official PyTorch).
- [PagedAttention: Behind vLLM's Insane Speed](https://www.youtube.com/watch?v=6uPnLkCiy5g) · Tales Of Tensors · 7 min. PagedAttention: how vLLM manages KV-cache memory like virtual memory.
- [SGLang vs vLLM: Which LLM Inference Framework Should You Use?](https://www.youtube.com/watch?v=18AkpuX3vkY) · Neural AI Flair · 12 min. SGLang vs vLLM: choosing a serving framework.
- [Llama.cpp vs vLLM: Which Local LLM Engine Actually Scales?](https://www.youtube.com/watch?v=0ujh7hfutq0) · IBM Technology · 11 min. llama.cpp vs vLLM: laptop-scale vs production-scale serving.

### Week 26: Quantization and sizing

- [LLM Quantization Explained](https://www.youtube.com/watch?v=jUIjgp4puvw) · KodeKloud · 4 min. Quantization in four minutes: smaller, faster models and what you give up.
- [How LLMs survive in low precision | Quantization Fundamentals](https://www.youtube.com/watch?v=qoQJq5UwV1c) · Julia Turc · 21 min. How LLMs survive in low precision: the fundamentals of quantization.
- [GGUF vs AWQ vs GPTQ: LLM Quantization Methods Explained](https://www.youtube.com/watch?v=7hYSmzIZXNs) · Cloud Codes · 10 min. GGUF vs AWQ vs GPTQ: which quantization format for which runtime.
- [Why LLMs Use Weird Numbers: FP8, BF16, INT4](https://www.youtube.com/watch?v=Fx2sLT-84V4) · ML Guy · 7 min. FP8, BF16 and INT4: the number formats behind fast inference.
- [Free VRAM Calculator: This Tiny Web App Calculates LLM Memory in Seconds!](https://www.youtube.com/watch?v=k1PheZjZHuE) · Fahd Mirza · 8 min. Working out how much GPU memory a model needs before you rent a GPU.

### Week 27: Kubernetes for GPUs

- [Kubernetes Simply Explained](https://www.youtube.com/watch?v=Xv9dnKHO8tg) · TechWorld with Nana · 4 min. Kubernetes, simply explained (2026).
- [What is Helm?](https://www.youtube.com/watch?v=fy8SHvNZGeE) · IBM Technology · 9 min. Helm: packaging and versioning Kubernetes deployments.
- [Kubernetes vs. OpenShift](https://www.youtube.com/watch?v=ZsOR8RkAOwI) · IBM Technology · 9 min. Kubernetes vs OpenShift: what Red Hat adds for enterprises.
- [NVIDIA GPU Operator Overview](https://www.youtube.com/watch?v=KER0dbfmAqQ) · NVIDIA Developer · 13 min. The NVIDIA GPU Operator: making GPUs schedulable in a cluster (official NVIDIA).
- [Kubernetes Autoscaling: HPA vs. VPA vs. Keda vs. CA vs. Karpenter vs. Fargate](https://www.youtube.com/watch?v=hsJ2qtwoWZw) · Anton Putra · 15 min. Autoscaling in Kubernetes: HPA, VPA, KEDA and node autoscalers compared.
- [LLM‑D Explained: Building Next‑Gen AI with LLMs, RAG & Kubernetes](https://www.youtube.com/watch?v=CNKGgOphAPM) · IBM Technology · 5 min. llm-d: Kubernetes-native distributed LLM serving.

### Week 28: Sovereign and enterprise deployment

- [What Is Digital Sovereignty? AI, Data & Control Explained](https://www.youtube.com/watch?v=Gj13NR35WU4) · IBM Technology · 10 min. Digital sovereignty: who controls the AI, the data and the infrastructure.
- [What is an Air Gap? Air Gapping and Cybersecurity](https://www.youtube.com/watch?v=rh3yG8fsYA8) · Eye on Tech · 3 min. What an air gap is and why regulated customers ask for one.
- [Single Sign-On (SSO) Explained in 10 Minutes | SAML, OIDC & SCIM](https://www.youtube.com/watch?v=5KChrGWFcpk) · ByteMonk · 8 min. Single sign-on with SAML, OIDC and SCIM, the way enterprises connect identity.
- [How to use Cloud Audit Logging](https://www.youtube.com/watch?v=SaLHDNqrZ80) · Google Cloud Tech · 7 min. Audit logging: recording who did what, for security and compliance.
- [What are the 7 principles of GDPR?](https://www.youtube.com/watch?v=NcHSD3fWJiQ) · Privacy Kitchen · 8 min. The seven principles of GDPR every data system must respect.
- [EU AI Act Explained - What You Need to Know](https://www.youtube.com/watch?v=LqqZFqWNtzY) · CyberPaw · 15 min. The EU AI Act: risk categories and what builders must do (2026).

### Want more depth? (longer, optional)

- [Mastering LLM Inference Optimization From Theory to Cost Effective Deployment: Mark Moyou](https://www.youtube.com/watch?v=9tvJ_GYJA-o) · AI Engineer · 34 min. LLM inference optimization from theory to cost-effective deployment.
- [Deep Dive: LLM Quantization, part 3 - FP8, FP4](https://www.youtube.com/watch?v=_hhbzZeQ8sY) · Julien Simon · 38 min. Deep dive on FP8 and FP4 quantization, with benchmarks.
- [Kubernetes Crash Course for Absolute Beginners [NEW]](https://www.youtube.com/watch?v=s_o8dwzRlu4) · TechWorld with Nana · 72 min. Kubernetes crash course for absolute beginners, hands on.

---

← [Phase 4: Model customization](../04-model-customization/README.md) · [Home](../../README.md) · [Phase 6: Forward-deployed practice](../06-forward-deployed-practice/README.md) →
