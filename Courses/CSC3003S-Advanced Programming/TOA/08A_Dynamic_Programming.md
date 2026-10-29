---
tags:
  - advanced-programming
---

# Dynamic Programming A: Fibonacci, Coins And Transitive Closure

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)  
**Source**: [8 - TOA Dynamic Programming-A.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/8%20-%20TOA%20Dynamic%20Programming-A.pdf), Patrick Marais, University of Cape Town, PDF pages 1–22  
**Generated**: 2026-10-02

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes. Examples and corrections appear beside the relevant concept.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Dynamic Programming And Optimal Substructure|Dynamic Programming And Optimal Substructure]]
  - [[#Fibonacci With Stored Results|Fibonacci With Stored Results]]
  - [[#Coin-Row Optimisation|Coin-Row Optimisation]]
  - [[#Minimum-Coin Change Making|Minimum-Coin Change Making]]
  - [[#Robot Coin Collection On A Grid|Robot Coin Collection On A Grid]]
  - [[#Transitive Closure And Warshall's Algorithm|Transitive Closure And Warshall's Algorithm]]
  - [[#Warshall Source Matrix Trace|Warshall Source Matrix Trace]]

---

## Core Content

### Dynamic Programming And Optimal Substructure

#### Definitions

> **Dynamic programming (DP)**: Solve overlapping subproblems once and store their answers for reuse, normally organised by a recurrence.

> **Principle of optimality**: An optimal overall solution can be obtained from optimal solutions to the relevant subinstances.

> **Tabulation**: Fill a table bottom up, calculating each state after its dependencies.

Richard Bellman developed dynamic programming for optimisation in the nineteen-fifties. Programming here means planning. It is also useful for non-optimisation tasks, such as Fibonacci values and Boolean reachability.

1. Define precisely what each stored state means.
2. Identify the alternatives leading to that state.
3. Derive a recurrence and its base cases.
4. Choose an order in which every dependency is already available.
5. Fill the table and read the final state.
6. Store choices or backtrack through values to recover the actual solution.

DP trades memory for reduced repeated work. Optimal substructure must be established for optimisation tasks; arbitrary local solutions do not automatically combine into a global optimum.

### Fibonacci With Stored Results

#### Definitions

> **Overlapping subproblems**: Subproblems appearing repeatedly in the recursive decomposition.

$$
F_0=0,\qquad F_1=1,\qquad F_i=F_{i-1}+F_{i-2}\quad(i\ge2).
$$

```java
FibonacciDP(n):
    if n == 0: return 0
    F[0] = 0; F[1] = 1
    for i = 2 to n:
        F[i] = F[i - 1] + F[i - 2]
    return F[n]
```

| Index | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---:|---:|---:|---:|---:|---:|
| Value | $0$ | $1$ | $1$ | $2$ | $3$ | $5$ |

![Repeated Fibonacci subproblems replaced by stored dependencies](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/08A_Dynamic_Programming/fibonacci-dp.svg)

*The recursive fifth-value tree repeats smaller values; the dependency chain computes each stored value once.*

Naive recursion uses $\Theta(\varphi^n)$ arithmetic operations. Tabulation uses $\Theta(n)$ operations and $\Theta(n)$ stored integers. Keeping only the last two values reduces storage to a constant number of integers; growing integer bit costs must still be counted in a bit-level analysis.

### Coin-Row Optimisation

#### Definitions

> **Coin-row problem**: Choose coins from a fixed row to maximise value without choosing coins adjacent in the original row.

> **State $F(i)$**: Maximum obtainable value from the first $i$ coins.

For positive coin values $c_1,\ldots,c_n$:

$$
F(0)=0,\quad F(1)=c_1,\qquad
F(i)=\max\{F(i-1),F(i-2)+c_i\}\quad(i\ge2).
$$

| Choice | Compatible earlier problem |
|---|---|
| Exclude coin $i$ | First $i-1$ coins |
| Include coin $i$ | First $i-2$ coins, because the adjacent coin is forbidden |

```java
CoinRow(C):
    if length(C) == 0: return 0
    F[0] = 0
    F[1] = C[1]
    for i = 2 to length(C):
        F[i] = max(F[i - 1], F[i - 2] + C[i])
    return F[length(C)]
```

The source values and final table are:

| $i$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Coin $c_i$ | — | $5$ | $1$ | $2$ | $10$ | $6$ | $2$ |
| Best value $F(i)$ | $0$ | $5$ | $5$ | $7$ | $15$ | $15$ | $17$ |

For example, $F(4)=\max(7,5+10)=15$ and $F(6)=\max(15,15+2)=17$.

Recover coins by walking backwards:

1. If $F(i)=F(i-1)$, an optimal solution excludes coin $i$; move to $i-1$.
2. Otherwise include coin $i$ and move to $i-2$.
3. At index one, include it if its value is needed; stop at zero.
4. On ties, either optimal branch can be selected consistently.

The source backtrack is $6\to4\to2\to1$, selecting coins $1,4,6$ with value $5+10+2=17$. Time and full-table space are $\Theta(n)$; value-only rolling storage is constant, while reconstruction needs retained decisions or recomputation.

### Minimum-Coin Change Making

#### Definitions

> **Change-making problem**: Make an exact amount using the fewest coins, with unlimited copies of each allowed denomination.

> **State $F(a)$**: Minimum number of coins needed for amount $a$.

For ascending positive denominations $d_1,\ldots,d_m$, with $d_1=1$ in the source:

$$
F(0)=0,\qquad F(a)=1+\min_{j:d_j\le a}F(a-d_j).
$$

Every possible final coin leaves a smaller exact-change problem. Minimise over all feasible final denominations, not just the largest one.

```java
MinimumCoins(D, n):
    F[0] = 0
    for amount = 1 to n:
        F[amount] = infinity
        choice[amount] = none
        for each denomination d in D with d <= amount:
            if F[amount - d] + 1 < F[amount]:
                F[amount] = F[amount - d] + 1
                choice[amount] = d
    return F[n], choice
```

For $D=\{1,3,4\}$ and $n=6$:

| Amount | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Minimum coins | $0$ | $1$ | $2$ | $1$ | $1$ | $2$ | $2$ |

$$
F(6)=1+\min\{F(5),F(3),F(2)\}=1+\min\{2,1,2\}=2.
$$

The stored choice takes a three-value coin, leaving amount three, then another three. Greedy chooses four, one, one, using three coins; DP finds the optimal pair.

Time is $O(nm)$ and space is $\Theta(n)$ for results and choices. If denomination one is absent, unreachable states remain infinity and reconstruction must detect them. Complexity depends on the numeric amount, rather than merely the number of bits encoding it.

### Robot Coin Collection On A Grid

#### Definitions

> **Robot coin-collection problem**: Move from top-left to bottom-right on a grid, taking only right or down moves, and maximise collected coins.

> **State $F(i,j)$**: Maximum coins collectable on a path ending at cell $(i,j)$.

Let $c_{ij}\in\{0,1\}$ indicate a coin. Each interior cell has only two possible predecessor cells:

$$
F(i,j)=\max\{F(i-1,j),F(i,j-1)\}+c_{ij}.
$$

Initialise the starting cell and cumulative first row and first column:

$$
F(1,1)=c_{11},\quad F(1,j)=F(1,j-1)+c_{1j},\quad
F(i,1)=F(i-1,1)+c_{i1}.
$$

The source's zero-valued virtual row and column also work for this nonnegative coin model. Explicit boundary initialisation makes the allowed moves clearer.

```java
RobotCoins(C, n, m):
    F[1, 1] = C[1, 1]
    for j = 2 to m: F[1, j] = F[1, j - 1] + C[1, j]
    for i = 2 to n:
        F[i, 1] = F[i - 1, 1] + C[i, 1]
        for j = 2 to m:
            F[i, j] = max(F[i - 1, j], F[i, j - 1]) + C[i, j]
    return F[n, m]
```

![Source coin board and an optimal route](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/08A_Dynamic_Programming/robot-grid.svg)

*The five-by-six source board has an optimal right/down route collecting five coins.*

The board has coins at $(1,5),(2,2),(2,4),(3,4),(3,6),(4,3),(4,6),(5,1),(5,5)$. The completed value table is:

| Row / column | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---:|---:|---:|---:|---:|---:|
| $1$ | $0$ | $0$ | $0$ | $0$ | $1$ | $1$ |
| $2$ | $0$ | $1$ | $1$ | $2$ | $2$ | $2$ |
| $3$ | $0$ | $1$ | $1$ | $3$ | $3$ | $4$ |
| $4$ | $0$ | $1$ | $2$ | $3$ | $3$ | $5$ |
| $5$ | $1$ | $1$ | $2$ | $3$ | $4$ | $5$ |

To reconstruct, start at $(n,m)$ and move to the predecessor with the larger table value, choosing either on ties. Boundary cells have only one legal predecessor.

One optimal path is:

$$
(1,1)\to(1,2)\to(2,2)\to(2,3)\to(2,4)\to(3,4)
\to(3,5)\to(3,6)\to(4,6)\to(5,6).
$$

Time and full-table space are $\Theta(nm)$; backtracking takes $\Theta(n+m)$. Rolling-row storage suffices for the value but discards information needed for direct path reconstruction.

### Transitive Closure And Warshall's Algorithm

#### Definitions

> **Transitive closure**: A Boolean matrix indicating whether a directed path exists from each vertex to each other vertex.

> **Adjacency matrix**: A Boolean matrix whose entry is one exactly when the corresponding directed edge exists.

> **State $R^{(k)}[i,j]$**: Whether a path from $i$ to $j$ exists using only vertices in $\{1,\ldots,k\}$ as intermediates.

The recurrence either retains an already known path, or joins a path to the new intermediate with a path from it:

$$
R^{(k)}[i,j]=R^{(k-1)}[i,j]\lor
\left(R^{(k-1)}[i,k]\land R^{(k-1)}[k,j]\right).
$$

Start with $R^{(0)}=A$, the adjacency matrix; finish with $R^{(n)}=T$. The source uses positive-length path reachability: a diagonal becomes one only when a directed cycle returns to that vertex. For reflexive reachability, initialise the diagonal to one as well.

![Warshall source graph and intermediate-path relation](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/08A_Dynamic_Programming/warshall-graph.svg)

*Paths through a newly allowed intermediate extend the reachability relation; vertex three is a sink.*

```java
Warshall(A):
    R = copy of A
    for k = 1 to n:
        for i = 1 to n:
            for j = 1 to n:
                R[i, j] = R[i, j] or (R[i, k] and R[k, j])
    return R
```

Keep the intermediate loop outermost. With Boolean reachability, in-place updates preserve the recurrence because permitting a cycle through the current intermediate does not introduce invalid reachability.

### Warshall Source Matrix Trace

The edges are $1\to3$, $2\to1$, $2\to4$, $4\to2$. Matrices use rows as origins and columns as destinations:

$$
R^{(0)}=\begin{bmatrix}0&0&1&0\\1&0&0&1\\0&0&0&0\\0&1&0&0\end{bmatrix},\qquad
R^{(1)}=\begin{bmatrix}0&0&1&0\\1&0&1&1\\0&0&0&0\\0&1&0&0\end{bmatrix}.
$$

Allowing vertex one adds $2\to3$. Allowing vertex two next adds paths from four to one, three and four:

$$
R^{(2)}=\begin{bmatrix}0&0&1&0\\1&0&1&1\\0&0&0&0\\1&1&1&1\end{bmatrix},\qquad R^{(3)}=R^{(2)}.
$$

Vertex three is a sink, so it creates no new joined paths. Allowing vertex four adds $2\to2$:

$$
T=R^{(4)}=\begin{bmatrix}0&0&1&0\\1&1&1&1\\0&0&0&0\\1&1&1&1\end{bmatrix}.
$$

The cycle between vertices two and four explains their diagonal ones. Vertex one can reach three but cannot return to itself; vertex three reaches no vertex under the positive-length convention.

Time is $\Theta(n^3)$. Storing every stage uses $\Theta(n^3)$ space; the in-place implementation uses $\Theta(n^2)$ matrix space.
