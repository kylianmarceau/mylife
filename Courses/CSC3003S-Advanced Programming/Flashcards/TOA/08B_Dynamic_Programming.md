---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 08B — Dynamic Programming II"
---

# TOA 08B — Dynamic Programming II

**Source note:** [Dynamic Programming II](../../TOA/08B_Dynamic_Programming.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Floyd's Algorithm|Floyd's Algorithm]]
  - [[#DP Principle|DP Principle]]
  - [[#Knapsack|Knapsack]]
  - [[#Memory Functions|Memory Functions]]

## Core Content

### Floyd's Algorithm

<!-- qard-id: ap-af58d55b676f6334c5ca -->
> [!qard]- What problem does Floyd's algorithm solve?
> All-pairs shortest paths in a weighted (directed or undirected) graph.

<!-- qard-id: ap-4129b6ea1a92268cfa77 -->
> [!qard]- How is Floyd's $D^{(0)}$ initialised?
> The weighted adjacency matrix: edge weights, 0 on the diagonal, $\infty$ where there is no edge.

<!-- qard-id: ap-77296457d92c650d21c1 -->
> [!qard]- State Floyd's update rule.
> $d^{(k)}_{ij}=\min\big(d^{(k-1)}_{ij},\ d^{(k-1)}_{ik}+d^{(k-1)}_{kj}\big)$.

<!-- qard-id: ap-3b3eb8f84ce66b6738e4 -->
> [!qard]- What are Floyd's time and space costs?
> $\Theta(n^3)$ time, $\Theta(n^2)$ space.

<!-- qard-id: ap-4e885ee3a7d0bbbc2d94 -->
> [!qard]- How do you recover the actual shortest paths from Floyd's algorithm?
> Keep a matrix $P$; when $k$ improves $d_{ij}$ set $P[i,j]=k$, then recursively print path$(i,k)$, $k$, path$(k,j)$.

<!-- qard-id: ap-3497011ce3786a3721c9 -->
> [!qard]- How are Floyd's and Warshall's algorithms related?
> Same triple loop over intermediate vertices; Warshall uses OR/AND on reachability, Floyd uses min/+ on distances.

### DP Principle

<!-- qard-id: ap-238d815003145bbcd699 -->
> [!qard]- What order must a bottom-up DP table be filled in?
> Smallest subproblems first, increasing in size, using only entries already computed; each entry exactly once.

### Knapsack

<!-- qard-id: ap-65535f667a1c1c67cd39 -->
> [!qard]- What does $V[i,j]$ mean in the knapsack DP?
> The value of the best subset of the first $i$ items fitting in capacity $j$.

<!-- qard-id: ap-90b68f580e6968f06f51 -->
> [!qard]- State the knapsack recurrence.
> $V[i,j]=V[i-1,j]$ if $j<w_i$, else $\max\big(V[i-1,j],\ V[i-1,j-w_i]+v_i\big)$; $V[0,j]=V[i,0]=0$.

<!-- qard-id: ap-f3eafa22c849b9e23835 -->
> [!qard]- How do you recover the knapsack contents from the table?
> From $V[n,W]$: if $V[i,j]\ne V[i-1,j]$ item $i$ is in, go to $V[i-1,j-w_i]$; otherwise go to $V[i-1,j]$.

<!-- qard-id: ap-de2da833041bd0e69c9f -->
> [!qard]- What is the time complexity of the knapsack DP?
> $\Theta(nW)$ to fill the table; $\Theta(n)$ to recover the contents.

### Memory Functions

<!-- qard-id: ap-ed603a5198fc42f985ba -->
> [!qard]- What is a memory function?
> Top-down recursion with a table: entries start as null and are computed only when needed, then stored.

<!-- qard-id: ap-67e4be1c62bcc9f499f2 -->
> [!qard]- How do memory functions compare with top-down recursion and bottom-up DP?
> Recursion repeats subproblems (exponential); bottom-up computes all of them once; memory functions compute only needed ones, once.

<!-- qard-id: ap-7b089a05006d9125af25 -->
> [!qard]- Which evaluation strategy is a memory function equivalent to?
> Lazy evaluation.

<!-- qard-id: ap-bf32d53772576bc6bdf2 -->
> [!qard]- What are DP's main limitations?
> It needs the principle of optimality, may store many partial solutions, and can be hard to formulate — greedy is sometimes simpler.
