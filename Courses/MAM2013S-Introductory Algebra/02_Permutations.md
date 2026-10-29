---
tags:
  - introductory-algebra
---

# Permutations: Composition, Cycles, and Parity

> [!abstract] <span style="color: #b89aff">Chapter reference</span>
> **Subject**: MAM2013S Introductory Algebra  
> **Source**: [Introductory Algebra — 2IA notes](../../Sources/MAM2013S%20-%20Introductory%20algebra/2IA%20notes.pdf), J. Sánchez-Ortega, Chapter 2, printed pages 33–54 (PDF pages 36–57)  
> **Generated**: 2026-10-03  
> **Scope**: The permutations chapter only. Arithmetic and typographical slips in the source are corrected in the derivations below.  
> **Related notes**: [Integers](01_Integers.md), [Groups](03_Groups.md)

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Is a Permutation?|What Is a Permutation?]]
  - [[#Product of Permutations|Product of Permutations]]
  - [[#Inverse Permutations|Inverse Permutations]]
  - [[#Disjoint Permutations|Disjoint Permutations]]
  - [[#Cycles and Cycle Decomposition|Cycles and Cycle Decomposition]]
  - [[#Transpositions, Parity, and the Alternating Group|Transpositions, Parity, and the Alternating Group]]

---

## Core Content

### What Is a Permutation?

#### Definitions

> **Bijection**: A map that is both one-to-one (different inputs have different images) and onto (every target element is an image).

> **Permutation of a set**: A bijection $\sigma:X\to X$ from a set onto itself.

> **Symmetric group of degree $n$**: The set $S_n$ of all permutations of $X_n=\{1,2,\ldots,n\}$, with composition as its operation.

> **Two-row / matrix-type notation**: The expression $\sigma=\begin{pmatrix}1&2&\cdots&n\\\sigma(1)&\sigma(2)&\cdots&\sigma(n)\end{pmatrix}$, with each input directly above its image.

A permutation rearranges a set without losing or repeating any element. It is still a function even when written in matrix-type notation; multiplication of permutations means composition of functions, not matrix multiplication.

For $X_3$, the six possible rearrangements are:

| Images of $1,2,3$, in that order | Function description |
|---|---|
| $1,2,3$ | $1\mapsto1$, $2\mapsto2$, $3\mapsto3$ |
| $1,3,2$ | $1\mapsto1$, $2\mapsto3$, $3\mapsto2$ |
| $2,1,3$ | $1\mapsto2$, $2\mapsto1$, $3\mapsto3$ |
| $2,3,1$ | $1\mapsto2$, $2\mapsto3$, $3\mapsto1$ |
| $3,1,2$ | $1\mapsto3$, $2\mapsto1$, $3\mapsto2$ |
| $3,2,1$ | $1\mapsto3$, $2\mapsto2$, $3\mapsto1$ |

Two permutations are equal exactly when they have the same image for every input. A proposed two-row expression is a permutation only if the bottom row contains every element of the top row exactly once.

Examples 2.1 are

$$
\sigma=\begin{pmatrix}1&2&3&4\\3&1&4&2\end{pmatrix}\in S_4,
\qquad
\beta=\begin{pmatrix}1&2&3&4&5&6\\6&3&1&5&2&4\end{pmatrix}\in S_6.
$$

![Reading a two-row permutation downwards and its inverse upwards](../../diagrams/MAM2013S-Introductory%20Algebra/02_Permutations/two-row-notation.svg)

*Each column pairs an input with its image. Reading down gives the map; reading up reverses it.*

**Theorem 2.2**: $|S_n|=n!$.

To construct a permutation, choose its images without repetition:

1. There are $n$ choices for $\sigma(1)$.
2. There are $n-1$ remaining choices for $\sigma(2)$.
3. Continue until the last image has only one choice.

The total is $n(n-1)\cdots2\cdot1=n!$. Every choice gives exactly one bijection, so none is omitted or counted twice.

A **function** $f:A\to B$ assigns exactly one element of $B$ to each element of $A$. This allows different inputs to share an output; **injectivity** rules out such sharing. **Surjectivity** means every element of the target set $B$ is reached. For counting successive choices, if there are $m$ first choices and each has exactly $r$ second choices, there are $mr$ pairs: each first choice contributes a separate group of $r$ pairs. Applying this reasoning repeatedly to permutation images gives $n(n-1)\cdots1$, since each chosen image removes one available target.

### Product of Permutations

#### Definitions

> **Product of permutations**: $\gamma\sigma=\gamma\circ\sigma$, defined by $(\gamma\sigma)(k)=\gamma(\sigma(k))$.

> **Commuting permutations**: Permutations satisfying $\sigma\tau=\tau\sigma$.

> **Identity permutation**: The map $\varepsilon(k)=k$ for every $k\in X_n$.

> **Power of a permutation**: Repeated composition of the same permutation, such as $\alpha^2=\alpha\alpha$ and $\alpha^3=\alpha\alpha\alpha$.

> [!important] <span style="color: #66b3ff">The rightmost permutation acts first</span>
> In $\gamma\sigma$, first apply $\sigma$, then $\gamma$. Keep this convention when using either two-row or cycle notation.

Composition of bijections is a bijection, so the product remains in $S_n$.

To compute a product in two-row notation:

1. Choose an input $k$ from the top row of the rightmost permutation.
2. Read its image $a=\sigma(k)$.
3. Locate $a$ in the top row of the left permutation and read $\gamma(a)$.
4. Put the resulting value beneath $k$ in the product.
5. Repeat for every input.

For

$$
\sigma=\begin{pmatrix}1&2&3&4&5\\2&4&3&5&1\end{pmatrix},
\quad
\gamma=\begin{pmatrix}1&2&3&4&5\\5&4&1&2&3\end{pmatrix},
$$

we obtain

| $k$ | $\sigma(k)$ | $\gamma(\sigma(k))$ |
|---|---|---|
| $1$ | $2$ | $4$ |
| $2$ | $4$ | $2$ |
| $3$ | $3$ | $1$ |
| $4$ | $5$ | $3$ |
| $5$ | $1$ | $5$ |

Thus $\gamma\sigma=\begin{pmatrix}1&2&3&4&5\\4&2&1&3&5\end{pmatrix}$.

In Example 2.3,

$$
\alpha=\begin{pmatrix}1&2&3\\1&3&2\end{pmatrix},
\qquad
\beta=\begin{pmatrix}1&2&3\\3&1&2\end{pmatrix},
\qquad
\alpha\beta=\begin{pmatrix}1&2&3\\2&1&3\end{pmatrix}.
$$

![Composition of the two permutations in Example 2.3](../../diagrams/MAM2013S-Introductory%20Algebra/02_Permutations/composition-example.svg)

*Follow each input through the blue arrows for the right permutation, then through the teal arrows for the left permutation. The resulting path gives the product.*

#### Order matters, but brackets do not

For Example 2.4, take

$$
\sigma=\begin{pmatrix}1&2&3&4\\3&4&1&2\end{pmatrix},
\qquad
\tau=\begin{pmatrix}1&2&3&4\\2&4&3&1\end{pmatrix}.
$$

Their products are

$$
\sigma\tau=\begin{pmatrix}1&2&3&4\\4&2&1&3\end{pmatrix},
\qquad
\tau\sigma=\begin{pmatrix}1&2&3&4\\3&1&2&4\end{pmatrix}.
$$

![The products in both possible orders](../../diagrams/MAM2013S-Introductory%20Algebra/02_Permutations/composition-order.svg)

*Changing which permutation acts first changes the paths and the resulting images. These two permutations do not commute.*

Permutation multiplication is **associative**:

$$
(\sigma\tau)\mu=\sigma(\tau\mu),
$$

because both sides send $k$ to $\sigma(\tau(\mu(k)))$. Associativity allows different bracketings while preserving the order of the factors.

The identity is

$$
\varepsilon=\begin{pmatrix}1&2&\cdots&n\\1&2&\cdots&n\end{pmatrix},
\qquad
\varepsilon\sigma=\sigma=\sigma\varepsilon.
$$

#### Constructing every element of the symmetric group of degree three

For Example 2.6, now use

$$
\alpha=\begin{pmatrix}1&2&3\\2&3&1\end{pmatrix},
\qquad
\beta=\begin{pmatrix}1&2&3\\1&3&2\end{pmatrix}.
$$

These labels apply to this example; the earlier examples use their own permutations.

![Powers of the permutations used to enumerate the symmetric group](../../diagrams/MAM2013S-Introductory%20Algebra/02_Permutations/s3-powers.svg)

*The powers give $\alpha^2$, $\alpha^3=\varepsilon$, and $\beta^2=\varepsilon$.*

![The two additional mixed products](../../diagrams/MAM2013S-Introductory%20Algebra/02_Permutations/s3-mixed-products.svg)

*The mixed products supply the two remaining transpositions.*

| Element | Images of $1,2,3$ | Cycle notation |
|---|---|---|
| $\varepsilon$ | $1,2,3$ | $\varepsilon$ |
| $\alpha$ | $2,3,1$ | $(1\,2\,3)$ |
| $\alpha^2$ | $3,1,2$ | $(1\,3\,2)$ |
| $\beta$ | $1,3,2$ | $(2\,3)$ |
| $\alpha\beta$ | $2,1,3$ | $(1\,2)$ |
| $\alpha^2\beta$ | $3,2,1$ | $(1\,3)$ |

The cycle notation is defined below. These six permutations are distinct, and $|S_3|=6$, so the list is complete.

### Inverse Permutations

#### Definitions

> **Inverse permutation**: The unique bijection $\sigma^{-1}$ that reverses $\sigma$, satisfying $\sigma\sigma^{-1}=\sigma^{-1}\sigma=\varepsilon$.

If $\sigma(k)=j$, then $\sigma^{-1}(j)=k$. To find the inverse:

1. Swap the two rows of the two-row expression.
2. Reorder whole columns until the top row is $1,2,\ldots,n$.
3. Read the inverse images from the bottom row.

Reordering columns does not change the function, because each input stays paired with its image.

For

$$
\sigma=\begin{pmatrix}1&2&3&4&5&6&7&8\\4&1&8&3&2&5&6&7\end{pmatrix},
$$

reading upward gives

$$
\sigma^{-1}=\begin{pmatrix}1&2&3&4&5&6&7&8\\2&5&4&1&6&7&8&3\end{pmatrix}.
$$

![Every input returns to itself when the inverse follows the permutation](../../diagrams/MAM2013S-Introductory%20Algebra/02_Permutations/inverse-check.svg)

*The composite $\sigma^{-1}\sigma$ fixes every input. Reading the paths in reverse also verifies $\sigma\sigma^{-1}=\varepsilon$.*

### Disjoint Permutations

#### Definitions

> **Fixed point**: An element $k$ satisfying $\sigma(k)=k$.

> **Moved point**: An element $k$ satisfying $\sigma(k)\ne k$.

> **Moved set / support**: $M_\sigma=\{k\in X_n:\sigma(k)\ne k\}$.

> **Disjoint permutations**: Permutations with no point moved by both, equivalently $M_\sigma\cap M_\tau=\varnothing$.

The identity is the only permutation fixing every point. The permutation sending $1\mapsto2\mapsto\cdots\mapsto n\mapsto1$ moves every point when $n\ge2$.

Examples 2.7 include

$$
\rho=\begin{pmatrix}1&2&3&4&5\\3&2&5&4&1\end{pmatrix},
$$

which moves $1,3,5$ and fixes $2,4$. Also,

$$
\sigma=\begin{pmatrix}1&2&3&4\\3&2&1&4\end{pmatrix},
\qquad
\tau=\begin{pmatrix}1&2&3&4\\1&4&3&2\end{pmatrix}
$$

are disjoint: their moved sets are $\{1,3\}$ and $\{2,4\}$.

#### Why disjoint permutations commute

**Lemma 2.9**: If $k$ is moved by $\sigma$, then $\sigma(k)$ is also moved by $\sigma$.

If $\sigma(k)$ were fixed, then $\sigma(\sigma(k))=\sigma(k)$. Injectivity would force $\sigma(k)=k$, contradicting that $k$ is moved.

**Theorem 2.8**: Disjoint permutations commute.

To prove it, compare $\sigma\tau$ and $\tau\sigma$ on every input:

| Position of $k$ | What the other permutation fixes | Both products send $k$ to |
|---|---|---|
| $k\in M_\sigma$ | $\tau$ fixes $k$ and $\sigma(k)$, by Lemma 2.9 and disjointness | $\sigma(k)$ |
| $k\in M_\tau$ | $\sigma$ fixes $k$ and $\tau(k)$ | $\tau(k)$ |
| $k\notin M_\sigma\cup M_\tau$ | Both fix $k$ | $k$ |

For the disjoint pair above,

$$
\sigma\tau=\tau\sigma=\begin{pmatrix}1&2&3&4\\3&4&1&2\end{pmatrix}.
$$

The converse is false. A permutation always commutes with its inverse, but they normally move the same points. For example,

$$
\sigma=\begin{pmatrix}1&2&3&4&5\\4&1&3&2&5\end{pmatrix},
\qquad
\sigma^{-1}=\begin{pmatrix}1&2&3&4&5\\2&4&3&1&5\end{pmatrix}
$$

both move $1,2,4$.

### Cycles and Cycle Decomposition

#### Definitions

> **Cycle of length $r$ / $r$-cycle**: For distinct $k_1,\ldots,k_r$, the permutation $(k_1\,k_2\,\cdots\,k_r)$ sends each listed point to the next, sends the last back to the first, and fixes all unlisted points.

> **Transposition**: A cycle of length $2$; $(a\,b)$ swaps $a,b$ and fixes everything else.

> **Disjoint-cycle decomposition**: An expression of a permutation as a product of cycles whose moved sets are pairwise disjoint.

For

$$
\sigma=\begin{pmatrix}1&2&3&4&5&6\\4&6&3&2&5&1\end{pmatrix},
$$

the points follow $1\mapsto4\mapsto2\mapsto6\mapsto1$, while $3,5$ are fixed. Thus $\sigma=(1\,4\,2\,6)$, a cycle of length $4$.

![A four-cycle and its two fixed points](../../diagrams/MAM2013S-Introductory%20Algebra/02_Permutations/single-cycle.svg)

*Only the four moved points appear in the nontrivial cycle. The fixed points remain part of the underlying set.*

![The general action of a cycle](../../diagrams/MAM2013S-Introductory%20Algebra/02_Permutations/general-cycle.svg)

*Each entry maps to the next; the amber return path maps the last entry back to the first.*

The formal action is

$$
\sigma(k_i)=k_{i+1}\ (1\le i<r),\qquad \sigma(k_r)=k_1.
$$

#### Equivalent notation and cycle inverses

Choosing a different starting point in the same traversal does not change the cycle:

$$
(k_1\,k_2\,\cdots\,k_r)
=(k_2\,\cdots\,k_r\,k_1)
=\cdots=(k_r\,k_1\,\cdots\,k_{r-1}).
$$

For example,

$$
(1\,4\,2\,6)=(6\,1\,4\,2)=(2\,6\,1\,4)=(4\,2\,6\,1).
$$

A written $1$-cycle acts as the identity on the entire underlying set. The three transpositions in $S_3$ are $(1\,2),(1\,3),(2\,3)$.

**Theorem 2.13**: Reverse the traversal to obtain the inverse:

$$
(k_1\,k_2\,\cdots\,k_r)^{-1}=(k_r\,k_{r-1}\,\cdots\,k_1).
$$

Both cycles fix unlisted points. For a listed point, the reversed cycle takes one step backward, and the original takes one step forward, so both composites fix every point. This also proves that the inverse is an $r$-cycle.

Examples 2.14:

| Two-row bottom row (top row is increasing) | Cycle | Length | Inverse cycle |
|---|---|---|---|
| $4,3,1,5,2$ in $S_5$ | $(1\,4\,5\,2\,3)$ | $5$ | $(3\,2\,5\,4\,1)$ |
| $4,7,1,6,5,2,3$ in $S_7$ | $(1\,4\,6\,2\,7\,3)$ | $6$ | $(3\,7\,2\,6\,4\,1)$ |
| $2,3,1,4,5$ in $S_5$ | $(1\,2\,3)$ | $3$ | $(3\,2\,1)$ |

In the final row, the fixed points are $4,5$. The ambient set matters: $(1\,2\,3)$ in $S_5$ also acts on $4,5$, fixing them.

#### Finding the disjoint cycles

A permutation need not be one cycle. For

$$
\sigma=\begin{pmatrix}1&2&3&4&5&6&7&8&9&10\\3&1&7&6&10&4&2&5&9&8\end{pmatrix},
$$

the decomposition is

$$
\sigma=(1\,3\,7\,2)(4\,6)(5\,10\,8),
$$

with $9$ fixed.

![The three disjoint cycles and the fixed point of the permutation](../../diagrams/MAM2013S-Introductory%20Algebra/02_Permutations/disjoint-cycles.svg)

*Each component records a separate traversal. Disjoint cycles commute, so their order in this product can be changed.*

To decompose any permutation:

1. Choose the smallest point not yet processed.
2. Repeatedly apply the permutation until you return to that starting point.
3. Write that traversal as a cycle.
4. Repeat with the smallest unprocessed point.
5. Omit fixed points from the final product if desired, but record which points are fixed.

The example in $S_9$ with bottom row $6,4,7,2,5,1,8,9,3$ gives

$$
1\mapsto6\mapsto1,\quad
2\mapsto4\mapsto2,\quad
3\mapsto7\mapsto8\mapsto9\mapsto3,
$$

while $5$ is fixed. Therefore

$$
\sigma=(1\,6)(2\,4)(3\,7\,8\,9).
$$

In Example 2.15,

$$
\sigma=\begin{pmatrix}1&2&3&4&5&6&7&8&9&10&11&12&13\\5&12&2&1&9&11&4&3&7&10&13&8&6\end{pmatrix}
$$

has traversals

$$
1\mapsto5\mapsto9\mapsto7\mapsto4\mapsto1,
\quad2\mapsto12\mapsto8\mapsto3\mapsto2,
\quad6\mapsto11\mapsto13\mapsto6.
$$

Thus $\sigma=(1\,5\,9\,7\,4)(2\,12\,8\,3)(6\,11\,13)$, with $10$ fixed.

For cycles of length at least $2$, disjointness means their lists have no common entry. For example, $(1\,3\,5)$ and $(2\,7\,6)$ are disjoint. Written $1$-cycles are an exception to this list-based test because they move no points.

#### Cycle decomposition theorem and proof

Every nonidentity permutation is a product of disjoint cycles of length at least $2$. The decomposition is unique up to the order of the factors; a single cycle may also be written from any starting point along its traversal.

**Existence, by induction on the size of the set**:

1. For $n=2$, the only nonidentity permutation is $(1\,2)$.
2. If $\sigma$ fixes $n$, apply the hypothesis to its restriction to $X_{n-1}$.
3. Otherwise let $k=\sigma^{-1}(n)$, so $k\ne n$, and set $\tau=\sigma(k\,n)$.
4. Then $\tau(n)=\sigma(k)=n$, so its restriction decomposes into disjoint cycles by induction. Also $\sigma=\tau(k\,n)$.
5. If $\tau$ fixes $k$, append the disjoint cycle $(k\,n)$.
6. Otherwise write $\tau=\mu(k\,k_1\,\cdots\,k_r)$, where $\mu$ consists of the other disjoint cycles. Then
   $$\sigma=\mu(k\,k_1\,\cdots\,k_r)(k\,n)=\mu(k\,n\,k_1\,\cdots\,k_r).$$
   The point $n$ has been inserted into one cycle, preserving disjointness.

An identity restriction simply has no nontrivial cycles to include.

**Uniqueness**: Suppose there are two decompositions. A moved point $m$ occurs in exactly one cycle of each decomposition. Rotate those cycles to start at $m$.

Their next entries must both be $\sigma(m)$, their following entries must both be $\sigma^2(m)$, and so on. They must return to $m$ at the same stage, because a cycle cannot repeat an entry before closing. Hence those two cycles agree.

Cancel that cycle and repeat on the remaining factors. Induction on the number of cycles proves that all factors agree after reordering.

#### Multiplying cycles that overlap

Cycles that overlap must still be applied right to left. They cannot in general be reordered.

For $\alpha=(2\,4\,5)$ and $\beta=(1\,2\,4)$ in $S_5$:

| Input | After $\beta$ | After $\alpha$ |
|---|---|---|
| $1$ | $2$ | $4$ |
| $2$ | $4$ | $5$ |
| $3$ | $3$ | $3$ |
| $4$ | $1$ | $1$ |
| $5$ | $5$ | $2$ |

![Multiplication of two overlapping cycles](../../diagrams/MAM2013S-Introductory%20Algebra/02_Permutations/cycle-product.svg)

*The paths give the same product whether the input permutations are written as cycles or in two-row notation.*

Therefore

$$
\alpha\beta=\begin{pmatrix}1&2&3&4&5\\4&5&3&1&2\end{pmatrix}=(1\,4)(2\,5).
$$

### Transpositions, Parity, and the Alternating Group

#### Definitions

> **Even permutation**: A permutation expressible as a product of an even number of transpositions.

> **Odd permutation**: A permutation expressible as a product of an odd number of transpositions.

> **Alternating group of degree $n$**: The set $A_n$ of all even permutations in $S_n$.

A transposition is its own inverse: $\delta^2=\varepsilon$ and $\delta^{-1}=\delta$.

**Theorem 2.17**: A cycle of length $r$ is a product of $r-1$ transpositions:

$$
(k_1\,k_2\,\cdots\,k_r)
=(k_1\,k_2)(k_2\,k_3)\cdots(k_{r-1}\,k_r).
$$

To check this, apply the rightmost swap first. Each $k_i$ with $i<r$ ultimately moves to $k_{i+1}$; $k_r$ moves successively backward through the swaps to $k_1$. Unlisted points are fixed. For $r=1$, the product has no factors and denotes the identity.

Together with cycle decomposition, this proves that every permutation is a product of transpositions. Such products are not unique:

$$
(1\,2)(2\,4)(4\,5)=(1\,2\,4\,5)=(1\,5)(1\,4)(1\,2).
$$

**Parity theorem**: Any two transposition factorisations of the same permutation have lengths of the same parity. A permutation cannot be both even and odd.

#### Computing parity

For disjoint cycles of lengths $r_1,\ldots,r_t$, a transposition factorisation uses

$$
\sum_{i=1}^t(r_i-1)
$$

factors. Its parity determines the permutation's parity.

| Cycle length | Number of transpositions | Parity of the cycle |
|---|---|---|
| Odd $r$ | Even $r-1$ | Even |
| Even $r$ | Odd $r-1$ | Odd |

To factor a general permutation into transpositions:

1. Decompose it into disjoint cycles.
2. Replace each cycle using Theorem 2.17.
3. Count the resulting transpositions.

For the permutation in $S_9$ with bottom row $5,4,6,1,7,8,2,9,3$,

$$
\sigma=(1\,5\,7\,2\,4)(3\,6\,8\,9)
$$

and

$$
\sigma=(1\,5)(5\,7)(7\,2)(2\,4)(3\,6)(6\,8)(8\,9).
$$

There are $4+3=7$ transpositions, so $\sigma$ is odd.

#### Why parity is well-defined

**Lemma 2.20**: The identity cannot be a product of an odd number of transpositions.

Use strong induction on the length $r$ of a transposition product equal to the identity. A product of length $0$ is even; a single transposition is not the identity. For a longer product, choose the last factor $(a\,b)$ and examine the preceding factor.

| Preceding factor | Rewrite of the last two factors | Effect |
|---|---|---|
| $(a\,b)$ | $(a\,b)(a\,b)=\varepsilon$ | Delete two factors |
| $(a\,c)$ | $(a\,c)(a\,b)=(a\,b)(b\,c)$ | Move the occurrence of $a$ one position left |
| $(b\,c)$ | $(b\,c)(a\,b)=(a\,c)(b\,c)$ | Move the occurrence of $a$ one position left |
| $(c\,d)$ disjoint from $(a\,b)$ | $(c\,d)(a\,b)=(a\,b)(c\,d)$ | Move the occurrence of $a$ one position left |

Here the letters in each row are distinct except where explicitly repeated. Continue sweeping the factor involving $a$ to the left.

- If two identical transpositions meet, delete them. The remaining identity factorisation has length $r-2$, which is even by the induction hypothesis, so $r$ is even.
- If the sweep reaches the first position without cancellation, only the first factor moves $a$. Every factor to its right fixes $a$, so the whole product moves $a$, contradicting that it is the identity.

Now suppose $\sigma=\gamma_r\cdots\gamma_1=\mu_s\cdots\mu_1$. Invert the second expression, noting that each transposition is self-inverse, to obtain

$$
\varepsilon=\mu_1\cdots\mu_s\gamma_r\cdots\gamma_1.
$$

The lemma makes $s+r$ even. Thus $s,r$ have the same parity, proving the parity theorem.

#### Structure and size of the alternating group

**Theorem 2.21**, for $n\ge2$:

1. $\varepsilon\in A_n$.
2. If $\sigma,\tau\in A_n$, then $\sigma\tau\in A_n$ and $\sigma^{-1}\in A_n$.
3. $|A_n|=n!/2$.

The identity is even, for example $\varepsilon=(1\,2)(1\,2)$. Products concatenate transposition expressions, so two even lengths add to an even length. Inverting reverses the transpositions without changing their number, preserving parity.

For the size, let $O_n$ be the set of odd permutations and fix $\gamma=(1\,2)$. Multiplication by $\gamma$ gives a bijection

$$
f:A_n\to O_n,\qquad f(\sigma)=\gamma\sigma.
$$

It reverses parity, and applying it twice returns the original permutation because $\gamma^2=\varepsilon$. Therefore $|A_n|=|O_n|$. Since $S_n$ is their disjoint union and has $n!$ elements, each set has $n!/2$ elements.

For example, $A_3=\{\varepsilon,(1\,2\,3),(1\,3\,2)\}$.

A **group of permutations** is a set of permutations containing the identity and closed under products and inverses. Composition supplies associativity automatically. Both $S_n$ and $A_n$ satisfy these conditions.
