<!-- GENERATED from CURRICULUM.md by scripts/build.py. Do not edit by hand: edit CURRICULUM.md, then run `python scripts/build.py`. -->

# Phase 1: Software engineering and ML foundations (weeks 5–10)

← [Phase 0: Programming and tooling](../00-programming-and-tooling/README.md) · [Home](../../README.md) · [Phase 2: LLM application engineering](../02-llm-application-engineering/README.md) →

The goal is to write clean, tested Python, ship a small web API to the cloud, and explain how a neural network learns. Every FDE posting treats this as assumed, not taught.

| Week | Topic | What you do |
| --- | --- | --- |
| 5 | Backend APIs | FastAPI, Pydantic, async, auth basics, OpenAPI docs. |
| 6 | Front-end just enough | Basic React or Streamlit/Gradio; call your API from a UI. |
| 7 | Cloud and deployment | Deploy a container to one cloud (AWS, Azure or GCP); secrets, logging, IAM basics. |
| 8 | Maths for ML | Vectors, matrices, dot products, gradients, probability and softmax. Intuition, not proofs. |
| 9 | Classical ML | Train/test split, overfitting, metrics (precision, recall, F1), scikit-learn on a tabular dataset. |
| 10 | Neural networks | Build a tiny network and backpropagation from scratch, then the same in PyTorch. |

**Resources:** FastAPI official tutorial; 3Blue1Brown *Essence of Linear Algebra* and *Neural Networks*; Andrej Karpathy *Neural Networks: Zero to Hero* (first videos); fast.ai *Practical Deep Learning for Coders*.

**Exit check:** a deployed FastAPI service with a small UI that serves a scikit-learn or PyTorch model, plus a README explaining the metric you chose and why. If you can already do this, skip to Phase 2.

---

← [Phase 0: Programming and tooling](../00-programming-and-tooling/README.md) · [Home](../../README.md) · [Phase 2: LLM application engineering](../02-llm-application-engineering/README.md) →
