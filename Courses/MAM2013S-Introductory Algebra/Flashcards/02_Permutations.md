---
tags:
  - introductory-algebra
  - flashcards
qard-deck: "Introductory Algebra"
qard-topic: "02 — Permutations: Composition, Cycles, and Parity"
---

# 02 — Permutations: Composition, Cycles, and Parity

**Source note:** [Permutations: Composition, Cycles, and Parity](../02_Permutations.md)

Exam recall cards covering concepts, definitions, methods, and qualifications. Worked examples are omitted; general proof methods are retained.

## Contents

- [[#Core Content|Core Content]]
  - [[#What Is a Permutation?|What Is a Permutation?]]
  - [[#Product of Permutations|Product of Permutations]]
  - [[#Inverse Permutations|Inverse Permutations]]
  - [[#Disjoint Permutations|Disjoint Permutations]]
  - [[#Cycles and Cycle Decomposition|Cycles and Cycle Decomposition]]
  - [[#Transpositions, Parity, and the Alternating Group|Transpositions, Parity, and the Alternating Group]]

## Core Content

### What Is a Permutation?

<!-- qard-id: alg-f7ac04e58105481c5767 -->
> [!qard]- What is a function $f:A\to B$?
> It assigns exactly one element of $B$ to every element of $A$; different inputs may share an output unless injectivity is required.

<!-- qard-id: alg-200b0f6261cc4b329a7f -->
> [!qard]- What do injective, surjective, and bijective mean?
> Injective: distinct inputs have distinct images. Surjective: every target is reached. Bijective: both injective and surjective.

<!-- qard-id: alg-2dc837407b7b9a8c0605 -->
> [!qard]- What is a permutation of a set $X$?
> A bijection $\sigma:X\to X$, rearranging without losing or repeating elements.

<!-- qard-id: alg-29f783b01d1a8921f43a -->
> [!qard]- What is the symmetric group $S_n$?
> All permutations of $X_n=\{1,2,\ldots,n\}$ with function composition as the operation.

<!-- qard-id: alg-cc46d64d76d7cf69f4ea -->
> [!qard]- How is two-row permutation notation interpreted?
> Each top-row input is directly above its bottom-row image; it represents a function, not a matrix to multiply numerically.

<!-- qard-id: alg-daa4113f993199b5bf76 -->
> [!qard]- What must a valid two-row permutation’s bottom row contain?
> Every underlying-set element exactly once.

<!-- qard-id: alg-527ff3113815f7f3af25 -->
> [!qard]- When are two permutations equal?
> When they send every input to the same image.

<!-- qard-id: alg-e547b3a8413b54f6ec16 -->
> [!qard]- What is $|S_n|$?
> $n!$.

<!-- qard-id: alg-c0919734dc29e1bbe1d6 -->
> [!qard]- How is the size of $S_n$ proved?
> Choose images without repetition: $n$ choices, then $n-1$, down to one. The multiplication principle gives $n!$, counting every bijection exactly once.

<!-- qard-id: alg-5e23e64f49a909b22843 -->
> [!qard]- What counting principle justifies multiplying successive choice counts?
> If each of $m$ first choices has exactly $r$ second choices, there are $mr$ pairs; repeat for the remaining stages.

### Product of Permutations

<!-- qard-id: alg-eea51294831ee544b231 -->
> [!qard]- What is the product $\gamma\sigma$ of permutations?
> Composition $\gamma\circ\sigma$, with $(\gamma\sigma)(k)=\gamma(\sigma(k))$.

<!-- qard-id: alg-2cdb39e283d7d171a9f1 -->
> [!qard]- Which factor acts first in a permutation product?
> The rightmost factor, in both two-row and cycle notation.

<!-- qard-id: alg-d71a0e0271c695b478f7 -->
> [!qard]- Why is a product of permutations a permutation?
> Composition of bijections is a bijection, so $S_n$ is closed under composition.

<!-- qard-id: alg-5bfd4373724dd177f9fe -->
> [!qard]- How do you compute a product in two-row notation?
> For each input, follow its image through the rightmost map and then the left map; record the final image and repeat for every input.

<!-- qard-id: alg-a5513de5c14978b69640 -->
> [!qard]- What does it mean for permutations to commute?
> $\sigma\tau=\tau\sigma$.

<!-- qard-id: alg-47512d67766e392b77d1 -->
> [!qard]- Is permutation multiplication commutative in general?
> No. Changing factor order can change images.

<!-- qard-id: alg-864c894123611651b742 -->
> [!qard]- Why is permutation multiplication associative?
> Both $(\sigma\tau)\mu$ and $\sigma(\tau\mu)$ send $k$ to $\sigma(\tau(\mu(k)))$.

<!-- qard-id: alg-b785b5d70be565586b56 -->
> [!qard]- What rearrangement does associativity allow—and leave forbidden?
> Change brackets without changing factor order; it does not permit swapping factors.

<!-- qard-id: alg-73e9d79c7a2542a97b85 -->
> [!qard]- What is the identity permutation?
> $\varepsilon(k)=k$ for every input, satisfying $\varepsilon\sigma=\sigma=\sigma\varepsilon$.

<!-- qard-id: alg-75039ebecfb45be8bf0d -->
> [!qard]- What is a power of a permutation?
> Repeated composition of that same permutation.

<!-- qard-id: alg-cf1fa5bfe14b31b3c9db -->
> [!qard]- How can counting establish completeness of a constructed permutation list?
> Show all listed permutations are distinct and that their number equals $|S_n|=n!$.

### Inverse Permutations

<!-- qard-id: alg-6cb8f92b5c71e1e7e147 -->
> [!qard]- What is an inverse permutation?
> The unique bijection reversing $\sigma$, satisfying $\sigma\sigma^{-1}=\sigma^{-1}\sigma=\varepsilon$.

<!-- qard-id: alg-157ce0c74f747bdb2587 -->
> [!qard]- How are images related to inverse images?
> If $\sigma(k)=j$, then $\sigma^{-1}(j)=k$.

<!-- qard-id: alg-fb0b610d404e73c9bdb3 -->
> [!qard]- How do you invert a two-row permutation?
> Swap the rows, then reorder whole columns to put the new input row in standard order.

<!-- qard-id: alg-27164a0fdd125fa67c4c -->
> [!qard]- Why does reordering whole columns preserve a permutation?
> Each input remains paired with its image, so the function is unchanged.

<!-- qard-id: alg-ff3095736b21fe0c6bc9 -->
> [!qard]- How do you verify a proposed inverse?
> Check that both compositions fix every point, or directly verify that every image is mapped back to its input.

### Disjoint Permutations

<!-- qard-id: alg-c33a77e427f40f04639c -->
> [!qard]- What are fixed points, moved points, and support?
> Fixed points satisfy $\sigma(k)=k$; moved points do not; support is $M_\sigma=\{k:\sigma(k)\ne k\}$.

<!-- qard-id: alg-dc1f947af81edf5e84d2 -->
> [!qard]- Which permutation fixes every point?
> Only the identity.

<!-- qard-id: alg-74fe650702a1d7f9bd44 -->
> [!qard]- What does disjointness of permutations mean?
> Their moved sets are disjoint: $M_\sigma\cap M_\tau=\varnothing$.

<!-- qard-id: alg-c8827039cf25adbd4f63 -->
> [!qard]- Why must the image of a moved point also be moved?
> If $\sigma(\sigma(k))=\sigma(k)$, injectivity gives $\sigma(k)=k$, contradicting that $k$ is moved.

<!-- qard-id: alg-4f90d1e802ab4d5b762d -->
> [!qard]- State the commuting theorem for disjoint permutations.
> Disjoint permutations commute.

<!-- qard-id: alg-68339f3fc655d9f77782 -->
> [!qard]- How is commutation of disjoint permutations proved?
> Split inputs into support of $\sigma$, support of $\tau$, or neither. The other permutation fixes both a moved point and its image, so both products agree in each case.

<!-- qard-id: alg-bcd83669a5697029ee50 -->
> [!qard]- Does commutation imply disjointness?
> No. A permutation commutes with its inverse even though they typically share the same moved points.

### Cycles and Cycle Decomposition

<!-- qard-id: alg-67c175ab548066fe57ee -->
> [!qard]- What is an $r$-cycle?
> For distinct $k_1,\ldots,k_r$, $(k_1\,\cdots\,k_r)$ sends each entry to the next, the last to the first, and fixes unlisted points.

<!-- qard-id: alg-d099468902ff0670656c -->
> [!qard]- What is a transposition?
> A two-cycle swapping two points and fixing all others.

<!-- qard-id: alg-ffe5b5a70bee4a791f2b -->
> [!qard]- What is a disjoint-cycle decomposition?
> A product of cycles whose moved sets are pairwise disjoint.

<!-- qard-id: alg-bd1cbd3ef288f50f4cfe -->
> [!qard]- Why does rotating a cycle’s written starting point leave it unchanged?
> It preserves the same directed traversal and image of every listed point.

<!-- qard-id: alg-ad9530d3faf8c189a15c -->
> [!qard]- What does a written one-cycle do?
> It is the identity on the entire underlying set, moving no points.

<!-- qard-id: alg-1cf3a16a19e5f2438757 -->
> [!qard]- How do you invert a cycle?
> Reverse its traversal: $(k_1\,\cdots\,k_r)^{-1}=(k_r\,\cdots\,k_1)$.

<!-- qard-id: alg-069e4d931177b3479408 -->
> [!qard]- Why does reversing a cycle give its inverse?
> It moves each listed point one step backward, undoing the original forward step; both fix all unlisted points.

<!-- qard-id: alg-3015bb33098fd38ac88b -->
> [!qard]- Why does the ambient set matter in cycle notation?
> The cycle also acts on all unlisted ambient points by fixing them; notation alone does not specify the entire underlying set.

<!-- qard-id: alg-967c304f9a13be863b06 -->
> [!qard]- How do you find all disjoint cycles of a permutation?
> Choose an unprocessed point, follow repeated images until returning to it, record the cycle, then repeat with remaining points; fixed points may be omitted but must be recognized.

<!-- qard-id: alg-779eed1acd98baabf8b3 -->
> [!qard]- When can disjoint cycles be detected by nonoverlapping written lists?
> For cycles of length at least two. One-cycles move nothing, so they are exceptions to the list-based test.

<!-- qard-id: alg-84ae0838483027e64b4e -->
> [!qard]- State the disjoint-cycle decomposition theorem.
> Every nonidentity permutation is a product of disjoint cycles of length at least two, unique up to factor order and each cycle’s starting point.

<!-- qard-id: alg-dfcfb06045f665abbf16 -->
> [!qard]- How does the inductive existence proof handle a permutation fixing $n$?
> Restrict it to $X_{n-1}$ and apply induction; an identity restriction contributes no nontrivial cycles.

<!-- qard-id: alg-89d648a5dbb2ed1e12fb -->
> [!qard]- How does the existence proof reduce the case where $n$ is moved?
> Set $k=\sigma^{-1}(n)$ and $\tau=\sigma(k\,n)$; then $\tau$ fixes $n$ and $\sigma=\tau(k\,n)$.

<!-- qard-id: alg-70332dbe63d34efc8555 -->
> [!qard]- How is $n$ inserted when $\tau$ already has a cycle containing $k$?
> Replace $(k\,k_1\,\cdots\,k_r)(k\,n)$ by $(k\,n\,k_1\,\cdots\,k_r)$; other cycles remain disjoint.

<!-- qard-id: alg-ff23e01702bfa69d439d -->
> [!qard]- How is the existence proof completed when $\tau$ fixes $k$?
> Append $(k\,n)$ as a disjoint cycle to its existing decomposition.

<!-- qard-id: alg-f045a01c157439e6de2c -->
> [!qard]- Why is disjoint-cycle decomposition unique?
> A moved point’s successive images force its complete cycle in any decomposition; cancel that common cycle and repeat on the remaining factors.

<!-- qard-id: alg-cfceb01cd177815a2141 -->
> [!qard]- How should overlapping cycles be multiplied?
> Apply them right to left on every relevant point; they generally cannot be reordered.

### Transpositions, Parity, and the Alternating Group

<!-- qard-id: alg-eb5bff0d86dc352b8e8f -->
> [!qard]- What is the inverse and square of a transposition $\delta$?
> $\delta^{-1}=\delta$ and $\delta^2=\varepsilon$.

<!-- qard-id: alg-4c00014e479b37d08555 -->
> [!qard]- How is an $r$-cycle expressed as $r-1$ transpositions?
> $(k_1\,\cdots\,k_r)=(k_1\,k_2)(k_2\,k_3)\cdots(k_{r-1}\,k_r)$, acting right to left.

<!-- qard-id: alg-dfdf167b2ef5309dedcf -->
> [!qard]- Why does that adjacent-transposition product implement the cycle?
> Each $k_i$ with $i<r$ ends at $k_{i+1}$; $k_r$ moves backward through the swaps to $k_1$; unlisted points stay fixed.

<!-- qard-id: alg-0b54d798e88846798f8f -->
> [!qard]- How is a one-cycle interpreted in the transposition-factorization formula?
> As an empty product of zero transpositions, equal to the identity.

<!-- qard-id: alg-223e231aff69ee022ae6 -->
> [!qard]- Why is every permutation a product of transpositions?
> Decompose into disjoint cycles, then replace each cycle with a transposition product.

<!-- qard-id: alg-032fb049ea14165f19fd -->
> [!qard]- Are transposition factorizations unique?
> No. Their lengths may differ, but their parity is invariant.

<!-- qard-id: alg-80f786b6b14c4cdf400f -->
> [!qard]- What are even and odd permutations?
> Those expressible as products of an even or odd number of transpositions respectively.

<!-- qard-id: alg-0da3aade5140709cb549 -->
> [!qard]- State the parity theorem.
> Any two transposition factorizations of the same permutation have lengths of the same parity; no permutation is both even and odd.

<!-- qard-id: alg-74f01031d9fc509ee9af -->
> [!qard]- How do you compute parity from disjoint cycle lengths $r_1,\ldots,r_t$?
> Compute the parity of $\sum_i(r_i-1)$.

<!-- qard-id: alg-ce5d5bc0b2d1dc5ceb50 -->
> [!qard]- What is the parity of a cycle of odd or even length?
> Odd length gives an even cycle; even length gives an odd cycle, since the transposition count is $r-1$.

<!-- qard-id: alg-b97f2eaa240054119204 -->
> [!qard]- What identity-factorization lemma establishes well-defined parity?
> The identity cannot be a product of an odd number of transpositions.

<!-- qard-id: alg-02145fc5e8441f20ad88 -->
> [!qard]- What is the inductive idea behind the identity-factorization lemma?
> Sweep a chosen moved letter’s transposition left using rewrites. Identical transpositions cancel in pairs; without cancellation only the first remaining factor moves that letter, contradicting identity.

<!-- qard-id: alg-08d2337545008ff1df9f -->
> [!qard]- Which transposition rewrite moves a shared letter past an overlapping factor?
> For distinct $a,b,c$, $(a\,c)(a\,b)=(a\,b)(b\,c)$, or $(b\,c)(a\,b)=(a\,c)(b\,c)$.

<!-- qard-id: alg-1553ee127a79b3549054 -->
> [!qard]- How do disjoint transpositions participate in the parity-lemma sweep?
> They commute, letting the selected transposition move left without changing the product.

<!-- qard-id: alg-136a70a05802756a7d78 -->
> [!qard]- Why does cancelling two identical transpositions preserve parity in the lemma?
> It removes two factors, producing a shorter identity expression to which strong induction applies.

<!-- qard-id: alg-165d09526c11219d708f -->
> [!qard]- How does the identity lemma prove the parity theorem?
> Combine one factorization with the inverse of another to get identity with $r+s$ transpositions; this sum is even, so $r$ and $s$ have the same parity.

<!-- qard-id: alg-2dc36ac6470931eb8732 -->
> [!qard]- What is the alternating group $A_n$?
> The set of even permutations in $S_n$.

<!-- qard-id: alg-95d19a2838bda7d55283 -->
> [!qard]- Why is the identity in $A_n$?
> It has an even transposition expression, including the empty product or two identical transpositions.

<!-- qard-id: alg-2b4ca00e9b245432a43c -->
> [!qard]- Why is $A_n$ closed under products?
> Concatenating two even transposition expressions gives an even total length.

<!-- qard-id: alg-bbd50eddce019fa2aa6b -->
> [!qard]- Why is the inverse of an even permutation even?
> Invert by reversing its transposition sequence; transpositions are self-inverse, so the count is unchanged.

<!-- qard-id: alg-21dbf06ffb75b138ddb0 -->
> [!qard]- What is $|A_n|$ for $n\ge2$?
> $n!/2$.

<!-- qard-id: alg-9680ccdd0b1c60648890 -->
> [!qard]- How is the size of $A_n$ proved?
> Multiplication by a fixed transposition bijects even and odd permutations and is its own inverse; they partition $S_n$, so each has half its $n!$ elements.

<!-- qard-id: alg-9b0b16b2357230cc7dd1 -->
> [!qard]- What conditions define a group of permutations?
> Include identity and be closed under products and inverses; associativity is inherited from composition. Both $S_n$ and $A_n$ qualify.
