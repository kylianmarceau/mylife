---
tags:
  - advanced-programming
---

# Artificial Intelligence In Software Development

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD20 Artificial intelligence - Copy.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD20%20Artificial%20intelligence%20-%20Copy.pdf), Johan Bontes, University of Cape Town, pages 1–38
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> What "AI" means (knowledge representation, reasoning, perception), how neural networks run on hardware, why scaling shows diminishing returns, the hype cycle, developer attitudes (Stack Overflow 2025), UCT's generative-AI policy, AI and learning, and the security of AI-generated code.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Is AI?|What Is AI?]]
  - [[#Knowledge Representation|Knowledge Representation]]
  - [[#Reasoning|Reasoning]]
  - [[#Perception And Neural Networks|Perception And Neural Networks]]
  - [[#AlexNet And Hardware Progress|AlexNet And Hardware Progress]]
  - [[#AI Scaling: Diminishing Returns|AI Scaling: Diminishing Returns]]
  - [[#Combining Perception And Reasoning|Combining Perception And Reasoning]]
  - [[#Problems With Matrix-Multiply Pattern Matching|Problems With Matrix-Multiply Pattern Matching]]
  - [[#The Hype Cycle|The Hype Cycle]]
  - [[#Developers And AI: Stack Overflow 2025|Developers And AI: Stack Overflow 2025]]
  - [[#UCT CS Generative AI Policy|UCT CS Generative AI Policy]]
  - [[#AI And Student Learning|AI And Student Learning]]
  - [[#Security Of AI-Generated Code|Security Of AI-Generated Code]]

---

## Core Content

### What Is AI?

Is "AI" a meaningless marketing term? The EU definition is broad: essentially anything you can do with a computer. The lecture groups AI into three families:

| Family | Kind | Examples |
|---|---|---|
| **Knowledge representation** | Exact | Knowledge bases (expert systems), ontologies |
| **Reasoning** | Exact | Boolean logic (including defeasible reasoning), optimisation (genetic algorithms) |
| **Perception** | Fuzzy | Neural networks — all of generative AI |

![Kinds of AI](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/20A_Artificial_Intelligence/ai-families.svg)

*Knowledge representation is exact but hand-built; reasoning is exact but NP-hard; perception is fuzzy pattern matching on GPUs.*

### Knowledge Representation

#### Definitions

> **Knowledge base (expert system)**: A curated store of facts and rules used to answer questions.

> **Ontology**: A human-curated representation of concepts and the relations between them.

- Strives to be exact, but real-world concepts are inherently fuzzy.
- Doesn't scale, because it must be built by hand.
- Effectively dead — killed off by perception AI.

### Reasoning

#### Definitions

> **Defeasible reasoning**: Exact logic plus "maybe" — conclusions that can be withdrawn when new information arrives.

Boolean-logic reasoning is either:

- **exact** — a mathematically ideal model of a real-world problem; or
- **defeasible** — exact + maybe.

Exact Boolean logic models a problem mathematically as an **NP-hard or NP-complete** representation, e.g.:

- integer linear programming (the high-school simplex method);
- Boolean satisfiability (SAT);
- knapsack, travelling salesman, bin packing.

### Perception And Neural Networks

All of generative AI is perception, built with neural networks:

- Layers are encoded as matrices of floats.
- Transformations are matrix multiply + add — the fused multiply-add (**FMA**) operation.

For an $n \times n$ matrix multiplication:

| Measure | Scaling | Example ($n = 100$) |
|---|---|---|
| Memory | $O(n^2)$ | $100^2 = 10^4$ values |
| Work | $O(n^3)$ | $100^3 = 10^6$ operations |

Work grows faster than memory and the operations are independent, so the problem is almost **embarrassingly parallel** and runs on GPUs.

### AlexNet And Hardware Progress

**AlexNet (2012)** was the watershed moment:

- ran on the GPU, massively parallel;
- 5 convolutional layers and 3 fully connected layers;
- much better than shallow neural networks.

Neural nets run on matrix multiplication, using **tensor cores** on GPUs (and NPUs).

Speed-ups in TPUs/NPUs have come from:

- bigger TPUs/NPUs;
- more GPUs and bigger models;
- **smaller floating-point numbers** (float32 → fp16 → fp8 → fp4).

Smaller formats lose precision. NVIDIA claims int4 is as good as fp32, which is hard to believe: 4 bits give only 16 values versus about 4 billion for 32 bits. Each move to smaller units needs new hardware — lots of money for NVIDIA.

### AI Scaling: Diminishing Returns

On a log–log plot of model quality against compute, the observed frontier is **not straight** — it isn't a power law, and it keeps flattening out: diminishing returns, terrible scaling.

![Diminishing returns of scaling](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/20A_Artificial_Intelligence/scaling.svg)

*Each tenfold increase in compute buys a smaller improvement (Toby Ord, "The Scaling Paradox").*

| Hype | Reality |
|---|---|
| "Scaling Laws for Neural Language Models" (OpenAI) | Terrible return on investment: minimal improvement for 10× compute (Toby Ord) |

Recap (from Toby Ord):

- AI progress as a function of **time** is impressive.
- AI progress as a function of **resources** is not.
- Smooth, long-lasting scaling laws are proof of **poor but predictable** scaling, not impressive scaling.
- AI quality metrics scale poorly with resources; real-world impacts may (?) scale better.

**The "circle r" test**: image generators asked to draw something like a circled "r" fail abjectly, because picture AI doesn't understand the concept of a word.

**The future?** The current approach scales poorly. Companies can still throw money at it — another 10× scale-up of data centres is possible (ouch!) — but the human brain scales much better. Perhaps a new algorithm will fix this: we're waiting for the next AlexNet-style discovery.

### Combining Perception And Reasoning

Humans use **perception + reasoning**, but no known algorithm combines both:

| Perception | Reasoning |
|---|---|
| Its knowledge representation is unknown (unknowable?) | Rigid facts and hard mathematical models (defeasible reasoning research works on soft "maybe" logic) |
| Everything fuzzy | Everything absolute |

How do you merge the two? Current "reasoning AI" is just a marketing term for perception — it has no understanding and no way to model concepts.

### Problems With Matrix-Multiply Pattern Matching

| Property | Effect |
|---|---|
| $x \times 0 = 0$ | Zeroed items are gone for good — partly good, as it limits scope to the question asked |
| $x \times \infty = \infty$ | Infinite values can't be recovered — the lecturer suspects this causes confabulation |
| Perception = pattern matching | Extreme patterns get magnified (e.g. LLMs and Nazi ideology); subtle patterns vanish into the noise (e.g. LLMs and nuance) |

Social networks optimise for engagement the same way: anger is good, nuance is bad.

### The Hype Cycle

#### Definitions

> **Gartner hype cycle**: The typical path of public expectations for a new technology over time.

![Gartner hype cycle](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/20A_Artificial_Intelligence/hype-cycle.svg)

*Visibility rises from a technology trigger to a peak of inflated expectations, falls into a trough of disillusionment, then climbs a slope of enlightenment to a plateau of productivity.*

1. Technology trigger
2. Peak of inflated expectations
3. Trough of disillusionment
4. Slope of enlightenment
5. Plateau of productivity

Gartner's 2025 hype cycle for generative AI places many GenAI technologies around the peak and heading into the trough.

### Developers And AI: Stack Overflow 2025

![Stack Overflow survey 2025](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/20A_Artificial_Intelligence/so-survey.svg)

*Most developers use AI tools, but few trust their accuracy or their handling of complex tasks.*

| Using AI tools? (84% use or plan to) | Share |
|---|---|
| Yes, daily | 47.1% |
| Yes, weekly | 17.7% |
| Yes, monthly | 13.7% |
| No, but planning to | 5.3% |
| No, and don't plan to | 16.2% |

| Trust the accuracy of AI output? | Share |
|---|---|
| Highly trust | 3.1% |
| Somewhat trust | 29.6% |
| Somewhat distrust | 26.1% |
| Highly distrust | 19.6% |

| How well does AI handle complex tasks? (professional devs) | Share |
|---|---|
| Very well | 3.9% |
| Good, but not great | 25.2% |
| Neither good nor bad | 14.2% |
| Bad | 22.8% |
| Very poor | 18.6% |
| Don't use / don't know | 15.3% |

| Biggest frustrations | Share |
|---|---|
| AI solutions that are almost right, but not quite | 66% |
| Debugging AI-generated code takes longer | 45.2% |
| Don't use AI tools regularly | 23.5% |
| Less confident in own problem-solving | 20% |
| Hard to understand how/why the code works | 16.3% |
| Other | 11.6% |
| No problems | 4% |

**Vibe coding at work?** No: 72.2%; no, emphatically: 5.3%; yes: 11.9%; yes, somewhat: 2.8%; yes, emphatically: 0.4%.

### UCT CS Generative AI Policy

| Rule | Consequence |
|---|---|
| Undeclared generative AI use | Plagiarism: zero for the course and a mark on your degree record |
| A vibe-coded assignment (no human effort) | 1% mark for the course |
| First-year CS | No generative AI allowed |
| Second and third year | Allowed, but must be declared, and the work must be mostly human |
| Explicitly allowed by a supervisor | May be used to expand the scope of an assignment (more interesting prototypes) |
| Science Dean | 80% of the mark must come from examinations in a controlled environment (no internet) |

If a student shows insufficient understanding or knowledge of work they claim to have done themselves, the grade may be lowered.

### AI And Student Learning

Research on AI's effect on learning is **inconclusive** and inconsistent. It:

- supports the creation of ideas;
- aids interaction;
- **hinders critical thinking and analytical skills**.

#### Definitions

> **Bloom's taxonomy**: A hierarchy of learning goals from lower-order to higher-order thinking.

![Bloom's taxonomy](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/20A_Artificial_Intelligence/blooms.svg)

*Learning goals from lower order (remember, understand, apply) to higher order (analyse, evaluate, create).*

| Level | Meaning |
|---|---|
| Create | Produce new or original work |
| Evaluate | Justify a stand or decision |
| Analyse | Draw connections among ideas |
| Apply | Use information in new situations |
| Understand | Explain ideas or concepts |
| Remember | Recall facts and basic concepts |

A meta-analysis ("The impact of generative AI on university students' learning outcomes via Bloom's taxonomy") of 24 studies was mostly positive:

| Outcome | Pooled effect (Hedges' $g$) | Result |
|---|---|---|
| Lower-order learning | ≈ 0.93 ($p < 0.001$) | Helps |
| Higher-order learning | ≈ 0.64 ($p \approx 0.001$) | Helps |
| Non-cognitive skills (motivation, self-efficacy, enjoyment) | ≈ 0.55 ($p \approx 0.004$) | Helps |

But treat this with caution:

- Studies were performed in controlled environments — does that translate to messy real-world universities?
- Studies with non-significant or negative results are less likely to be published (**publication bias**), and there may be funding bias (big tech).
- Only short-term effects were measured.
- GenAI is a social experiment that will take decades to play out.

### Security Of AI-Generated Code

The Veracode 2025 GenAI Code Security Report found that **45% of generated code contains a known security flaw** (only 55% of tasks produced secure code).

![Secure pass rates of AI-generated code](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/20A_Artificial_Intelligence/genai-security.svg)

*Security varies hugely by weakness type and somewhat by language, and has not improved with newer or larger models.*

| Language | Secure pass rate |
|---|---|
| Python | 61.69% |
| JavaScript | 57.34% |
| C# | 55.27% |
| Java | 28.5% |

| Weakness (CWE) | Secure pass rate |
|---|---|
| CWE-327 bad cryptography | 85.61% |
| CWE-89 SQL injection | 80.44% |
| CWE-80 XSS | 13.53% |
| CWE-117 log injection | 12.03% |

- Better models? **Syntax** has improved; **security** has not.
- Larger models are not significantly better.

Is insecure GenAI code a proxy for logical bugs too? Likely, because GenAI lacks understanding. (An interesting research question: GenAI code versus bugs found by sanitizers.)

GenAI shifts effort from writing functionality to finding and fixing bugs. Writing code is about 5% of effort, while finding and fixing bugs is about 50% — so this doesn't look like progress.
