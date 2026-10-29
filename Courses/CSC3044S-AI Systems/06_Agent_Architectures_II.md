---
tags:
  - ai-systems
---

# Agent Architectures II: Emergence, Subsumption, Continuum Crowds, and Boids

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3044S Artificial Intelligence: AI Systems  
> **Source**: [2026-CSC3044S-Lecture 6-Agent Architectures (II) - Copy (1).pdf](../../Sources/CSC3044S%20-%20AI%20Systems/2026-CSC3044S-Lecture%206-Agent%20Architectures%20%28II%29%20-%20Copy%20%281%29.pdf), Geoff Nitschke, slides 1-49  
> **Generated**: 2026-10-01  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Architecture overview and emergence|Architecture overview and emergence]]
  - [[#Deep learning, scale, and hallucinations|Deep learning, scale, and hallucinations]]
  - [[#Brooks' subsumption architecture|Brooks' subsumption architecture]]
  - [[#Continuum crowds|Continuum crowds]]
  - [[#Boids: local steering and collective patterns|Boids: local steering and collective patterns]]
  - [[#Stigmergy, combined models, and design limits|Stigmergy, combined models, and design limits]]

---

## Core Content

### Architecture overview and emergence

#### Definitions

> **Emergent behavior**: A global pattern arising from local components and their interactions with an environment rather than an explicit global instruction.

> **Multi-agent system (MAS)**: A system containing multiple interacting agents.

> **Generalization**: Applying learned behavior to inputs beyond exact training examples.

| Family | Examples grouped in the lecture |
|---|---|
| Reactive | Subsumption, Boids, continuum crowds, stigmergy |
| Deliberative | BDI |
| Cognitive | AASMO, Soar, ACT-R, Brahms, LIDA, PreAct, Cougaar, PRODIGY, FORR |
| Hybrid | 3T, AuRA, Brahms, GAIuS, GRL, ICARUS, InteRRaP, TinyCog, TouringMachines |

These are the lecture's broad groupings; named cognitive architectures need not all be purely neural, and architecture categories can overlap.

The BDI-to-LLM comparison is an analogy:

| BDI component | LLM-agent analogue |
|---|---|
| Beliefs: world model | Context window, retrieved memory, tool results |
| Desires: goals | System/task objectives |
| Intentions: committed plans | Maintained current plan or task state |

A generated reasoning trace is not automatically a formal intention-management mechanism.

![Architecture overview and emergence: local interactions and emergence](../../diagrams/CSC3044S-AI%20Systems/06_Agent_Architectures_II/local_interactions_and_emergence.svg)

*Global behavior depends on local interactions, parameters, and the environment.*

Examples include flocks, robot teams, termite construction, traffic, and interacting neural units. Local rules do not map one-to-one onto global patterns; parameters and environment matter.

### Deep learning, scale, and hallucinations

#### Definitions

> **Artificial neural network (ANN)**: A network of computational units connected by adjustable weights.

> **Deep learning (DL)**: Learning with models containing multiple processing layers.

> **Hallucination**: Generated content that is false or unsupported in the relevant factual or task context.

Designers choose architecture and training methods; learned weights jointly determine outputs. Universal function approximation describes what a model class can represent under assumptions, rather than proving that a trained model generalizes correctly.

| Illustrated scale plot | Pattern to recognize |
|---|---|
| Three-digit addition | Near-zero exact accuracy followed by a sharp increase |
| Massive multitask language understanding | Performance rises as size increases |
| Program synthesis | Improvement over scale with a sharper rise near the largest model |

*These qualitative plots relate parameter count to task metrics; a visible threshold does not by itself establish an all-or-nothing internal ability.*

| Failure illustration | What went wrong? |
|---|---|
| Asked to translate a question, but answered it | Instruction inconsistency |
| Summary changes the Nile's origin relative to retrieved text | Context/faithfulness inconsistency |
| Algebra starts correctly but ends with an inconsistent result | Logical inconsistency |

The neural-layer visualization traces information through repeated learned transformations. Complex interaction can be hard to inspect; failed generalization is one proposed explanation for hallucination, not a complete theory of every failure.

![Deep learning, scale, and hallucinations: successive learned representations](../../diagrams/CSC3044S-AI%20Systems/06_Agent_Architectures_II/successive_learned_representations.svg)

*The neural-layer visual is reconstructed as successive learned transformations; output depends on their combined behavior.*

Intentional fantasy art is not automatically a factual hallucination. Judge output against the task: inventiveness may be desired in art and harmful in factual reporting.

### Brooks' subsumption architecture

#### Definitions

> **Subsumption architecture**: A layered reactive architecture whose task-accomplishing behaviors can suppress or override signals in other behavior paths.

> **Behavior layer**: A controller for a particular task using relevant sensor information.

> **Situated/embodied intelligence**: Intelligent behavior arising through interaction with an actual environment.

Brooks' thesis is that intelligent behavior can arise without a detailed symbolic representation or explicit theorem-proving system. The world itself supplies continuing feedback.

Lower layers provide primitive competence; added layers support broader tasks. Generic higher layers can subsume lower outputs. Practical collision and avoidance priorities must still be designed explicitly; diagram height alone does not establish safety priority.

![Brooks' subsumption architecture: subsumption behaviour hierarchy](../../diagrams/CSC3044S-AI%20Systems/06_Agent_Architectures_II/subsumption_behaviour_hierarchy.svg)

*Parallel task controllers can suppress or override lower-level signal paths according to the designed hierarchy.*

The light-avoiding robot combines light avoidance, object avoidance, and collision recovery. Sensors feed the behavior modules and actuators change the robot's position, producing new sensor input.

| Maze behavior | Trigger and response |
|---|---|
| Collision recovery | On collision, back up and turn about $90^\circ$ in a random direction |
| Object avoidance | Move forward; near obstacles at roughly $5.0\,\mathrm{cm}$, turn about $90^\circ$ |
| Explore world | Move away from the starting point |

![Brooks' subsumption architecture: maze navigation behaviours](../../diagrams/CSC3044S-AI%20Systems/06_Agent_Architectures_II/maze_navigation_behaviours.svg)

*Local motion and recovery modules jointly produce maze traversal without a symbolic full-maze plan.*

All modules run in parallel. Maze traversal can emerge without explicitly storing the concepts “wall” or “maze navigation.” The outcome is not a guarantee of solving every maze or finding an optimal route.

| Benefit | Mechanism | Limit |
|---|---|---|
| Simplicity/modularity | Separate local controllers | Interactions can still be difficult to debug |
| Responsiveness | Tight sensor-action coupling | Weak long-range planning |
| Incremental construction | Add competence layers | New tasks often need new rules |
| Partial fault tolerance | Some behavior can continue after a module fails | Loss of a critical layer can remain serious |

Basic fixed-rule subsumption lacks rich memory, learning, and abstract reasoning. Extensions can add learned controllers, as in the next lecture; this does not remove the difficulty of achieving a desired global behavior.

### Continuum crowds

#### Definitions

> **Continuum crowd model**: A model guiding many agents through shared spatial fields that account for movement costs.

> **Discomfort field**: A spatial function $g(x)$ describing how undesirable positions are.

| Symbol | Meaning |
|---|---|
| $G$ | Geographic goal region |
| $f$ | Maximum feasible speed field |
| $g$ | Discomfort field |
| $x$ | Current position |
| $P$ | Paths from $x$ to a point in $G$ |

The four movement principles are:

1. Seek a geographic goal $G$.
2. Move at the feasible speed allowed by $f$.
3. Prefer lower discomfort: $g(x)<g(x_0)$ makes $x$ more desirable than $x_0$ on that criterion.
4. Select a path $p\in P$ considering length, travel time, and accumulated discomfort.

| Heat-map color in the example | Discomfort |
|---|---|
| Red | Highest |
| Purple | High |
| Orange | Low |
| Green | Lowest |

*The heat map marks spatial preference; it does not specify an exact numeric cost for each color.*

![Continuum crowds: continuum crowd path selection](../../diagrams/CSC3044S-AI%20Systems/06_Agent_Architectures_II/continuum_crowd_path_selection.svg)

*Shared spatial fields influence path choice for crowd agents.*

A **supplementary illustrative objective**, with nonnegative weights $\alpha,\beta,\gamma$, is:

$$
C(p)=\alpha L(p)+\beta T(p)+\gamma D(p),\qquad
p^*=\arg\min_{p\in P}C(p).
$$

The lecture does not specify these weights or this exact formula. A numeric comparison requires an explicit tradeoff between length, time, and discomfort. The crowd visual shows agents moving through a shared street environment; graphics, games, and movies are applications.

### Boids: local steering and collective patterns

#### Definitions

> **Boid**: One simulated flocking agent.

> **Neighborhood**: Agents within a selected distance and view angle.

> **Separation/repulsion**: Steering to avoid crowding nearby agents.

> **Alignment/orientation**: Steering toward the average heading of neighbors.

> **Cohesion/attraction**: Steering toward neighbors' average position.

> [!warning] <span style="color: #ffc778">Alignment and cohesion</span>
> **Terminology clarification**: The introductory rule list swaps the descriptions of attraction and orientation. The standard mapping is heading → alignment, position → cohesion. [Craig Reynolds' Boids description](https://www.red3d.com/cwr/boids/).  

![Boids: local steering and collective patterns: boids steering components](../../diagrams/CSC3044S-AI%20Systems/06_Agent_Architectures_II/boids_steering_components.svg)

*The three distinct steering effects combine to change individual movement.*

Boids react locally without needing a symbolic global flock plan. They still have physical state such as position and velocity; “no internal state” here should not be read as absence of any state in the simulation.

The radius notation in the examples is:

$$
r_c\le r_o\le r_a,
$$

for repulsion, orientation, and attraction radii. The later figure uses $r_r$ for the repulsion radius.

| Zone | Spatial meaning | Steering role |
|---|---|---|
| Inner | Within repulsion radius | Avoid crowding |
| Middle | Orientation region | Align headings |
| Outer | Attraction range | Maintain group cohesion |
| Blind sector | Outside the view angle | Neighbors there are not used |

*The concentric-zone diagram expresses increasing sensing ranges and a rear blind sector.*

The text's interval wording is inconsistent: it places orientation between $r_o$ and $r_a$, while the illustrated middle zone conventionally lies between $r_c$ and $r_o$. Treat the named steering effects as primary, and specify the intended neighborhoods when implementing a particular variant.

The demonstration uses $N=400$, view angle $\alpha=270^\circ$, and a displayed average heading $\theta=40^\circ$.

| Pattern | $r_o$ | $r_a$ | Shape to recognize |
|---|---:|---:|---|
| Swarming | $0.10$ | $0.85$ | Compact irregular swarm |
| Dispersion | $0.15$ | $0.25$ | Spread-out agents |
| Toroidal | $0.25$ | $0.85$ | Ring or circulating structure |
| Meteor | $0.45$ | $0.85$ | Elongated moving group |

*The plotted snapshots show that changes to local interaction parameters can alter global organization. They are examples, not guarantees independent of all other settings.*

### Stigmergy, combined models, and design limits

#### Definitions

> **Stigmergy**: Indirect coordination through modifications left in a shared environment.

Boids use direct local neighbor information; stigmergy uses environmental traces. Continuum fields can provide spatial guidance while Boids rules provide local group coordination. The combined-model fish visual illustrates these complementary roles.

![Stigmergy, combined models, and design limits: fields and flocking combined](../../diagrams/CSC3044S-AI%20Systems/06_Agent_Architectures_II/fields_and_flocking_combined.svg)

*Field guidance and local flocking can provide complementary movement constraints.*

The central engineering problem is choosing local rules, number of layers, neighborhood parameters, and environmental interactions so that the desired collective task is actually solved. Attractive motion alone is not proof of useful problem solving.
