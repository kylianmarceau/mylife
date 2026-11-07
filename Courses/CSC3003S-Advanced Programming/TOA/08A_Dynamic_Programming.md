---
tags:
  - advanced-programming
---

# Dynamic Programming I

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)
**Source**: [8 - TOA Dynamic Programming-A.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/8%20-%20TOA%20Dynamic%20Programming-A.pdf), Patrick Marais, University of Cape Town, pages 1–22
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> The dynamic programming principle, then Fibonacci, coin-row, change-making, robot coin collection, and Warshall's transitive closure.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Dynamic Programming Is|What Dynamic Programming Is]]
  - [[#Fibonacci With Dynamic Programming|Fibonacci With Dynamic Programming]]
  - [[#Coin-Row Problem|Coin-Row Problem]]
  - [[#Change-Making Problem|Change-Making Problem]]
  - [[#Coin-Collecting Robot|Coin-Collecting Robot]]
  - [[#Transitive Closure|Transitive Closure]]
  - [[#Warshall's Algorithm|Warshall's Algorithm]]
  - [[#Warshall Worked Example|Warshall Worked Example]]

---

## Core Content

### What Dynamic Programming Is

#### Definitions

> **Dynamic programming (DP)**: A general algorithm design technique, invented by the American mathematician Richard Bellman in the 1950s to solve optimisation problems. "Programming" here means "planning".

> **Overlapping subproblems**: Smaller instances that recur many times when the problem is broken down recursively.

> **Principle of optimality**: An optimal solution to the overall problem can be derived from optimal solutions to its sub-instances.

DP solves problems by storing optimal solutions to overlapping subproblems:

- Each subproblem is solved only once and stored for lookup, so DP is a **space–time trade-off**.
- The solution is derived from a **recurrence relation** that specifies how a solution builds on smaller ones.
- The problem must obey the **principle of optimality**.

Algorithms in this course:

| Group | Algorithms |
|---|---|
| Introductory | Fibonacci; change-making; coin collecting (coin-row and robot) |
| Graphs | Transitive closure (Warshall); all-pairs shortest paths (Floyd) |
| Optimisation | Knapsack problem |

### Fibonacci With Dynamic Programming

$$
F(n) = F(n-1) + F(n-2)
$$

| Brute force | Dynamic programming |
|---|---|
| `fibo(n):` | `fibo(n):` |
| `  if (n == 0) return 0` | `  F[0] = 0` |
| `  if (n == 1) return 1` | `  F[1] = 1` |
| `  return fibo(n-1) + fibo(n-2)` | `  for i = 2 to n do:` |
| | `    F[i] = F[i-1] + F[i-2]` |
| | `  return F[n]` |

The brute-force call tree recomputes the same values; the DP version fills the table $F[0], F[1], \dots, F[n]$ once, left to right.

![Fibonacci recursion and stored answers](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/08A_Dynamic_Programming/fibonacci-dp.svg)

*Repeated subtrees in the recursion become single table lookups in the DP version.*

### Coin-Row Problem

#### Definitions

> **Coin-row problem**: Given a row of $n$ coins with values $c_1, \dots, c_n$, pick up coins with the largest total value, subject to never picking two coins that are adjacent in the original row. (Select first, then pick up simultaneously.)

Let $F(n)$ be the maximum amount that can be picked up from the first $n$ coins. Split the allowed selections into two groups and take the better:

- Selections that include the last coin: $F(n-2) + c_n$ (coin $n-1$ is then excluded).
- Selections without the last coin: $F(n-1)$.

$$
F(0) = 0, \qquad F(1) = c_1, \qquad F(n) = \max\{F(n-2) + c_n,\ F(n-1)\} \quad (n > 1)
$$

Fill $F$ from left to right. Example with $C = [5, 1, 2, 10, 6, 2]$:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $C$ | — | 5 | 1 | 2 | 10 | 6 | 2 |
| $F$ | 0 | 5 | 5 | 7 | 15 | 15 | **17** |

| Step | Calculation |
|---|---|
| $F(2)$ | $\max(1 + 0, 5) = 5$ |
| $F(3)$ | $\max(2 + 5, 5) = 7$ |
| $F(4)$ | $\max(10 + 5, 7) = 15$ |
| $F(5)$ | $\max(6 + 7, 15) = 15$ |
| $F(6)$ | $\max(2 + 15, 15) = 17$ |

**Backtracking** to find which coins were chosen:

1. Start at $F(6) = 17$. It came from the option that adds a coin, $c_6$, which used $F(4)$.
2. $F(4) = 15$ also came from adding a coin, $c_4$, which used $F(2)$.
3. $F(2) = 5$ came from the option without a coin, $F(1)$.
4. $F(1) = c_1$ gives the last coin; stop.

The solution set is $\{c_1, c_4, c_6\}$, worth $5 + 10 + 2 = 17$. To make backtracking easy, store the choice made at each step.

### Change-Making Problem

#### Definitions

> **Change-making problem**: Given coin denominations $d_1 < d_2 < \dots < d_m$ with $d_1 = 1$ and an unlimited supply of each, find exact change for amount $n$ using the minimum number of coins.

For typical denomination sets an efficient greedy algorithm works; DP handles the general case.

Let $F(n)$ be the minimum number of coins adding up to $n$. The last coin added can be any denomination $d_j \le n$:

$$
F(0) = 0, \qquad F(n) = \min_{j:\ n \ge d_j} \{F(n - d_j)\} + 1 \quad (n > 0)
$$

```text
F[0] ← 0
for i ← 1 to n do
    temp ← ∞; j ← 1
    while j ≤ m and i ≥ D[j] do
        temp ← min(F[i − D[j]], temp)
        j ← j + 1
    F[i] ← temp + 1
return F[n]
```

Example: $n = 6$, $D = [1, 3, 4]$.

| $i$ | Calculation | $F[i]$ |
|---|---|---|
| 0 | — | 0 |
| 1 | $\min\{F[0]\} + 1$ | 1 |
| 2 | $\min\{F[1]\} + 1$ | 2 |
| 3 | $\min\{F[2], F[0]\} + 1$ | 1 |
| 4 | $\min\{F[3], F[1], F[0]\} + 1$ | 1 |
| 5 | $\min\{F[4], F[2], F[1]\} + 1$ | 2 |
| 6 | $\min\{F[5], F[3], F[2]\} + 1$ | 2 |

Backtracking from $F[6]$: the minimum came from $F[6-3] = F[3]$, and $F[3]$ from $F[0]$, so the change is two 3-coins. Greedy would choose $4 + 1 + 1$ (three coins), which is worse.

### Coin-Collecting Robot

#### Definitions

> **Robot coin-collecting problem**: An $n \times m$ board has at most one coin per cell. A robot starts at the top-left cell and must reach the bottom-right cell, moving only one cell right or one cell down at each step, and picks up the coin in every cell it visits. Find the maximum number of coins it can collect and its path.

Let $F(i, j)$ be the largest number of coins the robot can bring to cell $(i, j)$. Cell $(i, j)$ can only be reached from the cell above, $(i-1, j)$, or the cell to the left, $(i, j-1)$. The best route to $(i, j)$ is the better of those two, plus any coin at $(i, j)$:

$$
F(i, j) = \max\{F(i-1, j),\ F(i, j-1)\} + c_{ij}, \qquad 1 \le i \le n,\ 1 \le j \le m
$$

where $c_{ij} = 1$ if there is a coin at $(i, j)$ and 0 otherwise, and $F(0, j) = F(i, 0) = 0$.

```text
RobotCoinCollection(C[1..n, 1..m])
// In: coin matrix C (0 or 1); Out: largest number of coins brought to (n, m)
F[1, 1] ← C[1, 1]
for j ← 2 to m do F[1, j] ← F[1, j−1] + C[1, j]
for i ← 2 to n do
    F[i, 1] ← F[i−1, 1] + C[i, 1]
    for j ← 2 to m do
        F[i, j] ← max(F[i−1, j], F[i, j−1]) + C[i, j]
return F[n, m]
```

Example on a $5 \times 6$ board with coins at $(1,5)$, $(2,2)$, $(2,4)$, $(3,4)$, $(3,6)$, $(4,3)$, $(4,6)$, $(5,1)$, $(5,5)$:

| $F$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| 2 | 0 | 1 | 1 | 2 | 2 | 2 |
| 3 | 0 | 1 | 1 | 3 | 3 | 4 |
| 4 | 0 | 1 | 2 | 3 | 3 | 5 |
| 5 | 1 | 1 | 2 | 3 | 4 | **5** |

![Robot coin collection](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/08A_Dynamic_Programming/robot-grid.svg)

*An optimal route collects 5 coins; it is found by tracing back from $F(5, 6)$.*

**Backtracing** the path from $F(n, m)$:

- If $F(i-1, j) > F(i, j-1)$, the robot came from above.
- If $F(i, j-1) > F(i-1, j)$, it came from the left.
- If they are equal, choose either (several optimal paths exist).

| Phase | Efficiency |
|---|---|
| Filling the table | $\Theta(nm)$ time and space |
| Backtracing | $\Theta(n + m)$ |

### Transitive Closure

#### Definitions

> **Adjacency matrix**: The $n \times n$ Boolean matrix with a 1 in row $i$, column $j$ when there is a directed edge from vertex $i$ to vertex $j$.

> **Transitive closure**: For a directed graph with $n$ vertices, the $n \times n$ Boolean matrix $T = \{t_{ij}\}$ with $t_{ij} = 1$ if there is a directed path (of any length) from vertex $i$ to vertex $j$, and 0 otherwise.

Rows are "from" vertices and columns are "to" vertices.

### Warshall's Algorithm

Idea: if you can get from A to B, and from B to C, then you can get from A to C.

A path exists from $i$ to $j$ if and only if there is:

- an edge from $i$ to $j$; or
- a path from $i$ to $j$ through vertex 1; or
- a path through vertices 1 and/or 2; or
- a path through vertices 1, 2 and/or 3; or
- … a path through any of the other vertices.

Warshall's algorithm builds a sequence of matrices $R^{(0)}, R^{(1)}, \dots, R^{(n)} = T$. $R^{(k)}[i, j] = 1$ when there is a path from $i$ to $j$ whose intermediate vertices are all among $1, \dots, k$.

At stage $k$, either a path already existed using only vertices $1, \dots, k-1$, or a new path goes from $i$ to $k$ and from $k$ to $j$:

$$
R^{(k)}[i, j] = R^{(k-1)}[i, j] \ \lor\ \big(R^{(k-1)}[i, k] \land R^{(k-1)}[k, j]\big)
$$

```text
R(0) ← adjacency matrix
for k ← 1 to n do
    for i ← 1 to n do
        for j ← 1 to n do
            R(k)[i,j] ← R(k-1)[i,j] or (R(k-1)[i,k] and R(k-1)[k,j])
return R(n)
```

Rule of thumb for hand calculation: at stage $k$, change a 0 to a 1 at $(i, j)$ when row $k$ has a 1 in column $j$ and column $k$ has a 1 in row $i$.

| Measure | Efficiency |
|---|---|
| Time | $\Theta(n^3)$ |
| Space | $\Theta(n^3)$ if all matrices are kept; reducible to $\Theta(n^2)$ by overwriting one matrix |

### Warshall Worked Example

Graph with edges $1 \to 3$, $2 \to 1$, $2 \to 4$, $4 \to 2$:

![Warshall example graph](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/08A_Dynamic_Programming/warshall-graph.svg)

*Four vertices; vertex 3 is a sink, and vertices 2 and 4 form a cycle.*

$$
R^{(0)} = \begin{pmatrix} 0&0&1&0 \\ 1&0&0&1 \\ 0&0&0&0 \\ 0&1&0&0 \end{pmatrix}
\quad
R^{(1)} = \begin{pmatrix} 0&0&1&0 \\ 1&0&\mathbf{1}&1 \\ 0&0&0&0 \\ 0&1&0&0 \end{pmatrix}
$$

$$
R^{(2)} = \begin{pmatrix} 0&0&1&0 \\ 1&0&1&1 \\ 0&0&0&0 \\ \mathbf{1}&1&\mathbf{1}&\mathbf{1} \end{pmatrix}
\quad
R^{(3)} = R^{(2)}
\quad
T = R^{(4)} = \begin{pmatrix} 0&0&1&0 \\ 1&\mathbf{1}&1&1 \\ 0&0&0&0 \\ 1&1&1&1 \end{pmatrix}
$$

| Stage | New paths | Reason |
|---|---|---|
| $R^{(0)}$ | — | Adjacency matrix |
| $R^{(1)}$ (via 1) | $2 \to 3$ | $2 \to 1 \to 3$ |
| $R^{(2)}$ (via 2) | $4 \to 1$, $4 \to 3$, $4 \to 4$ | $4 \to 2$ then anywhere 2 reaches |
| $R^{(3)}$ (via 3) | none | Vertex 3 is a sink (no outgoing edges) |
| $R^{(4)}$ (via 4) | $2 \to 2$ | $2 \to 4 \to 2$ |
