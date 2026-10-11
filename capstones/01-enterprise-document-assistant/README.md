<!-- GENERATED from CURRICULUM.md by scripts/build.py. Do not edit by hand: edit CURRICULUM.md, then run `python scripts/build.py`. -->

# Capstone 1: Enterprise document assistant

[Home](../../README.md) · [Capstone 2](../02-eval-harness-and-red-team/README.md) →

Built during [Phase 2: LLM application engineering](../../phases/02-llm-application-engineering/README.md).

**Brief:** a domain team (pick your domain) wastes hours searching policy and procedure PDFs. Build an assistant that answers questions with citations and refuses when the documents do not contain the answer.

**Must include**

- Ingestion of at least 200 real public documents in your domain (regulations, policies, annual reports), including tables.
- Hybrid retrieval with a reranker, and every answer citing the source page.
- One agentic tool, for example a structured lookup or calculator, exposed through an MCP server.
- A FastAPI backend with streaming, and a simple UI.

**Definition of done:** a public repo, a 2-minute demo video, and a README with an architecture diagram and known failure cases.

**Proves:** RAG, agents, MCP, API and front-end delivery. These match requirements in the Anthropic, Cohere, Databricks and Mistral postings.

## Templates to use

- [capstone-README.md](../../templates/capstone-README.md)
- [customer-brief.md](../../templates/customer-brief.md)

## Submit

1. Publish your capstone in its own public repo, using the [capstone README template](../../templates/capstone-README.md).
2. Score it against the [rubric](../../docs/rubric.md): pass at 14/20 with no criterion below 2.
3. Open a **Capstone submission** issue in your fork of this repo with the links.

---

[Home](../../README.md) · [Capstone 2](../02-eval-harness-and-red-team/README.md) →
