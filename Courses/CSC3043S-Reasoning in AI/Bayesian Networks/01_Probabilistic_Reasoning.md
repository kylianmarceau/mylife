---
tags:
  - reasoning-in-ai
---

# Introduction to Probabilistic Reasoning

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Bayesian Networks  
> **Source**: [1-Probabilities.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/Bayesian%20Networks/1-Probabilities.pdf), Dr Jan Buys, slides 1-35 (based in part on Klein and Abbeel, CS188 UC Berkeley)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Uncertainty and probabilistic models|Uncertainty and probabilistic models]]
  - [[#Bayesian networks and module structure|Bayesian networks and module structure]]
  - [[#Random variables|Random variables]]
  - [[#Probability distributions|Probability distributions]]
  - [[#Joint distributions|Joint distributions]]
  - [[#Events|Events]]
  - [[#Marginal distributions|Marginal distributions]]
  - [[#Conditional probability|Conditional probability]]
  - [[#The normalization trick|The normalization trick]]
  - [[#Product rule and chain rule|Product rule and chain rule]]
  - [[#Independence|Independence]]
  - [[#Conditional independence|Conditional independence]]

---

## Core Content

### Uncertainty and probabilistic models

#### Definitions

> **Systematic uncertainty**: Uncertainty from observing only finite datasets; more data allows better predictions.

> **Intrinsic uncertainty**: Uncertainty because only partial information about the world is observable, so not every factor influencing a prediction can be modelled.

> **Probabilistic model**: A model that uses probabilities to describe the relationship between multiple variables that each have some degree of uncertainty.

> **Evidence (observed variables)**: Variables whose values are known, such as sensor readings or symptoms.

> **Unobserved variables**: Variables we must reason about, such as an object's location or which disease is present.

> **Probabilistic reasoning**: Using probabilistic models to manage beliefs and reason about unknown variables given evidence. There may or may not be actual randomness in the world.

Dealing with uncertainty is a central problem in AI. Probability theory quantifies and reasons about uncertainty.

| Framework | Comparison with probability |
|---|---|
| Logic-based frameworks | Probability is more flexible |
| Fuzzy logic and other degree-of-truth methods | Probability is more principled |

A probabilistic model's environment has three parts:

1. **Observed variables** — what we know about the state of the world.
2. **Unobserved variables** — what we need to infer.
3. **The model** — a description of how the known and unknown variables relate to each other.

Models describe how a portion of the world works. They are always simplifications and may omit variables or interactions. "All models are wrong; but some are useful." — George E. P. Box.

Two kinds of reasoning appear throughout the module:

| Reasoning type | Direction | Example |
|---|---|---|
| **Diagnostic reasoning** (explanation) | From effects back to causes | Symptoms → which disease? |
| **Causal reasoning** (prediction) | From causes forward to effects | Rain → will traffic be heavy? |

> [!info] <span style="color: #66b3ff">Why not just deep learning?</span>
> Deep learning models are powerful at predicting one variable from input features, but they cannot reason directly about the relationships between different variables. Probabilistic models make those relationships explicit.

### Bayesian networks and module structure

#### Definitions

> **Bayesian network**: A framework for probabilistic models that represents knowledge and enables reasoning under uncertainty.

The motivating example is web-service fault diagnosis. Possible faults (database failure, network outage, traffic spike) cause intermediate symptoms (query errors, server overload), which affect whether the service is up.

![Web-service fault diagnosis network](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/01_Probabilistic_Reasoning/web-service-faults.svg)

*Faults (database failure, network outage, traffic spike) cause symptoms (query errors, server overload), which determine whether the service is up. Observing that the service is down lets us reason backwards to the most likely fault.*

| Week | Topics |
|---|---|
| Week 1 | Probability; BN graphical models; BN inference; tutorial |
| Week 2 | BN conditional independence; BN approximate inference; DBNs/HMMs; decision networks; tutorial |

The assignment is a closed practical on applying Bayesian networks. Every later topic builds on random variables, distributions, marginals, conditionals, and (conditional) independence.

### Random variables

#### Definitions

> **Random variable**: A variable representing some aspect of the world about which we may be uncertain.

> **Domain**: The set of values a random variable can take.

| Variable | Meaning | Domain |
|---|---|---|
| $R$ | Is it raining? | $\{\text{true}, \text{false}\}$, written $\{+r, -r\}$ |
| $T$ | Is it hot or cold? | $\{\text{hot}, \text{cold}\}$ |
| $D$ | How long will it take to drive to campus? | $[0, \infty)$ |

- Capital letters denote random variables ($R$, $T$).
- Lower-case letters denote specific values or variables ranging over values ($r$, $t$).
- This module works mainly with **discrete (categorical)** variables.

### Probability distributions

#### Definitions

> **Probability distribution**: An association of each value in a variable's domain with a probability. For a discrete variable it is a table of probability values.

> **Probability**: A single number $P(X = x)$ satisfying non-negativity and summing to one over the domain.

Unobserved random variables have distributions.

| $T$ | $P$ |
|---|---|
| hot | 0.5 |
| cold | 0.5 |

| $W$ | $P$ |
|---|---|
| sun | 0.6 |
| rain | 0.1 |
| fog | 0.3 |
| meteor | 0.0 |

A probability must satisfy:

$$
\forall x \;\; P(X = x) \ge 0 \qquad\qquad \sum_x P(X = x) = 1
$$

For example, $P(W = \text{rain}) = 0.1$. When every domain value is unique across variables, the shorthand $P(\text{rain}) = P(W = \text{rain})$ is used.

### Joint distributions

#### Definitions

> **Joint distribution**: A specification of a real number for each possible assignment to a set of random variables $X_1, X_2, \dots, X_n$.

> **Outcome**: A complete assignment to all variables in the joint distribution.

Notation:

$$
P(X_1 = x_1, X_2 = x_2, \dots, X_n = x_n) \quad\text{or}\quad P(x_1, x_2, \dots, x_n)
$$

A joint distribution must satisfy:

$$
P(x_1, x_2, \dots, x_n) \ge 0 \qquad\qquad \sum_{(x_1, x_2, \dots, x_n)} P(x_1, x_2, \dots, x_n) = 1
$$

The running example $P(T, W)$:

| $T$ | $W$ | $P$ |
|---|---|---|
| hot | sun | 0.4 |
| hot | rain | 0.1 |
| cold | sun | 0.2 |
| cold | rain | 0.3 |

Key properties:

- A probabilistic model *is* a joint distribution over a set of random variables.
- The joint says how likely each outcome is.
- A joint over $n$ variables with domain size $d$ has $d^n$ entries.

> [!warning] <span style="color: #ff939b">Exponential size</span>
> Because the table grows as $d^n$, full joint tables quickly become unmanageable. Bayesian networks are the better representation developed in this module.

### Events

#### Definitions

> **Event**: A set of outcomes $E$.

The probability of an event is the sum over all outcomes consistent with it:

$$
P(E) = \sum_{(x_1, \dots, x_n) \in E} P(x_1, \dots, x_n)
$$

Given a joint distribution, the probability of any event can be calculated. Using the $P(T, W)$ table:

| Event | Matching outcomes | Probability |
|---|---|---|
| Hot AND sunny | (hot, sun) | $0.4$ |
| Hot | (hot, sun), (hot, rain) | $0.4 + 0.1 = 0.5$ |
| Hot OR sunny | (hot, sun), (hot, rain), (cold, sun) | $0.4 + 0.1 + 0.2 = 0.7$ |

The events we usually care about are **partial assignments**, such as $P(T = \text{hot})$.

### Marginal distributions

#### Definitions

> **Marginal distribution**: A distribution over a subset of the variables in a joint distribution.

> **Marginalization**: Computing a marginal by summing the probabilities of all assignments to the variables being eliminated ("summing out").

Marginals are sub-tables: collapse rows that agree on the kept variables and add their probabilities.

$$
P(t) = \sum_w P(t, w) \qquad\qquad P(w) = \sum_t P(t, w)
$$

| $T$ | $P$ |
|---|---|
| hot | $0.4 + 0.1 = 0.5$ |
| cold | $0.2 + 0.3 = 0.5$ |

| $W$ | $P$ |
|---|---|
| sun | $0.4 + 0.2 = 0.6$ |
| rain | $0.1 + 0.3 = 0.4$ |

### Conditional probability

#### Definitions

> **Conditional probability**: The probability of $a$ given $b$, defined as $P(a \mid b) = \dfrac{P(a, b)}{P(b)}$.

> **Evidence**: The observed variable(s) being conditioned on.

> **Conditional distribution**: A probability distribution over some variables given fixed values of others.

The intuition is: what does observing $b$ tell us about $a$? Conditioning restricts attention to the region where $b$ holds and rescales it to total probability one.

![Conditioning restricts to the evidence](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/01_Probabilistic_Reasoning/conditional-events.svg)

*Observing $b$ discards everything outside $b$ and treats $b$ as the new universe; $P(a \mid b)$ is the share of $b$'s mass that also lies in $a$.*

Example from the $P(T, W)$ table:

$$
P(W = \text{sun} \mid T = \text{cold}) = \frac{P(\text{sun}, \text{cold})}{P(\text{cold})} = \frac{0.2}{0.2 + 0.3} = 0.4
$$

Conditioning on each value of $T$ gives a family of conditional distributions:

| $W$ | $P(W \mid T = \text{hot})$ | $P(W \mid T = \text{cold})$ |
|---|---|---|
| sun | $0.4/0.5 = 0.8$ | $0.2/0.5 = 0.4$ |
| rain | $0.1/0.5 = 0.2$ | $0.3/0.5 = 0.6$ |

Together, these tables form the **full conditional distribution** $P(W \mid T)$. Each column sums to one; the table as a whole does not.

### The normalization trick

A more efficient way to compute a conditional distribution avoids computing $P(\text{evidence})$ separately.

1. **Select** the joint entries consistent with the evidence, giving $P(X_1, x_2)$ from $P(X_1, X_2)$.
2. **Normalize** the selection:
   1. Compute the sum of all selected entries, $Z = \sum_{x_1} P(x_1, x_2)$.
   2. Divide every entry by $Z$.

The sum $Z$ is exactly the probability of the evidence.

![Normalization trick](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/01_Probabilistic_Reasoning/normalization-trick.svg)

*Select the joint rows matching $T = \text{cold}$ ($0.2$, $0.3$), sum them to get $Z = 0.5 = P(\text{cold})$, then divide each by $Z$ to get $P(W \mid \text{cold}) = (0.4, 0.6)$.*

$$
P(w \mid c) = \frac{P(w, c)}{P(c)} = \frac{P(w, c)}{\sum_{w'} P(w', c)}
$$

Example: compute $P(W \mid T = c)$.

| Step | $W = \text{sun}$ | $W = \text{rain}$ |
|---|---|---|
| Select rows with $T = \text{cold}$ | $0.2$ | $0.3$ |
| $Z = 0.2 + 0.3 = 0.5 = P(c)$ | — | — |
| Divide by $Z$ | $0.4$ | $0.6$ |

### Product rule and chain rule

#### Definitions

> **Product rule**: The joint distribution written as a marginal times a conditional, $P(x, y) = P(y)\,P(x \mid y)$.

> **Chain rule**: Any joint distribution written as an incremental product of conditional distributions.

The product rule is a rearrangement of the definition of conditional probability. Example with weather $W$ and dryness $D$:

| $W$ | $P(W)$ |
|---|---|
| sun | 0.8 |
| rain | 0.2 |

| $D$ | $W$ | $P(D \mid W)$ | $P(D, W) = P(W)P(D \mid W)$ |
|---|---|---|---|
| wet | sun | 0.1 | $0.8 \times 0.1 = 0.08$ |
| dry | sun | 0.9 | $0.8 \times 0.9 = 0.72$ |
| wet | rain | 0.7 | $0.2 \times 0.7 = 0.14$ |
| dry | rain | 0.3 | $0.2 \times 0.3 = 0.06$ |

The chain rule generalizes this to $n$ variables:

$$
P(x_1, x_2, \dots, x_n) = P(x_1)\,P(x_2 \mid x_1)\,P(x_3 \mid x_1, x_2) \cdots = \prod_{i=1}^{n} P(x_i \mid x_1, \dots, x_{i-1})
$$

The chain rule holds for any ordering of variables. However, with many variables the later conditional tables (conditioned on all previous variables) become unmanageably large.

### Independence

#### Definitions

> **Independence**: $X$ and $Y$ are independent if $\forall x, y : P(x, y) = P(x)\,P(y)$. Notation: $X \perp\!\!\!\perp Y$.

The joint over two independent variables factors into a product of two simpler distributions. An equivalent definition:

$$
\forall x, y : P(x \mid y) = P(x)
$$

**Example: $n$ fair independent coin flips.** Each $P(X_i)$ is $H = 0.5$, $T = 0.5$. The joint $P(X_1, \dots, X_n)$ has $2^n$ entries, but independence means it is fully described by $n$ small tables.

**Testing independence** — check whether $P(t, w) = P(t)P(w)$ for *every* assignment. Both tables below have marginals $P(\text{hot}) = P(\text{cold}) = 0.5$, $P(\text{sun}) = 0.6$, $P(\text{rain}) = 0.4$.

| $T$ | $W$ | $P_1(t, w)$ | $P_2(t, w)$ | $P(t)P(w)$ |
|---|---|---|---|---|
| hot | sun | 0.4 | 0.3 | 0.3 |
| hot | rain | 0.1 | 0.2 | 0.2 |
| cold | sun | 0.2 | 0.3 | 0.3 |
| cold | rain | 0.3 | 0.2 | 0.2 |

- $P_1$: $0.4 \ne 0.3$, so $T$ and $W$ are **not** independent.
- $P_2$: every entry matches, so $T$ and $W$ **are** independent.

### Conditional independence

#### Definitions

> **Conditional independence**: $X$ is conditionally independent of $Y$ given $Z$ if and only if $\forall x, y, z : P(x, y \mid z) = P(x \mid z)\,P(y \mid z)$. Notation: $X \perp\!\!\!\perp Y \mid Z$.

Full independence is usually too strong an assumption. Conditional independence expresses independence that holds only once some other variable is known.

The equivalent definition is:

$$
\forall x, y, z : P(x \mid z, y) = P(x \mid z)
$$

**Toothache example.** Consider Boolean variables $P(\text{Toothache}, \text{Cavity}, \text{Detect})$. If you have a cavity, whether a probe detects it does not depend on whether you have toothache:

$$
P(+\text{detect} \mid +\text{toothache}, +\text{cavity}) = P(+\text{detect} \mid +\text{cavity})
$$

The same holds without a cavity:

$$
P(+\text{detect} \mid +\text{toothache}, -\text{cavity}) = P(+\text{detect} \mid -\text{cavity})
$$

So $\text{Detect} \perp\!\!\!\perp \text{Toothache} \mid \text{Cavity}$. These statements are all equivalent:

- $P(\text{Detect} \mid \text{Toothache}, \text{Cavity}) = P(\text{Detect} \mid \text{Cavity})$
- $P(\text{Toothache} \mid \text{Detect}, \text{Cavity}) = P(\text{Toothache} \mid \text{Cavity})$
- $P(\text{Toothache}, \text{Detect} \mid \text{Cavity}) = P(\text{Toothache} \mid \text{Cavity})\,P(\text{Detect} \mid \text{Cavity})$

> [!tip] <span style="color: #5ad4b5">Key point</span>
> Unconditional (absolute) independence is very rare. Conditional independence is our most basic and robust form of knowledge about uncertain environments.

More examples:

| Variables | Conditional independence | Reason |
|---|---|---|
| Traffic, Umbrella, Raining | $\text{Traffic} \perp\!\!\!\perp \text{Umbrella} \mid \text{Raining}$ | Rain causes both; once rain is known, umbrellas tell us nothing more about traffic |
| Fire, Smoke, Alarm | $\text{Alarm} \perp\!\!\!\perp \text{Fire} \mid \text{Smoke}$ | The alarm reacts to smoke; once smoke is known, fire adds nothing |

**Conditional independence and the chain rule.** The chain rule always gives:

$$
P(\text{Traffic}, \text{Rain}, \text{Umbrella}) = P(\text{Rain})\,P(\text{Traffic} \mid \text{Rain})\,P(\text{Umbrella} \mid \text{Rain}, \text{Traffic})
$$

With the assumption $\text{Umbrella} \perp\!\!\!\perp \text{Traffic} \mid \text{Rain}$, the last factor simplifies:

$$
P(\text{Traffic}, \text{Rain}, \text{Umbrella}) = P(\text{Rain})\,P(\text{Traffic} \mid \text{Rain})\,P(\text{Umbrella} \mid \text{Rain})
$$

Each factor now conditions on fewer variables, so the tables are smaller. Bayesian networks are a way of expressing exactly these conditional independence assumptions.
