---
tags:
  - reasoning-in-ai
---

# Bayesian Networks: Inference

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Bayesian Networks  
> **Source**: [3-BayesianNets-Inference.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/Bayesian%20Networks/3-BayesianNets-Inference.pdf), Dr Jan Buys, slides 1-20 (based on Klein and Abbeel, CS188 UC Berkeley)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Inference queries on the alarm network|Inference queries on the alarm network]]
  - [[#Inference by enumeration in a Bayesian network|Inference by enumeration in a Bayesian network]]
  - [[#Why enumeration is intractable|Why enumeration is intractable]]
  - [[#Factors|Factors]]
  - [[#Operation 1: join|Operation 1: join]]
  - [[#Operation 2: eliminate|Operation 2: eliminate]]
  - [[#Enumeration versus variable elimination|Enumeration versus variable elimination]]
  - [[#Handling evidence|Handling evidence]]
  - [[#General variable elimination procedure|General variable elimination procedure]]
  - [[#Alarm network with variable elimination|Alarm network with variable elimination]]
  - [[#Elimination order|Elimination order]]

---

## Core Content

### Inference queries on the alarm network

The alarm network has CPTs $P(B)$, $P(E)$, $P(A \mid B, E)$, $P(J \mid A)$, and $P(M \mid A)$.

![Alarm network query](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/03_Bayesian_Network_Inference/alarm-query.svg)

*For $P(B \mid +j, +m)$, $B$ is the query, $J$ and $M$ are observed evidence (shaded), and $E$ and $A$ are hidden variables to sum out.*

Typical queries:

- $P(M)$ — a marginal with no evidence.
- $P(B \mid E)$ — a causal-direction query between two root causes.
- $P(B \mid M)$ — a diagnostic query from an effect back to a cause.

### Inference by enumeration in a Bayesian network

The three enumeration steps from the previous lecture apply directly.

1. **Select** entries consistent with the evidence.
2. **Marginalize** the hidden variables.
3. **Normalize** by $\frac{1}{Z}$.

In a BN, the joint is not stored; each joint entry is built from the CPTs. For $P(B \mid +j, +m)$, with hidden variables $E$ and $A$:

$$
\begin{aligned}
P(B \mid +j, +m) &\propto_B P(B, +j, +m) \\
&= \sum_{e, a} P(B, e, a, +j, +m) \\
&= \sum_{e, a} P(B)\,P(e)\,P(a \mid B, e)\,P(+j \mid a)\,P(+m \mid a)
\end{aligned}
$$

Expanding the sum gives four full products, one for each $(e, a)$ combination:

$$
\begin{aligned}
&P(B)P(+e)P(+a \mid B, +e)P(+j \mid +a)P(+m \mid +a) + P(B)P(+e)P(-a \mid B, +e)P(+j \mid -a)P(+m \mid -a) \\
+\;&P(B)P(-e)P(+a \mid B, -e)P(+j \mid +a)P(+m \mid +a) + P(B)P(-e)P(-a \mid B, -e)P(+j \mid -a)P(+m \mid -a)
\end{aligned}
$$

The result is then multiplied by $\frac{1}{Z}$ to normalize over $B$.

### Why enumeration is intractable

- In a network with many variables (for example the car-insurance network, querying $P(\text{Antilock} \mid \text{observed variables})$), enumeration is not tractable.
- The whole joint is computed ("joined up") **before** the hidden variables are summed out.
- It is more efficient to **interleave** joining and marginalizing.

### Factors

#### Definitions

> **Factor**: Any quantity (table) based on a probability distribution. The initial factors are the local CPTs.

Inference by enumeration can be reframed as operations on factors. The running example is a chain $R \rightarrow T \rightarrow L$ (rain, traffic, late).

*The chain is $R \rightarrow T \rightarrow L$: rain influences traffic, which influences whether you are late ($L$).*

| $R$ | $P(R)$ |
|---|---|
| $+r$ | 0.1 |
| $-r$ | 0.9 |

| $R$ | $T$ | $P(T \mid R)$ |
|---|---|---|
| $+r$ | $+t$ | 0.8 |
| $+r$ | $-t$ | 0.2 |
| $-r$ | $+t$ | 0.1 |
| $-r$ | $-t$ | 0.9 |

| $T$ | $L$ | $P(L \mid T)$ |
|---|---|---|
| $+t$ | $+l$ | 0.3 |
| $+t$ | $-l$ | 0.7 |
| $-t$ | $+l$ | 0.1 |
| $-t$ | $-l$ | 0.9 |

### Operation 1: join

#### Definitions

> **Join**: Combine all factors that mention a joining variable into one new factor over the union of their variables. Each entry is a pointwise product. It works like a database join.

1. Get all factors over the joining variable.
2. Build a new factor over the union of the variables involved.
3. Fill each entry with the product of the matching entries.

**Join on $R$**: $P(R) \times P(T \mid R) \rightarrow P(R, T)$, e.g. $P(+r, +t) = 0.1 \times 0.8 = 0.08$.

| $R$ | $T$ | $P(R, T)$ |
|---|---|---|
| $+r$ | $+t$ | 0.08 |
| $+r$ | $-t$ | 0.02 |
| $-r$ | $+t$ | 0.09 |
| $-r$ | $-t$ | 0.81 |

**Then join on $T$**: $P(R, T) \times P(L \mid T) \rightarrow P(R, T, L)$.

| $R$ | $T$ | $L$ | $P(R, T, L)$ |
|---|---|---|---|
| $+r$ | $+t$ | $+l$ | 0.024 |
| $+r$ | $+t$ | $-l$ | 0.056 |
| $+r$ | $-t$ | $+l$ | 0.002 |
| $+r$ | $-t$ | $-l$ | 0.018 |
| $-r$ | $+t$ | $+l$ | 0.027 |
| $-r$ | $+t$ | $-l$ | 0.063 |
| $-r$ | $-t$ | $+l$ | 0.081 |
| $-r$ | $-t$ | $-l$ | 0.729 |

### Operation 2: eliminate

#### Definitions

> **Eliminate**: Take a factor and sum out (marginalize) a variable. This shrinks the factor and is a projection operation.

Summing $R$ out of $P(R, T)$:

| $T$ | $P(T)$ |
|---|---|
| $+t$ | $0.08 + 0.09 = 0.17$ |
| $-t$ | $0.02 + 0.81 = 0.83$ |

**Multiple elimination** from $P(R, T, L)$: sum out $R$ to get $P(T, L)$, then sum out $T$ to get $P(L)$.

| $T$ | $L$ | $P(T, L)$ |
|---|---|---|
| $+t$ | $+l$ | 0.051 |
| $+t$ | $-l$ | 0.119 |
| $-t$ | $+l$ | 0.083 |
| $-t$ | $-l$ | 0.747 |

| $L$ | $P(L)$ |
|---|---|
| $+l$ | $0.051 + 0.083 = 0.134$ |
| $-l$ | $0.119 + 0.747 = 0.866$ |

### Enumeration versus variable elimination

#### Definitions

> **Variable elimination (VE)**: An inference algorithm that interleaves join and eliminate operations, so that large joint factors are never built unnecessarily.

| Method | Order of operations | Largest factor in the $R \rightarrow T \rightarrow L$ example |
|---|---|---|
| Inference by enumeration | All joins first, then all eliminations | $P(R, T, L)$, 8 entries |
| Variable elimination | Join on a variable, eliminate it, repeat | $P(R, T)$ or $P(T, L)$, 4 entries |

![Enumeration versus variable elimination](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/03_Bayesian_Network_Inference/enumeration-vs-ve.svg)

*Enumeration joins everything into the 8-entry $P(R, T, L)$ before summing. Variable elimination joins and sums out one variable at a time, so no factor exceeds 4 entries.*

VE on the chain:

1. Join $R$: $P(R) \times P(T \mid R) \rightarrow P(R, T)$.
2. Sum out $R$: $P(R, T) \rightarrow P(T)$ $= (0.17, 0.83)$.
3. Join $T$: $P(T) \times P(L \mid T) \rightarrow P(T, L)$ $= (0.051, 0.119, 0.083, 0.747)$.
4. Sum out $T$: $P(T, L) \rightarrow P(L)$ $= (0.134, 0.866)$.

### Handling evidence

If there is evidence, first **select** it in the initial factors, then eliminate every hidden variable, then normalize.

**Example: $P(L \mid +r)$.** With no evidence the initial factors are $P(R)$, $P(T \mid R)$, $P(L \mid T)$. With $+r$ observed they become:

| Factor | Entries kept |
|---|---|
| $P(+r)$ | $+r$: 0.1 |
| $P(T \mid +r)$ | $+t$: 0.8, $-t$: 0.2 |
| $P(L \mid T)$ | unchanged (no $R$ in it) |

1. Eliminate the only hidden variable, $T$: join everything and sum out $T$.
2. The result is a selected joint of query and evidence, $P(+r, L)$: $+l$: $0.026$, $-l$: $0.074$.
3. Normalize: $Z = 0.1$, giving $P(+l \mid +r) = 0.26$ and $P(-l \mid +r) = 0.74$.

### General variable elimination procedure

For a query $P(Q \mid E_1 = e_1, \dots, E_k = e_k)$:

1. Start with initial factors: the local CPTs instantiated with the evidence.
2. While there are still hidden variables (not $Q$ or evidence):
   1. Pick a hidden variable $H$.
   2. Join all factors mentioning $H$.
   3. Eliminate (sum out) $H$.
3. Join all remaining factors and normalize.

```text
VariableElimination(Q, evidence e, BN):
    factors ← CPTs of BN, each restricted to e
    for each hidden variable H (in chosen order):
        F_H ← all factors mentioning H
        f   ← join(F_H)
        f'  ← sum out H from f
        factors ← (factors − F_H) ∪ {f'}
    f ← join(factors)
    return normalize(f)
```

### Alarm network with variable elimination

Query: $P(B \mid j, m) \propto P(B, j, m)$. Initial factors: $P(B)$, $P(E)$, $P(A \mid B, E)$, $P(j \mid A)$, $P(m \mid A)$.

1. **Choose $A$.** Join $P(A \mid B, E)$, $P(j \mid A)$, $P(m \mid A)$ into $P(j, m, A \mid B, E)$, then sum out $A$ to get $P(j, m \mid B, E)$.
2. Remaining factors: $P(B)$, $P(E)$, $P(j, m \mid B, E)$.
3. **Choose $E$.** Join $P(E)$ and $P(j, m \mid B, E)$ into $P(j, m, E \mid B)$, then sum out $E$ to get $P(j, m \mid B)$.
4. Remaining factors: $P(B)$, $P(j, m \mid B)$.
5. **Finally $B$.** Join into $P(j, m, B)$ and normalize to get $P(B \mid j, m)$.

![Variable elimination on the alarm network](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/03_Bayesian_Network_Inference/ve-alarm.svg)

*Eliminating $A$ produces $f_1(B, e, j, m)$; eliminating $E$ produces $f_2(B, j, m)$; joining with $P(B)$ and normalizing gives the answer.*

The same computation in equations:

$$
\begin{aligned}
P(B \mid j, m) &\propto P(B, j, m) \\
&= \sum_{e, a} P(B, j, m, e, a) && \text{marginal from joint by summing out} \\
&= \sum_{e, a} P(B)P(e)P(a \mid B, e)P(j \mid a)P(m \mid a) && \text{BN joint expression} \\
&= \sum_{e} P(B)P(e) \sum_{a} P(a \mid B, e)P(j \mid a)P(m \mid a) && x(y + z) = xy + xz \\
&= \sum_{e} P(B)P(e)\,f_1(B, e, j, m) && \text{join on } a\text{, sum out gives } f_1 \\
&= P(B) \sum_{e} P(e)\,f_1(B, e, j, m) && x(y + z) = xy + xz \\
&= P(B)\,f_2(B, j, m) && \text{join on } e\text{, sum out gives } f_2
\end{aligned}
$$

> [!tip] <span style="color: #5ad4b5">Why VE is faster</span>
> All VE does is exploit the distributive law, e.g. $uwy + uwz + uxy + uxz + vwy + vwz + vxy + vxz = (u + v)(w + x)(y + z)$. Pushing sums inside products avoids repeated multiplications.

### Elimination order

The elimination order changes the computational cost. Complexity depends critically on the size of the **largest factor** generated (its number of table entries).

**Example query** $P(X_3 \mid Y_1 = y_1, Y_2 = y_2, Y_3 = y_3)$, where $Z$ is the parent of $X_1, X_2, X_3$ and each $X_i$ has an observed child $Y_i$:

| Order | Effect |
|---|---|
| $X_1, X_2, Z$ | Every generated factor has one variable, size 2 |
| $Z$ first | Joining on $Z$ connects its children, giving a factor of size 4 |

![Elimination order](../../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/03_Bayesian_Network_Inference/elimination-order.svg)

*$Z$ is shared by every $X_i$. Eliminating $Z$ first creates one factor over all its children ($2^{n+1}$ entries); eliminating the $X_i$ first keeps every factor at 2 variables.*

**General query** $P(X_n \mid y_1, \dots, y_n)$ on the same structure:

| Order | Largest factor |
|---|---|
| $Z, X_1, \dots, X_{n-1}$ | $n + 1$ variables, $2^{n+1}$ entries |
| $X_1, \dots, X_{n-1}, Z$ | 2 variables, $2^2$ entries |

> [!warning] <span style="color: #ff939b">No guarantee of a good order</span>
> In general, there may be no ordering that only produces small factors.
