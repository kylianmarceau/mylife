---
tags:
  - ai-systems
---

# Agent Architectures V: Generative AI In Practice And Measurable Client Value

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3044S AI Systems  
> **Source**: [CSC3044S-Lecture 9-Agent Architectures V(LLMs).pdf](../../Sources/CSC3044S%20-%20AI%20Systems/CSC3044S-Lecture%209-Agent%20Architectures%20V%28LLMs%29.pdf), Isazi guest lecture, September 2026; presenter not named in the supplied PDF, pages 1-35  
> **Generated**: 2026-10-01  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Public Narratives And Grounded Evaluation|Public Narratives And Grounded Evaluation]]
  - [[#Consolidating Information For A New Client|Consolidating Information For A New Client]]
  - [[#Prompting For Opportunity Discovery|Prompting For Opportunity Discovery]]
  - [[#Structured Opportunities And Expert Selection|Structured Opportunities And Expert Selection]]
  - [[#Demos And AI-Generated Presentation Content|Demos And AI-Generated Presentation Content]]
  - [[#Legal-Document Review As A Search-Assistance Task|Legal-Document Review As A Search-Assistance Task]]
  - [[#Initial And Later Implementations|Initial And Later Implementations]]
  - [[#Measuring Client Impact|Measuring Client Impact]]
  - [[#Choosing An Appropriate Solution|Choosing An Appropriate Solution]]

---

## Core Content

### Public Narratives And Grounded Evaluation

#### Definitions

> **Generative AI**: AI that produces content such as text, code, and images from supplied context.

> **Business value**: An improvement to an operational outcome that matters to the client.

The opening material contrasts hype and investment narratives with rogue-agent stories, doomsday predictions, and embarrassing fabricated content. The screenshots serve as motivation for careful deployment; they are not evidence that every AI system will behave similarly.

| Opening visual | Concern it illustrates |
|---|---|
| AI-infrastructure expenditure chart | Large spending and hype do not establish useful task outcomes |
| Unexpected deletion or external-action anecdotes | Autonomous actions need reliable execution boundaries |
| Catastrophic-risk headline | Public discussion can become dramatic |
| Fabricated policy-citation headline | Generated factual claims require review |

*The source's news and expenditure visuals illustrate public narratives. They are not independently verified incident reports or current financial forecasts in these notes.*

The practical aim is to identify a suitable problem, integrate AI into a useful workflow, review its output, and measure its impact.

### Consolidating Information For A New Client

#### Definitions

> **Consolidation**: Combining dispersed information into a coherent, inspectable account.

> **Domain knowledge**: Understanding of the client's subject area and operations.

> **Pain point**: A specific operational difficulty or inefficiency.

A new client may supply little context, operate in an unfamiliar domain, and be unsure what solution is wanted. AI can help consolidate workshops, deep dives, and documents; experts still need to identify what creates value.

![Consolidating Information For A New Client: client opportunity funnel](../../diagrams/CSC3044S-AI%20Systems/09_Generative_AI_In_Practice/client_opportunity_funnel.svg)

*The consulting funnel combines AI consolidation with substantial expert effort to narrow broad evidence into a small set of valuable opportunities.*

| Source funnel stage | Recorded quantity |
|---|---|
| Evidence | $2$ workshops, $8$ deep dives, $63$ files |
| Analysis effort | AI-assisted corpus analysis and more than $200$ expert hours |
| Mapped information | $18$ metrics and $75$ pain points |
| Initial ideas | More than $100$ |
| Discovered opportunities | $17$ |
| Final priority set | $4$ |

These values demonstrate a case-study workflow, not a prescribed staffing ratio or guaranteed AI productivity multiplier.

### Prompting For Opportunity Discovery

#### Definitions

> **Impact**: The expected improvement from an opportunity.

> **Effort / implementation feasibility**: The work and practical constraints involved in delivering the opportunity.

An analysis prompt should:

1. Read the supplied documents carefully.
2. Identify explicit and implicit inefficiencies, technological gaps, and operational challenges.
3. Consider opportunities for automation, customer experience, products/services, and cost reduction.
4. Include both immediate tactical and longer-term strategic opportunities.
5. Evaluate impact and feasibility in the client's business context.

| Required opportunity field | Purpose |
|---|---|
| Pain point | State the actual problem |
| Proposed improvement | Explain how the solution addresses it |
| Appropriate solution type | Automation, predictive analytics, NLP, ML, or another technique |
| Business impact | Connect to workshop or deep-dive metrics where available |
| Complexity and feasibility | Identify implementation burden and constraints |
| Impact and effort scores | Support prioritisation with explicit reasons |

Scores must have a defined scale and justified assumptions; the PDF asks for scores but does not specify one universal ranking formula. An impressive model-generated list is a starting point for expert assessment.

### Structured Opportunities And Expert Selection

| Opportunity | Problem statement | Proposed solution | Business value |
|---|---|---|---|
| AI-powered report builder | Bespoke reports consume substantial consultant effort; ungoverned personal AI tools produce inconsistent results | Authoring tool using natural-language requests and validated templates | Protect and standardise high-value deliverables |
| Research and analysis recommendation agent | Existing research and data are underused; manual sourcing is slow | Recommend relevant research/benchmarks by engagement context; consultant selects before generation/insertion | Turn historical intellectual property into differentiated client insight |

*A reconstruction of the structured final-output table. Each idea connects a specific problem, a proposed mechanism, and client value.*

Expert review checks whether the evidence supports each opportunity, whether AI is appropriate, and whether the proposed solution can realistically be delivered. Consolidation accelerates analysis; it does not remove the need for domain judgment.

### Demos And AI-Generated Presentation Content

#### Definitions

> **Demo / prototype**: A limited implementation used to explore or demonstrate an idea.

> **Vibe coding**: Informal, prompt-driven software creation with substantial reliance on generated code.

The talk presents professional demos as a useful setting for rapid AI-assisted development. A demo can make an idea concrete without establishing production reliability or complete requirements.

For presentation drafting, the initial prompt asks for a plain professional deck, grouped logically from a supplied Markdown file, aimed at final-year students familiar with LLMs and agents.

| Prompt refinement | Intended effect |
|---|---|
| Minimise images | Keep attention on the content |
| Avoid verbose or exaggerated wording and imagery | Reduce sensational presentation |
| Keep a positive tone | Support a constructive industry discussion |

The example output remains dramatic in places despite style instructions. Review client-facing content for factual support, tone, audience fit, and structure. A style change does not correct an unsupported claim by itself.

### Legal-Document Review As A Search-Assistance Task

#### Definitions

> **Optical character recognition (OCR)**: Conversion of scanned or image-based text into machine-readable text.

> **Fuzzy matching**: Matching text approximately rather than requiring exact equality.

> **Human review**: Verification of model findings by the responsible expert.

The system helps a legal team identify where to look in large documents. It supplies relevant clauses and locations so reviewers can assess the evidence faster.

![Legal-Document Review As A Search-Assistance Task: legal document review pipeline](../../diagrams/CSC3044S-AI%20Systems/09_Generative_AI_In_Practice/legal_document_review_pipeline.svg)

*The document-analysis pipeline helps reviewers find relevant evidence. The human verifies findings and their source locations before accepting the assessment.*

| Illustrative document question | Answer recorded in the case-study example |
|---|---|
| May the trust bind assets as security? | Yes; clause 4.1, page 5 |
| May it acquire movable and immovable property? | Yes; clause 5.3, page 8 |
| May it open a bank account? | Yes; clause 7.2, page 10 |
| May it borrow money? | No; clause 6.5, page 9 |
| May it subscribe to shares in a legal entity? | Yes; clause 9.4, page 12 |

These are illustrative answers about the example document, not general legal rules. The actual trust instrument and cited clause must be checked in each review.

### Initial And Later Implementations

The initial workflow, constrained by available LLM use at the time, used:

1. A local Python OCR model to extract text.
2. Fuzzy matching for common phrases.
3. A small local LLM for difficult cases.
4. A human reviewer to confirm the findings.

| Initial version | Later fully LLM-based analysis |
|---|---|
| Worked usefully | Reported to work better in this case |
| Missed some clauses entirely | Missed fewer clauses |
| Similar phrases could retrieve unrelated clauses | Context narrowed findings more accurately |
| Human checks faster than searching the whole document | Human checks faster still because findings were more accurate |

The later approach preserves human review. Contextual interpretation helps distinguish clauses that share surface wording but differ in meaning.

The PDF does not identify the later model, exact prompt, dataset, or formal accuracy measurements. It supports the reported workflow and time comparison, not a claim that every LLM solution always outperforms fuzzy matching.

### Measuring Client Impact

#### Definitions

> **Success metric**: A defined measure of the outcome the solution should improve.

> **Baseline**: Performance before the change or under a reference process.

The agreed metric is time taken to vet a document.

| Process | Reported time per document | Speed-up relative to original | Time reduction relative to original |
|---|---:|---:|---:|
| Original manual review | $1.5$ hours $=90$ minutes | $1\times$ | $0\%$ |
| First solution | $15$ minutes | $90/15=6\times$ | $(90-15)/90\approx83.3\%$ |
| Later solution | $5$ minutes | $90/5=18\times$ | $(90-5)/90\approx94.4\%$ |

The later solution takes one third of the first solution's time, an additional reduction of $(15-5)/15\approx66.7\%$.

For before/after times $T_0$ and $T_1$:

$$
\operatorname{speedup}=\frac{T_0}{T_1},\qquad
\operatorname{time\ reduction}=\frac{T_0-T_1}{T_0}\times100\%.
$$

> [!warning] <span style="color: #ffc778">Measure quality alongside speed</span>
> These are derived calculations using the case-study times. The talk does not state a sample size, distribution of review times, or controlled-study methodology. Faster review should still be assessed alongside evidence accuracy and clauses missed.  

A practical evaluation process is:

1. Agree the relevant metric with the client before building.
2. Record the baseline on representative work.
3. Measure the assisted process under comparable conditions.
4. Include the time spent checking and correcting AI output.
5. Review quality as well as speed.
6. Use the comparison to decide whether the workflow delivers value.

### Choosing An Appropriate Solution

| Decision | Reason |
|---|---|
| Review generated client-facing content | Plausible language can contain wrong claims or unsuitable tone |
| Choose the tool for the problem | Some tasks are better served by conventional rules, search, or simpler automation |
| Keep an expert in consequential review | The system assists evidence finding; the reviewer accepts the interpretation |
| Define measurable success | Avoid treating AI usage itself as the objective |

Generative AI can be part of a useful solution when it fits the task, workflow, and evaluation. The strongest evidence here is the reported change in document-review time with human review retained.
