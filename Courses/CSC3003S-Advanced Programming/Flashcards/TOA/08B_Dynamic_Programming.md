---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 08B — Dynamic Programming B: Shortest Paths, Knapsack And Memoisation"
---

# TOA 08B — Dynamic Programming B: Shortest Paths, Knapsack And Memoisation

**Source note:** [Dynamic Programming B: Shortest Paths, Knapsack And Memoisation](../../TOA/08B_Dynamic_Programming.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Floyd's All-Pairs Shortest Paths|Floyd's All-Pairs Shortest Paths]]
  - [[#Recovering Floyd Paths|Recovering Floyd Paths]]
  - [[#Zero-One Knapsack State And Recurrence|Zero-One Knapsack State And Recurrence]]
  - [[#Knapsack Reconstruction And Storage|Knapsack Reconstruction And Storage]]
  - [[#Memory Functions And Memoisation|Memory Functions And Memoisation]]
  - [[#DP Formulation And Limits|DP Formulation And Limits]]
  - [[#Knapsack Source Table And Reconstruction|Knapsack Source Table And Reconstruction]]
  - [[#Shortest Paths And Item-State DP|Shortest Paths And Item-State DP]]

## Core Content

### Floyd's All-Pairs Shortest Paths

<!-- qard-id: ap-28e6a9a74a078180bff4 -->
> [!qard]- What does Floyd state $D^{(k)}[i,j]$ represent?
> Shortest path cost from $i$ to $j$ when only vertices in $\{1,\ldots,k\}$ may be intermediates.

<!-- qard-id: ap-36b8e07fba0c7a910fb2 -->
> [!qard]- How is Floyd's initial distance matrix formed?
> Put $0$ on the diagonal, direct edge weights on existing connections, and infinity where there is no edge.

<!-- qard-id: ap-a50389a59f90b32a4ef2 -->
> [!qard]- What is Floyd's recurrence?
> $D^{(k)}[i,j]=\min\{D^{(k-1)}[i,j],D^{(k-1)}[i,k]+D^{(k-1)}[k,j]\}$.

<!-- qard-id: ap-742a931ec38fe8b3290a -->
> [!qard]- Which loop must remain outermost in Floyd's algorithm?
> The intermediate-vertex loop $k$, preserving the allowed-intermediate state order.

<!-- qard-id: ap-e01d02c5948fa57149ed -->
> [!qard]- Why check that both legs are finite before adding Floyd distances?
> Finite infinity sentinels can overflow or create invalid values when added.

<!-- qard-id: ap-255ce7eebbdfae1dbaf4 -->
> [!qard]- What are Floyd's time and matrix-space costs?
> $\Theta(n^3)$ time and $\Theta(n^2)$ space.

<!-- qard-id: ap-dbe6a20d9e2b0c25a71f -->
> [!qard]- How does Floyd handle negative edges and negative cycles?
> Negative edges are allowed. A negative final diagonal entry reveals a negative cycle; pairs able to travel through such a cycle have no finite shortest-path value.

<!-- qard-id: ap-c826eaf7b2f5bc79962d -->
> [!qard]- How do Floyd and Warshall differ in stored values and operations?
> Floyd stores distances, takes minimum, and joins by addition; Warshall stores Booleans, takes OR, and joins by AND.

### Recovering Floyd Paths

<!-- qard-id: ap-ce1cd7648a2fba3ea721 -->
> [!qard]- What is Floyd's intermediate matrix $P$?
> A matrix recording the intermediate vertex responsible for a strict distance improvement.

<!-- qard-id: ap-15f02da0a5283e4de3d6 -->
> [!qard]- How are internal vertices recovered from Floyd's intermediate matrix?
> If $k=P[i,j]\ne0$, recursively recover $i$ to $k$, print $k$, then recover $k$ to $j$.

<!-- qard-id: ap-61476c5b16ef9d2c9f40 -->
> [!qard]- What initialisation, tie and endpoint rules matter for Floyd path reconstruction?
> Initialise $P$ to zero with one-based vertex labels; update on strict improvements only. The recursive helper prints internal vertices; the wrapper checks reachability and adds endpoints, avoiding a duplicate endpoint when start equals goal.

### Zero-One Knapsack State And Recurrence

<!-- qard-id: ap-94221a5add16b9f4d3ba -->
> [!qard]- What does knapsack state $V[i,j]$ mean?
> Maximum value obtainable from the first $i$ items within capacity $j$.

<!-- qard-id: ap-95b76e73a2dcd3a872c3 -->
> [!qard]- What are the zero-one knapsack base cases?
> $V[0,j]=0$ and $V[i,0]=0$.

<!-- qard-id: ap-bf3f443db9d81021e74c -->
> [!qard]- What is the zero-one knapsack recurrence?
> If $j<w_i$, $V[i,j]=V[i-1,j]$. Otherwise $V[i,j]=\max\{V[i-1,j],V[i-1,j-w_i]+v_i\}$: exclude or include item $i$.

<!-- qard-id: ap-1b2aa564f79353e8438c -->
> [!qard]- Why do both zero-one knapsack branches use the previous item row?
> To prevent including the current item more than once.

### Knapsack Reconstruction And Storage

<!-- qard-id: ap-0556f6def6fb444dc048 -->
> [!qard]- How is a zero-one knapsack solution reconstructed?
> Start at $(n,W)$. If $V[i,j]=V[i-1,j]$, exclude item $i$; otherwise include it and subtract $w_i$ from $j$. Decrease $i$ each step; ties permit either optimal branch.

<!-- qard-id: ap-555c361767d27d00d9be -->
> [!qard]- What are full-table zero-one knapsack DP's time and space costs?
> Both are $\Theta(nW)$ for $n$ positive-integer-weight items and integer capacity $W$. Backtracking takes $O(n)$ time.

<!-- qard-id: ap-ccf5d9b103db3f68c6a0 -->
> [!qard]- Why must one-row zero-one knapsack update capacities in descending order?
> So an inclusion reads an earlier-item state, not a newly updated state that would reuse the current item.

### Memory Functions And Memoisation

<!-- qard-id: ap-1793bc56785dca0fe198 -->
> [!qard]- What is memoisation, also called a memory function?
> A top-down recursive method caching each computed state's answer and returning it on repeated requests.

<!-- qard-id: ap-7180dc3dc13f2b197c81 -->
> [!qard]- How do tabulation and memoisation differ in traversal order?
> Tabulation is bottom up; memoisation follows top-down recursive requests.

<!-- qard-id: ap-97f432dc0a9b9db3493a -->
> [!qard]- Why must the uncomputed sentinel be distinguishable from valid answers?
> Otherwise a valid result could be treated as missing and recomputed, or an uncomputed state could be returned incorrectly.

<!-- qard-id: ap-aa73dccb960ec76cd14a -->
> [!qard]- What are the worst-case visited-state count and stack depth for memoised knapsack?
> $O(nW)$ visited states and $O(n)$ stack depth.

<!-- qard-id: ap-667b8537e64019cab87e -->
> [!qard]- How does a memoised knapsack call process an uncomputed state?
> Return zero at a base row/capacity. If cached, reuse it; otherwise recurse to exclude the item, and also include it if it fits, cache the maximum and return it. Use a sentinel distinct from valid answers.

<!-- qard-id: ap-41cbce7a056f067ca88e -->
> [!qard]- Does on-demand memoisation necessarily use less allocated memory than tabulation?
> No. A preallocated rectangular cache remains $\Theta(nW)$ even if many states are unvisited. A sparse cache stores visited states only, with extra lookup overhead and recursion stack.

### DP Formulation And Limits

<!-- qard-id: ap-5d38e24f4cb2608a0f17 -->
> [!qard]- Why is knapsack's $\Theta(nW)$ bound pseudo-polynomial?
> It is polynomial in numeric capacity $W$, but $W$ is encoded in only $\Theta(\log W)$ bits, so it is not polynomial in complete input bit length.

<!-- qard-id: ap-e3e832c88e4912e0740e -->
> [!qard]- Why is selecting the right DP state a correctness issue?
> The state must contain everything affecting future feasible choices and costs; conflating histories with different remaining possibilities can make the recurrence invalid. Even correct states may be too numerous to store.

### Knapsack Source Table And Reconstruction

<!-- qard-id: ap-7d74066d1320d5f77924 -->
> [!qard]- Why does a one-row zero-one knapsack need descending capacities, and what is lost?
> It reads previous-item states before they are overwritten, preventing repeated use of an item. Space becomes $\Theta(W)$, but the value-only row does not retain a straightforward reconstruction history.

### Shortest Paths And Item-State DP

<!-- qard-id: ap-c2210c05bff969ec00fb -->
> [!qard]- What do finite and infinite entries mean at the end of Floyd?
> A finite entry is the minimum reachable cost under the stated no-affecting-negative-cycle assumption; infinity means the destination is unreachable from that origin.

<!-- qard-id: ap-326be9f8a6c530cc07e4 -->
> [!qard]- Why does Floyd need the allowed-intermediate recurrence rather than simply choosing the smallest outgoing edge?
> The optimum can involve several edges and must compare whole path costs through permitted intermediate vertices; a local edge choice has no general shortest-path guarantee.

<!-- qard-id: ap-3a702f4ad5762968df73 -->
> [!qard]- Why should an infinity sentinel never participate in ordinary distance arithmetic unchecked?
> A finite representation may overflow or produce a bogus improvement, especially with negative edges; first establish that both legs exist.

<!-- qard-id: ap-ea60d597217387cc7ee2 -->
> [!qard]- Why does zero-one knapsack refer to row $i-1$ even in its include branch?
> That row excludes the current item from future selection, so the same listed item cannot be included again.

<!-- qard-id: ap-69db0e070e9b5895964b -->
> [!qard]- How does the knapsack “too heavy” branch simplify the decision?
> If $w_i>j$, inclusion is infeasible and the answer is exactly the previous-item optimum at the same capacity.

<!-- qard-id: ap-e66cb12cc290e90e8e3f -->
> [!qard]- Why can backtracking through equal knapsack values choose exclusion without losing optimality?
> Equality proves an optimum exists without the item; inclusion may also be optimal, but one correct solution is enough unless all optima are requested.

<!-- qard-id: ap-837852872b5258a4ed95 -->
> [!qard]- What overhead remains in memoisation even when relatively few states are requested?
> Cache representation/initialisation, lookups and recursive stack work. A dense preallocated cache may still allocate all states despite on-demand computation.

<!-- qard-id: ap-d699f24ac1aeea55b418 -->
> [!qard]- Why does numeric capacity create pseudo-polynomial rather than bit-polynomial knapsack time?
> Doubling the number of capacity bits can allow an exponentially larger numeric capacity/table; $nW$ is polynomial in the value $W$, not its encoded length.
