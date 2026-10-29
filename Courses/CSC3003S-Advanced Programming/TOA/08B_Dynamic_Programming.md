---
tags:
  - advanced-programming
---

# Dynamic Programming B: Shortest Paths, Knapsack And Memoisation

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)  
**Source**: [8 - TOA Dynamic Programming-B.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/8%20-%20TOA%20Dynamic%20Programming-B.pdf), Patrick Marais, University of Cape Town, PDF pages 1–22 (printed slides 23–44)  
**Generated**: 2026-10-02

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes. Examples and corrections appear beside the relevant concept.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Floyd's All-Pairs Shortest Paths|Floyd's All-Pairs Shortest Paths]]
  - [[#Floyd Source Matrix Trace|Floyd Source Matrix Trace]]
  - [[#Recovering Floyd Paths|Recovering Floyd Paths]]
  - [[#Zero-One Knapsack State And Recurrence|Zero-One Knapsack State And Recurrence]]
  - [[#Knapsack Source Table And Reconstruction|Knapsack Source Table And Reconstruction]]
  - [[#Memory Functions And Memoisation|Memory Functions And Memoisation]]
  - [[#DP Formulation And Limits|DP Formulation And Limits]]

---

## Core Content

### Floyd's All-Pairs Shortest Paths

#### Definitions

> **All-pairs shortest-path problem**: Find the minimum path cost for every ordered vertex pair in a weighted graph.

> **State $D^{(k)}[i,j]$**: Shortest path cost from $i$ to $j$ when only vertices in $\{1,\ldots,k\}$ may be intermediates.

> **Infinity**: A sentinel indicating that no path is currently known.

Initialise from direct edges, with zero on the diagonal and infinity for missing edges:

$$
D^{(0)}[i,j]=\begin{cases}0,&i=j,\\w_{ij},&\text{edge }i\to j\text{ exists},\\\infty,&\text{otherwise}.
\end{cases}
$$

Either an optimal path avoids the new intermediate or it splits into two optimal legs through that intermediate:

$$
D^{(k)}[i,j]=\min\left(D^{(k-1)}[i,j],D^{(k-1)}[i,k]+D^{(k-1)}[k,j]\right).
$$

![Source weighted Floyd graph](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/08B_Dynamic_Programming/floyd-graph.svg)

*Directed edge weights define the initial matrix; later stages can replace an edge by a cheaper multi-edge route.*

```pseudo
Floyd(W):
    D = copy of W
    for k = 1 to n:
        for i = 1 to n:
            for j = 1 to n:
                if D[i, k] != infinity and D[k, j] != infinity:
                    D[i, j] = min(D[i, j], D[i, k] + D[k, j])
    return D
```

Keep the intermediate loop outermost. Finite sentinel implementations must avoid overflow when adding an infinity marker.

Time is $\Theta(n^3)$ and matrix space is $\Theta(n^2)$. Negative edges are permitted, but finite shortest-path answers require the absence of reachable negative-cost cycles. A negative final diagonal indicates a negative cycle; affected path pairs have no finite minimum.

| Feature | Warshall | Floyd |
|---|---|---|
| Stored value | Reachability Boolean | Minimum distance |
| Retain or improve operation | OR | Minimum |
| Join two legs | AND | Addition |
| No connection | False | Infinity |
| Main time / space | $\Theta(n^3)$ / $\Theta(n^2)$ | $\Theta(n^3)$ / $\Theta(n^2)$ |

### Floyd Source Matrix Trace

The weighted edges are $1\to3$ of weight four; $2\to1$ of weight one; $2\to3$ of weight six; $2\to4$ of weight three; $4\to2$ of weight five; and $4\to3$ of weight one.

$$
D^{(0)}=\begin{bmatrix}0&\infty&4&\infty\\1&0&6&3\\\infty&\infty&0&\infty\\\infty&5&1&0\end{bmatrix}.
$$

Allowing vertex one improves $2\to3$ from six to $1+4=5$:

$$
D^{(1)}=\begin{bmatrix}0&\infty&4&\infty\\1&0&5&3\\\infty&\infty&0&\infty\\\infty&5&1&0\end{bmatrix}.
$$

Allowing vertex two finds $4\to1$ through $4\to2\to1$, cost $5+1=6$:

$$
D^{(2)}=\begin{bmatrix}0&\infty&4&\infty\\1&0&5&3\\\infty&\infty&0&\infty\\6&5&1&0\end{bmatrix},\qquad D^{(3)}=D^{(2)}.
$$

Vertex three cannot improve another route because it has no outgoing edge. Vertex four improves $2\to3$ again, now by $2\to4\to3$ with cost $3+1=4$:

$$
D=D^{(4)}=\begin{bmatrix}0&\infty&4&\infty\\1&0&4&3\\\infty&\infty&0&\infty\\6&5&1&0\end{bmatrix}.
$$

A shortest path need not be a single direct edge. An infinity in the final matrix means that destination remains unreachable from that origin.

### Recovering Floyd Paths

#### Definitions

> **Intermediate matrix**: A matrix $P$ recording the intermediate vertex responsible for a strict distance improvement.

Initialise every entry of $P$ to zero. Whenever using $k$ strictly improves a distance:

$$
\text{if }D[i,k]+D[k,j]<D[i,j],\quad
D[i,j]\leftarrow D[i,k]+D[k,j],\quad P[i,j]\leftarrow k.
$$

```pseudo
PrintIntermediateVertices(i, j, P):
    k = P[i, j]
    if k != 0:
        PrintIntermediateVertices(i, k, P)
        print k
        PrintIntermediateVertices(k, j, P)

PrintPath(i, j, D, P):
    if D[i, j] == infinity: report no path; return
    print i
    PrintIntermediateVertices(i, j, P)
    if i != j: print j
```

The source helper prints internal vertices only; endpoints must be included by a wrapper. Strict improvements avoid overwriting decisions on ties. This representation assumes one-based vertices so zero is an unused sentinel.

For the example, $P[2,3]$ is first set to one and later overwritten by four. Reconstruction therefore returns $2,4,3$, the final shortest route. Also $P[4,1]=2$, giving $4,2,1$.

### Zero-One Knapsack State And Recurrence

#### Definitions

> **Zero-one knapsack**: Maximise total item value without exceeding capacity, taking each item at most once.

> **State $V[i,j]$**: Maximum value from the first $i$ items that fits capacity $j$.

Assume positive integer weights $w_i$, nonnegative values $v_i$ and integer capacity $W$. Initialise:

$$
V[0,j]=0,\qquad V[i,0]=0.
$$

The current item is either excluded or included exactly once:

$$
V[i,j]=\begin{cases}
V[i-1,j],&j<w_i,\\
\max\{V[i-1,j],V[i-1,j-w_i]+v_i\},&j\ge w_i.
\end{cases}
$$

| Choice | Earlier state | Added value |
|---|---|---|
| Exclude current item | $V[i-1,j]$ | Zero |
| Include current item | $V[i-1,j-w_i]$ | $v_i$ |

Both branches use the previous item row, preventing reuse of the same item.

```pseudo
Knapsack(weights, values, W):
    V[0, 0 .. W] = all zeros
    for i = 1 to n:
        V[i, 0] = 0
        for j = 1 to W:
            if j < weights[i]:
                V[i, j] = V[i - 1, j]
            else:
                V[i, j] = max(V[i - 1, j],
                              V[i - 1, j - weights[i]] + values[i])
    return V[n, W], V
```

The illustrative packing figure before the DP table has item weights $8,16,20,24,32$ and values $30,50,55,80,90$. Its displayed subset has weight $68$ and value $215$; it illustrates feasible packing rather than certifying the optimum.

![Illustrative source knapsack packing](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/08B_Dynamic_Programming/knapsack-packing.svg)

*The illustrated bag contains weights 8, 16, 20 and 24; the separate DP example below uses different item data.*

### Knapsack Source Table And Reconstruction

The DP source example uses capacity $W=5$:

| Item | Weight | Value |
|---|---:|---:|
| $1$ | $2$ | $12$ |
| $2$ | $1$ | $10$ |
| $3$ | $3$ | $20$ |
| $4$ | $2$ | $15$ |

| Items considered / capacity | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---:|---:|---:|---:|---:|---:|
| None | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| $1$ | $0$ | $0$ | $12$ | $12$ | $12$ | $12$ |
| $1,2$ | $0$ | $10$ | $12$ | $22$ | $22$ | $22$ |
| $1,2,3$ | $0$ | $10$ | $12$ | $22$ | $30$ | $32$ |
| $1,2,3,4$ | $0$ | $10$ | $15$ | $25$ | $30$ | $37$ |

Examples of cell evaluation:

$$
\begin{aligned}
V[2,3]&=\max\{V[1,3],V[1,2]+10\}=\max\{12,22\}=22,\\
V[3,4]&=\max\{V[2,4],V[2,1]+20\}=\max\{22,30\}=30,\\
V[4,4]&=\max\{V[3,4],V[3,2]+15\}=\max\{30,27\}=30,\\
V[4,5]&=\max\{32,22+15\}=37.
\end{aligned}
$$

Recover an optimal subset:

1. Start at $(i,j)=(n,W)$.
2. If $V[i,j]=V[i-1,j]$, exclude item $i$ and move to $(i-1,j)$.
3. Otherwise include item $i$, subtract its weight, and move to $(i-1,j-w_i)$.
4. Stop after the first row or zero capacity.

On a tie, exclusion gives one valid optimum; inclusion may give another. The source trace is:

$$
(4,5)\xrightarrow{\text{include }4}(3,3)
\xrightarrow{\text{exclude }3}(2,3)
\xrightarrow{\text{include }2}(1,2)
\xrightarrow{\text{include }1}(0,0).
$$

Items $1,2,4$ have weight $2+1+2=5$ and value $12+10+15=37$.

Time and full-table space are $\Theta(nW)$. Reconstruction takes $O(n)$ steps. A one-row value-only implementation uses $\Theta(W)$ space and must update capacities descending to prevent repeatedly using the current item.

### Memory Functions And Memoisation

#### Definitions

> **Memory function / memoisation**: A top-down recursive method that stores each computed state and returns the stored answer on repeated requests.

> **Lazy evaluation of states**: Compute a state only when it is requested by the dependency structure.

| Approach | State traversal | Repeated states | Storage / overhead |
|---|---|---|---|
| Naive recursion | Top down | Recomputed | Call stack, potentially exponential work |
| Bottom-up DP | Predetermined table order | Computed once | Table; no recursion required |
| Memoised DP | Top down, on demand | Computed once | Cache and call stack |

> [!warning] <span style="color:#ffc778">Source qualification</span>
> The statement that DP uses iteration and never recursion describes bottom-up tabulation. Memoisation is a valid recursive DP technique, and the same lecture subsequently introduces it.

Initialise base row and column to zero; initialise other entries to an uncomputed sentinel such as minus one, which is safe for nonnegative optimum values.

```pseudo
MemoKnapsack(i, j):
    if i == 0 or j == 0: return 0
    if V[i, j] is uncomputed:
        if j < weight[i]:
            value = MemoKnapsack(i - 1, j)
        else:
            value = max(MemoKnapsack(i - 1, j),
                        itemValue[i] + MemoKnapsack(i - 1, j - weight[i]))
        V[i, j] = value
    return V[i, j]
```

For the source query $(4,5)$, the requested positive-capacity states include:

| Item row | Requested capacities | Computed values |
|---|---|---|
| $4$ | $5$ | $37$ |
| $3$ | $3,5$ | $22,32$ |
| $2$ | $2,3,5$ | $12,22,22$ |
| $1$ | $1,2,3,4,5$ | $0,12,12,12,12$ |

Other base entries are already zero. Memoisation skips unneeded states, but a preallocated rectangular table still takes $\Theta(nW)$ memory. A sparse cache allocates only visited states; worst-case visited-state count remains $O(nW)$ and stack depth is $O(n)$.

### DP Formulation And Limits

DP requires enough state information for the recurrence to remain correct. Its main practical limit is the number of states that must be stored and evaluated.

For knapsack, $W$ is a numeric input value encoded in $\Theta(\log W)$ bits. Therefore $\Theta(nW)$ is **pseudo-polynomial**, rather than polynomial in the complete bit-length input size. The same issue appears in amount-indexed change making.

When a simpler greedy method has a proof of optimality, it can avoid large DP tables. Choosing greedy merely because it is simpler is insufficient; counterexamples may show it fails.
