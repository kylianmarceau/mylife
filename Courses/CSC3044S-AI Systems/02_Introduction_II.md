---
tags:
  - ai-systems
---

# Introduction II: Reactive, Deliberative, and Learning Agents

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3044S Artificial Intelligence: AI Systems  
> **Source**: [2026-CSC3044S-Lecture 2-Introduction (II) - Copy.pdf](../../Sources/CSC3044S%20-%20AI%20Systems/2026-CSC3044S-Lecture%202-Introduction%20%28II%29%20-%20Copy.pdf), Geoff Nitschke, slides 1-55  
> **Generated**: 2026-10-01  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Rationality and control styles|Rationality and control styles]]
  - [[#Reactive stimulus-response architectures|Reactive stimulus-response architectures]]
  - [[#Deliberation and representation|Deliberation and representation]]
  - [[#Learning architectures|Learning architectures]]
  - [[#Braitenberg vehicles and vacuum robots|Braitenberg vehicles and vacuum robots]]
  - [[#Computer-use agents and OSWorld|Computer-use agents and OSWorld]]
  - [[#Generative AI, assistants, and agentic execution|Generative AI, assistants, and agentic execution]]

---

## Core Content

### Rationality and control styles

#### Definitions

> **Reactive agent**: An agent tightly coupling sensed information to action, with little or no explicit planning.

> **Deliberative agent**: An agent using a world representation and reasoning or planning to select actions.

> **Learning agent**: An agent whose behavior improves or changes using experience or data.

Rational agents aim to maximize expected utility. Reactive, deliberative, and learning describe how behavior is produced; none alone guarantees rationality.

### Reactive stimulus-response architectures

#### Definitions

> **Condition-action rule**: A rule selecting an action when a specified condition holds.

> **Simple reflex agent**: A controller using current percepts without a stored world model.

A simple reactive policy maps sensed states $S$ to available actions $A$:

$$
\operatorname{action}:S\to A.
$$

The heater example is:

$$
\operatorname{action}(T)=
\begin{cases}
\mathrm{on}, & T<T_{\mathrm{target}},\\
\mathrm{off}, & T\ge T_{\mathrm{target}}.
\end{cases}
$$

Here $T$ is temperature and $T_{\mathrm{target}}$ the required temperature. The simple-reflex version has no memory or explicit goal reasoning; the desired temperature is encoded in the controller.

![Reactive stimulus-response architectures: simple reflex controller](../../diagrams/CSC3044S-AI%20Systems/02_Introduction_II/simple_reflex_controller.svg)

*A simple-reflex architecture chooses an action from current sensed conditions and rules.*

> [!warning] <span style="color: #ffc778">Parallel behaviours still need coordination</span>
> Parallel sense-act modules can identify objects, monitor changes, explore, wander, and avoid objects. They need a way to combine or prioritize outputs; concurrent computation does not mean all incompatible motor commands can be executed together.  

![Reactive stimulus-response architectures: parallel sense act behaviours](../../diagrams/CSC3044S-AI%20Systems/02_Introduction_II/parallel_sense_act_behaviours.svg)

*The example sense-act controller has concurrent behavior modules feeding action control.*

| Benefit | Limitation |
|---|---|
| Fast response | No explicit long-term planning |
| Simple modules | Handcrafted rules require tuning |
| Works through continual environmental feedback | Task changes can require redesign |
| Can avoid a complex symbolic model | Hidden state and ambiguous observations can cause poor actions |

The absence of memory applies to the simplest controller. Model-based reflex designs can retain internal state while still selecting actions reactively.

### Deliberation and representation

#### Definitions

> **World model**: An internal representation of the environment and how actions affect it.

> **Plan**: A course of action intended to achieve a goal.

> **Transduction problem**: Converting observations into representations suitable for reasoning.

> **Representation problem**: Choosing how to encode knowledge, tasks, and data for an agent.

A deliberative controller follows these steps:

1. Receive percepts.
2. Update the internal account of the current world.
3. Predict the effects of candidate actions.
4. Compare those effects with goals.
5. Select and execute an action or plan.
6. Observe again and revise if needed.

![Deliberation and representation: deliberative world model](../../diagrams/CSC3044S-AI%20Systems/02_Introduction_II/deliberative_world_model.svg)

*A deliberative architecture combines observations, internal state, transition knowledge, and goals.*

Classical examples include game-search algorithms and rule-based planning. A search tree branches over candidate moves and responses; look-ahead increases the information used but also the amount of computation.

| Representation issue | What must be encoded? | Example |
|---|---|---|
| Knowledge | Facts, rules, causality, time | Rain affects road conditions |
| Problem | States, goals, actions, constraints | Legal chess moves and winning conditions |
| Data | Raw text, images, audio as usable structures | A camera image represented as features or vectors |

Rapidly changing environments can invalidate a symbolic model before planning finishes. Large search spaces and difficult representations limit scalability. These are challenges for particular designs, rather than a proof that all deliberative systems fail in real-world settings.

### Learning architectures

#### Definitions

> **Performance element**: The component that selects the agent's external actions.

> **Critic**: A component evaluating behavior using a performance standard.

> **Learning element**: A component modifying the performance element using feedback.

> **Problem generator**: A component proposing exploratory actions that can yield useful experience.

![Learning architectures: learning agent components](../../diagrams/CSC3044S-AI%20Systems/02_Introduction_II/learning_agent_components.svg)

*The critic evaluates, the learning element modifies control, and the problem generator proposes exploration.*

A learning controller can be trained from labeled examples or through reinforcement learning. In RL, the environment supplies rewards after actions; the agent learns a policy favoring useful future outcomes.

| Question | Reactive fixed rules | Deliberative fixed model | Learning design |
|---|---|---|---|
| What selects action? | Immediate rule match | Reasoning or planning | Learned policy or learned reasoning components |
| Is look-ahead required? | No | Usually | Depends on design |
| Can behavior change with experience? | Only if an adaptation mechanism is added | Only if an adaptation mechanism is added | Yes, through the learning mechanism |
| Main challenge | Tuning and task specificity | Representation and compute | Data, feedback, and generalization |

### Braitenberg vehicles and vacuum robots

#### Definitions

> **Braitenberg vehicle**: A simple vehicle connecting sensors to motors so that apparently purposeful behavior follows from the wiring.

With excitatory connections, more light causes the connected wheel to turn faster.

| Vehicle | Wiring | Response to brighter light on one side |
|---|---|---|
| 2a: avoid light | Same-side sensor to motor | Wheel on bright side speeds up; vehicle turns away |
| 2b: approach light | Crossed sensor to motor | Opposite wheel speeds up; vehicle turns toward light |

![Braitenberg vehicles and vacuum robots: braitenberg vehicle wiring](../../diagrams/CSC3044S-AI%20Systems/02_Introduction_II/braitenberg_vehicle_wiring.svg)

*Same-side excitatory wiring turns away from a light; crossed wiring turns toward it.*

These vehicles are reactive. “Approach” and “avoid” describe observable behavior; they do not establish that the controller represents a goal or learns.

Vacuum robots illustrate sensing and action in a real room: infrared sensing, bump detection, and cliff sensing support obstacle handling; wheels and brushes/suction perform movement and cleaning. Some designs add maps and planning. A brand name alone is insufficient to classify every implementation.

### Computer-use agents and OSWorld

#### Definitions

> **Computer-use agent**: An agent acting through a computer's graphical or operating-system interface.

> **Execution-based evaluation**: Checking the resulting system state after actions rather than just judging the generated answer.

AI-enhanced operating systems can integrate assistants, recognition, or optimization. An assistant accessible inside an OS is not equivalent to an OS wholly controlled by AI. Examples in the lecture include Braina, Copilot, Gravity/Invisibility, Siri, and Alexa as interface/application illustrations.

OSWorld's original benchmark contains 369 tasks covering real apps, operating-system operations, and workflows across apps. It supplies task setup and evaluation mechanisms. [Original OSWorld paper](https://arxiv.org/abs/2404.07972).

![Computer-use agents and OSWorld: computer use evaluation loop](../../diagrams/CSC3044S-AI%20Systems/02_Introduction_II/computer_use_evaluation_loop.svg)

*OSWorld sets up a task, lets an agent interact with real applications, and checks the resulting state.*

Examples include updating a bookkeeping spreadsheet using transaction records and fixing a game so the snake can eat its food. The important distinction is a verifiable resulting state, rather than a statement that the task was completed.

Leaderboard screenshots are historical examples. Success rates depend on the tested model, harness, settings, and task version.

### Generative AI, assistants, and agentic execution

#### Definitions

> **Generative AI**: AI that generates content such as text, images, audio, video, or code.

> **Large language model (LLM)**: A model trained to process and generate language using patterns learned from data.

> **Harness**: Software around the model that manages tools, context, execution, and permissions.

> **Autonomy**: The degree of independent choice an agent has in carrying out a task.

| Aspect | Generative interaction | Prompt-driven assistant | Agentic execution |
|---|---|---|---|
| Typical task | Produce content | Carry out a requested function | Work through a multi-step goal |
| Example | Space Opera Theater artwork | Produce a comparison table | Investigate, act, inspect outcomes, revise |
| Next step | Often ends with content | Usually constrained by request | Selected inside an execution loop |
| Tools | Optional | May be available | Usually important for acting |
| Persistence | Product-dependent | Product-dependent | Often carries state across steps |

The course contrasts limited assistants with agents having memory, tools, learning, and repeated interactions. Treat these as design features to inspect, rather than universal guarantees attached to product names. Remembering context is not automatically weight learning; not every agent retrains during use.

A booking assistant receives a reservation time, party size, and dietary/seating preferences. Its role prompt specifies a friendly, professional, concise voice and conversational pacing. A call can follow a scripted flow, or a broader agent can choose restaurants and revise the search when requests fail.

An autonomous vehicle maps traffic, weather, obstacles, and lighting observations to motor actions. The booking app that submits a ride request has a narrower role. Generating the app's code with AI does not itself make the app an autonomous agent.
