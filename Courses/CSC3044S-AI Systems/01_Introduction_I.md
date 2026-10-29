---
tags:
  - ai-systems
---

# Introduction I: Agents, Rationality, and Computational Complexity

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3044S Artificial Intelligence: AI Systems  
> **Source**: [2026-CSC3044S-Lecture 1-Introduction - Copy.pdf](../../Sources/CSC3044S%20-%20AI%20Systems/2026-CSC3044S-Lecture%201-Introduction%20-%20Copy.pdf), Geoff Nitschke, slides 1-55  
> **Generated**: 2026-10-01  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Course organization and assessment|Course organization and assessment]]
  - [[#AI traditions and disciplinary roots|AI traditions and disciplinary roots]]
  - [[#Agents and four views of intelligence|Agents and four views of intelligence]]
  - [[#Rationality, utility, and learning|Rationality, utility, and learning]]
  - [[#Intractable problems: packing, SAT, TSP, and VRP|Intractable problems: packing, SAT, TSP, and VRP]]
  - [[#Vehicle-routing project|Vehicle-routing project]]

---

## Core Content

### Course organization and assessment

The course has three sections: agents and agent architectures; AI systems design; and human-centered AI systems and societal impacts.

| Section | Lecturer | Email |
|---|---|---|
| Agents and architectures | Geoff Nitschke | gnitschke@cs.uct.ac.za |
| AI systems design | Francois Meyer | francois.meyer@uct.ac.za |
| Human-centered AI | Melissa Densmore | mdensmore@cs.uct.ac.za |
| Teaching assistant | Oliver Foxcroft | FXCOLI001@myuct.ac.za |
| Teaching assistant | Max Van Veen | VVNMAX002@myuct.ac.za |

| Assessment | Course weight | Arrangements recorded in the 2026 lecture |
|---|---:|---|
| Project | $25\%$ | Released 14 September; due 12 October |
| Test | $25\%$ | 2 October, 18:00-18:45, New LT |
| Exam | $50\%$ | 12 November, two hours, Snape TS2B |
| DP requirement | — | $45\%$ aggregate in practical work |

> [!info] <span style="color: #66b3ff">Course arrangements</span>
> These are the arrangements recorded in the supplied lecture, rather than a live timetable. Extension requests go to the convenor; assignment and test mark queries go to the TAs.

1. Weeks 1-2: AI agents and systems.
2. Week 3: human-centered AI and societal impacts I.
3. Week 4: AI systems design.
4. Week 5: project presentations and demonstrations.
5. Week 6: human-centered AI and societal impacts II.

Assigned chapters and papers are on Amathuba. Main books: Russell and Norvig, *Artificial Intelligence: A Modern Approach*, fourth edition, Chapter 2; Poole and Mackworth, *Artificial Intelligence: Foundations of Computational Agents*, third edition, Chapter 1.

### AI traditions and disciplinary roots

#### Definitions

> **Artificial intelligence (AI)**: The study and construction of systems that exhibit intelligent behavior, including perception, reasoning, learning, and action.

> **Symbolic AI**: A top-down approach using explicit symbols, logic, and rules.

> **Neural or connectionist AI**: A bottom-up approach using networks of connected computational units.

AI draws on computer science, psychology, philosophy, statistics, neuroscience, and machine learning. The overlapping disciplinary diagram represents contributions, rather than a strict classification.

| Method | Disciplinary connection |
|---|---|
| Bayes' rule | Probability |
| Game theory | Mathematics and economics |
| Stochastic gradient descent | Statistics and optimization |
| Value iteration | Control theory |
| Temporal-difference learning | Psychology |
| Artificial neural networks | Neuroscience |

| Aspect | Symbolic AI | Neural AI |
|---|---|---|
| Main representation | Explicit facts, rules, search states | Learned weights and representations |
| Construction | Specify rules and reasoning | Specify architecture, data, training |
| Example visual | Branching game-search tree | Interconnected neural units |
| Typical difficulty | Representation and search complexity | Data quality, generalization, interpretability |

![Symbolic, neural, and other methods contributing to an agent system](../../diagrams/CSC3044S-AI%20Systems/01_Introduction_I/ai_methods.svg)

*Symbolic, neural, and other disciplinary methods can contribute to one agent system.*

The modern agent approach can combine symbolic reasoning, neural learning, optimization, probabilistic inference, and game theory.

### Agents and four views of intelligence

#### Definitions

> **Agent**: An entity that perceives its environment and acts on it.

> **Percept**: Information received through sensing at a particular time.

> **Sensor**: A mechanism through which the agent receives percepts.

> **Actuator**: A mechanism through which the agent performs actions.

> **State**: A description of a situation relevant to decision-making.

> **Action space**: The set of actions available to an agent.

![Agent perception, decision, and action feedback loop](../../diagrams/CSC3044S-AI%20Systems/01_Introduction_I/agent_perception_action_loop.svg)

*The decision procedure connects observations to actions that alter the next observations.*

The decision procedure between sensors and actuators depends on the percepts, available state information, environment, and action space. A thermostat, vacuum robot, autonomous vehicle, and software agent each use different observations and actions.

| View | Main question | Example approach |
|---|---|---|
| Think humanly | Does the internal process resemble human cognition? | Cognitive science and neuroscience |
| Think rationally | Does reasoning follow valid logical rules? | Logic and automated inference |
| Act humanly | Does outward behavior resemble a human's? | Turing-test-style evaluation; ELIZA |
| Act rationally | Do decisions serve the objective well? | Intelligent-agent framework |

> [!tip] <span style="color: #5ad4b5">Behaviour and reasoning are different tests</span>
> A human-like answer need not be rational. A rational decision need not be produced by human-like thought.

| Historical family | Approximate emergence | Main idea |
|---|---|---|
| Symbolic reasoning agents | 1950s onward | Select actions through explicit reasoning |
| Reactive agents | 1980s onward | Respond directly to sensed situations |
| Hybrid agents | 1990s onward | Combine planning with fast reactions |
| Neural/cognitive agents | 2000s onward in this course overview | Learn representations and decision behavior |

### Rationality, utility, and learning

#### Definitions

> **Utility**: A numerical measure of how desirable an outcome is according to the agent's goals.

> **Rational agent**: An agent that selects actions expected to maximize its performance, given its information and available actions.

> **Expected utility**: Utility averaged over possible outcomes, weighted by their probabilities.

> **Reinforcement learning (RL)**: Learning behavior through interaction and reward feedback.

Rationality concerns the decision, rather than the appearance of the thought process. It depends on the performance metric, environmental knowledge, available actions, and sensory information.

A useful formalization is:

$$
a^*=\arg\max_{a\in A}\sum_o P(o\mid a,h)U(o),
$$

where $A$ is the action space, $o$ an outcome, $h$ the information available, and $U(o)$ its utility. This formula supplements the verbal expected-utility definition.

> [!important] <span style="color: #b89aff">Judge the decision using the information available</span>
> A rational action can still have an unlucky outcome. Conversely, a poor decision may succeed by chance. Limited information, inadequate computation, noisy inputs, and inappropriate training data can produce low-utility behavior.

**Hallucination** is a generated claim that is false or unsupported despite appearing plausible. The illustrative glue-on-pizza search result demonstrates why fluent output alone is not a reliable performance measure.

![Reinforcement learning action, state, and reward feedback loop](../../diagrams/CSC3044S-AI%20Systems/01_Introduction_I/reinforcement_learning_loop.svg)

*An RL agent receives state and reward feedback from the environment.*

Simple reflex agents react to current input. Model-based reflex agents also maintain a small internal state. Deliberative agents consider goals and future actions. Learning can improve any of these control styles; it is not a mutually exclusive category.

| Application family | Main activity | Examples named in the September 2026 lecture snapshot |
|---|---|---|
| Coding | Read, edit, run, debug a project | Claude Code, Codex, Cursor, Copilot, Cline, Devin |
| Computer use | Operate graphical interfaces | Computer Use, Operator, Project Mariner |
| Research | Search, compare sources, synthesize reports | Deep Research modes, DeepSearch |
| General tasks | Complete tasks across tools and web | Manus, ChatGPT Agent, Genspark, OpenManus |
| Creative tasks | Operate creative software through connectors | Adobe, Blender, Ableton, Autodesk Fusion workflows |

These names illustrate application families; they do not define rationality or establish a current product ranking.

### Intractable problems: packing, SAT, TSP, and VRP

#### Definitions

> **Decision problem**: A problem with a yes/no answer.

> **Polynomial time**: Runtime bounded by a polynomial in input size.

> **P**: The class of decision problems solvable in polynomial time.

> **NP**: The class of decision problems whose yes answers have certificates verifiable in polynomial time.

> **Polynomial-time reduction**: A transformation from one problem to another computable in polynomial time and preserving the answer.

> **NP-hard**: At least as hard as every problem in NP under polynomial-time reductions.

> **NP-complete**: A decision problem that is both in NP and NP-hard.

> **Optimization problem**: Finding the best feasible solution according to an objective.

The precise relationships are:

$$
\mathrm{P}\subseteq\mathrm{NP},\qquad
\mathrm{NP\text{-}complete}=\mathrm{NP}\cap\mathrm{NP\text{-}hard}.
$$

> [!warning] <span style="color: #ffc778">Three complexity distinctions</span>
> Whether $\mathrm{P}=\mathrm{NP}$ remains unresolved. NP does not mean “non-polynomial.” NP-hardness is a reduction-based property, not a synonym for “no efficient algorithm is known.” [Definition clarification: NIST](https://xlinux.nist.gov/dads/HTML/npcomplete.html).

![Subset relationships among P, NP, NP-complete, and NP-hard](../../diagrams/CSC3044S-AI%20Systems/01_Introduction_I/complexity_class_relationships.svg)

*NP-complete problems lie in both NP and NP-hard. The diagram does not assume that P and NP differ.*

| Problem | What must be found? | What a proposed solution lets us check |
|---|---|---|
| Bin packing | Pack items into the fewest fixed-capacity bins | Each item appears once; capacities and bin-count bound hold |
| Boolean satisfiability, **SAT** | A truth assignment making a formula true | Substitute the assignment and evaluate the formula |
| Traveling salesman, **TSP** | A minimum-length tour visiting each city and returning | Visit validity and whether tour length is at most a bound |
| Vehicle routing, **VRP** | Vehicle routes serving customers under constraints | Customer coverage, route constraints, and objective value |

The optimization versions of TSP and bin packing are NP-hard; the corresponding standard decision versions are NP-complete. Checking the length of a TSP tour does **not** prove global optimality. Exhaustive search illustrates difficulty but does not prove that every possible algorithm must take exponential time.

For a feasible solution set $S$ and cost function $c$:

$$
x^*=\arg\min_{x\in S}c(x).
$$

The raw enumeration example uses $n!$ city orderings: $10!=3{,}628{,}800$ and $50!\approx3.0414\times10^{64}$. Fixing the starting city and identifying reversed symmetric tours reduces duplicates, but leaves factorial growth.

At an optimistic $10^{12}$ orderings checked per second:

$$
T\approx\frac{50!}{10^{12}}\approx3.0414\times10^{52}\ \mathrm{s}
\approx9.64\times10^{44}\ \mathrm{years}.
$$

> [!warning] <span style="color: #ffc778">Factorial growth: arithmetic clarification</span>
> **Arithmetic clarification**: The displayed “31,000 years” does not follow from the given factorial and processing rate. The corrected value is vastly larger; real tour evaluation also costs more than one operation.

The routing diagram includes initially known customers and new customers arriving later:

![Two vehicle routes with later arrivals C8 and C7](../../diagrams/CSC3044S-AI%20Systems/01_Introduction_I/dynamic_vehicle_routes.svg)

*The initial two routes serve known customers; dotted segments accommodate later arrivals.*

Agents may find useful solutions through heuristics, learning, or search under resource constraints. This does not remove worst-case complexity or guarantee optimality.

### Vehicle-routing project

The task is to build an optimizer module that plugs into a VRP framework. Ten known maps support development; evaluation averages performance across ten unknown maps.

| Project component | Project weight |
|---|---:|
| Weekly repository commits | $5\%$ |
| Final performance score | $25\%$ |
| Presentation | $30\%$ |
| Session/prompt history | $40\%$ |

Weekly commits occur in weeks 1-4, final code submission in week 5, and presentations in weeks 5-6. The illustrative score compares task performance with a best score: matching or exceeding it gives $100\%$; one tenth gives $10\%$. Do not apply that illustration directly to a raw route cost without checking the framework's score direction.
