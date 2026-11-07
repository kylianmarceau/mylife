---
tags:
  - advanced-programming
---

# Divide And Conquer

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)
**Source**: [5 - TOA Divide and Conquer - Copy.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/5%20-%20TOA%20Divide%20and%20Conquer%20-%20Copy.pdf), Patrick Marais, University of Cape Town, pages 1–21
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Mergesort, quicksort with Hoare partitioning, Strassen's matrix multiplication, divide-and-conquer closest pair, and QuickHull.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#The Divide-And-Conquer Strategy|The Divide-And-Conquer Strategy]]
  - [[#Mergesort|Mergesort]]
  - [[#Quicksort And Hoare Partitioning|Quicksort And Hoare Partitioning]]
  - [[#Quicksort Efficiency And Improvements|Quicksort Efficiency And Improvements]]
  - [[#Strassen's Matrix Multiplication|Strassen's Matrix Multiplication]]
  - [[#Closest Pair By Divide And Conquer|Closest Pair By Divide And Conquer]]
  - [[#The Straddle Zone And The Packing Argument|The Straddle Zone And The Packing Argument]]
  - [[#QuickHull|QuickHull]]

---

## Core Content

### The Divide-And-Conquer Strategy

#### Definitions

> **Divide and conquer**: The best-known design strategy: (1) divide an instance into two or more smaller instances, (2) solve the smaller instances recursively, (3) combine their solutions into a solution of the original instance.

Divide-and-conquer algorithms are analysed with recurrences of the form:

$$
T(n) = aT(n/b) + f(n), \qquad a \ge 1,\ b \ge 2
$$

Simple example — adding $n$ numbers by splitting the list in half:

$$
a_0 + \dots + a_{n-1} = (a_0 + \dots + a_{\lfloor n/2\rfloor - 1}) + (a_{\lfloor n/2\rfloor} + \dots + a_{n-1})
$$

![Divide and combine](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/05_Divide_And_Conquer/divide-combine.svg)

*Unlike decrease and conquer, both subproblems are solved and their solutions combined.*

### Mergesort

Algorithm:

1. Split $A[1..n]$ in half and copy each half into arrays $B$ and $C$. If $n$ is odd, one array gets one more element.
2. Recursively mergesort $B$ and $C$.
3. Merge the sorted arrays $B$ and $C$ back into $A$.

Merging:

1. Compare the first unprocessed elements of $B$ and $C$.
2. Copy the smaller into $A$ and advance the index of the array it came from.
3. Repeat until one of $B$ or $C$ is exhausted.
4. Copy the remaining unprocessed elements of the other array into $A$.

Example: `7 2 1 6 4` splits into `7 2 1` and `6 4`, then `7 2` / `1`, then `7` / `2`. Merging back up gives `2 7`, `1 2 7`, `4 6`, and finally `1 2 4 6 7`.

![Mergesort example](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/05_Divide_And_Conquer/mergesort.svg)

*Splitting continues to single elements; all the work happens in the merges on the way back up.*

#### Analysis

Assume $n = 2^k$. Count key comparisons:

$$
C(n) = 2C(n/2) + C_{merge}(n) \ (n > 1), \qquad C(1) = 0
$$

In the worst case a merge makes $C_{merge}(n) = n - 1$ comparisons. With the Master Theorem, $a = 2$, $b = 2$, $d = 1$, so $a = b^d$ ($2 = 2^1$), giving:

$$
C(n) \in \Theta(n\log n) \quad \text{in all cases}
$$

| Pro | Con |
|---|---|
| **Stable** (equal keys keep their relative order), unlike quicksort and heapsort | Uses $\Theta(n)$ extra space |

### Quicksort And Hoare Partitioning

#### Definitions

> **Pivot (partitioning element)**: The element around which the list is rearranged, usually $A[0]$ (the first element of the subarray).

> **Partition**: Rearranging a list so that elements before the pivot are $\le p$ and elements after it are $\ge p$, leaving the pivot in its final sorted position.

Quicksort:

1. Select a pivot $p$.
2. Rearrange the list into two sublists: elements before the pivot are $\le p$, elements after are $\ge p$.
3. Exchange the pivot with the last element of the first sublist. The pivot is now in its final position.
4. Quicksort the two sublists.

```text
ALGORITHM Quicksort(A[l..r])
// Sorts a subarray by quicksort
// Input: subarray A[l..r] of A[0..n-1]
// Output: A[l..r] sorted in nondecreasing order
if l < r
    s ← HoarePartition(A[l..r])   // s is a split position
    Quicksort(A[l..s-1])
    Quicksort(A[s+1..r])
```

```text
ALGORITHM HoarePartition(A[l..r])
// Partitions a subarray using the first element as pivot
// Output: partition of A[l..r]; returns the split position
p ← A[l]
i ← l; j ← r + 1
repeat
    repeat i ← i + 1 until A[i] ≥ p
    repeat j ← j - 1 until A[j] ≤ p
    swap(A[i], A[j])
until i ≥ j
swap(A[i], A[j])      // undo last swap when i ≥ j
swap(A[l], A[j])
return j
```

How the two scans interact:

| Situation | Action |
|---|---|
| $i < j$ (scans have not crossed) | Swap $A[i]$ and $A[j]$, then continue both scans |
| $i > j$ (scans crossed) | Swap the pivot $A[l]$ with $A[j]$; partition done, split at $j$ |
| $i = j$ (scans meet) | $A[i] = p$; the split position is $i = j$ |

![Quicksort partition](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/05_Divide_And_Conquer/quicksort-partition.svg)

*The left scan stops at an element $\ge p$, the right scan at one $\le p$; out-of-place pairs are swapped until the scans cross.*

**Trace** on `5 3 1 9 8 2 7` (pivot 5):

| Step | Array | Note |
|---|---|---|
| 1 | `5 3 1 9 8 2 7` | $i$ stops at 9, $j$ stops at 2 → swap |
| 2 | `5 3 1 2 8 9 7` | $i$ stops at 8, $j$ stops at 2 → crossed |
| 3 | `2 3 1 5 8 9 7` | Swap pivot with $A[j]$; 5 is final |
| 4 | `2 3 1` | Pivot 2: swap 3 and 1 → `2 1 3`, scans cross, swap pivot → `1 2 3` |
| 5 | `8 9 7` | Pivot 8: swap 9 and 7 → `8 7 9`, scans cross, swap pivot → `7 8 9` |
| 6 | `1 2 3 5 7 8 9` | Remaining calls on single elements (`1`, `3`, `7`, `9`) do nothing |

### Quicksort Efficiency And Improvements

**Worst case**: all splits are completely skewed. An already sorted (ascending) list triggers this:

- The partition makes $n + 1$ comparisons.
- The pivot is exchanged with itself.
- Quicksort recurses on an empty left part and $A[1..n-1]$.

$$
C_{worst}(n) = (n+1) + n + \dots + 3 = \frac{(n+1)(n+2)}{2} - 3 \in \Theta(n^2)
$$

| Case | Efficiency |
|---|---|
| Best (split in the middle every time) | $\Theta(n\log n)$ |
| Average (random split) | $\Theta(n\log n)$ |
| Worst (sorted input, first-element pivot) | $\Theta(n^2)$ |

Improvements, which together make quicksort 20–25% faster:

- **Better pivot selection**: median-of-three partitioning avoids the worst case on sorted lists.
- **Switch to insertion sort** on small subarrays.
- **Eliminate recursion**.

Quicksort is considered the method of choice for internal sorting of large lists ($n \ge 10000$).

### Strassen's Matrix Multiplication

Brute-force multiplication of two $n \times n$ matrices takes $\Theta(n^3)$ operations. Splitting the matrices into blocks and multiplying recursively is still $\Theta(n^3)$ with 8 block multiplications. Strassen's method trades one multiplication for extra additions, using 7 recursive multiplications.

```text
STRASSEN(A, B):
1.  if n == 1: output A11 × B11
2.  else:
3.    split A and B into n/2 × n/2 blocks A11, A12, A21, A22, B11, ..., B22
4.    P1 = Strassen(A11, B12 − B22)
5.    P2 = Strassen(A11 + A12, B22)
6.    P3 = Strassen(A21 + A22, B11)
7.    P4 = Strassen(A22, B21 − B11)
8.    P5 = Strassen(A11 + A22, B11 + B22)
9.    P6 = Strassen(A12 − A22, B21 + B22)
10.   P7 = Strassen(A11 − A21, B11 + B12)
11.   C11 = P5 + P4 − P2 + P6
12.   C12 = P1 + P2
13.   C21 = P3 + P4
14.   C22 = P1 + P5 − P3 − P7
15.   output C
```

Recurrences:

$$
M(n) = 7M(n/2) \ (n > 1), \qquad M(1) = 1
$$

$$
A(n) = 7A(n/2) + 18(n/2)^2 \ (n > 1), \qquad A(1) = 0
$$

By the Master Theorem ($a = 7 > b^d$ for $b = 2$, $d \le 2$):

$$
M(n),\ A(n) \in \Theta(n^{\log_2 7}) \approx \Theta(n^{2.81})
$$

Better algorithms now exist, e.g. Coppersmith–Winograd at $O(n^{2.376})$ or faster. Many are only relevant to "galactic" problems — matrices so huge they never occur in practice.

### Closest Pair By Divide And Conquer

Algorithm:

1. Sort the points by $x$-coordinate (and keep a copy sorted by $y$).
2. Split the points into two equal-sized subsets with a vertical line $x = x_{median}$.
3. Recursively solve the left and right subsets, giving minimum distances $d_l$ and $d_r$. Let $d_{min} = \min(d_l, d_r)$.
4. **Straddle**: find the minimum distance among the points in the strip $S$ of width $2d$ around the vertical line. Update $d_{min}$ if a closer pair crosses the line.

```text
ALGORITHM EfficientClosestPair(P, Q)
// P: n ≥ 2 points sorted by x; Q: the same points sorted by y
// Output: Euclidean distance between the closest pair
if n ≤ 3
    return the minimal distance found by brute force
else
    copy the first ⌈n/2⌉ points of P to Pl
    copy the same ⌈n/2⌉ points from Q to Ql
    copy the remaining ⌊n/2⌋ points of P to Pr
    copy the same ⌊n/2⌋ points from Q to Qr
    dl ← EfficientClosestPair(Pl, Ql)
    dr ← EfficientClosestPair(Pr, Qr)
    d ← min{dl, dr}
    m ← P[⌈n/2⌉ − 1].x
    copy all points of Q with |x − m| < d into S[0..num−1]
    dminsq ← d²
    for i ← 0 to num − 2 do
        k ← i + 1
        while k ≤ num − 1 and (S[k].y − S[i].y)² < dminsq
            dminsq ← min((S[k].x − S[i].x)² + (S[k].y − S[i].y)², dminsq)
            k ← k + 1
return sqrt(dminsq)
```

Squared distances avoid computing square roots until the very end.

![Closest pair strip](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/05_Divide_And_Conquer/closest-strip.svg)

*Solve each half, then check only the strip of width $2d$ around the dividing line, where a closer crossing pair could exist.*

#### Efficiency

$$
T(n) = 2T(n/2) + f(n), \qquad f(n) \in \Theta(n) \text{ (split + strip merge)}
$$

$a = 2$, $b = 2$, $d = 1$, so $a = b^d$ and $T(n) \in \Theta(n\log n)$. This is the same cost as the presorting step.

### The Straddle Zone And The Packing Argument

At first it is hard to see why the strip check is better than brute force. What if $S$ holds almost as many points as the rest? Comparing each point in $S$ with all points after it would be:

```text
for i = 0 to n − 2:
    for j = i + 1 to n − 1: ...
```

which is $\Theta(n^2)$.

A property of $S$ dramatically limits the work:

- Points in $S$ are sorted by increasing $y$.
- Points on the same side of the dividing line are at least $d = d_{min}$ apart (otherwise that half's recursive answer would be smaller).
- A **packing argument** shows that within the $d \times 2d$ rectangle above a point $P$, at most a fixed small number of points fit while respecting that spacing.
- So each point only needs to be compared with the **next 5 points** in $y$-order. A 6th point cannot be closer to $P$ than $d$ in the sweep direction.

This makes the strip check $\Theta(n)$, which is what gives the $\Theta(n\log n)$ total.

### QuickHull

QuickHull solves the convex hull problem in a way reminiscent of quicksort.

1. Identify the leftmost and rightmost points $P_1$ and $P_2$. The line $P_1P_2$ splits the points into an upper and a lower set.
2. Compute the **upper hull**:
   1. Find the point $P_{max}$ farthest from line $P_1P_2$ (the triangle $P_1P_2P_{max}$ with the largest area).
   2. Points inside triangle $P_1 P_{max} P_2$ cannot be on the hull; discard them.
   3. Recursively QuickHull the points to the left of line $P_1P_{max}$.
   4. Recursively QuickHull the points to the left of line $P_{max}P_2$.
3. Compute the **lower hull** the same way.

The distance comparison uses triangle area, computed with a determinant:

$$
\text{Area}(P_1, P_2, P_{max}) = \tfrac12 \left|\det\begin{pmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_{max} & y_{max} & 1 \end{pmatrix}\right|
$$

The sign of the determinant (before taking the absolute value) tells you whether a point lies to the left of a directed line.

![QuickHull](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/05_Divide_And_Conquer/quickhull.svg)

*The farthest point joins the hull; points inside the triangle are discarded and the two outer sets are processed recursively.*

| Case | Efficiency |
|---|---|
| Average | $\Theta(n)$ (most points are discarded early) |
| Worst | $\Theta(n^2)$ |
