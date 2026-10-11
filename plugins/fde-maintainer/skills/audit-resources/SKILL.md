---
name: audit-resources
description: Audit the curriculum's links, learning resources and named tools for rot (dead links, retired courses, renamed or superseded libraries, outdated practices) and fix them. Use when asked to check links, verify resources are current, or during the monthly refresh.
---

# Audit resources and tools

## 1. Mechanical link check

```bash
python scripts/check_links.py --external
```

- **DEAD (404/410):** must be fixed. Find the moved page or a replacement.
- **REVIEW (403, 429, timeouts):** job boards and some sites block bots. Open each with WebFetch before deciding; a closed job posting stays (see `refresh-fde-market`).

## 2. Resource currency

For each `**Resources:**` line in `CURRICULUM.md`, confirm with a quick search or page fetch:

- the course, book or guide still exists and is maintained;
- a newer edition or a clearly better free resource has not replaced it.

Replace only with something at least as good and free or widely available. Keep one line per phase; don't grow the lists.

## 3. Tools and practices

Check the named tools are still the mainstream choice and correctly named. Current watch list:

| Area | Named in curriculum | Check for |
| --- | --- | --- |
| Agents and tools | MCP, LangGraph, function calling | Spec version changes, framework renames, a new de facto standard |
| RAG | pgvector, Qdrant, BM25 + dense, rerankers | Retired libraries; new defaults in hybrid search |
| Evals | RAGAS, DeepEval, LLM-as-judge, Langfuse, LangSmith | Renames, acquisitions, new widely used eval tools |
| Fine-tuning | TRL, PEFT, mistral-finetune, LoRA/QLoRA, DPO/ORPO | Deprecated trainers or repos; new preference methods in common use |
| Serving | vLLM, SGLang, TGI, AWQ/GPTQ/FP8 | Projects in maintenance mode; new quantization defaults |
| Platform | Kubernetes, Helm, GPU Operator, OpenShift | Major changes to GPU scheduling |
| Regulation | GDPR, EU AI Act | Obligations that now apply by date |

Change a tool name only when the evidence is clear (official docs, release notes or a deprecation notice you opened). Otherwise list it as "watch" in the report.

## 4. Apply and record

Edit `CURRICULUM.md` (never generated files), then:

```bash
python scripts/build.py
python scripts/check_repo.py
```

Add a `CHANGELOG.md` line under `## [Unreleased]`, for example `- Resources: replaced dead SQLBolt link; TGI noted as maintenance-only in Phase 5.`

## Report

A table of findings: item, location, status (fixed / replaced / watch), evidence link.
