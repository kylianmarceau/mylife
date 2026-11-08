---
tags:
  - ai-systems
---

# Agent Architectures IV: BDI Agents

**Subject**: CSC3044S AI Systems  
**Source**: `CSC3044S-Lecture 8-Agent Architectures IV(BDI) - Copy.pdf`, Deshen Moodley, pages 1-18  
**Generated**: 2026-11-08

---

## Contents

- [[#Core Content|Core Content]]
  - [[#The Agent Paradigm|The Agent Paradigm]]
  - [[#The BDI Agent Architecture|The BDI Agent Architecture]]
  - [[#Practical Reasoning And The BDI Cognitive Loop|Practical Reasoning And The BDI Cognitive Loop]]
  - [[#Beliefs, Desires, Intentions And The Sense-Revise-Plan-Act Cycle|Beliefs, Desires, Intentions And The Sense-Revise-Plan-Act Cycle]]
  - [[#Original BDI Control Loop|Original BDI Control Loop]]
  - [[#Abstract BDI Control Loop|Abstract BDI Control Loop]]
  - [[#Implementing BDI Agents|Implementing BDI Agents]]
  - [[#Advantages Of BDI Agents|Advantages Of BDI Agents]]
  - [[#Extending The BDI Architecture|Extending The BDI Architecture]]
  - [[#Sugarcane Grower Simulation Example|Sugarcane Grower Simulation Example]]
  - [[#Probabilistic BDI Agent|Probabilistic BDI Agent]]
  - [[#Dynamic Bayesian Decision Network|Dynamic Bayesian Decision Network]]
  - [[#Probabilistic BDI Control Loop|Probabilistic BDI Control Loop]]
  - [[#Discussion Points|Discussion Points]]
  - [[#References|References]]

---

## Core Content

### The Agent Paradigm

#### Definitions

> **Agent**: An entity situated in a world/environment that perceives it, reasons about what it perceives, and acts on it.

> **Environment (World)**: Everything outside the agent that it observes and acts upon.

The basic agent paradigm is a continuous interaction between agent and environment:

1. **Observe**: signals from the world/environment reach the agent.
2. **Perceive**: the agent turns those observations into percepts.
3. **Reason**: the agent decides what to do.
4. **Act**: the agent performs actions (through several effectors/outputs) that change the environment.

BDI is one particular way of structuring the "reason" step.

![Agent paradigm](../../../diagrams/CSC3044S-AI%20Systems/AIS/08_Agent_Architectures_IV_BDI/agent_paradigm.svg)
*The agent sits inside its environment: it observes, perceives and reasons, then acts back on the environment through several outputs.*

### The BDI Agent Architecture

#### Definitions

> **BDI (Belief-Desire-Intention) Architecture**: An agent architecture introduced in Bratman's practical reasoning system (Bratman et al., 1988), based on the mental attitudes of beliefs, desires and intentions.

> **Beliefs**: What the agent believes about its environment and itself.

> **Desires**: The set of goals the agent wants to achieve.

> **Intentions**: The goals the agent is currently committed to achieving.

A BDI agent represents three key **mental states**:

| Mental State | Meaning |
|---|---|
| Beliefs | What the agent believes about its environment and itself |
| Desires | The set of goals it wants to achieve |
| Intentions | The goals it is currently committed to achieving |

The BDI architecture formed the basis for much of the research on architectures for autonomous agents over the last 30 years.

### Practical Reasoning And The BDI Cognitive Loop

#### Definitions

> **Practical Reasoning**: Reasoning directed towards deciding what to do (action), carried out in two steps: deliberation and means-ends reasoning.

> **Deliberation**: Deciding *what* state of affairs to bring about from the (possibly conflicting) desires of the agent.

> **Means-Ends Reasoning**: Deciding *how* to bring about that state of affairs (i.e. finding a plan).

> **Bounded Rationality**: Selecting a course of action based on limited information and limited computation, rather than exploring every option with complete information.

> **Satisficing**: Choosing an option that is good enough rather than searching for the optimal one (Simon, 1996); the way humans typically take decisions.

Practical reasoning has two steps:

| Step | Question Answered | Output |
|---|---|---|
| 1. Deliberation | *What* do I want to achieve? | A selected goal (intention) from competing desires |
| 2. Means-ends reasoning | *How* do I achieve it? | A plan to achieve the intention |

The **BDI cognitive loop** runs these steps repeatedly:

1. Receive percepts and revise what the agent believes about the world and itself.
2. Deliberate about its goals and current intentions, consider its options, and select a goal to follow — this goal becomes its intention.
3. Focus on the most suitable intentions, find the most suitable plan, and execute it.

Using BDI, a course of action can be selected on **limited information**, in a **bounded rational** way (Bratman et al., 1988).

- Without bounding, a rational agent would explore all the options and expect all information at every time step.
- Bounding mimics how humans take decisions, using **satisficing** (Simon, 1996).

### Beliefs, Desires, Intentions And The Sense-Revise-Plan-Act Cycle

#### Definitions

> **Beliefs (detailed)**: The current state of the environment and the agent itself (the **context**), plus inference rules for reasoning (**knowledge**).

> **Desires (detailed)**: The overall goals or objectives of the agent — what it wants to achieve in the future. They can be inconsistent, unrealistic, and may conflict.

> **Intentions (detailed)**: The current subset of active desires/goals. They must be consistent and achievable in the current context.

The key contrast is between desires and intentions:

| Property | Desires | Intentions |
|---|---|---|
| Scope | All overall goals/objectives | Current active subset of desires |
| Consistency | May be inconsistent or conflicting | Must be consistent |
| Feasibility | May be unrealistic | Must be achievable in the current context |
| Commitment | No commitment | Agent is committed to achieving them |

Beliefs have two parts: the **context** (current state of world and self) and **knowledge** (inference rules used to reason over the context).

The architecture runs a four-stage cycle between observations and actions:

1. **Sense**: observations arrive from the environment.
2. **Revise beliefs**: the new observations update the store of beliefs and goals.
3. **Plan**: the planner uses beliefs and goals to produce a plan.
4. **Act**: the actuators carry out the plan, producing actions in the environment; the effects feed back into what is sensed next.

| Component | Role in the cycle |
|---|---|
| Beliefs / Goals store | Holds the agent's beliefs and goals; updated in "revise beliefs" |
| Planner | Builds a plan from beliefs and goals |
| Actuators | Execute the plan as actions on the environment |

![BDI architecture cycle](../../../diagrams/CSC3044S-AI%20Systems/AIS/08_Agent_Architectures_IV_BDI/bdi_architecture_cycle.svg)
*BDI architecture: observations are sensed, beliefs and goals are revised, the planner builds a plan, and actuators act; the results feed back into the next sensing step.*

### Original BDI Control Loop

#### Definitions

> **Belief Revision Function ($\mathrm{brf}$)**: Updates the current beliefs $B$ given a new percept $\rho$.

> **Options Function ($\mathrm{options}$)**: Generates the agent's desires (options) $D$ from its beliefs and current intentions.

> **Filter Function ($\mathrm{filter}$)**: Selects the intentions $I$ to commit to from beliefs, desires and existing intentions (deliberation).

> **Plan Function ($\mathrm{plan}$)**: Produces a plan $\pi$ that achieves the intentions given the beliefs (means-ends reasoning).

The original BDI agent control loop (Wooldridge, 2000):

```text
Algorithm: BDI agent's control loop (Wooldridge, 2000)
1:  B := B0              // B0 are the initial beliefs
2:  I := I0              // I0 are the initial intentions
3:  while true do
4:      get next percept ρ
5:      B := brf(B, ρ)
6:      D := options(B, I)
7:      I := filter(B, D, I)
8:      π := plan(B, I)
9:      execute(π)
10: end while
```

The same steps as update rules:

$$
B \leftarrow \mathrm{brf}(B, \rho), \quad D \leftarrow \mathrm{options}(B, I), \quad I \leftarrow \mathrm{filter}(B, D, I), \quad \pi \leftarrow \mathrm{plan}(B, I)
$$

How each line maps to practical reasoning:

| Line | Function | Stage |
|---|---|---|
| 4-5 | $\mathrm{brf}(B,\rho)$ | Perception and belief revision |
| 6 | $\mathrm{options}(B,I)$ | Deliberation: generate desires |
| 7 | $\mathrm{filter}(B,D,I)$ | Deliberation: commit to intentions |
| 8 | $\mathrm{plan}(B,I)$ | Means-ends reasoning |
| 9 | $\mathrm{execute}(\pi)$ | Action |

### Abstract BDI Control Loop

#### Definitions

> **Event ($Ev$)**: The set of pending events (e.g. new percepts, new goals, results of executed actions) the agent must respond to.

> **Plan Library ($PLib$)**: A pre-written set of plans the agent selects from, rather than generating plans from scratch.

> **Agent Interpreter**: The procedure that runs the BDI loop over the agent's events, beliefs, plan library and intentions.

The abstract BDI loop (De Silva, Meneguzzi and Logan, 2020) is the general interpreter used by BDI programming languages. The agent is the tuple $\langle Ev, Bel, PLib, Int \rangle$.

```text
Algorithm: BDI Agent Interpreter
1: procedure AGENTINTERPRETER(<Ev, Bel, PLib, Int>)
2:     while true do
3:         Ev  <- UPDATEEVENTS(Ev)
4:         Bel <- UPDATEBELIEFS(Ev, Bel)
5:         Int <- SELECTPLANS(Ev, Bel, PLib, Int)
6:         Ev  <- EXECUTEINTENTION(Int, Ev)
```

Step by step:

1. **Update events**: collect new events, e.g. incoming percepts.
2. **Update beliefs**: revise beliefs $Bel$ from the events.
3. **Select plans**: for the current events and beliefs, choose applicable plans from $PLib$ and add them to the intentions $Int$.
4. **Execute intention**: run a step of an intention; execution can generate new events, which feed the next iteration.

| Aspect | Original loop (Wooldridge) | Abstract loop (De Silva et al.) |
|---|---|---|
| Driven by | Percepts $\rho$ | Events $Ev$ |
| Plan source | $\mathrm{plan}(B,I)$ computes a plan | Plans selected from a plan library $PLib$ |
| Deliberation | Explicit $\mathrm{options}$ and $\mathrm{filter}$ | Folded into $\mathrm{selectPlans}$ |
| Execution output | Executes $\pi$ | Execution produces new events |

### Implementing BDI Agents

#### Definitions

> **Agent-Oriented Programming Language (AOPL)**: A programming language whose primitives are agent concepts such as beliefs, goals, plans and intentions.

BDI agents are implemented using agent-oriented programming languages:

| Language / Framework | Notes |
|---|---|
| AgentSpeak | Core BDI language; implemented by **JASON**; **ASTRA** is based on AgentSpeak |
| PRS (Procedural Reasoning System) | Early BDI system |
| JADEX | Programming BDI agents in Java |

### Advantages Of BDI Agents

BDI-based agent programming languages offer significant advantages for developing autonomous systems:

- **Rapid development**.
- **Context sensitive** behaviour.
- **Robust behaviour**.
- **Greater intelligibility** — the agent's reasoning is expressed in understandable beliefs, goals and plans.
- **Verifiability**, compared to agents whose programs are learned.

### Extending The BDI Architecture

#### Definitions

> **Reconsider Function**: A check placed before $\mathrm{options}(\cdot)$ and $\mathrm{filter}(\cdot)$ that decides whether the agent should deliberate about new intentions at all on this iteration.

> **Serendipity**: An intention becoming achieved without the agent's own action (e.g. through changes in the environment).

> **POMDP (Partially Observable Markov Decision Process)**: A decision model for sequential decisions under uncertainty about both action outcomes and the true state.

> **DDN (Dynamic Decision Network)**: A decision network unrolled over time steps, combining probabilistic belief nodes, decision nodes and utility nodes.

Ways the basic architecture is extended:

- **Goals as hierarchical plans**: goals decompose into sub-goals/sub-plans.
- **Reconsider function**, useful when the environment changes very fast:
  - comes just before $\mathrm{options}(\cdot)$ and $\mathrm{filter}(\cdot)$;
  - decides whether to consider new intentions;
  - saves computation/time;
  - keeps the agent focused on its current objectives.
- **Intention checking**: at every iteration through the main loop, test whether currently pursued intentions are still achievable, or already achieved (by serendipity).
- **Incorporating uncertainty**, e.g. using POMDPs or DDNs.

### Sugarcane Grower Simulation Example

The running example (Price et al., 2022) is based on a real-world sugarcane supply chain in KwaZulu-Natal.

A key grower (farmer) decision is **when to cut the sugarcane crop** to deliver it to the mill. Constraints:

- The cane must be **burned before delivery**.
- Burning **cannot happen when there is rain or high wind**.
- The grower has a **quota for weekly delivery** to the mill.

The grower agent interacts with an environment made up of the weather, the mill, the sugarcane grower and the actions taken: it **senses** the environment and **acts** on it.

![Sugarcane grower setup](../../../diagrams/CSC3044S-AI%20Systems/AIS/08_Agent_Architectures_IV_BDI/sugarcane_grower_setup.svg)
*Simulation setup: the grower agent senses the weather, mill and grower state, and acts back on the environment.*

### Probabilistic BDI Agent

The grower agent is a BDI agent whose "think" step is probabilistic. Its internal flow:

1. **Sense**: the environment (weather, mill, grower) produces **percepts**.
2. **Belief revision based on percepts**: percepts update the **beliefs** (beliefs also feed back into revision).
3. **Intention selection**: uses the revised beliefs and the **set of desires** to choose an intention.
4. **Act**: the selected **intention** is output as an action in the environment.

![Probabilistic BDI agent](../../../diagrams/CSC3044S-AI%20Systems/AIS/08_Agent_Architectures_IV_BDI/probabilistic_bdi_agent.svg)
*Inside the grower agent: percepts drive belief revision, revised beliefs and the set of desires feed intention selection, and the intention is output as an action. Dashed arrows show beliefs being read and updated.*

| BDI Component | Realisation in the grower agent |
|---|---|
| Percepts | Discretised weather observations and forecasts |
| Beliefs | Nodes in a DDN, revised by Bayesian inference |
| Desires | Fixed set of desires about cane burning |
| Intention selection | A decision node in the DDN, chosen by utility |

The belief revision and intention selection steps are implemented by a **DDN model**: percept nodes feed belief nodes, belief nodes feed an intention-selection (decision) node, and a utility node evaluates the choice. The network is repeated across time slices.

### Dynamic Bayesian Decision Network

#### Definitions

> **Dynamic Bayesian Decision Network**: A Bayesian decision network repeated over time steps ($t$, $t+1$, ...), where some nodes link across time slices so beliefs carry forward.

> **Inferred Belief Node**: A node whose value is inferred (not directly observed).

> **Percept Node**: A node entered as evidence from observations.

> **Outcome Node**: An inferred node that summarises an outcome used by the decision (e.g. burning conditions).

> **Intention Selection Node**: The decision node; its states are the possible intentions.

> **Utility Node**: A node giving the value of a decision in a given context.

> **Constant Node**: A fixed parameter of the agent.

![Dynamic Bayesian decision network](../../../diagrams/CSC3044S-AI%20Systems/AIS/08_Agent_Architectures_IV_BDI/dynamic_bayesian_decision_network.svg)
*The DDN unrolled over the previous day (t) and current day (t+1). White arrows carry cane dryness forward in time; dashed red outlines mark the four node groups.*

The network covers two time steps: **previous day** (time step $t$) and **current day** (time step $t+1$). Node types:

| Node Type | Nodes |
|---|---|
| Percepts | Observed rain type, observed wind, observed max temp; rain type forecast, wind forecast, max temp forecast; rain forecast for next 4 days, wind forecast for next 4 days; current day's burning requirements |
| Inferred beliefs | Cane dryness |
| Outcome nodes | Burning conditions, advance burning requirements |
| Intention selection | Amount of cane to burn |
| Utility | Value of burning |
| Constant | Grower size |

The nodes form four labelled groups:

| Group | Nodes | Purpose |
|---|---|---|
| "Cane dryness" nodes | Cane dryness at $t$, plus observed rain type, wind and max temp | Cane dryness at $t+1$ depends on cane dryness at $t$ and the observed weather — this is the temporal link |
| "Current day's weather" nodes | Rain type, wind and max temp forecasts | Together with cane dryness, determine **burning conditions** |
| "Advance burning requirements" nodes | Rain and wind forecasts for the next 4 days | Determine **advance burning requirements** (need to burn ahead of bad weather) |
| "Current day's burning requirements" | Current day's burning requirements | Feeds the decision about how much cane to burn |

How the decision is made each day:

1. Cane dryness is updated from the previous day's dryness and the observed weather.
2. Cane dryness and the day's forecasts give the **burning conditions**.
3. The 4-day forecasts give the **advance burning requirements**.
4. The decision node chooses the **amount of cane to burn**.
5. **Value of burning** (utility) scores that choice using burning conditions, advance burning requirements, current day's burning requirements and grower size.
6. The decision state with the highest expected utility becomes the intention:

$$
I_t = \arg\max_{a \in \text{amounts of cane to burn}} \; EU(a \mid B_t)
$$

### Probabilistic BDI Control Loop

The grower's loop is adapted from Wooldridge (2000). Input: a DDN containing initial beliefs and desires relating to cane burning. Output: the selected intention.

```text
Algorithm: Probabilistic BDI agent's control loop (adapted from Wooldridge, 2000)
1:  Input: DDN, containing initial beliefs and desires relating to cane burning
2:  Output: Selected intention
3:  t = 0                                       // time
4:  B0 = beliefs stored in the DDN
5:  D = set of desires
6:  I0 = ∅
7:  set GrowerSize (large/small) and MaxDailyDeliveryRate
8:  while true do
9:      t = t + 1
10:     get observations from environment
11:     Pt = discretised observations           // percepts
12:     BurningRequirements_t = calcBR(CaneAwaitingDelivery_t, DeliveryStatus_t,
                                        MaxDailyDeliveryRate, GrowerSize)
13:     enter relevant percepts Pt into DDN as evidence
14:     Bt = revised beliefs, using Bayesian inference
15:     if EmergencyIsPresent_t then
            It = address emergency
            enter "Burn no cane" into DDN decision node as evidence
16:     else if DayOfWeek_t = Sunday then
            It = rest
            enter "Burn no cane" into DDN decision node as evidence
17:     else if it is MillingSeason then
            It = DDN decision state with highest utility
18:     end if
19:     output It
20: end while
```

Initialisation:

- $B_0$ = beliefs stored in the DDN; $D$ = set of desires; $I_0 = \emptyset$.
- Grower size (large/small) and maximum daily delivery rate are set as constants.

Each iteration:

1. Advance time: $t \leftarrow t + 1$.
2. Get observations and discretise them into percepts $P_t$.
3. Compute the day's burning requirements:

$$
BR_t = \mathrm{calcBR}(\text{CaneAwaitingDelivery}_t, \text{DeliveryStatus}_t, \text{MaxDailyDeliveryRate}, \text{GrowerSize})
$$

4. Enter relevant percepts $P_t$ into the DDN as evidence.
5. Revise beliefs $B_t$ using **Bayesian inference**.
6. Select the intention $I_t$ using a priority ordering:

| Condition (checked in order) | Intention $I_t$ | DDN decision node |
|---|---|---|
| Emergency present | Address emergency | Evidence set to "Burn no cane" |
| Day is Sunday | Rest | Evidence set to "Burn no cane" |
| Milling season | DDN decision state with highest utility | Decided by the DDN |

7. Output $I_t$.

Compared with the original loop, $\mathrm{brf}$ becomes Bayesian inference in the DDN, and $\mathrm{filter}$/$\mathrm{plan}$ become rule-based overrides plus maximum-utility selection in the decision node.

### Discussion Points

Open questions for reflection on BDI agents:

- Do BDI agents think or act **rationally** or **humanly**?
- Are they **deliberative**, **reactive** or **hybrid**?
- How do BDI agents compare to purely ML-based learning agents, e.g. **Deep Reinforcement Learning** agents?

### References

General references:

- Bordini, R.H., El Fallah Seghrouchni, A., Hindriks, K., Logan, B. and Ricci, A., 2020. Agent programming in the cognitive era. *Autonomous Agents and Multi-Agent Systems*, 34(2), p.37.
- De Silva, L., Meneguzzi, F. and Logan, B., 2020. BDI agent architectures: A survey. *International Joint Conferences on Artificial Intelligence*.

Probabilistic extensions:

- Price, C.S., Moodley, D., Pillay, A.W. and Rens, G.B., 2022. An adaptive, probabilistic, cognitive agent architecture for modelling sugarcane growers' operational decision-making. *South African Computer Journal*, 34(1), pp.152-191.
- Wanyana, T. and Moodley, D., 2021. An agent architecture for knowledge discovery and evolution. *German Conference on Artificial Intelligence (KI)*, pp.241-256, Springer LNAI vol. 12873.
- Rens, G. and Moodley, D., 2017. A hybrid POMDP-BDI agent architecture with online stochastic planning and plan caching. *Cognitive Systems Research*, 43, pp.1-20.
