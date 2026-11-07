---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 05 — Divide And Conquer"
---

# TOA 05 — Divide And Conquer

**Source note:** [Divide And Conquer](../../TOA/05_Divide_And_Conquer.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Strategy|Strategy]]
  - [[#Mergesort|Mergesort]]
  - [[#Quicksort|Quicksort]]
  - [[#Strassen|Strassen]]
  - [[#Geometric Problems|Geometric Problems]]

## Core Content

### Strategy

<!-- qard-id: ap-a1c379a17dce99e45fe5 -->
> [!qard]- What are the three steps of divide and conquer?
> Divide into smaller instances, solve them recursively, combine their solutions.

<!-- qard-id: ap-bd240158a0335ab4a147 -->
> [!qard]- What recurrence form describes divide-and-conquer algorithms?
> $T(n)=aT(n/b)+f(n)$ with $a\ge1,b\ge2$.

### Mergesort

<!-- qard-id: ap-3d5cdef6452003d0fb1f -->
> [!qard]- Describe mergesort.
> Split the array into two halves, mergesort each recursively, then merge the two sorted halves.

<!-- qard-id: ap-c37575c5248e0dd58c7b -->
> [!qard]- How does merging two sorted arrays work?
> Repeatedly copy the smaller front element into the output; when one array runs out, copy the rest of the other.

<!-- qard-id: ap-dcab83563d51aa09ce9c -->
> [!qard]- What is mergesort's efficiency and its key pro and con?
> $\Theta(n\log n)$ in all cases ($C(n)=2C(n/2)+n-1$). Pro: stable. Con: $\Theta(n)$ extra space.

### Quicksort

<!-- qard-id: ap-b5299ddaab331db4b5c6 -->
> [!qard]- Describe quicksort.
> Pick a pivot, partition so smaller-or-equal elements precede it and larger follow, place the pivot in its final position, recurse on both parts.

<!-- qard-id: ap-30372511701c900eab47 -->
> [!qard]- How does Hoare partitioning work?
> $i$ scans right until $A[i]\ge p$, $j$ scans left until $A[j]\le p$; swap if $i<j$; when they cross, swap the pivot with $A[j]$.

<!-- qard-id: ap-af9b818f6830d5b3cfb1 -->
> [!qard]- What are quicksort's best, average and worst cases?
> Best and average $\Theta(n\log n)$; worst $\Theta(n^2)$ (skewed splits).

<!-- qard-id: ap-0a9b09f1f16236a6be91 -->
> [!qard]- What input causes quicksort's worst case with a first-element pivot?
> An already sorted array — every split leaves one side empty.

<!-- qard-id: ap-bc0afc762a48b5fdcebe -->
> [!qard]- Name three quicksort improvements.
> Median-of-three pivot selection, switching to insertion sort for small subarrays, eliminating recursion.

### Strassen

<!-- qard-id: ap-d6b0b18a8a8356adfa63 -->
> [!qard]- What is the key idea of Strassen's matrix multiplication?
> Split into $n/2$ blocks and compute the product with 7 block multiplications instead of 8, at the cost of extra additions.

<!-- qard-id: ap-ea6521533a92d33fbcd7 -->
> [!qard]- What is Strassen's complexity?
> $M(n)=7M(n/2)$ gives $\Theta(n^{\log_2 7})\approx\Theta(n^{2.81})$.

### Geometric Problems

<!-- qard-id: ap-5f6e349b6bf0ff0cd2a7 -->
> [!qard]- Describe divide-and-conquer closest pair.
> Sort by $x$, split at the median, solve each half giving $d=\min(d_l,d_r)$, then check pairs in the strip of width $2d$ around the dividing line.

<!-- qard-id: ap-a1cd05d8de451dab32eb -->
> [!qard]- Why does the strip check take only linear time?
> With strip points sorted by $y$, a packing argument shows each point need only be compared with the next 5.

<!-- qard-id: ap-17477aab5dda48e5694c -->
> [!qard]- What is the efficiency of divide-and-conquer closest pair?
> $T(n)=2T(n/2)+\Theta(n)$, so $\Theta(n\log n)$.

<!-- qard-id: ap-2353221601f34efa2b71 -->
> [!qard]- Describe QuickHull.
> Join the leftmost and rightmost points; find the farthest point from the line, discard points inside the triangle, and recurse on the outer sets for the upper and lower hulls.

<!-- qard-id: ap-ddfedd500b6df8892698 -->
> [!qard]- How is "farthest from the line" computed in QuickHull?
> By the largest triangle area $\tfrac12|\det|$ of the three points; the determinant's sign gives which side a point is on.

<!-- qard-id: ap-e043ec748d39d42141a0 -->
> [!qard]- What are QuickHull's average and worst cases?
> Average about linear ($\Theta(n)$ per the course); worst $\Theta(n^2)$.
