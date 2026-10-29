---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 03 — Brute Force And Exhaustive Search"
---

# TOA 03 — Brute Force And Exhaustive Search

**Source note:** [Brute Force And Exhaustive Search](../../TOA/03_Brute_Force_And_Exhaustive_Search.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

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
  - [[#Complete And Feasible Search|Complete And Feasible Search]]
  - [[#Graph And Geometry Guarantees|Graph And Geometry Guarantees]]

## Core Content

### Brute Force As A Design Strategy

<!-- qard-id: ap-f70dbd89ef2ee37975e8 -->
> [!qard]- What is brute force as an algorithm design strategy?
> A straightforward approach based directly on the problem statement or definition.

<!-- qard-id: ap-9f95ba3cf75094b0ebcd -->
> [!qard]- What is exhaustive search?
> Brute-force search systematically considering every candidate in a finite solution space.

<!-- qard-id: ap-ec80dc651c4b25638b69 -->
> [!qard]- Why keep a brute-force method even when a faster method exists?
> It is simple, widely applicable and useful as a correctness baseline or for small/occasional inputs. A fixed number of parallel workers improves constants, not the asymptotic class.

### Brute-Force String Matching

<!-- qard-id: ap-16b407f45285aa9cbfb1 -->
> [!qard]- How does brute-force string matching search the text?
> At each start position $0$ through $n-m$, compare the pattern left to right until mismatch or full match; after a mismatch, advance the start by one.

<!-- qard-id: ap-3b5cce93e0d2825cc00d -->
> [!qard]- What is the exact worst-case comparison count for brute-force string matching?
> $m(n-m+1)$ for $1\le m\le n$.

<!-- qard-id: ap-67b49729e9f869321833 -->
> [!qard]- How should first-occurrence matching handle empty or overlong patterns?
> The notes return zero for an empty pattern. If $m>n$, no nonempty alignment is possible; otherwise valid starts are $0$ through $n-m$, returning the first match or failure.

<!-- qard-id: ap-4f3b826e2bd1c17e1d91 -->
> [!qard]- When does brute-force matching's $m(n-m+1)$ worst count become approximately $mn$?
> When $m$ is small relative to $n$. If $m$ approaches $n$, the number of alignments matters; expected linear claims require a suitable text model, often fixed $m$.

### Closest Pair Of Points

<!-- qard-id: ap-935876393f2d71c4d759 -->
> [!qard]- How does the brute-force closest-pair algorithm work?
> Examine every unordered pair, compute its squared distance, and retain the pair with the smallest value.

<!-- qard-id: ap-64c1ebfd1134ace17d95 -->
> [!qard]- What are the time and auxiliary-space costs of brute-force closest pair?
> $\Theta(n^2)$ time and $\Theta(1)$ auxiliary space.

<!-- qard-id: ap-740756204904f54ad91c -->
> [!qard]- How many distinct point pairs are tested, and why compare squared distance?
> $n(n-1)/2$ unordered pairs for at least two points. Squared Euclidean distance preserves ordering without repeated square roots; take a square root only if the actual distance is requested.

### Convex Sets And Brute-Force Convex Hull

<!-- qard-id: ap-cc5f0f2b6d53bd17e4c1 -->
> [!qard]- What is the convex hull of a point set?
> The smallest convex set containing all the input points.

<!-- qard-id: ap-18b0b9c8b1ad01f146e0 -->
> [!qard]- What test identifies a supporting hull boundary from a candidate point pair?
> All remaining points must lie on the same side of the pair's supporting line, or on that line.

<!-- qard-id: ap-1aed0db26c3187dbb8f0 -->
> [!qard]- What orientation determinant tests a point's side of a directed line?
> $\operatorname{orient}(P_1,P_2,P)=(x_2-x_1)(y-y_1)-(y_2-y_1)(x-x_1)$.

<!-- qard-id: ap-a5d5696165f8f6070ee9 -->
> [!qard]- What is the worst-case cost of brute-force convex hull?
> $O(n^3)$: $\Theta(n^2)$ pairs with up to $\Theta(n)$ side tests each; the full unshortened version performs $\Theta(n^3)$ tests.

<!-- qard-id: ap-02f4f0af8177cb32cee9 -->
> [!qard]- What does convexity require, and how are orientation signs used in a hull test?
> Every segment joining two set points remains inside the set. Positive/negative orientation signs mark opposite sides of an edge; seeing both rejects that candidate; zero means collinear.

<!-- qard-id: ap-d1058471e9c522e33b51 -->
> [!qard]- Why must a convex-hull algorithm specify a collinearity policy?
> Several points may lie on one boundary line. Decide whether to retain only extreme endpoints or all boundary points, without inventing interior edges.

### Systematic Exhaustive Search

<!-- qard-id: ap-eae86c7a3fcce4ab7c74 -->
> [!qard]- What are the steps of exhaustive optimisation?
> Generate candidates systematically; reject infeasible ones; evaluate feasible ones and retain the best; return it after enumeration ends.

<!-- qard-id: ap-50ed5f6e4d18e34c5029 -->
> [!qard]- What makes an exhaustive optimisation argument correct, and what costs must it count?
> A complete candidate generator inspects every feasible possibility and retains the best. Include generation, feasibility tests and objective evaluation; avoid duplicate representations where possible.

### Travelling Salesman Problem

<!-- qard-id: ap-bbb62aacf7282753e6ab -->
> [!qard]- How does exhaustive search solve TSP?
> Generate city orders, form the corresponding tours, sum their edge costs, and retain the cheapest feasible tour.

<!-- qard-id: ap-4f349b1648d5e61b668c -->
> [!qard]- What is the straightforward total time for exhaustive TSP with full tour evaluation?
> $\Theta(n(n-1)!)=\Theta(n!)$, because each tour takes $\Theta(n)$ to sum.

<!-- qard-id: ap-4c62645a7a45966f8a52 -->
> [!qard]- How do fixing the start and identifying reversed tours affect TSP candidate count?
> Fixing the start leaves $(n-1)!$ orders. Symmetric undirected costs allow reversal pairs to be identified, giving $(n-1)!/2$ for $n\ge3$; directed costs generally do not.

<!-- qard-id: ap-c6786aeafc299ec16e8a -->
> [!qard]- What are a Hamiltonian circuit and the travelling salesman problem?
> A Hamiltonian circuit visits every vertex once and returns to its start. TSP asks for the minimum-total-cost such tour in a weighted instance; the candidate must satisfy the visit and return constraints.

### Zero-One Knapsack By Subsets

<!-- qard-id: ap-f6268912313caac8ae44 -->
> [!qard]- What is the zero-one knapsack problem?
> Choose a subset of items, each included once or excluded, maximising total value without exceeding capacity.

<!-- qard-id: ap-b01deb0a037c9a9cf06c -->
> [!qard]- How many candidates does exhaustive zero-one knapsack examine?
> All $2^n$ subsets, including the empty subset; each candidate is checked for capacity and total value.

<!-- qard-id: ap-89848275b37e800a2b14 -->
> [!qard]- What total time results from recomputing each knapsack subset's totals by inspecting all items?
> $\Theta(n2^n)$.

### Assignment By Permutations

<!-- qard-id: ap-af9417659cce7f57191c -->
> [!qard]- What does exhaustive assignment optimise, and how many candidates does it have?
> Assign $n$ people to $n$ jobs, using each job once, to minimise total cost. There are $n!$ candidate permutations.

<!-- qard-id: ap-74012e0664a414c7c88f -->
> [!qard]- What time does exhaustive assignment take if each candidate's $n$ costs are summed separately?
> $\Theta(n\,n!)$; $n!$ alone counts candidates.

<!-- qard-id: ap-39bf8cfee8361efebb70 -->
> [!qard]- Does factorial exhaustive assignment search prove that assignment itself requires factorial time?
> No. It describes that algorithm, not a lower bound for the problem; assignment has faster exact methods.

### Exhaustive Graph Traversal And Representations

<!-- qard-id: ap-f62b919c9a619bbd6675 -->
> [!qard]- How do BFS and DFS differ in exploration and frontier structure?
> BFS explores by distance in edges using a queue; DFS follows a branch deeply before backtracking, using a stack or recursion.

<!-- qard-id: ap-c999b4fbce7e37c29400 -->
> [!qard]- Why mark vertices as discovered when adding them to the frontier?
> To avoid repeatedly adding already discovered vertices.

<!-- qard-id: ap-cd07fa59b4144a8e6d5a -->
> [!qard]- How do you traverse every component of a disconnected graph?
> Restart at an undiscovered vertex whenever the current frontier becomes empty.

<!-- qard-id: ap-b4167fe799f78f72460c -->
> [!qard]- What is full BFS or DFS time with adjacency lists?
> $\Theta(\lvert V\rvert+\lvert E\rvert)$, because each vertex and adjacency entry is processed.

<!-- qard-id: ap-acbe1409b3c494fea272 -->
> [!qard]- What is full BFS or DFS time with an adjacency matrix?
> $\Theta(\lvert V\rvert^2)$, because a full row is scanned for each vertex.

<!-- qard-id: ap-4b8bd69c15f05a7357c9 -->
> [!qard]- How do adjacency lists and matrices represent the same graph?
> A list stores each vertex's neighbours; a matrix stores one entry per ordered vertex pair. Matrix row scans cost $\Theta(|V|)$ each; list traversal scans only stored adjacency entries.

### Complete And Feasible Search

<!-- qard-id: ap-59263f75b48e59b48205 -->
> [!qard]- What is the difference between a complete candidate generator and a sound feasibility test?
> Completeness ensures no possible solution is missed; sound feasibility checks reject candidates violating the actual constraints. Both are needed before keeping the best objective value proves an optimum.

<!-- qard-id: ap-21c899fc32a6c5815276 -->
> [!qard]- Why can duplicate candidates hurt exhaustive search without making its optimum wrong?
> They repeat equivalent work and distort candidate counts; a complete search can still find the optimum, but a duplicate-free representation is more efficient.

<!-- qard-id: ap-28d993057a807b2ac314 -->
> [!qard]- What does a TSP candidate need besides a permutation of cities?
> Edges connecting consecutive cities and the return to the start must be valid; include all their weights and reject a tour with a missing required edge.

<!-- qard-id: ap-9b6a05547647bf11e7dc -->
> [!qard]- Why is independently choosing each person's cheapest job not a valid general assignment algorithm?
> Several people may choose the same job; the global one-to-one constraint couples the choices, which permutation enumeration enforces.

<!-- qard-id: ap-7f805ae79fd337f4c8a7 -->
> [!qard]- How does zero-one knapsack differ from allowing repeated copies of an item?
> Each listed item is either absent or included once; an algorithm allowing reuse solves a different feasible set and can return an invalid answer.

### Graph And Geometry Guarantees

<!-- qard-id: ap-f715eff0202cfe87e02c -->
> [!qard]- What extra property does BFS provide on an unweighted graph?
> Vertices are discovered in nondecreasing edge-distance from the start, so parent links can recover a shortest edge-count path. This does not solve arbitrary weighted shortest paths.

<!-- qard-id: ap-8138f26e0592edafa529 -->
> [!qard]- How do adjacency-list and adjacency-matrix storage compare?
> Lists use $\Theta(|V|+|E|)$ structural space; a full matrix uses $\Theta(|V|^2)$ entries. Their traversal costs reflect those different representations.

<!-- qard-id: ap-735995409bb017ea3567 -->
> [!qard]- Why mark a vertex when discovering/enqueuing it rather than waiting until removal?
> Other frontier vertices might otherwise add it again before it is processed, creating repeated work and inconsistent discovery/parent bookkeeping.
