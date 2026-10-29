---
tags:
  - advanced-programming
---

# Divide And Conquer

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)  
**Source**: [5 - TOA Divide and Conquer - Copy.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/5%20-%20TOA%20Divide%20and%20Conquer%20-%20Copy.pdf), Patrick Marais, University of Cape Town, PDF pages 1–21  
**Generated**: 2026-10-02

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes. Examples and corrections appear beside the relevant concept.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Strategy And Recurrence Structure|Strategy And Recurrence Structure]]
  - [[#Mergesort|Mergesort]]
  - [[#Quicksort And Partition Mechanics|Quicksort And Partition Mechanics]]
  - [[#Quicksort Costs And Improvements|Quicksort Costs And Improvements]]
  - [[#Strassen Matrix Multiplication|Strassen Matrix Multiplication]]
  - [[#Closest Pair: Split, Solve And Straddle|Closest Pair: Split, Solve And Straddle]]
  - [[#QuickHull|QuickHull]]

---

## Core Content

### Strategy And Recurrence Structure

#### Definitions

> **Divide and conquer**: Divide an instance into smaller instances, solve them recursively, and combine their solutions.

1. Divide the input into two or more smaller instances.
2. Solve each needed instance recursively, with explicit base cases.
3. Combine the answers to recover the original solution.

![Divide and conquer split and combine](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/05_Divide_And_Conquer/divide-combine.svg)

*Both subproblem answers contribute to the original answer.*

For equal-sized parts:

$$
T(n)=aT(n/b)+f(n),
$$

where $a$ is the number of recursive subproblems, $b$ is the size-reduction factor, and $f(n)$ includes splitting and combining. Even summing an array can be expressed as the sum of the sums of its two halves; this still takes linear total work.

### Mergesort

#### Definitions

> **Mergesort**: Recursively sort two halves and merge the sorted results.

> **Merge**: Combine two sorted lists by repeatedly selecting the smaller of their next unconsumed entries.

```python
MergeSort(A):
    if length(A) <= 1: return A
    middle = floor(length(A) / 2)
    left = MergeSort(A[0 .. middle - 1])
    right = MergeSort(A[middle .. length(A) - 1])
    return Merge(left, right)

Merge(B, C):
    i = 0; j = 0
    result = empty list
    while i < length(B) and j < length(C):
        if B[i] <= C[j]:
            append B[i] to result; i = i + 1
        else:
            append C[j] to result; j = j + 1
    append unconsumed B entries to result
    append unconsumed C entries to result
    return result
```

Selecting from the left list on a tie preserves stability. Odd input sizes produce halves differing by one.

![Source mergesort tree](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/05_Divide_And_Conquer/mergesort.svg)

*Splitting 7, 2, 1, 6, 4 into singletons and merging yields 1, 2, 4, 6, 7.*

A merge of total size $n$ uses at most $n-1$ key comparisons. For powers of two:

$$
C(n)=2C(n/2)+(n-1),\quad C(1)=0,\qquad
C_{\mathrm{worst}}(n)=n\log_2n-n+1.
$$

The complete algorithm runs in $\Theta(n\log n)$ time in the usual best, average and worst cases, because copying and merging still process the entries. Standard array mergesort uses $\Theta(n)$ extra storage plus logarithmic recursion depth.

### Quicksort And Partition Mechanics

#### Definitions

> **Pivot**: A chosen value used to separate smaller and larger entries.

> **Partitioning**: Rearrange entries into regions according to their relationship with the pivot.

The source chooses the first value as pivot. Two scans move inward, swapping values found on inappropriate sides; after the scans cross, move the pivot into its final position.

```java
Partition(A, left, right):
    pivot = A[left]
    i = left + 1
    j = right
    while true:
        while i <= right and A[i] < pivot: i = i + 1
        while j > left and A[j] > pivot: j = j - 1
        if i >= j: break
        swap A[i], A[j]
        i = i + 1
        j = j - 1
    swap A[left], A[j]
    return j

Quicksort(A, left, right):
    if left < right:
        s = Partition(A, left, right)
        Quicksort(A, left, s - 1)
        Quicksort(A, s + 1, right)
```

This version adds bounds guards to the source's scan pseudocode and avoids its temporary swap-and-undo after crossing. The pivot occupies its final position. Values to its left are at most the pivot; values to its right are at least the pivot, with equality placement dependent on partition details.

![Quicksort scanning and pivot placement](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/05_Divide_And_Conquer/quicksort-partition.svg)

*The inward scans repair misplaced entries, then the pivot divides the two recursive ranges.*

For $5,3,1,9,8,2,7$, swapping nine and two gives $5,3,1,2,8,9,7$. Moving the pivot gives $2,3,1,5,8,9,7$. Recursively sorting the sides yields $1,2,3,5,7,8,9$.

### Quicksort Costs And Improvements

For balanced partitions:

$$
T(n)=2T(n/2)+\Theta(n)\in\Theta(n\log n).
$$

For maximally skewed partitions:

$$
T(n)=T(n-1)+\Theta(n)\in\Theta(n^2).
$$

Already sorted input is a bad case for consistently choosing the first element. The source's scan-count convention gives:

$$
C_{\mathrm{worst}}(n)=(n+1)+n+\cdots+3
=\frac{(n+1)(n+2)}2-3.
$$

Guarded partition implementations can have different exact counts, while retaining the quadratic class.

| Property | Mergesort | Ordinary quicksort |
|---|---|---|
| Best / expected time | $\Theta(n\log n)$ | $\Theta(n\log n)$ under usual random-pivot/input assumptions |
| Worst time | $\Theta(n\log n)$ | $\Theta(n^2)$ |
| Stability | Yes with tie-preserving merge | Usually no |
| Main extra space | $\Theta(n)$ array buffer | In-place partition; stack varies |

Common quicksort improvements:

- Select a **median-of-three** pivot to improve ordinary sorted-input behaviour; this does not guarantee avoidance of every worst case.
- Use insertion sort on small partitions to reduce overhead.
- Recurse on the smaller side and iterate on the larger side to control stack depth.
- Randomise pivot selection for expected good balance; an ordinary randomised quicksort still has a quadratic worst case.

Practical speed depends on data, implementation and machine; the lecture's percentage speedup is illustrative rather than a universal bound.

### Strassen Matrix Multiplication

#### Definitions

> **Block matrix**: A matrix expressed as submatrices, enabling operations on whole blocks.

> **Strassen's method**: Multiply two matrices by replacing eight recursive block multiplications with seven, at the cost of more additions and subtractions.

Partition each matrix into four equal blocks:

$$
A=\begin{bmatrix}A_{11}&A_{12}\\A_{21}&A_{22}\end{bmatrix},\qquad
B=\begin{bmatrix}B_{11}&B_{12}\\B_{21}&B_{22}\end{bmatrix}.
$$

Ordinary block multiplication uses eight half-size products, still giving cubic time. Strassen computes:

$$
\begin{aligned}
P_1&=A_{11}(B_{12}-B_{22}),&P_2&=(A_{11}+A_{12})B_{22},\\
P_3&=(A_{21}+A_{22})B_{11},&P_4&=A_{22}(B_{21}-B_{11}),\\
P_5&=(A_{11}+A_{22})(B_{11}+B_{22}),\\
P_6&=(A_{12}-A_{22})(B_{21}+B_{22}),\\
P_7&=(A_{11}-A_{21})(B_{11}+B_{12}).
\end{aligned}
$$

Each block product is recursively evaluated. Recombine:

$$
\begin{aligned}
C_{11}&=P_5+P_4-P_2+P_6,& C_{12}&=P_1+P_2,\\
C_{21}&=P_3+P_4,& C_{22}&=P_1+P_5-P_3-P_7.
\end{aligned}
$$

Use scalar multiplication when block size reaches one. Uneven matrix sizes can be padded before applying equal-block recursion.

$$
M(n)=7M(n/2),\quad M(1)=1,
$$
$$
A(n)=7A(n/2)+18(n/2)^2,\quad A(1)=0.
$$

Both costs are $\Theta(n^{\log_2 7})\approx\Theta(n^{2.807})$ by the Master Theorem. The eighteen additions/subtractions account for forming input combinations and output blocks.

The lecture names Coppersmith–Winograd as a historical example of a smaller theoretical exponent. Such asymptotic advances can have impractical constants and enormous crossover sizes; Strassen's advantage also depends on implementation size and numerical behaviour.

### Closest Pair: Split, Solve And Straddle

#### Definitions

> **Straddle strip**: The vertical region within distance $d$ of the dividing line, where a cross-boundary pair could improve the current best distance.

1. Sort the points by horizontal position and also keep a vertical-order list.
2. Divide by rank into near-equal left and right subsets.
3. Recursively compute distances $d_L$ and $d_R$; let $d=\min(d_L,d_R)$.
4. Select strip points satisfying $|x-x_{\mathrm{split}}|<d$, retaining vertical order.
5. Compare each strip point with subsequent points while the vertical separation can still be less than the current distance.
6. Return the smallest distance found.

![Closest pair strip and packing](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/05_Divide_And_Conquer/closest-strip.svg)

*The nearest pair may cross the split. The strip and within-half separation restrict useful comparisons.*

The source illustrates a five-successor packing claim. The implementation below follows the provided vertical-distance stopping rule rather than relying on a fixed five-point cutoff. The essential conclusion is a constant number of relevant successors, so the strip scan is linear. A more conservative packing argument and linear-merge explanation appear in [Carl Kingsford's CMU notes](https://www.cs.cmu.edu/~ckingsf/class/02713-s13/lectures/lec13-closestpoints.pdf).

```java
EfficientClosestPair(Px, Py):
    if length(Px) <= 3: return brute-force minimum distance
    split Px by rank into LeftX and RightX
    partition Py by the same point identities into LeftY and RightY
    dL = EfficientClosestPair(LeftX, LeftY)
    dR = EfficientClosestPair(RightX, RightY)
    d = min(dL, dR)
    splitX = largest x in LeftX
    S = points of Py with abs(x - splitX) < d
    bestSquared = d * d
    for i = 0 to length(S) - 2:
        j = i + 1
        while j < length(S) and (S[j].y - S[i].y)^2 < bestSquared:
            bestSquared = min(bestSquared, squaredDistance(S[i], S[j]))
            j = j + 1
    return sqrt(bestSquared)
```

Partition by point identity or rank when horizontal coordinates tie; splitting only by a strict coordinate comparison can create uneven subsets. Check for duplicate points, whose minimum distance is zero.

Maintaining vertical order allows linear partitioning and strip work:

$$
T(n)=2T(n/2)+\Theta(n)\in\Theta(n\log n).
$$

The initial two sorts have the same asymptotic cost. Sorting strip points afresh at every level can instead introduce $\Theta(n\log^2n)$ work. A strip may contain nearly all points; geometry, rather than strip population alone, makes the combine step efficient.

### QuickHull

#### Definitions

> **QuickHull**: A convex-hull construction that recursively selects a farthest point from a candidate edge and splits the remaining outer points around it.

1. Find leftmost and rightmost points $P_1,P_2$.
2. Split remaining points into sides of their line.
3. For a directed candidate edge, choose an outer point $P_{\max}$ with maximum perpendicular distance.
4. Discard points inside or on triangle $P_1P_{\max}P_2$, subject to the chosen collinearity policy.
5. Recurse on points outside edges $P_1P_{\max}$ and $P_{\max}P_2$.
6. Apply the same construction to the lower hull with reversed edge direction.
7. If no outer point remains, emit the candidate edge or its endpoint.

![QuickHull recursive upper and lower hull](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/05_Divide_And_Conquer/quickhull.svg)

*Each farthest point creates two candidate edges; points inside the triangle cannot become outer hull vertices.*

For fixed endpoints, maximising the absolute orientation determinant maximises triangle area and perpendicular distance:

$$
\operatorname{Area}(P_1,P_2,P)=\frac12\left|
\det\begin{bmatrix}x_1&y_1&1\\x_2&y_2&1\\x&y&1\end{bmatrix}\right|.
$$

Worst-case time is $\Theta(n^2)$ when repeated scans make poor reductions. The lecture quotes average $\Theta(n)$ behaviour, which depends on the input-point model and substantial point elimination; it is not a distribution-free bound. Balanced recursion retaining most points instead has the familiar $\Theta(n\log n)$ scan cost.
