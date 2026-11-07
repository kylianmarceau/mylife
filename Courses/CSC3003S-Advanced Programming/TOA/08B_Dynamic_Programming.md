---
tags:
  - advanced-programming
---

# Dynamic Programming II

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)
**Source**: [8 - TOA Dynamic Programming-B.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/8%20-%20TOA%20Dynamic%20Programming-B.pdf), Patrick Marais, University of Cape Town, pages 1–22
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Floyd's all-pairs shortest paths and path extraction, the 0/1 knapsack table and backtracking, and memory functions.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#All-Pairs Shortest Paths|All-Pairs Shortest Paths]]
  - [[#Floyd's Algorithm|Floyd's Algorithm]]
  - [[#Floyd Worked Example|Floyd Worked Example]]
  - [[#Extracting The Shortest Paths|Extracting The Shortest Paths]]
  - [[#The Dynamic Programming Principle Revisited|The Dynamic Programming Principle Revisited]]
  - [[#Knapsack: Subproblems And Recurrence|Knapsack: Subproblems And Recurrence]]
  - [[#Knapsack Worked Example|Knapsack Worked Example]]
  - [[#Recovering The Knapsack Contents|Recovering The Knapsack Contents]]
  - [[#Memory Functions|Memory Functions]]
  - [[#Dynamic Programming Summary|Dynamic Programming Summary]]

---

## Core Content

### All-Pairs Shortest Paths

#### Definitions

> **All-pairs shortest-paths problem**: In a weighted graph (directed or undirected), find the length of the shortest path between every pair of vertices.

The result is like a table of distances between every pair of places on a map. It is used for scheduling airlines and trains, for example. Cast in graph terms, it tells you the shortest path between any two vertices.

Floyd's algorithm solves it with the same idea as Warshall's algorithm.

### Floyd's Algorithm

Floyd's algorithm builds a series of distance matrices $D^{(0)}, D^{(1)}, \dots, D^{(n)}$. $D^{(k)}$ allows only the first $k$ vertices as intermediate vertices.

1. **Initialisation**: $d^{(0)}_{ij} = w_{ij}$, the weighted adjacency matrix (no intermediate vertices). Use $\infty$ where there is no edge and 0 on the diagonal.
2. **Iteration**: for $k \ge 1$,
$$
d^{(k)}_{ij} = \min\left(d^{(k-1)}_{ij},\ d^{(k-1)}_{ik} + d^{(k-1)}_{kj}\right)
$$
3. **Termination**: stop at $k = n$, when all vertices $\{1, \dots, n\}$ may be intermediates.

The best way from $i$ to $j$ using vertices $1..k$ either uses only $1..k-1$, or goes from $i$ to $k$ and then from $k$ to $j$, each part using only $1..k-1$.

```text
D ← W
for k ← 1 to n do
    for i ← 1 to n do
        for j ← 1 to n do
            D[i,j] ← min( D[i,j], D[i,k] + D[k,j] )
return D
```

| Measure | Efficiency |
|---|---|
| Time | $\Theta(n^3)$ |
| Space | $\Theta(n^2)$ (one matrix updated in place) |

Hand-calculation rule: at stage $k$, for each $(i, j)$ take the minimum of the current entry and (row $i$'s entry in column $k$) + (row $k$'s entry in column $j$).

### Floyd Worked Example

Directed graph with edges $1 \to 3$ (4), $2 \to 1$ (1), $2 \to 3$ (6), $2 \to 4$ (3), $4 \to 2$ (5), $4 \to 3$ (1):

![Floyd example graph](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/08B_Dynamic_Programming/floyd-graph.svg)

*Edge weights for the Floyd example; vertex 3 has no outgoing edges.*

$$
D^{(0)} = W = \begin{pmatrix} 0&\infty&4&\infty \\ 1&0&6&3 \\ \infty&\infty&0&\infty \\ \infty&5&1&0 \end{pmatrix}
\qquad
D^{(1)} = \begin{pmatrix} 0&\infty&4&\infty \\ 1&0&\mathbf{5}&3 \\ \infty&\infty&0&\infty \\ \infty&5&1&0 \end{pmatrix}
$$

$$
D^{(2)} = D^{(3)} = \begin{pmatrix} 0&\infty&4&\infty \\ 1&0&5&3 \\ \infty&\infty&0&\infty \\ \mathbf{6}&5&1&0 \end{pmatrix}
\qquad
D = D^{(4)} = \begin{pmatrix} 0&\infty&4&\infty \\ 1&0&\mathbf{4}&3 \\ \infty&\infty&0&\infty \\ 6&5&1&0 \end{pmatrix}
$$

| Stage | Improvement | Reason |
|---|---|---|
| $D^{(1)}$ (via 1) | $d_{23}: 6 \to 5$ | $2 \to 1 \to 3 = 1 + 4$ |
| $D^{(2)}$ (via 2) | $d_{41}: \infty \to 6$ | $4 \to 2 \to 1 = 5 + 1$ |
| $D^{(3)}$ (via 3) | none | Vertex 3 has no outgoing edges |
| $D^{(4)}$ (via 4) | $d_{23}: 5 \to 4$ | $2 \to 4 \to 3 = 3 + 1$ |

### Extracting The Shortest Paths

Dynamic programming often gives the optimal value but not the other information (here, the actual path). That information must be extracted separately.

For Floyd's algorithm, keep an $n \times n$ matrix $P$, initially all zeros. Whenever vertex $k$ reduces a distance, record it:

```text
if (D[i,k] + D[k,j] < D[i,j])
    P[i,j] = k        // intermediate node k used from i to j
```

Then print the path recursively:

```text
// input: matrix P, i = start, j = end
// output: the intermediate nodes on the shortest path from i to j
Algorithm ShortestPath(i, j, P[1..n, 1..n])
    k ← P[i,j]
    if k != 0
        ShortestPath(i, k)
        print(k)
        ShortestPath(k, j)
```

In the example, $P[2,3] = 4$ (last improvement) and $P[2,4] = 0$, so the path from 2 to 3 is $2 \to 4 \to 3$.

### The Dynamic Programming Principle Revisited

1. Construct a table of all subproblem results.
2. Initialise the entries for the smallest subproblems.
3. Fill in the rest in a precise order:
   - corresponding to increasing subproblem size, and
   - using only entries that have already been computed.
4. Each entry is calculated exactly once.
5. The final value computed is the solution to the original problem.

Bottom-up DP uses iteration (plus extra space for saved results), never recursion.

### Knapsack: Subproblems And Recurrence

#### Definitions

> **0/1 knapsack problem**: Fit items with given weights and values into a knapsack of limited weight capacity $W$ so that the total value is maximised. Each item is either taken or not.

![Knapsack packing](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/08B_Dynamic_Programming/knapsack-packing.svg)

*A knapsack packing: the chosen items have total weight 68 and value 215, within capacity.*

**Subproblem**: the first $i$ items ($1 \le i \le n$), with weights $w_1, \dots, w_i$ and values $v_1, \dots, v_i$, and a knapsack of capacity $j$ ($1 \le j \le W$).

**Table**: $V[i, j]$ is the value of the optimal subset of the first $i$ items that fits in capacity $j$. For example, $V[3, 4]$ may contain items up to and including item 3, with capacity 4.

For entry $V[i, j]$ there are two options:

- **Don't include item $i$** (it doesn't fit, or isn't optimal): use the previous optimal packing, $V[i-1, j]$.
- **Include item $i$**: use the optimal packing of the first $i-1$ items in a knapsack smaller by $w_i$, plus $v_i$: $V[i-1, j - w_i] + v_i$.

$$
V[0, j] = 0, \qquad V[i, 0] = 0
$$

$$
V[i, j] =
\begin{cases}
V[i-1, j] & \text{if } j < w_i \\
\max\big(V[i-1, j],\ V[i-1, j - w_i] + v_i\big) & \text{otherwise}
\end{cases}
$$

### Knapsack Worked Example

Capacity $W = 5$:

| Item | Weight | Value |
|---|---|---|
| 1 | $w_1 = 2$ | $v_1 = 12$ |
| 2 | $w_2 = 1$ | $v_2 = 10$ |
| 3 | $w_3 = 3$ | $v_3 = 20$ |
| 4 | $w_4 = 2$ | $v_4 = 15$ |

Fill the table row by row:

| $V[i,j]$ | $j=0$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $i = 0$ | 0 | 0 | 0 | 0 | 0 | 0 |
| $i = 1$ | 0 | 0 | 12 | 12 | 12 | 12 |
| $i = 2$ | 0 | 10 | 12 | 22 | 22 | 22 |
| $i = 3$ | 0 | 10 | 12 | 22 | 30 | 32 |
| $i = 4$ | 0 | 10 | 15 | 25 | 30 | **37** |

Sample entries:

| Entry | Calculation |
|---|---|
| $V[2, 3]$ | $\max(V[1,3],\ V[1,2] + 10) = \max(12, 22) = 22$ |
| $V[3, 4]$ | $\max(V[2,4],\ V[2,1] + 20) = \max(22, 30) = 30$ |
| $V[4, 4]$ | $\max(V[3,4],\ V[3,2] + 15) = \max(30, 27) = 30$ |
| $V[4, 5]$ | $\max(V[3,5],\ V[3,3] + 15) = \max(32, 37) = 37$ |

The maximum value is $V[4, 5] = 37$.

### Recovering The Knapsack Contents

$V[i, j]$ only gives values, not contents, but you can work backwards from $V[n, W]$:

1. If $V[i-1, j] \ne V[i, j]$, item $i$ was included. Continue from $V[i-1, j - w_i]$.
2. Otherwise item $i$ was not included. Continue from $V[i-1, j]$.

| Check | Result | Next cell |
|---|---|---|
| $V[4,5] = 37 \ne V[3,5] = 32$ | Item 4 **in** | $V[3, 3]$ |
| $V[3,3] = 22 = V[2,3] = 22$ | Item 3 **out** | $V[2, 3]$ |
| $V[2,3] = 22 \ne V[1,3] = 12$ | Item 2 **in** | $V[1, 2]$ |
| $V[1,2] = 12 \ne V[0,2] = 0$ | Item 1 **in** | done |

Optimal subset: items $\{1, 2, 4\}$, weight $2 + 1 + 2 = 5$, value $12 + 10 + 15 = 37$.

### Memory Functions

DP applies to recurrence relations with overlapping subproblems. The two classic approaches each have a weakness:

| Approach | Behaviour |
|---|---|
| Top-down (brute-force recursion) | Solves common subproblems more than once — exponential work |
| Bottom-up (dynamic programming) | Calculates each subproblem once, but fills in **all** subproblems, even unneeded ones |
| **Memory function** | Combines both: fill the table with nulls, recurse top-down, and compute an entry only when it is needed and not yet stored |

A memory function is equivalent to **lazy evaluation**.

Knapsack with a memory function (the table starts filled with $-1$ for "null", except row 0 and column 0, which are 0):

```text
sack(i, j)
    if V[i,j] < 0                // -1 means null
        if j < w[i] then val ← sack(i-1, j)
        else val ← max( sack(i-1, j),
                        v[i] + sack(i-1, j-w[i]) )
        V[i,j] ← val
    return V[i,j]
```

Called as `sack(4, 5)` on the example above, only the cells actually reached by the recursion are computed; the rest stay at $-1$.

### Dynamic Programming Summary

- DP is typically applied to a recurrence relation: break a problem into smaller, easier subproblems, and record their results in a table to avoid solving them several times.
- It can only be applied when the **principle of optimality** holds.
- Its biggest limitation is the number of partial solutions that must be stored.
- The memory function combines the strengths of top-down and bottom-up: it does only the needed subproblems, and each only once.
- DP can be hard to formulate. Often simpler greedy approaches do better.
