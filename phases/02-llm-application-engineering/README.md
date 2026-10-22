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

## Watch

Optional short videos for each week, all in English with English captions. Moodle learners get them embedded on a Watch page per week.

### Week 11: How LLMs behave

- [Most devs don't understand how LLM tokens work](https://www.youtube.com/watch?v=nKSk_TiR8YA) · Matt Pocock · 11 min. Tokens: what models actually read, and why they drive cost and limits.
- [What is a Context Window? Unlocking LLM Secrets](https://www.youtube.com/watch?v=-QVoIxEpFkM) · IBM Technology · 12 min. Context windows: how much a model can see at once, and what happens at the edge.
- [The Secret Controls for your LLM: Temperature, Top-K, Top-P, etc](https://www.youtube.com/watch?v=MkaazQttbpc) · Gary Explains · 15 min. Temperature, top-k and top-p: the controls that make output steady or creative.
- [Prompting 101 | Code w/ Claude](https://www.youtube.com/watch?v=ysPbXH0LpIE) · Anthropic · 25 min. Prompting 101 from Anthropic: structure, examples and iterating on a real prompt.
- [Getting Structured Output in JSON format](https://www.youtube.com/watch?v=CllLqPwCjD4) · Telusko · 9 min. Structured output: getting JSON you can parse instead of free text.

### Week 12: RAG fundamentals

- [RAG Explained For Beginners](https://www.youtube.com/watch?v=_HQ2H_0Ayy0) · KodeKloud · 10 min. RAG from the ground up: retrieve the right text, then generate from it.
- [What Is Docling? Transforming Unstructured Data for RAG and AI](https://www.youtube.com/watch?v=zSA7ylHP6AY) · IBM Technology · 8 min. Docling: turning messy PDFs, tables and scans into clean text for RAG.
- [Chunking Strategies Explained](https://www.youtube.com/watch?v=ZTOtxiWb2bE) · Redis · 8 min. Chunking strategies and how chunk size changes what retrieval finds.
- [What Are Vector Embeddings? (Explained in 2 Minutes) [Quick Question Ep. 6]](https://www.youtube.com/watch?v=bGNYyK1L41g) · Elastic · 2 min. Vector embeddings in two minutes.
- [What is a Vector Database? Powering Semantic Search & AI Applications](https://www.youtube.com/watch?v=gl1r1XV0SLw) · IBM Technology · 10 min. What a vector database does and why semantic search needs one.
- [How I Added Vector Search to my Course (Postgres + PGVector )](https://www.youtube.com/watch?v=OE279t8377o) · Web Dev Cody · 9 min. Adding vector search to Postgres with pgvector, in a real app.
- [Qdrant Essentials | Building Simple Vector Search in Qdrant](https://www.youtube.com/watch?v=_83L9ZIoOjM) · Qdrant Vector Search · 10 min. Building a simple vector search with Qdrant (official Qdrant).

### Week 13: Advanced RAG

- [Top 3 RAG Retrieval Strategies: Sparse, Dense, & Hybrid Explained](https://www.youtube.com/watch?v=r0Dciuq0knU) · IBM Technology · 9 min. Sparse, dense and hybrid retrieval, and when each wins.
- [BM25 Algorithm and Hybrid Search: AI Explained](https://www.youtube.com/watch?v=lD3_VF5bmWg) · Tejas Kumar · 10 min. BM25, the keyword algorithm inside hybrid search.
- [RAG Reranking Explained: How To Improve RAG Results](https://www.youtube.com/watch?v=R5MPqm0V6aQ) · pixegami · 14 min. Reranking: a second pass that puts the best chunks first.
- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](https://www.youtube.com/watch?v=tLMViADvSNE) · Cole Medin · 13 min. A tour of RAG strategies: query rewriting, contextual retrieval, reranking and more.
- [RAG's Evolution: From Simple Retrieval to Agentic AI](https://www.youtube.com/watch?v=JB2P5Gk23VI) · IBM Technology · 9 min. How RAG evolved from simple retrieval to agentic RAG.
- [Is RAG Still Needed? Choosing the Best Approach for LLMs](https://www.youtube.com/watch?v=UabBYexBD4k) · IBM Technology · 11 min. Is RAG still needed with long-context models? Choosing the right approach.

### Week 14: Agents and tools

- [What is Tool Calling? Connecting LLMs to Your Data](https://www.youtube.com/watch?v=h8gMhXYAv1k) · IBM Technology · 5 min. Tool calling: how a model asks your code to fetch data or take an action.
- [AI Agents, Clearly Explained](https://www.youtube.com/watch?v=FwOTs4UxQS4) · Jeff Su · 10 min. What makes something an agent, and how agents differ from workflows.
- [Tips for building AI agents](https://www.youtube.com/watch?v=LP5OCa20Zpg) · Anthropic · 18 min. Tips for building AI agents, from the team at Anthropic.
- [LangGraph Explained for Beginners](https://www.youtube.com/watch?v=cUfLrn3TM3M) · KodeKloud · 13 min. LangGraph: agents and workflows as graphs you can control and debug.
- [What is MCP? Integrate AI Agents with Databases & APIs](https://www.youtube.com/watch?v=eur8dUO9mvE) · IBM Technology · 4 min. MCP in four minutes: one standard way to connect agents to tools and data.
- [The Model Context Protocol (MCP)](https://www.youtube.com/watch?v=CQywdSdi5iA) · Anthropic · 20 min. The Model Context Protocol explained by Anthropic, who created it.
- [Build Anything With a CUSTOM MCP Server - Python Tutorial](https://www.youtube.com/watch?v=-8k9lGpGQ6g) · Tech With Tim · 26 min. Building a custom MCP server in Python, step by step.

### Week 15: Capstone 1 build week

- [How To Write a USEFUL README On Github](https://www.youtube.com/watch?v=E6NO0rgFub4) · Learn Fast Make Things · 8 min. Writing a README that makes reviewers want to run your project.
- [New to Mermaid? Here's Everything You Need to Know](https://www.youtube.com/watch?v=p4gTbKcOXqk) · Mermaid · 4 min. Architecture diagrams as code with Mermaid, rendered right in GitHub.
- [How to make a SaaS product demo video](https://www.youtube.com/watch?v=Edj_zj4U_9s) · Tom Bruining · 13 min. Recording a short product demo video people actually watch.

### Want more depth? (longer, optional)

- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) · Andrej Karpathy · 3.5 h. Andrej Karpathy's deep dive into how LLMs like ChatGPT are built and behave.
- [How We Build Effective Agents: Barry Zhang, Anthropic](https://www.youtube.com/watch?v=D7_ipDqhtwk) · AI Engineer · 15 min. How Anthropic builds effective agents: keep it simple until complexity pays.
- [Building Agents with Model Context Protocol - Full Workshop with Mahesh Murag of Anthropic](https://www.youtube.com/watch?v=kQmXtrmQ5Zg) · AI Engineer · 1.7 h. Hands-on workshop: building agents with MCP, from Anthropic.
- [LangGraph Complete Course for Beginners – Complex AI Agents with Python](https://www.youtube.com/watch?v=jGg_1h0qzaM) · freeCodeCamp.org · 3.2 h. Full LangGraph course for building complex agents in Python.

---

← [Phase 1: Software engineering and ML foundations](../01-swe-and-ml-foundations/README.md) · [Home](../../README.md) · [Phase 3: Evaluation and reliability](../03-evaluation-and-reliability/README.md) →
