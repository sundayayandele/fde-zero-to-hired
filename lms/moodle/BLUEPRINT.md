# Moodle course blueprint: FDE Zero-to-Hired

How to run this curriculum as a Moodle course at [itlearning.tech](https://itlearning.tech). GitHub stays the source of truth for content and code; Moodle runs the learner journey: enrolment, progress, grading, badges and the certificate.

**Rule:** never copy curriculum text into Moodle. Link to the GitHub page, so the monthly refresh updates the course for free.

Built for Moodle 5.2 with Custom certificate (`mod_customcert`) installed. No other plugins are needed.

## 1. Course settings

| Setting | Value |
| --- | --- |
| Category | Forward Deployed Engineering |
| Full name | Forward Deployed ML Engineer: Zero-to-Hired |
| Short name | FDE-Z2H |
| Course ID number | fde-z2h-2026 |
| Visibility | Hide until reviewed |
| Format | Custom sections, 9 sections (Start here + Phases 0 to 7) |
| Course layout | Show one section per page |
| Enable completion tracking | Yes |
| Show activity dates / completion conditions | Yes / Yes |
| Groups | No groups (add one group per cohort later) |
| Course summary | A 36-week, project-based path from basic programming to a hireable Forward Deployed ML Engineer. Built from 15 real FDE job postings. Every phase ends in evidence hiring loops check: shipped code, eval numbers, a private deployment and a customer-ready write-up. |

## 2. Link targets

All links use `https://github.com/sundayayandele/` as the base.

| Name in Moodle | Path after the base |
| --- | --- |
| Full curriculum | `fde-zero-to-hired/blob/main/CURRICULUM.md` |
| Phase N page | `fde-zero-to-hired/blob/main/phases/<slug>/README.md` |
| Capstone N brief | `fde-zero-to-hired/blob/main/capstones/<slug>/README.md` |
| Rubric | `fde-zero-to-hired/blob/main/docs/rubric.md` |
| Skills matrix | `fde-zero-to-hired/raw/main/tools/FDE_Skills_Matrix_90_Day_Plan.xlsx` |
| Starter (Phases 0 to 3) | `fde-0N-<name>-starter` |
| Codespaces for the starter | `https://codespaces.new/sundayayandele/fde-0N-<name>-starter?quickstart=1` |
| Reference solution | `fde-0N-<name>` |

Phase slugs: `00-programming-and-tooling`, `01-swe-and-ml-foundations`, `02-llm-application-engineering`, `03-evaluation-and-reliability`, `04-model-customization`, `05-inference-and-sovereign-ai`, `06-forward-deployed-practice`, `07-getting-hired`.

Capstone slugs: `01-enterprise-document-assistant`, `02-eval-harness-and-red-team`, `03-domain-fine-tune`, `04-sovereign-deployment`, `05-flagship-pilot`.

Code repos: Phase 0 `fde-00-programming`, Phase 1 `fde-01-foundations`, Phase 2 `fde-02-llm-applications`, Phase 3 `fde-03-evaluation`.

Set every URL resource to **Display: Open** (GitHub refuses to be embedded) and **Open in new window** off; learners use the browser back button.

## 3. Sections and activities

Completion rules use these short codes:

| Code | Moodle completion condition |
| --- | --- |
| **V** | Learner must view the activity |
| **S** | Learner must make a submission |
| **G** | Learner must receive a grade |
| **P** | Learner must receive a passing grade |
| **Pn** | Forum: learner must post *n* discussions or replies |

### Section 0: Start here

| Activity | Type | Settings | Completion |
| --- | --- | --- | --- |
| Welcome and how this course works | Page | Explain: GitHub holds content and code; Moodle tracks progress; capstones are graded with the rubric; reference solutions unlock after you try | V |
| Full curriculum | URL | Full curriculum link | V |
| Rate yourself: skills matrix | URL | Skills matrix link | V |
| Set up GitHub and Codespaces | Assignment | Online text: "Your GitHub username and the URL of your copy of `fde-00-programming-starter` (Use this template)". No grade | S |
| Questions and help | URL | GitHub Discussions: `fde-zero-to-hired/discussions` | none |

### Sections 1 and 2: Phases 0 and 1 (foundations)

Same pattern for both. N = 0 or 1, W = weeks in the phase (4 and 6).

| Activity | Type | Settings | Completion |
| --- | --- | --- | --- |
| Phase N: weekly plan and resources | URL | Phase N page | V |
| Start the lab: starter repo | URL | Starter repo. Description: "Click Use this template, then work through `labs/` until `make exercises` is green" | V |
| Open the starter in Codespaces | URL | Codespaces link | none |
| Weekly check-ins | Forum (standard, general use) | Prompt: done this week, evidence link, stuck on, next week | P*W* |
| Phase N exit check | Assignment | Online text: repo URL, CI link, one paragraph on what you learned. Grade type: Scale "Not yet / Competent". Additional attempts: manually | S + G |
| Reference solution | URL | Reference repo. **Restrict access:** activity completion of this phase's "Weekly check-ins" forum (every week posted). Moodle has no "submitted but not yet graded" condition, so the check-ins are the proof of effort | V |

### Sections 3 to 7: Phases 2 to 6 (each ends in a capstone)

| Phase | Weeks | Capstone | Code repos |
| --- | --- | --- | --- |
| 2 LLM application engineering | 11–15 | 1 Enterprise document assistant | fde-02 starter and reference |
| 3 Evaluation and reliability | 16–18 | 2 Eval harness and red-team report | fde-03 starter and reference |
| 4 Model customization | 19–24 | 3 Domain fine-tune with a defended decision | not yet |
| 5 Inference and sovereign AI | 25–28 | 4 Sovereign deployment | not yet |
| 6 Forward-deployed practice | 29–33 | 5 Flagship end-to-end pilot | not yet |

Activities in each:

| Activity | Type | Settings | Completion |
| --- | --- | --- | --- |
| Phase N: weekly plan and resources | URL | Phase N page | V |
| Start the lab / Codespaces / Reference solution | URL ×3 | Phases 2 and 3 only, as in Phases 0 and 1, including the same restriction on the reference solution | V / none / V |
| Weekly check-ins | Forum | As above | P*W* |
| Capstone N brief | URL | Capstone N brief | V |
| **Capstone N submission** | Assignment | See section 4 | **P** |

Phase 6 also gets a **Workshop** "Peer review: customer brief" (submission: the one-page brief; assessment form: the Communication row of the rubric; 2 peer reviews each). Completion: submission and assessments done.

### Section 8: Phase 7, getting hired

| Activity | Type | Settings | Completion |
| --- | --- | --- | --- |
| Phase 7: portfolio, interviews, applications | URL | Phase 7 page | V |
| Interview loop preparation | URL | `fde-zero-to-hired/blob/main/docs/interview-prep.md` | V |
| Mock decomposition interviews | BigBlueButton (optional) | One recurring room; record sessions | none |
| Evidence checklist | Assignment | Online text: one link per line of the evidence checklist in the rubric page. Scale "Not yet / Complete" | P |
| Certificate | Custom certificate | See section 6 | none |

## 4. Capstone assignment settings (all five)

| Setting | Value |
| --- | --- |
| Name | Capstone N submission: <capstone name> |
| Description | Link to the capstone brief. "Submit links, not files: repo, demo video, customer brief or memo. Your repo must have a green CI badge." |
| Submission types | Online text (word limit off). File submissions off |
| Require students to click the submit button | Yes |
| Additional attempts | Manually; maximum attempts unlimited |
| Grade type | Point, maximum grade 20 |
| Grading method | **Rubric** (section 5) |
| Grade to pass | 14 (set under Grade, or in the gradebook) |
| Anonymous submissions | No |
| Notify graders | Yes |
| Completion | Receive a passing grade |

Gradebook: put the five capstones in a category **Capstones** (natural weighting, 100 points). Exit checks and the evidence checklist use scales and carry no weight.

## 5. Rubric, ready to paste

In each capstone: **Advanced grading → Define new grading form from scratch → Rubric**. Name it `FDE capstone rubric` and tick **Save as a template** on the first one, so the other four can reuse it.

**Rubric options:** untick **Calculate grade having a minimum score of the rubric**. With it ticked, Moodle maps the lowest possible score (5) to a grade of 0, and a learner scoring 14 would get about 12. Unticked, the grade equals the rubric total out of 20. Tick **Allow users to preview rubric** and **Display rubric description to those being graded**.

**Description:** Score each criterion from 1 to 4. A capstone passes at 14 of 20 with no criterion below 2.

| Criterion | 1 point: Not yet | 2 points: Developing | 3 points: Hireable | 4 points: Standout |
| --- | --- | --- | --- | --- |
| Problem framing | No stated user or metric | Metric stated after the build | Metric agreed before building, tied to a business outcome | Metric validated with a real stakeholder |
| Engineering quality | Runs only on your machine | Runs from README with effort | Reproducible, tested, CI green | Clean abstractions others could reuse |
| Evidence | Screenshots and claims | One headline number | Baseline vs improvement with method explained | Multiple metrics, error analysis, failure cases shown |
| Deployment | Notebook only | Local container | Deployed with monitoring | Private or production-like, with security notes |
| Communication | Code only | README describes what | README explains why and trade-offs | Customer-ready brief or talk a non-engineer understands |

The wording matches [docs/rubric.md](../../docs/rubric.md). If CURRICULUM.md changes the rubric, update the Moodle template too.

**"No criterion below 2" is not something Moodle can enforce.** Grader rule: if any criterion scores 1 and the total is still 14 or more, override the grade to 13 in the gradebook, say which criterion in the feedback, and reopen the submission.

## 6. Badges and certificate

Badge images: 300×300 PNG, one colour per phase, plain text "FDE · Capstone N". Issuer: ITLearning. Expiry: none.

| Badge | Description | Criteria |
| --- | --- | --- |
| FDE Capstone 1: Document assistant | Built a cited, refusing document assistant with hybrid retrieval and an MCP tool | Activity completion: Capstone 1 submission |
| FDE Capstone 2: Evaluation and red team | Measured an LLM system with a calibrated judge, red-teamed it and gated releases in CI | Activity completion: Capstone 2 submission |
| FDE Capstone 3: Defended fine-tune | Fine-tuned an open-weight model and defended prompt vs RAG vs fine-tune with numbers | Activity completion: Capstone 3 submission |
| FDE Capstone 4: Sovereign deployment | Served a fine-tuned model privately with monitoring and a reference architecture | Activity completion: Capstone 4 submission |
| FDE Capstone 5: Flagship pilot | Ran an end-to-end pilot for a real organisation, with a case study and presentation | Activity completion: Capstone 5 submission |
| FDE Zero-to-Hired graduate | Completed all five capstones and the evidence checklist | Awarded badges: all five above, plus activity completion of Evidence checklist |

Each capstone badge fires when its assignment is complete, which requires a passing grade. Badges and completion need Moodle cron running every minute.

**Certificate** (Custom certificate activity "Certificate of completion"):

- Restrict access: activity completion of all five capstone submissions and the Evidence checklist.
- Elements: Student name, Course name, Date (course completion date), Code (unique verification code), QR code (links to the verification page), Text: "Evidence: see the learner's capstone repositories on GitHub."
- Allow anyone to verify a certificate: Yes.

**Course completion** (Course administration → Course completion): all five capstone submissions and the Evidence checklist complete.

## 7. Build order

1. Category and course, hidden.
2. Sections and URL resources.
3. Forums and exit checks.
4. Capstone assignments, then the rubric on Capstone 1, saved as a template and reused on 2 to 5.
5. Restrictions on the reference-solution links.
6. Course completion, badges, certificate.
7. Check as a student (switch role), then unhide.
