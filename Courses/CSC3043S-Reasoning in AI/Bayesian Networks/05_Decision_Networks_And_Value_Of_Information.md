---
tags:
  - reasoning-in-ai
---

# Decision Networks and Value of Information

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Bayesian Networks  
> **Source**: [5-DecisionNetworks.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/Bayesian%20Networks/5-DecisionNetworks.pdf), Dr Jan Buys, slides 1-31 (based on Klein and Abbeel, CS188 UC Berkeley; some slides from Deshen Moodley)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Rationality and expected utility|Rationality and expected utility]]
  - [[#Utility-based agents and utilities|Utility-based agents and utilities]]
  - [[#Decision networks|Decision networks]]
  - [[#Node types|Node types]]
  - [[#Maximum expected utility|Maximum expected utility]]
  - [[#Action selection procedure|Action selection procedure]]
  - [[#Umbrella example|Umbrella example]]
  - [[#Information links and decision tables|Information links and decision tables]]
  - [[#Machine repair example|Machine repair example]]
  - [[#Value of perfect information|Value of perfect information]]

---

## Core Content

### Rationality and expected utility

#### Definitions

> **Rational**: Maximally achieving pre-defined goals. Rationality concerns only which decisions are made, not the thought process behind them.

> **Expected utility**: The probability-weighted average utility of an action's possible outcomes.

The goal of AI can be defined as building agents that act rationally. Goals are expressed as the **utility** of outcomes, so being rational means **maximizing expected utility**.

Many AI problems can be framed as decision making. A rational agent chooses actions that maximize its expected utility given its knowledge. This raises two questions:

- Where do utilities come from?
- How can Bayesian networks be extended to choose actions that maximize expected utility?

### Utility-based agents and utilities

#### Definitions

> **Utility function**: A measure of success or happiness at a given state; it can measure the degree to which a goal is achieved.

> **Utilities**: Functions from outcomes to real numbers that describe an agent's preferences. They summarize "what the agent wants" as a preference ranking over outcomes.

A utility-based agent:

- Can trade off conflicting goals.
- Can weigh the likelihood of success against the importance of a goal.
- Selects the action with the highest expected utility — the action most likely to lead to a future state closest to the desired goal.

Properties of utilities:

- **Rational preferences** are defined by axioms of rationality. These can be shown to be consistent with maximizing expected utility.
- The standard approach is to set utilities manually and let behaviour emerge from maximizing expected utility.

### Decision networks

#### Definitions

> **Decision network (influence diagram)**: A Bayesian network with added nodes for actions and utility, used to calculate the expected utility of actions.

**Example**: decide whether to take an umbrella when going outside. What is the utility of taking an umbrella if it rains, versus if it is sunny?

![Umbrella decision network](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/05_Decision_Networks_And_Value_Of_Information/umbrella-influence.svg)

*Weather affects the forecast and the utility. The umbrella decision also affects utility. The forecast is observable; the weather is not.*

### Node types

| Node | Shape | Represents | Rules |
|---|---|---|---|
| **Chance node** | Ellipse | Observed or unobserved random variables, as in a BN | Has a CPT given its parents |
| **Action / decision node** | Rectangle | A decision; acts as observed evidence | Chance-node parents mean their evidence is available at decision time. Action-node parents represent the order of decisions |
| **Utility node** | Diamond | A utility function quantifying how desirable outcomes are | Depends on action and chance nodes; cannot have children |

### Maximum expected utility

#### Definitions

> **Principle of maximum expected utility (MEU)**: Choose the action that maximizes the expected utility given the evidence.

The network designer must define the utility function. Utilities can be analogous to money, with caveats:

- They have no units, only a scale distinguishing best, neutral, and worst outcomes.
- They are best read in relative terms: $20$ is twice as desirable as $10$; $-20$ is as undesirable as $20$ is desirable; $0$ is usually neutral.

For action $a$, evidence $E = e$, hidden parent(s) $S$ of the utility node, and utility $U(s, a)$:

$$
\text{EU}(a, e) = \mathbb{E}_{P(S \mid e)}\big[U(s, a)\big] = \sum_s P(s \mid e)\,U(s, a)
$$

$$
\text{MEU}(e) = \max_a \text{EU}(a, e)
$$

### Action selection procedure

1. Instantiate all the evidence $e$.
2. For each possible value $a$ of the action node:
   1. Compute the posterior $P(S \mid a, e)$ over the unobserved parents $S$ of the utility node — ordinary BN inference with those parents as query variables.
   2. Compute $\text{EU}(a, e)$.
3. Choose the action with the maximum expected utility.

### Umbrella example

| $W$ | $P(W)$ |
|---|---|
| sun | 0.7 |
| rain | 0.3 |

| $A$ | $W$ | $U(A, W)$ |
|---|---|---|
| leave | sun | 100 |
| leave | rain | 0 |
| take | sun | 20 |
| take | rain | 70 |

**No evidence:**

$$
\text{EU}(\text{leave}) = 0.7(100) + 0.3(0) = 70 \qquad \text{EU}(\text{take}) = 0.7(20) + 0.3(70) = 35
$$

$\text{MEU}(\varnothing) = 70$, so the optimal decision is **leave**.

**With evidence $F = \text{bad}$:** inference gives $P(W \mid F = \text{bad})$: sun $0.34$, rain $0.66$.

$$
\text{EU}(\text{leave} \mid \text{bad}) = 0.34(100) + 0.66(0) = 34 \qquad \text{EU}(\text{take} \mid \text{bad}) = 0.34(20) + 0.66(70) = 53
$$

$\text{MEU}(F = \text{bad}) = 53$, so the optimal decision is **take**.

### Information links and decision tables

#### Definitions

> **Information link**: An arc from a chance node to a decision node, indicating that the chance node's value is known when the decision is made. It has no parameters and is not part of the basic evaluation.

> **Decision table (policy)**: A table of optimal actions conditioned on the relevant states of affairs, i.e. on the values of the decision node's parents.

With an information link, evaluation is extended to say explicitly which decision to make for each value of that chance node. This adds an outer loop to action selection:

1. Instantiate any observed evidence.
2. For each combination of values of the decision node's parents:
   1. Compute the expected utility of each action as before.
   2. Record the action with maximum expected utility.

### Machine repair example

A factory machine has a hidden fault with probability $0.2$.

- A faulty machine that is not repaired breaks down mid-production, costing $1000$.
- A repair costs $100$, whether or not the fault was there.
- A diagnostic test reports positive for $90\%$ of faulty machines and $10\%$ of healthy ones.

Questions: should the engineer repair? Should the engineer test first, and what is the test worth?

| $F$ | $P(F)$ |
|---|---|
| faulty | 0.2 |
| ok | 0.8 |

| $F$ | $P(T = \text{pos} \mid F)$ | $P(T = \text{neg} \mid F)$ |
|---|---|---|
| faulty | 0.9 | 0.1 |
| ok | 0.1 | 0.9 |

| $F$ | $D$ | $U(F, D)$ |
|---|---|---|
| faulty | repair | $-100$ |
| ok | repair | $-100$ |
| faulty | don't | $-1000$ |
| ok | don't | $0$ |

**No information.** Act on the prior alone:

$$
\text{EU}(\text{repair}) = 0.2(-100) + 0.8(-100) = -100 \qquad \text{EU}(\text{don't}) = 0.2(-1000) + 0.8(0) = -200
$$

$\text{MEU} = -100$: with no information, always repair.

**Add the information link $T \rightarrow D$.** The link only says $T$ will be known when deciding. The answer becomes a decision table.

![Repair decision network with information link](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/05_Decision_Networks_And_Value_Of_Information/repair-policy.svg)

*Fault influences the test result and the utility. The information link from Test to Repair makes the test result available before choosing.*

**Case $T = \text{pos}$:**

$$
P(\text{pos}) = 0.2(0.9) + 0.8(0.1) = 0.26 \qquad P(\text{faulty} \mid \text{pos}) = \frac{0.18}{0.26} = 0.692
$$

$\text{EU}(\text{repair} \mid \text{pos}) = -100$; $\text{EU}(\text{don't} \mid \text{pos}) = 0.692(-1000) = -692$. So $\pi(\text{pos}) = \text{repair}$.

**Case $T = \text{neg}$:**

$$
P(\text{neg}) = 0.2(0.1) + 0.8(0.9) = 0.74 \qquad P(\text{faulty} \mid \text{neg}) = \frac{0.02}{0.74} = 0.027
$$

$\text{EU}(\text{repair} \mid \text{neg}) = -100$; $\text{EU}(\text{don't} \mid \text{neg}) = 0.027(-1000) = -27$. So $\pi(\text{neg}) = \text{don't repair}$. The observation reverses the decision.

| $T$ | $P(T)$ | $P(\text{faulty} \mid T)$ | EU(repair) | EU(don't) | $\pi(T)$ |
|---|---|---|---|---|---|
| pos | 0.26 | 0.692 | $-100$ | $-692$ | repair |
| neg | 0.74 | 0.027 | $-100$ | $-27$ | don't repair |

Compare this with the no-information answer, "always repair".

**The policy is a threshold.** With $p = P(\text{faulty} \mid T)$, repair is optimal exactly when

$$
-100 > -1000\,p \iff p > 0.1
$$

The two observations ($0.692$ and $0.027$) fall on opposite sides of $0.1$.

**What is the test worth?** Average the MEU of each branch over $P(T)$:

$$
\text{MEU}_{\text{test}} = 0.26(-100) + 0.74(-27) = -46 \qquad \text{MEU}_{\text{no test}} = -100
$$

The expected gain is $-46 - (-100) = 54$. It is worth paying up to $54$ to run the test.

> [!warning] <span style="color: #ff939b">Information does not always help</span>
> If repair is cheap, $U(F, \text{repair}) = -5$, the threshold becomes $-5 > -1000\,p \iff p > 0.005$. Both $0.692$ and $0.027$ exceed it, so the policy is "repair" either way and MEU is $-5$ with or without the test. Information has value only when it can change what you do.

### Value of perfect information

#### Definitions

> **Value of perfect information (VPI)**: The expected gain in MEU from observing a variable $E'$ before acting, compared with acting now.

The expected MEU after observing $E'$:

$$
\text{MEU}(E', e) = \mathbb{E}_{P(E' \mid e)}\big[\text{MEU}(e', e)\big] = \sum_{e'} P(e' \mid e)\,\text{MEU}(e', e)
$$

$$
\text{VPI}(E' \mid e) = \text{MEU}(E', e) - \text{MEU}(e)
$$

VPI is **non-negative**: on average, observing more can never hurt a rational decision maker.

**Umbrella example.** $P(F)$: good $0.59$, bad $0.41$.

| Situation | Best action | MEU |
|---|---|---|
| No evidence | leave | $70$ |
| Forecast bad | take | $53$ |
| Forecast good | leave | $95$ |

$$
\text{MEU}(F) = \sum_f P(f)\,\text{MEU}(f) = 0.59 \cdot 95 + 0.41 \cdot 53 = 77.8
$$

$$
\text{VPI}(F) = \text{MEU}(F) - \text{MEU}(\varnothing) = 77.8 - 70 = 7.8
$$
