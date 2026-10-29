---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 04 — Decrease And Conquer"
---

# TOA 04 — Decrease And Conquer

**Source note:** [Decrease And Conquer](../../TOA/04_Decrease_And_Conquer.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Strategy And Variants|Strategy And Variants]]
  - [[#Insertion Sort|Insertion Sort]]
  - [[#Topological Sorting|Topological Sorting]]
  - [[#Generating The Power Set|Generating The Power Set]]
  - [[#Permutations By Insertion And Johnson–Trotter|Permutations By Insertion And Johnson–Trotter]]
  - [[#Binary Search And Exponentiation|Binary Search And Exponentiation]]
  - [[#Fake-Coin Detection|Fake-Coin Detection]]
  - [[#Russian Multiplication|Russian Multiplication]]
  - [[#Euclid And Quickselect|Euclid And Quickselect]]
  - [[#Interpolation Search|Interpolation Search]]
  - [[#Reduction And Enumeration Details|Reduction And Enumeration Details]]

## Core Content

### Strategy And Variants

<!-- qard-id: ap-327e9a6ca1c001815fbd -->
> [!qard]- What are the three decrease-and-conquer variants, with examples?
> Constant decrease ($n-1$: insertion sort); constant-factor decrease ($n/2$: binary search); variable decrease (input-dependent remainder: Euclid).

<!-- qard-id: ap-a7acb809154a8f66fe10 -->
> [!qard]- How does decrease and conquer differ from divide and conquer?
> It solves one smaller instance; divide and conquer solves multiple smaller instances and combines them.

### Insertion Sort

<!-- qard-id: ap-68f3cf2630c29d2d6b09 -->
> [!qard]- What invariant supports insertion sort's correctness?
> Before each insertion, the existing prefix is sorted; inserting the next element correctly produces a longer sorted prefix.

<!-- qard-id: ap-aa85f42cbba8a3e1b445 -->
> [!qard]- What are the steps of one insertion-sort insertion?
> Save the next element, shift larger prefix elements right, then place the saved element in the gap.

<!-- qard-id: ap-8f89730ae85d28bde34c -->
> [!qard]- What is insertion sort's worst-case time and shift count?
> Reverse-sorted input causes $n(n-1)/2$ shifts and $\Theta(n^2)$ time.

<!-- qard-id: ap-0b4f0b6faf22da11ff42 -->
> [!qard]- What is insertion sort's best-case time?
> $\Theta(n)$ on already sorted input, with one key comparison per insertion.

<!-- qard-id: ap-3421c8f2ce0d55f268fc -->
> [!qard]- Why is ordinary insertion sort stable, and what are its average and space costs?
> Shift only strictly larger keys so equal-key order is preserved. Random-permutation average time is $\Theta(n^2)$; iterative auxiliary space is $\Theta(1)$, while explicit recursion can add stack space.

### Topological Sorting

<!-- qard-id: ap-c1072d03ba5ba0c61858 -->
> [!qard]- What is a topological ordering?
> A vertex ordering in which every directed edge's source appears before its destination.

<!-- qard-id: ap-958d157f3ea0a5a07979 -->
> [!qard]- When does a directed graph have a topological ordering?
> Exactly when it is acyclic; a directed cycle prevents any valid ordering.

<!-- qard-id: ap-4743d2ffdad3c8f44720 -->
> [!qard]- How does source-removal topological sorting work, and what is its cost?
> Start with all zero-indegree vertices. Output one, decrement its outgoing neighbours' indegrees, and add any new zero-indegree vertices. Adjacency lists give $\Theta(|V|+|E|)$ time.

<!-- qard-id: ap-66a28856a79aede20311 -->
> [!qard]- How does source-removal topological sorting detect a cycle?
> If the source collection empties before all vertices are output, a cycle remains.

<!-- qard-id: ap-566747787d05e249c1c4 -->
> [!qard]- How does DFS produce a topological order?
> Check for directed cycles; if none exist, reverse the vertex finish order. A cycle makes a topological ordering impossible.

<!-- qard-id: ap-ba7710da89cb5ef38c38 -->
> [!qard]- What are indegree and a source vertex, and can a DAG have several topological orders?
> Indegree counts incoming edges; a source has zero in the remaining graph. Multiple available sources allow different valid orders, all respecting the dependencies.

### Generating The Power Set

<!-- qard-id: ap-4715a50f9f8f7c03390e -->
> [!qard]- How many subsets does a set of $n$ distinct elements have?
> $2^n$.

<!-- qard-id: ap-79d2d11ae5d3c2fe0093 -->
> [!qard]- What property does binary reflected Gray code give subset enumeration?
> Consecutive masks differ in exactly one bit, so consecutive subsets add or remove one element.

<!-- qard-id: ap-4d7848577febeb216789 -->
> [!qard]- What recurrence generates a power set by extending smaller subsets?
> $\mathcal P(\varnothing)=\{\varnothing\}$; retain every subset of $S$ and add a copy containing the new element $a$: $\mathcal P(S\cup\{a\})=\mathcal P(S)\cup\{X\cup\{a\}:X\in\mathcal P(S)\}$.

<!-- qard-id: ap-fca3be2c73cfacd16f0d -->
> [!qard]- How do bit masks and reflected Gray codes enumerate subsets?
> Bit $i$ records membership of element $i$. Ordinary masks run from $0$ to $2^n-1$; Gray code $g(i)=i\oplus\lfloor i/2\rfloor$ changes one bit per step. Explicitly writing all subset elements costs $\Theta(n2^n)$.

### Permutations By Insertion And Johnson–Trotter

<!-- qard-id: ap-3371a98580a4975e04ab -->
> [!qard]- How does insertion-based permutation generation extend a smaller answer?
> Insert the new largest element into each of the $n$ positions of every $(n-1)$-element permutation, producing all $n!$ permutations.

<!-- qard-id: ap-659193bf37f1eacaaa11 -->
> [!qard]- What is a mobile element in Johnson–Trotter enumeration?
> An element whose direction points to an adjacent smaller element.

<!-- qard-id: ap-40e2afcba13b561729a1 -->
> [!qard]- What is one Johnson–Trotter step, and when does it stop?
> Move the largest mobile element by swapping it with the adjacent smaller element its arrow points to; reverse all larger elements' arrows. Each output differs by one adjacent swap. Stop when no element is mobile.

<!-- qard-id: ap-07310c9e155397696733 -->
> [!qard]- How is Johnson–Trotter initialised, and what does a simple implementation cost?
> Start ascending, all arrows left. Scan for the largest mobile value and reverse larger arrows after each move: $O(n)$ per permutation, $O(n\,n!)$ total and $O(n)$ working storage when streaming outputs.

<!-- qard-id: ap-5138f32abcc14aad6942 -->
> [!qard]- Why alternate insertion direction when generating permutations from smaller permutations?
> Moving the new largest value right-to-left then left-to-right preserves adjacent-swap minimal change across consecutive outputs.

### Binary Search And Exponentiation

<!-- qard-id: ap-8555fe41c611ead393c4 -->
> [!qard]- What precondition and recurrence give binary search its worst-case bound?
> The input is sorted. Discard the half that cannot contain the target: $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)$, giving $\Theta(\log n)$ comparisons.

<!-- qard-id: ap-e5b762d2985c40454ac6 -->
> [!qard]- What formula underlies exponentiation by squaring for nonnegative integer $n$?
> $a^0=1$; for positive even $n$, $a^n=(a^{\lfloor n/2\rfloor})^2$; for odd $n$, $a^n=a(a^{\lfloor n/2\rfloor})^2$.

<!-- qard-id: ap-bd83442e705f80bbf7c4 -->
> [!qard]- Why cache the half-power in exponentiation by squaring?
> Compute it once, then reuse it when squaring. This gives $\Theta(\log n)$ multiplications; two recursive calls would repeat the work.

<!-- qard-id: ap-a37e83408ce079904eee -->
> [!qard]- What is binary search's best case, and how does it differ from its worst-case recurrence?
> An immediate midpoint match takes $\Theta(1)$; repeatedly halving the remaining interval gives $\Theta(\log n)$ worst-case comparisons.

### Fake-Coin Detection

<!-- qard-id: ap-d78351ae9c3a3b74eb56 -->
> [!qard]- Why can three-way fake-coin detection use fewer weighings than two-way detection?
> With exactly one lighter coin, weigh two equal-sized groups and use lighter-left, lighter-right or balance to select one of three candidate groups. The information lower bound is $\lceil\log_3 n\rceil$ weighings, achievable with suitable balanced groups.

<!-- qard-id: ap-f64d48843723654c8aa7 -->
> [!qard]- How do two-group and three-group fake-coin partitions handle leftover coins?
> With one lighter coin, two groups weigh $\lfloor n/2\rfloor$ against the same count, leaving at most one aside. Three groups use $q,q,q$ for $3q$; $q,q,q+1$ for $3q+1$; and $q+1,q+1,q$ for $3q+2$.

<!-- qard-id: ap-8c5e86e5ef43e6ce7c87 -->
> [!qard]- How do the two-group and three-group weighing counts compare for one lighter coin?
> The notes' two-group strategy has worst count $\lfloor\log_2 n\rfloor$; a suitable near-equal three-group strategy achieves $\lceil\log_3 n\rceil$. Both are logarithmic, but three balance outcomes can reduce the constant factor.

### Russian Multiplication

<!-- qard-id: ap-0fef1a2ed518a3d06ca6 -->
> [!qard]- What identities justify Russian multiplication?
> If $n$ is even, $nm=(n/2)(2m)$; if odd, $nm=\lfloor n/2\rfloor(2m)+m$.

<!-- qard-id: ap-358701bd68ef854879b5 -->
> [!qard]- How is Russian multiplication implemented, and what does $50\times20$ illustrate?
> While the first nonnegative operand is positive, add the second when the first is odd, halve the first with floor and double the second. For $50\times20$, add $40+320+640=1000$; iterations are logarithmic, with bit costs analysed separately.

### Euclid And Quickselect

<!-- qard-id: ap-24059236afe861344138 -->
> [!qard]- Why is Euclid a variable-size decrease algorithm?
> The remainder in $\gcd(m,n)=\gcd(n,m\bmod n)$ determines the next instance size from the input.

<!-- qard-id: ap-b6cd99cc931cc0187c0a -->
> [!qard]- How does quickselect choose its next action after partitioning at index $s$?
> Return the pivot if $s$ equals the target; otherwise recurse left or right according to the target's position.

<!-- qard-id: ap-670b9e2da0b6d4264159 -->
> [!qard]- What are quickselect's expected and worst-case time bounds?
> Expected $\Theta(n)$ with random pivots; balanced pivots also give linear time. Repeatedly reducing by only one irrelevant element gives $\Theta(n^2)$ worst case.

<!-- qard-id: ap-1f7a7321ff2cac32051a -->
> [!qard]- What index represents the $k$th order statistic, and what partition contract does quickselect require?
> Target index $k-1$ in a zero-based array. The partition must place its pivot in its final position so the target determines which one side remains relevant; stop at a singleton or matching pivot.

### Interpolation Search

<!-- qard-id: ap-9497be133c9bb7e33c64 -->
> [!qard]- When is interpolation search fast, and what is its worst case?
> On sorted numeric keys with a suitable approximately uniform distribution, a value-based probe gives expected $O(\log\log n)$ time. Skewed distributions can give $O(n)$ worst-case time.

<!-- qard-id: ap-19cbdc2b6c7a8a586e6f -->
> [!qard]- What is interpolation search's probe formula, and what guards prevent invalid probes?
> $x=l+\lfloor(v-A[l])(r-l)/(A[r]-A[l])\rfloor$. Ensure the key is within endpoint values; handle equal endpoints without division; keep the probe in bounds and exclude it from the next interval.

### Reduction And Enumeration Details

<!-- qard-id: ap-78484efa185a9158e1f6 -->
> [!qard]- Why can decrease-and-conquer be implemented bottom up as well as recursively?
> If the smaller solution can be extended in an increasing sequence of sizes, iteration can build the same inductive result without retaining recursive frames.

<!-- qard-id: ap-fa857c8448738e55f87d -->
> [!qard]- What initial condition and invariant support recursive insertion sort?
> Inputs of size at most one are sorted. Recursively sort the first $n-1$ entries, then insert the last into that sorted prefix without losing or duplicating elements.

<!-- qard-id: ap-a0ca3200e9be39030ef7 -->
> [!qard]- Why does source removal fail precisely when a directed cycle remains with no available source?
> Every vertex on a cycle has an incoming edge from another cycle vertex, preventing their indegrees from dropping to zero through source removal alone.

<!-- qard-id: ap-8e3dbdffbe9d64aa972a -->
> [!qard]- What condition makes Johnson–Trotter's arrow-directed element mobile?
> Its indicated neighbour exists and is smaller; boundary-pointing arrows and arrows toward larger values are not mobile.

<!-- qard-id: ap-97a25d2fad270435c82d -->
> [!qard]- Why does materialising every permutation cost more than merely counting $n!$ outputs?
> Writing each full length-$n$ permutation requires $\Theta(n)$ element-output work, so explicit total output alone is $\Theta(n\,n!)$.

<!-- qard-id: ap-fbf311ba7368041e3d8f -->
> [!qard]- Why must the groups placed on a balance contain the same number of genuine-weight coins in the fake-coin model?
> Otherwise ordinary group size creates an imbalance unrelated to which coin is lighter, invalidating the outcome-based reduction.

<!-- qard-id: ap-e21d60ea084a154b9990 -->
> [!qard]- What distinguishes lower median selection from averaging two central values on even-size input?
> Lower median is one order statistic, rank $\lceil n/2\rceil$; averaging two middle entries requires both central values and may not be an input element.

<!-- qard-id: ap-ef70deff505620c68b39 -->
> [!qard]- After an unsuccessful interpolation probe, why exclude the probed index from the next interval?
> Its value is already known not to match; keeping it can prevent the interval shrinking and cause repeated probes or nontermination.
