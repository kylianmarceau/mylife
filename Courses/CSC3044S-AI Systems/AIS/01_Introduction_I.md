---
tags:
  - ai-systems
---

# Introduction I: AI, Agents, And Intractable Problems

**Subject**: CSC3044S AI Systems  
**Source**: `2026-CSC3044S-Lecture 1-Introduction - Copy.pdf`, Geoff Nitschke, pages 1-55  
**Generated**: 2026-11-08

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Course Overview And Logistics|Course Overview And Logistics]]
  - [[#What Is Artificial Intelligence|What Is Artificial Intelligence]]
  - [[#Symbolic AI Versus Neural AI|Symbolic AI Versus Neural AI]]
  - [[#The AI Renaissance And Agents|The AI Renaissance And Agents]]
  - [[#A Brief History Of Agents|A Brief History Of Agents]]
  - [[#Classic Definitions Of AI|Classic Definitions Of AI]]
  - [[#Designing Agents|Designing Agents]]
  - [[#Rational Agents|Rational Agents]]
  - [[#Reinforcement Learning As A Rational Agent Algorithm|Reinforcement Learning As A Rational Agent Algorithm]]
  - [[#Examples Of Rational Agents|Examples Of Rational Agents]]
  - [[#Irrational Agents|Irrational Agents]]
  - [[#What Rationality Depends On|What Rationality Depends On]]
  - [[#Types Of Rational Agents|Types Of Rational Agents]]
  - [[#The 2026 Agent Landscape|The 2026 Agent Landscape]]
  - [[#Solving Intractable Problems|Solving Intractable Problems]]
  - [[#Logistics Problems And Bin Packing|Logistics Problems And Bin Packing]]
  - [[#Complexity Classes: P, NP, NP-Complete, NP-Hard|Complexity Classes: P, NP, NP-Complete, NP-Hard]]
  - [[#The Vehicle Routing Problem|The Vehicle Routing Problem]]
  - [[#Traveling Salesman Problem And Search Space Size|Traveling Salesman Problem And Search Space Size]]
  - [[#NP-Hard Optimisation|NP-Hard Optimisation]]
  - [[#AI Project: Solving The VRP|AI Project: Solving The VRP]]
  - [[#What You Should Know And Reading|What You Should Know And Reading]]

---

## Core Content

### Course Overview And Logistics

The course has three sections, each taught by a different lecturer.

| Section | Topic | Lecturer |
|---|---|---|
| 1 | Agents and Agent Architectures | Geoff Nitschke (gnitschke@cs.uct.ac.za) |
| 2 | AI Systems Design | Francois Meyer (francois.meyer@uct.ac.za) |
| 3 | Human-centered AI Systems & Societal Impacts of AI | Melissa Densmore (mdensmore@cs.uct.ac.za) |

TAs: Oliver Foxcroft (FXCOLI001@myuct.ac.za) and Max Van Veen (VVNMAX002@myuct.ac.za).

Weekly structure:

| Week | Content |
|---|---|
| 1-2 | AI Agents and Systems |
| 3 | Human-centered AI Systems & Societal Impacts I (Melissa Densmore) |
| 4 | AI Systems Design (Francois Meyer) |
| 5 | Project Presentations and Demos |
| 6 | Human-centered AI Systems & Societal Impacts II (Melissa Densmore) |

Assessment:

| Component | Weight | Details |
|---|---:|---|
| Project | 25% | Released 14 September, due 12 October |
| Test | 25% | 2 October, 18:00-18:45, New LT |
| Exam | 50% | 2 hours, 12 November, Snape TS2B |

- **DP requirement**: 45% aggregate in practical work.
- Assignment extension requests go to the course convenor (Geoff Nitschke).
- Assignment and test mark queries go to the TAs.
- The course notes hold all relevant course information.

Recommended books:

- Russell, S., and Norvig, P. (2021). *Artificial Intelligence: A Modern Approach*, 4th Edition (aima.cs.berkeley.edu).
- Poole, D., and Mackworth, A. (2023). *Artificial Intelligence: Foundations of Computational Agents*, 3rd Edition (artint.info/3e/html/ArtInt3e.html).

Chapters and papers are assigned per lecture on Amathuba.

### What Is Artificial Intelligence

#### Definitions

> **Artificial Intelligence (AI)**: An interdisciplinary field drawing on computer science, psychology, statistics, philosophy, and neuroscience, with machine learning at its overlapping core.

> **Machine Learning (ML)**: The sub-area of AI concerned with learning from data; it sits at the intersection of the contributing disciplines.

AI is not a single discipline. It overlaps with several fields, and machine learning sits in the region where they all meet, inside AI.

![AI and its contributing disciplines](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/ai_disciplines.svg)
*Computer science, psychology, statistics, philosophy, and neuroscience overlap in AI, with machine learning at its core.*

Many core AI techniques were borrowed from other fields:

| AI Technique | Field Of Origin |
|---|---|
| **Bayes rule** | Probability |
| **Game theory** | Mathematics and economics |
| **Stochastic gradient descent** | Statistics |
| **Value iteration** | Control theory |
| **Temporal difference learning** | Psychology |
| **Artificial neural networks** | Neuroscience |

### Symbolic AI Versus Neural AI

#### Definitions

> **Symbolic AI**: A top-down approach to AI based on logic and rules.

> **Neural AI**: A bottom-up approach to AI that is connectionist and neuro-inspired.

> **Connectionist**: Describes systems where intelligence emerges from many simple connected units (artificial neurons), rather than from explicit rules.

Neural AI is now the dominant, very successful approach in AI research. It goes beyond symbolic AI rather than replacing every idea from it.

| Aspect | Symbolic AI | Neural AI |
|---|---|---|
| Direction | Top-down | Bottom-up |
| Basis | Logic, explicit rules | Connectionist networks, inspired by the brain |
| Example | Game-tree search over board positions (e.g. Go) | Networks of neurons, like the brain's connections |

![Symbolic AI versus Neural AI](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/symbolic_vs_neural.svg)
*Symbolic AI searches a game tree top-down. In neural AI, behaviour emerges bottom-up from connected units.*

**Top-down example (symbolic):** a game tree for Go.

1. The root node is the current board position.
2. Each branch is a legal move, producing a child board position.
3. Each child expands into further moves, so the tree grows exponentially with depth.
4. The agent reasons explicitly over this tree of symbolic states to choose a move.

**Bottom-up example (neural):** a brain-like network of many interconnected neurons. Behaviour emerges from the connections rather than from hand-written rules.

### The AI Renaissance And Agents

The current AI renaissance combines symbolic AI, neural AI, and tools and ideas from other fields. Agents are the result: the unifying idea that brings all three together.

![The AI renaissance](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/ai_renaissance.svg)
*Symbolic AI, neural AI, and tools from optimization, algorithms, probabilistic inference, statistics, and game theory combine into agents.*

Examples of agents and AI systems:

- Google Gemini voice assistant on a phone.
- A humanoid android built as a lookalike of its creator.
- AlphaGo playing Go against Ke Jie.
- IBM Watson playing Jeopardy!.
- AlphaFold 3 predicting protein structure.
- A humanoid robot conducting an orchestra.
- An autonomous car from a self-driving vehicle challenge.
- A quadruped robot dog.
- A Mars rover.

### A Brief History Of Agents

#### Definitions

> **Symbolic Reasoning Agent**: An agent that decides what to do via symbol manipulation. In its purest form, it uses explicit logical reasoning to decide what to do.

> **Reactive Agent**: An agent design that arose from problems with symbolic reasoning; it responds to its environment rather than reasoning explicitly.

> **Hybrid Agent**: An agent architecture that attempts to combine the best of reasoning and reactive architectures.

> **Neuro (Cognitive) Agent**: The most recent agent family, based on neural approaches. Its full characterisation is left open.

![A brief history of agents](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/agent_history_timeline.svg)
*Each agent family began in a different decade and is still in use today.*

| Period | Agent Family | Key Idea |
|---|---|---|
| 1950s-present | Symbolic reasoning agents | Explicit logical reasoning via symbol manipulation |
| 1980s-present | Reactive agents | Response to the problems with symbolic reasoning |
| 1990s-present | Hybrid agents | Combine reasoning and reactive architectures |
| 2000s-present | Neuro (cognitive) agents | Open question: what these agents are is still being defined |

Each family runs to the present: newer families did not replace older ones.

### Classic Definitions Of AI

#### Definitions

> **Turing Test**: A test of whether a machine can act like a human well enough to be indistinguishable from one in conversation.

The classic definitions of AI sit on two axes: **thinking vs acting**, and **human-like vs rational**.

![Classic definitions of AI](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/classic_definitions.svg)
*The four classic views of AI. Acting rationally is the basis for the intelligent agents framework.*

In the "act like a human" quadrant, a human-like machine might answer "What is $1228 \times 5873$?" with "I don't know, I'm just a human".

The "act like a human" example shows a weakness: imitating humans means imitating human limitations, even when a computer could easily do better.

"Act rationally" is the view this course builds on.

### Designing Agents

#### Definitions

> **Agent**: An entity that perceives and acts.

> **Percept**: The input an agent receives from the environment through its sensors.

> **Sensors**: The parts of an agent that receive percepts from the environment.

> **Actuators**: The parts of an agent that carry out actions on the environment.

> **Action Space**: The set of actions available to the agent.

The characteristics of the **percepts**, **state**, **environment**, and **action space** dictate which methods suit selecting actions.

![Agent-environment loop](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/agent_environment.svg)
*Percepts flow from the environment into the sensors and actions flow out through the actuators. The "?" is the decision-making component an agent design must supply.*

The agent-environment loop:

1. The environment sends **percepts** to the agent's **sensors**.
2. Inside the agent, an unknown component "?" maps sensor input to a decision.
3. The decision goes to the **actuators**.
4. The actuators perform **actions** on the environment.
5. The environment changes and produces new percepts, and the loop repeats.

The central design question is: what is the "?" between sensors and actuators? That decision-making component is what agent architectures supply.

Example: a robot on a cliff edge reaching for an apple on a tree. It perceives the apple and acts with its grabber arm.

### Rational Agents

#### Definitions

> **Rational**: Maximally achieving pre-defined goals (objectives).

> **Utility**: A measure of how good an outcome is; goals are expressed in terms of the utility of outcomes.

> **Expected Utility**: The average utility of an action's outcomes, weighted by their probabilities.

Key properties of rationality:

- Rationality only concerns *what decisions* are made, not the "thought" processes behind them.
- Goals are expressed in terms of the **utility** of outcomes.
- Being rational means **maximizing your expected utility**.

In standard notation, a rational agent picks the action

$$
a^* = \arg\max_{a} \; \mathbb{E}[U \mid a] = \arg\max_{a} \sum_{o} P(o \mid a)\, U(o)
$$

where $o$ ranges over possible outcomes, $P(o \mid a)$ is the probability of outcome $o$ given action $a$, and $U(o)$ is its utility.

### Reinforcement Learning As A Rational Agent Algorithm

#### Definitions

> **Reinforcement Learning (RL)**: A classic rational agent algorithm in which an agent learns by interacting with an environment, receiving states and rewards and choosing actions to maximise reward.

> **State ($s_t$)**: The environment's situation at time $t$, as observed by the agent.

> **Reward ($R_t$)**: The scalar feedback signal the environment gives the agent at time $t$.

> **Action ($a_t$)**: The choice the agent makes at time $t$.

RL is the classic example of a rational agent algorithm. The reward plays the role of utility.

The RL loop:

1. The agent observes the current state $s_t$ and reward $R_t$ from the environment.
2. The agent chooses an action $a_t$.
3. The action is applied to the environment.
4. The environment moves to a new state and returns a new state and reward to the agent.
5. Repeat.

![Reinforcement learning loop](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/rl_loop.svg)
*The agent sends action $a_t$ to the environment, which returns reward $R_t$ and state $s_t$.*

### Examples Of Rational Agents

Real-world rational agents, each maximising some objective:

| Agent | What It Optimises (typical objective) |
|---|---|
| Algorithmic trading agent | Trading profit |
| GPS navigation device (e.g. Garmin) | Route to destination |
| Self-driving car (e.g. Waymo) | Safe, efficient driving to destination |
| Robot vacuum cleaner (e.g. Roomba) | Floor area cleaned |
| Smart thermostat (e.g. Nest) | Target temperature with low energy use |

### Irrational Agents

#### Definitions

> **Irrational Agent**: An agent that takes actions leading to low utility (reward).

> **Incomplete Information**: The agent's model of the world, (sensory) input, or training data is too simple, there is not enough compute time, or there is too much noise in training data or inputs, leading to poor outputs.

> **Hallucination**: Inconsistent or fabricated output, e.g. from Large Language Models (LLMs), caused by problems with training data or noise in the data. These are irrational outputs.

> **Large Language Model (LLM)**: A neural model trained on large text datasets to generate language.

Causes of irrational behaviour:

| Cause | What Goes Wrong |
|---|---|
| Incomplete information | World model, sensory input, or training data too simple; too little compute time; too much noise in training data or inputs |
| Hallucinations and noise | Training-data problems or noisy data lead LLMs to produce inconsistent, fabricated outputs |

Example: a search engine's AI overview answered "cheese slides off pizza" by suggesting adding about $1/8$ cup of non-toxic glue to the sauce. The answer came from a joke forum comment in its source data. The system reproduced noisy data as advice, giving a low-utility, irrational output.

### What Rationality Depends On

What counts as rational depends on four things:

1. **Performance metric** (objective function).
2. **Agent's knowledge of the environment** (data).
3. **Actions available** to the agent.
4. **Sensory information**.

So an agent is rational relative to what it knows, what it can sense, and what it can do. It is not judged against an all-knowing ideal. Being rational still means maximizing your expected utility.

### Types Of Rational Agents

#### Definitions

> **Reactive (Reflexive) Agent**: An agent that maps current percepts (and possibly an internal model) directly to actions. It comes in *simple* and *model-based* forms.

> **Deliberative (Goal-Based) Agent**: An agent that reasons about goals to decide what to do.

> **Learning Agent**: An agent that improves its behaviour from experience or data, e.g. RL, artificial neural network (ANN), or LLM agents.

| Type | Variants / Examples |
|---|---|
| Reactive (reflexive) | Simple; model-based |
| Deliberative (goal-based) | Goal-based reasoning |
| Learning | RL, ANN, LLM, ... |

The three types are not mutually exclusive: learning can be added to reactive or deliberative designs.

### The 2026 Agent Landscape

Modern (rational) agents fall into five families. Coding agents are the family most relevant to this course, since the project is assessed partly on agent session history.

| Family | What It Does | Representative Tools (September 2026) |
|---|---|---|
| Coding agents | Read, write, run, and debug code across a whole project, often unsupervised for long stretches | Claude Code, OpenAI Codex, Cursor, GitHub Copilot, Cline, Devin |
| Computer-use agents | Drive a graphical interface (click, type, scroll) the way a person would, for tasks with no API | Anthropic Computer Use, OpenAI Operator, Gemini Computer Use / Project Mariner |
| Research agents | Plan a multi-step search, gather and cross-check sources, and synthesise a cited report ("Deep Research" modes) | Deep Research modes in ChatGPT, Gemini, Claude and Perplexity; Grok DeepSearch |
| General agents | Attempt arbitrary multi-step tasks across tools and the web from a single instruction | Manus (now Meta), ChatGPT Agent, Genspark, OpenManus |
| Creative agents | Drive creative software (3D, audio, design) through tool connectors | Claude's creative connectors (Adobe, Blender, Ableton, Autodesk Fusion) |

### Solving Intractable Problems

#### Definitions

> **Intractable Problem**: A problem for which no known algorithm finds an exact solution in reasonable (polynomial) time as the input grows.

Agents can also solve intractable problems:

| Application | Example |
|---|---|
| Logistics | Factory packing |
| Games | Sudoku, Go |
| Vehicle routing | Multi-modal Traveling Salesman Problem |
| Engineering design | Designing a satellite antenna |
| Robotics | Driving autonomous vehicles |

### Logistics Problems And Bin Packing

#### Definitions

> **Bin Packing Problem**: Given $n$ items of different (1D) sizes and some fixed-capacity bins, pack the items into a minimum number of bins.

![Bin packing](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/bin_packing.svg)
*Items of different sizes packed into six fixed-capacity bins. Item sizes are illustrative.*

In the example, one packing uses six bins, and the last bin holds only one small item.

The key question is whether that is the *minimal* number of bins. Checking a given packing is easy, but proving it uses the fewest bins requires considering a huge number of alternative packings.

Real factory and pallet packing is the 3D version: stacking boxes of different sizes on a pallet within a bounding box. This raises the question of what type of computational complexity problem this is. It is an NP-hard problem, covered next.

### Complexity Classes: P, NP, NP-Complete, NP-Hard

#### Definitions

> **P (Polynomial)**: Problems solved in polynomial time: run time increases proportional to a power of the input size, e.g. $n^2$.

> **NP (Non-deterministic Polynomial)**: Problems whose solutions can be *verified* quickly, even if finding solutions takes a long time (found in a non-deterministic way).

> **NP-Complete**: Problems whose solution validity can be verified quickly (in polynomial time), where brute-force search can find a valid solution by trying all possible solutions, and which are "complete" for NP.

> **"Complete"**: The problem is as universal and tough as any other problem in NP. If you find a fast, efficient way to solve *one* NP-complete problem, you can use that method to solve *all* other NP problems.

> **NP-Hard**: Problems at least as hard as NP-complete problems, but which may not be solvable (and verifiable) in non-deterministic polynomial time. There is no known efficient solution.

#### P And NP

A problem is in P if it can be solved in time $O(n^k)$ for some constant $k$, where $n$ is the input size.

A problem is in NP if a proposed solution can be checked in polynomial time. Finding the solution may still take exponential time.

**NP example: Traveling Salesman Problem (TSP)**, finding the shortest path between $n$ cities.

- **Verifiable**: you can quickly compute the length of a given path between $n$ cities to check whether it is the shortest found so far.
- **Difficulty**: the time to find the shortest path increases exponentially with $n$.

#### NP-Complete

NP-complete problems are the hardest problems inside NP.

**NP-complete example: Boolean Satisfiability Problem (SAT)**: assign true/false values to $n$ variables to make a given Boolean formula true.

- **Verification**: given a proposed solution (a specific combination of true/false values), you can check that the formula evaluates to true.
- **Difficulty**: the time to find a solution increases exponentially with $n$. Brute force tries all $2^n$ assignments.

#### NP-Hard

NP-hard problems have no known efficient solution.

- Example: the **Vehicle Routing Problem**.
- Every NP-complete problem is NP-hard, but not all NP-hard problems are in NP.

#### How The Classes Relate

The classes are nested, assuming $P \neq NP$. P sits inside NP, NP-Hard extends beyond NP, and NP-Complete is where NP and NP-Hard overlap.

![Complexity classes](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/complexity_classes.svg)
*P is inside NP, and NP-Hard overlaps NP in the NP-Complete region. Complexity increases upward.*

| Class | Solvable In Polynomial Time? | Verifiable In Polynomial Time? | Example |
|---|---|---|---|
| P | Yes | Yes | Problems with $O(n^2)$ algorithms |
| NP | Not necessarily known | Yes | TSP (decision form) |
| NP-Complete | No known algorithm | Yes | Boolean Satisfiability |
| NP-Hard | No known algorithm | Not necessarily | Vehicle Routing Problem, bin packing (optimisation) |

$$
P \subseteq NP, \qquad \text{NP-Complete} = NP \cap \text{NP-Hard}
$$

The open question: are there polynomial-time algorithms for solving all NP problems, i.e. is $P = NP$? There are no polynomial-time algorithms (yet!) for solving all NP problems, and it is widely believed that $P \neq NP$.

Note on TSP: the lecture uses TSP both as an NP example (verifying a tour) and as an NP-hard problem. The decision version ("is there a tour shorter than $k$?") is NP-complete. The optimisation version ("find the shortest tour") is NP-hard.

### The Vehicle Routing Problem

#### Definitions

> **Vehicle Routing Problem (VRP)**: An NP-hard problem of planning routes for a fleet of vehicles that start and end at a depot and together serve a set of customers.

> **Static Customer**: A customer known at time $t = 0$, included in the initial route plan.

> **Dynamic Customer**: A customer who appears at time $t > 0$, after routes have been planned. Routes must be adjusted to serve them.

Dynamic VRP example with one depot and two vans:

![Dynamic vehicle routing problem](../../../diagrams/CSC3044S-AI%20Systems/AIS/01_Introduction_I/dynamic_vrp.svg)
*Two routes start and end at the depot. Dynamic customers $C_7$ and $C_8$ appear later and are inserted with new route segments.*

- Customers $C_1$ to $C_6$ are static, known at $t = 0$.
- $C_7$ and $C_8$ are dynamic, appearing at $t > 0$.
- Each new customer is inserted into an existing route by replacing one edge with two new route segments.

### Traveling Salesman Problem And Search Space Size

#### Definitions

> **Traveling Salesman Problem (TSP)**: Given $n$ cities, visit each only once and minimise the total tour length. It is NP-hard (no known efficient solution).

> **Search Space**: The set of all candidate solutions; for TSP, all possible tours.

> **Simple Enumeration**: Brute force that evaluates every candidate solution; for TSP its time is proportional to $n!$.

The TSP search space grows factorially:

| Cities $n$ | Possible Tours $n!$ |
|---:|---:|
| $10$ | $10! = 3\,628\,800$ |
| $50$ | $50! \approx 3 \times 10^{64}$ |

Time to solve a 50-city TSP by simple enumeration, assuming the CPU executes $10^{12}$ operations per second:

$$
\text{time} \approx \frac{50!}{10^{12}} \approx \frac{3 \times 10^{64}}{10^{12}} = 3 \times 10^{52} \text{ seconds}
$$

The lecture quotes this as roughly $31\,000$ years. Converting directly gives far longer:

$$
\frac{3 \times 10^{52}\ \text{s}}{3.15 \times 10^{7}\ \text{s/year}} \approx 10^{45}\ \text{years}
$$

Either way the conclusion is the same: brute-force enumeration is hopeless even for 50 cities.

### NP-Hard Optimisation

#### Definitions

> **Optimisation Problem**: Searching for the best solution $x^*$ out of some fixed set $S$ of candidate solutions.

Formally, with an objective (cost) function $f$ to minimise:

$$
x^* = \arg\min_{x \in S} f(x)
$$

For TSP, $S$ is the set of all tours and $f(x)$ is the tour length.

The central question: given computation, memory, and time constraints, how do we find this best solution? Exhaustive search is infeasible for NP-hard problems, which motivates agents and heuristic optimisers that find good solutions within resource limits.

### AI Project: Solving The VRP

The project runs from 14 September to 12 October. The task is to solve the Vehicle Routing Problem (VRP).

Hand-ins and milestones:

| Week | Milestone |
|---|---|
| 1-4 | Weekly code repo commits |
| 5 | Final code hand-in |
| 5-6 | Presentations |

Agent solution:

1. The agent must design an **optimiser module** for solving the VRP.
2. The module plugs into a VRP framework and is tested on 10 known maps.
3. The **final score** measures how close your task performance (averaged over 10 unknown maps) is to a best score.

Scoring example: matching or beating the best score gives $100\%$; reaching $0.1$ of the best score gives $10\%$. So, in effect,

$$
\text{final score} = \min\!\left(1, \frac{\text{your performance}}{\text{best performance}}\right) \times 100\%
$$

Project mark breakdown:

| Component | Weight |
|---|---:|
| Weekly code repo commits | 5% |
| Final score | 25% |
| Presentation | 30% |
| Session history (prompts) | 40% |

### What You Should Know And Reading

After this lecture you should know:

- What an agent is.
- The types of agents.
- What agents can and cannot do.

Reading (on Amathuba):

- Russell & Norvig (2021), *Artificial Intelligence: A Modern Approach*, 4th Edition, Ch. 2 (Intelligent Agents).
- Poole & Mackworth (2023), *Artificial Intelligence: Foundations of Computational Agents*, 3rd Edition, Ch. 1 (Artificial Intelligence and Agents): https://artint.info/3e/html/ArtInt3e.Ch1.html
