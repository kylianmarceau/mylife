---
tags:
  - ai-systems
---

# Introduction I: AI, Agents and Intractable Problems

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3044S AI Systems: Section 1, Agents and Agent Architectures  
> **Source**: [2026-CSC3044S-Lecture 1-Introduction - Copy.pdf](../../../Sources/CSC3044S%20-%20AI%20Systems/AIS/2026-CSC3044S-Lecture%201-Introduction%20-%20Copy.pdf), Geoff Nitschke, slides 1-55  
> **Reading**: Russell & Norvig (2021), *AIMA* 4th ed., Ch 2 (Intelligent Agents); Poole & Mackworth (2023), *Artificial Intelligence: Foundations of Computational Agents* 3rd ed., Ch 1  
> **Generated**: 2026-11-07

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Course overview|Course overview]]
  - [[#What is AI|What is AI]]
  - [[#Symbolic AI versus neural AI|Symbolic AI versus neural AI]]
  - [[#The AI renaissance|The AI renaissance]]
  - [[#What is an agent|What is an agent]]
  - [[#A brief history of agents|A brief history of agents]]
  - [[#Classic definitions of AI|Classic definitions of AI]]
  - [[#Designing agents|Designing agents]]
  - [[#Rational agents|Rational agents]]
  - [[#Reinforcement learning as a classic rational agent|Reinforcement learning as a classic rational agent]]
  - [[#Irrational agents|Irrational agents]]
  - [[#What rationality depends on|What rationality depends on]]
  - [[#Types of rational agents|Types of rational agents]]
  - [[#The 2026 agent landscape|The 2026 agent landscape]]
  - [[#Solving intractable problems|Solving intractable problems]]
  - [[#P, NP, NP-complete and NP-hard|P, NP, NP-complete and NP-hard]]
  - [[#The Travelling Salesman Problem|The Travelling Salesman Problem]]
  - [[#NP-hard optimisation|NP-hard optimisation]]
  - [[#Course project: the Vehicle Routing Problem|Course project: the Vehicle Routing Problem]]

---

## Core Content

### Course overview

CSC3044S has three sections, each taught by a different lecturer.

| Section | Topic | Lecturer |
|---|---|---|
| 1 | Agents and Agent Architectures | Geoff Nitschke |
| 2 | AI Systems Design | Francois Meyer |
| 3 | Human-centred AI Systems and Societal Impacts of AI | Melissa Densmore |

| Week | Content |
|---|---|
| 1-2 | AI agents and systems |
| 3 | Human-centred AI systems and societal impacts I |
| 4 | AI systems design |
| 5 | Project presentations and demos |
| 6 | Human-centred AI systems and societal impacts II |

| Assessment | Weight | Details |
|---|---|---|
| Project | 25% | Released 14 September, due 12 October |
| Test | 25% | 2 October, 18:00-18:45, New LT |
| Exam | 50% | 2 hours, 12 November, Snape TS2B |

- **DP requirement**: 45% aggregate in practical work.
- Extension requests go to the course convenor (Geoff Nitschke). Mark queries go to the TAs.
- Recommended books: Russell & Norvig, *AIMA* (4th ed.), and Poole & Mackworth, *Foundations of Computational Agents* (3rd ed.). Readings are assigned per lecture on Amathuba.

### What is AI

#### Definitions

> **Artificial Intelligence (AI)**: A field with roots in many disciplines, including computer science, statistics, psychology, neuroscience and philosophy, that overlaps heavily with machine learning.

AI is not one technique. Many of its core methods were borrowed from other fields.

| Method | Field it came from |
|---|---|
| Bayes rule | Probability |
| Game theory | Mathematics and economics |
| Stochastic gradient descent | Statistics |
| Value iteration | Control theory |
| Temporal difference learning | Psychology |
| Artificial neural networks | Neuroscience |

![AI sits at the overlap of many fields](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/ai_roots.svg)

*AI and machine learning sit where computer science, statistics, psychology, neuroscience and philosophy overlap. Each field contributed a core method.*

### Symbolic AI versus neural AI

#### Definitions

> **Symbolic AI**: A top-down approach to AI based on logic and explicit rules.

> **Neural AI**: A bottom-up approach to AI that is connectionist and neuro-inspired.

The approach that now dominates AI research is neural AI. It goes beyond symbolic AI rather than fully replacing it.

| | Symbolic AI | Neural AI |
|---|---|---|
| Direction | Top-down | Bottom-up |
| Basis | Logic, rules | Connections between simple units (neuro-inspired) |
| Typical example | Game-tree search (e.g. tic-tac-toe tree) | Network of neurons |
| Where knowledge lives | Rules written by the designer | Weights learned from data |

![Symbolic versus neural AI](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/symbolic_vs_neural.svg)

*Symbolic AI reasons down a tree of explicit states; neural AI builds behaviour up from many connected units whose weights are learned.*

### The AI renaissance

The current AI renaissance comes from combining three ingredients:

1. Symbolic AI.
2. Neural AI.
3. Tools and ideas from other fields: optimisation, algorithms, probabilistic inference, statistics and game theory.

The result of this combination is **agents**.

![The AI renaissance produces agents](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/ai_renaissance.svg)

*Agents are what you get when symbolic AI, neural AI and borrowed tools are combined.*

### What is an agent

Familiar examples of agents include:

- Game-playing systems such as AlphaGo and the Jeopardy-winning IBM Watson.
- Scientific systems such as AlphaFold 3.
- Robots: humanoids, legged robots (e.g. a robot dog), planetary rovers.
- Autonomous vehicles.
- Chat assistants built on large language models.

All of these perceive something about their world and act on it. That is the core idea behind the formal definition in [[#Designing agents|Designing agents]].

### A brief history of agents

#### Definitions

> **Symbolic reasoning agent**: An agent that decides what to do by symbol manipulation. In its purest form, it uses explicit logical reasoning to decide what to do.

> **Reactive agent**: An agent design that arose from the problems with symbolic reasoning; it reacts to its environment rather than reasoning explicitly.

> **Hybrid agent**: An architecture that tries to combine the best of reasoning and reactive architectures.

> **Neuro (cognitive) agent**: The most recent family, built on neural methods. The lecture leaves its full definition open.

| Period | Agent family |
|---|---|
| 1950s-present | Symbolic reasoning agents |
| 1980s-present | Reactive agents |
| 1990s-present | Hybrid agents |
| 2000s-present | Neuro (cognitive) agents |

Each family is still in use. A new family was added each time the older ones hit a limit, but none was discarded.

### Classic definitions of AI

AI has traditionally been defined along two axes: thinking versus acting, and human-like versus rational.

| | Human-like | Rational |
|---|---|---|
| **Think** | Cognitive science and neuroscience. Raises the question: does intelligence require biology? | Logic and automated reasoning. Not every problem can be solved this way. |
| **Act** | Turing test, ELIZA, the Loebner prize. A chatbot dodging "What is 1228 × 5873?" with "I don't know, I'm just a human" passes as human without being rational. | The basis of the intelligent agents framework. It is unclear whether this captures the full scope of AI research. |

This course takes the **act rationally** view: an AI system is an agent that acts to achieve its goals.

### Designing agents

#### Definitions

> **Agent**: An entity that perceives and acts.

> **Percepts**: The inputs an agent receives from the environment through its sensors.

> **Sensors**: The parts of an agent that take in percepts.

> **Actuators**: The parts of an agent that carry out actions on the environment.

> **Action space**: The set of actions available to the agent.

An agent sits in an environment. Percepts come in through sensors, and actions go out through actuators.

The characteristics of the percepts, state, environment and action space decide which methods are suitable for selecting actions.

![Agent and environment](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/agent_environment.svg)

*The "?" between sensors and actuators is the agent program, the part that turns percepts into actions. Agent architectures are different answers to what goes in that box.*

### Rational agents

#### Definitions

> **Rational**: Maximally achieving pre-defined goals (objectives).

> **Utility**: A measure of how good an outcome is. Goals are expressed in terms of the utility of outcomes.

> **Rational agent**: An agent that maximises its expected utility.

Key properties of rationality:

- Rationality only concerns **what decisions are made**, not the "thought" processes behind them.
- Goals are expressed as the utility of outcomes.
- Being rational means **maximising expected utility**.

If $U(o)$ is the utility of outcome $o$ and $P(o \mid a)$ is the probability that action $a$ leads to $o$, a rational agent picks:

$$
a^* = \arg\max_{a} \sum_{o} P(o \mid a)\, U(o)
$$

Real-world examples of rational agents:

| Example | What it maximises |
|---|---|
| Algorithmic trading agent | Profit from trades |
| GPS navigation | Route quality (e.g. shortest travel time) |
| Self-driving car | Safe, efficient arrival |
| Robot vacuum cleaner | Floor area cleaned |
| Smart thermostat | Comfort at low energy use |

### Reinforcement learning as a classic rational agent

#### Definitions

> **Reinforcement learning (RL) agent**: An agent that learns, through repeated interaction, which actions maximise the reward it receives from the environment.

> **Reward** ($R_t$): The scalar feedback signal the environment gives the agent at time $t$.

> **State** ($s_t$): The situation of the environment observed by the agent at time $t$.

> **Action** ($a_t$): The choice the agent makes at time $t$.

RL is the classic example of a rational agent algorithm. The loop runs as follows:

1. The agent observes state $s_t$.
2. It chooses action $a_t$.
3. The environment changes and returns reward $R_t$ and a new state.
4. The agent uses the reward to improve future choices, then repeats.

Over time the agent tries to maximise total (expected) reward, which is the RL version of maximising expected utility.

![Reinforcement learning loop](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/rl_loop.svg)

*The agent sends an action to the environment; the environment returns a reward and the next state, closing the loop.*

### Irrational agents

#### Definitions

> **Irrational agent**: An agent that takes actions leading to low utility (reward).

> **Hallucination**: Inconsistent or fabricated output, for example from an LLM, caused by problems with training data or noise in the data.

Agents behave irrationally for two main reasons.

| Cause | What goes wrong |
|---|---|
| **Incomplete information** | The agent's world model, sensory input or training data is too simple. There may not be enough compute time, or too much noise in training data or inputs. The result is poor outputs. |
| **Hallucinations and noise** | Problems with training data or noisy data. For example, LLMs can produce inconsistent and fabricated outputs, which are irrational outputs. |

> [!warning] <span style="color: #ff939b">Example: glue on pizza</span>
> A search engine's AI overview recommended mixing about 1/8 cup of non-toxic glue into pizza sauce to stop cheese sliding off. The advice came from a joke forum post in its training data. The system acted on bad data and produced a low-utility, irrational output.

### What rationality depends on

Whether an action counts as rational depends on four things:

1. The **performance metric** (objective function).
2. The agent's **knowledge of the environment** (data).
3. The **actions available** to the agent.
4. The agent's **sensory information**.

Being rational still means maximising expected utility, but always relative to these four constraints. An agent is not irrational for failing to use information it could not sense.

### Types of rational agents

#### Definitions

> **Reactive (reflexive) agent**: An agent that responds directly to its percepts. It comes in two forms, simple and model-based.

> **Deliberative (goal-based) agent**: An agent that reasons about goals to decide what to do.

> **Learning agent**: An agent that improves its behaviour from experience, for example with RL, artificial neural networks (ANNs) or LLMs.

| Type | Variants / methods |
|---|---|
| Reactive (reflexive) | Simple, model-based |
| Deliberative | Goal-based |
| Learning | RL, ANN, LLM, … |

These types are covered in detail in [Introduction II](02_Introduction_II.md).

### The 2026 agent landscape

In 2026 most deployed agents fall into five families. Coding agents get the most attention.

| Family | What it does | Representative tools (September 2026) |
|---|---|---|
| **Coding agents** | Read, write, run and debug code across a whole project, often unsupervised for long stretches | Claude Code, OpenAI Codex, Cursor, GitHub Copilot, Cline, Devin |
| **Computer-use agents** | Drive a graphical interface (click, type, scroll) the way a person would, for tasks with no API | Anthropic Computer Use, OpenAI Operator, Gemini Computer Use / Project Mariner |
| **Research agents** | Plan a multi-step search, gather and cross-check sources, and synthesise a cited report ("Deep Research" modes) | Deep Research modes in ChatGPT, Gemini, Claude and Perplexity; Grok DeepSearch |
| **General agents** | Attempt arbitrary multi-step tasks across tools and the web from a single instruction | Manus (now Meta), ChatGPT Agent, Genspark, OpenManus |
| **Creative agents** | Drive creative software (3D, audio, design) through tool connectors | Claude's creative connectors (Adobe, Blender, Ableton, Autodesk Fusion) |

### Solving intractable problems

#### Definitions

> **Bin packing problem**: Given $n$ items of different (1D) sizes and bins of fixed capacity, pack the items into the minimum number of bins.

Agents are also used to solve intractable problems, such as:

- Logistics, e.g. factory packing (bin packing).
- Games, e.g. Sudoku and Go.
- Vehicle routing, e.g. the multi-modal Travelling Salesman Problem.
- Engineering design, e.g. designing a satellite antenna.
- Robotics, e.g. driving autonomous vehicles.

![Bin packing](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/bin_packing.svg)

*Checking a packing is easy. Proving it uses the minimum number of bins is not, which is why bin packing is a hard computational problem.*

### P, NP, NP-complete and NP-hard

#### Definitions

> **P (Polynomial)**: Problems solved in polynomial time. Run time grows in proportion to a power of the input size, e.g. $n^2$.

> **NP (Non-deterministic Polynomial)**: Problems whose solutions can be verified quickly, even if finding a solution takes a long time (it is found in a non-deterministic way).

> **NP-complete**: Problems in NP whose solution validity can be verified quickly (in polynomial time). Brute-force search can find a valid solution by trying all possible solutions. "Complete" means the problem is as universal and hard as any other problem in NP.

> **NP-hard**: Problems at least as hard as NP-complete problems, but which may not be solvable (and verifiable) in non-deterministic polynomial time. There is no known efficient solution.

The key distinction is between **finding** a solution and **verifying** one.

| Class | Verify quickly? | Solve quickly? | Example |
|---|---|---|---|
| P | Yes | Yes | Sorting |
| NP | Yes | Not necessarily | Travelling Salesman (decision form) |
| NP-complete | Yes | No known method | Boolean Satisfiability (SAT) |
| NP-hard | Not necessarily | No known method | Vehicle Routing Problem |

**Why "complete" matters.** If you find a fast, efficient way to solve *one* NP-complete problem, you can use that method to solve *all* other NP problems.

**Boolean Satisfiability (SAT)**, an NP-complete example:

- **Task**: assign true or false to $n$ variables so that a given Boolean formula is true.
- **Verification**: given a proposed assignment, you can quickly check that the formula evaluates to true.
- **Difficulty**: the time to find a solution grows exponentially with $n$, because there are $2^n$ assignments.

**Travelling Salesman Problem (TSP)**, an NP example:

- **Task**: find the shortest path between $n$ cities.
- **Verification**: you can quickly compute a path's length to check whether it is the shortest found so far.
- **Difficulty**: the time to find the shortest path grows exponentially with $n$.

**Relationships between the classes:**

- $P \subseteq NP$.
- Every NP-complete problem is NP-hard, but not all NP-hard problems are in NP.
- Whether $P = NP$ is unproven. There are no polynomial-time algorithms (yet) for solving all NP problems.

![Complexity classes](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/complexity_classes.svg)

*Assuming $P \neq NP$: P sits inside NP, NP-complete is where NP meets NP-hard, and part of NP-hard lies outside NP entirely.*

### The Travelling Salesman Problem

#### Definitions

> **Travelling Salesman Problem (TSP)**: Visit each of $n$ cities exactly once and minimise the total tour length. It is NP-hard (no known efficient solution).

The search space grows factorially.

| Cities $n$ | Possible tours ($n!$) |
|---|---|
| 10 | $10! = 3\,628\,800$ |
| 50 | $50! \approx 10^{64}$ |

**Time to solve a 50-city TSP by simple enumeration.** Enumeration time is proportional to $n!$. Assume a CPU executes $10^{12}$ operations per second:

$$
\frac{50!}{10^{12}} \approx \frac{3 \times 10^{64}}{10^{12}} = 3 \times 10^{52} \text{ seconds}
$$

The lecture quotes this as roughly 31 000 years. Either way it is far too long, so brute force is not an option.

### NP-hard optimisation

#### Definitions

> **NP-hard optimisation**: Searching for the best solution $x^*$ out of some fixed set $S$, under constraints on computation, memory and time.

Formally:

$$
x^* = \arg\min_{x \in S} f(x)
$$

where $f$ is the cost to minimise (e.g. tour length).

The open question for agent design is: **given computation, memory and time constraints, how do we find this best solution?** Exhaustive search is infeasible, so agents need heuristics, optimisers or learning.

### Course project: the Vehicle Routing Problem

#### Definitions

> **Vehicle Routing Problem (VRP)**: An NP-hard problem of planning routes for one or more vehicles from a depot to serve a set of customers at minimum cost.

> **Dynamic VRP**: A VRP in which some customers are known at the start ($t = 0$, static customers) and others appear later ($t > 0$, dynamic customers), so routes must be re-planned.

In the dynamic version, the initial route plan covers static customers. When a dynamic customer appears, a new route segment is inserted into an existing route.

![Dynamic vehicle routing](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/dynamic_vrp.svg)

*Two routes leave the depot to serve static customers C1-C6. Dynamic customers C8 and C7 appear later and are inserted as new segments (dashed) into the existing routes.*

**Project brief** (14 September to 12 October):

- The agent must design an **optimiser module** for solving the VRP.
- The module plugs into a VRP framework and is tested on 10 known maps.
- **Final score**: how close your performance (averaged over 10 unknown maps) is to a best score. Matching or beating it gives 100%; reaching 0.1 of the best score gives 10%.

| Milestone | When |
|---|---|
| Weekly code repo commits | Weeks 1-4 |
| Final code hand-in | Week 5 |
| Presentations | Weeks 5-6 |

| Project component | Weight |
|---|---|
| Weekly code repo commits | 5% |
| Final score | 25% |
| Presentation | 30% |
| Session history (prompts) | 40% |

> [!tip] <span style="color: #5ad4b5">What you should know</span>
> - What an agent is.
> - The types of agents.
> - What agents can and cannot do.
