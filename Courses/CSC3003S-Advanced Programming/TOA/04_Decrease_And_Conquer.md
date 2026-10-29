---
tags:
  - advanced-programming
---

# Decrease And Conquer

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)  
**Source**: [4 - TOA Decrease and Conquer.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/4%20-%20TOA%20Decrease%20and%20Conquer.pdf), Patrick Marais, University of Cape Town, PDF pages 1–27  
**Generated**: 2026-10-02

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes. Examples and corrections appear beside the relevant concept.

---

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

---

## Core Content

### Strategy And Variants

#### Definitions

> **Decrease and conquer**: Solve one smaller instance, then use its solution to obtain the original solution; also called an inductive or incremental strategy.

| Variant | Smaller instance | Examples |
|---|---|---|
| Constant decrease | $n-c$, commonly $n-1$ | Insertion sort; topological sort; generating subsets/permutations |
| Constant-factor decrease | $n/c$, commonly half | Binary search; exponentiation; fake coins; Russian multiplication |
| Variable-size decrease | Reduction depends on input | Euclid; quickselect; interpolation search |

![Decrease variants and comparison with divide and conquer](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/04_Decrease_And_Conquer/decrease-variants.svg)

*Decrease and conquer solves one smaller instance. Divide and conquer solves multiple instances and combines their results.*

The method can be implemented top down with recursion or bottom up with iteration. It can be highly efficient, but the existence of a useful reduction depends on the problem.

### Insertion Sort

#### Definitions

> **Insertion sort**: Build a sorted prefix by inserting each next element into its correct position.

> **Stable sort**: A sort preserving the original relative order of records with equal keys.

Assume the first $n-1$ entries are sorted. Save the remaining entry, shift larger entries right, and insert the saved value into the gap.

```java
InsertionSortRecursive(A, n):
    if n <= 1: return
    InsertionSortRecursive(A, n - 1)
    inserted = A[n - 1]
    j = n - 2
    while j >= 0 and A[j] > inserted:
        A[j + 1] = A[j]
        j = j - 1
    A[j + 1] = inserted
```

The bottom-up version repeats the insertion body for prefix lengths from two through the full size, avoiding recursion storage.

| Sorted prefix after insertion | Remaining suffix |
|---|---|
| $6$ | $5,0,2,8,7,4$ |
| $5,6$ | $0,2,8,7,4$ |
| $0,5,6$ | $2,8,7,4$ |
| $0,2,5,6$ | $8,7,4$ |
| $0,2,5,6,8$ | $7,4$ |
| $0,2,5,6,7,8$ | $4$ |
| $0,2,4,5,6,7,8$ | None |

Replacing the final four with nine leaves the last insertion in place, producing $0,2,5,6,7,8,9$. This illustrates how nearly sorted input reduces shifting.

| Case or property | Result |
|---|---|
| Reverse-sorted input | $\sum_{i=1}^{n-1}i=n(n-1)/2$ shifts; $\Theta(n^2)$ time |
| Already sorted input | One key comparison per insertion; $\Theta(n)$ time |
| Ordinary average case | $\Theta(n^2)$ under random-permutation assumptions |
| Iterative auxiliary space | $\Theta(1)$ |
| Stability | Preserved by shifting only strictly larger keys |

### Topological Sorting

#### Definitions

> **Directed acyclic graph (DAG)**: A directed graph containing no directed cycle.

> **Topological ordering**: A vertex ordering in which the source of every directed edge precedes its destination.

> **Source vertex**: A vertex with no incoming edges in the remaining graph.

> **Indegree**: Number of incoming edges to a vertex.

Dependencies occur in course prerequisites, spreadsheet calculations and project tasks. Several valid orders can exist; a directed cycle prevents any topological order.

1. Compute every vertex's indegree.
2. Put all zero-indegree vertices in a queue or other source collection.
3. Remove a source, append it to the output, and remove its outgoing edges by decrementing neighbour indegrees.
4. Add any newly zero-indegree neighbours to the source collection.
5. If fewer than all vertices are output, the remaining graph has a cycle.

```java
TopologicalSort(G):
    indegree = count incoming edges for every vertex
    sources = all vertices with indegree zero
    result = empty list
    while sources is not empty:
        u = remove one source
        append u to result
        for each edge u -> v:
            indegree[v] = indegree[v] - 1
            if indegree[v] == 0: add v to sources
    if length(result) != number of vertices: report cycle
    return result
```

![Source-removal topological sort](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/04_Decrease_And_Conquer/topological-sort.svg)

*Removing a, then b, then c, then d respects all five dependencies in the source graph.*

