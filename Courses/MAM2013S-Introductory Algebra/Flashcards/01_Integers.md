---
tags:
  - introductory-algebra
  - flashcards
qard-deck: "Introductory Algebra"
qard-topic: "01 — Integers: Induction, Divisibility, and Modular Arithmetic"
---

# 01 — Integers: Induction, Divisibility, and Modular Arithmetic

**Source note:** [Integers: Induction, Divisibility, and Modular Arithmetic](../01_Integers.md)

Exam recall cards covering concepts, definitions, methods, and qualifications. Worked examples are omitted; general proof methods are retained.

## Contents

- [[#Core Content|Core Content]]
  - [[#Induction|Induction]]
  - [[#Division Algorithm|Division Algorithm]]
  - [[#Greatest Common Divisor, Primes, and Coprime Integers|Greatest Common Divisor, Primes, and Coprime Integers]]
  - [[#Euclidean Algorithm|Euclidean Algorithm]]
  - [[#Prime Factorisation|Prime Factorisation]]
  - [[#Integers Modulo a Modulus|Integers Modulo a Modulus]]
  - [[#Modular Arithmetic|Modular Arithmetic]]
  - [[#Solving Linear Equations and Systems in Modular Arithmetic|Solving Linear Equations and Systems in Modular Arithmetic]]
  - [[#Classical Chinese Remainder Theorem|Classical Chinese Remainder Theorem]]
  - [[#Fermat’s Little Theorem|Fermat’s Little Theorem]]

## Core Content

### Induction

<!-- qard-id: alg-130924c21afdcc8aeadf -->
> [!qard]- What sets do $\mathbb N$ and $\mathbb Z$ denote in this chapter?
> $\mathbb N=\{1,2,3,\ldots\}$; $\mathbb Z=\{\ldots,-2,-1,0,1,2,\ldots\}$.

<!-- qard-id: alg-fc230cc9775a75148006 -->
> [!qard]- What is proof by induction?
> Establish a starting statement and prove that truth at one stage implies truth at the next, giving the result for every permitted stage.

<!-- qard-id: alg-a9843e30416aa2ec24f7 -->
> [!qard]- What is an induction hypothesis?
> The assumed statement $P(k)$ used to prove the next case $P(k+1)$.

<!-- qard-id: alg-d67fb226664fe302a14d -->
> [!qard]- Why is recognizing a pattern not a proof?
> Agreement in observed cases does not establish the statement for every permitted integer.

<!-- qard-id: alg-33d3b44b0ce40fa5e51d -->
> [!qard]- State ordinary mathematical induction.
> If $P(1)$ holds and $P(k)\Rightarrow P(k+1)$ for every $k\ge1$, then $P(n)$ holds for every $n\ge1$.

<!-- qard-id: alg-a436575f2f365986d767 -->
> [!qard]- What steps must an ordinary induction proof contain?
> Explicitly verify the base case, assume $P(k)$ for arbitrary permitted $k$, use it to prove $P(k+1)$, and conclude the universal result.

<!-- qard-id: alg-25795d7b59b0b6dc588c -->
> [!qard]- State induction starting at an arbitrary integer $m$.
> If $P(m)$ holds and $P(k)\Rightarrow P(k+1)$ for every $k\ge m$, then $P(n)$ holds for all integers $n\ge m$.

<!-- qard-id: alg-73301750d0e0803800b3 -->
> [!qard]- How is induction from $m$ obtained by reindexing ordinary induction?
> Define $T(j)=P(m+j-1)$ for $j\ge1$ and apply ordinary induction to $T$.

<!-- qard-id: alg-b4269095ab207f0f3289 -->
> [!qard]- State strong induction starting at $m$.
> If $P(m)$ holds and $P(m),\ldots,P(k)$ together imply $P(k+1)$ for every $k\ge m$, then all $P(n)$ for $n\ge m$ hold.

<!-- qard-id: alg-de2585bfc9b0d9113682 -->
> [!qard]- How do ordinary and strong induction differ in hypothesis?
> Ordinary uses $P(k)$; strong uses all earlier permitted cases $P(m),\ldots,P(k)$. They have equivalent logical strength.

<!-- qard-id: alg-3b3f0181bef4a0d8141e -->
> [!qard]- When is strong induction particularly useful?
> When the next case depends on several earlier cases, possibly nonadjacent ones.

<!-- qard-id: alg-8bf0beac99d61af39502 -->
> [!qard]- How does ordinary induction imply strong induction?
> Apply induction to $T(n)$ asserting that all statements $P(m),\ldots,P(n)$ hold; the strong-induction step extends this cumulative statement.

<!-- qard-id: alg-202300b8b4d7ee9395b8 -->
> [!qard]- What is a prime?
> A natural number $p\ge2$ whose only positive divisors are $1$ and $p$.

<!-- qard-id: alg-47b96247fe7b0f2f8af9 -->
> [!qard]- What is a composite integer?
> An integer $n\ge2$ that is not prime, equivalently $n=ab$ with $2\le a,b<n$.

<!-- qard-id: alg-447b460bba531789adb5 -->
> [!qard]- Is $1$ prime or composite?
> Neither, under the chapter’s definitions.

<!-- qard-id: alg-0a0f46c48dd894ff71d1 -->
> [!qard]- What prime-product existence theorem does strong induction prove?
> Every integer $n\ge2$ is a product of one or more primes.

<!-- qard-id: alg-c1ea9b1d6b921d8155b8 -->
> [!qard]- How does the strong-induction proof of prime-product existence work?
> Base $2$ is prime. For $k+1$, either it is prime or it equals $ab$ with both factors between $2$ and $k$; factor both by the hypothesis and multiply.

<!-- qard-id: alg-f451ea1e038f510ce435 -->
> [!qard]- Does proving prime-product existence establish uniqueness?
> No. Unique prime factorization requires a separate proof.

<!-- qard-id: alg-c9b41447c11e3c9733a1 -->
> [!qard]- What is the well-ordering principle?
> Every nonempty subset of $\mathbb N$ has a least element.

<!-- qard-id: alg-105a2e08d59bacfe6bc9 -->
> [!qard]- Which three principles are equivalent?
> Well-ordering, ordinary induction, and strong induction.

<!-- qard-id: alg-9af0bbf1ec27ff75aa83 -->
> [!qard]- How does well-ordering prove ordinary induction?
> If a failure exists, choose its least index $m$. The base makes $m>1$, and minimality gives $P(m-1)$; the inductive step forces $P(m)$, a contradiction.

<!-- qard-id: alg-2736f2cf4aa98cdb05ac -->
> [!qard]- How does strong induction prove well-ordering?
> For nonempty $X$, induct on the assertion that if $n\in X$ then $X$ has a least element. Either $n$ is least or a smaller member’s inductive statement supplies a least element.

<!-- qard-id: alg-84809148e7835cdfdaf5 -->
> [!qard]- Why does well-ordering extend to nonnegative integers?
> If the set contains zero, zero is least; otherwise it is a nonempty subset of $\mathbb N$.

### Division Algorithm

<!-- qard-id: alg-faf7da1c9b58c9449658 -->
> [!qard]- State the division algorithm with all hypotheses and bounds.
> For every $n\in\mathbb Z$ and integer $d\ge1$, unique integers $q,r$ satisfy $n=qd+r$ and $0\le r<d$.

<!-- qard-id: alg-40579fa999907c887c84 -->
> [!qard]- What are quotient, remainder, and floor?
> $q,r$ in the division identity are quotient/remainder; $\lfloor x\rfloor$ is the largest integer at most $x$.

<!-- qard-id: alg-538957f6277410b70d49 -->
> [!qard]- What set is used to prove division-algorithm existence?
> $X=\{n-td:t\in\mathbb Z,\ n-td\ge0\}$; choose its least member as remainder.

<!-- qard-id: alg-7522b34d13e275426b39 -->
> [!qard]- Why is the set in the division-algorithm existence proof nonempty?
> For $n\ge0$, choose $t=0$. For $n<0$, choose $t=n$, giving $n(1-d)\ge0$ because $d\ge1$.

<!-- qard-id: alg-ac0523b0710a60955046 -->
> [!qard]- Why must the least nonnegative division remainder be less than $d$?
> If $r\ge d$, then $r-d=n-(q+1)d$ is a smaller nonnegative member of the same set, contradicting minimality.

<!-- qard-id: alg-87e97d4faf6162213dd0 -->
> [!qard]- How is uniqueness of quotient and remainder proved?
> Two identities give $(q'-q)d=r-r'$ with $|r-r'|<d$; the only such multiple of $d$ is zero, so $r=r'$ and $q=q'$.

<!-- qard-id: alg-14a3bf8c5240b69ee66c -->
> [!qard]- How are quotient and remainder computed for any integer dividend?
> $q=\lfloor n/d\rfloor$ and $r=n-qd$; verify $0\le r<d$.

<!-- qard-id: alg-4d7b85ea6ab4a2a0a164 -->
> [!qard]- Why is truncating toward zero unsuitable for negative dividends?
> It can give a negative remainder; flooring ensures the division algorithm’s nonnegative remainder bound.

### Greatest Common Divisor, Primes, and Coprime Integers

<!-- qard-id: alg-b122616667952db01974 -->
> [!qard]- What does $d\mid n$ mean in this chapter?
> For nonzero integer $d$, $n=qd$ for some integer $q$; $d$ is a divisor and $n$ a multiple. $d\nmid n$ means this fails.

<!-- qard-id: alg-96dc432623e4979c3682 -->
> [!qard]- Which universal divisibility facts concern $1$ and $0$?
> $1$ divides every integer, and every nonzero integer divides zero.

<!-- qard-id: alg-58d550e4d85cf1424f18 -->
> [!qard]- How does divisibility by positive $d$ relate to the division remainder?
> $d\mid n$ exactly when dividing $n$ by $d$ gives remainder zero.

<!-- qard-id: alg-9ba8482194cc39bad95d -->
> [!qard]- What are an integer linear combination and a common divisor?
> A combination $xm+yn$ with $x,y\in\mathbb Z$; a nonzero integer dividing both inputs.

<!-- qard-id: alg-e0a3c53cdb8b481176be -->
> [!qard]- State the divisibility characterization of $\gcd(m,n)$.
> For $m,n$ not both zero, it is positive, divides both inputs, and is divisible by every common divisor.

<!-- qard-id: alg-1fc08f01d59cc8c4b9cc -->
> [!qard]- What does coprime mean?
> $\gcd(m,n)=1$; neither input has to be prime.

<!-- qard-id: alg-09330006c049365e6b2f -->
> [!qard]- What are the reflexive and transitive divisibility laws?
> Nonzero $n$ divides itself; if $d\mid m$ and $m\mid n$, then $d\mid n$ by multiplying the integer quotient identities.

<!-- qard-id: alg-f492fe094c6dda8b8a9a -->
> [!qard]- What follows if two nonzero integers divide each other?
> $d\mid n$ and $n\mid d$ imply $d=\pm n$, because the two integer quotients multiply to one.

<!-- qard-id: alg-bf4835b09e17f95da4b4 -->
> [!qard]- Why does a common divisor divide every integer linear combination?
> If $n=qd$ and $m=q'd$, then $xn+ym=(xq+yq')d$.

<!-- qard-id: alg-37221b2d6eb610e0fb18 -->
> [!qard]- How can linear combinations constrain a common divisor of two expressions?
> Eliminate their shared unknown by integer multiplication/subtraction; the common divisor must divide the resulting constant.

<!-- qard-id: alg-f6fb83f78b84b5b2ff80 -->
> [!qard]- Do signs change a positive gcd?
> No. Replacing inputs by their absolute values preserves their positive common divisors.

<!-- qard-id: alg-460ee0f662700a69dbfa -->
> [!qard]- What is $\gcd(m,0)$, and is $\gcd(0,0)$ included?
> For $m\ne0$, $\gcd(m,0)=|m|$. The pair $(0,0)$ is excluded by the chapter’s definition.

<!-- qard-id: alg-507599a7e6d5f5b6abc4 -->
> [!qard]- State Bézout’s lemma.
> For integers $m,n$ not both zero, the gcd exists and equals $xm+yn$ for some integers $x,y$.

<!-- qard-id: alg-71eb8286ae4a871b1a45 -->
> [!qard]- What well-ordered set is used in Bézout’s proof?
> Positive integer linear combinations $X=\{sm+tn:s,t\in\mathbb Z,\ sm+tn\ge1\}$; it is nonempty since $m^2+n^2>0$ belongs to it.

<!-- qard-id: alg-7f25c8cc4a59d44c6035 -->
> [!qard]- Why does the least positive linear combination in Bézout’s proof divide both inputs?
> Divide each input by that combination. A positive remainder would be a smaller positive linear combination, contradicting minimality, so both remainders are zero.

<!-- qard-id: alg-cea5ac07cc2e1cf75c96 -->
> [!qard]- Why does every common divisor divide Bézout’s chosen least combination?
> It divides both original integers and therefore every integer linear combination of them.

<!-- qard-id: alg-aca2fec431a5dd33e19e -->
> [!qard]- What is the Bézout characterization of coprimality?
> $\gcd(m,n)=1$ exactly when $xm+yn=1$ for some integers $x,y$.

<!-- qard-id: alg-0f3083bdf843ee8be86e -->
> [!qard]- How is the reverse direction of Bézout’s coprimality test proved?
> The positive gcd divides every linear combination, hence divides $1$ and must equal $1$.

<!-- qard-id: alg-0b339f6234083ca280be -->
> [!qard]- Why are consecutive integers coprime?
> $(-1)k+(k+1)=1$ supplies a Bézout combination equal to one.

<!-- qard-id: alg-ceb03f4e82b1f4127980 -->
> [!qard]- What happens to the gcd after dividing both inputs by their gcd $d$?
> $\gcd(m/d,n/d)=1$; divide the Bézout identity $d=xm+yn$ by $d$.

<!-- qard-id: alg-5fb60b16e41046cbf559 -->
> [!qard]- When does a positive linear combination identify the gcd?
> If it also divides both original integers; being a positive linear combination alone is insufficient.

<!-- qard-id: alg-5a9cb3ac956d6217db3a -->
> [!qard]- What coprime product-divisor result holds?
> If $\gcd(m,n)=1$ and both $m\mid k$ and $n\mid k$, then $mn\mid k$.

<!-- qard-id: alg-4dbbea9a0eef52db9c64 -->
> [!qard]- How is the coprime product-divisor result proved using Bézout?
> Write $xm+yn=1$ and $k=qm=pn$; then $k=(xm+yn)k=(xp+yq)mn$.

<!-- qard-id: alg-d2c1d85cd1a205b7dc71 -->
> [!qard]- What coprime cancellation result holds for integer divisibility?
> If $\gcd(m,n)=1$ and $m\mid kn$, then $m\mid k$.

<!-- qard-id: alg-51c2b957c2c185f59afe -->
> [!qard]- How is coprime cancellation proved using Bézout?
> With $xm+yn=1$ and $nk=qm$, write $k=xmk+ynk=(xk+yq)m$.

<!-- qard-id: alg-a2f5921c50b046c6b064 -->
> [!qard]- State Euclid’s lemma.
> For prime $p$, if $p\mid mn$, then $p\mid m$ or $p\mid n$.

<!-- qard-id: alg-d8d31b00db9ec050b36a -->
> [!qard]- How does coprime cancellation prove Euclid’s lemma?
> $\gcd(m,p)$ is either $p$ or $1$. The former gives $p\mid m$; the latter cancels $m$ from $p\mid mn$, giving $p\mid n$.

<!-- qard-id: alg-1be1c28b6564ac30aff7 -->
> [!qard]- How does Euclid’s lemma extend to many factors?
> If a prime divides $m_1\cdots m_r$, it divides at least one factor; prove by induction using the two-factor lemma.

<!-- qard-id: alg-58f241204992ef93462d -->
> [!qard]- Can Euclid’s lemma be assumed for an arbitrary composite divisor?
> No. A composite can divide a product while dividing neither factor; primality is essential.

### Euclidean Algorithm

<!-- qard-id: alg-3a25368f5eb3de4a4567 -->
> [!qard]- What is the Euclidean algorithm?
> Repeated division, replacing a pair by the divisor and remainder until remainder zero; return the last nonzero remainder as gcd.

<!-- qard-id: alg-999847b0c82a7a5d13bf -->
> [!qard]- What is the extended Euclidean or back-substitution method?
> Reverse the remainder equations to express the gcd as an integer linear combination of the original inputs.

<!-- qard-id: alg-caf14403cd85ed25f4f8 -->
> [!qard]- Why does $m=qn+r$ imply $\gcd(m,n)=\gcd(n,r)$?
> A divisor of $m,n$ divides $r=m-qn$; a divisor of $n,r$ divides $m=qn+r$. The pairs have exactly the same common divisors.

<!-- qard-id: alg-a4d13dde8dd1b18cc946 -->
> [!qard]- How should Euclid’s algorithm handle signs and zero inputs?
> Use absolute values; if one input is zero, return the other positive input, excluding the both-zero case.

<!-- qard-id: alg-bab6475965a1ddd03e85 -->
> [!qard]- Why does Euclid’s algorithm terminate?
> Its nonnegative remainders strictly decrease, so well-ordering prevents an infinite decreasing sequence.

<!-- qard-id: alg-fdd5155a2ba776fd282a -->
> [!qard]- Why is the last nonzero remainder the gcd?
> Repeated gcd-preserving replacement reaches $\gcd(r_{t-1},r_t)$ with $r_t\mid r_{t-1}$, so the gcd is $r_t$.

<!-- qard-id: alg-2aa6a0b9908db0fe164b -->
> [!qard]- How do you obtain Bézout coefficients after Euclid’s algorithm?
> Start with the equation producing the final nonzero remainder, then substitute earlier remainder equations until only the original inputs remain.

### Prime Factorisation

<!-- qard-id: alg-430ace3e49206796ee55 -->
> [!qard]- What is prime factorization?
> An expression of an integer $n\ge2$ as a product of primes.

<!-- qard-id: alg-a3faf36a1991938d275b -->
> [!qard]- What is a prime power?
> $p^e$ with prime $p$ and $e\ge1$, having exactly one distinct prime divisor.

<!-- qard-id: alg-4d98e512f5e5a7bafce4 -->
> [!qard]- What is a square-free integer?
> An integer whose prime factorization has no repeated prime factor: every exponent is one.

<!-- qard-id: alg-f23f0279df45cdfb9ab6 -->
> [!qard]- Is every prime square-free?
> Yes. Its prime factorization consists of that prime to exponent one.

<!-- qard-id: alg-dd6d5c3ff294d44951cd -->
> [!qard]- What is the least common multiple of positive integers?
> A positive common multiple dividing every other common multiple.

<!-- qard-id: alg-8970084436f797008838 -->
> [!qard]- State the prime factorization theorem.
> Every integer $n\ge2$ is a product of primes, uniquely up to factor order.

<!-- qard-id: alg-4dfc538bb5945079a658 -->
> [!qard]- What is the uniqueness proof’s least-counterexample strategy?
> Choose the smallest integer with two distinct prime factorizations; Euclid’s lemma identifies a shared prime, and cancelling it gives a smaller counterexample, a contradiction.

<!-- qard-id: alg-4758bc11e9665ea639bb -->
> [!qard]- Why must a prime dividing another prime equal it?
> The latter prime’s only positive divisors are one and itself, and the former is at least two.

<!-- qard-id: alg-e8fcb5c6d485e47cee59 -->
> [!qard]- What form results from grouping equal factors in unique prime factorization?
> $n=p_1^{e_1}\cdots p_r^{e_r}$ with distinct primes and $e_i\ge1$, uniquely determined apart from ordering.

<!-- qard-id: alg-c5e1e1bcc6b2134ee64f -->
> [!qard]- How are all positive divisors characterized from prime exponents?
> If $n=\prod_i p_i^{e_i}$, divisors are exactly $d=\prod_i p_i^{f_i}$ with $0\le f_i\le e_i$.

<!-- qard-id: alg-0b4fbcf3bcdb60c0cae3 -->
> [!qard]- Why do those bounded-exponent products divide $n$?
> $n/d=\prod_i p_i^{e_i-f_i}$ is an integer.

<!-- qard-id: alg-16ddc789c1b15ebd1797 -->
> [!qard]- Why can a divisor have no extra prime or larger exponent?
> In $n=dc$, uniqueness of prime factorization forces every divisor prime and exponent to fit within $n$’s factorization.

<!-- qard-id: alg-a4aab1ab115846385f06 -->
> [!qard]- How are gcd and lcm computed from prime factorizations?
> Include every prime occurring in any input, use exponent zero where absent, then take minimum exponents for gcd and maximum exponents for lcm.

<!-- qard-id: alg-9423b51362a42427e7fe -->
> [!qard]- Why do minimum exponents give the gcd?
> A common divisor’s exponent cannot exceed any input exponent, and every common divisor divides the minimum-exponent product.

<!-- qard-id: alg-e227a7bbbe69b171d805 -->
> [!qard]- Why do maximum exponents give the lcm?
> Every common multiple must contain all input exponents, so the maximum-exponent product divides every common multiple.

<!-- qard-id: alg-84df7c30345a1b2e50c4 -->
> [!qard]- What identity relates gcd, lcm, and two positive integers?
> $\gcd(a,b)\operatorname{lcm}(a,b)=ab$.

<!-- qard-id: alg-eafadb8fc5e7393d3ac8 -->
> [!qard]- Why does the gcd-lcm product identity hold for two inputs?
> For each prime, the minimum and maximum of two exponents sum to their total, giving identical prime exponents on both sides.

<!-- qard-id: alg-10240dbb3f52437a6708 -->
> [!qard]- Does the gcd-lcm product identity generally extend to three or more inputs?
> No. The sum of all exponents need not equal their minimum plus maximum.

<!-- qard-id: alg-1f7feae42d568d0922a7 -->
> [!qard]- How do prime-factorization and Euclidean gcd methods differ?
> Factorization needs prime exponents and directly gives gcd/lcm; Euclid needs only division and yields Bézout coefficients by back-substitution.

<!-- qard-id: alg-8a5862d40ad6d5cfe553 -->
> [!qard]- How can lcm be computed from Euclid’s gcd for positive $a,b$?
> $\operatorname{lcm}(a,b)=ab/\gcd(a,b)$.

<!-- qard-id: alg-8cbec526eab385bbeff0 -->
> [!qard]- State Euclid’s theorem about primes.
> There are infinitely many primes.

<!-- qard-id: alg-8f9672866efd90720105 -->
> [!qard]- What is Euclid’s proof of infinitely many primes?
> Assume a finite list $p_1,\ldots,p_r$ and form $M=1+p_1\cdots p_r$. A prime divisor of $M$ is listed and also divides the product, hence divides one, a contradiction.

<!-- qard-id: alg-2b8f0f5d96a10ace36c1 -->
> [!qard]- Must the product-plus-one number in Euclid’s proof itself be prime?
> No. The proof only needs it to have a prime divisor.

### Integers Modulo a Modulus

<!-- qard-id: alg-f64547d0aa3fa6c707e3 -->
> [!qard]- What does $a\equiv b\pmod n$ mean?
> For modulus $n\ge2$, $n\mid(a-b)$; the integers have the same remainder on division by $n$.

<!-- qard-id: alg-cd54ea0885d9d626403e -->
> [!qard]- How does congruence differ from integer equality?
> Congruent integers can differ by a nonzero multiple of the modulus; they need not be equal.

<!-- qard-id: alg-3376763df99c53f22daa -->
> [!qard]- What is an equivalence relation?
> A relation that is reflexive, symmetric, and transitive.

<!-- qard-id: alg-c1d9a20025dc3ac684a6 -->
> [!qard]- What is a residue class modulo $n$?
> $[a]_n=\{x\in\mathbb Z:x\equiv a\pmod n\}=\{a+kn:k\in\mathbb Z\}$.

<!-- qard-id: alg-2973e01f01a3db4df909 -->
> [!qard]- What is a representative of a residue class?
> Any integer belonging to the class and used to name it; the source also calls it a generator of that class.

<!-- qard-id: alg-8eead132d78c07da3aab -->
> [!qard]- What is $\mathbb Z_n$?
> The set of all residue classes modulo $n$, rather than a set of arbitrary individual integer representatives.

<!-- qard-id: alg-35971cd08661b2ba3cbe -->
> [!qard]- How does parity relate to congruence?
> Modulo two, integers are congruent exactly when they are both even or both odd.

<!-- qard-id: alg-d9bb4bc2d352c88102a2 -->
> [!qard]- What does congruence modulo $10^k$ imply for positive integers?
> Their last $k$ decimal digits agree, allowing leading zeros within that final block.

<!-- qard-id: alg-af29c8a88bcf36d7c658 -->
> [!qard]- What happens modulo one and under the stated extension modulo zero?
> Modulo one all integers are congruent. If $0\mid c$ means $c=0$, modulo-zero congruence is equality. The chapter otherwise uses $n\ge2$.

<!-- qard-id: alg-095c9090ca6ae0017923 -->
> [!qard]- How does a modular clock represent congruence?
> Whole turns add multiples of the modulus and return to the same residue; on a twelve-hour clock label twelve represents residue zero.

<!-- qard-id: alg-1fd9238e1228ef77e845 -->
> [!qard]- Why is congruence reflexive?
> $n\mid(a-a)=0$.

<!-- qard-id: alg-0a9f5353be23fbb3b6e4 -->
> [!qard]- Why is congruence symmetric?
> If $n\mid(a-b)$, then $n$ also divides its negative $b-a$.

<!-- qard-id: alg-22b897a73a994d14fffe -->
> [!qard]- Why is congruence transitive?
> Divisibility of $a-b$ and $b-c$ implies divisibility of their sum $a-c$.

<!-- qard-id: alg-c674900ad1e0741144b5 -->
> [!qard]- When are two residue classes equal?
> $[a]_n=[b]_n$ exactly when $a\equiv b\pmod n$.

<!-- qard-id: alg-652617b10e40b91412ab -->
> [!qard]- Why does congruence of representatives imply equality of their classes?
> Transitivity puts every member of either class in the other; conversely class equality puts $a$ in $[b]_n$.

<!-- qard-id: alg-29d7adba078e3be290b5 -->
> [!qard]- What standard representatives name all classes in $\mathbb Z_n$?
> $[0]_n,[1]_n,\ldots,[n-1]_n$, exactly $n$ distinct classes.

<!-- qard-id: alg-7b11a8ccb5c00ac6b0ac -->
> [!qard]- Why does every residue class have a unique representative in $0\le r<n$?
> Division gives existence. Two such representatives differ by a multiple of $n$ of absolute value below $n$, hence must be equal.

<!-- qard-id: alg-167d322508cd2699d98d -->
> [!qard]- How do a class, an arbitrary representative, and its standard remainder differ?
> A class contains infinitely many integers; any can name it. Its unique standard representative is their common remainder and need not equal the chosen arbitrary representative.

### Modular Arithmetic

<!-- qard-id: alg-a23c57b6ae9d5513948a -->
> [!qard]- How are addition and multiplication defined on residue classes?
> $[a]_n+[b]_n=[a+b]_n$ and $[a]_n[b]_n=[ab]_n$.

<!-- qard-id: alg-3ec00a170b89ad2e766a -->
> [!qard]- What does it mean for a class operation to be well-defined?
> Its result is independent of the chosen representatives of the input classes.

<!-- qard-id: alg-4f679b075cf6676e504c -->
> [!qard]- How is modular addition proved well-defined?
> If $a_1\equiv a_2$ and $b_1\equiv b_2$, their sum difference is $(a_1-a_2)+(b_1-b_2)$, divisible by $n$.

<!-- qard-id: alg-f3ea5e528bbb415f7f1b -->
> [!qard]- How is modular multiplication proved well-defined?
> $a_1b_1-a_2b_2=(a_1-a_2)b_1+a_2(b_1-b_2)$, divisible by $n$ when corresponding representatives are congruent.

<!-- qard-id: alg-9bf82a16f88ae18a84c9 -->
> [!qard]- Why can congruent bases be substituted in positive powers?
> Repeated application of multiplication compatibility gives $a_1^m\equiv a_2^m\pmod n$ for $m\ge1$.

<!-- qard-id: alg-579bd4d93f4b8989ef7b -->
> [!qard]- What do bars, zero, unity, and additive inverse denote in $\mathbb Z_n$?
> Bars denote classes; $\overline0$ is additive identity, $\overline1$ multiplicative identity, and $-\overline a=\overline{-a}$.

<!-- qard-id: alg-0b5cd9ce4205bb6fa927 -->
> [!qard]- What are an idempotent and a zero divisor?
> An idempotent satisfies $x^2=x$. A zero divisor is nonzero and multiplies some nonzero element to zero.

<!-- qard-id: alg-82877f3bb71936f69312 -->
> [!qard]- What is a Cayley table, and how is a modular operation table read?
> A table of all pairwise operation results; apply the row element first and column element second, reducing the result to its standard representative.

<!-- qard-id: alg-117d4cc6f3354a8b1f43 -->
> [!qard]- How can a known modular power cycle reduce a large exponent?
> If $a^t\equiv1\pmod n$, write $e=qt+r$ and use $a^e\equiv a^r\pmod n$.

<!-- qard-id: alg-0b12b01cab3cb8d67b5a -->
> [!qard]- Which addition and multiplication laws hold in $\mathbb Z_n$?
> Both are commutative and associative; zero and one are their respective identities; every class has an additive inverse; multiplication distributes over addition.

<!-- qard-id: alg-2f8ef9ddd5320187ab0e -->
> [!qard]- How are modular algebraic laws proved from integer laws?
> Apply the class-operation definitions to corresponding integer identities, relying on well-definedness.

<!-- qard-id: alg-15fedf6591a24e706d9c -->
> [!qard]- Does every modular class have a multiplicative inverse?
> No. Unlike additive inverses, multiplicative inverses require a coprimality condition.

<!-- qard-id: alg-f20e2f57e6ac1eb9cea0 -->
> [!qard]- Why can nontrivial idempotents and nonzero zero divisors occur modulo a composite?
> Modular products can equal zero without a factor being zero, so integer zero-product reasoning does not carry over generally.

<!-- qard-id: alg-b47dfba6d0b70f149b9b -->
> [!qard]- Can a nonzero modular factor always be cancelled?
> No. Nonzero need not mean invertible for a composite modulus; cancellation is valid for invertible factors.

### Solving Linear Equations and Systems in Modular Arithmetic

<!-- qard-id: alg-dd7249dfed8b732f0b69 -->
> [!qard]- What is a multiplicative inverse in $\mathbb Z_n$?
> A class $\overline b$ with $\overline a\overline b=\overline b\overline a=\overline1$, denoted $\overline a^{-1}$.

<!-- qard-id: alg-ce38200a14918c048853 -->
> [!qard]- What is a linear congruence?
> $ax\equiv c\pmod n$, equivalently $\overline a\,\overline x=\overline c$ in $\mathbb Z_n$.

<!-- qard-id: alg-4286e1b22459c6f0b844 -->
> [!qard]- What do simultaneous modular linear equations require?
> The same unknown classes must satisfy every equation together; congruence and residue-class notation express the same conditions.

<!-- qard-id: alg-0dc5dee555e30bae0ec8 -->
> [!qard]- How do same-modulus class equations differ from different-modulus congruences?
> Same-modulus equations involve unknowns in one $\mathbb Z_n$; different moduli describe conditions on the same integer represented in different class systems.

<!-- qard-id: alg-d1ba8417fd2c72e4d644 -->
> [!qard]- When does $\overline a$ have a multiplicative inverse modulo $n$?
> Exactly when $\gcd(a,n)=1$.

<!-- qard-id: alg-6e66850f115769ed52d6 -->
> [!qard]- How does Bézout prove the modular inverse criterion?
> An inverse gives $ba\equiv1\pmod n$, equivalently $1=ba+qn$; such an identity exists exactly when the gcd is one.

<!-- qard-id: alg-195cb602e1c44d30427f -->
> [!qard]- How do you compute an inverse using extended Euclid?
> Compute $\gcd(a,n)$; if one, back-substitute to $1=ba+qn$, reduce $b$ modulo $n$, and verify $ab\equiv1$.

<!-- qard-id: alg-d543b892e899274b4dd3 -->
> [!qard]- What does self-inverse mean for a modular unit?
> Its inverse equals itself, equivalently its square is unity.

<!-- qard-id: alg-5d4889d5abc3a6d7a765 -->
> [!qard]- Which three statements are equivalent for $n\ge2$?
> Every nonzero class is invertible; there are no nonzero zero divisors; and $n$ is prime.

<!-- qard-id: alg-d2282cdd6ed9815a12ef -->
> [!qard]- Why do inverses rule out nonzero zero divisors?
> If $\overline a\overline b=0$ and $\overline a\ne0$, multiply by its inverse to obtain $\overline b=0$.

<!-- qard-id: alg-2826c3d0e7649c3efc58 -->
> [!qard]- Why does a composite modulus yield nonzero zero divisors?
> Write $n=ab$ with $2\le a,b<n$; their nonzero classes multiply to $\overline n=0$.

<!-- qard-id: alg-d85df96cd559195c5082 -->
> [!qard]- Why is every nonzero class invertible for a prime modulus?
> A representative not divisible by prime $p$ is coprime to $p$, so the inverse criterion applies.

<!-- qard-id: alg-d6e6a8e422cf976b4fdf -->
> [!qard]- When does $ax\equiv c\pmod n$ have the guaranteed unique solution class in the notes?
> If $\gcd(a,n)=1$, then for every $c$ there is a unique solution $x\equiv bc\pmod n$, where $ba\equiv1$.

<!-- qard-id: alg-931d7d7ce9622b88efcf -->
> [!qard]- Why is the solution unique when $a$ is coprime to $n$?
> Two solutions give $n\mid a(x_1-x_2)$; coprime cancellation yields $n\mid(x_1-x_2)$.

<!-- qard-id: alg-13604aff1b2b63a709fa -->
> [!qard]- What linear-congruence corollary holds for a prime $p$?
> If $p\nmid a$, then $ax\equiv c\pmod p$ is solvable with one solution class.

<!-- qard-id: alg-d9a8e203b120532aefce -->
> [!qard]- How does one solution class differ from one integer solution?
> A class contains infinitely many integer solutions $x=x_0+nk$, even when the class solution is unique.

<!-- qard-id: alg-8083830b0a410b3ef48e -->
> [!qard]- What can happen when a linear-congruence coefficient is not invertible?
> Inverse multiplication is unavailable; the equation may have multiple solution classes or no solution.

<!-- qard-id: alg-98c0c5795724f1e9ab95 -->
> [!qard]- What is the general method for a modular linear system by elimination?
> Multiply/subtract equations to eliminate a variable, solve the remaining congruence with a valid inverse, substitute back, and verify every original equation.

<!-- qard-id: alg-a415839621e32b4368dc -->
> [!qard]- What must be checked before each division or cancellation in modular elimination?
> The factor is invertible; modulo a prime every nonzero factor is invertible, but this fails generally for composite moduli.

### Classical Chinese Remainder Theorem

<!-- qard-id: alg-640ab31a68d9adf77061 -->
> [!qard]- What are simultaneous congruences?
> Conditions a single integer must satisfy at the same time, possibly using different moduli.

<!-- qard-id: alg-cce6574832d7e5725cc0 -->
> [!qard]- State the classical two-modulus Chinese remainder theorem.
> For coprime $m,n\ge2$, $x\equiv s\pmod m$ and $x\equiv t\pmod n$ have a common solution, unique modulo $mn$.

<!-- qard-id: alg-b04b31547f6af919e45d -->
> [!qard]- What coprime-divisor lemma is needed for CRT uniqueness?
> If $\gcd(a,b)=1$ and both $a,b$ divide $c$, then $ab\mid c$.

<!-- qard-id: alg-63c09de2399f86fffa55 -->
> [!qard]- Why is coprimality essential to multiplying divisor conditions?
> Shared factors can make both integers divide $c$ without their product dividing it; Bézout’s identity for one is unavailable.

<!-- qard-id: alg-8af245ea6f31bf38c193 -->
> [!qard]- How is a CRT solution constructed by substitution?
> Write $x=s+mk$, solve $mk\equiv t-s\pmod n$ using the inverse of $m$, then substitute a representative of $k$.

<!-- qard-id: alg-35264c196a46c4217341 -->
> [!qard]- Why does the coefficient in the CRT substitution have an inverse?
> The hypothesis $\gcd(m,n)=1$ makes $m$ invertible modulo $n$.

<!-- qard-id: alg-5ae79fbee877b0e3c2d8 -->
> [!qard]- How is CRT uniqueness modulo $mn$ proved?
> Two common solutions differ by a multiple of both $m$ and $n$; the coprime-divisor lemma makes their difference a multiple of $mn$.

<!-- qard-id: alg-fb353f98607de851c783 -->
> [!qard]- What are all integer solutions once a CRT solution $x_0$ is known?
> $x=x_0+mn\ell$ for $\ell\in\mathbb Z$; adding a multiple of $mn$ preserves both congruences.

<!-- qard-id: alg-06c275cd23c7ccc8e68c -->
> [!qard]- How can a congruence with a coefficient be prepared for classical CRT?
> If the coefficient is invertible modulo its modulus, multiply by its inverse to obtain a direct congruence for $x$, then check coprimality of the moduli.

### Fermat’s Little Theorem

<!-- qard-id: alg-f9aafcf1316daec451d5 -->
> [!qard]- State Fermat’s little theorem with its hypotheses.
> If $p$ is prime and $p\nmid a$, then $a^{p-1}\equiv1\pmod p$.

<!-- qard-id: alg-c76ebdce342f1c1be5df -->
> [!qard]- What is factorial?
> For positive integer $r$, $r!=1\cdot2\cdots r$.

<!-- qard-id: alg-d0d4beb917559947168f -->
> [!qard]- Why does multiplication by a nonzero class permute the nonzero classes in $\mathbb Z_p$?
> It is invertible, so products are nonzero and pairwise distinct; $p-1$ such products must cover all $p-1$ nonzero classes.

<!-- qard-id: alg-16d7b970ecece1386cd3 -->
> [!qard]- What equation results from multiplying all those permuted nonzero classes?
> $a^{p-1}(p-1)!\equiv(p-1)!\pmod p$.

<!-- qard-id: alg-294cb0d0eeeee4cc2aaa -->
> [!qard]- Why may $(p-1)!$ be cancelled in Fermat’s proof?
> No factor is divisible by $p$; Euclid’s lemma gives $p\nmid(p-1)!$, making its class invertible.

<!-- qard-id: alg-810ce412ede61d9b9cdc -->
> [!qard]- State the power corollary of Fermat’s theorem.
> For prime $p$, every integer $a$, and $k\ge1$, $a^{p^k}\equiv a\pmod p$.

<!-- qard-id: alg-82b3c51cf044d67052a0 -->
> [!qard]- Why does $a^p\equiv a\pmod p$ hold even if $p\mid a$?
> In that case both sides are zero; otherwise multiply Fermat’s congruence by $a$.

<!-- qard-id: alg-b0aca9e1f2d5322413ab -->
> [!qard]- How is the $a^{p^k}$ corollary proved for all $k$?
> Base $k=1$ is $a^p\equiv a$; raise the previous congruence to the $p$th power and use it again to advance the induction.

<!-- qard-id: alg-e84f1abdc9f95772e273 -->
> [!qard]- How can Fermat reduce a large exponent modulo a prime?
> When $p\nmid a$, write $e=q(p-1)+r$ with $0\le r<p-1$; then $a^e\equiv a^r\pmod p$.

<!-- qard-id: alg-05cb2e56c43c48000104 -->
> [!qard]- What does failure of a Fermat primality check establish?
> For $n\ge2$ and a base coprime to $n$, failure of $a^{n-1}\equiv1\pmod n$ proves $n$ composite.

<!-- qard-id: alg-36bdb279377b59ca8475 -->
> [!qard]- Does passing one Fermat check prove primality?
> No. A composite can pass, so the converse of the theorem cannot be assumed.

<!-- qard-id: alg-63f9441657674b44131b -->
> [!qard]- Why must the base be checked before applying a Fermat test?
> It must be coprime to the candidate; using base ten excludes primes two and five from that hypothesis.
