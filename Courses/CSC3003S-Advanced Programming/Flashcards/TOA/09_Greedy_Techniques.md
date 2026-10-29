---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 09 — Greedy Techniques"
---

# TOA 09 — Greedy Techniques

**Source note:** [Greedy Techniques](../../TOA/09_Greedy_Techniques.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Greedy Choices And Optimality|Greedy Choices And Optimality]]
  - [[#Greedy Change Making|Greedy Change Making]]
  - [[#Fixed-Length And Prefix-Free Codes|Fixed-Length And Prefix-Free Codes]]
  - [[#Huffman Construction|Huffman Construction]]
  - [[#Huffman Optimality, Compression And Limits|Huffman Optimality, Compression And Limits]]
  - [[#Minimum Spanning Trees|Minimum Spanning Trees]]
  - [[#Prim's Algorithm|Prim's Algorithm]]
  - [[#Prim Complexity And Implementation Choices|Prim Complexity And Implementation Choices]]
  - [[#Kruskal, Limits And Course Skills|Kruskal, Limits And Course Skills]]
  - [[#Prim Source Example And Complexity|Prim Source Example And Complexity]]
  - [[#Greedy Guarantees And Coding|Greedy Guarantees And Coding]]
  - [[#Spanning-Tree Invariants|Spanning-Tree Invariants]]

## Core Content

### Greedy Choices And Optimality

<!-- qard-id: ap-b600172baca345d09885 -->
> [!qard]- What is the greedy technique?
> Build a solution by repeatedly committing to a feasible locally best choice.

<!-- qard-id: ap-eaf64cad49208bbad445 -->
> [!qard]- Does local optimality imply global optimality?
> No. A greedy rule needs an optimality proof or an explicitly weaker guarantee.

<!-- qard-id: ap-688710783b8b4206cbc3 -->
> [!qard]- What is an exchange argument?
> Transform an optimal solution to include the greedy choice without worsening its cost.

<!-- qard-id: ap-effb2634e8042450a7ee -->
> [!qard]- How does greedy selection differ from dynamic programming?
> Greedy commits to a local choice; DP considers alternatives and stores state results.

<!-- qard-id: ap-40453b63955b163ac613 -->
> [!qard]- How can induction and exchange structure support greedy correctness, and when is a heuristic acceptable?
> Prove the chosen step can belong to an optimum, then reduce to the remaining problem; some independence systems formalise this through matroids. Without exact optimality, state the heuristic/approximation guarantee rather than assuming it.

<!-- qard-id: ap-667ea49596a207653d7e -->
> [!qard]- What edge-weight restriction supports Dijkstra's settled-distance greedy argument?
> Nonnegative edge weights. A negative edge can invalidate the conclusion that an extracted tentative distance can never improve; the notes name Dijkstra without developing the full algorithm.

### Greedy Change Making

<!-- qard-id: ap-8f5f4774550cf22ab321 -->
> [!qard]- Why does a unit coin not guarantee optimal greedy change?
> It guarantees exact change is feasible, not minimal. With coins $1,3,4$ and target $6$, greedy uses $4+1+1$, while $3+3$ uses fewer coins.

<!-- qard-id: ap-a7025fa9736434ef6784 -->
> [!qard]- How does denomination-loop greedy change work, and why use integer currency units?
> In descending denominations, take $\lfloor amount/d\rfloor$ coins and reduce the remainder; report failure if it stays nonzero. Integer smallest units avoid floating-point currency errors. For 254 cents, $200+50+2+2$ uses four coins.

### Fixed-Length And Prefix-Free Codes

<!-- qard-id: ap-b12ab59f17bc278f01ca -->
> [!qard]- What is a prefix-free code?
> No complete symbol codeword is a prefix of another codeword.

<!-- qard-id: ap-79062fcb38520218182b -->
> [!qard]- How is a binary prefix-free tree decoded?
> Follow bits from the root to a symbol leaf, emit it, then restart at the root.

<!-- qard-id: ap-6077e333a5ce46b298f3 -->
> [!qard]- How do fixed-length, variable-length and entropy coding relate?
> Fixed-width codes split at known boundaries; variable widths can assign short words to frequent symbols. Entropy coding exploits frequencies, while prefix-free codes allow unambiguous leaf-by-leaf decoding without external separators.

<!-- qard-id: ap-9d63678e7fbe8bf5958e -->
> [!qard]- Why must a prefix tree store symbols only at leaves, and why does Morse need extra signalling?
> A leaf cannot prefix another leaf's path. Morse's variable-length words rely on timing/separators, so the raw signal symbols alone are not a binary prefix-free code.

### Huffman Construction

<!-- qard-id: ap-42a4b020ed3f412e65c1 -->
> [!qard]- How is a Huffman tree built?
> Start with one weighted leaf per symbol. Repeatedly remove the two lowest-weight trees, join them under a parent weighted by their sum, and reinsert it until one tree remains.

<!-- qard-id: ap-666b7276f64fffb147b2 -->
> [!qard]- How are codewords read from a completed Huffman tree?
> Label branches with bits and read the root-to-leaf path for each symbol.

<!-- qard-id: ap-26f551452500bd086894 -->
> [!qard]- What is expected code length for symbol probabilities $p(s)$ and lengths $\ell(s)$?
> $L=\sum_sp(s)\ell(s)$ bits per symbol.

<!-- qard-id: ap-da36f8535848e16d810b -->
> [!qard]- What is Huffman construction's cost with a binary heap?
> $O(s\log s)$ time and $O(s)$ tree storage.

### Huffman Optimality, Compression And Limits

<!-- qard-id: ap-e60c25b7f498d19e1b05 -->
> [!qard]- Why is Huffman's greedy merge safe?
> An optimal binary prefix tree can place the two least probable symbols as deepest siblings. Merge them, solve the smaller problem, then expand; the added expected length is exactly their total probability.

<!-- qard-id: ap-21e0c999c4162673ed7a -->
> [!qard]- What class of codes does Huffman optimise?
> Symbol-by-symbol binary prefix codes for the specified symbol probabilities.

<!-- qard-id: ap-544a7b0f0bbbf7035901 -->
> [!qard]- Why can two-symbol Huffman coding fail to exploit a heavily biased bit stream?
> Both symbols normally need a one-bit codeword, so symbol-by-symbol coding cannot go below one bit each. Block coding or arithmetic coding can exploit skew more closely; adaptive Huffman updates frequencies during processing.

<!-- qard-id: ap-acf745c9638b3694deac -->
> [!qard]- What compression percentage convention and practical overhead do the notes use?
> Saving is $100(y-x)/y$ for original size $y$ and encoded size $x$. Include the code tree/model and headers; illustrative percentages are not universal guarantees or the only “compression ratio” convention.

### Minimum Spanning Trees

<!-- qard-id: ap-7739af4e78b4fa517bfb -->
> [!qard]- What is a minimum spanning tree?
> A connected, acyclic subgraph spanning all vertices of a connected undirected weighted graph, minimising total edge weight. It has $|V|-1$ edges.

<!-- qard-id: ap-6936b20f7532290c3dad -->
> [!qard]- What objective distinguishes an MST from source shortest paths?
> An MST minimises the network's total edge weight, not each vertex's distance from a source.

<!-- qard-id: ap-159008368a946e229864 -->
> [!qard]- What safe greedy step does the MST cut property justify?
> For a cut respecting the selected tree edges, a minimum-weight crossing edge can be included in an MST consistent with those edges.

<!-- qard-id: ap-7b044829c7246f12a9d7 -->
> [!qard]- How do Prim's and Kruskal's greedy choices differ?
> Prim takes the lightest edge from the current tree to a new vertex; Kruskal takes the lightest edge connecting different forest components.

<!-- qard-id: ap-4140f01f09e2380f313b -->
> [!qard]- How does an exchange argument justify the MST cut property?
> A minimum crossing edge respecting chosen forest edges can replace a no-lighter crossing edge in an optimum, preserving a spanning tree without increasing total weight. Ties may yield several MSTs.

### Prim's Algorithm

<!-- qard-id: ap-40e7ba35c10acef113a7 -->
> [!qard]- What is a vertex key in Prim's algorithm?
> The lowest known edge weight connecting that non-tree vertex to any current tree vertex.

<!-- qard-id: ap-2ad88b24028ce811a40d -->
> [!qard]- How does Prim update a neighbour outside the tree?
> If the edge from the newly selected vertex is lighter than its key, update the key and parent and perform decrease-key.

<!-- qard-id: ap-5a7b66bacbdf618be3d1 -->
> [!qard]- How does Prim's key differ from Dijkstra's tentative distance?
> Prim stores one connecting-edge weight; Dijkstra stores a complete source-to-vertex path length.

<!-- qard-id: ap-8e459d274e65e337e218 -->
> [!qard]- How is Prim initialised, and what does an extracted infinite key reveal?
> Pick any start with key zero; others have infinity and no parent. Repeatedly extract minimum, add its parent edge and relax only outside neighbours. An infinite extracted key means the connected-graph algorithm cannot reach that component.

### Prim Complexity And Implementation Choices

<!-- qard-id: ap-9aaf1d3be5c93b4bf4a4 -->
> [!qard]- What time does Prim use with adjacency lists and a binary min-heap?
> $O((\lvert V\rvert+\lvert E\rvert)\log\lvert V\rvert)$, usually $O(\lvert E\rvert\log\lvert V\rvert)$ on connected graphs.

<!-- qard-id: ap-ace969a624950bc7ddfe -->
> [!qard]- What time does Prim use with a matrix and linear minimum scans?
> $\Theta(\lvert V\rvert^2)$.

### Kruskal, Limits And Course Skills

<!-- qard-id: ap-9798f5d90d4c29233fd5 -->
> [!qard]- What are the steps of Kruskal's algorithm?
> Start with one component per vertex, sort edges by weight, accept only edges joining different components, merge those components, and stop at $\lvert V\rvert-1$ accepted edges.

<!-- qard-id: ap-81b62d3a5e075970ce20 -->
> [!qard]- What is Kruskal's typical time bound?
> $O(\lvert E\rvert\log\lvert E\rvert)$, dominated by sorting edges.

### Prim Source Example And Complexity

<!-- qard-id: ap-4a26eee0f652459ad321 -->
> [!qard]- How do density and priority-queue choice affect Prim's cost?
> Binary heaps suit sparse graphs; on dense graphs a matrix's $\Theta(V^2)$ may beat $O(E\log V)$. Fibonacci heaps give $O(E+V\log V)$ amortised but add implementation complexity; no implementation is universally fastest.

### Greedy Guarantees And Coding

<!-- qard-id: ap-d96f1eea8e4ad888d02c -->
> [!qard]- What separates feasibility, local optimality and irrevocability of a greedy choice?
> Feasibility meets constraints; local optimality is best by the current criterion; irrevocability commits without later undo. None by itself proves the full solution globally optimal.

<!-- qard-id: ap-e65fa1d04169c55315f7 -->
> [!qard]- What must an exchange argument preserve when inserting a greedy choice into an optimum?
> Feasibility and an objective value no worse than the original optimum, leaving a smaller compatible subproblem for the next step.

<!-- qard-id: ap-67dbe7b579c251bb784f -->
> [!qard]- Why do Huffman internal weights equal the sum of their descendant symbol weights?
> Merging combines those symbols into one reduced-problem alternative, so its occurrence weight is their total; the priority queue must compare these combined weights thereafter.

<!-- qard-id: ap-9428451ecaf2abe10538 -->
> [!qard]- Why can Huffman codewords change while expected encoded length stays optimal?
> Ties and left/right branch labels can produce different codes with the same relevant depths/weighted length; encoder and decoder still need the same chosen code.

<!-- qard-id: ap-6d60fbdac6f95abd1f76 -->
> [!qard]- How does the weighted path-length objective connect Huffman to compression?
> Each symbol contributes its probability/frequency times its leaf depth; the sum is the average bits per symbol before model/header overhead.

### Spanning-Tree Invariants

<!-- qard-id: ap-43a12047cd499d5bbf9f -->
> [!qard]- Why does Prim update only vertices still outside the selected tree?
> Their keys represent candidate attachments. Already selected vertices have fixed tree membership; treating updates as new choices can violate the intended construction.

<!-- qard-id: ap-6c2730ce79009639f03f -->
> [!qard]- Why does Kruskal reject an edge whose endpoints are already connected in the selected forest?
> A path already joins them, so adding the edge would make a cycle rather than connect two components.

<!-- qard-id: ap-d335e8d93d8dc5c8847a -->
> [!qard]- How does disjoint-set union support Kruskal's invariant?
> Find identifies each endpoint's current component; union merges components after accepting an edge, maintaining exactly the forest's connectivity partition.
