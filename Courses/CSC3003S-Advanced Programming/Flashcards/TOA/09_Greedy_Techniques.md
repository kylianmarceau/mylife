---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 09 — Greedy Techniques"
---

# TOA 09 — Greedy Techniques

**Source note:** [Greedy Techniques](../../TOA/09_Greedy_Techniques.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Greedy Principle|Greedy Principle]]
  - [[#Change Making|Change Making]]
  - [[#Huffman Coding|Huffman Coding]]
  - [[#Minimum Spanning Trees|Minimum Spanning Trees]]

## Core Content

### Greedy Principle

<!-- qard-id: ap-b85e6fc6b1f380bff7f0 -->
> [!qard]- What three properties must each greedy choice have?
> Feasible (meets constraints), locally optimal (best available now), irrevocable (never undone).

<!-- qard-id: ap-d8f2355bc8f1895ee85b -->
> [!qard]- Does a greedy algorithm always find the optimum?
> No — only for some problems; optimality can sometimes be proved by induction or matroid theory.

<!-- qard-id: ap-e97b0149af52dab57f7e -->
> [!qard]- Name four greedy algorithms.
> Dijkstra's shortest paths, Prim's and Kruskal's MST, greedy change making, Huffman coding.

<!-- qard-id: ap-e93ba09042f2cd4f757f -->
> [!qard]- What are greedy's strengths and weaknesses?
> Simple and intuitive; but only for optimisation problems and not always optimal.

### Change Making

<!-- qard-id: ap-1c530ca56e1837448753 -->
> [!qard]- What is the greedy change-making rule?
> Repeatedly take the largest coin not exceeding the remaining amount.

<!-- qard-id: ap-9af0f2c9bb8dcadb413b -->
> [!qard]- Give a denomination set where greedy change making fails.
> $\{4,3,1\}$ for 6: greedy gives $4+1+1$, optimal is $3+3$.

### Huffman Coding

<!-- qard-id: ap-7f73123f94de4b620783 -->
> [!qard]- Fixed-length versus variable-length encoding?
> Fixed: every character uses the same number of bits (ASCII). Variable: frequent characters get shorter codes, compressing better.

<!-- qard-id: ap-07b15f8cd8e1d5f940e6 -->
> [!qard]- What is a prefix-free code and why is it needed?
> No codeword is a prefix of another, so a variable-length bit stream decodes unambiguously.

<!-- qard-id: ap-11e4db17545084c96cc6 -->
> [!qard]- How is a Huffman tree read?
> Characters are leaves; left edges are 0, right edges 1; a codeword is the root-to-leaf path.

<!-- qard-id: ap-18a59b24bf9f42a676a4 -->
> [!qard]- State the Huffman tree construction algorithm.
> Start with one-node trees weighted by frequency; repeatedly merge the two lightest trees under a new root with their summed weight, until one tree remains.

<!-- qard-id: ap-225f55d117921db37957 -->
> [!qard]- Define the compression ratio.
> $100\times(y-x)/y$, where $x$ is the compressed and $y$ the uncompressed size; Huffman typically gets 20–80%.

<!-- qard-id: ap-75194ecaf91c02ad1c4e -->
> [!qard]- When is Huffman coding optimal, and when is it useless?
> Optimal when probabilities are independent, known and negative powers of 2. Useless on a two-symbol alphabet $\{0,1\}$.

<!-- qard-id: ap-c39ba25f87d725102583 -->
> [!qard]- What is adaptive Huffman coding?
> A variant that builds the frequency table on the fly.

### Minimum Spanning Trees

<!-- qard-id: ap-d23eaf08dbc240cd43c0 -->
> [!qard]- Define a spanning tree and a minimum spanning tree.
> Spanning tree: a connected, acyclic subgraph containing every vertex. MST: one with minimum total edge weight.

<!-- qard-id: ap-3de79895efff47f38e61 -->
> [!qard]- How do Prim and Kruskal differ, and what are their complexities?
> Prim grows one tree by adding vertices, $O(|E|\log|V|)$; Kruskal adds cheapest edges across a forest, $O(|E|\log|E|)$.

<!-- qard-id: ap-d45124a73efbf065f9d9 -->
> [!qard]- Describe Prim's algorithm.
> Start from one vertex; repeatedly add the non-tree vertex with the cheapest edge to the tree, then update neighbours' labels if the new vertex offers a cheaper edge.

<!-- qard-id: ap-d01e03c63009c41d818f -->
> [!qard]- What data structure finds Prim's next vertex efficiently?
> A min-heap (priority queue); a Fibonacci heap gives $O(|E|+|V|\log|V|)$.

<!-- qard-id: ap-51b5bb2628d17d565355 -->
> [!qard]- Is Prim or Kruskal better for dense graphs?
> Prim.
