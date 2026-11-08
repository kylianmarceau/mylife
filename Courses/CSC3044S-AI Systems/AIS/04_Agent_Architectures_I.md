---
tags:
  - ai-systems
---

# Agent Architectures I: Reactive, Deliberative, And Hybrid Agents

**Subject**: CSC3044S AI Systems
**Source**: `2026-CSC3044S-Lecture 4-Agent Architectures - Copy (1).pdf`, Geoff Nitschke, pages 1-49
**Generated**: 2026-11-08

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What An Agent Architecture Is|What An Agent Architecture Is]]
  - [[#Modern LLM Agents: Model Plus Harness|Modern LLM Agents: Model Plus Harness]]
  - [[#The Agent Architecture Landscape And Rationality|The Agent Architecture Landscape And Rationality]]
  - [[#Reactive Agent Architectures|Reactive Agent Architectures]]
  - [[#Deliberative Agent Architectures|Deliberative Agent Architectures]]
  - [[#Deductive Reasoning Agents|Deductive Reasoning Agents]]
  - [[#The Vacuum World Example|The Vacuum World Example]]
  - [[#Problems With Deductive Agents And The Roomba Alternative|Problems With Deductive Agents And The Roomba Alternative]]
  - [[#Hybrid Agent Architectures|Hybrid Agent Architectures]]
  - [[#Horizontal And Vertical Layering|Horizontal And Vertical Layering]]
  - [[#TouringMachines|TouringMachines]]
  - [[#Problems With Layered Architectures: The Mediator Function|Problems With Layered Architectures: The Mediator Function]]
  - [[#Why Reactive Architectures Came Back|Why Reactive Architectures Came Back]]
  - [[#Intelligence And Embodiment|Intelligence And Embodiment]]
  - [[#Symbol Grounding In Current Generative Agents|Symbol Grounding In Current Generative Agents]]
  - [[#Comparing Reactive, Deliberative, And Hybrid Agents|Comparing Reactive, Deliberative, And Hybrid Agents]]

---

## Core Content

### What An Agent Architecture Is

#### Definitions

> **Agent Architecture (Maes, 1991)**: A particular methodology for building agents. It specifies how the agent can be decomposed into a set of component modules and how these modules should interact. The total set of modules and their interactions must answer how the sensor data and the current internal state of the agent determine the actions and future internal state of the agent. An architecture encompasses the techniques and algorithms that support this methodology.

> **Agent Architecture (Kaelbling, 1991)**: A specific collection of software (or hardware) modules, typically drawn as boxes with arrows indicating the data and control flow among the modules. More abstractly, a general methodology for designing particular modular decompositions for particular tasks.

Both definitions say the same core thing: an architecture is a **modular decomposition** of an agent plus the rules for how those modules interact.

The central question any architecture must answer is:

$$
(\text{sensor data}, \text{current internal state}) \;\longrightarrow\; (\text{action}, \text{next internal state})
$$

| Aspect | Maes (1991) | Kaelbling (1991) |
|---|---|---|
| Emphasis | Methodology for building agents | Concrete set of modules with data/control flow |
| What it specifies | Module decomposition, module interaction, supporting techniques and algorithms | Boxes (modules) and arrows (data and control flow) |
| Abstract view | Answers how percepts + internal state determine actions + future state | General methodology for designing modular decompositions for particular tasks |

### Modern LLM Agents: Model Plus Harness

#### Definitions

> **Harness**: Everything around the model in an LLM agent: the infrastructure that assembles context, provides tools, validates outputs, routes actions, and makes every stage observable. "The model reasons. The harness governs everything else."

> **Chain**: A fixed, pre-scripted sequence of model calls. The developer hard-codes the steps; the model does not decide what to do next.

> **Agent (LLM sense)**: A system in which the model chooses its own next action inside a loop.

A modern LLM agent is a **hybrid architecture** summarised as:

$$
\text{Agent} = \text{Model} + \text{Harness}
$$

![Agent = Model + Harness](../../../diagrams/CSC3044S-AI%20Systems/AIS/04_Agent_Architectures_I/model_plus_harness.svg)
*The LLM only reasons; the harness assembles context, provides tools, validates outputs, routes actions (execute, review, escalate) and makes every stage observable.*

The harness components, in the order data flows through them:

1. **Context assembly** curates what the model sees from incoming data, queries, and events.
2. **Tool access** provides managed credentials and connections (keys, APIs) the model can call.
3. The **LLM** reasons over the assembled context and tool results.
4. **Output validation** applies guardrails before any action is taken.
5. **Action routing** uses confidence, rules, and escalation policies to **execute**, send for **review**, or **escalate**.
6. **Observability** spans every stage, so each stage is inspectable and auditable.

What is and is not an agent:

| System | Who decides the next step? | Agent? |
|---|---|---|
| Chatbot with browsing | Makes one tool call, then answers | Not yet an agent in the full sense |
| Chain | The developer, by hard-coding the sequence | No |
| Agent | The model, at each loop iteration | Yes |

The model, not the developer, deciding execution at each loop iteration is what changed between 2023 and 2026. That shift is the source of both the new capabilities and the new failure modes of agents.

### The Agent Architecture Landscape And Rationality

Agent architectures branch into five families: **reactive agents**, **deliberative agents**, **hybrid agents**, **multi-agent systems**, and **neuro-agents**. The question posed is: where are the **rational agents**?

![Agent architecture landscape](../../../diagrams/CSC3044S-AI%20Systems/AIS/04_Agent_Architectures_I/architecture_landscape.svg)
*All five families sit inside the Rational region; hybrid agents and neuro-agents are also circled as possibly Irrational?.*


| Family | Rationality grouping |
|---|---|
| Reactive agents | Rational |
| Deliberative agents | Rational |
| Multi-agent systems | Rational |
| Hybrid agents | Overlaps with the "Irrational?" region |
| Neuro-agents | Overlaps with the "Irrational?" region |

The broad "Rational" region covers all five families. A second, smaller region labelled "Irrational?" circles hybrid agents and neuro-agents, flagging that architectures containing neural (e.g. LLM) components may not always behave rationally. The question mark marks this as an open issue rather than a settled classification.

### Reactive Agent Architectures

#### Definitions

> **Reactive Agent**: An agent with at most a very simple internal representation of the world, providing tight coupling of perception and action.

> **Behaviour-Based Paradigm**: The design approach behind reactive agents, in which intelligence is a product of interaction between an agent and its environment.

> **Stimulus-Response Behaviour**: A direct mapping from a sensed state to an action, with no planning step in between.

> **Emergent Behaviour**: Global behaviour of a system that arises from simple local interactions rather than being explicitly programmed.

![Reactive agent architecture](../../../diagrams/CSC3044S-AI%20Systems/AIS/04_Agent_Architectures_I/reactive_agent.svg)
*Sensors feed a bank of stimulus-response rules, each mapping a state directly to an action that drives the effectors.*

Each behaviour is a pair $\text{State}_i \rightarrow \text{Action}_i$ for $i = 1, \dots, n$. There is no world model and no planner: perception maps almost directly to action.

Key properties:

- At most a very simple internal world representation
- Tight perception-action coupling
- Behaviour-based paradigm
- Intelligence emerges from agent-environment interaction

Examples of reactive architectures:

| Example | Description | Reference |
|---|---|---|
| **Subsumption architecture** | Layered reactive behaviours (covered next lecture) | Brooks (1991), "Intelligence Without Representation" |
| **Boids** | Emergent flocking/herding/schooling multi-agent model | Reynolds (1987) |
| **Stigmergy model** | Coordination through modifications left in the environment (distributed building) | Theraulaz & Bonabeau (1995) |
| A few others | Other emergent-behaviour multi-agent system models | — |

### Deliberative Agent Architectures

#### Definitions

> **Deliberative Agent**: An agent that follows a sense-plan-act cycle: it senses its environment, generates a plan, and acts on that plan.

> **Sense-Plan-Act**: The framework describing how agents sense their environment, generate a plan, and act on the plan.

> **World Model**: An internal representation of the environment that the planner reasons over.

![Deliberative agent architecture](../../../diagrams/CSC3044S-AI%20Systems/AIS/04_Agent_Architectures_I/deliberative_agent.svg)
*Sense-plan-act: sensor data updates a world model, the planner builds a plan over it, and the plan executor drives the effectors.*

Unlike a reactive agent, every percept passes through the world model and planner before any action is taken.

Deliberative behaviour is dictated by:

- **Environment state**
- **Internal state**
- **Plan**, produced by logical reasoning, symbolic manipulation, a rule set, an ANN, etc.

Overall, the agent maps inputs to outputs:

$$
\text{inputs} \rightarrow \text{outputs}
$$

Examples of deliberative architectures:

| Example | Reference |
|---|---|
| **Belief-Desire-Intention (BDI) architecture** | Rao & Georgeff (1991) |
| **Agent-Oriented Programming** | Shoham (1990) |
| **Deductive reasoning agents** | Walton (2006) |

### Deductive Reasoning Agents

#### Definitions

> **Deductive Reasoning Agent**: A deliberative agent that decides what to do by theorem proving: logic encodes a theory stating the best action to perform in any given situation.

> **Theory $\rho$**: The set of rules (deduction rules) that state which action is best in each situation.

> **Database $\Delta$**: A logical database describing the current state of the world.

> **Action Set $Ac$**: The set of actions the agent can perform.

> **Provability $\Delta \vdash_{\rho} \varphi$**: The formula $\varphi$ can be proved from $\Delta$ using the rules $\rho$.

The agent answers "what should I do?" by trying to prove that an action should be done.

| Symbol | Meaning |
|---|---|
| $\rho$ | Theory / rule set |
| $\Delta$ | Current world-state database |
| $Ac$ | Set of available actions |
| $\alpha \in Ac$ | A candidate action |
| $Do(\alpha)$ | Predicate "action $\alpha$ should be done" |
| $\Delta \vdash_{\rho} \varphi$ | $\varphi$ is provable from $\Delta$ using $\rho$ |
| $\Delta \nvdash_{\rho} \neg Do(\alpha)$ | It cannot be proved that $\alpha$ should *not* be done |

Action selection algorithm:

```text
for each α ∈ Ac do                 /* try to find an action explicitly prescribed */
    if Δ ⊢ρ Do(α) then
        return α
    end-if
end-for

for each α ∈ Ac do                 /* try to find an action not excluded */
    if Δ ⊬ρ ¬Do(α) then
        return α
    end-if
end-for

return null                        /* no action found */
```

Step by step:

1. For each action $\alpha \in Ac$, try to prove $\Delta \vdash_{\rho} Do(\alpha)$. If successful, return $\alpha$: this action is **explicitly prescribed**.
2. If no action is prescribed, loop over $Ac$ again. Return the first $\alpha$ for which $\Delta \nvdash_{\rho} \neg Do(\alpha)$: this action is **not excluded**, so it is at least consistent with the rules.
3. If every action is excluded, return `null`: no action found.

### The Vacuum World Example

#### Definitions

> **Vacuum World**: A $3 \times 3$ grid in which a cleaning robot must clear up all the dirt.

> **Domain Predicate**: A logical predicate describing part of the world state.

The grid uses coordinates $(x, y)$ with $x, y \in \{0, 1, 2\}$. The robot starts at $(0, 0)$, and dirt is at $(0, 2)$ and $(1, 2)$. The goal is to clear up all dirt.

![Vacuum world grid](../../../diagrams/CSC3044S-AI%20Systems/AIS/04_Agent_Architectures_I/vacuum_world_grid.svg)
*The 3×3 vacuum world: robot at (0,0) facing north, dirt at (0,2) and (1,2).*

Domain predicates:

| Predicate | Meaning |
|---|---|
| $In(x, y)$ | The agent is at $(x, y)$ |
| $Dirt(x, y)$ | There is dirt at $(x, y)$ |
| $Facing(d)$ | The agent is facing direction $d$ |

Possible actions:

$$
Ac = \{ turn,\ forward,\ suck \}
$$

where $turn$ means turn right.

#### Example Run (State Transitions)

Initial state: $In(0,0)$, $Facing(north)$, $Dirt(0,2)$, $Dirt(1,2)$. Each action produces a new world state:

![Vacuum world example run](../../../diagrams/CSC3044S-AI%20Systems/AIS/04_Agent_Architectures_I/vacuum_example_run.svg)
*State transitions from the initial state. The teal path (forward, forward, suck) removes Dirt(0,2); sucking at (1,0) leaves the state unchanged.*

The top path (forward, forward, suck) reaches and removes the dirt at $(0,2)$. The lower branches show that other action choices move the robot away from the dirt or waste actions, which is why the rule set $\rho$ must prescribe the right action in each state.

#### Rules $\rho$ For Deciding What To Do

$$
\begin{aligned}
In(0,0) \wedge Facing(north) \wedge \neg Dirt(0,0) &\longrightarrow Do(forward) \\
In(0,1) \wedge Facing(north) \wedge \neg Dirt(0,1) &\longrightarrow Do(forward) \\
In(0,2) \wedge Facing(north) \wedge \neg Dirt(0,2) &\longrightarrow Do(turn) \\
In(0,2) \wedge Facing(east) &\longrightarrow Do(forward)
\end{aligned}
$$

Plus a control rule: if the robot is at $In(0,2)$, reset its position to $(0,0)$.

How the rules drive the robot:

1. At $(0,0)$ facing north with no dirt, move forward to $(0,1)$.
2. At $(0,1)$ facing north with no dirt, move forward to $(0,2)$.
3. At $(0,2)$ facing north: if there is dirt, a cleaning rule must fire first (the general cleaning rule $In(x,y) \wedge Dirt(x,y) \longrightarrow Do(suck)$ is the standard companion to these movement rules). Once $\neg Dirt(0,2)$ holds, turn right to face east.
4. At $(0,2)$ facing east, move forward towards $(1,2)$.

Starting at $(0,0)$, the robot will clean up the dirt. The open questions are: what are the problems with this approach, and is there a better way?

### Problems With Deductive Agents And The Roomba Alternative

#### Definitions

> **Static Environment Assumption**: The assumption that the world does not change while the agent is deliberating.

> **First-Order Logic (FOL)**: Logic with quantified variables over objects, e.g. $\forall x$.

> **Propositional Logic**: Logic over true/false statements without variables or quantifiers.

> **Boolean Satisfiability Problem (SAT)**: Deciding whether a propositional formula has a satisfying true/false assignment; NP-complete.

Problems with the deductive (logic-based) vacuum agent:

| Problem | Explanation |
|---|---|
| Perception-to-symbol conversion | How do you convert raw video-camera input into a predicate like $Dirt(0,1)$? |
| Static environment | Decision making assumes the world does not change during reasoning |
| FOL is impractical | Decision making in first-order logic is impractical; see example below |
| Propositional logic is intractable | Worst-case decision making is NP-complete, like SAT |

First-order logic example of domain knowledge:

$$
\forall x \,\big( is\text{-}carpet(x) \rightarrow is\text{-}floor(x) \big);\quad is\text{-}floor(x) \rightarrow cleanable(x);\ \dots
$$

Propositional logic example: a chain of true/false conditions such as "if $x$ = carpet, $x$ = adjacent, $x$ = dirty then $clean(x)$; else if ...". Like SAT, the time to find a solution grows exponentially with the number of variables $n$:

$$
\text{worst-case time} \in O(2^{n})
$$

#### A Better Approach: The Roomba

The Roomba robot vacuum is a practical answer to "is there a better way?". Instead of a logical world model, it relies on simple sensors and reactive behaviours.

Sensors and parts on the robot:

- **Infrared sensor**
- **Cliff sensor** (detects drops such as stairs)
- **Smart bumper** (detects contact with obstacles)
- **Side brush**
- Handle, power button, bin release, wheels

Cleaning behaviour:

![Roomba cleaning pattern](../../../diagrams/CSC3044S-AI%20Systems/AIS/04_Agent_Architectures_I/roomba_coverage.svg)
*The Roomba spirals out from its start point, follows walls and furniture edges, and bounces across the room in straight lines on contact.*


A long-exposure photograph of a Roomba's light trail shows dense, overlapping straight-line paths covering the whole floor. The full coverage emerges from simple react-to-contact rules, not from planning a route over a map.

### Hybrid Agent Architectures

#### Definitions

> **Hybrid Agent**: An agent that combines a deliberative component and a reactive component.

> **Deliberative Component**: Subsystems that make decisions using cognitive (e.g. neuro-based) or symbolic (e.g. logic-based) reasoning.

> **Reactive Component**: Subsystems that react quickly to events without complex reasoning.

![Hybrid agent architecture](../../../diagrams/CSC3044S-AI%20Systems/AIS/04_Agent_Architectures_I/hybrid_agent.svg)
*Sensors feed both components. The reactive component sends observations up; the deliberative component sends modifications down; both drive the effectors.*

The two components interact in both directions:

- The reactive component passes **observations** up to the deliberative component.
- The deliberative component sends **modifications** down, changing the reactive behaviours.

| Component | Reasoning | Speed | Typical role |
|---|---|---|---|
| Deliberative | Cognitive (neuro) or symbolic (logic) | Slow | Planning, goals, world modelling |
| Reactive | No complex reasoning | Fast | Immediate responses to events |

Hybrid architectures combine the two components into a **hierarchy of interacting layers**. Each layer reasons at a different **level of abstraction**.

### Horizontal And Vertical Layering

#### Definitions

> **Horizontal Layering**: Every layer is directly connected to the sensor input and to the action output; each layer acts like a separate agent proposing actions.

> **Vertical Layering**: Sensor input and action output are handled by at most one layer each; control passes up (and possibly down) through the layers in sequence.

> **One-Pass Vertical Architecture**: Control flows up through the layers from sensor input at $\text{Layer}_1$ to action output at $\text{Layer}_n$.

> **Two-Pass Vertical Architecture**: Information flows up through the layers, then control flows back down, with action output leaving from the bottom layer.

![Horizontal vs vertical layering](../../../diagrams/CSC3044S-AI%20Systems/AIS/04_Agent_Architectures_I/layering.svg)
*Horizontal: every layer sees the input and proposes output. Vertical one-pass: input flows up to the top layer, which acts. Vertical two-pass: information flows up, control flows back down, and action leaves at the bottom.*

| Property | Horizontal layering | Vertical layering |
|---|---|---|
| Sensor input reaches | Every layer | Bottom layer only |
| Action output comes from | Every layer | Top layer (one-pass) or bottom layer (two-pass) |
| Conceptual simplicity | High: each layer is a separate behaviour | Lower: layers depend on each other in sequence |
| Coordination need | Needs a mediator to resolve competing layer outputs | Built into the pass order |
| Risk | Mediator becomes a bottleneck | Failure in one layer blocks the whole chain |

### TouringMachines

#### Definitions

> **TouringMachines (Ferguson, 1992)**: A horizontally layered hybrid architecture with three control layers embedded in a control framework, sitting between a perception subsystem and an action subsystem.

> **Control Framework**: The mediating mechanism that decides which layer has control at any time.

![TouringMachines architecture](../../../diagrams/CSC3044S-AI%20Systems/AIS/04_Agent_Architectures_I/touringmachines.svg)
*The perception subsystem feeds the modelling (M), planning (P) and reactive (R) layers in parallel inside the control framework; all three connect to the action subsystem.*

Because every layer connects to both perception and action, TouringMachines is horizontally layered.

The hybrid structure makes TouringMachines suitable for complex, dynamic environments:

| Application area | Why the hybrid structure helps |
|---|---|
| **Autonomous robotics** | Reactive layer handles obstacle avoidance; planning layer handles navigation |
| **Multi-agent systems** | Effective for traffic control simulations, automated factory floors, and distributed problem-solving nodes |

#### Warehouse Robot Example

A warehouse floor with package-moving robots maps onto the three layers:

| Layer | Robot behaviour |
|---|---|
| Planning layer | Transport package to drop-point $(x, y)$ |
| Modelling layer | Map of the warehouse floor |
| Reactive layer | Avoid collisions |

### Problems With Layered Architectures: The Mediator Function

#### Definitions

> **Mediator Function**: A central control system that decides which layers are active, and when, in a layered architecture.

> **Bottleneck**: A single point through which all decisions must pass, limiting speed and robustness.

The core problem: how do we decide which layers are active, and when?

The mediator function answers this, but it must consider every combination of layer suggestions. With $n$ layers, each capable of $m$ possible actions, the number of possible interactions is

$$
m^{n}
$$

(Wooldridge's standard result for horizontally layered architectures; the lecture writes this as "$mn$" interactions.) Either way, the mediator must handle a combinatorial number of cases, and because all decisions pass through it, it can introduce a **bottleneck** into the agent's decision making.

#### Mediator Function For Warehouse Packing/Sorting

```text
WHILE package NOT dropped                 // Planning layer active
    WHILE collision NOT imminent          // Reactive layer inactive
        Map path (next package) pick-up -> drop-off;
                                          // Modeling layer active; Planning layer inactive
        Go;                               // Planning layer active; Modelling layer inactive
    DO
DO
RESTART
```

How control switches between layers:

1. While the package has not been dropped, the **planning layer** is active.
2. While no collision is imminent, the **reactive layer** stays inactive.
3. To map the path from pick-up to drop-off for the next package, the **modelling layer** becomes active and the planning layer goes inactive.
4. To execute the path ("Go"), the **planning layer** is active again and the modelling layer goes inactive.
5. If a collision becomes imminent, the inner loop exits and the reactive layer takes over.
6. When the package is dropped, the outer loop ends and the process restarts for the next package.

### Why Reactive Architectures Came Back

Many problems in **symbolic AI** remained unsolved: perception-to-symbol conversion, static-world assumptions, and intractable logical reasoning. This led researchers to question the viability of the whole symbolic paradigm, and so they developed **reactive** and then **hybrid** architectures.

| Architecture style | Cycle | Current status |
|---|---|---|
| Deliberative | Sense-plan-act | Popular current agents (Claude, Gemini, GPT, ...) are all deliberative; overly complex for many real-world problems and unsuitable for others |
| Reactive | Sense-react | The simplest approach |
| Hybrid | Both | Combines fast reaction with planning |

### Intelligence And Embodiment

#### Definitions

> **Computational Functionalism**: The view that intelligence is complex information processing, independent of substrates and referents (Newell & Simon, 1976).

> **Embodied Cognition**: The view that intelligent agents must interact with the real world; embodiment is necessary to give meaning to symbols.

> **Symbol Grounding Problem (Harnad, 1990)**: The problem of how symbols manipulated by a system acquire real meaning, rather than meaning only in relation to other symbols.

Two perspectives on how to achieve general intelligence:

| Perspective | Claim | Supporting evidence / proponents |
|---|---|---|
| Computational functionalism | Intelligence is information processing independent of the physical substrate and of what symbols refer to | Newell & Simon (1976); recent LLM agents with emergent reasoning abilities (Wei et al., 2022) |
| Embodied cognition | Intelligence requires real-world (physical) interaction; embodiment gives symbols meaning | Harnad (1990), Brooks (1991), Dreyfus (2006) |

Dreyfus (2006) puts the embodied view this way: "What separates humans from machines is the fact that we exist in situations, not apart from them, and that we do so in an embodied and non-conceptual way." This is again the symbol grounding problem.

### Symbol Grounding In Current Generative Agents

#### Definitions

> **Ontological Grounding**: A connection between a system's representations and real-world experience.

> **Absorbed Coping**: Handling situations through practised, non-reflective engagement rather than explicit reasoning.

For **text generation**, the lack of symbol grounding is not obvious. LLMs can get away with vague, general statements because the reader's imagination fills in the gaps.

Example: asked to explain "engineers working on a runway, aided by drones", an LLM gives a plausible general answer listing:

1. Inspection and monitoring
2. Surveying
3. Data collection
4. Maintenance and repairs

The text reads well because it stays general.

For **image generation**, the gap is exposed. Given the same prompt, DALL-E 3 produces an image that must commit to concrete details. The scene is physically incoherent: for example, an aircraft flying low directly over engineers working on an active runway, among construction cranes. These are details a system grounded in real-world experience would not produce.

Conclusions:

- AI systems do not exist in the world in an embodied sense.
- They experience things through absorbed coping and inference.
- AI processing has no ontological grounding (real-world experience).

### Comparing Reactive, Deliberative, And Hybrid Agents

| Agent type | Internal world model | Decision mechanism | Strength | Weakness |
|---|---|---|---|---|
| Reactive | None or very simple | Direct stimulus-response ($\text{State}_i \rightarrow \text{Action}_i$) | Fast, robust, simple | Limited long-term goal-directed behaviour |
| Deliberative | Explicit world model | Sense-plan-act (logic, rules, ANN) | Goal-directed planning | Perception-to-symbol problem, static-world assumption, intractable reasoning |
| Hybrid | Deliberative layer has one; reactive layer does not | Layered: reactive + deliberative, coordinated by a mediator | Fast reactions plus planning in dynamic environments | Deciding which layer is active; mediator bottleneck and combinatorial interactions |

The next lecture covers the **subsumption architecture**: what it is, its benefits, and its limits.
