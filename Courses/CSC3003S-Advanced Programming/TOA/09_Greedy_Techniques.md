---
tags:
  - advanced-programming
---

# Greedy Techniques

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)
**Source**: [9 - TOA Greedy Techniques.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/9%20-%20TOA%20Greedy%20Techniques.pdf), Patrick Marais, University of Cape Town, pages 1–15
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> The greedy principle, greedy change-making, Huffman coding, minimum spanning trees with Prim's algorithm, and the TOA course conclusion.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#The Greedy Technique|The Greedy Technique]]
  - [[#Change-Making Revisited|Change-Making Revisited]]
  - [[#Text Encoding|Text Encoding]]
  - [[#Huffman Trees And Prefix-Free Codes|Huffman Trees And Prefix-Free Codes]]
  - [[#Huffman Coding Algorithm|Huffman Coding Algorithm]]
  - [[#Notes On Huffman Coding|Notes On Huffman Coding]]
  - [[#Minimum Spanning Trees|Minimum Spanning Trees]]
  - [[#Prim's Algorithm|Prim's Algorithm]]
  - [[#Prim's Algorithm Complexity|Prim's Algorithm Complexity]]
  - [[#Greedy Strengths And Weaknesses|Greedy Strengths And Weaknesses]]
  - [[#Course Conclusion|Course Conclusion]]

---

## Core Content

### The Greedy Technique

#### Definitions

> **Greedy technique**: Repeatedly make the choice that maximises the immediate return, based on local conditions, hoping the outcome is good for the global problem.

> **Feasible choice**: A choice that satisfies the problem's constraints.

> **Locally optimal choice**: The best choice among all feasible options at that step.

> **Irrevocable choice**: A choice that cannot be undone later — no backing out.

Greedy algorithms solve optimisation problems through a sequence of choices that are feasible, locally optimal and irrevocable. Each step greedily grabs the best alternative, hoping the sequence of locally optimal steps leads to a globally optimal solution.

- Sometimes an approximation is acceptable, and local optimality is waived.
- Not all optimisation problems can be solved this way.
- Optimality can sometimes be proved by induction; more complex cases use abstract mathematics such as **matroids**.

Examples:

- Dijkstra's single-source shortest paths
- Minimum spanning tree construction (Prim and Kruskal)
- Change making
- Huffman coding

### Change-Making Revisited

Give change for amount $n$ with the fewest coins, using denominations $d_1 > d_2 > \dots > d_m$.

**Greedy algorithm**: at each step, choose the largest denomination that does not exceed the remaining amount. Repeat until the amount is paid.

Example: R2.54 with R5, R2, R1, 50c, 20c, 10c, 5c, 2c, 1c:

$$
\text{R}2 + 50\text{c} + 2\text{c} + 2\text{c} = \text{R}2.54 \quad (4 \text{ coins})
$$

Greedy is optimal for reasonable (real-world) coin sets, but not for all. With denominations $\{4, 3, 1\}$ and $n = 6$, greedy gives $4 + 1 + 1$ (3 coins), but $3 + 3$ (2 coins) is optimal. The DP algorithm in [Dynamic Programming I](08A_Dynamic_Programming.md#Change-Making%20Problem) handles the general case.

### Text Encoding

#### Definitions

> **Entropy coding**: Assigning bit patterns to an alphabet of characters so that, on typical texts, fewer bits are used overall.

> **Fixed-length encoding**: Every character uses the same number of bits, e.g. ASCII.

> **Variable-length encoding**: The number of bits per character varies with its probability of occurrence, giving better compression, e.g. Morse's telegraph codes.

### Huffman Trees And Prefix-Free Codes

#### Definitions

> **Prefix-free code**: A code in which no character's codeword is a prefix of another's, so a bit stream can be split into characters unambiguously.

> **Huffman tree**: A binary tree implementing a prefix-free code. Leaves are characters, left edges encode 0 and right edges encode 1; a character's codeword is the path from the root to its leaf.

With variable-length codes, you need a way to know which bits belong to which character. Prefix-free codes solve this, and the tree is walked to encode and decode.

Example tree: A = `0`, B = `100`, C = `101`, D = `11`.

![Prefix-free code tree](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/09_Greedy_Techniques/prefix-tree.svg)

*Every character sits at a leaf, so no codeword can be the start of another.*

| Operation | Input | Output |
|---|---|---|
| Encode | `ABADC` | `0 100 0 11 101` = `0100011101` |
| Decode | `11000101` | `11 0 0 0 101` = `DAAAC` |

### Huffman Coding Algorithm

Build a Huffman tree from an alphabet and the characters' probabilities:

1. Initialise $n$ one-node trees, each labelled with a character of the alphabet.
2. Record each character's frequency (weight) in its tree's root.
3. Repeat until a single tree remains:
   1. Find the two trees with the smallest weights.
   2. Make them the left and right subtrees of a new tree, and record the sum of their weights in the new root.

**Example**: C = 0.15, A = 0.4, B = 0.45.

| Step | Trees |
|---|---|
| Start | C (0.15), A (0.4), B (0.45) |
| Merge C and A | (C, A) 0.55; B 0.45 |
| Merge B and (C, A) | Root 1.0 with B on the left and (C, A) on the right |

| Character | Code |
|---|---|
| A | `11` |
| B | `0` |
| C | `10` |

![Huffman construction](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/09_Greedy_Techniques/huffman-build.svg)

*The two lightest trees are merged at each step; the most probable character ends up closest to the root.*

### Notes On Huffman Coding

#### Definitions

> **Compression ratio (CR)**: $\text{CR} = 100 \times \dfrac{y - x}{y}$, where $x$ is the compressed size and $y$ the uncompressed size.

- Huffman coding typically achieves a compression ratio of 20–80%.
- It yields optimal compression provided the character probabilities are independent, known in advance, and negative powers of 2 (e.g. $\tfrac12, \tfrac14, \tfrac18, \tfrac18$).
- It is terrible on bit strings with alphabet $\{0, 1\}$: each symbol still needs at least one bit, so no compression is possible.
- **Adaptive Huffman** coding is more sophisticated: it builds the frequency table on the fly.

### Minimum Spanning Trees

#### Definitions

> **Spanning tree**: For an undirected connected graph, a tree (connected, no cycles) that contains every vertex of the graph exactly once.

> **Minimum spanning tree (MST)**: A spanning tree of minimal total edge weight in a graph with edge weights.

![Spanning tree illustration](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/09_Greedy_Techniques/spanning-tree.svg)

*A spanning tree connects all vertices with no cycles; an MST does so with the smallest total weight.*

MSTs are used in network communications, social media (and other) relationship analysis, approximate TSP solutions, and more.

Exhaustively constructing all spanning trees is exponential, so greedy approaches are used. Both of these produce provably optimal MSTs:

| Algorithm | Builds by | Complexity |
|---|---|---|
| Prim | Adding vertices to one growing tree | $O(\lvert E\rvert \log \lvert V\rvert)$ |
| Kruskal | Adding edges (a growing collection of trees) | $O(\lvert E\rvert \log \lvert E\rvert)$ |

### Prim's Algorithm

Prim's algorithm greedily grows a subtree from an initial vertex $v_1$.

1. Start the tree with $v_1$.
2. Label every other vertex with its nearest tree vertex and the edge weight, e.g. $v_2(v_1, 3)$ means $v_2$ connects to tree vertex $v_1$ with weight 3. Unconnected vertices get weight $\infty$.
3. Repeat until all vertices are in the tree:
   1. Add the nearest non-tree vertex $v^*$ — the one with the lowest edge weight to the tree (it may connect to any tree vertex).
   2. Remove $v^*$ from the list of unprocessed vertices.
   3. **Update labels**: for each non-tree vertex adjacent to $v^*$, if the edge to $v^*$ is lighter than its current label, change its label to $v^*$ and the smaller weight.

Finding the minimum label each round is done with a **min-heap**.

**Example** graph: $ab = 3$, $bc = 1$, $bf = 4$, $cf = 4$, $cd = 6$, $af = 5$, $fd = 5$, $ae = 6$, $fe = 2$, $ed = 8$.

| Tree vertex added | Remaining vertices (labels) |
|---|---|
| $a(-, -)$ | $\mathbf{b(a, 3)}$, $c(-, \infty)$, $d(-, \infty)$, $e(a, 6)$, $f(a, 5)$ |
| $b(a, 3)$ | $\mathbf{c(b, 1)}$, $d(-, \infty)$, $e(a, 6)$, $f(b, 4)$ |
| $c(b, 1)$ | $d(c, 6)$, $e(a, 6)$, $\mathbf{f(b, 4)}$ |
| $f(b, 4)$ | $d(f, 5)$, $\mathbf{e(f, 2)}$ |
| $e(f, 2)$ | $\mathbf{d(f, 5)}$ |
| $d(f, 5)$ | — |

![Prim example](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/09_Greedy_Techniques/prim-example.svg)

*The selected MST edges are $ab, bc, bf, fe, fd$ with total weight $3 + 1 + 4 + 2 + 5 = 15$.*

### Prim's Algorithm Complexity

- With an adjacency-list representation and a min-heap ($O(\log\lvert V\rvert)$ per closest-vertex lookup), the time is $O(\lvert E\rvert \log \lvert V\rvert)$.
- Prim is better than Kruskal for dense graphs.
- It can be optimised further; the best choice depends on the graph's characteristics. A **Fibonacci heap** reduces the time to $O(\lvert E\rvert + \lvert V\rvert \log \lvert V\rvert)$.
- For dense graphs, $\lvert E\rvert = \Theta(\lvert V\rvert^2)$, and easier approaches also exist, since Fibonacci heaps are complex to implement.

### Greedy Strengths And Weaknesses

| Strengths | Weaknesses |
|---|---|
| Intuitively simple and appealing | Only applicable to optimisation problems |
| | Doesn't always produce an optimal solution |
| | More sophisticated alternatives can work better (e.g. arithmetic coding beats Huffman) |

### Course Conclusion

The TOA section covered algorithmic strategies for solving computational problems, including well-known solutions to common optimisation, computational geometry and graph problems.

Key skills:

| Skill | What you must be able to do |
|---|---|
| Problem solving | Understand how to apply the different algorithmic strategies |
| Analysis | Determine the efficiency of a simple iterative or recursive algorithm |
| Knowledge and application | Know the common algorithms under each strategy and apply them to sample data |
