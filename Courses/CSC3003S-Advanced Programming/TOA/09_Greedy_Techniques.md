---
tags:
  - advanced-programming
---

# Greedy Techniques

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)  
**Source**: [9 - TOA Greedy Techniques.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/9%20-%20TOA%20Greedy%20Techniques.pdf), Patrick Marais, University of Cape Town, PDF pages 1–15  
**Generated**: 2026-10-02

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes. Examples and corrections appear beside the relevant concept.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Greedy Choices And Optimality|Greedy Choices And Optimality]]
  - [[#Greedy Change Making|Greedy Change Making]]
  - [[#Fixed-Length And Prefix-Free Codes|Fixed-Length And Prefix-Free Codes]]
  - [[#Huffman Construction|Huffman Construction]]
  - [[#Huffman Optimality, Compression And Limits|Huffman Optimality, Compression And Limits]]
  - [[#Minimum Spanning Trees|Minimum Spanning Trees]]
  - [[#Prim's Algorithm|Prim's Algorithm]]
  - [[#Prim Source Example And Complexity|Prim Source Example And Complexity]]
  - [[#Kruskal, Limits And Course Skills|Kruskal, Limits And Course Skills]]

---

## Core Content

### Greedy Choices And Optimality

#### Definitions

> **Greedy technique**: Build a solution by repeatedly making a feasible locally best choice and committing to it.

> **Feasible choice**: A choice satisfying the problem's constraints.

> **Locally optimal choice**: The best available option according to the current step's criterion.

> **Irrevocable choice**: A choice not later withdrawn by the algorithm.

Local optimality does not establish global optimality. Some greedy algorithms have proofs, such as Prim, Kruskal and Huffman; other plausible rules have counterexamples.

| Proof idea | Use |
|---|---|
| **Exchange argument** | Transform an optimum to include the greedy choice without worsening it |
| **Induction** | Establish a correct choice, then reduce to a smaller problem |
| **Matroid structure** | A formal independence/exchange structure supporting certain greedy optimisation rules |

Greedy rules are often simple and efficient, while DP considers alternatives and stores state results. A heuristic or approximation may be acceptable when an exact optimum is not required, but its guarantees must be stated.

The examples named in the lecture are Dijkstra's single-source shortest paths, minimum spanning trees, change making and Huffman coding. Dijkstra's settled-distance greedy argument requires nonnegative edge weights; it is not developed as a full worked algorithm in this PDF.

### Greedy Change Making

#### Definitions

> **Greedy change rule**: Repeatedly take the largest denomination not exceeding the remaining amount.

```pseudo
GreedyChange(D, amount):
    // denominations D are descending positive integer values
    result = empty list
    for each denomination d in D:
        count = floor(amount / d)
        append count copies of d to result
        amount = amount - count * d
    if amount != 0: report exact change unavailable by this method
    return result
```

The source uses denominations $500,200,100,50,20,10,5,2,1$ in cents. For $254$ cents, the greedy result is:

$$
254=200+50+2+2.
$$

This uses four coins. Work in integer smallest units to avoid currency floating-point errors.

For denominations $\{4,3,1\}$ and amount six, greedy returns $4+1+1$ while the optimum is $3+3$. The denominations determine whether greedy is always optimal; a unit coin ensures feasibility, not optimality. General change making can use DP.

### Fixed-Length And Prefix-Free Codes

#### Definitions

> **Encoding**: Assign a bit string to each symbol of an alphabet.

> **Fixed-length code**: Every symbol receives the same number of bits.

> **Variable-length code**: Different symbols may receive different numbers of bits, typically giving shorter words to frequent symbols.

> **Prefix-free code**: No symbol's complete codeword is a prefix of another symbol's codeword.

> **Entropy coding**: Use symbol occurrence frequencies or probabilities to reduce expected encoded length.

| Code style | Main property | Decoding requirement |
|---|---|---|
| Fixed length | Same width for every symbol | Split at fixed-width boundaries |
| Variable length, prefix-free | Symbols end at tree leaves | Follow bits to a leaf and restart at the root |

Morse code illustrates variable symbol lengths, but needs timing/separators; it is not a binary prefix-free code without that extra signalling.

A binary prefix-code tree labels left edges zero and right edges one, with symbols only at leaves. A leaf cannot be an ancestor of another leaf, guaranteeing the prefix-free property.

![Source four-symbol prefix tree](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/09_Greedy_Techniques/prefix-tree.svg)

*The source tree gives A code 0, B code 100, C code 101 and D code 11.*

| Symbol | Code |
|---|---|
| $A$ | `0` |
| $B$ | `100` |
| $C$ | `101` |
| $D$ | `11` |

Encoding `ABADC` concatenates `0`, `100`, `0`, `11`, `101` into `0100011101`. Decoding `11000101` splits into `11|0|0|0|101`, giving `DAAAC`.

### Huffman Construction

#### Definitions

> **Huffman tree**: A prefix-code tree formed by repeatedly merging the two lowest-weight trees.

> **Weight**: Symbol frequency or probability; an internal node stores the sum of descendant weights.

1. Create one leaf for each symbol with its frequency or probability.
2. Place those trees in a min-priority queue by weight.
3. Remove the two lowest-weight trees.
4. Make them children of a new node weighted by their sum.
5. Put the merged tree back into the queue.
6. Continue until only one tree remains; label branches and read root-to-leaf codes.

```pseudo
Huffman(symbolWeights):
    Q = min-priority queue containing one leaf per symbol
    while size(Q) > 1:
        left = ExtractMinimum(Q)
        right = ExtractMinimum(Q)
        parent = Node(left.weight + right.weight, left, right)
        Insert(Q, parent)
    return ExtractMinimum(Q)
```

Equal weights permit multiple trees; swapping left and right children also changes codewords without changing expected length. Encoding and decoding must share the same chosen tree.

For $p(A)=0.40,p(B)=0.45,p(C)=0.15$:

| Merge step | Trees combined | New weight |
|---|---|---:|
| $1$ | $C$ and $A$ | $0.55$ |
| $2$ | $B$ and the $CA$ subtree | $1.00$ |

![Huffman source merge sequence](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/09_Greedy_Techniques/huffman-build.svg)

*The two least probable symbols merge first, leaving the most probable symbol with a one-bit code.*

The resulting source codes are $B:$ `0`, $C:$ `10`, $A:$ `11`. Expected bits per symbol are:

$$
L=\sum_s p(s)\ell(s)=0.45(1)+0.15(2)+0.40(2)=1.55.
$$

A fixed two-bit code for three symbols uses two bits per symbol. Ignoring tree/header overhead, the expected saving is $100(2-1.55)/2=22.5\%$.

With $s$ symbols and a binary heap, construction takes $O(s\log s)$ time and $O(s)$ tree storage. Each merge reduces the tree count by one, so there are $s-1$ merges.

### Huffman Optimality, Compression And Limits

#### Definitions

> **Expected code length**: Probability-weighted average number of encoded bits per symbol.

The two least probable symbols can be placed as deepest sibling leaves in some optimal prefix tree. Merging them reduces to a smaller instance; expanding that merged symbol adds exactly their total probability to expected length. This supports the greedy choice and induction.

Huffman minimises expected length among binary prefix codes for the specified symbol probabilities; those probabilities need not be negative powers of two. The prefix-code optimality argument is developed in [MIT's Huffman lecture](https://ocw.mit.edu/courses/18-200-principles-of-discrete-applied-mathematics-spring-2024/mit18_200_s24_lec19.pdf).

> [!warning] <span style="color:#ffc778">Source optimality qualification</span>
> Negative-power-of-two probabilities concern achieving ideal entropy lengths exactly. They are not required for Huffman's optimality among symbol-by-symbol binary prefix codes. Huffman does not guarantee optimal compression among every possible encoding scheme.

The source's saving percentage is:

$$
\mathrm{CR}=100\frac{y-x}{y},
$$

where $y$ is uncompressed size and $x$ compressed size. Some contexts use the term compression ratio differently, so state this convention. The lecture's twenty-to-eighty percent examples are empirical illustrations, not a universal guarantee.

For an alphabet with only two symbols, both Huffman codewords normally have length one. Encoding individual zero/one symbols cannot reduce a bit string below one bit per symbol, even if one symbol is much more common. Blocks or different coding methods can exploit that imbalance.

**Adaptive Huffman coding** updates frequency information during processing. Arithmetic coding can approach noninteger average bit lengths more closely, especially for skewed probabilities; actual gains depend on the model and overhead. Decoder knowledge of the model or code tree also costs space.

### Minimum Spanning Trees

#### Definitions

> **Spanning tree**: A connected acyclic subgraph containing all vertices of a connected undirected graph.

> **Minimum spanning tree (MST)**: A spanning tree minimising the sum of its edge weights.

> **Cut**: A partition of graph vertices into two nonempty sets; a crossing edge has endpoints in different sets.

A spanning tree has $\lvert V\rvert-1$ edges. An MST may not be unique when weights tie. It minimises total network edge weight, rather than distances from a source.

Applications include communication networks, relationship graphs and components of approximation methods for suitable TSP variants. The source's example of a spanning tree with total weight thirty-eight illustrates the concept; the worked Prim graph below is a different instance.

![Source spanning-tree illustration](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/09_Greedy_Techniques/spanning-tree.svg)

*Highlighted edges span the source ten-vertex graph without a cycle; their total weight is thirty-eight.*

The **cut property** gives a safe greedy step: a minimum-weight crossing edge can be included in an MST consistent with the chosen tree edges. If an optimum uses another crossing edge, replacing it with the no-heavier greedy edge preserves connectivity and cannot increase the cost.

| Algorithm | Greedy choice | Main structure | Typical cost |
|---|---|---|---|
| **Prim** | Lightest edge joining the current tree to a new vertex | Vertex keys and min-heap | $O(\lvert E\rvert\log\lvert V\rvert)$ on connected graphs |
| **Kruskal** | Lightest edge joining different forest components | Sorted edges and disjoint sets | $O(\lvert E\rvert\log\lvert E\rvert)$ |

### Prim's Algorithm

#### Definitions

> **Vertex key**: The lowest known edge weight connecting a non-tree vertex to any current tree vertex.

> **Parent**: The tree vertex providing the edge currently represented by a vertex key.

1. Choose any starting vertex and give it key zero; all others start at infinity.
2. Remove the non-tree vertex with minimum key.
3. Add its parent edge to the tree unless it is the start.
4. For each neighbour outside the tree, replace its key and parent if the new edge is lighter.
5. Repeat until all vertices are selected.

```pseudo
Prim(G, start):
    for each vertex v:
        key[v] = infinity
        parent[v] = none
    key[start] = 0
    Q = min-heap of all vertices by key
    treeEdges = empty set
    while Q is not empty:
        u = ExtractMinimum(Q)
        if key[u] == infinity: report graph disconnected
        if parent[u] != none: add edge (parent[u], u) to treeEdges
        for each neighbour v still in Q:
            if weight(u, v) < key[v]:
                parent[v] = u
                key[v] = weight(u, v)
                DecreaseKey(Q, v, key[v])
    return treeEdges
```

Prim's key is a single connecting-edge weight. Dijkstra uses a complete source-to-vertex path length; confusing these update meanings gives the wrong algorithm.

### Prim Source Example And Complexity

![Source weighted Prim graph and selected MST](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/09_Greedy_Techniques/prim-example.svg)

*Starting at a, the selected edges have weights 3, 1, 4, 2 and 5, totalling fifteen.*

The source edge list is $ab:3,bc:1,bf:4,cf:4,cd:6,af:5,fd:5,ae:6,fe:2,ed:8$.

| Vertex just added | Remaining best attachments after update |
|---|---|
| $a$ | $b:(a,3),\ f:(a,5),\ e:(a,6),\ c:\infty,\ d:\infty$ |
| $b$ | $c:(b,1),\ f:(b,4),\ e:(a,6),\ d:\infty$ |
| $c$ | $f:(b,4),\ d:(c,6),\ e:(a,6)$ |
| $f$ | $e:(f,2),\ d:(f,5)$ |
| $e$ | $d:(f,5)$ |
| $d$ | None |

The equal edge $cf$ does not replace $bf$ under strict-improvement updates. Other tie conventions can produce a different MST of equal total weight.

Selected edges are $ab,bc,bf,fe,fd$, with total $3+1+4+2+5=15$.

| Implementation | Cost | Useful setting |
|---|---|---|
| Adjacency lists and binary min-heap | $O((\lvert V\rvert+\lvert E\rvert)\log\lvert V\rvert)$, usually $O(\lvert E\rvert\log\lvert V\rvert)$ for connected graphs | Sparse graphs |
| Matrix and linear minimum scan | $\Theta(\lvert V\rvert^2)$ | Dense graphs, simpler implementation |
| Fibonacci heap | $O(\lvert E\rvert+\lvert V\rvert\log\lvert V\rvert)$ amortised | Better theoretical bound with implementation complexity |

For dense graphs, $\lvert E\rvert=\Theta(\lvert V\rvert^2)$, so the matrix version can be preferable to a binary-heap version. The choice depends on representation and data; Prim is not universally faster than Kruskal.

### Kruskal, Limits And Course Skills

Kruskal's method is named in the source and complements Prim:

1. Start with one component per vertex.
2. Sort edges by nondecreasing weight.
3. Include an edge only if its endpoints currently belong to different components.
4. Merge those components; stop after $\lvert V\rvert-1$ included edges.

A **disjoint-set structure** tracks component membership efficiently. Rejecting edges within one component prevents cycles; the cut property supports correctness.

Greedy strengths are simplicity and often low cost. Its limitation is applicability: a feasible local choice can be globally wrong. The course expects you to choose an appropriate design strategy, analyse iterative and recursive costs, and apply common algorithms to sample data, including geometry and graph optimisation.