The edges are $a\to b$, $a\to c$, $b\to c$, $b\to d$, $c\to d$. Initial indegrees are $0,1,2,2$; after removing $a$, the remaining indegrees are $0,1,2$ for $b,c,d$.

With adjacency lists, time is $\Theta(\lvert V\rvert+\lvert E\rvert)$. A DFS alternative appends vertices on completion and reverses that finish order; it must detect cycles, usually via active-recursion marks.

### Generating The Power Set

#### Definitions

> **Power set**: The set of every subset of a given set, including the empty set and the full set.

> **Minimal-change order**: An enumeration in which consecutive outputs differ by a small prescribed change.

For $n$ distinct elements there are $2^n$ subsets. Solve for the first $n-1$ elements, then retain each earlier subset and make a copy containing the new element:

$$
\mathcal P(S\cup\{a\})=\mathcal P(S)\cup\{X\cup\{a\}:X\in\mathcal P(S)\},\qquad
\mathcal P(\varnothing)=\{\varnothing\}.
$$

For $\{a,b,c\}$ the generated sequence is:

$$
\varnothing,\{a\},\{b\},\{a,b\},\{c\},\{a,c\},\{b,c\},\{a,b,c\}.
$$

An alternative enumerates integer masks from zero through $2^n-1$. A set element is present exactly when its assigned bit is one.

**Binary reflected Gray code** gives consecutive masks differing in one bit:

$$
g(i)=i\mathbin{\oplus}\lfloor i/2\rfloor.
$$

For three bits: $000,001,011,010,110,111,101,100$. Ordinary binary enumeration does not have this property; for example $011\to100$ changes three bits.

Generating compact masks requires at least one output per subset. Writing full explicit subsets takes $\Theta(n2^n)$ total element-output work.

### Permutations By Insertion And Johnson–Trotter

#### Definitions

> **Permutation**: An ordering of all elements of a set; there are $n!$ permutations of $n$ distinct elements.

> **Mobile element**: In Johnson–Trotter enumeration, an element whose direction points to an adjacent smaller element.

Generate all permutations of the first $n-1$ elements, then insert the new largest element into each of the $n$ positions. Alternate insertion from right to left and left to right across consecutive smaller permutations to preserve adjacent-swap minimal change.

![Permutation insertion tree](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/04_Decrease_And_Conquer/permutation-tree.svg)

*Alternating insertion directions produces 123, 132, 312, 321, 231, 213.*

The **Johnson–Trotter algorithm** avoids explicitly constructing smaller permutation lists:

1. Start with ascending values, all directed left, and output this permutation.
2. Find the largest mobile value.
3. Swap it with the neighbour it points to.
4. Reverse the directions of all values greater than the swapped value.
5. Output the new permutation and repeat until no element is mobile.

For the directed sequence $\overrightarrow3,\overleftarrow2,\overrightarrow4,\overleftarrow1$, values three and four are mobile; two and one are not. Four is the chosen value.

![Johnson–Trotter direction trace](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/04_Decrease_And_Conquer/johnson-trotter.svg)

*For three values, the largest mobile element determines each adjacent swap and later direction reversal.*

The output order is $123,132,312,321,231,213$. A simple implementation scans the values to find mobility and reverse directions, taking $O(n)$ per permutation and $O(n\,n!)$ overall, with $O(n)$ working storage if outputs are streamed.

### Binary Search And Exponentiation

#### Definitions

> **Binary search**: Search sorted input by comparing with a midpoint and continuing only in the half that can contain the key.

> **Exponentiation by squaring**: Compute a power by recursively solving the half-exponent power once, then squaring it.

Binary search has worst-case $\Theta(\log n)$ comparisons because $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)$. Its best case is a midpoint match, $\Theta(1)$.

For a nonnegative integer exponent:

$$
a^0=1,\qquad
a^n=\begin{cases}(a^{\lfloor n/2\rfloor})^2,&n>0\text{ even},\\
a(a^{\lfloor n/2\rfloor})^2,&n\text{ odd}.
\end{cases}
$$

```java
Power(a, n):
    if n == 0: return 1
    halfPower = Power(a, floor(n / 2))
    result = halfPower * halfPower
    if n is odd: result = result * a
    return result
```

Repeated multiplication uses $\Theta(n)$ multiplications. Squaring uses $M(n)=M(\lfloor n/2\rfloor)+\Theta(1)$, hence $\Theta(\log n)$ for growing positive exponents. Cache the half-power: calling the recursive function twice repeats work and defeats the single-subproblem strategy. The multiplication-count base case is $M(0)=0$, not one.

### Fake-Coin Detection

#### Definitions

> **Fake-coin problem**: Among otherwise equal coins, find the single lighter coin using a balance comparing two equal-sized groups.

