---
tags:
  - ai-systems
---

# Agent Architectures: Deductive Control, Hybrid Layers, and Grounding

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3044S Artificial Intelligence: AI Systems  
> **Source**: [2026-CSC3044S-Lecture 4-Agent Architectures - Copy (1).pdf](../../Sources/CSC3044S%20-%20AI%20Systems/2026-CSC3044S-Lecture%204-Agent%20Architectures%20-%20Copy%20%281%29.pdf), Geoff Nitschke, slides 1-49  
> **Generated**: 2026-10-01  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Architecture as modules and interactions|Architecture as modules and interactions]]
  - [[#Deductive action selection|Deductive action selection]]
  - [[#Vacuum world: facts, rules, and execution|Vacuum world: facts, rules, and execution]]
  - [[#Limits of symbolic control and real-world sensing|Limits of symbolic control and real-world sensing]]
  - [[#Hybrid control and layer organization|Hybrid control and layer organization]]
  - [[#TouringMachines and warehouse robots|TouringMachines and warehouse robots]]
  - [[#Embodiment and the symbol-grounding problem|Embodiment and the symbol-grounding problem]]

---

## Core Content

### Architecture as modules and interactions

#### Definitions

> **Agent architecture**: A set of components and a methodology for their interaction that determines actions and future internal state from sensor input and current state.

> **Reactive control**: Direct or tightly coupled observation-to-action control.

> **Deliberative control**: Selection of actions using a represented world and planning or reasoning.

Maes' methodological definition and Kaelbling's module/data-flow definition are complementary. An architecture must identify both the parts and how data and control pass between them.

| Family | Decision structure | Representative examples |
|---|---|---|
| Reactive | Sensors, condition-action behavior, effectors | Subsumption, Boids, stigmergy |
| Deliberative | Sensors, world model, planner, executor, effectors | BDI, agent-oriented programming, deductive reasoning |
| Hybrid | Reactive and deliberative paths with coordination | TouringMachines; model-harness systems |
| Neural/cognitive | Learned components for perception or decisions | ANN/DL-based agents |
| Multi-agent | Several agents interacting | Teams, swarms, distributed problem solving |

Rationality is not guaranteed by selecting a family. A neural or hybrid controller may act well or poorly depending on its information and objective.

![Architecture as modules and interactions: reactive and deliberative paths](../../diagrams/CSC3044S-AI%20Systems/04_Agent_Architectures/reactive_and_deliberative_paths.svg)

*Reactive control offers a direct path; deliberative control inserts a world model, planner, and executor.*

A modern harness can combine model decisions with deterministic validation, context assembly, tools, permissions, and action routing. This is one form of architectural combination, rather than evidence that every LLM product has identical internals.

### Deductive action selection

#### Definitions

> **Deductive agent**: An agent selecting actions by proving statements from a logical description of the world and action rules.

> **Logical database**: A set of facts describing the current world, denoted $\Delta$.

> **Theory**: The rules used for inference, denoted $p$.

> **Predicate**: A logical expression describing a property or relation.

| Symbol | Meaning |
|---|---|
| $\Delta$ | Current-world facts |
| $p$ | Action-selection rules |
| $Ac$ | Available actions |
| $\Delta\vdash_p\Phi$ | Statement $\Phi$ is provable using the facts and rules |
| $\operatorname{Do}(a)$ | Action $a$ is prescribed |
| $\Delta\nvdash_p\neg\operatorname{Do}(a)$ | Prohibition of $a$ is not provable |

The controller first tries to find an explicitly prescribed action. If none is found, it tries an action not ruled out. If both searches fail, it returns no action.

```pseudocode
for each action in available_actions:
    if prescribed(action) is provable:
        return action
for each action in available_actions:
    if prohibited(action) is not provable:
        return action
return null
```

Formally, the two tests are $\Delta\vdash_p\operatorname{Do}(a)$ and $\Delta\nvdash_p\neg\operatorname{Do}(a)$. The second is **not** a proof that the action is safe or beneficial. Action iteration order can influence the returned choice when several actions qualify.

### Vacuum world: facts, rules, and execution

The robot must remove all dirt in a three-by-three grid.

| $y\backslash x$ | $0$ | $1$ | $2$ |
|---|---|---|---|
| $2$ | Dirt | Dirt | Clean |
| $1$ | Clean | Clean | Clean |
| $0$ | Robot, facing north | Clean | Clean |

*The initial grid has dirt at $(0,2)$ and $(1,2)$, with the robot at $(0,0)$.*

| Predicate/action | Meaning |
|---|---|
| $\operatorname{In}(x,y)$ | Robot occupies position $(x,y)$ |
| $\operatorname{Dirt}(x,y)$ | Dirt is at $(x,y)$ |
| $\operatorname{Facing}(d)$ | Robot faces direction $d$ |
| $\operatorname{turn}$ | Turn right |
| $\operatorname{forward}$ | Move forward |
| $\operatorname{suck}$ | Remove dirt at the current cell |

$$
Ac=\{\operatorname{turn},\operatorname{forward},\operatorname{suck}\}.
$$

The illustrated positional rules are:

$$
\begin{aligned}
\operatorname{In}(0,0)\land\operatorname{Facing}(\mathrm{north})\land\neg\operatorname{Dirt}(0,0)
&\to\operatorname{Do}(\operatorname{forward}),\\
\operatorname{In}(0,1)\land\operatorname{Facing}(\mathrm{north})\land\neg\operatorname{Dirt}(0,1)
&\to\operatorname{Do}(\operatorname{forward}),\\
\operatorname{In}(0,2)\land\operatorname{Facing}(\mathrm{north})\land\neg\operatorname{Dirt}(0,2)
&\to\operatorname{Do}(\operatorname{turn}),\\
\operatorname{In}(0,2)\land\operatorname{Facing}(\mathrm{east})
&\to\operatorname{Do}(\operatorname{forward}).
\end{aligned}
$$

The source also gives a reset instruction at $(0,2)$. Taken literally without a condition, resetting there conflicts with continuing east. It is an underspecified part of the example, rather than a complete coverage algorithm.

A natural **supplementary cleaning rule**, needed to connect the dirt-removal goal with the pictured suction action, is:

$$
\operatorname{In}(x,y)\land\operatorname{Dirt}(x,y)
\to\operatorname{Do}(\operatorname{suck}).
$$

> [!warning] <span style="color: #ffc778">The rule sketch is incomplete</span>
> Give cleaning suitable priority and update the database after each action. The displayed four rules alone do not establish cleaning of the full grid.  

![Vacuum world: facts, rules, and execution: vacuum world transitions](../../diagrams/CSC3044S-AI%20Systems/04_Agent_Architectures/vacuum_world_transitions.svg)

*The vacuum-world transition sketch branches into northward and eastward actions. Only suction at a dirty cell changes the dirt set.*

The alternative branches in the example are possible transitions, rather than one mandatory sequential plan. Suction removes the dirt fact at the current location but leaves other dirt facts unchanged.

### Limits of symbolic control and real-world sensing

A logical controller needs accurate facts before reasoning begins. Converting a camera image to $\operatorname{Dirt}(0,1)$ requires perception, not just a theorem prover.

1. Capture observations.
2. Identify relevant features or objects.
3. Translate them into facts and uncertainty estimates.
4. Update the world model.
5. Reason and act before that model becomes stale.

Key problems include difficult transduction, changing environments, and inference cost. General first-order validity is undecidable; unrestricted proof search is not guaranteed to terminate on all inputs. Propositional **SAT** is NP-complete, while propositional entailment in general is coNP-complete. This does not mean every small condition-action rule check is NP-complete.

Vacuum robots provide a practical alternative using continuous feedback from distance, cliff, and bump sensors. Some also use maps and planning. The architecture should match the sensing and task requirements rather than force all raw observations into unrestricted logic.

### Hybrid control and layer organization

#### Definitions

> **Hybrid architecture**: An architecture combining deliberative and reactive components.

> **Horizontal layering**: Layers receive sensor information in parallel and can propose actions directly.

> **Vertical layering**: Information or control passes through layers in sequence.

The deliberative component may use symbolic or learned reasoning. The reactive component handles events without waiting for expensive reasoning. Layers operate at different levels of abstraction.

![Hybrid control and layer organization: hybrid control feedback](../../diagrams/CSC3044S-AI%20Systems/04_Agent_Architectures/hybrid_control_feedback.svg)

*The hybrid architecture joins immediate behavior with a deliberative path and cross-component feedback.*

![Hybrid control and layer organization: horizontal and vertical layers](../../diagrams/CSC3044S-AI%20Systems/04_Agent_Architectures/horizontal_and_vertical_layers.svg)

*Parallel access defines horizontal layering; the vertical variant sends information upward and action control back downward.*

| Aspect | Horizontal | Vertical |
|---|---|---|
| Sensor input | Reaches multiple layers | Enters a layered processing path |
| Action proposals | Multiple layers can contribute | Passed through layers toward output |
| Coordination issue | Conflicting proposals need arbitration | Serial dependencies and delay |
| Variant | Parallel control with mediation | One-pass or two-pass sensor/action flow |

The source includes a vertical variant with upward processing and a returning downward action path. “Horizontal” and “vertical” describe information/control routing, rather than just box placement on a page.

### TouringMachines and warehouse robots

#### Definitions

> **TouringMachines**: Ferguson's hybrid architecture with modeling, planning, and reactive layers inside a control framework.

> **Mediator/control framework**: The mechanism deciding how layer outputs influence behavior.

![TouringMachines and warehouse robots: touring machines control framework](../../diagrams/CSC3044S-AI%20Systems/04_Agent_Architectures/touring_machines_control_framework.svg)

*TouringMachines coordinates three layers inside a common control framework.*

| Layer | Warehouse responsibility | Example output |
|---|---|---|
| Modeling | Represent/update the warehouse and relevant agents | Map and revised obstacle information |
| Planning | Achieve package pickup and drop-off | Route to drop point $(x,y)$ |
| Reactive | Respond to imminent local problems | Stop or turn to avoid collision |
| Control framework | Coordinate their outputs | Allow avoidance to interrupt transport |

Applications include autonomous robots, traffic simulations, automated factories, and distributed problem solving.

A readable reconstruction of the warehouse-control sketch is:

```pseudocode
while packages_remain:
    identify_pickup_and_dropoff()
    update_warehouse_model()
    plan_transport_route()
    while package_not_dropped:
        sense_environment()
        if collision_imminent:
            avoid_collision()
            update_model_and_replan_if_needed()
        else:
            follow_route()
    record_dropoff()
```

The collision handling completes a branch not specified in the short original sketch. It illustrates the intended coordination, rather than claiming to reproduce a complete executable TouringMachines implementation.

If $n$ layers each propose one of $m$ alternatives, there are $mn$ individual candidate proposals. If arbitration considers every joint combination, there can be $m^n$ combinations. The source's $mn$ interaction count should be distinguished from the latter combinatorial case.

A centralized mediator can become a bottleneck. Poor coordination may also create oscillation, delayed emergency response, or contradictory actions.

### Embodiment and the symbol-grounding problem

#### Definitions

> **Computational functionalism**: The position that cognition depends on appropriate information-processing organization rather than a particular physical substrate.

> **Embodied cognition**: The position that cognition depends importantly on bodily interaction with the environment.

> **Symbol grounding**: Connecting symbols to what they mean through perceptual or other world-related capacities rather than only other symbols.

| View | Main emphasis | Implication discussed in the course |
|---|---|---|
| Functionalism | Information processing | Complex reasoning need not use a biological body |
| Embodied cognition | Situated action and perception | Physical interaction contributes meaning and competence |

Brooks argues that useful intelligence can emerge from situated reactive interaction. Dreyfus emphasizes humans' being involved in situations. These are theoretical positions; whether physical embodiment is necessary for general intelligence is not settled simply by an LLM's fluent answer.

The runway example asks for engineers working with drones. Plausible text describes inspection, surveying, sensing, or equipment support. An image can visibly combine engineers, tools, drones, and aircraft in an operationally questionable scene.

| Output | What can look convincing? | What still needs checking? |
|---|---|---|
| Text explanation | General descriptions of inspection and maintenance | Real causal, spatial, and operational details |
| Generated image | Recognizable objects and visual composition | Physical consistency and whether the depicted practice is plausible |
| Embodied action | Direct interaction with sensors and environment | Whether actual outcomes support the chosen actions |

*The text/image comparison illustrates why plausible symbols or recognizable objects do not establish grounded understanding.*
