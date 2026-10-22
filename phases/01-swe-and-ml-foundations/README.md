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

**Code:** start with [fde-01-foundations-starter](https://github.com/sundayayandele/fde-01-foundations-starter) and complete the exercises in `labs/` week by week. The reference solution, [fde-01-foundations](https://github.com/sundayayandele/fde-01-foundations), is a complaint-routing classifier that compares scikit-learn, PyTorch and DistilBERT and sends uncertain cases to a person. Open it only after you have tried each exercise.

**Exit check:** a deployed FastAPI service with a small UI that serves a scikit-learn or PyTorch model, plus a README explaining the metric you chose and why. If you can already do this, skip to Phase 2.

## Watch

Optional short videos for each week, all in English with English captions. Moodle learners get them embedded on a Watch page per week.

### Week 5: Backend APIs

- [Python FastAPI Tutorial (Part 1): Getting Started - Web App + REST API](https://www.youtube.com/watch?v=7AMjmCTumuo) · Corey Schafer · 24 min. Building a web app and REST API with FastAPI, step by step (2026).
- [Pydantic Tutorial • Solving Python's Biggest Problem](https://www.youtube.com/watch?v=XIdQ6gO3Anc) · pixegami · 11 min. Pydantic models: validating the data that comes into your API.
- [AsyncIO, await, and async - Concurrency in Python](https://www.youtube.com/watch?v=K56nNuBEd0c) · Socratica · 9 min. async and await: how one server handles many requests at once.
- [Session vs Token Authentication in 100 Seconds](https://www.youtube.com/watch?v=UBUNrFtufWo) · Fireship · 2 min. Sessions vs tokens: the two ways a server remembers who you are.
- [OAuth 2 Explained In Simple Terms](https://www.youtube.com/watch?v=ZV5yTm4pT8g) · ByteByteGo · 5 min. OAuth 2 in plain terms, the standard behind 'Sign in with...'.

### Week 6: Front-end just enough

- [React in 100 Seconds](https://www.youtube.com/watch?v=Tn6-PIqc4UM) · Fireship · 2 min. What React is and why most web front ends use it.
- [Streamlit: The Fastest Way To Build Python Apps?](https://www.youtube.com/watch?v=D0D4Pa22iG0) · pixegami · 12 min. Streamlit: a working UI for your model in pure Python.
- [Gradio Crash Course - Fastest way to build & share Machine Learning apps](https://www.youtube.com/watch?v=eE7CamOE-PA) · AssemblyAI · 14 min. Gradio: shareable demos for ML models, the format Hugging Face Spaces uses.

### Week 7: Cloud and deployment

- [The Basics You Need to Know about AWS, Azure, and Google Cloud](https://www.youtube.com/watch?v=wFsOjHgvUfM) · ArjanCodes · 7 min. What AWS, Azure and Google Cloud offer, and how they line up.
- [How to deploy a container image to Cloud Run](https://www.youtube.com/watch?v=zihPR6TeqjY) · Google Cloud Tech · 3 min. Deploying a container to Cloud Run in three minutes (official Google Cloud).
- [Learn AWS IAM in less than 10 minutes](https://www.youtube.com/watch?v=9Pk2J_5qnlk) · AWS Developers · 9 min. IAM basics: users, roles and least-privilege permissions (official AWS).
- [Secrets Management: Secure Credentials & Avoid Data Leaks](https://www.youtube.com/watch?v=BqekRTA6VCs) · IBM Technology · 10 min. Keeping API keys and passwords out of code with a secrets manager.
- [Why Most Python Logging Setups Fail in Production](https://www.youtube.com/watch?v=pxuXaaT1u3k) · ArjanCodes · 11 min. Logging that still helps you when something breaks in production.

### Week 8: Maths for ML

- [Vectors | Chapter 1, Essence of linear algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs) · 3Blue1Brown · 10 min. Vectors: the language every embedding and model weight is written in.
- [Linear transformations and matrices | Chapter 3, Essence of linear algebra](https://www.youtube.com/watch?v=kYB8IZa5AuE) · 3Blue1Brown · 11 min. Matrices as transformations, the picture behind every neural network layer.
- [Dot products and duality | Chapter 9, Essence of linear algebra](https://www.youtube.com/watch?v=LyGKycYT2v0) · 3Blue1Brown · 14 min. Dot products: the operation behind similarity search and attention.
- [Gradient descent, how neural networks learn | Deep Learning Chapter 2](https://www.youtube.com/watch?v=IHZwWFHWa-w) · 3Blue1Brown · 21 min. Gradient descent: how a model improves by following the slope.
- [The Main Ideas behind Probability Distributions](https://www.youtube.com/watch?v=oI3hZJqXJuc) · StatQuest with Josh Starmer · 5 min. Probability distributions, the main ideas, in five minutes.
- [Softmax - What is the Temperature of an AI??](https://www.youtube.com/watch?v=YjVuJjmgclU) · MarbleScience · 9 min. Softmax and temperature: how model scores become probabilities.

### Week 9: Classical ML

- [Machine Learning Explained in 100 Seconds](https://www.youtube.com/watch?v=PeMlggyqz0Y) · Fireship · 3 min. Machine learning in 100 seconds: the big picture before the details.
- [Machine Learning Fundamentals: Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw) · StatQuest with Josh Starmer · 6 min. Cross-validation: testing a model on data it has not seen.
- [Machine Learning Fundamentals: Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA) · StatQuest with Josh Starmer · 7 min. Bias and variance: why models underfit or overfit.
- [Machine Learning Fundamentals: The Confusion Matrix](https://www.youtube.com/watch?v=Kdsp6soqA7o) · StatQuest with Josh Starmer · 7 min. The confusion matrix: where every classification metric comes from.
- [Never Forget Again! // Precision vs Recall with a Clear Example of Precision and Recall](https://www.youtube.com/watch?v=qWfzIYCvBqo) · Kimberly Fessel · 5 min. Precision vs recall, with an example you will remember.
- [Simple Machine Learning Code Tutorial for Beginners with Sklearn Scikit-Learn](https://www.youtube.com/watch?v=-IvNzmrcyUM) · Python Simplified · 24 min. Training and evaluating a first model with scikit-learn.

### Week 10: Neural networks

- [But what is a neural network? | Deep learning chapter 1](https://www.youtube.com/watch?v=aircAruvnKk) · 3Blue1Brown · 19 min. What a neural network is, built up visually from scratch.
- [Backpropagation, intuitively | Deep Learning Chapter 3](https://www.youtube.com/watch?v=Ilg3gGewQ5U) · 3Blue1Brown · 13 min. Backpropagation, intuitively: how each weight learns its share of the error.
- [Backpropagation calculus | Deep Learning Chapter 4](https://www.youtube.com/watch?v=tIeHLnjs5U8) · 3Blue1Brown · 10 min. The calculus of backpropagation, for when you build it yourself.
- [PyTorch in 100 Seconds](https://www.youtube.com/watch?v=ORMx45xqWkA) · Fireship · 3 min. PyTorch in 100 seconds: what the framework does for you.
- [The Fundamentals of Autograd](https://www.youtube.com/watch?v=M0fX15_-xrY) · PyTorch · 14 min. Autograd: how PyTorch computes gradients automatically (official PyTorch).
- [Create a Basic Neural Network Model - Deep Learning with PyTorch 5](https://www.youtube.com/watch?v=JHWqWIoac2I) · John Elder · 16 min. Building and training a basic neural network model in PyTorch.

### Want more depth? (longer, optional)

- [The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) · Andrej Karpathy · 2.4 h. Andrej Karpathy builds backpropagation from scratch (micrograd). The best long watch for week 10.
- [Build Your First Pytorch Model In Minutes! [Tutorial + Code]](https://www.youtube.com/watch?v=tHL5STNJKag) · Rob Mulla · 32 min. Rob Mulla builds a first PyTorch model end to end, with code.

---

← [Phase 0: Programming and tooling](../00-programming-and-tooling/README.md) · [Home](../../README.md) · [Phase 2: LLM application engineering](../02-llm-application-engineering/README.md) →