For two groups, weigh $\lfloor n/2\rfloor$ against $\lfloor n/2\rfloor$, leaving one coin aside if necessary. If balanced, the aside coin is fake; otherwise recurse into the lighter group.

$$
W(1)=0,\qquad W(n)=1+W(\lfloor n/2\rfloor),\qquad
W(n)=\lfloor\log_2n\rfloor\text{ in the worst case}.
$$

A balance has three outcomes, so three groups use its information more effectively. Partition into near-equal groups, weigh equal-sized first and second groups, and continue in the lighter group or the third group if balanced.

| Coin count | First two groups | Third group |
|---|---|---|
| $3q$ | $q,q$ | $q$ |
| $3q+1$ | $q,q$ | $q+1$ |
| $3q+2$ | $q+1,q+1$ | $q$ |

This ensures the chosen group has at most $\lceil n/3\rceil$ coins, giving $\Theta(\log_3n)$ worst-case weighings and an information bound of $\lceil\log_3n\rceil$.

> [!warning] <span style="color:#ffc778">Small-instance correction</span>
> The PDF's formula using two groups of size $\lceil n/3\rceil$ gives a negative third-group size when there are four coins. Use the partition above. Equal weighed-group sizes are required for a meaningful balance comparison.

The two- and three-group versions have the same logarithmic asymptotic class, but the latter improves the constant factor by roughly $\log_2 3\approx1.585$.

### Russian Multiplication

#### Definitions

> **Russian peasant multiplication**: Multiply integers using halving, doubling and addition, selecting doubled values corresponding to odd halved values.

For a nonnegative integer $n$:

$$
nm=\begin{cases}
(n/2)(2m),&n\text{ even},\\
\lfloor n/2\rfloor(2m)+m,&n\text{ odd}.
\end{cases}
$$

```java
RussianMultiply(n, m):
    result = 0
    while n > 0:
        if n is odd: result = result + m
        n = floor(n / 2)
        m = 2 * m
    return result
```

| Halved value | Doubled value | Added? |
|---:|---:|---|
| $50$ | $20$ | No |
| $25$ | $40$ | Yes |
| $12$ | $80$ | No |
| $6$ | $160$ | No |
| $3$ | $320$ | Yes |
| $1$ | $640$ | Yes |

Thus $50\cdot20=40+320+640=1000$. There are $\Theta(\log n)$ iterations; shifts implement halving and doubling efficiently for fixed-size integers. Arbitrary-precision bit costs are a separate analysis.

### Euclid And Quickselect

#### Definitions

> **Order statistic**: An element at a specified rank in sorted order; the $k$th order statistic is the $k$th smallest element.

> **Quickselect**: Select an order statistic by partitioning around a pivot and recursively processing only the side containing the required rank.

Euclid's reduction $\gcd(m,n)=\gcd(n,m\bmod n)$ has an input-dependent smaller instance. For example, $(60,24)\to(24,12)\to(12,0)$ returns twelve.

For a zero-based array, the desired $k$th smallest value has target index $k-1$:

```java
Quickselect(A, left, right, target):
    if left == right: return A[left]
    s = PartitionWithPivotInFinalPosition(A, left, right)
    if s == target: return A[s]
    if target < s: return Quickselect(A, left, s - 1, target)
    return Quickselect(A, s + 1, right, target)
```

![Quickselect keeps one partition](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/04_Decrease_And_Conquer/quickselect.svg)

*Only the partition containing the target rank remains relevant after the pivot is placed.*

Each partition costs linear time in its current size. Balanced or random pivots give expected $\Theta(n)$ time; repeatedly removing only one irrelevant element gives worst-case $\Theta(n^2)$. A median is rank $\lceil n/2\rceil$ under the lower-median convention; some even-size definitions average the two central values.

### Interpolation Search

#### Definitions

> **Interpolation search**: Search sorted numeric input using the relative key value to estimate its array position.

Assuming values approximately increase linearly between the endpoints, the estimated zero-based probe is:

$$
x=l+\left\lfloor\frac{(v-A[l])(r-l)}{A[r]-A[l]}\right\rfloor.
$$

![Interpolation search projection](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/04_Decrease_And_Conquer/interpolation.svg)

*Projecting the target value onto the endpoint line estimates a position, instead of always probing the midpoint.*

1. Ensure the key is between the endpoint values; otherwise fail.
2. If the endpoint values are equal, check that value and avoid dividing by zero.
3. Compute a valid probe in the current range.
4. Return if the value matches; otherwise continue to the appropriate side, excluding the probe.

Expected cost is $O(\log\log n)$ under suitable approximately uniform value distributions, with worst-case $O(n)$. Nonuniform data can produce poor probes. It may be useful when the distribution fits the model and accesses or comparisons are expensive.
