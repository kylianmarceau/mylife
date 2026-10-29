---
tags:
  - advanced-programming
---

# Artificial Intelligence In Software Development

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD20 Artificial intelligence - Copy.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD20%20Artificial%20intelligence%20-%20Copy.pdf), Johan Bontes, University of Cape Town, PDF pages 1–38  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: what "AI" means (knowledge representation, reasoning, perception), how neural networks run, scaling and its diminishing returns, the hype cycle, developer survey data, UCT's GenAI policy, effects on learning, and the security of AI-generated code.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Is AI?|What Is AI?]]
  - [[#Knowledge Representation|Knowledge Representation]]
  - [[#Reasoning|Reasoning]]
  - [[#Perception: Neural Networks|Perception: Neural Networks]]
  - [[#AlexNet And Hardware Progress|AlexNet And Hardware Progress]]
  - [[#AI Scaling: Diminishing Returns|AI Scaling: Diminishing Returns]]
  - [[#Perception Plus Reasoning?|Perception Plus Reasoning?]]
  - [[#Problems With Matrix-Multiply AI|Problems With Matrix-Multiply AI]]
  - [[#The Hype Cycle|The Hype Cycle]]
  - [[#Developers And AI: Stack Overflow Survey 2025|Developers And AI: Stack Overflow Survey 2025]]
  - [[#UCT CS Generative AI Policy|UCT CS Generative AI Policy]]
  - [[#Effect Of AI On Student Learning|Effect Of AI On Student Learning]]
  - [[#Security Of AI-Generated Code|Security Of AI-Generated Code]]

---

## Core Content

### What Is AI?

"AI" is close to a meaningless marketing term. The EU definition is essentially anything you can do with a computer. The lecture divides it into three families.

| Family | Nature | Includes |
|---|---|---|
| **Knowledge representation** | Exact (aims to be) | Knowledge bases, ontologies |
| **Reasoning** | Exact | Boolean logic (including defeasible reasoning); optimisation such as genetic algorithms |
| **Perception** | Fuzzy | Neural networks |

![AI families](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/20A_Artificial_Intelligence/ai-families.svg)

*Knowledge representation is effectively dead, reasoning gives exact but hard models, and perception (all of generative AI) is fuzzy pattern matching.*

### Knowledge Representation

#### Definitions

> **Knowledge base (expert system)**: A store of facts and rules used to answer questions.

> **Ontology**: A human-curated representation of concepts and the relations between them.

- Ontologies strive to be exact, but real-world concepts are inherently fuzzy.
- They don't scale, because they must be built by hand.
- The approach is effectively dead, killed off by perception AI.

### Reasoning

#### Definitions

> **Exact Boolean reasoning**: A mathematically ideal model of a real-world problem.

> **Defeasible reasoning**: Exact reasoning plus "maybe": conclusions that can be withdrawn given new information.

Exact Boolean logic models a problem as an **NP-hard or NP-complete** representation, for example:

- integer linear programming (cf. the high-school simplex method)
- Boolean satisfiability (SAT)
- knapsack, travelling salesman and bin packing

### Perception: Neural Networks

#### Definitions

> **Perception AI**: All of generative AI, built from neural networks whose layers are matrices of floats and whose transformations are matrix multiply-and-add (fused multiply-add, FMA).

For an $n\times n$ matrix:

$$
\text{memory} = O(n^2),\qquad \text{operations} = O(n^3)
$$

For example, a $100\times100$ matrix needs $100^2$ memory cells and $100^3$ operations. The work is almost embarrassingly parallel, so it runs on GPUs, using tensor cores on GPUs or NPUs.

### AlexNet And Hardware Progress

**AlexNet (2012)** was the watershed moment:

- it ran on the GPU, massively in parallel
- it had 5 convolutional layers and 3 fully connected layers
- it was much better than shallow neural nets

The source compares it with LeNet-style architectures: stacked convolution and pooling layers, then fully connected layers, ending in 1000 output classes.

Speed-ups in TPUs and NPUs came from:

- bigger TPUs and NPUs
- more GPUs and bigger models
- **smaller floating-point numbers** (float32 → fp16 → fp8 → fp4), which loses precision

NVIDIA claims int4 is as good as fp32, which is hard to believe: 16 values versus about 4 billion. Moving to smaller number formats needs new hardware, which is expensive (and profitable for NVIDIA).

### AI Scaling: Diminishing Returns

![Scaling diminishing returns](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/20A_Artificial_Intelligence/scaling.svg)

*On a log–log plot of loss against compute, the frontier is not a straight power law. It keeps flattening, so each 10× of compute buys less.*

- In the scaling plot (training loss versus FLOPs for models of 75 M to 10 000 M parameters), the black frontier line is **not straight**, so it is not a power law. It keeps flattening out: diminishing returns and terrible scaling.
- **Hype**: OpenAI's "Scaling Laws for Neural Language Models" fits $L=(C_{\min}/2.3\cdot10^{8})^{-0.050}$.
- **Reality** (Toby Ord, "The Scaling Paradox"): compute required rises steeply for small accuracy gains, a terrible return on investment with minimal improvement per 10× compute.
- AI progress **over time** is impressive; AI progress **per unit of resources** is not. Smooth, long-lasting scaling laws are proof of poor but predictable scaling, not impressive scaling.
- Real-world impact may scale better than the quality metrics.
- Image models fail the "circle the r's" test because they do not understand the concept of a "word".

**The future**:

- The current approach scales poorly. Companies can still throw money at it; a 10× data-centre scale-up is possible ("ouch!").
- The human brain scales much better, so perhaps a new algorithm will fix this. The field is waiting for the next AlexNet-level discovery.

### Perception Plus Reasoning?

Humans use both perception and reasoning, but no known algorithm combines them:

- **Perception**: how knowledge is represented is unknown, perhaps unknowable.
- **Reasoning**: rigid facts and hard mathematical models. "Tommie's research" at UCT works on soft/maybe (defeasible) reasoning.

Perception is fuzzy and reasoning is absolute, so it is unclear how to merge them. **Current "reasoning AI" is just a marketing term**: it is perception, with no understanding and no way to model concepts.

### Problems With Matrix-Multiply AI

| Property | Consequence |
|---|---|
| $x\times 0 = 0$ | Zeroed items are gone for good. This is partly good, since it limits scope to the question asked. |
| $x\times\infty = \infty$ | Infinite values cannot be recovered; the lecturer suspects this causes **confabulation** |
| Perception = pattern matching | Extreme patterns get magnified (e.g. an LLM and Nazi ideology); subtle patterns disappear into noise (nuance) |

This parallels social networks optimising for engagement: anger is good, nuance is bad.

### The Hype Cycle

![Gartner hype cycle](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/20A_Artificial_Intelligence/hype-cycle.svg)

*A new technology rises from its trigger to a peak of inflated expectations, crashes into the trough of disillusionment, then climbs the slope of enlightenment to a plateau of productivity.*

Gartner's 2025 hype cycle for generative AI places GenAI past the peak, heading into the trough.

### Developers And AI: Stack Overflow Survey 2025

![Stack Overflow survey 2025](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/20A_Artificial_Intelligence/so-survey.svg)

*84% use or plan to use AI tools, yet more developers distrust AI accuracy than trust it, most rate it poor at complex tasks, and the top frustration is "almost right, but not quite".*

- 84% use or plan to use AI tools (up from 76%); 51% of professional developers use them daily.
- 46% actively distrust AI accuracy against 33% who trust it; only 3% "highly trust" it. Experienced developers are the most cautious (2.6% highly trust, 20% highly distrust).
- Most developers (72.2%) do not vibe code at work.

### UCT CS Generative AI Policy

| Rule | Consequence |
|---|---|
| GenAI use not declared | Plagiarism: zero for the course plus a mark on the degree record |
| Vibe-coded assignment (no human effort) | 1% mark for the course |
| First-year CS | No GenAI allowed |
| Second and third year | Allowed, but must be declared and the work must be mostly human |
| Explicitly allowed by a supervisor | May be used to expand an assignment's scope (more interesting prototypes) |
| Science Dean | 80% of the mark must come from examination in a controlled environment (no internet) |

If a student shows insufficient understanding of work they claim as their own, the grade may be lowered.

### Effect Of AI On Student Learning

Research is inconclusive. Results are inconsistent:

- AI supports the creation of ideas and aids interaction.
- It hinders critical thinking and analytical skills.

![Bloom's taxonomy](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/20A_Artificial_Intelligence/blooms.svg)

*Bloom's taxonomy ranks learning from remembering up to creating.*

A meta-analysis ("The impact of generative AI on university students' learning outcomes via Bloom's taxonomy") pooled 24 studies. The pooled effects (Hedges' $g$) all favour "helps":

| Outcome | Pooled $g$ | Verdict |
|---|---:|---|
| Lower-order learning | $\approx 0.93$ | Helps |
| Higher-order learning | $\approx 0.64$ | Helps |
| Non-cognitive skills | $\approx 0.55$ | Helps |

The lecturer's caveats:

- the studies ran in controlled environments; does that translate to messy real-world universities?
- non-significant or negative results are less likely to be published, and big-tech funding bias is possible
- only short-term effects were measured
- GenAI is a social experiment that will take decades to play out

### Security Of AI-Generated Code

From the Veracode 2025 GenAI Code Security Report:

- Across all models and tasks, **only 55% of generation tasks produced secure code**: 45% introduced a known security flaw.
- Security has stayed **largely unchanged** over time even as models produce more syntactically correct code.
- Larger models do **not** perform significantly better.
- Security varies **dramatically by CWE type**, somewhat by language, and is remarkably consistent across models.

![GenAI code security](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/20A_Artificial_Intelligence/genai-security.svg)

*Java fares worst by language (28.5% secure). By weakness, models mostly avoid bad crypto and SQL injection but almost always fail XSS and log injection.*

| CWE | Weakness | Secure pass rate |
|---|---|---:|
| CWE-327 | Bad cryptography | 85.61% |
| CWE-89 | SQL injection | 80.44% |
| CWE-80 | XSS | 13.53% |
| CWE-117 | Log injection | 12.03% |

**Insecure code as a proxy for bugs?**

- Insecure code may indicate logical bugs too, likely because GenAI lacks understanding. Comparing GenAI code against bugs found by sanitisers would be interesting research.
- GenAI shifts effort from writing functionality to finding and fixing bugs. Writing code is about 5% of effort while finding and fixing bugs is about 50%, so this "does not look like progress".
