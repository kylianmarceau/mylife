---
tags:
  - ai-systems
---

# Agent Architectures III: Multi-Agent Systems And The Subsumption Architecture

**Subject**: CSC3044S AI Systems
**Source**: `2026-CSC3044S-Lecture 7-Agent Architectures (III) - Copy (1).pdf`, Geoff Nitschke, pages 1-42
**Generated**: 2026-11-08

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Agent Architecture Families|Agent Architecture Families]]
  - [[#Multi-Agent Systems And Applications|Multi-Agent Systems And Applications]]
  - [[#The Multi-Agent Subsumption Architecture|The Multi-Agent Subsumption Architecture]]
  - [[#RoboCup Layered Team Behaviour|RoboCup Layered Team Behaviour]]
  - [[#The Pass-Or-Shoot Problem And ANN Design|The Pass-Or-Shoot Problem And ANN Design]]
  - [[#Generating Labelled Training Data|Generating Labelled Training Data]]
  - [[#Training And Testing The Pass-Or-Shoot ANN|Training And Testing The Pass-Or-Shoot ANN]]
  - [[#Cooperative Behaviour With Pass-Or-Shoot And Intercept|Cooperative Behaviour With Pass-Or-Shoot And Intercept]]
  - [[#Adding Dribble And The Intercept ANN|Adding Dribble And The Intercept ANN]]
  - [[#Assembling Team Behaviour From The Layers|Assembling Team Behaviour From The Layers]]
  - [[#Random Versus Trained Teams|Random Versus Trained Teams]]
  - [[#Limitations Of Reactive (Subsumption) Architectures|Limitations Of Reactive (Subsumption) Architectures]]
  - [[#What To Know And Further Reading|What To Know And Further Reading]]

---

## Core Content

### Agent Architecture Families

#### Definitions

> **Agent Architecture**: The internal design of an agent, specifying how perception is turned into action (e.g. by direct reaction, symbolic reasoning, neural processing, or a combination).

> **Reactive Architecture**: An architecture that maps current sensory input directly to actions, without an internal world model or explicit planning.

> **Deliberative (Symbolic-Based) Architecture**: An architecture that reasons over an explicit symbolic representation of the world (e.g. beliefs and goals) to choose actions.

> **Cognitive (Neural-Based) Architecture**: An architecture modelled on cognition, built around (neural or cognitive) processing of perception, memory, and learning.

> **Hybrid Architecture**: An architecture combining reactive and deliberative (and/or cognitive) components, typically in layers.

Agent architectures fall into a few broad families. Each family has well-known example systems:

| Family | Examples |
|---|---|
| **Reactive** | Subsumption, Boids, Continuum (crowds), Stigmergy |
| **Deliberative** (symbolic-based) | Belief-Desire-Intention (BDI) |
| **Cognitive** (neural-based) | AASMO, Soar, ACT-R, Brahms, LIDA, PreAct, Cougaar, PRODIGY, FORR, ... |
| **Hybrid** | 3T, AuRA, Brahms, GAIuS, GRL, ICARUS, InteRRaP, TinyCog, TouringMachines, and LLM-based agents such as Claude, Gemini, DeepSeek, GPT |

Brahms appears under both cognitive and hybrid, since it combines cognitive modelling with other components.

The course map of architectures branches from "Agent Architectures" into five categories, all of which sit inside the umbrella of **rational** agents:

![Agent architecture families](../../../diagrams/CSC3044S-AI%20Systems/AIS/07_Agent_Architectures_III/architecture_families.svg)
*Reactive, deliberative, hybrid, multi-agent and neural-based agents all branch from agent architectures and sit within rational agents; multi-agent systems are the focus here.*

### Multi-Agent Systems And Applications

#### Definitions

> **Multi-Agent System (MAS)**: A system of multiple interacting agents situated in a shared environment, whose combined behaviour solves a task that individual agents could not (easily) solve alone.

> **Swarm Robotics**: A MAS approach where many simple robots coordinate through local interactions to achieve a collective goal.

MAS are used wherever a task is spatially distributed, too large for a single agent, or benefits from redundancy. Application areas include:

| Application | What the agents do |
|---|---|
| Satellite constellations | Multiple small satellites cooperating in orbit (e.g. Earth observation, communications) |
| Medical nanorobots | Swarms of micro-robots operating inside the bloodstream |
| Agricultural swarm robotics (e.g. SAGA) | Drones patrol a field, map infested areas, home in on targets, and attract other agents to remove weeds |
| Search and rescue / environmental monitoring | Networked flying robots covering rough terrain and relaying information |
| Firefighting drone swarms | Many drones coordinating over a wildfire alongside human firefighters |
| Robot soccer (RoboCup) | Teams of physical or simulated robots playing soccer against an opposing team |

### The Multi-Agent Subsumption Architecture

#### Definitions

> **Subsumption Architecture**: A reactive, layered architecture in which each layer implements a behaviour, all layers receive the sensor stream in parallel, and higher layers can *subsume* (override/suppress) the outputs of lower layers.

> **Subsumption**: The mechanism by which a higher-level behaviour overrides or suppresses the output of a lower-level behaviour before it reaches the action stream.

> **Bottom-Up Control**: Building control from the simplest behaviours upwards, with each new layer adding competence on top of already-working lower layers.

> **Emergent Behaviour**: Collective (e.g. team) behaviour that arises from interactions among individual agents and is not explicitly programmed into any single agent.

Designing MAS behaviour with a multi-agent subsumption architecture follows three stages:

1. **Agents learn individual behaviours** first (each agent becomes competent on its own).
2. **Bottom-up control** is applied: layers are stacked from simple to complex.
3. **Individual agents interact**, and **team behaviours emerge** from those interactions.

The subsumption structure has three behaviour layers fed by one sensation stream:

![Multi-agent subsumption architecture](../../../diagrams/CSC3044S-AI%20Systems/AIS/07_Agent_Architectures_III/subsumption_layers.svg)
*Every layer sees the sensation stream; Behaviour 3 subsumes Behaviour 2, which subsumes Behaviour 1 before the action stream. In the multi-agent version each layer is a different agent.*

The flow is:

1. The **sensation stream** is fed in parallel to every behaviour layer.
2. Each layer computes its own proposed action.
3. Behaviour 3's output subsumes Behaviour 2's output.
4. That combined output subsumes Behaviour 1's output.
5. Whatever survives is emitted as the **action stream**.

In the multi-agent version, each layer can correspond to a different agent: Agent 1 at the bottom layer, Agent 2 in the middle, Agent 3 at the top. The agents still share the same sensation stream (the shared environment), and the "higher" agents' behaviours can subsume lower ones, so the action stream reflects the whole group. Robot soccer is the motivating application.

### RoboCup Layered Team Behaviour

#### Definitions

> **RoboCup**: An international robot soccer competition and research testbed, with leagues for humanoid robots, wheeled robots, 3D simulation, and 2D simulation.

> **Individual Behaviour**: A behaviour involving one agent and the ball (e.g. kick, dribble, intercept).

> **Cooperative Behaviour**: A behaviour involving two (or more) teammates working together (e.g. pass and intercept).

> **Team Behaviour**: Behaviour of three or more agents (teammates plus goalie) deciding collectively (e.g. pass, dribble or shoot).

> **Adversarial Behaviour**: Behaviour of a team acting against an opposing team (two teams of three or more agents).

RoboCup team behaviour can be decomposed into five layers, from the simplest player-ball interactions up to adapting to an opponent:

| Layer | Type | Behaviour | Example |
|---|---|---|---|
| 1 | Player-ball | Individual | Ball interception |
| 2 | 1-to-1 player | Multi-agent | Pass or shoot? |
| 3 | 1-to-N player | Team | Pass or shoot? |
| 4 | Team formation | Team | Strategic positioning |
| 5 | Team-to-opponent | Adversarial | Strategic adaptation |

For the game-playing example, these collapse into a three-level subsumption hierarchy. Lower layers feed upward into higher ones:

![Game-playing behaviour layers](../../../diagrams/CSC3044S-AI%20Systems/AIS/07_Agent_Architectures_III/game_playing_behaviours.svg)
*Individual skills (kick, dribble, intercept) feed cooperative skills (pass, intercept), which feed adversarial team play (pass, shoot).*

- **Individual** (1 agent): kick and dribble are "hard-wired" rules.
- **Cooperative** (2 agents): intercept and pass.
- **Adversarial** (2 teams of $\geq 3$ agents): pass, dribble or shoot?

A separate **team** level (between cooperative and adversarial) covers $\geq 3$ agents on one side (teammates plus goalie), where the decision is again pass, dribble or shoot.

### The Pass-Or-Shoot Problem And ANN Design

#### Definitions

> **Artificial Neural Network (ANN)**: A network of weighted, connected nodes (input, hidden, output) that learns a mapping from inputs to outputs by adjusting its weights.

> **ANN Topology**: The structure of an ANN, i.e. its number of input, hidden and output nodes and how they are connected.

The scenario has three agents near the opponent's goal:

| Agent | Role | Behaviour used |
|---|---|---|
| A | Attacker with the ball | Uses a learned shoot behaviour; **must learn pass-or-shoot** |
| B | Teammate of A | Uses a learned shoot behaviour (and receives passes) |
| C | Goalie (opponent) | Uses a learned intercept behaviour |

Two outcomes are possible for A: shoot directly at goal (risking C intercepting), or pass to B who then shoots. Choosing between them is a learned team behaviour.

![Pass-or-shoot scenario](../../../diagrams/CSC3044S-AI%20Systems/AIS/07_Agent_Architectures_III/pass_or_shoot_scenario.svg)
*Agent A must decide whether to shoot past goalie C or pass to teammate B, who then shoots.*

Agent A's **pass-or-shoot ANN** has the following topology:

![Pass-or-shoot ANN](../../../diagrams/CSC3044S-AI%20Systems/AIS/07_Agent_Architectures_III/pass_or_shoot_ann.svg)
*A fully connected 4-2-2 network: four geometric inputs, two hidden nodes, and Pass and Shoot outputs.*

All four inputs are measured from Agent A's position:

- **Angle to B / distance to B**: the direction and length of the line from A to teammate B.
- **Angle to goalie / distance to goalie**: the direction and length of the line from A to the goalie.

### Generating Labelled Training Data

#### Definitions

> **Training Example**: One input vector (here, the four geometric features) paired with a target label.

> **Labelled Data**: Training examples whose target outputs are known, enabling supervised learning.

> **Normalisation**: Rescaling a feature (here, distances) to a fixed range such as $[0,1]$ so features are comparable.

Each training example is the input vector

$$
\mathbf{x} = \left(\theta_B,\ d_B,\ \theta_G,\ d_G\right)
$$

where $\theta_B$ is the angle to B, $d_B$ the (normalised) distance to B, $\theta_G$ the angle to the goalie, and $d_G$ the (normalised) distance to the goalie.

Labelled data is generated by simulation:

1. Run **5000 simulations**, with Agent A, Agent B and the goalie starting in random positions.
2. In each simulation, Agent A **randomly shoots or passes** (if A passes, Agent B intercepts the ball and shoots).
3. Record A's four inputs at the moment of the decision.
4. If a **goal is scored**, label the example "good" ($1$).
5. If **no goal** is scored, label it "bad" ($0$).

This produced **915 positive** examples (label $1$) and **4085 negative** examples (label $0$), so only

$$
\frac{915}{5000} \approx 18.3\%
$$

of random decisions scored.

Example labelled training example:

$$
\{\,110,\ 0.39,\ 10,\ 0.38,\ 0\,\}
$$

| Field | Value | Meaning |
|---|---|---|
| $\theta_B$ | $110^\circ$ | Angle to B |
| $d_B$ | $0.39$ | Distance to B (normalised) |
| $\theta_G$ | $10^\circ$ | Angle to goalie |
| $d_G$ | $0.38$ | Distance to goalie (normalised) |
| Label | $0$ | No goal ("bad") |

![Pass-or-shoot input geometry](../../../diagrams/CSC3044S-AI%20Systems/AIS/07_Agent_Architectures_III/input_geometry.svg)
*The four inputs are the angle and distance from Agent A to teammate B and to the goalie; with a goal/no-goal label they form one training example.*

### Training And Testing The Pass-Or-Shoot ANN

#### Definitions

> **Backpropagation**: A supervised learning algorithm that propagates the output error backwards through the network and adjusts each weight in the direction that reduces the error.

> **Learning Rate ($\eta$)**: The step size used when updating weights during training.

> **Mean Squared Error (MSE)**: The average squared difference between target and network outputs over the training set.

> **Winner-Takes-All Action Selection**: Choosing the action whose output node has the highest activation.

Training parameters:

| Parameter | Value |
|---|---|
| Training examples | $5000$ |
| Weight adaptation | Backpropagation |
| Learning rate | $\eta = 10^{-6}$ |
| Result | $\text{MSE} = 0.0598$ |

The error being minimised is

$$
\text{MSE} = \frac{1}{N}\sum_{i=1}^{N}\left(y_i - \hat{y}_i\right)^2
$$

with $N$ training examples, target $y_i$ and network output $\hat{y}_i$.

Testing procedure:

1. Run **2000 test simulations**.
2. Place the goalie and Agent B in random positions within the angle range $[-60^\circ, 30^\circ]$ relative to Agent A.
3. Each tick, feed A's ANN its 4 inputs.
4. Select the action of the output node with **highest activation**: output node 1 = Pass, output node 2 = Shoot.

![Test angle range](../../../diagrams/CSC3044S-AI%20Systems/AIS/07_Agent_Architectures_III/test_angle_range.svg)
*Test placements: the goalie and Agent B are randomly positioned within -60 to +30 degrees of Agent A.*

Test results (percentage of decisions of each kind that were good or bad):

| Outcome | Pass | Shoot | Total |
|---|---|---|---|
| Good | $31.4\%$ | $52.1\%$ | $40.9\%$ |
| Bad | $68.6\%$ | $47.9\%$ | $59.1\%$ |

So the trained network scored on $40.9\%$ of decisions overall, more than double the $\approx 18.3\%$ success of random decisions in the training data. Shooting was the more successful choice when selected.

The network's outputs as a function of the **direction to the opponent player** (goalie), swept from $-60^\circ$ to $30^\circ$, show what it learned:

![Pass and shoot output vs opponent direction](../../../diagrams/CSC3044S-AI%20Systems/AIS/07_Agent_Architectures_III/output_vs_direction.svg)
*Shoot output collapses when the opponent lies in the direction of the goal, where pass dominates; shoot is near 1 when the opponent is off the shooting line (e.g. towards the teammate).*

| Opponent direction | Shoot output | Pass output | Preferred action |
|---|---|---|---|
| Near the direction to teammate ($\approx -53^\circ$) and from $-60^\circ$ to $\approx -35^\circ$ | $\approx 1.0$ | Low (dips to $\approx 0.2$ at $\approx -42^\circ$) | Shoot (goalie is away from the goal line of fire, blocking the pass instead) |
| Around $-20^\circ$ | Falling sharply ($\approx 0.4$) | Rising ($\approx 0.4$) | Crossover point |
| Near the direction to goal ($\approx -6^\circ$ to $0^\circ$) | Minimum ($\approx 0.03$) | $\approx 0.57$-$0.6$ | Pass (goalie blocks the shot) |
| $\approx 10^\circ$ to $30^\circ$ | Rises back to $\approx 0.8$ | Peaks $\approx 0.71$ at $\approx 11^\circ$, then $\approx 0.65$ | Pass then shoot again as the goalie moves off the shooting line |

In short: when the goalie stands between A and the goal, the ANN passes; when the goalie is off the shooting line (e.g. covering the teammate), it shoots.

### Cooperative Behaviour With Pass-Or-Shoot And Intercept

#### Definitions

> **Intercept ANN**: A trained 3-input network that outputs the turn angle an agent should take to intercept a moving ball.

Cooperative and adversarial play uses two trained networks, chosen by the state of the ball:

| Condition | Who | Network | Ball state |
|---|---|---|---|
| IF Pass OR Shoot | Agent A | Pass-or-shoot ANN (trained, 4 inputs) | Stationary |
| IF Intercept | Agent B, goalie | Intercept ANN (trained, 3 inputs) | Moving |

The intercept ANN topology:

![Intercept ANN](../../../diagrams/CSC3044S-AI%20Systems/AIS/07_Agent_Architectures_III/intercept_ann.svg)
*A 3-4-1 network: distance to ball at t and t-1 plus angle to ball at t map to a turn angle in [0, 90] degrees; the agent then moves at fixed speed.*

Using the distance at both $t$ and $t-1$ lets the network infer the ball's motion relative to the agent.

### Adding Dribble And The Intercept ANN

#### Definitions

> **Dribble**: Moving with the ball under control rather than releasing it by passing or shooting.

On a full pitch, an agent with the ball has three options: shoot, pass or dribble. For example, a player in its own half might dribble forward, pass up the wing, have the ball passed again near the opponent's box, and finally have a teammate shoot.

![Shoot, pass or dribble on the pitch](../../../diagrams/CSC3044S-AI%20Systems/AIS/07_Agent_Architectures_III/pitch_shoot_pass_dribble.svg)
*A dribbles then passes to B, B passes to D, D passes to G, and G shoots; each question mark is an alternative choice the ball carrier could have made.*

Agent A's ANN is extended by adding a third output:

![Adding a dribble output](../../../diagrams/CSC3044S-AI%20Systems/AIS/07_Agent_Architectures_III/pass_shoot_dribble_ann.svg)
*The 4-2-2 pass-or-shoot network becomes a 4-2-3 pass-shoot-dribble network; the inputs are unchanged.*

When each network is used:

| Network | Activation condition | Output |
|---|---|---|
| Pass, shoot or dribble ANN | IF the ball is stationary or intercepted, AND teammates and opponents are nearby | Pass, Dribble or Shoot |
| Intercept ANN (Agent B, goalie) | IF the ball is moving towards my team's goal or towards me | Angle to turn (agent then moves at a fixed speed) |

More training data is collected for both networks:

| Network | Output labels | Range |
|---|---|---|
| ANN1 (pass-shoot-dribble) | $\{\text{Shoot},\ \text{Pass to B},\ \text{Dribble}\}$ | $[0, 1]$ |
| ANN2 (intercept) | $\{\text{Intercept}\}$ as a turn angle | $[0.0, 90.0]$ |

ANN1's training input is the same vector $(\theta_B, d_B, \theta_G, d_G)$, e.g. angle to B $=110^\circ$, angle to goalie $=10^\circ$.

Testing the extended networks:

1. **Agent A (pass, shoot, dribble)**: 2000 test simulations, goalie and Agent B in random positions within $[-60^\circ, 30^\circ]$ of A. A's ANN receives 4 inputs; the highest-activation node selects the action: node 1 = Pass, node 2 = Dribble, node 3 = Shoot.
2. **Agent B and goalie (intercept)**: 2000 test simulations. The ANN receives 3 inputs and outputs a turn; movement speed is preset. The output node's activation selects the turn angle in $[0^\circ, 90^\circ]$.

### Assembling Team Behaviour From The Layers

Team behaviour is obtained by having each agent use **whichever trained ANN suits the current game state**. Example triggers:

- If I have the ball, and a teammate and an opponent are in close proximity: use the pass-shoot-dribble ANN.
- If an opponent has the ball, with another opponent in close proximity: use the intercept ANN.
- If the ball is moving towards my team's goal: use the intercept ANN.

Putting the layers together gives the full subsumption hierarchy for team play:

![Team play subsumption layers with ANNs](../../../diagrams/CSC3044S-AI%20Systems/AIS/07_Agent_Architectures_III/team_play_layers.svg)
*The individual layer uses the Pass-Shoot-Dribble ANN; the cooperative (1 team) and adversarial (2 teams) layers use both the Pass-Shoot-Dribble and Intercept ANNs.*

Each level builds on the one below: individual skills feed cooperative skills, which feed adversarial play. No agent is programmed with "team strategy"; team play emerges from agents switching between learned behaviours.

### Random Versus Trained Teams

#### Definitions

> **Random (Fixed-Rule) Team**: A baseline team whose agents use fixed hand-written rules, choosing among ball actions at random.

> **Trained Team**: A team whose agents select actions using the trained intercept and pass-shoot-dribble ANNs.

Two experiments compare team designs (red always starts with the ball):

| Team | Agent A, B behaviour |
|---|---|
| Random team | IF no other teammates are closer, move straight to intercept the ball; IF have ball, randomly shoot, pass or dribble |
| Trained team | Use either the intercept (3-input) ANN or the pass, shoot or dribble (4-input) ANN |

| Match | Red | Blue |
|---|---|---|
| 1 | Random team | Trained team |
| 2 | Trained team | Trained team |

The first match tests whether learned behaviours beat random choices; the second shows play when both sides use the same learned layers.

### Limitations Of Reactive (Subsumption) Architectures

Reactive architectures such as subsumption have four main limitations:

| Limitation | Explanation |
|---|---|
| **Lacks memory, learning** | Without memory, robots cannot learn from experience or store complex data, limiting long-term adaptability. |
| **Limited planning** | The reactive nature is not suited to tasks requiring detailed planning or sequential steps. |
| **Difficult to adapt to new tasks** | Each behaviour layer is task-specific, making it hard to modify for new objectives. |
| **Designing emergent behaviour** | It is very difficult to design agents (behaviours) so that they interact to produce a desired, problem-solving emergent behaviour. |

The **biggest problem** is the last one: designing emergent behaviour. Team play in the RoboCup example emerges from interactions, but there is no systematic way to engineer individual behaviours that guarantee the desired collective outcome.

### What To Know And Further Reading

For the agent-architecture block, be able to:

- Compare reactive vs deliberative vs hybrid agent architectures.
- Give the pros and cons of each.
- Explain how each works, with examples of each.

The next architecture covered is the deliberative **Belief-Desire-Intention (BDI)** agent architecture.

Reading:

| Reference | Topic |
|---|---|
| Russell & Norvig (2021), *Artificial Intelligence: A Modern Approach*, 4th ed., Ch. 2 | Intelligent agents |
| Poole & Mackworth (2023), *Artificial Intelligence: Foundations of Computational Agents*, 3rd ed., Ch. 1 | AI and agents |
| Krakauer et al. (2026), "Large language models and emergence: a complex systems perspective", *Phil. Trans. R. Soc. A* 384(2320) | LLMs and emergence |
| Reynolds (1987), "Flocks, herds and schools: A distributed behavioral model", SIGGRAPH | Boids |
| Treuille et al. (2006), "Continuum crowds", *ACM Transactions on Graphics* 25(3) | Continuum crowds |
| Theraulaz & Bonabeau (1995), "Coordination in Distributed Building", *Science* 269 | Stigmergy |
