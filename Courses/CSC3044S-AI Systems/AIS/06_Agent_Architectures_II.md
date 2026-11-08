---
tags:
  - ai-systems
---

# Agent Architectures II

**Subject**: CSC3044S AI Systems
**Source**: `2026-CSC3044S-Lecture 6-Agent Architectures (II) - Copy (1).pdf`, Geoff Nitschke, pages 1-49
**Generated**: 2026-11-08

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Agent Architecture Taxonomy And Examples|Agent Architecture Taxonomy And Examples]]
  - [[#BDI And The LLM Agent Mapping|BDI And The LLM Agent Mapping]]
  - [[#Emergent Behaviour|Emergent Behaviour]]
  - [[#Emergence In Deep Learning And LLMs|Emergence In Deep Learning And LLMs]]
  - [[#LLM Hallucinations|LLM Hallucinations]]
  - [[#Reactive Agents Recap|Reactive Agents Recap]]
  - [[#Brooks Thesis And Situated Intelligence|Brooks Thesis And Situated Intelligence]]
  - [[#Subsumption Architecture Structure|Subsumption Architecture Structure]]
  - [[#Light Avoiding Robot And Maze Navigation|Light Avoiding Robot And Maze Navigation]]
  - [[#Subsumption Benefits And Limits|Subsumption Benefits And Limits]]
  - [[#Multi-Agent Reactive Models And Continuum Crowds|Multi-Agent Reactive Models And Continuum Crowds]]
  - [[#Boids Flocking Model|Boids Flocking Model]]
  - [[#Problems With Reactive Architectures|Problems With Reactive Architectures]]
  - [[#Types Of Architectures Compared|Types Of Architectures Compared]]

---

## Core Content

### Agent Architecture Taxonomy And Examples

#### Definitions

> **Agent Architecture**: The internal organisation of an agent: how it turns perceptions into actions.

> **Reactive Agent**: An agent that maps sensor data directly to actions, deciding from current environmental stimuli rather than memory or prediction.

> **Deliberative Agent**: An agent that decides by reasoning and planning over an internal world model used to predict future outcomes.

> **Hybrid Agent**: An agent that combines reactive, deliberative and cognitive elements.

> **Neural (Connectionist) Agent**: An agent whose decision-making is implemented by artificial neural networks / deep learning.

> **Multi-Agent System (MAS)**: A system of many interacting agents, where system-level behaviour arises from their interactions.

Agent architectures branch into five families. Reactive, deliberative, hybrid, multi-agent and neural (connectionist) agents can all be treated as **rational** agents, since each tries to act well given what it perceives.

![Agent architecture taxonomy](../../../diagrams/CSC3044S-AI%20Systems/AIS/06_Agent_Architectures_II/architecture_taxonomy.svg)
*The five architecture families branch from one root, and all sit inside the rational-agent boundary.*

| Family | Example Architectures |
|---|---|
| Reactive | *Subsumption*, *Boids*, *Continuum crowds*, *Stigmergy* |
| Deliberative (symbolic AI) | *Belief-Desire-Intention (BDI)* |
| Cognitive (neural AI) | AASMO, Soar, ACT-R, Brahms, LIDA, PreAct, Cougaar, PRODIGY, FORR |
| Hybrid | 3T, AuRA, Brahms, GAIuS, GRL, ICARUS, InteRRaP, TinyCog, *TouringMachines* |
| Open question | Where do LLM agents such as Claude, Gemini and DeepSeek fit? |

Brahms appears under both cognitive and hybrid, which shows that the categories overlap.

### BDI And The LLM Agent Mapping

#### Definitions

> **Belief-Desire-Intention (BDI) Architecture**: A deliberative architecture (Rao & Georgeff, 1991) where an agent is described by its beliefs (world model), desires (goals) and intentions (committed plans).

> **Agent-Oriented Programming (AOP)**: Shoham's (1990) programming paradigm where agents are programmed in terms of mental-state notions such as beliefs and commitments.

> **Context Window**: The text an LLM can attend to in one inference call, including the prompt, retrieved memories and tool outputs.

> **Chain-of-Thought**: Intermediate reasoning steps an LLM writes out before giving an answer, acting as its current plan.

BDI and AOP are the two deliberative/hybrid reference points. A modern LLM agent can be read as a BDI agent, with each mental-state component mapping onto a part of the LLM pipeline.

![BDI to LLM agent mapping](../../../diagrams/CSC3044S-AI%20Systems/AIS/06_Agent_Architectures_II/bdi_llm_mapping.svg)
*Each BDI mental state maps to a component of an LLM agent: beliefs to the context window, memories and tool outputs; desires to the system prompt objective; intentions to the chain-of-thought plan.*

This mapping suggests one answer to the open question in the taxonomy: an LLM agent behaves like a deliberative or hybrid agent built on a connectionist core.

### Emergent Behaviour

#### Definitions

> **Emergent Behaviour (Emergence)**: Global behaviour that arises from interactions between local rules and the environment, so that the whole is more than the sum of its parts.

> **Base Behaviour**: An individual behaviour that is pre-coded into an agent.

> **Observed (Global) Behaviour**: The behaviour of the whole system as seen from outside.

Emergence is important but poorly understood. It appears in behaviour-based, reactive (agent-based) systems and throughout nature.

Natural and artificial examples:

- Fish schooling into a single ball-shaped mass.
- Robot soccer teams.
- Termite mounds.
- Busy city traffic and crowds.
- Biological neural networks.

The defining relationship between the two levels:

1. Individual (base) behaviours are pre-coded.
2. Observed (global) behaviours are emergent.
3. There is no one-to-one mapping between the two.
4. When observed behaviour "exceeds" programmed behaviour, the system shows emergence.

The open research question is which kinds of individual (rule, behaviour) interactions produce which kinds of global behaviour.

### Emergence In Deep Learning And LLMs

#### Definitions

> **Artificial Neural Network (ANN)**: A network of connected artificial neurons with weighted connections and activation functions, trained from data.

> **Generalisation**: Producing correct outputs for inputs not seen during training.

> **Universal Function Approximation**: The property that a sufficiently large ANN can approximate any continuous function to arbitrary accuracy.

> **Black-Box Model**: A model whose input-output behaviour can be observed but whose internal reasoning cannot be directly read off.

> **All-or-Nothing Emergence**: Emergence measured by a discrete metric: either a problem-solving behaviour appears at some scale or it does not.

In deep learning, emergence is the rule rather than the exception:

- ANN output is emergent (black-box), which is what gives generalisation through universal function approximation.
- Only the ANN structure (connections) and the training algorithm are designed. The learned behaviour is not.

Scaling the parameter count into the billions (connection weights, activation functions) raises the question of whether genuinely new abilities emerge. Task performance does improve with scale. The debate is whether it improves smoothly or appears abruptly in an all-or-nothing way.

Evidence from three benchmarks (performance against number of parameters, log scale):

![Emergence in LLMs with scale](../../../diagrams/CSC3044S-AI%20Systems/AIS/06_Agent_Architectures_II/llm_emergence_curves.svg)
*3-digit addition (GPT-3) stays near $0$ until about $10^{10}$ parameters, then jumps to about $0.8$. MMLU (Massive Multitask Language Understanding) is near chance ($\approx 0.25$) until the largest models (Gopher about $0.6$, GPT-3 about $0.43$). Program synthesis (Google LM) rises slowly to about $3\%$, then sharply to about $13\%$ near $10^{11}$.*

The sharp "knee" in these curves is what gets called emergence in LLMs (Wei et al., 2022; Krakauer et al., 2026). Whether it reflects a real qualitative change or just the choice of metric remains contested.

### LLM Hallucinations

#### Definitions

> **Hallucination**: LLM output that is fluent but unfaithful to the instruction, the supplied context, or logic and facts.

> **Faithfulness Hallucination**: A hallucination where the output is inconsistent with what the user supplied (instruction or context) or with its own reasoning.

> **Instruction Inconsistency**: The output ignores or deviates from the user's instruction.

> **Context Inconsistency**: The output contradicts the context it was given.

> **Logical Inconsistency**: The output's reasoning steps contradict each other.

Hallucinations raise the question of whether they are a bug or a feature. The same generative process that produces errors also produces novel outputs such as generative AI artwork, which can be seen as a "useful hallucination".

Types of faithfulness hallucination, with examples:

| Type | Input | Hallucinated Response | Why It Is Wrong |
|---|---|---|---|
| Instruction inconsistency | "Translate the English question into Spanish: 'What is the capital of France?'" | "The capital of France is Paris." | The model answered the question instead of translating it |
| Context inconsistency | Retrieved text says the Nile originates in the Great Lakes region of central Africa; instruction: summarise it | "The Nile originates from the mountain ranges of central Africa..." | The summary contradicts the retrieved paragraph |
| Logical inconsistency | "Solve $2x + 3 = 11$ step by step." | Step 1: $2x = 8$. Step 2: divide by 2 to get $x = 3$. | Step 1 is right, but $8/2 = 4$, so step 2 contradicts the earlier reasoning |

**Hallucination theory**: a hallucination is a *failed generalisation* from training data (the trained connection weights) to real-world data (previously unseen input). With enough scale, neurons and connection layers interact in unpredictable ways.

A layered CNN illustrates this. A stimulus image passes through convolution, max-pooling and normalisation layers 1-5, then fully connected layers 6-8, to produce the label "orange".

![CNN layers and emergent pathways](../../../diagrams/CSC3044S-AI%20Systems/AIS/06_Agent_Architectures_II/cnn_layer_interactions.svg)
*Top: the CNN pipeline from stimulus to label. Bottom: active units in layers 1-5 branch into a dense web, so the label emerges from many interacting paths and no single path explains it.*

### Reactive Agents Recap

#### Definitions

> **Sensors**: Components that perceive the environment and supply input to the agent.

> **Effectors (Actuators)**: Components through which the agent acts on the environment.

> **Stimulus-Response Behaviour**: A rule that maps a sensed state directly to an action.

Deep and symbolic approaches are complex and opaque, which raises the question of whether there is a simpler approach. Reactive agents are that approach.

Reactive agent structure:

1. Input from the environment arrives at the **sensors**.
2. Sensor data is matched against a set of stimulus-response behaviours: $\text{State}_1 \rightarrow \text{Action}_1$, $\text{State}_2 \rightarrow \text{Action}_2$, ..., $\text{State}_n \rightarrow \text{Action}_n$.
3. The selected actions go to the **effectors**, which act on the environment.

There is no internal world model and no planning step between sensing and acting.

![Reactive agent structure](../../../diagrams/CSC3044S-AI%20Systems/AIS/06_Agent_Architectures_II/reactive_agent.svg)
*Sensors feed a bank of state-to-action rules, which drive the effectors directly.*

### Brooks Thesis And Situated Intelligence

#### Definitions

> **Brooks' Thesis**: The claim that intelligent behaviour can be produced without explicit representations or explicit reasoning, and that intelligence is an emergent property of reactive components.

> **Situated Intelligence**: Intelligence that exists through an agent's interaction with a real environment.

> **Embodied System**: A system with a physical body, such as a robot, that senses and acts in the real world.

> **Disembodied System**: A system with no body acting in the world, such as a theorem prover, expert system or LLM.

Brooks' thesis has three claims:

1. Intelligent behaviour can be generated **without explicit representations** (neural-based or symbolic-based).
2. Intelligent behaviour can be generated **without explicit reasoning**, which is what neural and symbolic AI propose.
3. Intelligence is an **emergent property** of reactive components.

The subsumption view of intelligence follows from this:

- "Real" intelligence is situated in the world, not in disembodied systems like theorem provers, expert systems or LLMs.
- "Intelligent" behaviour arises from the agent's interaction with its environment.
- The subsumption architecture was designed for embodied (robotic) systems.

### Subsumption Architecture Structure

#### Definitions

> **Subsumption Architecture**: Brooks' reactive architecture made of a hierarchy of task-accomplishing behaviours, where each behaviour is a simple rule-like module.

> **Subsumption**: The mechanism by which one behaviour layer overrides (suppresses) the output of another layer.

> **Sensation Stream**: The continuous flow of sensor input into the behaviour layers.

> **Action Stream**: The continuous flow of motor output from the behaviour layers.

Properties of the architecture:

- It is a **hierarchy of task-accomplishing behaviours**.
- Each behaviour encodes a simple rule-like structure.
- **Lower layers** represent more primitive behaviour (e.g. avoiding obstacles).
- Interaction between lower-level behaviours gives rise to higher-level (task-accomplishing) behaviour.

Data flow through a three-layer subsumption controller:

1. The sensation stream is fed **in parallel** to every behaviour (Behaviour 1, 2 and 3).
2. Each behaviour computes its own proposed output.
3. Behaviour 3's output feeds into the output path of Behaviour 2 through a **subsumption** link.
4. The combined Behaviour 2/3 output feeds into Behaviour 1's output path through another subsumption link.
5. The result leaves Behaviour 1's line as the action stream.

![Subsumption architecture data flow](../../../diagrams/CSC3044S-AI%20Systems/AIS/06_Agent_Architectures_II/subsumption_layers.svg)
*All behaviours receive the sensation stream in parallel; subsumption links let higher layers override lower outputs before the action stream.*

So no layer calls another layer. Layers run concurrently, and the subsumption links decide which output actually reaches the actuators.

### Light Avoiding Robot And Maze Navigation

#### Definitions

> **Collision Recovery**: The behaviour where a robot that hits an object backs up and turns about $90^\circ$ in a random direction.

> **Object (Obstacle) Avoidance**: The behaviour where a robot moves forward but turns about $90^\circ$ in a random direction when closer than $5.0\,\text{cm}$ to an obstacle.

> **Explore World**: The behaviour where a robot moves away from its starting point.

> **Light Avoidance**: The behaviour where a robot steers away from light sources.

**Light avoiding robot.** A small physical robot (a LEGO-style platform) runs a three-layer controller:

![Light avoiding robot controller](../../../diagrams/CSC3044S-AI%20Systems/AIS/06_Agent_Architectures_II/light_avoiding_robot.svg)
*Light avoidance (top), object avoidance and collision recovery (bottom) run in parallel; outputs are combined by subsumption, drive the actuators, and movement feeds back into the sensors.*

The control loop:

1. Sensor information is read. It depends on the robot's current position.
2. All three behaviours receive the sensor information in parallel.
3. Light avoidance's output joins object avoidance's output, which then joins collision recovery's output.
4. The combined command drives the actuators.
5. Actuator movement changes the robot's position, which changes the next sensor readings. The loop repeats.

**Maze navigation.** The same structure with different layers produces maze solving. The robot is coded with three simple behaviours that all run in parallel:

1. **Collision recovery**: if the robot collides with an object, it backs up and turns about $90^\circ$ in a random direction.
2. **Object avoidance (move forward)**: move forward, but if closer than $5.0\,\text{cm}$ to an obstacle, turn about $90^\circ$ in a random direction.
3. **Explore world**: move away from the starting point.

![Maze navigation subsumption controller](../../../diagrams/CSC3044S-AI%20Systems/AIS/06_Agent_Architectures_II/maze_navigation_layers.svg)
*Explore world, object avoidance and collision recovery are the only coded layers; maze navigation (dashed) is emergent.*

Nothing in the controller mentions mazes. Maze navigation sits above the stack as an emergent behaviour, not a coded layer.

Why maze navigation is emergent:

- The robot is not aware of walls. It only reacts to distance readings.
- The concepts "wall" and "navigation" are not stored anywhere in the controller.
- The system is just a collection of rules: collision recovery, obstacle avoidance, explore.


![Maze robot behaviours and emergent path](../../../diagrams/CSC3044S-AI%20Systems/AIS/06_Agent_Architectures_II/maze_robot_behaviours.svg)
*The three coded behaviours (top) combine into a curving path that swings away from walls and keeps leaving the start, which reads as purposeful navigation to an observer.*

### Subsumption Benefits And Limits

#### Definitions

> **Modularity**: Each behaviour layer works independently and can be built and tested on its own.

> **Fault Tolerance**: The system keeps working when one component fails.

Benefits and limits side by side:

| Benefits | Limits |
|---|---|
| **Simplicity, modularity**: each layer works independently, so the system is easier to build, debug and expand | **Lacks memory, learning**: without memory the robot cannot learn from experience or store complex data, limiting long-term adaptability |
| **Responsiveness**: sensory input is used without complex processing, so responses to environmental change are quick | **Limited planning**: the reactive nature does not suit tasks needing detailed planning or sequential steps |
| **Scalability**: basic behaviours are added first, then more complex layers on top | **Difficult to adapt to new tasks**: each layer is task-specific, so it is hard to modify for new objectives |
| **Fault tolerance**: if one behaviour fails, other layers still work | **No abstract concepts**: without neural or symbolic processing it cannot handle language or abstract reasoning |

### Multi-Agent Reactive Models And Continuum Crowds

#### Definitions

> **Boids**: Reynolds' (1987) reactive flocking model.

> **Continuum Crowds**: Treuille et al.'s (2006) crowd simulation model where agents move through a discomfort field towards goals.

> **Stigmergy**: Indirect coordination through modifications to a shared environment (Theraulaz & Bonabeau, 1995, distributed building).

> **Discomfort Field ($g$)**: A function over space giving how undesirable each location is.

> **Goal ($G$)**: The geographic region an agent is trying to reach.

> **Maximum Speed ($f$)**: The speed at which an agent moves.

Multi-agent system models produce emergent behaviour from many simple agents. Besides subsumption, the reactive multi-agent models are Boids, continuum crowds and stigmergy.

**Continuum crowds** are used in CGI (games, movies) to simulate crowds, such as pedestrians at a city intersection. The environment is shown as a heat-map of discomfort: red is highest, purple high, orange low, and green lowest (the goal area).

![Continuum crowds discomfort field](../../../diagrams/CSC3044S-AI%20Systems/AIS/06_Agent_Architectures_II/continuum_crowds_field.svg)
*Schematic discomfort field: agents flow out of high-discomfort red and purple cells, around obstacles, to the low-discomfort green goal $G$.*

The four rules each agent follows:

1. Each agent tries to reach a geographic goal $G$.
2. Agents move at the maximum speed possible, $f$.
3. There is a discomfort field $g$. An agent prefers point $x$ to point $x_0$ when
$$
g(x_0) > g(x).
$$
4. Let $P$ be the set of all paths from $x$ to some point in $G$. With $f$, $g$ and $G$ fixed, the agent at $x$ picks the path $p \in P$ minimising path length, time and discomfort:
$$
p^* = \arg\min_{p \in P} C(p), \qquad C(p) = \text{cost from (path length, travel time, discomfort along } p)
$$

In the original paper the cost is a weighted sum $C(p) = \alpha \int_p 1\,ds + \beta \int_p 1\,dt + \gamma \int_p g\,dt$, with weights $\alpha, \beta, \gamma$ trading off length, time and discomfort.

Combining Boids with continuum models gives richer simulations, such as fish schools flocking around obstacles and a predator in an underwater scene.

### Boids Flocking Model

#### Definitions

> **Boid**: A single agent in the Boids model. It reacts only to flock mates in its local neighbourhood.

> **Repulsion (Separation)**: Steering to avoid crowding local flock mates.

> **Orientation (Alignment)**: Steering towards the average heading of local flock mates.

> **Attraction (Cohesion)**: Steering towards the average position of local flock mates.

> **View Angle ($\alpha$)**: The field of view of a boid. The blind region behind it is $360^\circ - \alpha$.

The Boids model (Reynolds, 1987) was built to visualise flocking for computer graphics. Key properties:

- It is a **reactive MAS model**: each agent is a rule-set with **no internal state**.
- Flocking emerges from $N$ local agent interactions.
- The type of emergent flocking can be changed by changing parameter values in the agent rules.

**Three steering rules.** Each rule acts on the flock mates inside the boid's neighbourhood circle:

| Rule | Steering Effect |
|---|---|
| Repulsion | Steer away to avoid local flock mates |
| Orientation | Turn to match the average heading of local flock mates |
| Attraction | Steer towards the average position (centre) of local flock mates |

![Boids steering rules](../../../diagrams/CSC3044S-AI%20Systems/AIS/06_Agent_Architectures_II/boids_steering_rules.svg)
*The focal boid steers away from close mates (repulsion), turns to their average heading (orientation), and moves towards their average position (attraction).*

The lecture's first rule list pairs attraction with "average heading" and orientation with "average position". That is swapped relative to the zone rules below and to the standard Boids definitions. The table above uses the consistent, standard pairing.

**Zone radii.** The rules act in nested zones around the boid with radii
$$
r_c \le r_o \le r_a
$$
where $r_c$ is the repulsion radius (also written $r_r$), $r_o$ the orientation radius and $r_a$ the attraction radius.

| Zone | Region | Rule |
|---|---|---|
| Zone of repulsion | Inside radius $r_c$ | **Rule 1 (Repulsion)**: move away from agents in the circle of radius $r_c$, in the direction opposite to their average direction |
| Zone of orientation | Between $r_o$ and $r_a$ | **Rule 2 (Orientation)**: align with the average direction of agents between $r_o$ and $r_a$ |
| Zone of attraction | Between $r_c$ and $r_a$ | **Rule 3 (Attraction)**: move in the average direction of all agents between $r_c$ and $r_a$ |

![Boids interaction zones](../../../diagrams/CSC3044S-AI%20Systems/AIS/06_Agent_Architectures_II/boids_zones.svg)
*Nested zones around a boid facing up: repulsion innermost ($r_c$), then orientation ($r_o$), then attraction ($r_a$), with a blind wedge of $360^\circ - \alpha$ behind it.*

**Emergent behaviours from parameter choice.** Fixed parameters:

- View angle $\alpha = 270^\circ$.
- Average direction of agents $\theta = 40^\circ$.
- Number of agents $N = 400$.

Varying $r_o$ and $r_a$ produces different collective behaviours:

| Emergent Behaviour | $r_o$ | $r_a$ | Appearance |
|---|---|---|---|
| Swarming | $0.1$ | $0.85$ | Loose, disordered cluster with no common heading |
| Dispersion | $0.15$ | $0.25$ | Agents spread out and scatter |
| Toroidal | $0.25$ | $0.85$ | Agents circle a common empty centre (a milling doughnut) |
| Meteor | $0.45$ | $0.85$ | Tightly aligned group moving in one direction, leaving parallel trails |

![Boids emergent behaviours](../../../diagrams/CSC3044S-AI%20Systems/AIS/06_Agent_Architectures_II/boids_emergent_behaviours.svg)
*The same three rules give swarming, dispersion, toroidal milling or a meteor-like group depending only on $r_o$ and $r_a$.*

As $r_o$ grows with $r_a$ fixed at $0.85$, the behaviour shifts from swarming to toroidal to meteor. A small $r_a$ ($0.25$) gives dispersion, because agents feel too little attraction to stay grouped.

### Problems With Reactive Architectures

Reactive approaches have a general design problem. It is not obvious how to get a desired collective behaviour from $N$ agent behaviours, which makes them impractical for complex task solving.

Open design questions:

| Architecture | Questions |
|---|---|
| Subsumption | How many layers? What rules (behaviours) to encode? What will the emergent behaviour be? |
| Boids | Can Boids solve real-world tasks, or only produce visually interesting motion? |

The mapping from local rules to global behaviour is not one-to-one, so the designer cannot easily work backwards from the desired global behaviour to the rules.

### Types Of Architectures Compared

#### Definitions

> **Cognitive Agent**: An agent that uses ANN/deep-learning (connectionist) models to try to mimic human-like reasoning, learning and decision-making.

| Type | How Decisions Are Made | Internal Model / Memory | Typical Methods | Examples |
|---|---|---|---|---|
| Reactive | Maps sensor data directly to actions | None. Decisions come from environmental stimuli, not memory or prediction | Stimulus-response rules, layered behaviours | Subsumption, Boids, continuum crowds, stigmergy |
| Deliberative | Reasoning and planning | Internal world model used to predict future outcomes | Symbolic AI | BDI |
| Cognitive | Learned ANN/DL models that try to mimic human-like reasoning, learning and decision-making | Implicit, stored in learned weights (black box) | Usually supervised and reinforcement learning | Soar, ACT-R, LIDA |
| Hybrid | Combines reactive, deliberative and cognitive elements | Mixed | Layered combination | 3T, AuRA, InteRRaP, TouringMachines |

The two examinable outcomes for this lecture:

- The difference between reactive, deliberative and hybrid agents.
- The subsumption architecture: what it is, its benefits and its limits.
