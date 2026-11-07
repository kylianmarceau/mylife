---
tags:
  - advanced-programming
---

# Brute Force And Exhaustive Search

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)
**Source**: [3 - TOA Brute Force.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/3%20-%20TOA%20Brute%20Force.pdf), Patrick Marais, University of Cape Town, pages 1–22
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Brute-force string matching, closest pair and convex hull, then exhaustive search for TSP, knapsack, assignment and graph traversal.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Brute Force Means|What Brute Force Means]]
  - [[#Brute-Force String Matching|Brute-Force String Matching]]
  - [[#Brute-Force Closest Pair|Brute-Force Closest Pair]]
  - [[#Brute-Force Convex Hull|Brute-Force Convex Hull]]
  - [[#Strengths And Weaknesses Of Brute Force|Strengths And Weaknesses Of Brute Force]]
  - [[#Exhaustive Search|Exhaustive Search]]
  - [[#Travelling Salesman Problem|Travelling Salesman Problem]]
  - [[#Knapsack Problem|Knapsack Problem]]
  - [[#Assignment Problem|Assignment Problem]]
  - [[#Exhaustive Graph Traversal: BFS And DFS|Exhaustive Graph Traversal: BFS And DFS]]
  - [[#Comments On Exhaustive Search|Comments On Exhaustive Search]]

---

## Core Content

### What Brute Force Means

#### Definitions

> **Brute force**: A straightforward approach directly based on the problem statement and the definitions of the concepts involved.

> **Exhaustive search**: A special case of brute force that generates and checks every candidate solution.

Brute force implies a lack of sophistication, but it has real advantages:

- It is often the quickest and easiest approach to implement.
- Sometimes it is the best solution too.
- It is often good enough for occasional use or small problem sizes.

Examples:

| Problem | Brute-force approach | Efficiency |
|---|---|---|
| Exponentiation | $a^n = a \cdot a \cdots a$ ($n$ times) | $\Theta(n)$ multiplications |
| Searching | Linear search | $\Theta(n)$ |
| Sorting | Bubble sort, insertion sort | $\Theta(n^2)$ |

### Brute-Force String Matching

#### Definitions

> **String matching**: Given a text $T$ of $n$ characters and a pattern $P$ of $m$ characters, find the index of the first occurrence of $P$ in $T$, or return $-1$ if it does not occur.

The last viable starting position is $n - m$; past that, the pattern would run off the end of the text.

High-level algorithm:

1. Align the pattern with the beginning of the text.
2. Moving left to right, compare each pattern character with the corresponding text character until either:
   - all characters match (successful search), or
   - a mismatch is detected.
3. While the pattern is not found and the text is not exhausted, shift the pattern one position right and repeat step 2.

```text
BruteForceStringMatch( T[0..n-1], P[0..m-1] )
    // T is the text; P is the pattern we're searching for
    for k ← 0 to n - m do                     // each start position in T
        j ← 0
        while j < m and P[j] = T[k+j] do      // each char in P
            j ← j + 1
        if j = m return k
    return -1
```

**Example**: match `SEA` in `SEE SHE SEA`. The pattern is tried at every position from 0, shifting one place after each mismatch, until it matches at index 8.

![Brute-force matching of SEA](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/03_Brute_Force_And_Exhaustive_Search/string-alignments.svg)

*Each row is one alignment; the pattern shifts one position right after a mismatch until all three characters match.*

#### Efficiency

The worst case happens when the pattern matches every character except the last, at every alignment.

- Example: text `aaaa…a` ($n$ characters), pattern `aaab` ($m$ characters).
- Each of the $n - m + 1$ alignments costs $m$ comparisons:

$$
C_{worst}(n, m) = m(n - m + 1) \in \Theta(mn) \quad \text{for } m \ll n
$$

In practice $m$ is much smaller than $n$. The worst case is very unlikely with natural language, where mismatches usually occur at the first or second character. The average case on natural-language text is $\Theta(n)$.

### Brute-Force Closest Pair

#### Definitions

> **Closest-pair problem**: Find the two points that are closest together in a set of $n$ 2D points $P_1 = (x_1, y_1), \dots, P_n = (x_n, y_n)$.

The brute-force solution computes the distance between every pair of points, much like the brute-force "is this a set?" check.

```text
dmin ← ∞
for i ← 1 to n-1 do
    for j ← i+1 to n do
        d ← sqrt((xi - xj)^2 + (yi - yj)^2)
        if d < dmin
            dmin ← d
            index1 ← i
            index2 ← j
return index1, index2
```

The distance used is Euclidean:

$$
d(P_i, P_j) = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}
$$

![Closest pair by checking all pairs](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/03_Brute_Force_And_Exhaustive_Search/closest-pair.svg)

*Every unordered pair is compared once; the smallest distance wins.*

- Efficiency: $\Theta(n^2)$, from $n(n-1)/2$ distance computations.
- The square root is expensive in practice but can be avoided: comparing squared distances gives the same ordering.

### Brute-Force Convex Hull

#### Definitions

> **Convex set**: A set of points in the plane is convex if, for any two points $P$ and $Q$ in the set, the whole line segment joining $P$ and $Q$ belongs to the set.

> **Convex hull**: The convex hull of a set of points $S$ is the smallest convex set containing $S$.

Picture stretching a rubber band around all the points: the band settles on the hull.

Algorithm:

1. For each pair of points $p_1$ and $p_2$:
2. Determine whether all other points lie on the same side of the straight line through $p_1$ and $p_2$.
3. If they do, the segment $p_1p_2$ is part of the convex hull boundary.

The side test uses the line through $(x_1, y_1)$ and $(x_2, y_2)$, written $ax + by = c$ with $a = y_2 - y_1$, $b = x_1 - x_2$, $c = x_1y_2 - y_1x_2$. The sign of $ax + by - c$ tells you which side a point lies on.

![Convexity and hull edges](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/03_Brute_Force_And_Exhaustive_Search/convex-hull.svg)

*A segment belongs to the hull when every other point lies on one side of its line.*

Efficiency: there are $\Theta(n^2)$ pairs and each needs a check against the other $n-2$ points, so $\Theta(n^3)$.

### Strengths And Weaknesses Of Brute Force

| Strengths | Weaknesses |
|---|---|
| Wide applicability | Rarely produces efficient algorithms |
| Simplicity | Some brute-force algorithms are infeasibly slow |
| Reasonable algorithms for some important problems (e.g. matrix multiplication, sorting, searching, string matching) | |
| Standard algorithms for simple computational tasks | |
| A good yardstick for judging better algorithms | |
| Sometimes doing better is not worth the bother | |

### Exhaustive Search

Exhaustive search is the brute-force way to look for an element with a special property, usually among combinatorial objects such as permutations, combinations or subsets. It generates every element of the problem's domain.

Method:

1. Construct a way of listing all potential solutions in a systematic manner, such that:
   - all solutions are eventually listed, and
   - no solution is repeated.
2. Evaluate the solutions one by one, disqualifying infeasible ones and keeping track of the best found so far.
3. When the search ends, announce the winner.

### Travelling Salesman Problem

#### Definitions

> **Travelling Salesman Problem (TSP)**: Given $n$ cities with known distances between each pair, find the shortest tour that passes through all cities exactly once before returning to the starting city.

> **Hamiltonian circuit**: A cycle in a graph that visits every vertex exactly once and returns to its start. TSP is equivalently the problem of finding the shortest Hamiltonian circuit in a weighted connected graph.

Exhaustive search generates all permutations of routes. Two improvements reduce the work:

- Start and end at one particular city (fixing the start removes rotations of the same tour).
- Remove tours that differ only in direction (each tour appears once forwards and once backwards).

Example with four cities $a, b, c, d$ and edge weights $ab = 2$, $bc = 3$, $cd = 7$, $ad = 5$, $ac = 8$, $bd = 4$:

| Tour | Cost |
|---|---|
| $a \to b \to c \to d \to a$ | $2 + 3 + 7 + 5 = 17$ (optimal) |
| $a \to b \to d \to c \to a$ | $2 + 4 + 7 + 8 = 21$ |
| $a \to c \to b \to d \to a$ | $8 + 3 + 4 + 5 = 20$ |
| $a \to c \to d \to b \to a$ | $8 + 7 + 4 + 2 = 21$ |
| $a \to d \to b \to c \to a$ | $5 + 4 + 3 + 8 = 20$ |
| $a \to d \to c \to b \to a$ | $5 + 7 + 3 + 2 = 17$ (optimal, reverse of the first) |

![Four-city TSP](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/03_Brute_Force_And_Exhaustive_Search/tsp.svg)

*The highlighted minimum tour costs 17; the table shows each tour appearing in both directions.*

Efficiency:

$$
\frac{(n-1)!}{2} \in \Theta((n-1)!)
$$

### Knapsack Problem

#### Definitions

> **Knapsack problem**: Given $n$ items with weights $w_1, \dots, w_n$, values $v_1, \dots, v_n$ and a knapsack of capacity $W$, find the most valuable subset of items that fits into the knapsack.

Example with capacity $W = 16$ kg:

| Item | Weight | Value |
|---|---|---|
| 1 | 2 kg | R200 |
| 2 | 5 kg | R300 |
| 3 | 10 kg | R500 |
| 4 | 5 kg | R100 |

Exhaustive search enumerates all subsets, calculates each subset's total weight and value, and chooses the best feasible one:

| Subset | Total weight | Total value |
|---|---|---|
| $\{\}$ | 0 kg | R0 |
| $\{1\}$ | 2 kg | R200 |
| $\{2\}$ | 5 kg | R300 |
| $\{3\}$ | 10 kg | R500 |
| $\{4\}$ | 5 kg | R100 |
| $\{1,2\}$ | 7 kg | R500 |
| $\{1,3\}$ | 12 kg | R700 |
| $\{1,4\}$ | 7 kg | R300 |
| $\{2,3\}$ | 15 kg | **R800** (best) |
| $\{2,4\}$ | 10 kg | R400 |
| $\{3,4\}$ | 15 kg | R600 |
| $\{1,2,3\}$ | 17 kg | not feasible |
| $\{1,2,4\}$ | 12 kg | R600 |
| $\{1,3,4\}$ | 17 kg | not feasible |
| $\{2,3,4\}$ | 20 kg | not feasible |
| $\{1,2,3,4\}$ | 22 kg | not feasible |

The optimal subset is $\{2, 3\}$ with value R800. There are $2^n$ subsets, so the efficiency is $\Omega(2^n)$.

### Assignment Problem

#### Definitions

> **Assignment problem**: Assign $n$ people to $n$ jobs so that each person does exactly one job and each job is done by exactly one person, minimising total cost, where $C[i, j]$ is the cost of person $i$ doing job $j$.

Example cost matrix ($n = 4$):

| | Job 1 | Job 2 | Job 3 | Job 4 |
|---|---|---|---|---|
| Person 1 | 9 | 2 | 7 | 8 |
| Person 2 | 6 | 4 | 3 | 7 |
| Person 3 | 5 | 8 | 1 | 8 |
| Person 4 | 7 | 6 | 9 | 4 |

A feasible assignment selects one element in each row, all in different columns. Write it as a permutation: $\{1, 4, 3, 2\}$ means person 1 gets job 1, person 2 gets job 4, person 3 gets job 3 and person 4 gets job 2.

Exhaustive search:

1. Generate all permutations of $1, \dots, n$.
2. Compute the total cost of each assignment.
3. Retain the cheapest.

| Permutation | Costs | Total |
|---|---|---|
| $\{1,2,3,4\}$ | $9 + 4 + 1 + 4$ | 18 |
| $\{1,2,4,3\}$ | $9 + 4 + 8 + 9$ | 30 |
| $\{1,3,2,4\}$ | $9 + 3 + 8 + 4$ | 24 |
| … | … | … |

Continuing through all 24 permutations gives the optimum $\{2, 1, 3, 4\}$ with cost $2 + 6 + 1 + 4 = 13$.

There are $n!$ permutations, so the efficiency is $\Theta(n!)$. This is poor, and better algorithms exist (e.g. the Hungarian method).

### Exhaustive Graph Traversal: BFS And DFS

#### Definitions

> **Graph traversal**: Systematically visiting all vertices of a graph — an exhaustive search over the vertices.

> **Breadth-first search (BFS)**: Visits all neighbours of the current vertex before moving further away; uses a **queue**.

> **Depth-first search (DFS)**: Goes as deep as possible along one path before backtracking; uses a **stack** (or recursion).

The source slide swaps the two data structures: BFS uses a queue and DFS uses a stack.

![Graph for BFS and DFS](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/03_Brute_Force_And_Exhaustive_Search/traversal-graph.svg)

*Both traversals visit every vertex; they differ only in the order, set by the queue or stack.*

| Graph representation | Traversal time (BFS and DFS) |
|---|---|
| Adjacency matrix | $\Theta(\lvert V\rvert^2)$ |
| Adjacency list | $\Theta(\lvert V\rvert + \lvert E\rvert)$ |

Here $\lvert V\rvert$ is the number of vertices and $\lvert E\rvert$ the number of edges.

### Comments On Exhaustive Search

- Exhaustive search runs in a realistic amount of time only on very small instances.
- In many cases there are much better alternatives (e.g. dynamic programming for knapsack, the Hungarian method for assignment).
- In some cases exhaustive search, or a variation of it, is the only known solution — as for TSP.
- Parallel solutions can speed it up.
