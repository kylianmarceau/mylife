---
tags:
  - advanced-programming
---

# Transform And Conquer

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)  
**Source**: [6 - TOA Transform and Conquer.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/6%20-%20TOA%20Transform%20and%20Conquer.pdf), Patrick Marais, University of Cape Town, PDF pages 1–27  
**Generated**: 2026-10-02

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes. Examples and corrections appear beside the relevant concept.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Transformation Types|Transformation Types]]
  - [[#Gaussian Elimination|Gaussian Elimination]]
  - [[#Presorting And Selection|Presorting And Selection]]
  - [[#Balanced Trees And Heaps|Balanced Trees And Heaps]]
  - [[#Horner's Rule For Polynomial Evaluation|Horner's Rule For Polynomial Evaluation]]
  - [[#Binary Exponentiation Through Representation Change|Binary Exponentiation Through Representation Change]]
  - [[#LCM And Optimisation Reductions|LCM And Optimisation Reductions]]
  - [[#Reducing River Crossing To A Graph|Reducing River Crossing To A Graph]]

---

## Core Content

### Transformation Types

#### Definitions

> **Transform and conquer**: Transform an instance into a more useful instance, representation or problem, solve it, and recover the required answer.

| Type | What changes | Examples |
|---|---|---|
| **Instance simplification** | A more convenient instance of the same problem | Presorting; Gaussian elimination |
| **Representation change** | How the same instance is stored or expressed | Balanced trees; heaps; Horner's rule; binary exponentiation |
| **Problem reduction** | The problem being solved | LCM via GCD; optimisation sign changes; graph reductions |

![Transform and conquer alternatives](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/06_Transform_And_Conquer/transform-types.svg)

*Three transformation routes lead to a solvable representation, followed by recovery of the original answer.*

Benefits include access to powerful data structures and relationships between problem complexities. Finding a useful reduction can be difficult, and transformation overhead belongs in total cost.

### Gaussian Elimination

#### Definitions

> **Gaussian elimination**: Transform a linear system by row operations into an equivalent upper-triangular system.

> **Upper-triangular matrix**: A matrix with zero entries below its main diagonal.

> **Back substitution**: Solve a triangular system from its final equation upward, using already known variables.

For $A\mathbf{x}=\mathbf{b}$, row operations transform both the coefficient matrix and right-hand side to $U\mathbf{x}=\mathbf{y}$:

$$
U=\begin{bmatrix}
u_{11}&u_{12}&u_{13}&u_{14}\\
0&u_{22}&u_{23}&u_{24}\\
0&0&u_{33}&u_{34}\\
0&0&0&u_{44}
\end{bmatrix}.
$$

1. Choose a nonzero pivot in each current column; swap rows when needed.
2. For each lower row, subtract a multiple of the pivot row to eliminate its current-column coefficient.
3. Apply the same operations to the right-hand side.
4. Solve the triangular system from the last variable upward.

$$
x_i=\frac{y_i-\sum_{j=i+1}^{n}u_{ij}x_j}{u_{ii}}.
$$

The system must have appropriate nonzero pivots for a unique solution; singular systems need separate treatment. Partial pivoting also helps reduce numerical instability.

| Stage | Cost |
|---|---|
| Forward elimination | $\Theta(n^3)$ |
| Back substitution | $\Theta(n^2)$ |
| Total | $\Theta(n^3)$ |

### Presorting And Selection

#### Definitions

> **Presorting**: Sort data as preprocessing so that the remaining task becomes easier.

For efficient comparison sorting, the preprocessing cost is $\Theta(n\log n)$. Include that cost before deciding whether the transformed solution is worthwhile.

| Task | Direct or alternative cost | Presorting approach | Decision for one query |
|---|---|---|---|
| Closest pair | Brute force $\Theta(n^2)$ | Sort then geometric divide and conquer, $\Theta(n\log n)$ | Useful |
| Uniqueness | Pair checking $\Theta(n^2)$ | Sort then adjacent scan, $\Theta(n\log n)$ | Useful |
| Minimum and maximum | Scan $\Theta(n)$ | Sort then endpoints, $\Theta(n\log n)$ | Scan is cheaper |
| Median / general rank | Simple repeated-selection baseline $\Theta(n^2)$ | Sort then rank lookup, $\Theta(n\log n)$ | Improves baseline; expected-linear quickselect can do better |
| Single key search | Scan $\Theta(n)$ | Sort then binary search, $\Theta(n\log n)$ overall | Scan is cheaper |

For repeated queries, sorting can be reused. A sorted list allows each subsequent binary search in logarithmic time, which can justify the initial overhead.

The $k$th smallest entry is $A[k]$ under one-based indexing after sorting, or $A[k-1]$ under zero-based indexing. Sorting also makes all of the first $k$ values readily available in order.

Quickselect instead partitions and follows only the target side. Its usual expected and best costs are $\Theta(n)$, and its worst cost is $\Theta(n^2)$. Use a simple scan for minimum or maximum.

### Balanced Trees And Heaps

#### Definitions

> **Balanced search tree**: A search tree whose height is maintained logarithmic in its number of entries.

> **Heap**: A tree-shaped priority structure whose parent-child key relationships expose an extreme key at the root.

The lecture names these representation-change examples as prior CS2 material. A balanced search tree supports key search, insertion and deletion in logarithmic time under its balancing guarantees.

A binary heap supports extreme-key lookup in constant time and extraction or insertion in logarithmic time. Building a heap can take linear time, followed by logarithmic extraction per entry for $\Theta(n\log n)$ heapsort.

| Representation | Main benefit | Qualification |
|---|---|---|
| Balanced search tree | Ordered key operations | Maintaining balance has a cost |
| Heap | Repeated minimum/maximum extraction | Does not provide general binary-search-tree ordering |

### Horner's Rule For Polynomial Evaluation

#### Definitions

> **Horner's rule**: Evaluate a polynomial using nested multiplication and addition rather than computing each power separately.

$$
p(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0
=\bigl(\cdots((a_nx+a_{n-1})x+a_{n-2})x+\cdots\bigr)x+a_0.
$$

```java
Horner(coefficients, x):
    n = length(coefficients) - 1
    p = coefficients[n]
    for i = n - 1 downto 0:
        p = x * p + coefficients[i]
    return p
```

Coefficients are indexed by power in this pseudocode. A presentation listing highest-degree coefficients first must reverse its traversal convention.

For $2x^4-x^3+3x^2+x-5$:

$$
p(x)=(((2x-1)x+3)x+1)x-5,\qquad p(3)=160.
$$

For the cubic source example $2x^3-x^2-6x+5$ at $x=3$:

| Coefficient consumed | Accumulator |
|---|---:|
| $2$ | $2$ |
| $-1$ | $2\cdot3-1=5$ |
| $-6$ | $5\cdot3-6=9$ |
| $5$ | $9\cdot3+5=32$ |

A degree-$n$ polynomial takes exactly $n$ multiplications and $n$ additions/subtractions:

$$
M(n)=A(n)=\sum_{i=0}^{n-1}1=n\in\Theta(n).
$$

Independently computing every power by repeated multiplication gives $\Theta(n^2)$ work for a dense polynomial. Reusing consecutive powers is another linear alternative; Horner's rule offers a particularly simple linear evaluation.

A sparse polynomial such as $x^n$ has no dense sequence of nonzero coefficients to exploit; binary exponentiation can be preferable to running Horner through every zero coefficient.

### Binary Exponentiation Through Representation Change

#### Definitions

> **Binary representation**: An integer written as a sum of powers of two with bit coefficients.

For a positive exponent with bits $b_k\cdots b_0$:

$$
n=\sum_{i=0}^{k}b_i2^i,\qquad b_i\in\{0,1\},\quad b_k=1.
$$

Applying Horner to those bits builds a partial exponent through $q\leftarrow2q+b_i$. The corresponding power update is:

$$
a^{2q+b_i}=(a^q)^2a^{b_i}.
$$

```java
BinaryPower(a, n):
    if n == 0: return 1
    bits = binary representation of n, highest bit first
    result = a
    for each bit after the leading one:
        result = result * result
        if bit == 1: result = result * a
    return result
```

For $n=13=(1101)_2$:

| Next bit | Partial exponent | Power accumulator |
|---|---:|---|
| Leading $1$ | $1$ | $a$ |
| $1$ | $3$ | $a^3$ |
| $0$ | $6$ | $a^6$ |
| $1$ | $13$ | $a^{13}$ |

There are $\lfloor\log_2n\rfloor$ bits after the leading one, each requiring one squaring and at most one extra multiplication:

$$
\lfloor\log_2n\rfloor\le M(n)\le2\lfloor\log_2n\rfloor.
$$

Thus arithmetic-operation count is $\Theta(\log n)$. The source exponent thirteen requires five multiplications: three squarings and two extra multiplications.

### LCM And Optimisation Reductions

#### Definitions

> **Least common multiple (LCM)**: The smallest positive integer divisible by both given positive integers.

> **Reduction**: Transform a problem into another problem so that its solution can be used to solve the original.

$$
\operatorname{lcm}(m,n)=\frac{mn}{\gcd(m,n)}.
$$

For $m=24,n=60$, Euclid returns $12$, so the LCM is $1440/12=120$. In fixed-width arithmetic, dividing before multiplying can reduce avoidable intermediate overflow:

$$
\operatorname{lcm}(m,n)=\left(\frac{m}{\gcd(m,n)}\right)n.
$$

Minimisation and maximisation can be related by sign changes:

$$
\min_x f(x)=-\max_x(-f(x)).
$$

Use the same feasible domain. The transformation changes the objective's sign while retaining the location of an optimal solution.

### Reducing River Crossing To A Graph

#### Definitions

> **State-space graph**: A graph whose vertices are valid configurations and whose edges are allowed transitions.

The peasant $P$ must ferry a wolf $w$, goat $g$ and cabbage $c$. The boat carries the peasant and at most one item. The wolf and goat, or goat and cabbage, cannot be left together on a bank without the peasant.

1. Represent a state by which bank contains each participant.
2. Retain only safe states.
3. Connect states when the peasant crosses, alone or with one item, producing another safe state.
4. Find a path from everyone-left to everyone-right.
5. Use BFS when each crossing has equal cost and the shortest crossing sequence is required.

![Complete safe river-crossing state graph](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/06_Transform_And_Conquer/river-crossing.svg)

*All ten safe states and their reversible legal crossings represent the original puzzle.*

A seven-crossing solution is:

| Step | Move | Left bank after move | Right bank after move |
|---:|---|---|---|
| $0$ | Initial | $P,w,g,c$ | Empty |
| $1$ | Take goat right | $w,c$ | $P,g$ |
| $2$ | Return alone | $P,w,c$ | $g$ |
| $3$ | Take wolf right | $c$ | $P,w,g$ |
| $4$ | Bring goat left | $P,g,c$ | $w$ |
| $5$ | Take cabbage right | $g$ | $P,w,c$ |
| $6$ | Return alone | $P,g$ | $w,c$ |
| $7$ | Take goat right | Empty | $P,w,g,c$ |

Exchanging wolf and cabbage gives another shortest solution. The reduction preserves legal moves and solutions, while making graph-search algorithms applicable.
