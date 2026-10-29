---
tags:
  - advanced-programming
---

# Brute Force And Exhaustive Search

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)  
**Source**: [3 - TOA Brute Force.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/3%20-%20TOA%20Brute%20Force.pdf), Patrick Marais, University of Cape Town, PDF pages 1–22  
**Generated**: 2026-10-02

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes. Examples and corrections appear beside the relevant concept.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Brute Force As A Design Strategy|Brute Force As A Design Strategy]]
  - [[#Brute-Force String Matching|Brute-Force String Matching]]
  - [[#Closest Pair Of Points|Closest Pair Of Points]]
  - [[#Convex Sets And Brute-Force Convex Hull|Convex Sets And Brute-Force Convex Hull]]
  - [[#Systematic Exhaustive Search|Systematic Exhaustive Search]]
  - [[#Travelling Salesman Problem|Travelling Salesman Problem]]
  - [[#Zero-One Knapsack By Subsets|Zero-One Knapsack By Subsets]]
  - [[#Assignment By Permutations|Assignment By Permutations]]
  - [[#Exhaustive Graph Traversal And Representations|Exhaustive Graph Traversal And Representations]]

---

## Core Content

### Brute Force As A Design Strategy

#### Definitions

> **Brute force**: A straightforward approach based directly on the problem statement or definition.

> **Exhaustive search**: A brute-force search that systematically considers every candidate in a finite solution space.

Brute force includes direct repeated multiplication, linear search and checking all point pairs. Exhaustive search is the special case that enumerates candidate solutions such as permutations or subsets.

| Strength | Limitation |
|---|---|
| Simple and widely applicable | Often has poor time efficiency |
| Quick to implement and check | Large combinatorial spaces can be infeasible |
| Useful baseline for better methods | Parallel execution reduces constants, not the growth class |
| Often adequate for small or occasional tasks | A large workload may require another strategy |

### Brute-Force String Matching

#### Definitions

> **Text**: The string being searched, with length $n$.

> **Pattern**: The string sought in the text, with length $m$.

> **Alignment**: A placement of the pattern against a substring of the text.

Return the zero-based index of the first occurrence, or a failure value if there is none.

1. Align the pattern at the first text character.
2. Compare left to right until all pattern characters match or a mismatch occurs.
3. On mismatch, shift right by one position and repeat.
4. Stop after the final valid start position $n-m$.

```java
BruteForceMatch(T, P):
    n = length(T)
    m = length(P)
    if m == 0: return 0
    for start = 0 to n - m:
        j = 0
        while j < m and P[j] == T[start + j]:
            j = j + 1
        if j == m: return start
    return -1
```

![SEA alignment trace](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/03_Brute_Force_And_Exhaustive_Search/string-alignments.svg)

*The pattern SEA first matches SEE SHE SEA at index eight after unit shifts.*

For text containing only `a` and pattern `aaab`, every viable alignment matches the first characters and fails at the last:

$$
C_{\mathrm{worst}}(n,m)=m(n-m+1),\qquad 1\le m\le n.
$$

This is $\Theta(mn)$ when $m$ is much smaller than $n$, but the exact expression matters when $m$ approaches $n$. For fixed pattern length under ordinary random-text models, expected searching is linear in text length; this is not a guarantee for every text distribution.

### Closest Pair Of Points

#### Definitions

> **Closest-pair problem**: Find the pair of distinct input points with minimum Euclidean distance.

For points $P_i=(x_i,y_i)$ and $P_j=(x_j,y_j)$:

$$
d(P_i,P_j)=\sqrt{(x_i-x_j)^2+(y_i-y_j)^2}.
$$

Compare every unordered pair and retain the best pair:

```java
ClosestPair(P):
    bestSquared = infinity
    bestPair = none
    for i = 0 to length(P) - 2:
        for j = i + 1 to length(P) - 1:
            squared = (P[i].x - P[j].x)^2 + (P[i].y - P[j].y)^2
            if squared < bestSquared:
                bestSquared = squared
                bestPair = (i, j)
    return bestPair
```

There are $n(n-1)/2$ pair comparisons, giving $\Theta(n^2)$ time and constant auxiliary space. At least two points are required to return a pair.

Squared distances preserve the ordering of nonnegative distances. Avoid square roots inside the loop; compute one afterwards if the distance itself is needed.

![Closest pair highlighted in a point cloud](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/03_Brute_Force_And_Exhaustive_Search/closest-pair.svg)

*Every pair is a candidate; the highlighted pair has the smallest separation.*

### Convex Sets And Brute-Force Convex Hull

#### Definitions

> **Convex set**: A set containing the entire line segment joining any two of its points.

> **Convex hull**: The smallest convex set containing the input points.

![Convex and nonconvex shapes and a point hull](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/03_Brute_Force_And_Exhaustive_Search/convex-hull.svg)

*A segment stays inside a convex set, while a segment can leave a nonconvex set. A hull encloses every input point.*

1. Select a pair of distinct points.
2. Test which side of their supporting line contains each remaining point.
3. If all remaining points are on one side or on the line, the pair identifies a supporting hull boundary.
4. Repeat for every pair, and assemble boundary points in order.

Use the orientation determinant:

$$
\operatorname{orient}(P_1,P_2,P)=
(x_2-x_1)(y-y_1)-(y_2-y_1)(x-x_1).
$$

Positive and negative signs identify opposite sides; zero means collinear. A candidate fails as soon as both nonzero signs occur.

There are $\Theta(n^2)$ candidate pairs and up to $\Theta(n)$ side tests per pair, giving a cubic worst-case upper bound. The full all-pairs/all-points version performs $\Theta(n^3)$ tests. Collinear boundary points need an explicit policy: keep only endpoints for a minimal vertex list, or retain boundary points without creating spurious interior edges.

### Systematic Exhaustive Search

Enumerating candidates must be complete and avoid duplicates.

1. Define a systematic candidate generator.
2. Reject infeasible candidates.
3. Evaluate each feasible candidate and retain the best so far.
4. Return the retained solution after enumeration ends.

Correctness follows from inspecting every feasible candidate. Feasibility checks, generation costs and objective calculation must all be included when reporting total time.

### Travelling Salesman Problem

#### Definitions

> **Travelling salesman problem (TSP)**: Find a minimum-cost tour visiting each city exactly once before returning to its start.

> **Hamiltonian circuit**: A cycle visiting every graph vertex exactly once before returning to the start.

A TSP instance is a weighted graph. Exhaustive search generates city permutations and adds tour-edge costs.

![Four-city TSP graph](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/03_Brute_Force_And_Exhaustive_Search/tsp.svg)

*The source graph has six weighted edges; the highlighted tour costs seventeen.*

| Tour | Cost |
|---|---:|
| $a\to b\to c\to d\to a$ | $2+3+7+5=17$ |
| $a\to b\to d\to c\to a$ | $2+4+7+8=21$ |
| $a\to c\to b\to d\to a$ | $8+3+4+5=20$ |
| $a\to c\to d\to b\to a$ | $8+7+4+2=21$ |
| $a\to d\to b\to c\to a$ | $5+4+3+8=20$ |
| $a\to d\to c\to b\to a$ | $5+7+3+2=17$ |

Fixing the start removes rotational duplicates, leaving $(n-1)!$ orders. For symmetric undirected distances, reverse tours are equivalent, leaving $(n-1)!/2$ candidates for $n\ge3$. Reversal is not generally equivalent for directed distances.

The PDF's factorial class describes candidate count. If each tour is summed from scratch, each costs $\Theta(n)$ to evaluate, so total straightforward time is $\Theta(n(n-1)!)=\Theta(n!)$.

### Zero-One Knapsack By Subsets

#### Definitions

> **Zero-one knapsack**: Choose a subset of items, each either included once or excluded, maximising total value without exceeding capacity.

$$
\max_{S\subseteq\{1,\ldots,n\}}\sum_{i\in S}v_i
\quad\text{subject to}\quad \sum_{i\in S}w_i\le W.
$$

The source instance has capacity $W=16$:

| Item | Weight | Value |
|---|---:|---:|
| $1$ | $2$ | $200$ |
| $2$ | $5$ | $300$ |
| $3$ | $10$ | $500$ |
| $4$ | $5$ | $100$ |

| Subset | Weight | Value or feasibility |
|---|---:|---|
| $\varnothing$ | $0$ | $0$ |
| $\{1\}$ | $2$ | $200$ |
| $\{2\}$ | $5$ | $300$ |
| $\{3\}$ | $10$ | $500$ |
| $\{4\}$ | $5$ | $100$ |
| $\{1,2\}$ | $7$ | $500$ |
| $\{1,3\}$ | $12$ | $700$ |
| $\{1,4\}$ | $7$ | $300$ |
| $\{2,3\}$ | $15$ | $800$ — optimal |
| $\{2,4\}$ | $10$ | $400$ |
| $\{3,4\}$ | $15$ | $600$ |
| $\{1,2,3\}$ | $17$ | Infeasible |
| $\{1,2,4\}$ | $12$ | $600$ |
| $\{1,3,4\}$ | $17$ | Infeasible |
| $\{2,3,4\}$ | $20$ | Infeasible |
| $\{1,2,3,4\}$ | $22$ | Infeasible |

There are $2^n$ subsets, including the empty set. Enumeration therefore requires $\Omega(2^n)$ work. Recomputing every subset's totals by inspecting all items gives $\Theta(n2^n)$ time.

### Assignment By Permutations

#### Definitions

> **Assignment problem**: Match each of $n$ people to exactly one of $n$ jobs, using each job once, with minimum total cost.

A permutation $\pi$ specifies the job assigned to each person:

$$
\min_{\pi}\sum_{i=1}^{n}C[i,\pi(i)].
$$

| Person | Job $1$ | Job $2$ | Job $3$ | Job $4$ |
|---|---:|---:|---:|---:|
| $1$ | $9$ | $2$ | $7$ | $8$ |
| $2$ | $6$ | $4$ | $3$ | $7$ |
| $3$ | $5$ | $8$ | $1$ | $8$ |
| $4$ | $7$ | $6$ | $9$ | $4$ |

For $(1,2,3,4)$ the cost is $18$; for $(1,2,4,3)$ it is $28$; for $(1,3,2,4)$ it is $24$. Enumerating all permutations finds $(2,1,3,4)$ with cost $2+6+1+4=13$.

There are $n!$ assignments. Summing all $n$ entries separately for each candidate gives $\Theta(n\,n!)$ time; the PDF's $\Theta(n!)$ refers to the number of candidates. Unlike general TSP, assignment has more efficient exact algorithms.

### Exhaustive Graph Traversal And Representations

#### Definitions

> **Breadth-first search (BFS)**: Explore vertices in nondecreasing number of edges from a start using a first-in, first-out queue.

> **Depth-first search (DFS)**: Explore a branch before returning to its alternatives using a stack or recursive call stack.

> **Adjacency list**: For each vertex, a list of its neighbours.

> **Adjacency matrix**: A matrix indicating whether each vertex pair is connected.

> [!warning] <span style="color:#ffc778">Source correction</span>
> The PDF swaps the data structures: BFS uses a queue, and DFS uses a stack.

![Traversal example graph](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/03_Brute_Force_And_Exhaustive_Search/traversal-graph.svg)

*The same six-vertex graph can be represented by neighbour lists or a matrix.*

| Vertex | Neighbours |
|---|---|
| $a$ | $c,d$ |
| $b$ | $c,f$ |
| $c$ | $a,b,e$ |
| $d$ | $a,e$ |
| $e$ | $c,d,f$ |
| $f$ | $b,e$ |

$$
A=\begin{bmatrix}
0&0&1&1&0&0\\0&0&1&0&0&1\\1&1&0&0&1&0\\
1&0&0&0&1&0\\0&0&1&1&0&1\\0&1&0&0&1&0
\end{bmatrix}.
$$

1. Mark the start as discovered and put it in the frontier.
2. Remove the next vertex using the chosen queue or stack policy.
3. Inspect neighbours; mark and add previously undiscovered vertices.
4. Repeat until the frontier is empty.
5. Restart at an undiscovered vertex if the task requires traversing every component.

| Representation | Time for full BFS or DFS | Reason |
|---|---|---|
| Adjacency list | $\Theta(\lvert V\rvert+\lvert E\rvert)$ | Visits each vertex and scans each adjacency entry |
| Adjacency matrix | $\Theta(\lvert V\rvert^2)$ | Scans a row for each vertex |

Traversal inspects vertices and edges; it does not enumerate every possible path or tour. With alphabetical neighbour order, BFS from $a$ visits $a,c,d,b,e,f$; recursive DFS visits $a,c,b,f,e,d$.
