# Forward Deployed ML Engineer: Zero-to-Hired

A 36-week, project-based curriculum that takes you from basic programming to a hireable **Forward Deployed ML Engineer (FDE)**, built from 15 real FDE job postings at Mistral AI, OpenAI, Anthropic, Google DeepMind, Cohere, Databricks, Scale AI, Modal, Hugging Face, Palantir and others.

Every phase ends in a capstone that produces the evidence FDE hiring loops actually check: shipped code, eval numbers, a private deployment and a customer-style write-up.

**Last reviewed:** 2026-10-11 · [Changelog](CHANGELOG.md) · Market evidence is refreshed monthly.

![Curriculum roadmap: 8 phases, 5 capstones](assets/roadmap.png)

## Start here

| If you are… | Start at | Time |
| --- | --- | --- |
| New to programming | [Phase 0](phases/00-programming-and-tooling/README.md) | ~36 weeks |
| A software or data engineer | [Phase 2](phases/02-llm-application-engineering/README.md) (test out of Phase 1 with its exit check) | ~24 weeks |
| An experienced platform or cloud engineer | [Phase 3](phases/03-evaluation-and-reliability/README.md), Capstones 2–5 | ~12–16 weeks |

Rate yourself first with the [skills matrix and 90-day plan](tools/FDE_Skills_Matrix_90_Day_Plan.xlsx), then read the full [curriculum](CURRICULUM.md).

## Phases

| Phase | Weeks | Focus | Ends with |
| --- | --- | --- | --- |
| [0 · Programming and tooling](phases/00-programming-and-tooling/README.md) | 1–4 | Python, Git, SQL, Docker | Exit check |
| [1 · SWE and ML foundations](phases/01-swe-and-ml-foundations/README.md) | 5–10 | APIs, cloud, maths, classical ML, neural nets | Exit check |
| [2 · LLM application engineering](phases/02-llm-application-engineering/README.md) | 11–15 | Prompting, RAG, agents, MCP | [Capstone 1](capstones/01-enterprise-document-assistant/README.md) |
| [3 · Evaluation and reliability](phases/03-evaluation-and-reliability/README.md) | 16–18 | Golden sets, LLM-as-judge, guardrails, CI evals | [Capstone 2](capstones/02-eval-harness-and-red-team/README.md) |
| [4 · Model customization](phases/04-model-customization/README.md) | 19–24 | PyTorch, transformers, SFT, DPO | [Capstone 3](capstones/03-domain-fine-tune/README.md) |
| [5 · Inference and sovereign AI](phases/05-inference-and-sovereign-ai/README.md) | 25–28 | vLLM, quantization, Kubernetes, on-prem | [Capstone 4](capstones/04-sovereign-deployment/README.md) |
| [6 · Forward-deployed practice](phases/06-forward-deployed-practice/README.md) | 29–33 | Discovery, decomposition, ROI, pre-sales | [Capstone 5 (flagship)](capstones/05-flagship-pilot/README.md) |
| [7 · Getting hired](phases/07-getting-hired/README.md) | 34–36 | Portfolio, open source, interview loop | Offers |

## Three rules

1. **Evidence over certificates.** Hiring loops read repos, eval tables and write-ups, not course completions.
2. **Eval before build.** From Phase 3 on, nothing is "done" without a measured baseline and a measured improvement.
3. **Talk like a deployer.** Every capstone ends with a one-page [customer brief](templates/customer-brief.md).

Pick **one domain** in Phase 2 (banking KYC, insurance claims, recruiting, public-sector search…) and keep it through Capstone 5, so your portfolio reads as one coherent customer engagement.

## Repository map

```
CURRICULUM.md        Full curriculum in one file (the source of truth)
docs/                Market research, interview prep, rubric, sources (generated)
phases/              One folder per phase: weekly plan, resources, exit check (generated)
capstones/           One folder per capstone: brief, must-include, definition of done (generated)
templates/           Customer brief, decision memo, data card, model card, capstone README
tools/               Skills matrix + 90-day plan (Excel)
scripts/             build.py, check_repo.py, check_links.py
plugins/             fde-maintainer Claude Code plugin (skills, agents, command, hooks)
AGENTS.md, CLAUDE.md Instructions for AI agents maintaining the repo
.github/             Issue templates, consistency check, monthly refresh reminder
```

## Keeping it current

Edit `CURRICULUM.md`, then run `python scripts/build.py` and `python scripts/check_repo.py`. Pages in `phases/`, `capstones/` and `docs/` are generated from it. A monthly GitHub Action opens a refresh issue; the [fde-maintainer plugin](plugins/fde-maintainer/README.md) runs the refresh in Claude Code.

## Track your progress

Fork this repo, then open a **Weekly progress** issue each week and a **Capstone submission** issue for each capstone (see `.github/ISSUE_TEMPLATE`). Score each capstone with the [rubric](docs/rubric.md).

## Author

Created by **Sunday Ayandele**, Managing Consultant and platform engineer working on enterprise and sovereign AI deployment.

## License

Content is licensed under [CC BY-SA 4.0](LICENSE). Share and adapt it with attribution; derivatives must use the same license.

Job postings are cited as evidence of market requirements as of October 2026. Many have since closed; check each company's careers page for current openings.
