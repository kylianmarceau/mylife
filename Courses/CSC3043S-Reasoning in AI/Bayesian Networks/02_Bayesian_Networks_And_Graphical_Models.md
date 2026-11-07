---
tags:
  - reasoning-in-ai
---

# Bayesian Networks: Graphical Models

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Bayesian Networks  
> **Source**: [2-BayesianNetworks-GraphicalModels.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/Bayesian%20Networks/2-BayesianNetworks-GraphicalModels.pdf), Dr Jan Buys, slides 1-23 (based in part on Klein and Abbeel, CS188 UC Berkeley)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Probabilistic inference|Probabilistic inference]]
  - [[#Inference by enumeration|Inference by enumeration]]
  - [[#Complexity of enumeration|Complexity of enumeration]]
  - [[#What a Bayesian network is|What a Bayesian network is]]
  - [[#Graphical model notation|Graphical model notation]]
  - [[#Example networks|Example networks]]
  - [[#Probabilities in Bayesian networks|Probabilities in Bayesian networks]]
  - [[#Why the product defines a valid joint|Why the product defines a valid joint]]
  - [[#Worked network examples|Worked network examples]]
  - [[#Bayesian networks and causality|Bayesian networks and causality]]
  - [[#Size and uses of a Bayesian network|Size and uses of a Bayesian network]]

---

## Core Content

### Probabilistic inference

#### Definitions

> **Probabilistic inference**: Computing a desired probability from other known probabilities, most commonly a conditional probability computed from joint or other conditional probabilities.

> **Belief**: A conditional probability representing what the agent believes given the evidence it conditions on.

> **Query variable**: The variable $Q$ whose distribution we want.

> **Hidden variables**: Variables $H_1, \dots, H_r$ that are neither query nor evidence.

Beliefs change as new evidence arrives:

| Evidence | Belief |
|---|---|
| No reported accidents | $P(\text{on time} \mid \text{no accidents}) = 0.9$ |
| + it is 5 a.m. | $P(\text{on time} \mid \text{no accidents}, \text{5 a.m.}) = 0.95$ |
| + it is raining | $P(\text{on time} \mid \text{no accidents}, \text{5 a.m.}, \text{raining}) = 0.80$ |

The general inference setup has three kinds of variables:

- **Evidence variables**: $E_1, \dots, E_k = e_1, \dots, e_k$.
- **Query variable**: $Q$.
- **Hidden variables**: $H_1, \dots, H_r$.

The goal is to compute $P(Q \mid e_1, \dots, e_k)$.

### Inference by enumeration

#### Definitions

> **Inference by enumeration**: Computing a query by selecting joint entries consistent with evidence, summing out hidden variables, and normalizing.

1. **Select** the entries consistent with the evidence: $P(Q, H_1, \dots, H_r, e_1, \dots, e_k)$.
2. **Marginalize** the hidden variables:

$$
P(Q, e_1, \dots, e_k) = \sum_{h_1, \dots, h_r} P(Q, h_1, \dots, h_r, e_1, \dots, e_k)
$$

3. **Normalize**:

$$
Z = \sum_q P(q, e_1, \dots, e_k) \qquad P(Q \mid e_1, \dots, e_k) = \frac{1}{Z}\,P(Q, e_1, \dots, e_k)
$$

**Example** — joint over season $S$, temperature $T$, weather $W$:

| $S$ | $T$ | $W$ | $P$ |
|---|---|---|---|
| summer | hot | sun | 0.30 |
| summer | hot | rain | 0.05 |
| summer | cold | sun | 0.10 |
| summer | cold | rain | 0.05 |
| winter | hot | sun | 0.10 |
| winter | hot | rain | 0.05 |
| winter | cold | sun | 0.15 |
| winter | cold | rain | 0.20 |

| Query | Computation | Result |
|---|---|---|
| $P(W)$ | $P(W) = \sum_{s,t} P(s, t, W)$ | sun $0.65$, rain $0.35$ |
| $P(W \mid \text{winter})$ | $P(W, \text{winter}) = \sum_t P(\text{winter}, t, W)$, then $Z = \sum_w P(\text{winter}, w) = 0.5$ | sun $0.25/0.5 = 0.5$, rain $0.5$ |
| $P(W \mid \text{winter}, \text{hot})$ | $Z = \sum_w P(\text{winter}, \text{hot}, w) = 0.15$, then $\frac{1}{Z}P(\text{winter}, \text{hot}, W)$ | sun $2/3$, rain $1/3$ |

### Complexity of enumeration

For a joint over $n$ variables with domain size $d$:

| Resource | Cost |
|---|---|
| Worst-case time | $O(d^n)$ |
| Space to store the joint | $O(d^n)$ |

This is intractable for many variables. However, not all variables interact directly, so we make **(conditional) independence assumptions** to shrink the model.

### What a Bayesian network is

#### Definitions

> **Bayesian network (BN)**: A framework for describing complex joint distributions using simple, local distributions (conditional probability distributions). Also called a **directed probabilistic graphical model**.

- BNs describe how variables interact **locally**.
- Local interactions chain together to produce global, indirect interactions.

A real example is a car-insurance cost network, with variables such as age, socio-economic status, risk aversion, driving skill, vehicle properties, accidents, and the resulting costs.

![Car insurance Bayesian network](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/02_Bayesian_Networks_And_Graphical_Models/insurance-network.svg)

*The car-insurance network has 27 variables and 52 arcs: observable driver and car attributes (blue) feed hidden factors (violet) that determine the costs (amber). Each node only needs a CPT over its few parents, not over all 26 other variables.*

### Graphical model notation

#### Definitions

> **Node**: A random variable. It can be assigned (observed) or unassigned (unobserved); observed nodes are shaded.

> **Arc**: A directed edge representing an interaction between variables. Intuitively it indicates direct influence; formally it encodes (the lack of) conditional independence.

- Arcs are directed. It helps to imagine they indicate direct causation, but in general they do not.
- Missing arcs are what carry information: they encode independence assumptions.

![Graphical model notation](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/02_Bayesian_Networks_And_Graphical_Models/cavity-network.svg)

*Weather has no arcs, so it is independent of the rest. Cavity is a common parent of Toothache and Detect, so the two symptoms are independent once Cavity is known.*

### Example networks

![Coin flips and two traffic models](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/02_Bayesian_Networks_And_Graphical_Models/simple-networks.svg)

*Coin flips have no arcs (absolute independence). For traffic, model 1 assumes rain and traffic are independent; model 2 adds the arc $R \rightarrow T$.*

**$N$ independent coin flips.** Nodes $X_1, \dots, X_n$ with no arcs, so there is no interaction: absolute independence.

**Traffic with two variables** ($R$: it rains, $T$: there is traffic):

| Model | Graph | Assumption |
|---|---|---|
| Model 1: independence | $R$ and $T$, no arc | Rain and traffic are independent |
| Model 2: rain causes traffic | $R \rightarrow T$ | Traffic depends on rain |

**Extended traffic** — $T$: traffic, $R$: rain, $L$: low pressure, $D$: roof drips, $S$: sports match, $C$: cavity.

![Extended traffic network](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/02_Bayesian_Networks_And_Graphical_Models/traffic-model.svg)

*Low pressure causes rain; rain causes roof drips and traffic; a sports match also causes traffic. Cavity is unrelated to everything else, so it has no arcs.*

**Alarm network** — $B$: burglary, $E$: earthquake, $A$: alarm goes off, $J$: John calls, $M$: Mary calls.

![Alarm network](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/02_Bayesian_Networks_And_Graphical_Models/alarm-network.svg)

*Burglary and earthquake can each set off the alarm; the alarm prompts John and Mary to call. Each node stores one CPT over its parents.*

### Probabilities in Bayesian networks

#### Definitions

> **Directed acyclic graph (DAG)**: A directed graph with no directed cycles. In a BN each node represents a random variable $X$.

> **Parents**: The nodes $A_1, \dots, A_n$ with incoming edges to $X$.

> **Conditional probability table (CPT)**: The local distribution $P(X \mid A_1, \dots, A_n)$: one distribution $P(X \mid a_1, \dots, a_n)$ for each combination of parent values.

A Bayesian network consists of:

1. A DAG, with one node per random variable.
2. A local conditional distribution for each node given its parents, stored as a CPT.

A CPT can be thought of as describing a noisy "causal" process from parents to child.

![A node and its CPT](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/02_Bayesian_Networks_And_Graphical_Models/cpt-node.svg)

*Node $X$ with parents $A_1, \dots, A_n$ stores one distribution $P(X \mid a_1, \dots, a_n)$ for every combination of parent values.*

BNs **implicitly** encode the joint as the product of local conditionals. To get the probability of a full assignment, multiply the relevant conditional probabilities:

$$
P(x_1, x_2, \dots, x_n) = \prod_{i=1}^{n} P(x_i \mid \text{parents}(X_i))
$$

Example on the Cavity network ($\text{Cavity} \rightarrow \text{Toothache}$, $\text{Cavity} \rightarrow \text{Detect}$):

$$
P(+\text{cavity}, +\text{detect}, -\text{toothache}) = P(+\text{cavity})\,P(-\text{toothache} \mid +\text{cavity})\,P(+\text{detect} \mid +\text{cavity})
$$

### Why the product defines a valid joint

1. The chain rule holds for **all** distributions:

$$
P(x_1, \dots, x_n) = \prod_{i=1}^{n} P(x_i \mid x_1, \dots, x_{i-1})
$$

2. Order the nodes **topologically** (parents before children) and assume the BN's conditional independences — each variable depends only on its parents among its predecessors:

$$
P(x_i \mid x_1, \dots, x_{i-1}) = P(x_i \mid \text{parents}(X_i))
$$

3. Substituting gives the BN product:

$$
P(x_1, \dots, x_n) = \prod_{i=1}^{n} P(x_i \mid \text{parents}(X_i))
$$

> [!warning] <span style="color: #ff939b">Topology restricts what a BN can represent</span>
> Not every BN can represent every joint distribution. The topology enforces certain conditional independences, so a BN can only represent distributions consistent with them.

### Worked network examples

**Coin flips** — no arcs, each $P(X_i)$ is $h = 0.5$, $t = 0.5$:

$$
P(h, h, t, h) = 0.5 \cdot 0.5 \cdot 0.5 \cdot 0.5 = 0.0625
$$

**Alarm network CPTs:**

| $B$ | $P(B)$ |
|---|---|
| $+b$ | 0.001 |
| $-b$ | 0.999 |

| $E$ | $P(E)$ |
|---|---|
| $+e$ | 0.002 |
| $-e$ | 0.998 |

| $B$ | $E$ | $P(+a \mid B, E)$ | $P(-a \mid B, E)$ |
|---|---|---|---|
| $+b$ | $+e$ | 0.95 | 0.05 |
| $+b$ | $-e$ | 0.94 | 0.06 |
| $-b$ | $+e$ | 0.29 | 0.71 |
| $-b$ | $-e$ | 0.001 | 0.999 |

| $A$ | $P(+j \mid A)$ | $P(-j \mid A)$ |
|---|---|---|
| $+a$ | 0.9 | 0.1 |
| $-a$ | 0.05 | 0.95 |

| $A$ | $P(+m \mid A)$ | $P(-m \mid A)$ |
|---|---|---|
| $+a$ | 0.7 | 0.3 |
| $-a$ | 0.01 | 0.99 |

For example, the probability of a burglary with no earthquake, the alarm going off, and both calling:

$$
P(+b, -e, +a, +j, +m) = P(+b)\,P(-e)\,P(+a \mid +b, -e)\,P(+j \mid +a)\,P(+m \mid +a) = 0.001 \times 0.998 \times 0.94 \times 0.9 \times 0.7
$$

**Traffic, $R \rightarrow T$:**

| $R$ | $P(R)$ |
|---|---|
| $+r$ | $1/4$ |
| $-r$ | $3/4$ |

| $R$ | $P(+t \mid R)$ | $P(-t \mid R)$ |
|---|---|---|
| $+r$ | $3/4$ | $1/4$ |
| $-r$ | $1/2$ | $1/2$ |

Multiplying gives the joint, e.g. $P(+r, -t) = \frac{1}{4} \cdot \frac{1}{4} = \frac{1}{16}$:

| $R$ | $T$ | $P(R, T)$ |
|---|---|---|
| $+r$ | $+t$ | $3/16$ |
| $+r$ | $-t$ | $1/16$ |
| $-r$ | $+t$ | $6/16$ |
| $-r$ | $-t$ | $6/16$ |

**Different topology, same joint ($T \rightarrow R$):**

| $T$ | $P(T)$ |
|---|---|
| $+t$ | $9/16$ |
| $-t$ | $7/16$ |

| $T$ | $P(+r \mid T)$ | $P(-r \mid T)$ |
|---|---|---|
| $+t$ | $1/3$ | $2/3$ |
| $-t$ | $1/7$ | $6/7$ |

Multiplying these out gives exactly the same four joint entries.

![Two topologies, same joint](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/02_Bayesian_Networks_And_Graphical_Models/same-joint-topologies.svg)

*$R \rightarrow T$ and $T \rightarrow R$ use different CPTs but produce the identical joint $P(R, T)$: arc direction is not causality.* Two networks with different arc directions can represent the same distribution.

### Bayesian networks and causality

- Arc direction does **not** necessarily imply causality.
- When BNs reflect the true causal patterns they are often simpler, easier to reason with, and easier to elicit from experts.
- In domains without causality, the arrows reflect correlation.
- The topology really encodes **conditional independence**, which may happen to correspond to causal structure.

### Size and uses of a Bayesian network

| Representation | Size for $N$ Boolean variables |
|---|---|
| Full joint distribution | $2^N$ |
| BN with up to $k$ parents per node | $O(N \cdot 2^{k+1})$ |

Each node's CPT has $2^k$ parent combinations, each with 2 values of the node itself, giving $2^{k+1}$ entries per node.

Advantages over the full joint:

- Substantial space saving.
- Local CPTs are easier to elicit.
- Inference is also faster.

A BN is an efficient encoding of a probabilistic model of a domain. Three questions organize the rest of the module:

| Task | Question |
|---|---|
| **Inference** | Given a fixed BN, what is $P(X \mid e)$? |
| **Representation** | Given a BN graph, what kinds of distributions can it encode? |
| **Modelling** | What BN is most appropriate for a given domain? |

When modelling a domain, understand which assumptions the BN design is making.
