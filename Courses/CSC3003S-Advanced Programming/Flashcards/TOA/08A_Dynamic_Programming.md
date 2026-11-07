---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 08A — Dynamic Programming I"
---

# TOA 08A — Dynamic Programming I

**Source note:** [Dynamic Programming I](../../TOA/08A_Dynamic_Programming.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Principle|Principle]]
  - [[#Coin Row|Coin Row]]
  - [[#Change Making|Change Making]]
  - [[#Robot Coin Collection|Robot Coin Collection]]
  - [[#Warshall|Warshall]]

## Core Content

### Principle

<!-- qard-id: ap-0ba3747b4db38a07490a -->
> [!qard]- What is dynamic programming?
> Solving a problem by storing optimal solutions to overlapping subproblems, each solved once, via a recurrence relation.

<!-- qard-id: ap-6e01d1730f3764b1f545 -->
> [!qard]- What is the principle of optimality?
> An optimal solution can be built from optimal solutions to its sub-instances; DP requires it.

<!-- qard-id: ap-90d9b16beb2865a89ceb -->
> [!qard]- Who invented dynamic programming, and what does "programming" mean in the name?
> Richard Bellman in the 1950s; "programming" means planning.

<!-- qard-id: ap-8e519adf2e00ef99db99 -->
> [!qard]- Why is DP a space–time trade-off?
> It stores subproblem answers in a table to avoid recomputing them.

### Coin Row

<!-- qard-id: ap-056f2e3e778a85141c0b -->
> [!qard]- State the coin-row recurrence.
> $F(0)=0,\ F(1)=c_1,\ F(n)=\max\{F(n-2)+c_n,\ F(n-1)\}$.

<!-- qard-id: ap-e8355ce9b2138445d239 -->
> [!qard]- How do you recover which coins were chosen in the coin-row problem?
> Backtrack from $F(n)$: if it came from $F(n-2)+c_n$ take coin $n$ and jump to $n-2$, else move to $n-1$ (or store each choice).

### Change Making

<!-- qard-id: ap-895d4179d5b72400f9d5 -->
> [!qard]- State the change-making recurrence.
> $F(0)=0,\ F(n)=\min_{j:\,n\ge d_j}F(n-d_j)+1$.

<!-- qard-id: ap-85d242929dd6233f912a -->
> [!qard]- Why use DP for change making instead of greedy?
> Greedy is optimal only for typical coin systems; DP is correct for any denominations.

### Robot Coin Collection

<!-- qard-id: ap-87ec60607b22fa0b4f73 -->
> [!qard]- State the robot coin-collection recurrence.
> $F(i,j)=\max\{F(i-1,j),F(i,j-1)\}+c_{ij}$, with $F(0,j)=F(i,0)=0$.

<!-- qard-id: ap-100f1cd1095b22ced1a2 -->
> [!qard]- What are the costs of filling the robot table and of backtracing the path?
> Filling: $\Theta(nm)$ time and space. Backtracing: $\Theta(n+m)$.

<!-- qard-id: ap-3eabb84fa1c4b84fd5c6 -->
> [!qard]- How do you backtrace the robot's path?
> From $(n,m)$, move to whichever of above/left has the larger $F$ (either if equal).

### Warshall

<!-- qard-id: ap-d51c2987a05d9463b04d -->
> [!qard]- What is the transitive closure of a directed graph?
> The Boolean matrix with $t_{ij}=1$ iff there is a directed path from $i$ to $j$.

<!-- qard-id: ap-980b9eb536d67f798b8f -->
> [!qard]- What does $R^{(k)}[i,j]=1$ mean in Warshall's algorithm?
> There is a path from $i$ to $j$ using only vertices $1..k$ as intermediates.

<!-- qard-id: ap-ff04502329a8ec56aa7c -->
> [!qard]- State Warshall's update rule.
> $R^{(k)}[i,j]=R^{(k-1)}[i,j]\lor\big(R^{(k-1)}[i,k]\land R^{(k-1)}[k,j]\big)$.

<!-- qard-id: ap-5ef45d6700846fe9f94d -->
> [!qard]- What is a quick hand rule for computing $R^{(k)}$?
> Set $(i,j)$ to 1 where row $k$ has a 1 in column $j$ and column $k$ has a 1 in row $i$.

<!-- qard-id: ap-284ff7f80168da01a3d4 -->
> [!qard]- What are Warshall's time and space costs?
> $\Theta(n^3)$ time; $\Theta(n^2)$ space if one matrix is updated in place.

<!-- qard-id: ap-df9f729be173702d9f5a -->
> [!qard]- Why does a sink vertex add no paths at its stage of Warshall?
> It has no outgoing edges, so no path can continue through it.
