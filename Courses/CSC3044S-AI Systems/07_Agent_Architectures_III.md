---
tags:
  - ai-systems
---

# Agent Architectures III: Learned Reactive Controllers and RoboCup Team Behavior

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3044S Artificial Intelligence: AI Systems  
> **Source**: [2026-CSC3044S-Lecture 7-Agent Architectures (III) - Copy (1).pdf](../../Sources/CSC3044S%20-%20AI%20Systems/2026-CSC3044S-Lecture%207-Agent%20Architectures%20%28III%29%20-%20Copy%20%281%29.pdf), Geoff Nitschke, slides 1-42  
> **Generated**: 2026-10-01  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Multi-agent subsumption and bottom-up design|Multi-agent subsumption and bottom-up design]]
  - [[#RoboCup layers and behavior hierarchy|RoboCup layers and behavior hierarchy]]
  - [[#Pass-or-shoot network: perception and outputs|Pass-or-shoot network: perception and outputs]]
  - [[#Data collection, supervision, and backpropagation|Data collection, supervision, and backpropagation]]
  - [[#Testing and interpreting results|Testing and interpreting results]]
  - [[#Extend to dribbling and ball interception|Extend to dribbling and ball interception]]
  - [[#Combine learned behaviors and compare teams|Combine learned behaviors and compare teams]]

---

## Core Content

### Multi-agent subsumption and bottom-up design

#### Definitions

> **Multi-agent system (MAS)**: A system in which several agents interact in a shared environment.

> **Bottom-up control**: Building system behavior from individual competencies and their interactions.

> **Emergent team behavior**: Collective behavior produced by interacting individual controllers rather than an explicit instruction for the entire team trajectory.

> **Subsumption**: Coordination of behavior layers through suppression or overriding of signals.

The design approach is:

1. Train or define individual behaviors.
2. Use bottom-up control to combine those competencies.
3. Let agents interact and evaluate the resulting team behavior.

Applications illustrated include satellite groups, small robots, drone teams, environmental monitoring, and robot soccer. Their common property is interacting autonomous components, rather than a specific model type.

![Multi-agent subsumption and bottom-up design: multi agent shared environment](../../diagrams/CSC3044S-AI%20Systems/07_Agent_Architectures_III/multi_agent_shared_environment.svg)

*Individual reactive competencies influence one another through the shared environment; team behavior is evaluated at that level.*

The architecture landscape includes reactive, deliberative, cognitive, hybrid, and multi-agent designs. A trained neural controller can still select actions reactively at runtime. Learning method and execution architecture are different axes.

### RoboCup layers and behavior hierarchy

#### Definitions

> **Cooperative behavior**: Behavior involving agents working toward compatible goals.

> **Adversarial behavior**: Behavior shaped by opponents pursuing conflicting goals.

> **Interception**: Movement to meet a moving ball.

| Layer | Interaction type | Behavior level | Example |
|---:|---|---|---|
| 1 | Player-ball | Individual | Ball interception |
| 2 | One-to-one players | Multi-agent | Pass or shoot |
| 3 | One-to-many players | Team | Pass or shoot with several players |
| 4 | Team formation | Team | Strategic positioning |
| 5 | Team-to-opponent | Adversarial | Strategic adaptation |

![RoboCup layers and behavior hierarchy: robocup competency tiers](../../diagrams/CSC3044S-AI%20Systems/07_Agent_Architectures_III/robocup_competency_tiers.svg)

*Individual competencies support cooperative and adversarial behavior tiers.*

Individual kick/dribble/intercept competence supports paired pass/intercept behavior. A team of at least three agents, including a goalie, can decide among passing, dribbling, and shooting. Two such teams create an adversarial setting.

The five-layer interaction table and the three-tier behavior diagram describe different levels of detail. They should not be treated as contradictory layer counts.

### Pass-or-shoot network: perception and outputs

#### Definitions

> **Artificial neural network (ANN)**: A network of weighted computational connections trained to map inputs to outputs.

> **Normalized distance**: A distance rescaled relative to a chosen reference.

> **Activation**: A node's output value after computation.

> **Hidden layer**: Processing nodes between input and output nodes.

Agents A and B use learned shooting behavior; they must also learn when to pass or shoot. Agent C, the goalie, uses a learned interception controller.

Agent A's input vector is:

$$
\mathbf{x}=\bigl(\theta_B,d_B,\theta_C,d_C\bigr),
$$

with angle and normalized distance to teammate B and goalie C.

![Pass-or-shoot network: perception and outputs: pass shoot neural network](../../diagrams/CSC3044S-AI%20Systems/07_Agent_Architectures_III/pass_shoot_neural_network.svg)

*The depicted four-input network connects through two hidden nodes to pass and shoot scores.*

Each input connects through the depicted hidden layer to pass and shoot outputs. At each tick, choose the output with highest activation:

$$
a_t=\arg\max_{a\in\{\mathrm{pass},\mathrm{shoot}\}}z_a(\mathbf{x}_t).
$$

The scores are activations, not necessarily calibrated success probabilities. A tie needs an implementation policy; no tie rule is specified.

The geometric training illustration places B at $110^\circ$ and the goalie at $10^\circ$ relative to A's reference direction, with normalized distances $0.39$ and $0.38$.

| Feature | Example value | Meaning |
|---|---:|---|
| $\theta_B$ | $110^\circ$ | Teammate direction |
| $d_B$ | $0.39$ | Teammate normalized distance |
| $\theta_C$ | $10^\circ$ | Goalie direction |
| $d_C$ | $0.38$ | Goalie normalized distance |

*The four-feature geometry separates teammate and goalie direction from distance.*

### Data collection, supervision, and backpropagation

#### Definitions

> **Labeled example**: An input paired with a training target.

> **Backpropagation**: Computing parameter gradients through the network to support weight adaptation.

> **Learning rate**: The step-size factor used in weight updates.

> **Mean squared error (MSE)**: Average squared difference between predicted and target values.

1. Run 5,000 simulations with randomized positions for A, B, and the goalie.
2. A randomly passes or shoots; B tries to intercept.
3. Record the input geometry and the resulting goal outcome.
4. Label a scored goal “good,” $1$; otherwise “bad,” $0$.
5. Train through backpropagation weight adaptation.

There are 915 positive and 4,085 negative examples. An illustrated record is:

$$
(110,0.39,10,0.38,0).
$$

The final value is an outcome label, not a pass/shoot action index. The displayed tuple does not state which action was attempted. A complete training implementation must define how outcome feedback is associated with each output; the slide does not provide that target-construction detail.

Training uses learning rate $\eta=10^{-6}$ and reports MSE $0.0598$.

For an illustrative scalar-target dataset:

$$
L=\frac{1}{N}\sum_{i=1}^N(\hat y_i-y_i)^2,\qquad
\mathbf{w}\leftarrow\mathbf{w}-\eta\nabla_{\mathbf{w}}L.
$$

For multi-output targets, specify averaging over outputs as well. These formulas explain the stated training method; the exact loss aggregation is not given in the source.

### Testing and interpreting results

Test using 2,000 simulations with B and the goalie randomized within A's angle range $[-60^\circ,30^\circ]$. A receives the same four features and selects the largest output activation.

| Outcome | Pass | Shoot | Total |
|---|---:|---:|---:|
| Good | $31.4\%$ | $52.1\%$ | $40.9\%$ |
| Bad | $68.6\%$ | $47.9\%$ | $59.1\%$ |

*These are reported outcome rates, not a confusion matrix for action classification. Total success depends on how often each action is selected.*

The response plot varies opponent direction while displaying pass and shoot outputs, with markers for teammate and goal direction.

| Approximate opponent direction | Pass activation | Shoot activation | Largest-output action |
|---:|---:|---:|---|
| $-53^\circ$, near teammate marker | $0.42$ | $1.00$ | Shoot |
| $-40^\circ$ | $0.20$ | $0.98$ | Shoot |
| $-20^\circ$ | $0.44$ | $0.32$ | Pass |
| $-6^\circ$, near goal marker | $0.57$ | $0.03$ | Pass |
| $10^\circ$ | $0.71$ | $0.67$ | Pass |
| $30^\circ$ | $0.65$ | $0.83$ | Shoot |

*Approximate values reconstruct the qualitative response curves. As an opponent blocks the goal direction, shoot activation falls and pass becomes preferred; the values are read from the plot rather than raw experimental data.*

> [!important] <span style="color: #b89aff">Training loss and game performance</span>
> Low training MSE is not the same as high game success. Held-out simulations evaluate behavior; training loss evaluates fit to the training targets.  

### Extend to dribbling and ball interception

#### Definitions

> **Discrete action selection**: Choosing one action from a finite set.

> **Continuous control output**: Producing a numerical control value within a range.

The expanded action network keeps four inputs and adds a dribble output. It applies when the ball is stationary or intercepted and teammates/opponents are nearby.

$$
a_t=\arg\max_{a\in\{\mathrm{pass},\mathrm{dribble},\mathrm{shoot}\}}z_a(\mathbf{x}_t).
$$

![Extend to dribbling and ball interception: pass dribble shoot selection](../../diagrams/CSC3044S-AI%20Systems/07_Agent_Architectures_III/pass_dribble_shoot_selection.svg)

*The expanded action network adds dribble while preserving the four input features.*

The intercept ANN takes three inputs:

$$
\mathbf{x}^{\mathrm{intercept}}_t=\bigl(d_t,d_{t-1},\theta_t\bigr),
$$

where $d_t$ and $d_{t-1}$ are current/previous ball distance and $\theta_t$ is current ball angle. Output is a turn angle, with movement then at a preset speed.

![Extend to dribbling and ball interception: ball interception network](../../diagrams/CSC3044S-AI%20Systems/07_Agent_Architectures_III/ball_interception_network.svg)

*Interception uses temporal distance information and produces a turn-angle control value.*

| Controller | Inputs | Output | Relevant condition |
|---|---|---|---|
| Pass/shoot/dribble | Teammate angle/distance; goalie angle/distance | Highest of three scores, shown in $[0,1]$ | Possession or stationary/intercepted ball |
| Intercept | Current distance, previous distance, current angle | Turn angle in illustrated range $[0^\circ,90^\circ]$ | Ball moving toward player or defended goal |

The intercept inputs explicitly include a previous-time-step measurement. This design is not wholly memoryless, despite the broad “reactive architectures lack memory” warning.

Both expanded action selection and interception are tested in 2,000 simulations in the described experiments. No additional numerical team-win rates are supplied.

### Combine learned behaviors and compare teams

1. Observe ball motion, possession, teammate/opponent proximity, and goal threat.
2. Choose the controller appropriate to that situation.
3. Execute the action or turn-angle output.
4. Let all agents repeat their local decisions.
5. Evaluate the resulting passing, interception, formation, and opposition behavior.

![Combine learned behaviors and compare teams: possession and interception loop](../../diagrams/CSC3044S-AI%20Systems/07_Agent_Architectures_III/possession_and_interception_loop.svg)

*Situation-dependent controller selection combines possession and interception skills in the reactive loop.*

| Team configuration | Individual decision behavior |
|---|---|
| Random baseline | If no teammate is closer, move straight to intercept; with possession randomly pass, shoot, or dribble |
| Trained team | Select either the three-input interception ANN or four-input pass/shoot/dribble ANN |
| Trained versus trained | Both teams use the learned controllers |

The demonstration setups let red start with the ball. One compares random red with trained blue; another compares two trained teams. The exported video frames do not provide quantitative results, so no winner or success rate should be inferred from them.

The biggest challenge is **designing desired emergence**. Good local skills do not guarantee good team tactics. Fixed task-specific layers have limited adaptability and planning; offline-trained neural modules do not automatically learn during play.
