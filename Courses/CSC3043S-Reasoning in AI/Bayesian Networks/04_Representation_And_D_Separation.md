---
tags:
  - reasoning-in-ai
---

# Bayesian Networks: Representation and D-Separation

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Bayesian Networks  
> **Source**: [4-BayesianNetworks-Representation.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/Bayesian%20Networks/4-BayesianNetworks-Representation.pdf), Dr Jan Buys, slides 1-14 (based on Klein and Abbeel, CS188 UC Berkeley)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Conditional independence in a Bayesian network|Conditional independence in a Bayesian network]]
  - [[#Implied independences: a chain example|Implied independences: a chain example]]
  - [[#The three canonical triples|The three canonical triples]]
  - [[#Case 1: causal chain|Case 1: causal chain]]
  - [[#Case 2: common cause|Case 2: common cause]]
  - [[#Case 3: common effect (v-structure)|Case 3: common effect (v-structure)]]
  - [[#Active and inactive paths|Active and inactive paths]]
  - [[#The d-separation algorithm|The d-separation algorithm]]
  - [[#D-separation examples|D-separation examples]]

---

## Core Content

### Conditional independence in a Bayesian network

#### Definitions

> **Conditional independence**: $X$ is conditionally independent of $Y$ given $Z$ when $\forall x, y, z : P(x \mid z, y) = P(x \mid z)$, written $X \perp\!\!\!\perp Y \mid Z$.

Conditional independence is a property of a **distribution**. Defining a BN makes one assumption per node — each variable depends only on its parents given its predecessors in a topological order:

$$
P(x_i \mid x_1, \dots, x_{i-1}) = P(x_i \mid \text{parents}(X_i))
$$

There may be **additional** conditional independences in the distribution beyond these. D-separation reads them off the graph.

### Implied independences: a chain example

Consider the chain $X \rightarrow Y \rightarrow Z \rightarrow W$. Compare the chain rule with the BN joint:

$$
P(X)P(Y \mid X)P(Z \mid X, Y)P(W \mid X, Y, Z) = P(X)P(Y \mid X)P(Z \mid Y)P(W \mid Z)
$$

![Chain X to W](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/04_Representation_And_D_Separation/chain-example.svg)

*In the chain $X \rightarrow Y \rightarrow Z \rightarrow W$, each node depends only on its immediate predecessor.*

Matching factors gives independences directly from the BN definition:

- $Z \perp\!\!\!\perp X \mid Y$
- $W \perp\!\!\!\perp X, Y \mid Z$

An additional implied independence, not stated directly by any single factor:

- $W \perp\!\!\!\perp X \mid Y$

### The three canonical triples

#### Definitions

> **D-separation**: A procedure for deriving conditional independences from a Bayesian network graph.

D-separation considers variable triples and decides whether they are (conditionally) independent. Any graph can be analyzed using three cases.

![Canonical triples](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/04_Representation_And_D_Separation/canonical-triples.svg)

*The three lecture examples: a causal chain (low pressure → rain → traffic), a common cause (project due → forums busy, lab full), and a common effect (raining, sports match → traffic).*

| Case | Structure | Without evidence on $Y$ | Given $Y$ |
|---|---|---|---|
| Causal chain | $X \rightarrow Y \rightarrow Z$ | Dependence possible | $X \perp\!\!\!\perp Z \mid Y$ |
| Common cause | $X \leftarrow Y \rightarrow Z$ | Dependence possible | $X \perp\!\!\!\perp Z \mid Y$ |
| Common effect | $X \rightarrow Z \leftarrow Y$ | $X \perp\!\!\!\perp Y$ | Dependence possible |

### Case 1: causal chain

$X$: low pressure → $Y$: rain → $Z$: traffic. The joint is $P(x, y, z) = P(x)P(y \mid x)P(z \mid y)$.

- We **cannot** guarantee that $X$ is independent of $Z$.
- We **can** say $X$ is independent of $Z$ given $Y$:

$$
P(z \mid x, y) = \frac{P(x, y, z)}{P(x, y)} = \frac{P(x)P(y \mid x)P(z \mid y)}{P(x)P(y \mid x)} = P(z \mid y)
$$

Evidence along the chain "blocks" the influence.

### Case 2: common cause

$Y$: project due is the parent of $X$: forums busy and $Z$: lab full. The joint is $P(x, y, z) = P(y)P(x \mid y)P(z \mid y)$.

- We **cannot** guarantee that $X$ is independent of $Z$.
- We **can** say $X$ and $Z$ are independent given $Y$:

$$
P(z \mid x, y) = \frac{P(x, y, z)}{P(x, y)} = \frac{P(y)P(x \mid y)P(z \mid y)}{P(y)P(x \mid y)} = P(z \mid y)
$$

Observing the cause blocks the influence between the effects.

### Case 3: common effect (v-structure)

#### Definitions

> **V-structure (collider)**: A triple $X \rightarrow Z \leftarrow Y$ where two arcs meet head-to-head at $Z$.

$X$: raining and $Y$: sports match are both parents of $Z$: traffic. The joint is $P(x, y, z) = P(x)P(y)P(z \mid x, y)$.

- $X$ **is** independent of $Y$: $P(x \mid y) = P(x)$.
- $X$ and $Y$ are **not** conditionally independent given $Z$.

This is backwards from the other two cases. Observing an effect activates influence between its possible causes, because they are **two competing explanations**. If traffic is heavy and you learn there is a sports match, rain becomes less likely.

### Active and inactive paths

#### Definitions

> **Active path**: An undirected path between two nodes along which influence can flow given the evidence. A path is active only if **every** triple on it is active.

> **Inactive (blocked) path**: A path containing at least one inactive triple. A single inactive segment blocks the whole path.

To ask whether $X$ and $Y$ are conditionally independent given evidence $Z$, shade the evidence nodes and consider all undirected paths from $X$ to $Y$. **No active paths means independence.**

> [!warning] <span style="color: #ff939b">A blocked-by-shading rule is not enough</span>
> A first attempt — "two nodes are independent if every path is blocked by an observed node" — works for chains and forks but fails for v-structures, where observing the middle node *opens* the path. Paths must be checked triple by triple.

![Active and inactive triples](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/04_Representation_And_D_Separation/active-inactive-triples.svg)

*Chains and forks are active only when the middle node is unobserved. A v-structure is the opposite: it becomes active when the middle node or any descendant is observed (shaded).*

| Triple type | Active when | Inactive when |
|---|---|---|
| Causal chain $A \rightarrow B \rightarrow C$ (either direction) | $B$ unobserved | $B$ observed |
| Common cause $A \leftarrow B \rightarrow C$ | $B$ unobserved | $B$ observed |
| Common effect $A \rightarrow B \leftarrow C$ | $B$ **or one of its descendants** observed | $B$ and all its descendants unobserved |

### The d-separation algorithm

Query: $X_i \perp\!\!\!\perp X_j \mid \{X_{k_1}, \dots, X_{k_n}\}$?

1. Shade the evidence nodes $X_{k_1}, \dots, X_{k_n}$.
2. Enumerate all (undirected) paths between $X_i$ and $X_j$.
3. For each path, check every consecutive triple against the active/inactive table.
4. If one or more paths are active, independence is **not guaranteed**.
5. If **all** paths are inactive, independence **is guaranteed**.

Running d-separation over all queries gives a complete list of conditional independences for a BN. That list determines the set of probability distributions the BN can represent.

### D-separation examples

**Example 1** — $R \rightarrow T \leftarrow B$, $T \rightarrow T'$.

![D-separation example 1](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/04_Representation_And_D_Separation/dsep-example-1.svg)

*With a collider at $T$, $R$ and $B$ are independent until $T$ or its descendant $T'$ is observed.*

| Query | Answer | Reason |
|---|---|---|
| $R \perp\!\!\!\perp B$ | Yes | Collider at $T$ is unobserved |
| $R \perp\!\!\!\perp B \mid T$ | No | Observing the collider activates it |
| $R \perp\!\!\!\perp B \mid T'$ | No | Observing a descendant of the collider activates it |

**Example 2** — add $L \rightarrow R$ and $R \rightarrow D$ to example 1.

![Extended traffic network](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/04_Representation_And_D_Separation/extended-traffic.svg)

*$L \rightarrow R$, $R \rightarrow D$, $R \rightarrow T \leftarrow B$, $T \rightarrow T'$. The collider at $T$ connects $R$ and $B$ when $T$ or $T'$ is observed, but observing $R$ blocks the chain from $L$.*

| Query | Answer | Reason |
|---|---|---|
| $L \perp\!\!\!\perp T' \mid T$ | Yes | Chain $R \rightarrow T \rightarrow T'$ blocked by observed $T$ |
| $L \perp\!\!\!\perp B$ | Yes | Collider at $T$ unobserved |
| $L \perp\!\!\!\perp B \mid T$ | No | Collider at $T$ observed; chain $L \rightarrow R \rightarrow T$ active |
| $L \perp\!\!\!\perp B \mid T'$ | No | Descendant of collider observed |
| $L \perp\!\!\!\perp B \mid T, R$ | Yes | Observed $R$ blocks the chain $L \rightarrow R \rightarrow T$ |

**Example 3** — $R$: raining, $T$: traffic, $D$: roof drips, $S$: I'm sad. $R \rightarrow T$, $R \rightarrow D$, $T \rightarrow S$, $D \rightarrow S$.

![Rain, traffic, drips, and sadness](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/04_Representation_And_D_Separation/rain-traffic-drips.svg)

*There are two paths between $T$ and $D$: a fork through $R$ and a collider through $S$. Each query depends on which of these is open.*

| Query | Answer | Reason |
|---|---|---|
| $T \perp\!\!\!\perp D$ | No | Fork through unobserved $R$ is active |
| $T \perp\!\!\!\perp D \mid R$ | Yes | Fork blocked by $R$; collider at $S$ unobserved |
| $T \perp\!\!\!\perp D \mid R, S$ | No | Observing $S$ activates the collider path |
