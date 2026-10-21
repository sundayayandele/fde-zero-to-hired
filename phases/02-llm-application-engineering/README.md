<!-- GENERATED from CURRICULUM.md by scripts/build.py. Do not edit by hand: edit CURRICULUM.md, then run `python scripts/build.py`. -->

# Phase 2: LLM application engineering (weeks 11–15)

← [Phase 1: Software engineering and ML foundations](../01-swe-and-ml-foundations/README.md) · [Home](../../README.md) · [Phase 3: Evaluation and reliability](../03-evaluation-and-reliability/README.md) →

The goal is to build retrieval and agent systems on hosted model APIs that hold up on messy enterprise documents. This is the shared core of every FDE family.

| Week | Topic | What you do |
| --- | --- | --- |
| 11 | How LLMs behave | Tokens, context windows, temperature, cost per call. Prompting patterns: few-shot, structured output, chain of thought. Use at least two providers (for example Mistral and one other). |
| 12 | RAG fundamentals | Document parsing (PDF, tables, OCR), chunking strategies, embeddings, a vector store (pgvector or Qdrant). |
| 13 | Advanced RAG | Hybrid search (BM25 + dense), reranking, query rewriting, metadata filters, citations back to sources. |
| 14 | Agents and tools | Function calling, JSON schemas, ReAct and plan-and-execute loops, an orchestration framework (LangGraph or similar), MCP servers. |
| 15 | Capstone 1 build week | Ship Capstone 1. |

**Resources:** provider docs (Mistral, OpenAI, Anthropic cookbooks); Hugging Face LLM Course; the MCP specification and SDK examples; LangGraph tutorials.

**Code:** start with [fde-02-llm-applications-starter](https://github.com/sundayayandele/fde-02-llm-applications-starter) and complete the exercises in `labs/` week by week. The reference solution, [fde-02-llm-applications](https://github.com/sundayayandele/fde-02-llm-applications), is a cited document assistant over company filings with hybrid retrieval, refusals, streaming and an MCP server. Open it only after you have tried each exercise.

## Capstone 1

This phase ends with **[Capstone 1: Enterprise document assistant](../../capstones/01-enterprise-document-assistant/README.md)**. Read the brief before week 1 of the phase so you build towards it.

---

← [Phase 1: Software engineering and ML foundations](../01-swe-and-ml-foundations/README.md) · [Home](../../README.md) · [Phase 3: Evaluation and reliability](../03-evaluation-and-reliability/README.md) →
