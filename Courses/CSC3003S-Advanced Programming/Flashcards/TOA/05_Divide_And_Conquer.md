---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 05 — Divide And Conquer"
---

# TOA 05 — Divide And Conquer

**Source note:** [Divide And Conquer](../../TOA/05_Divide_And_Conquer.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Strategy And Recurrence Structure|Strategy And Recurrence Structure]]
  - [[#Mergesort|Mergesort]]
  - [[#Quicksort And Partition Mechanics|Quicksort And Partition Mechanics]]
  - [[#Quicksort Costs And Improvements|Quicksort Costs And Improvements]]
  - [[#Strassen Matrix Multiplication|Strassen Matrix Multiplication]]
  - [[#Closest Pair: Split, Solve And Straddle|Closest Pair: Split, Solve And Straddle]]
  - [[#QuickHull|QuickHull]]
  - [[#Sorting And Geometric Invariants|Sorting And Geometric Invariants]]

## Core Content

### Strategy And Recurrence Structure

<!-- qard-id: ap-d5e9230d84209c2e24ea -->
> [!qard]- What are the three stages of divide and conquer?
> Divide into smaller instances, solve all needed instances recursively with base cases, then combine their answers.

<!-- qard-id: ap-e71c721ef993a369dc88 -->
> [!qard]- What do the terms of $T(n)=aT(n/b)+f(n)$ count?
> $a$ recursive subproblems, each of size $n/b$, plus split/combine work $f(n)$. Dividing a sum into halves still processes linear total work, rather than making the whole computation logarithmic.

### Mergesort

<!-- qard-id: ap-7942ca0a3e44f58e0bd1 -->
> [!qard]- How does a merge combine two sorted lists?
> Repeatedly append the smaller next unconsumed entry; when one list is exhausted, append the remainder of the other.

<!-- qard-id: ap-98f3dec0be996942d432 -->
> [!qard]- What merge tie rule preserves stability?
> Take the entry from the left list first when keys are equal.

<!-- qard-id: ap-5690020d33286d02bcae -->
> [!qard]- What are mergesort's usual best, average, and worst time bounds?
> All are $\Theta(n\log n)$, since merging and copying still process entries at each level.

<!-- qard-id: ap-2215976109c588370659 -->
> [!qard]- What extra storage does standard array mergesort use?
> $\Theta(n)$ array storage plus logarithmic recursion depth.

<!-- qard-id: ap-d4b7cf6703f6c4e6bec9 -->
> [!qard]- What are mergesort's base case, odd-size split and worst-case comparison count?
> Zero or one entry is sorted; odd halves differ by one. A merge uses at most $n-1$ comparisons, giving $C(n)=2C(n/2)+n-1$ and $n\log_2n-n+1$ on powers of two.

### Quicksort And Partition Mechanics

<!-- qard-id: ap-f3344887d9035a951a18 -->
> [!qard]- How does the notes' two-scan quicksort partition work?
> Use the first value as pivot; scan inward, swap misplaced values, then place the pivot after the scans cross. Left entries are at most the pivot and right entries are at least it.

<!-- qard-id: ap-39c1fb0ab1843609b5ed -->
> [!qard]- Which ranges does quicksort recurse on after the pivot is placed at index $s$?
> The ranges ending at $s-1$ and starting at $s+1$, excluding the already placed pivot.

<!-- qard-id: ap-a6da4768ab4fc91acd45 -->
> [!qard]- Why do two-scan partitions need bounds checks and index advancement after swaps?
> Guards prevent scanning beyond the current range; advancing after swapping equal/misplaced values ensures progress rather than repeatedly visiting the same pair.

### Quicksort Costs And Improvements

<!-- qard-id: ap-ddef6ed30b61fc357362 -->
> [!qard]- What recurrence and cost describe balanced quicksort partitions?
> $T(n)=2T(n/2)+\Theta(n)$, giving $\Theta(n\log n)$.

<!-- qard-id: ap-3533afdeb6a650818dd8 -->
> [!qard]- What recurrence and cost describe maximally skewed quicksort partitions?
> $T(n)=T(n-1)+\Theta(n)$, giving $\Theta(n^2)$.

<!-- qard-id: ap-1055b19e918dc3658e4d -->
> [!qard]- What is ordinary quicksort's expected time, and what assumption is needed?
> $\Theta(n\log n)$ under usual random-pivot or random-input assumptions.

<!-- qard-id: ap-5a7aa6e9a2843f4ec329 -->
> [!qard]- How can quicksort bound its recursion-stack space even with poor pivots?
> Recurse on the smaller partition and iterate over the larger one. The recursion stack stays $O(\log n)$, although total work can still be quadratic.

<!-- qard-id: ap-ede7374a0800e090e41d -->
> [!qard]- How do mergesort and ordinary quicksort differ in stability, storage and pivot improvements?
> Tie-preserving mergesort is stable with a linear array buffer; ordinary quicksort is generally unstable with in-place partitioning and a stack. Median-of-three/random pivots improve typical behaviour without eliminating the quadratic worst case; small partitions may use insertion sort.

### Strassen Matrix Multiplication

<!-- qard-id: ap-021e43c744dff62a82be -->
> [!qard]- What changes in Strassen multiplication, and what recurrence results?
> Seven half-size matrix products replace eight, at the cost of extra block additions/subtractions: $T(n)=7T(n/2)+\Theta(n^2)$.

<!-- qard-id: ap-1478d236e55e932c520a -->
> [!qard]- What is Strassen's asymptotic arithmetic cost?
> $\Theta(n^{\log_2 7})$, with exponent $\log_2 7\approx2.807$.

<!-- qard-id: ap-591bd18978a707e66474 -->
> [!qard]- In the notes' Strassen convention, what are $P_1,P_2,P_3,P_4$?
> $P_1=A_{11}(B_{12}-B_{22})$; $P_2=(A_{11}+A_{12})B_{22}$; $P_3=(A_{21}+A_{22})B_{11}$; $P_4=A_{22}(B_{21}-B_{11})$.

<!-- qard-id: ap-624f0d3591810cbc7322 -->
> [!qard]- In the notes' Strassen convention, what are $P_5,P_6,P_7$?
> $P_5=(A_{11}+A_{22})(B_{11}+B_{22})$; $P_6=(A_{12}-A_{22})(B_{21}+B_{22})$; $P_7=(A_{11}-A_{21})(B_{11}+B_{12})$.

<!-- qard-id: ap-0b2834cf78319d56b5d4 -->
> [!qard]- How are Strassen's output blocks reconstructed?
> $C_{11}=P_5+P_4-P_2+P_6$; $C_{12}=P_1+P_2$; $C_{21}=P_3+P_4$; $C_{22}=P_1+P_5-P_3-P_7$.

<!-- qard-id: ap-f8d4ab347b5e3a3c363b -->
> [!qard]- What are Strassen's arithmetic recurrences and practical qualifications?
> Scalar products: $M(n)=7M(n/2)$, $M(1)=1$. Additions: $A(n)=7A(n/2)+18(n/2)^2$. Pad uneven dimensions and use scalar/small-size base cases; constants, crossover size and numerical behaviour affect practical value.

<!-- qard-id: ap-d588872e97ac453ae4b6 -->
> [!qard]- What is a block matrix, and why is it useful for recursive multiplication?
> A matrix partitioned into submatrices treated as algebraic blocks. Splitting each input into four compatible blocks expresses the product through smaller matrix products and block additions.

### Closest Pair: Split, Solve And Straddle

<!-- qard-id: ap-b5ec11055123b303f531 -->
> [!qard]- What preprocessing supports divide-and-conquer closest pair?
> Sort points horizontally and maintain a vertically ordered list as well.

<!-- qard-id: ap-ce1efce83c0b62532d24 -->
> [!qard]- What is the straddle strip in divide-and-conquer closest pair?
> After solving the halves, let $d$ be their smaller closest-pair distance. Any improving cross-boundary pair must have both points within $d$ of the dividing line.

<!-- qard-id: ap-d1b3ae5a696a25561ee3 -->
> [!qard]- How are strip points scanned efficiently?
> In vertical order; compare a point with successors only while their vertical separation is below the current best distance.

<!-- qard-id: ap-f95156997ddb99b6958f -->
> [!qard]- Why does the strip combine step take linear time?
> Within-half separation and geometric packing permit only a constant number of relevant successors per point.

<!-- qard-id: ap-a0a47776161fec0a9645 -->
> [!qard]- What recurrence gives efficient divide-and-conquer closest pair?
> $T(n)=2T(n/2)+\Theta(n)$, hence $\Theta(n\log n)$ including the initial sorts.

<!-- qard-id: ap-da200c7b4a5c8b1dc417 -->
> [!qard]- What can happen if vertical sorting is repeated at every recursion level?
> The work can rise to $\Theta(n\log^2n)$.

<!-- qard-id: ap-48713d9cb1f05a0994bf -->
> [!qard]- Why split closest-pair points by rank/identity and preserve vertical order?
> Equal $x$ coordinates must not unbalance the split. Partition the vertically sorted list by the same identities; re-sorting at every level can raise work to $\Theta(n\log^2n)$.

<!-- qard-id: ap-3e96910cebec2cd72b74 -->
> [!qard]- What closest-pair base cases and duplicate-point cases must be handled?
> Use brute force for a few points, such as at most three. Duplicate points give distance zero. A large strip is still tractable because geometric packing bounds relevant successors, not its total population.

### QuickHull

<!-- qard-id: ap-614edec845746b166824 -->
> [!qard]- How does QuickHull initialise and choose its next hull point?
> Begin with leftmost and rightmost points and process each side separately. For a candidate edge, choose an outer point farthest from its supporting line, then recurse on the two new edges.

<!-- qard-id: ap-85c7d23e98e4d8af8b04 -->
> [!qard]- Why can QuickHull discard points inside the triangle formed by its endpoints and farthest point?
> They cannot be outer hull vertices beyond the newly formed edges.

<!-- qard-id: ap-e8cef7904602f78ab63b -->
> [!qard]- What is QuickHull's base case for a candidate edge?
> If no outer point remains, emit the edge or its endpoint.

<!-- qard-id: ap-852d9fbe1c193a2aea90 -->
> [!qard]- What is QuickHull's worst-case time?
> $\Theta(n^2)$ when repeated scans make poor reductions.

<!-- qard-id: ap-3c24b10ad7723dc2c561 -->
> [!qard]- How does orientation identify QuickHull's farthest point, and what average-time qualification matters?
> For fixed endpoints, maximise the absolute determinant, proportional to perpendicular distance and twice triangle area. Average linear behaviour needs a favourable point model and substantial elimination; balanced recursion retaining most points costs $\Theta(n\log n)$.

### Sorting And Geometric Invariants

<!-- qard-id: ap-f6d526254a18e8f985eb -->
> [!qard]- Why does a stable merge choose the left record on equal keys?
> All records in the left half preceded those in the right half originally; preserving that precedence on ties maintains equal-key order across the merged halves.

<!-- qard-id: ap-66aaae622465c573cf76 -->
> [!qard]- Why does a merge stop comparing after one side is exhausted?
> The remaining entries of the other sorted side are already in correct relative order and no opposing entries remain to interleave; append them directly.

<!-- qard-id: ap-4a5176cd9cb577e8f55c -->
> [!qard]- Why can equal keys require explicit scan progress in a quicksort partition?
> Strict less/greater scans may both stop on equal values. After handling the pair, move indices or use a partition scheme designed to ensure progress.

<!-- qard-id: ap-7e2c33ba0f8b7b026162 -->
> [!qard]- How do balanced and skewed quicksort recursion depths affect ordinary stack use?
> Balanced calls have logarithmic depth; repeatedly peeling one value can give linear depth unless the implementation controls recursion by iterating on the larger side.

<!-- qard-id: ap-08b63acfc6aff7714338 -->
> [!qard]- Why can closest-pair strip pruning compare vertical separation with the current best distance?
> Euclidean distance is at least vertical separation; once that separation reaches the bound in y-order, later points cannot improve the best pair for this point.

<!-- qard-id: ap-ac0896f7a10bdf3ac69c -->
> [!qard]- Why is the closest-pair strip allowed to contain many points without quadratic combine work?
> Minimum separation within the already solved halves gives a geometric packing bound on relevant nearby successors for each point.

<!-- qard-id: ap-3faa8fab6757a54bda35 -->
> [!qard]- What does QuickHull's empty outer-point set establish about a candidate edge?
> No remaining candidate lies beyond that edge on its chosen side, so it can be emitted as a hull boundary under the selected collinearity convention.

<!-- qard-id: ap-218bdb2ab39273d96d0d -->
> [!qard]- Why is an explicit hull collinearity rule needed in both brute-force hull and QuickHull?
> A boundary may contain several collinear points; choose whether output lists only extreme vertices or all boundary points, and avoid reporting interior points/edges inconsistently.
