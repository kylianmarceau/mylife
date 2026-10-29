---
tags:
  - introductory-algebra
  - flashcards
qard-deck: "Introductory Algebra"
qard-topic: "03 — Groups: Subgroups, Cyclic Groups, and Isomorphisms"
---

# 03 — Groups: Subgroups, Cyclic Groups, and Isomorphisms

**Source note:** [Groups: Subgroups, Cyclic Groups, and Isomorphisms](../03_Groups.md)

Exam recall cards covering concepts, definitions, methods, and qualifications. Worked examples are omitted; general proof methods are retained.

## Contents

- [[#Core Content|Core Content]]
  - [[#What Is a Group?|What Is a Group?]]
  - [[#Cayley Tables|Cayley Tables]]
  - [[#Inverses, Orders, Exponent Laws, and Cancellation|Inverses, Orders, Exponent Laws, and Cancellation]]
  - [[#Isomorphism and Small Groups|Isomorphism and Small Groups]]
  - [[#Subgroups and the Centre|Subgroups and the Centre]]
  - [[#Cyclic Groups|Cyclic Groups]]
  - [[#Properties and Generators of Cyclic Groups|Properties and Generators of Cyclic Groups]]
  - [[#Fundamental Theorem of Finite Cyclic Groups|Fundamental Theorem of Finite Cyclic Groups]]
  - [[#Homomorphisms and Isomorphisms|Homomorphisms and Isomorphisms]]

## Core Content

### What Is a Group?

<!-- qard-id: alg-269fa93160b5d05ca088 -->
> [!qard]- What is a binary operation on a set $G$?
> A function $G\times G\to G$ assigning each ordered pair exactly one element of $G$; closure is built into the codomain.

<!-- qard-id: alg-a47213439533311b2afd -->
> [!qard]- What axioms define a group $(G,\cdot)$?
> A binary operation that is associative, has a two-sided identity, and gives every element a two-sided inverse in $G$.

<!-- qard-id: alg-741c1c706a1f1876ddfd -->
> [!qard]- What is associativity of a group operation?
> $a(bc)=(ab)c$ for all $a,b,c\in G$.

<!-- qard-id: alg-d3ade4c97c2f4fdbd8c5 -->
> [!qard]- What is the identity of a group?
> An element $1_G$ with $1_Gg=g1_G=g$ for every $g\in G$.

<!-- qard-id: alg-1eec63e18aa2ad4aa807 -->
> [!qard]- What is the inverse of a group element $g$?
> An element $g^{-1}\in G$ with $gg^{-1}=g^{-1}g=1_G$.

<!-- qard-id: alg-fabf87d286ae61a1290e -->
> [!qard]- What makes a group abelian?
> Its operation is commutative: $gh=hg$ for every pair $g,h\in G$.

<!-- qard-id: alg-2f27f427c65376f8c336 -->
> [!qard]- What is the order of a finite group?
> Its number of elements, denoted $|G|$.

<!-- qard-id: alg-8b0bcd0259ae727f1bfb -->
> [!qard]- Why must a proposed group specify both its set and its operation?
> The group axioms depend on the operation; the same set may be a group under one operation and fail under another.

<!-- qard-id: alg-4ad28cbd85983d80a352 -->
> [!qard]- Why is the identity of a group unique?
> If $e,f$ are identities, $e=ef=f$.

<!-- qard-id: alg-51faa6e80af25eed1fd3 -->
> [!qard]- Why is an element's inverse unique?
> If $b,c$ are inverses of $a$, then $b=b(ac)=(ba)c=c$.

<!-- qard-id: alg-e1ff943a02639b082a23 -->
> [!qard]- How do identity, inverse, and powers translate into additive notation?
> $1$ becomes $0$, $g^{-1}$ becomes $-g$, and $g^n$ becomes $ng$; multiplication becomes addition.

<!-- qard-id: alg-9e92d3ac88b9ab110776 -->
> [!qard]- Does $1_G$ have to be the ordinary number $1$?
> No. It denotes the identity for the specified operation.

<!-- qard-id: alg-076c4fea83488cc50f2e -->
> [!qard]- Which operation makes $\mathbb Z,\mathbb Q,\mathbb R,\mathbb C$ abelian groups?
> Addition, with identity $0$ and inverse $-a$.

<!-- qard-id: alg-d437475e4d86c061771f -->
> [!qard]- Which operation makes $\mathbb Q^*,\mathbb R^*,\mathbb C^*$ abelian groups?
> Multiplication on the nonzero elements, with identity $1$ and inverse $1/a$.

<!-- qard-id: alg-de0fddf2a4747adfda39 -->
> [!qard]- Why is $\mathbb Z$ not a group under multiplication?
> Not every integer has a multiplicative inverse in $\mathbb Z$; for instance, $2$ has none.

<!-- qard-id: alg-ab5e8c486d60af45b304 -->
> [!qard]- What are the operation, identity, and inverses in the additive group $\mathbb Z_n$?
> Addition modulo $n$, identity $\overline0$, and inverse $-\overline a=\overline{-a}$.

<!-- qard-id: alg-a94346a471795c6d049f -->
> [!qard]- Why is all of $\mathbb Z_n$ not a group under modular multiplication?
> $\overline0$ has no multiplicative inverse.

<!-- qard-id: alg-c2a2af015c8cc537ab8e -->
> [!qard]- What operation makes $S_n$ a group, and when is it nonabelian?
> Permutation composition, with identity permutation $\varepsilon$ and inverse permutations. It is nonabelian for $n\ge3$.

<!-- qard-id: alg-dfc9682a10cb4743311e -->
> [!qard]- What operation is assumed here for $\mathbb Z_n,\mathbb Z,\mathbb Q,\mathbb R,\mathbb C$ when none is specified?
> Addition; a multiplicative group must be specified separately.

<!-- qard-id: alg-3d514f93aa84ea3d2e73 -->
> [!qard]- What is a unit in a coefficient system?
> An element with a multiplicative inverse in that same system.

<!-- qard-id: alg-23f2f80075792e5aa59e -->
> [!qard]- What is the unit group $\mathbb Z_n^*$?
> $\{\overline a:\gcd(a,n)=1\}$ under modular multiplication, with identity $\overline1$.

<!-- qard-id: alg-b3836018f22d2da53778 -->
> [!qard]- How does $\mathbb Z^*$ differ from the nonzero multiplicative groups of fields?
> $\mathbb Z^*=\{1,-1\}$; most nonzero integers are not units. In $\mathbb Q,\mathbb R,\mathbb C$, every nonzero element is a unit.

<!-- qard-id: alg-6022084b0e5a0f744141 -->
> [!qard]- What is $\mathrm{GL}_n(R)$?
> The invertible $n\times n$ matrices over $R$, under matrix multiplication.

<!-- qard-id: alg-30b512f6e84d90335436 -->
> [!qard]- What determinant condition characterises invertibility over the coefficient systems in these notes?
> The determinant must be a unit in that coefficient system.

<!-- qard-id: alg-3689803d6c186a9e58ed -->
> [!qard]- What determinant condition defines $\mathrm{GL}_n(R)$ for $R=\mathbb Q,\mathbb R,\mathbb C$?
> $\det A\ne0$.

<!-- qard-id: alg-7e99642ab1af4f4a4b4a -->
> [!qard]- What determinant condition defines $\mathrm{GL}_n(\mathbb Z)$?
> $\det A=\pm1$; a merely nonzero determinant does not ensure an integer matrix inverse.

<!-- qard-id: alg-5a6c3f017114367a9144 -->
> [!qard]- What determinant condition gives invertibility over $\mathbb Z_m$?
> If $\det A=\overline a$, require $\gcd(a,m)=1$.

<!-- qard-id: alg-c6dbfa0528270ea5f1ae -->
> [!qard]- Why do invertible matrices form a group?
> Matrix multiplication is associative; $I_n$ is the identity; matrix inverses belong to the set; and $(AB)^{-1}=B^{-1}A^{-1}$ proves closure.

<!-- qard-id: alg-4ac7535e69639217fc0a -->
> [!qard]- What is the direct product of groups $G_1,\ldots,G_r$?
> Their Cartesian product with componentwise operation: $(g_1,\ldots,g_r)(h_1,\ldots,h_r)=(g_1h_1,\ldots,g_rh_r)$.

<!-- qard-id: alg-a5c4d7010880a3f6fc2c -->
> [!qard]- What are the identity and inverse in a direct product?
> Identity $(1_{G_1},\ldots,1_{G_r})$; inverse $(g_1^{-1},\ldots,g_r^{-1})$.

<!-- qard-id: alg-95c4f411fed1b86faf55 -->
> [!qard]- Why is a direct product of groups a group?
> Closure, associativity, identity, and inverse equations each hold independently in every component.

### Cayley Tables

<!-- qard-id: alg-f24c5a98a79faa721d16 -->
> [!qard]- What does a Cayley table record?
> The operation of a finite group: entry in row $a$, column $b$ is $ab$.

<!-- qard-id: alg-16caec08d7ead49fad56 -->
> [!qard]- When a Cayley table describes permutations, which factor acts first?
> The column factor, because $ab$ means apply $b$ first and then $a$.

<!-- qard-id: alg-d2bce94ad31a70e6209b -->
> [!qard]- What are generators of a group?
> Elements from which every group element can be obtained through products and inverses.

<!-- qard-id: alg-4577e4edcf2687b5e6e1 -->
> [!qard]- What are relations among group generators?
> Equations they satisfy, used to simplify products.

<!-- qard-id: alg-80153f2c8a6d5d388568 -->
> [!qard]- Which generators and relations describe $S_3$ in these notes?
> $\sigma=(1\,2\,3)$ and $\tau=(1\,2)$, with $\sigma^3=\tau^2=\varepsilon$ and $\sigma\tau\sigma=\tau$.

<!-- qard-id: alg-6eb16c2474db9fbd3aed -->
> [!qard]- What normal forms list the elements of $S_3$ using $\sigma$ and $\tau$?
> $\varepsilon,\sigma,\sigma^2,\tau,\tau\sigma,\tau\sigma^2$.

<!-- qard-id: alg-92d2c9395b8170485b70 -->
> [!qard]- Which useful rewriting relations follow from $\sigma\tau\sigma=\tau$ in $S_3$?
> $\sigma\tau=\tau\sigma^2$ and $\sigma^2\tau=\tau\sigma$.

<!-- qard-id: alg-d442804153f3a6c3a035 -->
> [!qard]- What group structure does $\mathbb Z_2\times\mathbb Z_2$ have?
> The Klein four-group structure: every element is self-inverse, and two distinct nonidentity elements combine to give the third.

<!-- qard-id: alg-a5a4a9ad5e935e8aed95 -->
> [!qard]- How does a Cayley table reveal whether a group is abelian?
> It is symmetric across the main diagonal exactly when $ab=ba$ for every pair.

<!-- qard-id: alg-cf4c80f10f30a0b0a757 -->
> [!qard]- How do you find the identity in a Cayley table?
> Its row and column reproduce the column and row labels respectively.

<!-- qard-id: alg-705d8256df8599019b86 -->
> [!qard]- How do you find an element's inverse in a Cayley table?
> Find the element whose product with it is the identity in both orders.

<!-- qard-id: alg-524ccd45750edefc5351 -->
> [!qard]- What occurrence property holds in every row and column of a group table?
> Each group element occurs exactly once, by the existence and uniqueness of solutions to $gx=h$ and $xg=h$.

### Inverses, Orders, Exponent Laws, and Cancellation

<!-- qard-id: alg-1f8764ac415647640e4b -->
> [!qard]- How are powers $g^n$ defined for all integers $n$?
> Positive powers are repeated products, $g^0=1$, and $g^{-n}=(g^{-1})^n=(g^n)^{-1}$ for $n>0$.

<!-- qard-id: alg-07d6d742a07d8b80d391 -->
> [!qard]- What is the order $o(g)$ of a group element?
> The least positive $n$ with $g^n=1$, if one exists; otherwise $g$ has infinite order.

<!-- qard-id: alg-69254215a23a780f948b -->
> [!qard]- What is the additive version of the element-order condition?
> The least positive $n$ with $ng=0$, or infinite order if no such $n$ exists.

<!-- qard-id: alg-5376153eb52887e86b51 -->
> [!qard]- How do group order and element order differ?
> $|G|$ counts elements of the group; $o(g)$ measures the least positive identity power of one element.

<!-- qard-id: alg-1bedc4017219b34f8633 -->
> [!qard]- What is the order of the identity?
> $1$.

<!-- qard-id: alg-3ffc4b25384273a888de -->
> [!qard]- What is the order of a nonidentity self-inverse element?
> $2$, since $g^2=1$ and $g\ne1$.

<!-- qard-id: alg-6cf28b83c205224c07fe -->
> [!qard]- If $o(g)=n$ and $g^\ell=1$, what can be concluded about $\ell$?
> $n\mid\ell$.

<!-- qard-id: alg-a9ff10f8f459b171056a -->
> [!qard]- How does division with remainder prove that $g^\ell=1$ implies $o(g)\mid\ell$?
> Write $\ell=qn+r$, $0\le r<n$, where $n=o(g)$. Then $g^r=1$; minimality of $n$ forces $r=0$.

<!-- qard-id: alg-bf741dafa51bdfb9777d -->
> [!qard]- What are the inverse of the identity and the inverse of an inverse?
> $1^{-1}=1$ and $(g^{-1})^{-1}=g$.

<!-- qard-id: alg-093535c05f65e12de82b -->
> [!qard]- What is the inverse of a product $gh$?
> $(gh)^{-1}=h^{-1}g^{-1}$; the order reverses.

<!-- qard-id: alg-dc452e6f627f51291e69 -->
> [!qard]- How do you prove $(gh)^{-1}=h^{-1}g^{-1}$?
> Both $(gh)(h^{-1}g^{-1})$ and $(h^{-1}g^{-1})(gh)$ simplify to $1$; uniqueness of inverses gives the result.

<!-- qard-id: alg-637c7f41df6f45d67325 -->
> [!qard]- What is the inverse of a product of several group elements?
> $(g_1\cdots g_r)^{-1}=g_r^{-1}\cdots g_1^{-1}$, by repeatedly applying the two-factor inverse law.

<!-- qard-id: alg-0babc9f75324a3e40527 -->
> [!qard]- Which same-base exponent laws hold in any group for integers $m,n$?
> $g^ng^m=g^{n+m}$ and $(g^n)^m=g^{nm}$.

<!-- qard-id: alg-889ff2dfa426c0b7fcfb -->
> [!qard]- Under what condition does $(gh)^n=g^nh^n$ hold for all integers $n$?
> When $g$ and $h$ commute.

<!-- qard-id: alg-68ba377c6e97519c95b3 -->
> [!qard]- If $g$ commutes with $h$, what can be said about $g^n$ and $h$?
> $g^nh=hg^n$ for every integer $n$.

<!-- qard-id: alg-1de6b9a7c95e91a7c205 -->
> [!qard]- Why do powers of the same element always commute?
> $g^ng^m=g^{n+m}=g^{m+n}=g^mg^n$.

<!-- qard-id: alg-4c52ca91beea49ab9c99 -->
> [!qard]- How do you show that $g^{-1}$ commutes with $h$ when $g$ does?
> Multiply $gh=hg$ on the left and right by $g^{-1}$ to obtain $hg^{-1}=g^{-1}h$.

<!-- qard-id: alg-ec34e3cc381e67865bea -->
> [!qard]- How are positive exponent laws extended to negative powers?
> Use $g^{-n}=(g^n)^{-1}$, the reverse-product inverse law, and commutation of inverses when the original factors commute.

<!-- qard-id: alg-b5983a687061a7917d19 -->
> [!qard]- How are mixed-sign same-base exponent laws justified?
> Cancel inverse factors in $g^n(g^{-1})^t$, leaving the power corresponding to $n-t$.

<!-- qard-id: alg-2656ee21d1257680f037 -->
> [!qard]- What are the exponent laws in additive notation?
> $(n+m)g=ng+mg$ and $m(ng)=(mn)g$; for commuting $g,h$, $n(g+h)=ng+nh$.

<!-- qard-id: alg-f3d6ca893c270a8525ce -->
> [!qard]- What are left and right cancellation in a group?
> $gh=gf\Rightarrow h=f$ and $hg=fg\Rightarrow h=f$.

<!-- qard-id: alg-82d2db9f246afb6fbcea -->
> [!qard]- How are the cancellation laws proved?
> Multiply by $g^{-1}$ on the left for left cancellation and on the right for right cancellation.

<!-- qard-id: alg-666ec4bd781671823efc -->
> [!qard]- What is the unique solution to $gx=h$?
> $x=g^{-1}h$.

<!-- qard-id: alg-f576099a4c5f5961b5da -->
> [!qard]- What is the unique solution to $xg=h$?
> $x=hg^{-1}$.

<!-- qard-id: alg-3dec9b16ebef00c04e55 -->
> [!qard]- Why must the side of multiplication be respected when solving group equations?
> A group can be nonabelian; multiplying by an inverse on the wrong side changes the expression.

<!-- qard-id: alg-6012178d61716b397411 -->
> [!qard]- Why does every element occur exactly once in each Cayley-table row?
> For a fixed $g$ and desired entry $h$, $gx=h$ has exactly one solution $x$; columns use $xg=h$.

### Isomorphism and Small Groups

<!-- qard-id: alg-b5ca46cdd1e9e5d13f99 -->
> [!qard]- What does isomorphism of finite groups mean in terms of their tables?
> A consistent bijective relabelling makes their Cayley tables identical.

<!-- qard-id: alg-df366ea5ea8eeb28bbf7 -->
> [!qard]- What is a cyclic group?
> A group whose elements are all integer powers of one element, or all integer multiples in additive notation.

<!-- qard-id: alg-704a365d7e0e71c3d6f8 -->
> [!qard]- What is the structure of the Klein group $K_4$?
> $\{1,a,b,c\}$, with $a^2=b^2=c^2=1$ and the product of two distinct nonidentity elements equal to the third.

<!-- qard-id: alg-3880859a26f9eabb268b -->
> [!qard]- How many groups of each order $1,2,3$ exist up to isomorphism?
> One at each order; each is cyclic.

<!-- qard-id: alg-65149bfe40f5d4b82270 -->
> [!qard]- Why must the nonidentity element of a group of order $2$ square to the identity?
> Its square is either itself or $1$. The first possibility contradicts cancellation, so $g^2=1$.

<!-- qard-id: alg-f1957430e2df991f03c8 -->
> [!qard]- How does cancellation determine a group's structure when it has order $3$?
> For distinct nonidentity $g,h$, $gh$ cannot equal $g$ or $h$, so $gh=hg=1$. Table uniqueness forces $g^2=h$, $h^2=g$, and $g^3=1$.

<!-- qard-id: alg-281a72ceda2a6793f91b -->
> [!qard]- Which two groups of order $4$ occur up to isomorphism?
> $C_4$ and $K_4$, represented additively by $\mathbb Z_4$ and $\mathbb Z_2\times\mathbb Z_2$.

<!-- qard-id: alg-e912ce591a1895c0a888 -->
> [!qard]- How do the element orders of $C_4$ and $K_4$ differ?
> The nonidentity orders in $C_4$ are $4,2,4$; in $K_4$ they are all $2$.

<!-- qard-id: alg-f2434311666a4c0daae0 -->
> [!qard]- Why is $K_4$ not cyclic?
> The identity generates one element and every nonidentity element generates only two, so no element generates all four.

<!-- qard-id: alg-c9fd1fb1365e7471a059 -->
> [!qard]- Are all abelian groups cyclic?
> No; $K_4$ is abelian but noncyclic.

### Subgroups and the Centre

<!-- qard-id: alg-b850b7f7818d3ac0e0de -->
> [!qard]- What is a subgroup $H\le G$?
> A subset of $G$ that is a group under the operation inherited from $G$.

<!-- qard-id: alg-32762823f192212b7031 -->
> [!qard]- What three conditions constitute the subgroup test?
> $1_G\in H$, closure under products, and closure under inverses.

<!-- qard-id: alg-80a9c691c826d98b674b -->
> [!qard]- Why need associativity not be checked again in the subgroup test?
> It is inherited from the parent group $G$.

<!-- qard-id: alg-5603f1dc315bd869b02a -->
> [!qard]- Why does a subgroup have the same identity as its parent group?
> If $e$ is its identity, $e^2=e=e1_G$; cancellation in $G$ yields $e=1_G$.

<!-- qard-id: alg-68b11d31a0b925ce9102 -->
> [!qard]- Why are inverses in a subgroup the same as inverses in its parent group?
> If $h'$ is the subgroup inverse of $h$, $hh'=1_G=hh^{-1}$; cancellation gives $h'=h^{-1}$.

<!-- qard-id: alg-a851e4a090a8408ec0c5 -->
> [!qard]- What is the combined subgroup test using $hh_1^{-1}$?
> A nonempty subset $H\subseteq G$ is a subgroup exactly when $hh_1^{-1}\in H$ for all $h,h_1\in H$.

<!-- qard-id: alg-eadf616ecde9d5c8f07e -->
> [!qard]- How does closure under $hh_1^{-1}$ yield the identity and inverses?
> Equal inputs give $hh^{-1}=1_G$; then using $1_G$ as the first input gives each $h_1^{-1}$.

<!-- qard-id: alg-e79578733d8792f6c67c -->
> [!qard]- How does the combined subgroup test yield closure under products?
> Having obtained inverses, use $h_1^{-1}$ as the second input: $h(h_1^{-1})^{-1}=hh_1$.

<!-- qard-id: alg-7ca0b9a778677de45b98 -->
> [!qard]- What is the combined subgroup test for additive groups?
> Nonemptiness and closure under differences: $h-h_1\in H$ for every $h,h_1\in H$.

<!-- qard-id: alg-c48107b3b41d8144f148 -->
> [!qard]- Why is $n\mathbb Z$ a subgroup of $(\mathbb Z,+)$ for $n\ge0$?
> It contains $0$, and $nk+nm=n(k+m)$ and $-(nk)=n(-k)$ remain in the set.

<!-- qard-id: alg-39991658ce8401db5ab6 -->
> [!qard]- What does $0\mathbb Z$ denote?
> The trivial subgroup $\{0\}$.

<!-- qard-id: alg-dac8f11dd4cde3cac5d5 -->
> [!qard]- What is the finite subgroup test?
> A finite nonempty subset of a group is a subgroup exactly when it is closed under the group operation.

<!-- qard-id: alg-2b5cb010f06b6584407c -->
> [!qard]- How does finiteness plus product closure force the identity into a nonempty subset $H$?
> Powers of $h\in H$ stay in $H$; some $h^i=h^j$ with $i<j$. Cancellation gives $h^{j-i}=1_G\in H$.

<!-- qard-id: alg-595268e50fdca56f8060 -->
> [!qard]- How does the finite subgroup-test proof obtain the inverse of each $h\in H$?
> From $h^r=1$ with $r>0$, $h^{-1}=h^{r-1}$; positive powers lie in $H$, and the zero-power case is the established identity.

<!-- qard-id: alg-23f4ea0ea7e33916c2bd -->
> [!qard]- Why are finiteness and nonemptiness essential to the finite subgroup test?
> An empty subset cannot be a group; an infinite closed subset may lack identity or inverses, as positive integers under addition do.

<!-- qard-id: alg-c96367c715ee34b6e684 -->
> [!qard]- What are all the subgroups of $C_4=\langle a\rangle$?
> $\{1\}$, $\{1,a^2\}$, and $C_4$.

<!-- qard-id: alg-7691f3d5da254193f934 -->
> [!qard]- Why does a subgroup of $C_4$ containing $a$ or $a^3$ equal $C_4$?
> Either element generates all of $C_4$, so closure under powers forces the whole group.

<!-- qard-id: alg-b7cc9a64b00c3f99e7a9 -->
> [!qard]- What are all the subgroups of $K_4=\{1,a,b,c\}$?
> $\{1\}$, $\{1,a\}$, $\{1,b\}$, $\{1,c\}$, and $K_4$.

<!-- qard-id: alg-a2b53bea5efa8e60486f -->
> [!qard]- Why does a subgroup of $K_4$ containing two distinct nonidentity elements equal $K_4$?
> Their product is the third nonidentity element, so all four elements belong to it.

<!-- qard-id: alg-aba5f60b9a4d80150ad6 -->
> [!qard]- What does a subgroup lattice diagram represent?
> Subgroup containment: smaller subgroups lie below larger ones, and upward paths record inclusions.

<!-- qard-id: alg-c71b7e407b6f28af38b3 -->
> [!qard]- What is the centre $Z(G)$ of a group?
> $Z(G)=\{z\in G:zg=gz\text{ for every }g\in G\}$.

<!-- qard-id: alg-dbd7f9b760df04f8144e -->
> [!qard]- When does $Z(G)=G$?
> Exactly when $G$ is abelian.

<!-- qard-id: alg-ba970eab05be74e84db1 -->
> [!qard]- Why is the identity in $Z(G)$?
> It commutes with every group element.

<!-- qard-id: alg-7fe9a206c1403fc49536 -->
> [!qard]- Why is $Z(G)$ closed under products?
> For central $z,z'$ and arbitrary $g$, $gzz'=zgz'=zz'g$, so $zz'$ is central.

<!-- qard-id: alg-4e84470e26e72e26746c -->
> [!qard]- Why is $Z(G)$ closed under inverses?
> From $zg=gz$, multiply on the left and right by $z^{-1}$ to get $gz^{-1}=z^{-1}g$.

<!-- qard-id: alg-95e561130c3c0404c398 -->
> [!qard]- What establishes that the centre is a subgroup?
> It contains the identity and is closed under products and inverses, so the subgroup test gives $Z(G)\le G$.

<!-- qard-id: alg-9a9d8ce8aee2264350f2 -->
> [!qard]- What is the centre of $S_3$?
> $\{\varepsilon\}$; every nonidentity element fails to commute with at least one other element.

### Cyclic Groups

<!-- qard-id: alg-8816a6ec40293f136d42 -->
> [!qard]- What is the cyclic subgroup $\langle g\rangle$?
> $\{g^k:k\in\mathbb Z\}$.

<!-- qard-id: alg-863957216dfde48a10bd -->
> [!qard]- What does it mean for $g$ to generate $G$?
> $G=\langle g\rangle$.

<!-- qard-id: alg-8be875a0c234295886e2 -->
> [!qard]- Why is $\langle g\rangle$ a subgroup?
> It contains $g^0=1$, products add exponents, and inverses negate exponents.

<!-- qard-id: alg-2bc46e70a19094f6af73 -->
> [!qard]- Why is $\langle g\rangle$ the smallest subgroup containing $g$?
> Every subgroup containing $g$ must contain its inverse and all positive and negative powers of $g$.

<!-- qard-id: alg-0610e5ec00b318ddaab5 -->
> [!qard]- How is $\langle g\rangle$ written in additive notation?
> $\{kg:k\in\mathbb Z\}=\mathbb Zg$.

<!-- qard-id: alg-a1660554fc720895f0b8 -->
> [!qard]- What are the elements of a cyclic group generated by an element of order $n$?
> $1,g,\ldots,g^{n-1}$, all distinct.

<!-- qard-id: alg-fb8643f7b811bd2507ed -->
> [!qard]- How are exponents reduced in a cyclic group with $o(g)=n$?
> Write $k=qn+r$, $0\le r<n$. Then $g^k=(g^n)^qg^r=g^r$.

<!-- qard-id: alg-6d78ae8d2a714172e289 -->
> [!qard]- What is the product rule for elements of a finite cyclic group of order $n$?
> $g^ig^j=g^{(i+j)\bmod n}$ for $0\le i,j<n$.

<!-- qard-id: alg-2a5682b3358cfc385496 -->
> [!qard]- Which elements generate the additive group $\mathbb Z$?
> Only $1$ and $-1$.

<!-- qard-id: alg-1f88a671659c8d0d4d6a -->
> [!qard]- Why is the additive group $\mathbb Z_n$ cyclic?
> $\overline1$ generates it, because $\overline k=k\overline1$.

<!-- qard-id: alg-149e4b8dfa91c860d5f7 -->
> [!qard]- Does being a unit group modulo $n$ guarantee cyclicity?
> No. For example, $\mathbb Z_8^*$ has Klein-group structure and is noncyclic.

<!-- qard-id: alg-bf7dca8c5eade82d3dd7 -->
> [!qard]- For $o(g)=n$, when is $g^k=1$?
> Exactly when $n\mid k$.

<!-- qard-id: alg-3d36799361f2c3cde9ed -->
> [!qard]- For $o(g)=n$, when do $g^k$ and $g^m$ coincide?
> Exactly when $k\equiv m\pmod n$.

<!-- qard-id: alg-d36f9b14bc5cd33cec39 -->
> [!qard]- For an infinite-order element $g$, when is $g^k=1$?
> Exactly when $k=0$.

<!-- qard-id: alg-d8d4b2d5acbadd0b8360 -->
> [!qard]- For an infinite-order element $g$, when do $g^k$ and $g^m$ coincide?
> Exactly when $k=m$.

<!-- qard-id: alg-05b198f5990b14731a83 -->
> [!qard]- Why does a finite cyclic subgroup have a positive identity power?
> Finitely many elements force two positive powers to coincide; cancelling yields $g^{m-k}=1$ for a positive exponent.

<!-- qard-id: alg-36d6b267f0df90e6c604 -->
> [!qard]- How does the identity-power criterion give the equality-of-powers criterion?
> $g^k=g^m$ exactly when $g^{k-m}=1$, so apply the criterion to $k-m$.

<!-- qard-id: alg-5961afc179fc121b6155 -->
> [!qard]- Why are $1,g,\ldots,g^{n-1}$ distinct when $o(g)=n$?
> Equal powers would have exponents congruent modulo $n$; two distinct exponents in that range cannot be congruent.

<!-- qard-id: alg-9ad2c718dd189b857b77 -->
> [!qard]- Why would a nonzero identity exponent make a cyclic subgroup finite?
> Its absolute value gives a positive identity exponent, allowing every exponent to be reduced to finitely many residues.

<!-- qard-id: alg-07b06d9608aedc2bd2fa -->
> [!qard]- What is the relationship between element order and cyclic-subgroup size?
> $o(g)=|\langle g\rangle|$, including the infinite case.

### Properties and Generators of Cyclic Groups

<!-- qard-id: alg-473c81c7307be3e1a2c0 -->
> [!qard]- Why is every cyclic group abelian?
> $g^kg^m=g^{k+m}=g^{m+k}=g^mg^k$.

<!-- qard-id: alg-78626c3ded9caacb3a7f -->
> [!qard]- What does the subgroup theorem for cyclic groups say?
> Every subgroup of a cyclic group is cyclic.

<!-- qard-id: alg-55dc871b02d5de0cb5eb -->
> [!qard]- How is the trivial subgroup handled in the proof that every cyclic-group subgroup is cyclic?
> $\{1\}=\langle1\rangle$.

<!-- qard-id: alg-1c482a05aeeaef85c77b -->
> [!qard]- For a nontrivial $H\le\langle g\rangle$, which exponent is chosen to prove that $H$ is cyclic?
> The smallest positive $m$ with $g^m\in H$; such an exponent exists by taking a nonidentity power and inverting if necessary.

<!-- qard-id: alg-aa1b34b28a701041b233 -->
> [!qard]- How does division with remainder prove $H=\langle g^m\rangle$ for the minimal positive exponent $m$?
> If $g^s\in H$, write $s=qm+r$, $0\le r<m$. Then $g^r=(g^m)^{-q}g^s\in H$, so minimality forces $r=0$.

<!-- qard-id: alg-15bb891017a8574d0b39 -->
> [!qard]- What are all subgroups of $(\mathbb Z,+)$?
> $m\mathbb Z$ for $m\ge0$.

<!-- qard-id: alg-5ca75265dee98686a8a3 -->
> [!qard]- Which powers generate $G=\langle g\rangle$ when $|G|=n$?
> $g^k$ generates $G$ exactly when $\gcd(k,n)=1$.

<!-- qard-id: alg-a0fb9e41101c339a56a2 -->
> [!qard]- Why does $\langle g^k\rangle=\langle g\rangle$ imply $\gcd(k,n)=1$ when $o(g)=n$?
> Write $g=(g^k)^m$. Then $n\mid(1-km)$, yielding $1=km+qn$; Bézout's criterion gives gcd $1$.

<!-- qard-id: alg-2df0b0df85aeddb548f9 -->
> [!qard]- How does Bézout prove that $\gcd(k,n)=1$ makes $g^k$ a generator?
> Choose $xk+yn=1$. Then $g=(g^k)^x(g^n)^y=(g^k)^x$, so $\langle g^k\rangle$ contains the original generator.

<!-- qard-id: alg-19372a7601476c4a1a8c -->
> [!qard]- Which elements generate the additive group $\mathbb Z_n$?
> Exactly the classes $\overline k$ with $\gcd(k,n)=1$.

<!-- qard-id: alg-a95dabaa5ff05c16db5c -->
> [!qard]- What are the only generators of an infinite cyclic group $\langle g\rangle$?
> $g$ and $g^{-1}$.

<!-- qard-id: alg-ebae86f3fa84688e6062 -->
> [!qard]- Why can an infinite cyclic group have no generators other than $g^{\pm1}$?
> If $g=(g^k)^m$, equality of powers forces $km=1$, so $k=\pm1$.

### Fundamental Theorem of Finite Cyclic Groups

<!-- qard-id: alg-1bdee7a79d74ba25847c -->
> [!qard]- What is the fundamental theorem of finite cyclic groups?
> If $G=\langle g\rangle$ has order $n$, its subgroups correspond to positive divisors of $n$; for each $k\mid n$ there is exactly one subgroup of order $k$, namely $\langle g^{n/k}\rangle$.

<!-- qard-id: alg-b903b3b30c20a5e16ae2 -->
> [!qard]- Which exponents can be used to describe every subgroup of a finite cyclic group of order $n$?
> Each subgroup is $\langle g^d\rangle$ for a positive divisor $d$ of $n$.

<!-- qard-id: alg-b37aac8b16cd677d7554 -->
> [!qard]- What is $o(g^d)$ when $o(g)=n$ and $d$ is a positive divisor of $n$?
> $n/d$.

<!-- qard-id: alg-98bcef9955c5ced5c318 -->
> [!qard]- Why does $(g^d)^{n/d}=1$ show only an upper bound for the order?
> The order is the least positive identity exponent; one must also exclude smaller exponents.

<!-- qard-id: alg-9e84b0299ba1922700d9 -->
> [!qard]- How do you prove that $o(g^d)=n/d$ when $d\mid n$?
> If $(g^d)^r=1$ with $r>0$, then $n\mid dr$. Writing $n=dk$ yields $k\mid r$, so no positive identity exponent is smaller than $k=n/d$.

<!-- qard-id: alg-cd4759837522993ed3eb -->
> [!qard]- For $o(g)=n$, why does $d=\gcd(m,n)$ give $\langle g^m\rangle\subseteq\langle g^d\rangle$?
> $d\mid m$, so $g^m$ is a power of $g^d$.

<!-- qard-id: alg-73d58127ea0a4510b0a4 -->
> [!qard]- How does Bézout give the reverse inclusion $\langle g^d\rangle\subseteq\langle g^m\rangle$, with $d=\gcd(m,n)$?
> Choose $d=xm+yn$. Then $g^d=(g^m)^x(g^n)^y=(g^m)^x\in\langle g^m\rangle$.

<!-- qard-id: alg-be1e09ecbc1047355a37 -->
> [!qard]- How is the trivial subgroup included in the divisor description of a finite cyclic group's subgroups?
> $\{1\}=\langle g^n\rangle$, corresponding to divisor $d=n$.

<!-- qard-id: alg-571e8267a9bacf039f88 -->
> [!qard]- Why does every subgroup order divide the order of a finite cyclic group?
> Each subgroup is $\langle g^d\rangle$ with $d\mid n$, and its order is $n/d$.

<!-- qard-id: alg-f5408a71341eb0f93c89 -->
> [!qard]- Why is the subgroup of each divisor order unique in a finite cyclic group?
> A subgroup of order $k$ must have form $\langle g^d\rangle$ with $k=n/d$, forcing $d=n/k$.

<!-- qard-id: alg-2f721f109d6139216e21 -->
> [!qard]- What is the general order formula for $g^m$ when $o(g)=n$?
> $o(g^m)=n/\gcd(m,n)$, for every integer $m$.

<!-- qard-id: alg-f4d731e272f2e898504b -->
> [!qard]- How is a cyclic subgroup generated by an arbitrary power simplified?
> $\langle g^m\rangle=\langle g^{\gcd(m,n)}\rangle$ when $o(g)=n$.

<!-- qard-id: alg-6a8e9eab2a44a7491d9c -->
> [!qard]- What is the additive order of $\overline m\in\mathbb Z_n$?
> $n/\gcd(m,n)$.

<!-- qard-id: alg-aca840c538f3dd6251ac -->
> [!qard]- For positive divisors $k,m$ of $n$, when is $\langle g^m\rangle\subseteq\langle g^k\rangle$?
> Exactly when $k\mid m$.

<!-- qard-id: alg-bc47f2e2fa0fc1487c1a -->
> [!qard]- Why does inclusion $\langle g^m\rangle\subseteq\langle g^k\rangle$ force $k\mid m$ for divisors $k,m$ of $n$?
> $g^m=g^{kt}$ gives $n\mid(m-kt)$. Since $k\mid n$, it follows that $k\mid m$.

<!-- qard-id: alg-618629d17eea68cbf214 -->
> [!qard]- Why does $k\mid m$ give $\langle g^m\rangle\subseteq\langle g^k\rangle$?
> Write $m=ku$; then $g^m=(g^k)^u$.

<!-- qard-id: alg-0c53342ffcf61c044d66 -->
> [!qard]- What is the containment criterion for cyclic subgroups with arbitrary integer exponents $k,m$?
> $\langle g^m\rangle\subseteq\langle g^k\rangle$ exactly when $\gcd(k,n)\mid\gcd(m,n)$, where $o(g)=n$.

<!-- qard-id: alg-0c7fe551dd0406e486d1 -->
> [!qard]- How do you list all subgroups of a finite cyclic group of order $n$?
> List positive divisors $k\mid n$; for each, write $\langle g^{n/k}\rangle$ of order $k$. Use divisor containment to draw the lattice.

<!-- qard-id: alg-e5c1df4e1ffa86df155b -->
> [!qard]- How are all subgroups of additive $\mathbb Z_n$ written using divisors $d\mid n$?
> $d\mathbb Z_n=\langle\overline d\rangle$, of order $n/d$; $d=n$ gives $\{\overline0\}$.

<!-- qard-id: alg-791302e7021d941cb753 -->
> [!qard]- Which part of the finite cyclic subgroup theorem is special to cyclic groups?
> Uniqueness and existence of a subgroup for every divisor order. Order divisibility extends to all finite groups through Lagrange's theorem.

### Homomorphisms and Isomorphisms

<!-- qard-id: alg-e94b77b0a5dbcc73f3a2 -->
> [!qard]- What is a group homomorphism between groups with operations $\cdot_1$ and $\cdot_2$?
> A map $\varphi:G_1\to G_2$ with $\varphi(a\cdot_1b)=\varphi(a)\cdot_2\varphi(b)$ for all $a,b\in G_1$.

<!-- qard-id: alg-b92ea9b1e987b0bdfb00 -->
> [!qard]- Must a group homomorphism be injective or surjective?
> No; operation preservation alone defines it.

<!-- qard-id: alg-194a47f85e5a06def806 -->
> [!qard]- What is a monomorphism?
> An injective group homomorphism.

<!-- qard-id: alg-f8695c2d39bb3f28c803 -->
> [!qard]- What is an epimorphism in this course's terminology?
> A surjective group homomorphism.

<!-- qard-id: alg-c6e37ee59c250adaf6e7 -->
> [!qard]- What is an isomorphism?
> A bijective group homomorphism; its existence is denoted $G_1\cong G_2$.

<!-- qard-id: alg-c7abc5422955d410fba5 -->
> [!qard]- What is an automorphism of a group?
> An isomorphism from that group to itself.

<!-- qard-id: alg-bc43b0fd64c8254c138f -->
> [!qard]- What must be checked when proving a proposed map is an isomorphism?
> Specify domain and codomain; prove the map is well-defined and bijective; verify operation preservation for arbitrary elements.

<!-- qard-id: alg-8fdeadb383309aa9f967 -->
> [!qard]- Why keep both group operations explicit when checking a homomorphism?
> They may differ; the map must send the domain's operation to the codomain's operation.

<!-- qard-id: alg-f8522e14b1f664f90cfe -->
> [!qard]- What familiar map identifies $(\mathbb R,+)$ with $(\mathbb R^+,\times)$?
> $x\mapsto e^x$, with inverse $y\mapsto\ln y$; exponentiation sends addition to multiplication.

<!-- qard-id: alg-92694afe9d9dfff239b7 -->
> [!qard]- What does the determinant homomorphism send $\mathrm{GL}_n(\mathbb R)$ to?
> $\mathbb R^*$ under multiplication, because $\det(AB)=\det A\det B$.

<!-- qard-id: alg-3c22ac6fcfcbe560fc7c -->
> [!qard]- When is the determinant map on $\mathrm{GL}_n(\mathbb R)$ an isomorphism?
> For $n=1$; for $n\ge2$ it is surjective but not injective.

<!-- qard-id: alg-94fd3ed6d387d244565c -->
> [!qard]- What three basic structures does every group homomorphism preserve?
> Identity, inverses, and all integer powers: $\varphi(1)=1$, $\varphi(g^{-1})=\varphi(g)^{-1}$, and $\varphi(g^k)=\varphi(g)^k$.

<!-- qard-id: alg-307571979e208401d6af -->
> [!qard]- Why must a homomorphism preserve the identity?
> $\varphi(1)=\varphi(1\cdot1)=\varphi(1)\varphi(1)$; cancellation in the codomain yields $\varphi(1)=1$.

<!-- qard-id: alg-096b46c74687c1ff37fd -->
> [!qard]- Why must a homomorphism preserve inverses?
> Applying it to $gg^{-1}=g^{-1}g=1$ makes $\varphi(g^{-1})$ the inverse of $\varphi(g)$.

<!-- qard-id: alg-80af94f12d232f9bb038 -->
> [!qard]- How do you prove that a homomorphism preserves positive powers?
> Induct using $\varphi(g^{k+1})=\varphi(g)\varphi(g^k)$.

<!-- qard-id: alg-faeb5a3a18b7cdcc14b0 -->
> [!qard]- How does power preservation extend to zero and negative exponents?
> The zero case uses identity preservation; for $m>0$, $\varphi(g^{-m})=\varphi((g^m)^{-1})=\varphi(g^m)^{-1}=\varphi(g)^{-m}$.

<!-- qard-id: alg-68fd80144ca3b196d5cd -->
> [!qard]- Why is the identity map on any group an isomorphism?
> It is bijective and directly preserves every product.

<!-- qard-id: alg-cab1fb21cc5d662e3131 -->
> [!qard]- Why is the inverse of an isomorphism a homomorphism?
> Write $u=\varphi(a)$ and $v=\varphi(b)$; then $\varphi^{-1}(uv)=ab=\varphi^{-1}(u)\varphi^{-1}(v)$.

<!-- qard-id: alg-fd537b9af063ef19f796 -->
> [!qard]- Why is a composition of isomorphisms an isomorphism?
> Composition is bijective, and applying the product-preserving equation for each map shows the composite preserves products.

<!-- qard-id: alg-26e7487ab501716a1f72 -->
> [!qard]- Why is group isomorphism an equivalence relation?
> Identity maps give reflexivity, inverse isomorphisms give symmetry, and compositions give transitivity.

<!-- qard-id: alg-6ce91eac19a9bdea6378 -->
> [!qard]- What is $\operatorname{Aut}(G)$, and what operation makes it a group?
> The automorphisms of $G$ under composition; the identity map is its identity and inverse maps give inverses.

<!-- qard-id: alg-47195fd468578672ed95 -->
> [!qard]- Why does $\operatorname{Aut}(G)$ satisfy the group axioms?
> Isomorphism composition gives closure; function composition is associative; the identity map and inverse automorphisms supply identity and inverses.

<!-- qard-id: alg-a0d09b1c1ee3b1de3a8d -->
> [!qard]- How can structural invariants show that two groups are not isomorphic?
> Find a group property preserved by isomorphisms that differs between the two groups.

<!-- qard-id: alg-64705f575e07411a6796 -->
> [!qard]- Which isomorphism invariants are listed in these notes?
> Number of elements, commutativity, cyclicity, element orders, generation by two elements, and every element being a square.

<!-- qard-id: alg-e6c600d487371bb1d0d6 -->
> [!qard]- Why does an isomorphism preserve the number of elements?
> It is a bijection.

<!-- qard-id: alg-2e74aab76c9d2f77dfd0 -->
> [!qard]- Why does an isomorphism preserve commutativity?
> Product preservation transfers $ab=ba$ to the images; surjectivity covers every pair in the codomain, and the inverse gives the converse.

<!-- qard-id: alg-9d8f5e8b3c67ac689047 -->
> [!qard]- Why does an isomorphism preserve cyclicity?
> If $G=\langle g\rangle$, power preservation and surjectivity give $\varphi(G)=\langle\varphi(g)\rangle$.

<!-- qard-id: alg-cd5821712bfc05171ff9 -->
> [!qard]- Why does an isomorphism preserve element orders?
> Identity and power preservation transfer each identity-power relation; the inverse isomorphism transfers it back, preserving the least positive exponent or infinite order.

<!-- qard-id: alg-39ffd3af8c947be99a91 -->
> [!qard]- Why does an isomorphism preserve generation by two elements?
> Images of products and inverses of the generators produce all codomain elements by surjectivity.

<!-- qard-id: alg-38dc04187fbb2667147b -->
> [!qard]- Why does an isomorphism preserve the property that every element is a square?
> Each $g^2$ maps to $\varphi(g)^2$; surjectivity covers the codomain, and the inverse gives the reverse direction.

<!-- qard-id: alg-7f1b5512885ea279789a -->
> [!qard]- Is having the same number of elements sufficient for groups to be isomorphic?
> No. Groups can have equal size but different cyclicity or element orders, as $C_4$ and $K_4$ do.

<!-- qard-id: alg-585601b07c63a82e7714 -->
> [!qard]- Why are $\mathbb Z_4$ and $\mathbb Z_2\times\mathbb Z_2$ not isomorphic?
> The first is cyclic with elements of order $4$; the second is noncyclic and has only element orders $1,2$.

<!-- qard-id: alg-c5593b8a867a2ffdb357 -->
> [!qard]- Which element-order obstruction separates $(\mathbb R,+)$ from $(\mathbb R^*,\times)$?
> $\mathbb R^*$ has the nonidentity order-$2$ element $-1$; $2a=0$ in additive $\mathbb R$ forces $a=0$.

<!-- qard-id: alg-020eee56fa9d0ed84a22 -->
> [!qard]- What is the classification of finite cyclic groups up to isomorphism?
> Every finite cyclic group of order $n$ is isomorphic to $(\mathbb Z_n,+)$; two finite cyclic groups of the same order are isomorphic.

<!-- qard-id: alg-9b27a835f945618de1c4 -->
> [!qard]- What is the classification of infinite cyclic groups up to isomorphism?
> Every infinite cyclic group is isomorphic to $(\mathbb Z,+)$.

<!-- qard-id: alg-308a957a05f03b7683d9 -->
> [!qard]- Which map proves $\mathbb Z_n\cong\langle a\rangle$ when $o(a)=n$?
> $\varphi(\overline i)=a^i$.

<!-- qard-id: alg-c840f147682e0bbf538b -->
> [!qard]- Why is the cyclic classification map $\varphi(\overline i)=a^i$ well-defined?
> Congruent exponents modulo $n$ give the same power of an element of order $n$.

<!-- qard-id: alg-131905bd5f175a03f535 -->
> [!qard]- Why is $\varphi:\mathbb Z_n\to\langle a\rangle$, $\overline i\mapsto a^i$, bijective?
> Every element is a power; the finite equality-of-powers criterion makes distinct residue classes give distinct powers.

<!-- qard-id: alg-54ce4c7d49ac4a8a0568 -->
> [!qard]- Why does the finite cyclic classification map preserve the operation?
> $\varphi(\overline i+\overline j)=a^{i+j}=a^ia^j=\varphi(\overline i)\varphi(\overline j)$.

<!-- qard-id: alg-fc1602747458e3ae4666 -->
> [!qard]- Which map proves $\mathbb Z\cong\langle a\rangle$ when $a$ has infinite order?
> $i\mapsto a^i$; distinct integer exponents give distinct powers, all elements are powers, and exponent addition preserves the operation.
