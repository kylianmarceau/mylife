---
tags:
  - ai-systems
---

# Agent Architectures IV: Beliefs, Desires, Intentions, And Probabilistic BDI

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3044S AI Systems  
> **Source**: [CSC3044S-Lecture 8-Agent Architectures IV(BDI) - Copy.pdf](../../Sources/CSC3044S%20-%20AI%20Systems/CSC3044S-Lecture%208-Agent%20Architectures%20IV%28BDI%29%20-%20Copy.pdf), Deshen Moodley, pages 1-18  
> **Generated**: 2026-10-01  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#The Agent Paradigm And BDI Mental States|The Agent Paradigm And BDI Mental States]]
  - [[#Practical Reasoning And Bounded Rationality|Practical Reasoning And Bounded Rationality]]
  - [[#Original BDI Control Loop|Original BDI Control Loop]]
  - [[#Abstract BDI Interpreter And Plan Libraries|Abstract BDI Interpreter And Plan Libraries]]
  - [[#Implementation And Advantages|Implementation And Advantages]]
  - [[#Reconsideration, Hierarchies, And Uncertainty|Reconsideration, Hierarchies, And Uncertainty]]
  - [[#Sugarcane Grower: Operational Decision-Making|Sugarcane Grower: Operational Decision-Making]]
  - [[#The Dynamic Bayesian Decision Network|The Dynamic Bayesian Decision Network]]
  - [[#Probabilistic BDI Control Loop|Probabilistic BDI Control Loop]]
  - [[#Rational, Human-Like, Reactive, Or Deliberative?|Rational, Human-Like, Reactive, Or Deliberative?]]

---

## Core Content

### The Agent Paradigm And BDI Mental States

#### Definitions

> **Beliefs**: What an agent believes about its environment and itself, including contextual facts and inference rules.

> **Desires**: The goals or states of affairs the agent would like to achieve.

> **Intentions**: The goals the agent is currently committed to achieving.

> **BDI architecture**: An agent architecture organised around beliefs, desires, and intentions, derived from practical-reasoning ideas.

The BDI tradition builds on Bratman's practical reasoning system and mental attitudes. An agent observes its environment, perceives relevant information, reasons, acts, and observes the resulting world again.

![The Agent Paradigm And BDI Mental States: bdi practical reasoning loop](../../diagrams/CSC3044S-AI%20Systems/08_BDI_Agent_Architectures/bdi_practical_reasoning_loop.svg)

*The BDI agent senses, revises beliefs, deliberates about goals, selects a plan for its intentions, and acts. Its previous commitments influence later deliberation.*

| Mental state | Contents                                               | Constraint or role                                          |
| ------------ | ------------------------------------------------------ | ----------------------------------------------------------- |
| Beliefs      | Current environment/self state and inference knowledge | May be incomplete, uncertain, or wrong                      |
| Desires      | Possible future objectives                             | Can conflict, be unrealistic, or be mutually inconsistent   |
| Intentions   | Selected active commitments                            | Must be coherent and achievable relative to current beliefs |

Intentions are not a list of every desirable outcome. Committing to a selected objective focuses planning and prevents the agent from reconsidering every possibility at every step.

### Practical Reasoning And Bounded Rationality

#### Definitions

> **Deliberation**: Deciding which state of affairs to bring about from possibly conflicting desires.

> **Means-ends reasoning**: Deciding how to bring about the selected state of affairs.

> **Bounded rationality**: Decision-making under limits on information, time, and computation.

> **Satisficing**: Selecting an adequate option under the available constraints instead of exhaustively seeking an ideal one.

| Stage | Question | Result |
|---|---|---|
| Deliberation | Which desires should become commitments? | Intentions |
| Means-ends reasoning | Which actions or plan achieve those commitments? | Executable plan |

The cognitive loop is:

1. Receive percepts and revise beliefs about the world and the agent itself.
2. Consider goals, current intentions, and available options.
3. Select goals to pursue, making them intentions.
4. Find a suitable plan for the chosen intentions.
5. Execute it and use subsequent observations to continue or revise it.

> [!important] <span style="color: #b89aff">Commitments bound deliberation</span>
> An idealised fully informed optimiser is different from a practical agent with limited resources. BDI uses commitments to bound deliberation; it does not guarantee global expected-utility optimality merely by maintaining three named data structures.  

### Original BDI Control Loop

#### Definitions

> **Belief revision function**, $\operatorname{brf}$: Updates beliefs using a percept.

> **Options function**: Generates candidate desires given beliefs and current intentions.

> **Filter function**: Chooses intentions from beliefs, candidate desires, and existing commitments.

> **Plan**, $\pi$: A course of action selected for the current beliefs and intentions.

| Symbol | Meaning |
|---|---|
| $B_0,B$ | Initial and current beliefs |
| $I_0,I$ | Initial and current intentions |
| $p$ | Next percept |
| $D$ | Candidate desires/options |
| $\pi$ | Selected plan |

The original loop's formal operations are:

$$
\begin{aligned}
B&\leftarrow B_0,\qquad I\leftarrow I_0,\\
B&\leftarrow\operatorname{brf}(B,p),\\
D&\leftarrow\operatorname{options}(B,I),\\
I&\leftarrow\operatorname{filter}(B,D,I),\\
\pi&\leftarrow\operatorname{plan}(B,I),\\
&\operatorname{execute}(\pi).
\end{aligned}
$$

```pseudocode
initialise beliefs and intentions
repeat forever:
    get the next percept
    revise beliefs
    generate options using beliefs and current intentions
    filter options and previous commitments into current intentions
    find a plan using beliefs and intentions
    execute the plan
```

This is an abstract control loop. Implementations must define action granularity, how execution is interrupted, and how plan failure is reported. The notation alone does not mean an entire long plan is executed blindly before sensing again.

### Abstract BDI Interpreter And Plan Libraries

#### Definitions

> **Event**: A change or request that triggers agent processing.

> **Plan library**: A collection of available plans that can be selected for events and contexts.

The interpreter in the survey uses events $E_v$, beliefs $B_{el}$, plan library $P_{lib}$, and intentions $I_{nt}$:

$$
\begin{aligned}
E_v&\leftarrow\operatorname{UpdateEvents}(E_v),\\
B_{el}&\leftarrow\operatorname{UpdateBeliefs}(E_v,B_{el}),\\
I_{nt}&\leftarrow\operatorname{SelectPlans}(E_v,B_{el},P_{lib},I_{nt}),\\
E_v&\leftarrow\operatorname{ExecuteIntention}(I_{nt},E_v).
\end{aligned}
$$

1. Update pending events.
2. Revise beliefs from those events.
3. Select applicable plans using events, beliefs, the plan library, and current intentions.
4. Execute an intention, potentially creating further events.
5. Repeat.

| Original loop | Interpreter view |
|---|---|
| Percept-driven belief revision | Event processing and belief updates |
| Options and intention filtering | Applicable plan selection |
| Plan generation/selection | Explicit plan library |
| Execute selected plan | Execute an intention and update events |

Both describe committed goal pursuit, but at different abstraction levels. The interpreter representation is especially useful for implementing BDI programs. [De Silva, Meneguzzi, and Logan: BDI Agent Architectures](https://www.ijcai.org/Proceedings/2020/0684.pdf).

### Implementation And Advantages

| Language or system | Relationship recorded in the lecture |
|---|---|
| AgentSpeak | Agent-oriented programming language |
| JASON | Implements AgentSpeak |
| ASTRA | Based on AgentSpeak |
| PRS | Procedural Reasoning System |
| JADEX | Agent programming in Java |

BDI languages can support rapid development, context-sensitive responses, robust behaviour, and greater intelligibility. Explicit beliefs, plans, and commitments can be inspected more directly than an entirely learned policy.

Verifiability is a relative advantage, not a guarantee that every BDI agent is correct. Correctness also depends on the belief updates, plan library, selection rules, and environment assumptions.

### Reconsideration, Hierarchies, And Uncertainty

#### Definitions

> **Reconsideration function**: A test deciding whether to deliberate about new or revised intentions.

> **Hierarchical plan**: A plan decomposed into subgoals or smaller plans.

> **Partially observable Markov decision process (POMDP)**: A decision model with uncertain state inferred from observations.

> **Dynamic decision network (DDN)**: A probabilistic model of changing beliefs, decisions, and utility across time.

![Reconsideration, Hierarchies, And Uncertainty: selective intention reconsideration](../../diagrams/CSC3044S-AI%20Systems/08_BDI_Agent_Architectures/selective_intention_reconsideration.svg)

*A reconsideration test avoids unnecessary full deliberation while still checking whether an intention is achieved, impossible, or inappropriate.*

Insert reconsideration immediately before generating options and filtering intentions. This saves computation and maintains focus when current commitments remain appropriate.

At every loop iteration, test whether a pursued intention is:

- Still achievable under the updated context.
- Already achieved, including by an external event or serendipity.
- Still appropriate to pursue given relevant changes.

| Reconsider too often | Reconsider too rarely |
|---|---|
| Repeated deliberation consumes time | Agent follows outdated goals |
| Commitments may become unstable | Impossible intentions remain active |
| Agent can thrash between goals | Opportunities or emergencies may be missed |

Hierarchical goals structure complex plans. POMDP or DDN extensions allow uncertain beliefs and stochastic outcomes to influence choice while keeping explicit goal commitments.

### Sugarcane Grower: Operational Decision-Making

The example models growers in a KwaZulu-Natal sugarcane supply chain. A grower decides when and how much cane to burn before cutting and delivering it to the mill.

| Constraint or information | Role |
|---|---|
| Cane burning before delivery | Preparation step |
| Rain or high wind | Prevent safe/feasible burning in the scenario |
| Weekly delivery quota | Delivery objective |
| Cane awaiting delivery | Current workload |
| Mill delivery status | Affects required burning |
| Grower size and maximum daily delivery rate | Operational limits |
| Forecasts | Uncertain information about future conditions |
| Emergency or Sunday | Explicit override in the control loop |

The source models this particular operational practice; its rules are not a general prescription for agricultural burning.

![Sugarcane Grower: Operational Decision-Making: sugarcane grower control loop](../../diagrams/CSC3044S-AI%20Systems/08_BDI_Agent_Architectures/sugarcane_grower_control_loop.svg)

*The grower architecture uses a dynamic decision network for uncertain beliefs and utility-based intention selection, while retaining explicit desires and action priorities.*

### The Dynamic Bayesian Decision Network

#### Definitions

> **Bayesian inference**: Updating probabilities using observed evidence.

> **Decision node**: A node representing the agent's choice.

> **Utility node**: A node evaluating the desirability of outcomes.

![The Dynamic Bayesian Decision Network: two day bayesian decision network](../../diagrams/CSC3044S-AI%20Systems/08_BDI_Agent_Architectures/two_day_bayesian_decision_network.svg)

*A readable reconstruction of the two-slice decision network. Weather observations update cane dryness across days; forecasts and delivery-related requirements influence burning decisions and their utility.*

| Node group | Variables and dependencies |
|---|---|
| Cane dryness | Previous dryness plus observed rain, wind, maximum temperature influence later dryness |
| Current weather | Rain-type, wind, and temperature forecasts combine with dryness into burning conditions |
| Advance requirements | Next-four-day rain and wind forecasts influence advance burning requirements |
| Current requirements | Delivery needs and grower size relate to current burning requirements |
| Intention selection | Amount of cane to burn |
| Utility | Value of burning depends on the decision, conditions, and requirements |

*The two time slices represent previous and current day; the original visual's node types distinguish percepts, inferred beliefs, an intention decision, utility, outcomes, and grower-size constants. The recreated diagram groups repeated weather variables for readability.*

New weather observations become evidence in the network. Probabilistic belief revision influences the feasible or desirable burning choice; the agent does not treat a forecast as certainty.

A general expected-utility expression for the decision is:

$$
I_t\in\arg\max_{i\in\mathcal I_t}\sum_sP(s\mid P_{1:t})U(i,s).
$$

Here $P_{1:t}$ is the accumulated percept evidence and $\mathcal I_t$ is the set of admissible decisions. This explains highest-utility decision selection; the PDF does not supply the network's numerical probability tables or utility function.

### Probabilistic BDI Control Loop

The input is a DDN containing initial beliefs and desires relating to cane burning. Initialise $t=0$, $B_0$ from the DDN, a desire set $D$, and $I_0=\varnothing$. Set grower size and maximum daily delivery rate.

The burning requirement is calculated using:

$$
\operatorname{BurningRequirements}_t=
\operatorname{calcBR}(\operatorname{CaneAwaitingDelivery}_t,
\operatorname{DeliveryStatus}_t,
\operatorname{MaxDailyDeliveryRate},\operatorname{GrowerSize}).
$$

The source names these inputs but does not define the calculation's numerical formula.

```pseudocode
initialise network beliefs, desires, empty intention, and grower constants
repeat forever:
    advance the time step
    obtain and discretise environmental observations
    calculate burning requirements from cane, delivery, and capacity data
    enter percepts into the decision network as evidence
    revise beliefs using Bayesian inference
    if an emergency is present:
        select address-emergency intention
        fix the burning decision to no cane
    else if the day is Sunday:
        select rest intention
        fix the burning decision to no cane
    else if it is milling season:
        select the network decision state with highest utility
    output the selected intention
```

| Priority | Condition | Intention / network decision |
|---:|---|---|
| 1 | Emergency | Address emergency; burn no cane |
| 2 | Sunday | Rest; burn no cane |
| 3 | Milling season | Choose the highest-utility decision |

**Source completeness clarification**: the pseudocode does not state an explicit off-season fallback when none of the conditions holds. A real implementation must define one to avoid unintentionally reusing a prior intention. Rain and wind influence the network's burning conditions; they are not separate branches in the displayed priority code.

### Rational, Human-Like, Reactive, Or Deliberative?

| Question | Reasoned interpretation |
|---|---|
| Humanly or rationally? | BDI draws on human practical reasoning while pursuing coherent goal-directed behaviour; a probabilistic extension can explicitly maximise utility |
| Deliberative? | Yes, when it selects intentions and plans from beliefs and goals |
| Reactive? | Event-triggered plans can provide rapid responses |
| Hybrid? | A concrete system may combine reactive event handling, deliberation, and probabilistic/learned components |

| BDI approach | Pure learned policy such as deep RL |
|---|---|
| Explicit beliefs, goals, plans, commitments | Behaviour encoded largely in learned parameters |
| Developer can inspect plans and goal structure | Internal decision explanations may be harder |
| Knowledge/plan engineering effort | Training data, reward, and exploration effort |
| Adapt through belief updates and plan selection | Adapt through learning or supplied state features |
| Can incorporate uncertain probabilistic reasoning | Can learn behaviour under stochastic experience |

Neither family guarantees correctness or generalisation. A hybrid can use learned perception or decision models while retaining explicit BDI commitments.

Further references recorded in the material are Bordini et al. (2020) on agent programming in the cognitive era; De Silva et al. (2020) on BDI architectures; Price et al. (2022) on probabilistic sugarcane growers; Wanyana and Moodley (2021) on knowledge discovery/evolution; and Rens and Moodley (2017) on POMDP-BDI planning and plan caching.
