---
tags:
  - introductory-algebra
---

# Groups: Subgroups, Cyclic Groups, and Isomorphisms

> [!abstract] <span style="color: #b89aff">Chapter reference</span>
> **Subject**: MAM2013S Introductory Algebra  
> **Source**: [Introductory Algebra — 2IA notes](../../Sources/MAM2013S%20-%20Introductory%20algebra/2IA%20notes.pdf), J. Sánchez-Ortega, Chapter 3, printed pages 55–91 (PDF pages 58–94)  
> **Generated**: 2026-10-03  
> **Scope**: The groups chapter only. Arithmetic and typographical slips in the source are corrected in the derivations below.  
> **Related notes**: [Integers](01_Integers.md), [Permutations](02_Permutations.md)

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Is a Group?|What Is a Group?]]
  - [[#Cayley Tables|Cayley Tables]]
  - [[#Inverses, Orders, Exponent Laws, and Cancellation|Inverses, Orders, Exponent Laws, and Cancellation]]
  - [[#A Taste of Isomorphic Groups|A Taste of Isomorphic Groups]]
  - [[#Subgroups and the Centre|Subgroups and the Centre]]
  - [[#Cyclic Groups|Cyclic Groups]]
  - [[#Properties and Generators of Cyclic Groups|Properties and Generators of Cyclic Groups]]
  - [[#Fundamental Theorem of Finite Cyclic Groups|Fundamental Theorem of Finite Cyclic Groups]]
  - [[#Homomorphisms and Isomorphisms|Homomorphisms and Isomorphisms]]

---

## Core Content

### What Is a Group?

#### Definitions

> **Binary operation on a set**: A rule $\cdot:G\times G\to G$ assigning each ordered pair a single element of the same set. This includes closure: $a\cdot b\in G$ for all $a,b\in G$.

> **Group**: A set with a binary operation that is associative, has a two-sided identity, and gives every element a two-sided inverse in the set.

> **Identity / unity**: An element $1_G$ satisfying $1_Gg=g1_G=g$ for every $g\in G$.

> **Inverse of a group element**: An element $g^{-1}$ satisfying $gg^{-1}=g^{-1}g=1_G$.

> **Abelian group**: A group whose operation is also commutative: $gh=hg$ for every $g,h$.

> **Order of a finite group**: The number $|G|$ of its elements.

The notation $(G,\cdot)$ specifies both a set and its operation. A set may form a group under one operation and fail to form one under another.

| Requirement | Formal statement | What to check |
|---|---|---|
| Closure | $ab\in G$ | The operation stays inside the proposed set |
| Associativity | $a(bc)=(ab)c$ | Bracketing does not affect the result |
| Identity | $1_Ga=a1_G=a$ | One element acts as an identity on both sides |
| Inverses | $aa^{-1}=a^{-1}a=1_G$ | Every inverse belongs to the proposed set |
| Optional commutativity | $ab=ba$ | This additional condition makes the group abelian |

Identity and inverses are unique. If $e,f$ are identities, then $e=ef=f$. If $b,c$ are both inverses of $a$, then

$$
b=b(ac)=(ba)c=c.
$$

Unless the operation needs emphasis, write $ab$ instead of $a\cdot b$. The symbol $1_G$ names an abstract identity; it need not be the ordinary number $1$.

| Concept | Multiplicative notation | Additive notation |
|---|---|---|
| Operation | $gh$ | $g+h$ |
| Identity | $1$ | $0$ |
| Inverse | $g^{-1}$ | $-g$ |
| Repeated operation | $g^n$ | $ng$ |

#### Standard examples

The following sets form groups under the stated operations. Here $i$ is the complex number satisfying $i^2=-1$.

| Set | Operation | Identity | Inverse of an element | Abelian? |
|---|---|---|---|---|
| $\{1\}$ | Multiplication | $1$ | $1$ | Yes |
| $\{1,-1\}$ | Multiplication | $1$ | Each element is self-inverse | Yes |
| $\{1,-1,i,-i\}$ | Multiplication | $1$ | $i^{-1}=-i$, $(-i)^{-1}=i$ | Yes |
| $\mathbb Q\setminus\{0\}$, $\mathbb R\setminus\{0\}$, $\mathbb C\setminus\{0\}$ | Multiplication | $1$ | $a^{-1}=1/a$ | Yes |
| $\mathbb Z,\mathbb Q,\mathbb R,\mathbb C$ | Addition | $0$ | $-a$ | Yes |
| $\mathbb Z_n$, $n\ge2$ | Modular addition | $\overline0$ | $-\overline a=\overline{-a}$ | Yes |
| $S_n$ | Composition | $\varepsilon$ | Inverse permutation | For $n\ge3$, no |

When referring to $\mathbb Z_n,\mathbb Z,\mathbb Q,\mathbb R,\mathbb C$ as groups without another operation specified, the convention here is addition. Their nonzero multiplicative groups are written explicitly or with a superscript star.

For example, $\mathbb Z$ is an additive group but is not a multiplicative group: $2$ has no multiplicative inverse in $\mathbb Z$. Similarly, modular multiplication on all of $\mathbb Z_n$ fails to give a group because $\overline0$ has no multiplicative inverse.

> **Unit**: An element of a coefficient system with a multiplicative inverse in that same system.

> **Unit group modulo $n$**: $\mathbb Z_n^*=\{\overline a:\gcd(a,n)=1\}$, with modular multiplication. Its identity is $\overline1$, and every listed class has a modular multiplicative inverse.

The integer unit group is $\mathbb Z^*=\{1,-1\}$ under multiplication. Unlike $\mathbb Q^*,\mathbb R^*,\mathbb C^*$, it does not consist of all nonzero elements of its coefficient system.

#### Matrix groups

> **General linear group**: $\mathrm{GL}_n(R)$, the group of invertible $n\times n$ matrices with entries in $R$, under matrix multiplication.

Write $M_n(R)$ for all $n\times n$ matrices over $R$. For the coefficient systems used here, a matrix is invertible exactly when its determinant is a unit:

| Coefficient system | Invertible matrices |
|---|---|
| $R=\mathbb Q,\mathbb R,\mathbb C$ | $\mathrm{GL}_n(R)=\{A\in M_n(R):\det A\ne0\}$ |
| $R=\mathbb Z$ | $\mathrm{GL}_n(\mathbb Z)=\{A\in M_n(\mathbb Z):\det A=\pm1\}$ |
| $R=\mathbb Z_m$ | $\det A=\overline a$ with $\gcd(a,m)=1$ |

The identity is the identity matrix $I_n$. Associativity comes from matrix multiplication. Products of invertible matrices stay invertible because $(AB)^{-1}=B^{-1}A^{-1}$.

For integers, nonzero determinant alone is insufficient: the matrix inverse must also have integer entries. For modular coefficients, the determinant must satisfy the modular inverse criterion.

#### Direct products

> **Direct product of groups**: The Cartesian product $G_1\times\cdots\times G_r$ with the operation performed separately in each component.

The operation is

$$
(g_1,\ldots,g_r)(h_1,\ldots,h_r)=(g_1h_1,\ldots,g_rh_r).
$$

Associativity holds component by component. The identity and inverse are

$$
(1_{G_1},\ldots,1_{G_r}),
\qquad
(g_1,\ldots,g_r)^{-1}=(g_1^{-1},\ldots,g_r^{-1}).
$$

For the additive product $\mathbb R\times\mathbb Z_2$,

$$
(a,\overline c)+(b,\overline d)=(a+b,\overline{c+d}),
$$

with identity $(0,\overline0)$ and inverse $(-a,\overline{-c})$. In particular,

$$
(2,\overline1)+(-1,\overline1)=(1,\overline0).
$$

### Cayley Tables

#### Definitions

> **Cayley table / group table**: For a finite group, a table with the group elements as row and column labels, and the product $ab$ in row $a$, column $b$.

> **Generators of a group**: Elements from which every group element can be obtained using products and inverses.

> **Relations among generators**: Equations satisfied by the generators, used to simplify products.

A table completely specifies the operation. Read the row factor first and the column factor second; for permutations, the column factor therefore acts first.

#### The symmetric group of degree three

In this section, use $\sigma=(1\,2\,3)$ and $\tau=(1\,2)$. Then

$$
\sigma^2=(1\,3\,2),\quad \sigma^3=\varepsilon=\tau^2,
\quad \sigma\tau\sigma=\tau,
\quad \tau\sigma=(2\,3),\quad\tau\sigma^2=(1\,3).
$$

Thus $S_3=\{\varepsilon,\sigma,\sigma^2,\tau,\tau\sigma,\tau\sigma^2\}$ and $\sigma,\tau$ generate it.

Multiplying $\sigma\tau\sigma=\tau$ on the right by $\sigma^2$ gives $\sigma\tau=\tau\sigma^2$. Multiplying on the left gives $\sigma^2\tau=\tau\sigma$.

For example,

$$
\begin{aligned}
(\tau\sigma)\tau&=(\sigma^2\tau)\tau=\sigma^2,\\
\sigma^2(\tau\sigma)&=(\sigma^2\tau)\sigma=\tau\sigma^2,\\
(\tau\sigma^2)(\tau\sigma^2)&=\tau(\sigma^2\tau)\sigma^2=\tau(\tau\sigma)\sigma^2=\varepsilon.
\end{aligned}
$$

The complete table is:

| $S_3$ | $\varepsilon$ | $\sigma$ | $\sigma^2$ | $\tau$ | $\tau\sigma$ | $\tau\sigma^2$ |
|---|---|---|---|---|---|---|
| $\varepsilon$ | $\varepsilon$ | $\sigma$ | $\sigma^2$ | $\tau$ | $\tau\sigma$ | $\tau\sigma^2$ |
| $\sigma$ | $\sigma$ | $\sigma^2$ | $\varepsilon$ | $\tau\sigma^2$ | $\tau$ | $\tau\sigma$ |
| $\sigma^2$ | $\sigma^2$ | $\varepsilon$ | $\sigma$ | $\tau\sigma$ | $\tau\sigma^2$ | $\tau$ |
| $\tau$ | $\tau$ | $\tau\sigma$ | $\tau\sigma^2$ | $\varepsilon$ | $\sigma$ | $\sigma^2$ |
| $\tau\sigma$ | $\tau\sigma$ | $\tau\sigma^2$ | $\tau$ | $\sigma^2$ | $\varepsilon$ | $\sigma$ |
| $\tau\sigma^2$ | $\tau\sigma^2$ | $\tau$ | $\tau\sigma$ | $\sigma$ | $\sigma^2$ | $\varepsilon$ |

#### The product of two additive groups of order two

For $\mathbb Z_2\times\mathbb Z_2$, abbreviate

$$
e=(\overline0,\overline0),\quad a=(\overline0,\overline1),\quad
b=(\overline1,\overline0),\quad c=(\overline1,\overline1).
$$

Add coordinates modulo $2$:

| $+$ | $e$ | $a$ | $b$ | $c$ |
|---|---|---|---|---|
| $e$ | $e$ | $a$ | $b$ | $c$ |
| $a$ | $a$ | $e$ | $c$ | $b$ |
| $b$ | $b$ | $c$ | $e$ | $a$ |
| $c$ | $c$ | $b$ | $a$ | $e$ |

For instance, $a+b=c$ and $a+a=e$. Every element is self-inverse.

#### Information visible in a group table

| Feature | How to recognise it |
|---|---|
| Abelian group | The table is symmetric across its main diagonal |
| Identity | Its row and column reproduce the column and row labels |
| Inverse of $a$ | Find $b$ for which both entries $ab$ and $ba$ are the identity |
| Cancellation | Every element occurs exactly once in each row and column |

The last property is proved below. The table of $S_3$ is not symmetric, while that of $\mathbb Z_2\times\mathbb Z_2$ is symmetric.

In $S_3$, $\sigma$ and $\sigma^2$ are inverses of one another. The identity and all three transpositions are self-inverse.

### Inverses, Orders, Exponent Laws, and Cancellation

#### Definitions

> **Integer power**: $g^0=1$, $g^n=gg^{n-1}$ for $n\ge1$, and $g^{-n}=(g^{-1})^n=(g^n)^{-1}$ for $n\ge1$.

> **Order of an element**: The least positive integer $n$ with $g^n=1$, denoted $o(g)$. If no positive power is the identity, the order is infinite.

The order of an element and the order of its group are different notions. In an additive group, $o(g)$ is the smallest positive $n$ satisfying $ng=0$.

The identity has order $1$. A nonidentity self-inverse element has order $2$.

For $\mathbb Z_4$, $\overline2+\overline2=\overline0$, so $o(\overline2)=2$. The successive positive multiples of $\overline3$ are

$$
\overline3,\quad\overline2,\quad\overline1,\quad\overline0,
$$

so $o(\overline3)=4$. Also $o((1\,2))=2$ in $S_3$, and $o((\overline1,\overline0))=2$ in $\mathbb Z_2\times\mathbb Z_2$.

If $g^\ell=1$ and $o(g)=n$, then $n\mid\ell$. Divide $\ell=qn+r$ with $0\le r<n$; the exponent laws give $g^r=1$, forcing $r=0$ by minimality. A fuller version is proved in the cyclic-group section.

#### Inverse laws

**Theorem 3.8**:

$$
1^{-1}=1,\qquad(g^{-1})^{-1}=g,\qquad(gh)^{-1}=h^{-1}g^{-1},
$$

and more generally

$$
(g_1g_2\cdots g_r)^{-1}=g_r^{-1}\cdots g_2^{-1}g_1^{-1}.
$$

The first two identities follow from the definition and uniqueness of inverses. To verify the product rule,

$$
(gh)(h^{-1}g^{-1})=g(hh^{-1})g^{-1}=1,
\quad
(h^{-1}g^{-1})(gh)=h^{-1}(g^{-1}g)h=1.
$$

Induction on the number of factors then gives the general reversal rule.

> [!important] <span style="color: #ffc778">Reverse the order when taking an inverse</span>
> The inverse of $gh$ is $h^{-1}g^{-1}$. Commutativity is not part of the group axioms, so factor order must be preserved unless commutation has been established.

#### Exponent laws, including negative exponents

| Law | Conditions |
|---|---|
| $g^nh=hg^n$ | $gh=hg$, $n\in\mathbb Z$ |
| $(gh)^n=g^nh^n$ | $gh=hg$, $n\in\mathbb Z$ |
| $g^ng^m=g^{n+m}$ | Any $g$, $n,m\in\mathbb Z$ |
| $(g^n)^m=g^{nm}$ | Any $g$, $n,m\in\mathbb Z$ |

Here is how each extension to integer exponents is justified.

**Commuting with a power**: For positive $n$, induct using

$$
g^nh=g(g^{n-1}h)=g(hg^{n-1})=hgg^{n-1}=hg^n.
$$

The zero case uses $g^0=1$. If $gh=hg$, multiplying on the left and right by $g^{-1}$ gives $g^{-1}h=hg^{-1}$. Apply the positive case to $g^{-1}$ to cover negative powers.

**Power of a commuting product**: The zero case is immediate. For positive $n$, the preceding result and induction give

$$
(gh)^n=(gh)(g^{n-1}h^{n-1})=g^nh^n.
$$

For negative $n=-t$, the commuting elements $g^{-1},h^{-1}$ satisfy

$$
(gh)^{-t}=(h^{-1}g^{-1})^t=(g^{-1})^t(h^{-1})^t=g^{-t}h^{-t}.
$$

**Adding exponents of one element**: For nonnegative exponents, fix $m$ and induct on $n$:

$$
g^ng^m=g(g^{n-1}g^m)=gg^{n+m-1}=g^{n+m}.
$$

For negative exponents, write them as positive powers of $g^{-1}$ and apply the same argument. For mixed signs, set $m=-t$ with $t>0$:

| Relation of $n\ge0$ to $t$ | Computation |
|---|---|
| $n=t$ | $g^ng^{-t}=1=g^0$ |
| $n>t$ | $g^n=g^{n-t}g^t$, so multiplication by $g^{-t}$ leaves $g^{n-t}$ |
| $n<t$ | $g^{-t}=g^{-n}g^{-(t-n)}$, so multiplication by $g^n$ leaves $g^{n-t}$ |

Powers of the same element commute: $g$ commutes with its inverse, and repeated use of the first law extends this to their integer powers. Thus the mixed-sign result also holds when the negative exponent is first.

**Power of a power**: For fixed integer $n$ and positive $m$, induct using

$$
(g^n)^m=g^n(g^n)^{m-1}=g^ng^{n(m-1)}=g^{nm}.
$$

For $m=0$, both sides are the identity. For $m=-t<0$, use $(g^n)^{-1}=g^{-n}$ and the positive case:

$$
(g^n)^{-t}=(g^{-n})^t=g^{-nt}.
$$

The laws involving two different bases require commutation; those involving only powers of one base do not.

#### Cancellation and solving group equations

**Theorem 3.9**:

| Statement | Method |
|---|---|
| $gh=gf\Rightarrow h=f$ | Multiply on the left by $g^{-1}$ |
| $hg=fg\Rightarrow h=f$ | Multiply on the right by $g^{-1}$ |
| $gx=h$ has unique solution $x=g^{-1}h$ | Remove the left factor on the left |
| $xg=h$ has unique solution $x=hg^{-1}$ | Remove the right factor on the right |

The displayed candidates solve the equations by associativity and the inverse laws. Cancellation proves uniqueness.

**Corollary 3.10**: Every row and column in the Cayley table of a finite group contains every group element exactly once.

For a fixed row factor $g$, each desired entry $h$ occurs because $gx=h$ has a solution, and occurs only once because that solution is unique. For columns, use $xg=h$ instead.

In additive notation the exponent laws become

$$
(n+m)g=ng+mg,\qquad m(ng)=(mn)g,
$$

and for commuting $g,h$,

$$
n(g+h)=ng+nh.
$$

### A Taste of Isomorphic Groups

#### Definitions

> **Isomorphic finite groups, in table form**: Groups whose Cayley tables become identical after a consistent bijective relabelling of the elements. The full map-based definition appears below.

> **Cyclic group**: A group whose elements are all integer powers of one element; in additive notation, all integer multiples of one element.

> **Klein group**: The group $K_4=\{1,a,b,c\}$ with $a^2=b^2=c^2=1$ and the product of two distinct nonidentity elements equal to the third.

The multiplicative group $\mathbb Z^*=\{1,-1\}$ and the additive group $\mathbb Z_2$ have the same table structure under the relabelling $1\leftrightarrow\overline0$, $-1\leftrightarrow\overline1$:

| $\times$ | $1$ | $-1$ |
|---|---|---|
| $1$ | $1$ | $-1$ |
| $-1$ | $-1$ | $1$ |

| $+$ | $\overline0$ | $\overline1$ |
|---|---|---|
| $\overline0$ | $\overline0$ | $\overline1$ |
| $\overline1$ | $\overline1$ | $\overline0$ |

The elements and operation symbols differ, but the multiplication pattern is the same.

#### Groups with at most three elements

- For order $1$, the group is $\{1\}$.
- For order $2$, write $G=\{1,g\}$. The possibility $g^2=g$ forces $g=1$ by cancellation, so $g^2=1$.
- For order $3$, write $G=\{1,g,h\}$. Cancellation rules out $gh=g$ and $gh=h$, so $gh=1$; similarly $hg=1$. The row and column uniqueness property then forces $g^2=h$ and $h^2=g$, giving $g^3=1$.

Their nontrivial tables are therefore:

| $C_2$ | $1$ | $g$ |
|---|---|---|
| $1$ | $1$ | $g$ |
| $g$ | $g$ | $1$ |

| $C_3$ | $1$ | $g$ | $g^2$ |
|---|---|---|---|
| $1$ | $1$ | $g$ | $g^2$ |
| $g$ | $g$ | $g^2$ | $1$ |
| $g^2$ | $g^2$ | $1$ | $g$ |

Thus every group of order $1,2,3$ is cyclic, and there is only one group of each such order up to isomorphism. In particular, $C_2\cong\mathbb Z_2$ and $C_3\cong\mathbb Z_3$.

#### The two groups of order four

Up to isomorphism, the groups of order $4$ are $C_4$ and $K_4$. Their structures differ:

| Feature | $C_4$ | $K_4$ |
|---|---|---|
| Elements | $1,a,a^2,a^3$, with $o(a)=4$ | $1,a,b,c$ |
| Nonidentity element orders | $4,2,4$ | $2,2,2$ |
| Cyclic? | Yes | No |
| Additive model | $\mathbb Z_4$ | $\mathbb Z_2\times\mathbb Z_2$ |

The table of $K_4$ is

| $\times$ | $1$ | $a$ | $b$ | $c$ |
|---|---|---|---|---|
| $1$ | $1$ | $a$ | $b$ | $c$ |
| $a$ | $a$ | $1$ | $c$ | $b$ |
| $b$ | $b$ | $c$ | $1$ | $a$ |
| $c$ | $c$ | $b$ | $a$ | $1$ |

No element of $K_4$ generates four elements: the identity generates only itself, and each nonidentity element generates a two-element subgroup. The same reasoning proves that $\mathbb Z_2\times\mathbb Z_2$ is noncyclic.

The identity has order $1$, including in the Klein group. Statements about order $2$ here refer to the nonidentity elements.

### Subgroups and the Centre

#### Definitions

> **Subgroup**: A subset $H\subseteq G$ that is itself a group using the operation inherited from $G$. Write $H\le G$.

> **Subgroup lattice diagram**: A diagram recording subgroup containment, with smaller subgroups below larger ones. Lines between adjacent levels record inclusions, and upward paths give further inclusions.

> **Centre of a group**: $Z(G)=\{z\in G:zg=gz\text{ for every }g\in G\}$.

For additive groups, $\mathbb Z\le\mathbb Q\le\mathbb R\le\mathbb C$. Also $A_n\le S_n$, since even permutations contain the identity and are closed under products and inverses.

#### Subgroup test

A subset $H\subseteq G$ is a subgroup exactly when:

1. $1_G\in H$.
2. For every $h,h_1\in H$, $hh_1\in H$.
3. For every $h\in H$, $h^{-1}\in H$.

![Products, inverses, and the identity stay within the subgroup](../../diagrams/MAM2013S-Introductory%20Algebra/03_Groups/subgroup-test.svg)

*The subgroup boundary contains the identity, both chosen elements, their product, and the illustrated inverse. Associativity is inherited from the surrounding group.*

If the three conditions hold, they supply closure, identity, and inverses, while associativity comes from $G$.

Conversely, if $H$ is a subgroup with identity $e$, then $e^2=e=e1_G$. Cancellation in $G$ gives $e=1_G$. Closure holds because $H$ is a group. If $h'$ is the inverse of $h$ in $H$, then $hh'=1_G=hh^{-1}$, and cancellation gives $h'=h^{-1}$.

Thus a subgroup has the same identity as its parent group, and its elements have the same inverses as in the parent group.

An equivalent combined test is

$$
1_G\in H,\qquad h,h_1\in H\Rightarrow hh_1^{-1}\in H.
$$

Taking $h=1_G$ supplies inverses; then using an inverse as the second input supplies products. Another equivalent formulation is that $H$ is nonempty and closed under $hh_1^{-1}$: taking equal inputs first supplies the identity.

For additive groups, this combined condition becomes closure under differences: $h-h_1\in H$.

#### Integer-multiple subgroups

For each $n\ge0$, the set

$$
n\mathbb Z=\{nk:k\in\mathbb Z\}
$$

is a subgroup of $(\mathbb Z,+)$:

- $0=n\cdot0$ belongs to the set.
- $nk+nm=n(k+m)$ belongs to the set.
- $-(nk)=n(-k)$ belongs to the set.

The cyclic-group proof below shows that these are all the subgroups of $\mathbb Z$. The case $n=0$ gives $\{0\}$.

#### Finite subgroup test

A finite, nonempty subset $H$ of a group is a subgroup if and only if it is closed under the group operation.

For the nontrivial direction, choose $h\in H$. Closure puts all positive powers of $h$ in $H$. Finiteness forces a repetition $h^i=h^j$ with $i<j$. Cancellation gives $h^{j-i}=1_G$, so $1_G\in H$.

The inverse of $h$ is $h^{j-i-1}$; it is in $H$ by closure, or is the already-established identity if the exponent is zero. Apply this reasoning to each element, then use the ordinary subgroup test.

Finiteness and nonemptiness are required. For instance, positive integers are closed under addition but are not an additive subgroup of $\mathbb Z$.

Example 3.15 uses $H=\{\overline2,\overline4,\overline6\}=\{\overline0,\overline2,\overline4\}\subseteq\mathbb Z_6$. It is closed: sums of even residues are even residues. In particular,

$$
\overline2+\overline2=\overline4,\quad
\overline2+\overline4=\overline0,\quad
\overline4+\overline4=\overline2.
$$

The finite subgroup test therefore applies.

#### Subgroups of the cyclic and Klein groups of order four

For $C_4=\{1,a,a^2,a^3\}$, the subgroups are exactly

$$
\{1\},\qquad\{1,a^2\},\qquad C_4.
$$

The two-element set is closed because $(a^2)^2=a^4=1$. Any subgroup containing $a$ contains all its powers. A subgroup containing $a^3$ also contains $(a^3)^2=a^2$ and $(a^3)^3=a$, so it must be the whole group.

For $K_4$, the complete list is

$$
\{1\},\qquad\{1,a\},\qquad\{1,b\},\qquad\{1,c\},\qquad K_4.
$$

Each two-element set is closed. If a subgroup contains two distinct nonidentity elements, it also contains their product, the third, so it is $K_4$.

![The subgroup lattices of the two groups of order four](../../diagrams/MAM2013S-Introductory%20Algebra/03_Groups/order-four-lattices.svg)

*The cyclic group has one intermediate subgroup; the Klein group has three. Each upward path records subgroup containment.*

#### The centre is a subgroup

A group is abelian exactly when $Z(G)=G$.

**Proposition 3.19**: $Z(G)\le G$.

1. The identity commutes with every element, so $1_G\in Z(G)$.
2. If $z,z'\in Z(G)$ and $g\in G$, then
   $$g(zz')=(gz)z'=(zg)z'=z(gz')=z(z'g)=(zz')g.$$
   Thus $zz'\in Z(G)$.
3. From $zg=gz$, multiply on the left and right by $z^{-1}$ to obtain $gz^{-1}=z^{-1}g$. Thus $z^{-1}\in Z(G)$.

The subgroup test proves the result.

Examples 3.20:

- $Z(\mathbb Z_4)=\mathbb Z_4$ and $Z(K_4)=K_4$, since both groups are abelian.
- $Z(S_3)=\{\varepsilon\}$.

For the second claim, use the earlier $S_3$ table. Neither $\sigma$ nor $\sigma^2$ commutes with $\tau$, and $\tau$ does not commute with $\sigma$. The remaining two transpositions also fail to commute:

$$
(\tau\sigma)(\tau\sigma^2)=\sigma\ne\sigma^2=(\tau\sigma^2)(\tau\sigma).
$$

Hence every nonidentity element fails the defining condition of the centre.

### Cyclic Groups

#### Definitions

> **Cyclic subgroup generated by $g$**: $\langle g\rangle=\{g^k:k\in\mathbb Z\}$, the subgroup of all integer powers of $g$.

> **Generator of a cyclic group**: An element $g$ satisfying $G=\langle g\rangle$.

> **Finite cyclic group of order $n$**: A group $C_n=\langle g\rangle=\{1,g,\ldots,g^{n-1}\}$ where $o(g)=n$.

The exponent laws prove that $\langle g\rangle$ is a subgroup: it contains $g^0=1$, products add exponents, and inverses negate exponents.

It is the smallest subgroup containing $g$: any subgroup containing $g$ must contain its inverse, every positive power, and every negative power.

For additive notation,

$$
\langle g\rangle=\{kg:k\in\mathbb Z\}=\mathbb Zg.
$$

In $C_n$, every exponent is reduced modulo $n$. If $k=qn+r$ with $0\le r<n$, then

$$
g^k=(g^n)^qg^r=g^r.
$$

Consequently, the entire Cayley table is given by

$$
g^ig^j=g^{(i+j)\bmod n}\qquad(0\le i,j<n).
$$

| Row / column | $1$ | $g$ | $g^2$ | $\cdots$ | $g^{n-1}$ |
|---|---|---|---|---|---|
| $1$ | $1$ | $g$ | $g^2$ | $\cdots$ | $g^{n-1}$ |
| $g$ | $g$ | $g^2$ | $g^{3\bmod n}$ | $\cdots$ | $1$ |
| $g^2$ | $g^2$ | $g^{3\bmod n}$ | $g^{4\bmod n}$ | $\cdots$ | $g$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ | $\vdots$ |
| $g^{n-1}$ | $g^{n-1}$ | $1$ | $g$ | $\cdots$ | $g^{(n-2)\bmod n}$ |

This pattern is for $n\ge3$; the order-one and order-two tables were given above.

#### Examples and nonexamples

- For $\sigma=(1\,2\,3)$, $\langle\sigma\rangle=\{\varepsilon,\sigma,\sigma^2\}$.
- In $(\mathbb Z,+)$, $\langle2\rangle=2\mathbb Z$, the even integers.
- The infinite group $(\mathbb Z,+)$ is cyclic, with generators $1,-1$ only. If $|n|\ge2$, its multiples omit $1$; $n=0$ generates only $0$.
- The group $\mathbb Z_n$ is cyclic of order $n$, generated by $\overline1$, since $\overline k=k\overline1$.

The unit group $\mathbb Z_9^*=\{\overline1,\overline2,\overline4,\overline5,\overline7,\overline8\}$ is cyclic under multiplication:

| Exponent $k$ | $\overline2^k$ in $\mathbb Z_9$ |
|---|---|
| $0$ | $\overline1$ |
| $1$ | $\overline2$ |
| $2$ | $\overline4$ |
| $3$ | $\overline8$ |
| $4$ | $\overline7$ |
| $5$ | $\overline5$ |
| $6$ | $\overline1$ |

Thus $\mathbb Z_9^*=\langle\overline2\rangle$, with order $6$.

In contrast, $\mathbb Z_8^*=\{\overline1,\overline3,\overline5,\overline7\}$ is not cyclic:

$$
\langle\overline1\rangle=\{\overline1\},\quad
\langle\overline3\rangle=\{\overline1,\overline3\},\quad
\langle\overline5\rangle=\{\overline1,\overline5\},\quad
\langle\overline7\rangle=\{\overline1,\overline7\}.
$$

The squares of $\overline3,\overline5,\overline7$ are all $\overline1$. Their pairwise products give the third nonidentity element, so this group has the Klein-group table.

#### Finite and infinite cyclic subgroups

**Theorem 3.24**:

| Property | Finite case, $o(g)=n$ | Infinite case |
|---|---|---|
| When is a power the identity? | $g^k=1\Longleftrightarrow n\mid k$ | $g^k=1\Longleftrightarrow k=0$ |
| When are two powers equal? | $g^k=g^m\Longleftrightarrow k\equiv m\pmod n$ | $g^k=g^m\Longleftrightarrow k=m$ |
| Distinct elements | $1,g,\ldots,g^{n-1}$ | All powers $\ldots,g^{-2},g^{-1},1,g,g^2,\ldots$ |
| Number of elements | $n$ | Infinite |

**Proof in the finite case**:

1. Finitely many elements force two positive powers to coincide, say $g^k=g^m$ with $k<m$. Then $g^{m-k}=1$.
2. Well-ordering gives the smallest positive exponent $n$ with $g^n=1$.
3. If $n\mid k$, then $g^k=(g^n)^q=1$.
4. Conversely, divide $k=qn+r$ with $0\le r<n$. If $g^k=1$, then $g^r=1$, and minimality forces $r=0$.
5. Apply this equivalence to $g^kg^{-m}=g^{k-m}$ to obtain the equality-of-powers criterion.
6. Every power reduces to one of $1,g,\ldots,g^{n-1}$; the equality criterion makes these representatives distinct.

**Proof in the infinite case**: A relation $g^k=1$ with $k\ne0$ would also give a positive identity power and reduce every exponent modulo that positive integer, making the subgroup finite. Hence only $k=0$ gives the identity. Apply this to the difference of two exponents to prove that all powers are distinct.

**Corollary 3.25**:

$$
o(g)=|\langle g\rangle|.
$$

For example, the subgroups generated by $\overline3,\overline5,\overline7$ in $\mathbb Z_8^*$ each have two elements, agreeing with the order of their generator.

### Properties and Generators of Cyclic Groups

#### Definitions

> **Generator criterion for a finite cyclic group**: If $G=\langle g\rangle$ has order $n$, then $g^k$ generates $G$ exactly when $\gcd(k,n)=1$.

**Theorem 3.27**: Every cyclic group is abelian, every subgroup of a cyclic group is cyclic, and the finite generator criterion above holds.

#### Why a cyclic group is abelian

For $x=g^k$, $y=g^m$,

$$
xy=g^{k+m}=g^{m+k}=yx.
$$

The converse fails: the Klein group and $\mathbb Z_8^*$ are abelian but not cyclic.

#### Why every subgroup is cyclic

Let $H\le\langle g\rangle$. If $H=\{1\}$, then $H=\langle1\rangle$.

Otherwise, choose a nonidentity power $g^k\in H$. Inverting if needed gives a positive exponent whose power belongs to $H$. Let $m$ be the smallest positive integer with $g^m\in H$.

Closure gives $\langle g^m\rangle\subseteq H$. For the reverse containment, take $g^s\in H$ and divide $s=qm+r$ with $0\le r<m$. Then

$$
g^r=(g^m)^{-q}g^s\in H.
$$

If $r>0$, this contradicts minimality of $m$. Thus $r=0$ and $g^s=(g^m)^q$. Hence $H=\langle g^m\rangle$.

For $(\mathbb Z,+)$ this proves that every subgroup is $m\mathbb Z$ for some $m\ge0$, including the trivial subgroup $0\mathbb Z$.

#### Which powers generate the whole finite group?

Suppose first that $G=\langle g^k\rangle$ and $o(g)=n$. Then $g=(g^k)^m$ for some integer $m$, so

$$
n\mid(1-km)\quad\Rightarrow\quad1=km+qn
$$

for an integer $q$. Bézout's criterion gives $\gcd(k,n)=1$.

Conversely, if $\gcd(k,n)=1$, choose $xk+yn=1$. Then

$$
g=g^{xk+yn}=(g^k)^x(g^n)^y=(g^k)^x.
$$

Thus the subgroup generated by $g^k$ contains $g$, and therefore equals $G$.

In additive notation, $\overline k$ generates $\mathbb Z_n$ exactly when $\gcd(k,n)=1$. In $\mathbb Z_{12}$ the generators are

$$
\overline1,\quad\overline5,\quad\overline7,\quad\overline{11}.
$$

For example, the successive multiples of $\overline5$ are

$$
\overline0,\overline5,\overline{10},\overline3,\overline8,\overline1,
\overline6,\overline{11},\overline4,\overline9,\overline2,\overline7,
$$

which include every class. In particular, $\overline1=5\overline5$, $\overline2=10\overline5$, $\overline3=3\overline5$, and $\overline4=8\overline5$.

For an infinite cyclic group $\langle g\rangle$, the only generators are $g,g^{-1}$. If $g^k$ generates it, then $g=(g^k)^m$ implies $km=1$ because distinct integer exponents give distinct powers; hence $k=\pm1$.

### Fundamental Theorem of Finite Cyclic Groups

#### Definitions

> **Fundamental theorem of finite cyclic groups**: If $G=\langle g\rangle$ has order $n$, its subgroups correspond exactly to the positive divisors of $n$. For each divisor $k$ there is precisely one subgroup of order $k$, namely $\langle g^{n/k}\rangle$.

The theorem can be stated as:

1. Every subgroup is $\langle g^d\rangle$ for some positive divisor $d\mid n$.
2. Every subgroup order divides $n$.
3. If $k\mid n$, the unique subgroup of order $k$ is $\langle g^{n/k}\rangle$.

#### Order of a divisor power

**Lemma 3.29**: If $o(g)=n$ and $d$ is a positive divisor of $n$, then

$$
o(g^d)=\frac nd.
$$

Let $k=n/d$. Then $(g^d)^k=g^n=1$. If $(g^d)^r=1$ for a positive $r$, the power criterion gives $n\mid dr$. Write $dr=qn=qdk$ and cancel the positive integer $d$ to get $r=qk\ge k$. Thus $k$ is the least positive identity exponent.

#### Proof of the fundamental theorem

From the preceding cyclic-subgroup result, write a nontrivial subgroup as $H=\langle g^m\rangle$. Let $d=\gcd(m,n)$.

- Since $d\mid m$, $g^m=(g^d)^q$ for some $q$, giving $\langle g^m\rangle\subseteq\langle g^d\rangle$.
- Bézout gives $d=xm+yn$, so
  $$g^d=(g^m)^x(g^n)^y=(g^m)^x\in\langle g^m\rangle.$$
  This proves the reverse containment.

Therefore $H=\langle g^d\rangle$ with $d\mid n$. The trivial subgroup is $\langle g^n\rangle$.

By Lemma 3.29, $|H|=n/d$, which divides $n$. If a subgroup has order $k$, this equation forces $d=n/k$, so there is only one possible subgroup, $\langle g^{n/k}\rangle$.

**Corollary 3.30**: For any positive integer $m$, set $d=\gcd(m,n)$. Then

$$
\langle g^m\rangle=\langle g^d\rangle,
\qquad o(g^m)=\frac{n}{\gcd(m,n)}.
$$

The same formula holds for any integer exponent by reducing it modulo $n$. In additive notation,

$$
o(\overline m\text{ in }\mathbb Z_n)=\frac{n}{\gcd(m,n)}.
$$

For Example 3.31, $\gcd(18,30)=6$, so

$$
o(\overline{18})=5,\qquad
\langle\overline{18}\rangle=\langle\overline6\rangle
=\{\overline0,\overline6,\overline{12},\overline{18},\overline{24}\}.
$$

#### Containment and lattice diagrams

For positive divisors $k,m$ of $n$,

$$
\langle g^m\rangle\subseteq\langle g^k\rangle\quad\Longleftrightarrow\quad k\mid m.
$$

If the inclusion holds, $g^m=g^{kt}$ for an integer $t$, so $n\mid(m-kt)$. Since $k\mid n$, it follows that $k\mid m$. Conversely, $m=ku$ gives $g^m=(g^k)^u$, proving inclusion.

The divisor condition matters: for arbitrary exponents, first replace them by their gcds with $n$. Equivalently, containment holds when $\gcd(k,n)\mid\gcd(m,n)$.

#### All subgroups of the cyclic group of order twelve

The divisors of $12$ are $1,2,3,4,6,12$. The subgroup of order $k$ is generated by $g^{12/k}$:

| Subgroup order | Subgroup | Elements |
|---|---|---|
| $1$ | $\langle g^{12}\rangle$ | $\{1\}$ |
| $2$ | $\langle g^6\rangle$ | $\{1,g^6\}$ |
| $3$ | $\langle g^4\rangle$ | $\{1,g^4,g^8\}$ |
| $4$ | $\langle g^3\rangle$ | $\{1,g^3,g^6,g^9\}$ |
| $6$ | $\langle g^2\rangle$ | $\{1,g^2,g^4,g^6,g^8,g^{10}\}$ |
| $12$ | $\langle g\rangle$ | $C_{12}$ |

![Subgroup lattice of the cyclic group of order twelve](../../diagrams/MAM2013S-Introductory%20Algebra/03_Groups/c12-lattice.svg)

*The subgroup generated by $g^6$ lies in those generated by $g^2$ and $g^3$. The subgroup generated by $g^4$ lies in the one generated by $g^2$.*

#### All subgroups of the additive group modulo one hundred

Define $d\mathbb Z_{100}=\langle\overline d\rangle$ for positive divisors $d$ of $100$. Since $100=2^2\cdot5^2$, it has the nine divisors $1,2,4,5,10,20,25,50,100$.

| Order | Generator | Subgroup |
|---|---|---|
| $1$ | $\overline0=\overline{100}$ | $\{\overline0\}$ |
| $2$ | $\overline{50}$ | $50\mathbb Z_{100}$ |
| $4$ | $\overline{25}$ | $25\mathbb Z_{100}$ |
| $5$ | $\overline{20}$ | $20\mathbb Z_{100}$ |
| $10$ | $\overline{10}$ | $10\mathbb Z_{100}$ |
| $20$ | $\overline5$ | $5\mathbb Z_{100}$ |
| $25$ | $\overline4$ | $4\mathbb Z_{100}$ |
| $50$ | $\overline2$ | $2\mathbb Z_{100}$ |
| $100$ | $\overline1$ | $\mathbb Z_{100}$ |

![Subgroup lattice for the integers modulo one hundred](../../diagrams/MAM2013S-Introductory%20Algebra/03_Groups/z100-lattice.svg)

*The nine nodes correspond to the nine divisor orders. A line or upward path records inclusion; for example, $20\mathbb Z_{100}\subseteq4\mathbb Z_{100}\subseteq2\mathbb Z_{100}$.*

Other useful containment chains are

$$
\begin{aligned}
20\mathbb Z_{100}&\subseteq10\mathbb Z_{100}\subseteq5\mathbb Z_{100},\\
50\mathbb Z_{100}&\subseteq10\mathbb Z_{100}\subseteq2\mathbb Z_{100},\\
50\mathbb Z_{100}&\subseteq25\mathbb Z_{100}\subseteq5\mathbb Z_{100}.
\end{aligned}
$$

The theorem proves order divisibility and unique divisor-order subgroups for finite cyclic groups. The later Lagrange chapter generalises order divisibility to all finite groups; uniqueness of each divisor-order subgroup is a special cyclic-group conclusion.

### Homomorphisms and Isomorphisms

#### Definitions

> **Group homomorphism**: A map $\varphi:(G_1,\cdot_1)\to(G_2,\cdot_2)$ satisfying $\varphi(a\cdot_1b)=\varphi(a)\cdot_2\varphi(b)$ for every $a,b\in G_1$.

> **Monomorphism**: An injective group homomorphism.

> **Epimorphism**: In this course's terminology, a surjective group homomorphism.

> **Isomorphism**: A bijective group homomorphism. If one exists, write $G_1\cong G_2$.

> **Automorphism**: An isomorphism from a group to itself.

A homomorphism preserves the group operation; it need not be one-to-one or onto. An isomorphism identifies the entire structure by relabelling its elements bijectively.

The geometric comparison is helpful: congruent figures preserve shape and size, while similar figures permit uniform scaling. For groups, the structure to preserve is the operation.

![Congruence and similarity as geometric analogies for preserving structure](../../diagrams/MAM2013S-Introductory%20Algebra/03_Groups/geometric-analogy.svg)

*Moving, rotating, or reflecting preserves congruence; uniform scaling preserves similarity. A group isomorphism preserves the corresponding algebraic structure through a bijection.*

![A Cayley-table entry before and after a structure-preserving relabelling](../../diagrams/MAM2013S-Introductory%20Algebra/03_Groups/cayley-relabelling.svg)

*The entry for the original product must relabel to the product of the relabelled row and column elements. This is the equation $\varphi(ab)=\varphi(a)\varphi(b)$.*

#### Proving a proposed map is an isomorphism

1. Specify a candidate map and its domain and codomain.
2. Check that it is well-defined and bijective.
3. Take arbitrary $a,b$ in the domain and verify the operation-preserving equation.
4. Keep the operation of each group explicit when the two operations differ.

The map

$$
f:(\mathbb R,+)\to(\mathbb R^+,\times),\qquad f(x)=e^x,
$$

is an isomorphism. Here $\mathbb R^+$ means the positive real numbers.

- If $e^a=e^b$, taking logarithms gives $a=b$, so it is injective.
- For every $y>0$, $y=e^{\ln y}$, so it is surjective.
- It preserves the operations because $f(a+b)=e^{a+b}=e^ae^b=f(a)f(b)$.

#### Three homomorphism examples

For $\varphi:(\mathbb Z,+)\to(\mathbb Z,+)$ defined by $\varphi(a)=3a$,

$$
\varphi(a+b)=3(a+b)=3a+3b=\varphi(a)+\varphi(b).
$$

It is injective because $3a=3b$ implies $a=b$, but not surjective because, for example, $4$ is not a multiple of $3$. It is a monomorphism, but not an isomorphism onto $\mathbb Z$.

The absolute-value map

$$
\psi:(\mathbb C^*,\times)\to(\mathbb R^+,\times),\qquad\psi(z)=|z|
$$

is an epimorphism: $|zw|=|z||w|$, and every positive real is the absolute value of itself. It is not injective, since $|1|=|-1|$.

The determinant map

$$
\det:\mathrm{GL}_n(\mathbb R)\to\mathbb R^*,\qquad A\mapsto\det A
$$

is a homomorphism because $\det(AB)=\det A\det B$. It is onto: any $r\ne0$ is the determinant of $\operatorname{diag}(r,1,\ldots,1)$.

For $n\ge2$ it is not injective. For example, both $I_2$ and $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ have determinant $1$; the same example extends to larger dimensions by adding identity blocks. For $n=1$, the determinant map is an isomorphism.

#### What every homomorphism preserves

**Theorem 3.36**: A homomorphism $\varphi:G_1\to G_2$ satisfies

$$
\varphi(1_{G_1})=1_{G_2},\qquad
\varphi(g^{-1})=\varphi(g)^{-1},\qquad
\varphi(g^k)=\varphi(g)^k\quad(k\in\mathbb Z).
$$

**Proof**:

1. Since $\varphi(1)=\varphi(1\cdot1)=\varphi(1)\varphi(1)$, cancellation in $G_2$ gives $\varphi(1)=1$.
2. Applying $\varphi$ to $gg^{-1}=1$ gives $\varphi(g)\varphi(g^{-1})=1$. Applying it to the reversed product gives the other inverse equation, so uniqueness proves the inverse rule.
3. For positive powers, induct using $\varphi(g^{k+1})=\varphi(g)\varphi(g^k)$. The zero case uses identity preservation. For $k=-m<0$, use
   $$\varphi(g^{-m})=\varphi((g^m)^{-1})=\varphi(g^m)^{-1}=\varphi(g)^{-m}.$$

#### Isomorphisms form an equivalence relation

**Theorem 3.37**:

- The identity map of any group is an isomorphism.
- The inverse of an isomorphism is an isomorphism.
- A composition of isomorphisms is an isomorphism.

The identity map preserves every product directly. If $\varphi$ is bijective and $u=\varphi(a)$, $v=\varphi(b)$, then

$$
\varphi^{-1}(uv)=\varphi^{-1}(\varphi(ab))=ab
=\varphi^{-1}(u)\varphi^{-1}(v).
$$

If $\varphi,\psi$ are isomorphisms, their composition is bijective and

$$
(\psi\circ\varphi)(ab)
=\psi(\varphi(a)\varphi(b))
=(\psi\circ\varphi)(a)(\psi\circ\varphi)(b).
$$

These give reflexivity, symmetry, and transitivity, so $\cong$ is an equivalence relation (Corollary 3.38).

**Corollary 3.39**: The set $\operatorname{Aut}(G)$ of automorphisms is a group under composition. Closure and inverses follow from Theorem 3.37; function composition is associative, and the identity map is its identity.

#### Proving groups are not isomorphic

An isomorphism preserves properties expressible through the group structure. A mismatch in any such property rules out an isomorphism.

| Property | Why it is preserved |
|---|---|
| Number of elements | The map is bijective |
| Commutativity | The product-preserving equation carries $ab=ba$ across the map |
| Cyclicity | If every element is a power of $g$, every image is a power of $\varphi(g)$ |
| Orders of elements | Power and identity preservation, together with the inverse isomorphism, preserve the least identity exponent |
| Generation by two elements | Images of the two generators generate the codomain |
| Every element being a square | $\varphi(g^2)=\varphi(g)^2$, and surjectivity covers every codomain element |

Thus $\mathbb Z_4$ and $\mathbb Z_2\times\mathbb Z_2$ are not isomorphic: the former is cyclic and has elements of order $4$, while the latter has only orders $1,2$.

Also $(\mathbb R,+)$ is not isomorphic to $(\mathbb R^*,\times)$. The latter contains the nonidentity element $-1$ with $(-1)^2=1$. The corresponding additive condition would require a nonzero real $a$ with $2a=0$, which is impossible.

Having the same number of elements is necessary but insufficient for isomorphism, as the order-four examples show.

#### Classification of cyclic groups up to isomorphism

**Theorem 3.40**:

1. Every cyclic group of finite order $n$ is isomorphic to $(\mathbb Z_n,+)$.
2. Every infinite cyclic group is isomorphic to $(\mathbb Z,+)$.

![The finite and infinite cyclic correspondences](../../diagrams/MAM2013S-Introductory%20Algebra/03_Groups/cyclic-correspondence.svg)

*Integer exponents become additive labels. In the finite case they are residue classes; in the infinite case every distinct integer labels a distinct power.*

For a finite cyclic group $\langle a\rangle$ of order $n$, define

$$
\varphi:\mathbb Z_n\to\langle a\rangle,\qquad\varphi(\overline i)=a^i.
$$

This is well-defined: congruent exponents modulo $n$ give the same power. It is bijective by the finite equality-of-powers criterion, and

$$
\varphi(\overline i+\overline j)=a^{i+j}=a^ia^j
=\varphi(\overline i)\varphi(\overline j).
$$

For an infinite cyclic group, define $\varphi:\mathbb Z\to\langle a\rangle$ by $\varphi(i)=a^i$. Distinct exponents give distinct powers, every element is a power, and the same exponent-addition equation proves the homomorphism condition.

Therefore any two finite cyclic groups of the same order are isomorphic, and any two infinite cyclic groups are isomorphic.
