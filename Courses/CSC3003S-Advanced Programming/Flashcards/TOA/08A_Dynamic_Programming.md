---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 08A — Dynamic Programming A: Fibonacci, Coins And Transitive Closure"
---

# TOA 08A — Dynamic Programming A: Fibonacci, Coins And Transitive Closure

**Source note:** [Dynamic Programming A: Fibonacci, Coins And Transitive Closure](../../TOA/08A_Dynamic_Programming.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Dynamic Programming And Optimal Substructure|Dynamic Programming And Optimal Substructure]]
  - [[#Coin-Row Optimisation|Coin-Row Optimisation]]
  - [[#Minimum-Coin Change Making|Minimum-Coin Change Making]]
  - [[#Robot Coin Collection On A Grid|Robot Coin Collection On A Grid]]
  - [[#Transitive Closure And Warshall's Algorithm|Transitive Closure And Warshall's Algorithm]]
  - [[#Fibonacci With Stored Results|Fibonacci With Stored Results]]
  - [[#State, Dependencies And Reconstruction|State, Dependencies And Reconstruction]]

## Core Content

### Dynamic Programming And Optimal Substructure

<!-- qard-id: ap-80aff200735831a32dac -->
> [!qard]- What is dynamic programming?
> Solve overlapping subproblems once and store their answers for reuse, organised by a recurrence.

<!-- qard-id: ap-b5f71efc2a46d3e47d32 -->
> [!qard]- What is the principle of optimality?
> An optimal overall solution can be obtained from optimal solutions to the relevant subinstances.

<!-- qard-id: ap-0dff6bbff2f30011afec -->
> [!qard]- What are the main steps of a DP design?
> Define states, identify alternatives, derive recurrence and base cases, choose dependency order, fill the table, then reconstruct a solution if required.

<!-- qard-id: ap-c8d166fed4aead5f8672 -->
> [!qard]- Are overlapping subproblems and optimal substructure the same requirement?
> No. Overlap enables reuse; optimal substructure justifies constructing an optimum from suitable optimal substates. DP also solves non-optimisation tasks such as reachability.

### Coin-Row Optimisation

<!-- qard-id: ap-736490854ea39855833c -->
> [!qard]- What does coin-row state $F(i)$ represent?
> The maximum value selectable from the first $i$ coins subject to choosing no adjacent coins.

<!-- qard-id: ap-2310f551473cbe7d8508 -->
> [!qard]- What are the coin-row base cases for positive coin values?
> $F(0)=0$ and $F(1)=c_1$.

<!-- qard-id: ap-eba528b26f5c610d908b -->
> [!qard]- What is the coin-row recurrence?
> $F(i)=\max\{F(i-1),F(i-2)+c_i\}$ for $i\ge2$.

<!-- qard-id: ap-34aa5f75de54d5c44fe5 -->
> [!qard]- How is an optimal coin-row selection reconstructed?
> From $i=n$, exclude coin $i$ and move to $i-1$ if $F(i)=F(i-1)$; otherwise include it and move to $i-2$. Either optimal choice is valid on a tie.

<!-- qard-id: ap-8b68b5eb74e4dab925a3 -->
> [!qard]- What are coin-row DP's time and full-table-space costs?
> Both $\Theta(n)$.

<!-- qard-id: ap-55a91e622714875967a8 -->
> [!qard]- Why can rolling coin-row storage complicate reconstruction?
> Two previous values suffice for the optimum, but discarded earlier choices/table entries are needed for direct backtracking; retain decisions or recompute.

### Minimum-Coin Change Making

<!-- qard-id: ap-451b1318587d9eaffd9b -->
> [!qard]- What does state $F(a)$ mean in minimum-coin DP?
> The minimum number of coins needed to make exact amount $a$.

<!-- qard-id: ap-3204ff6414b55191b588 -->
> [!qard]- What base case and recurrence define minimum-coin DP?
> $F(0)=0$; $F(a)=1+\min_{j:d_j\le a}F(a-d_j)$. Initialise other amounts to infinity and fill in increasing amount order; if no predecessor is reachable, leave infinity.

<!-- qard-id: ap-15f3101f25597babb622 -->
> [!qard]- What information enables reconstruction of minimum-coin change?
> Store the denomination chosen for each improved amount, then repeatedly subtract the stored choice.

<!-- qard-id: ap-872b6393fd9b8e1f36b8 -->
> [!qard]- What happens if denomination $1$ is absent?
> Some amounts may remain unreachable with value infinity; reconstruction must detect failure.

<!-- qard-id: ap-bb9f81d774ecb7b76aed -->
> [!qard]- What are minimum-coin DP's time and space costs for target $n$ and $m$ denominations?
> $O(nm)$ time and $\Theta(n)$ storage for results and choices.

<!-- qard-id: ap-edc439095e99ca9a1bc7 -->
> [!qard]- How does amount-indexed change making differ from zero-one knapsack?
> Coin denominations can be reused indefinitely and state tracks remaining amount; zero-one knapsack tracks which items remain so none is reused. Amount-based costs can be pseudo-polynomial in bit input size.

### Robot Coin Collection On A Grid

<!-- qard-id: ap-26673451fc9f58a7a237 -->
> [!qard]- What does robot coin-grid state $F(i,j)$ represent?
> The maximum coins collected on a path from the top-left cell to $(i,j)$, using only right and down moves.

<!-- qard-id: ap-6538241d193654e0e9c7 -->
> [!qard]- What is the recurrence for an interior robot-grid cell?
> $F(i,j)=\max\{F(i-1,j),F(i,j-1)\}+c_{ij}$.

<!-- qard-id: ap-791f7d5334c2e5b28797 -->
> [!qard]- How are the robot-grid base case and boundary cells initialised?
> $F(1,1)=c_{11}$; accumulate along the first row and column: $F(1,j)=F(1,j-1)+c_{1j}$ and $F(i,1)=F(i-1,1)+c_{i1}$.

<!-- qard-id: ap-bda115abe6809a7cedff -->
> [!qard]- How is an optimal robot route reconstructed?
> Start at $(n,m)$ and move backwards to the predecessor with larger table value; choose either on ties and respect boundaries.

<!-- qard-id: ap-fe036ececd2519c3283d -->
> [!qard]- What are grid DP's time and full-table-space costs?
> $\Theta(nm)$ for an $n$-by-$m$ grid.

<!-- qard-id: ap-c46323b87302343b922f -->
> [!qard]- Which grid fill order and space reduction respect the robot recurrence?
> Row-major or column-major order with above/left states available. One rolling row gives value-only $O(m)$ storage, but direct reconstruction needs more information; backtracking through a full table takes $\Theta(n+m)$.

<!-- qard-id: ap-f2c8bc73556f04ee4929 -->
> [!qard]- What is the optimal collected value for coin grid $[[0,1,0],[1,0,1]]$ using right/down moves?
> Two. DP rows are $[0,1,1]$ and $[1,1,2]$. Either tied predecessor may be chosen when reconstructing an optimal route.

### Transitive Closure And Warshall's Algorithm

<!-- qard-id: ap-d795e643a3a0eaf62dc6 -->
> [!qard]- What is the transitive closure of a directed graph?
> A Boolean matrix indicating whether a directed path exists from each vertex to each other vertex.

<!-- qard-id: ap-05a14b57391730ff6b68 -->
> [!qard]- What does Warshall state $R^{(k)}[i,j]$ mean?
> A path from $i$ to $j$ exists using only vertices in $\{1,\ldots,k\}$ as intermediates.

<!-- qard-id: ap-84a7540e49f8c07633fd -->
> [!qard]- What is Warshall's recurrence?
> $R^{(k)}[i,j]=R^{(k-1)}[i,j]\lor(R^{(k-1)}[i,k]\land R^{(k-1)}[k,j])$.

<!-- qard-id: ap-319ad3ff2e739e4251f9 -->
> [!qard]- Which loop must remain outermost in Warshall?
> The intermediate-vertex loop $k$, followed by loops over origins $i$ and destinations $j$.

<!-- qard-id: ap-b32498557b3d32b3bb40 -->
> [!qard]- What are Warshall's time and space costs?
> $\Theta(n^3)$ time and $\Theta(n^2)$ space with one in-place matrix; storing every stage instead uses $\Theta(n^3)$ space.

<!-- qard-id: ap-af97559b96c69be46b0c -->
> [!qard]- How is Warshall initialised, and what changes for reflexive reachability?
> Start from the adjacency matrix for positive-length paths; set the diagonal to one as well if zero-length paths count. Under the first convention, diagonal ones indicate return paths/cycles.

### Fibonacci With Stored Results

<!-- qard-id: ap-3a84beb18708d587c6da -->
> [!qard]- How do Fibonacci tabulation and rolling storage illustrate DP's time–memory trade-off?
> Both avoid exponentially repeated subproblems, using linear arithmetic work. A full table stores all values; value-only rolling storage keeps two, while growing integer bit sizes still matter.

### State, Dependencies And Reconstruction

<!-- qard-id: ap-798574e6215e97402c1f -->
> [!qard]- Why is the meaning of a DP state part of the proof rather than merely a table label?
> The recurrence's alternatives and base cases must exactly solve that state; an ambiguous meaning can mix incompatible subproblems and invalidate the result.

<!-- qard-id: ap-67b72164dc9d2fa6a8fe -->
> [!qard]- How does a recurrence justify a bottom-up fill order?
> Every right-hand-side dependency must already be available, defining an acyclic dependency order; array row order is a consequence, not the definition of DP.

<!-- qard-id: ap-754d5996ea38d18470e0 -->
> [!qard]- Why does coin-row inclusion skip the immediately preceding position?
> Adjacency is defined in the original row, so selecting coin $i$ forbids $i-1$ and leaves the best compatible prefix ending at $i-2$.

<!-- qard-id: ap-a282bc66d5bb97c1a687 -->
> [!qard]- Why does minimum-coin DP consider every feasible last denomination?
> Every optimal nonempty change ends with some allowed coin; testing all such last choices avoids the unsupported greedy assumption that the largest must be right.

<!-- qard-id: ap-248bc7ed00578275d5b8 -->
> [!qard]- What happens to a change-making state with no reachable predecessor?
> It remains infinity/unreachable and has no reconstructible chosen coin; detect that result before following a choice chain.

<!-- qard-id: ap-273bc8e0dfe48be7cb6c -->
> [!qard]- Why must robot-grid boundary treatment respect the allowed moves?
> The starting cell and first row/column cannot receive paths from arbitrary outside positions. Explicit cumulative boundaries preserve the required start and right/down paths.

<!-- qard-id: ap-bb08ae47e5fc799e47c0 -->
> [!qard]- Why are zero virtual borders safe only under the note's nonnegative grid setup?
> With negative rewards they can admit an apparent path starting partway along a boundary, bypassing required negative cells; explicit legal base cases avoid that error.

<!-- qard-id: ap-977e5eb6ebe89bbb24f1 -->
> [!qard]- Why is the intermediate-vertex loop outermost in Warshall?
> Each stage must represent paths using the allowed set of intermediates. Mixing origins/destinations outside that stage order loses the recurrence's invariant.
