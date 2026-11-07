---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 03 — Brute Force And Exhaustive Search"
---

# TOA 03 — Brute Force And Exhaustive Search

**Source note:** [Brute Force And Exhaustive Search](../../TOA/03_Brute_Force_And_Exhaustive_Search.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Brute Force|Brute Force]]
  - [[#String Matching|String Matching]]
  - [[#Closest Pair And Convex Hull|Closest Pair And Convex Hull]]
  - [[#Exhaustive Search|Exhaustive Search]]
  - [[#Graph Traversal|Graph Traversal]]

## Core Content

### Brute Force

<!-- qard-id: ap-fbe2a2a111af0923be12 -->
> [!qard]- What is brute force?
> A straightforward approach based directly on the problem statement and definitions.

<!-- qard-id: ap-d169e25490b051cb1205 -->
> [!qard]- Give three reasons to use brute force despite its inefficiency.
> Simple and widely applicable; good enough for small or occasional problems; a yardstick for better algorithms (and sometimes not worth doing better).

<!-- qard-id: ap-be1a4e3b3c349f75f462 -->
> [!qard]- What are brute force's main weaknesses?
> It rarely gives efficient algorithms, and some brute-force algorithms are infeasibly slow.

### String Matching

<!-- qard-id: ap-4a7bc0bb45ae8e3a6a26 -->
> [!qard]- Describe brute-force string matching.
> Align the pattern at each text position $0..n-m$, compare left to right until all match or a mismatch, then shift right by one.

<!-- qard-id: ap-880f607d3588bb85e1d6 -->
> [!qard]- What is the worst-case cost of brute-force string matching, and when does it occur?
> $m(n-m+1)\in\Theta(mn)$, when every alignment matches all but the last character (e.g. text `aaaa…`, pattern `aaab`).

<!-- qard-id: ap-85b40479e330cea3d965 -->
> [!qard]- What is its average case on natural language text?
> $\Theta(n)$ — mismatches usually happen within the first character or two.

### Closest Pair And Convex Hull

<!-- qard-id: ap-87752d7e88ff79b148b2 -->
> [!qard]- What is the brute-force closest-pair algorithm and its efficiency?
> Compute the distance for every pair of points and keep the minimum: $\Theta(n^2)$.

<!-- qard-id: ap-e1a30ae056eea113787b -->
> [!qard]- How can brute-force closest pair avoid the expensive square root?
> Compare squared distances — they give the same ordering.

<!-- qard-id: ap-39e9f6a89ba97549dfde -->
> [!qard]- Define a convex set and the convex hull.
> Convex: the segment between any two points stays in the set. Convex hull: the smallest convex set containing the points.

<!-- qard-id: ap-397d499bf93b067ae695 -->
> [!qard]- How does the brute-force convex hull algorithm work, and what does it cost?
> For each pair of points, check whether all other points lie on one side of their line; if so the segment is a hull edge. $\Theta(n^3)$.

### Exhaustive Search

<!-- qard-id: ap-4e336d8874d7df96e1f4 -->
> [!qard]- What is exhaustive search?
> Brute-force search over combinatorial objects: systematically list every candidate (no repeats, none missed), evaluate each, keep the best.

<!-- qard-id: ap-a0e279310695080a8744 -->
> [!qard]- What is the TSP and its exhaustive-search cost?
> Find the shortest tour visiting every city once and returning (shortest Hamiltonian circuit). $(n-1)!/2\in\Theta((n-1)!)$ tours.

<!-- qard-id: ap-44eaf393c0c7829067c9 -->
> [!qard]- What two tricks reduce TSP exhaustive search?
> Fix the start city, and ignore tours that differ only in direction.

<!-- qard-id: ap-922ded2a56ad1acb0797 -->
> [!qard]- What is the 0/1 knapsack problem and its exhaustive-search cost?
> Choose the most valuable subset of items whose total weight fits capacity $W$; all $2^n$ subsets, so $\Omega(2^n)$.

<!-- qard-id: ap-bea72167bc7fd82d0359 -->
> [!qard]- What is the assignment problem and its exhaustive-search cost?
> Assign $n$ people to $n$ jobs one-to-one minimising total cost $\sum C[i,j]$; try all $n!$ permutations, $\Theta(n!)$.

### Graph Traversal

<!-- qard-id: ap-482fc7492e409105bfe5 -->
> [!qard]- Which data structures do BFS and DFS use?
> BFS uses a queue; DFS uses a stack (or recursion).

<!-- qard-id: ap-d80351eb5274e6573665 -->
> [!qard]- What is the traversal time of BFS/DFS for adjacency matrix and adjacency list?
> Matrix: $\Theta(|V|^2)$. List: $\Theta(|V|+|E|)$.

<!-- qard-id: ap-8b01983747c5cad27748 -->
> [!qard]- When is exhaustive search acceptable?
> Only for very small instances, or when it (or a variant) is the only known solution; parallelism can help.
