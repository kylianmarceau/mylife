---
tags:
  - introductory-algebra
---

# Integers: Induction, Divisibility, and Modular Arithmetic

> [!abstract] <span style="color: #b89aff">Chapter reference</span>
> **Subject**: MAM2013S Introductory Algebra  
> **Source**: [Introductory Algebra — 2IA notes](../../Sources/MAM2013S%20-%20Introductory%20algebra/2IA%20notes.pdf), J. Sánchez-Ortega, Chapter 1, printed pages 1–31 (PDF pages 4–34)  
> **Generated**: 2026-10-03  
> **Scope**: The integers chapter only. Arithmetic and typographical slips in the source are corrected in the derivations below.  
> **Related notes**: [Permutations](02_Permutations.md), [Groups](03_Groups.md)

---

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
  - [[#Fermat's Little Theorem|Fermat's Little Theorem]]

---

## Core Content

### Induction

#### Definitions

> **Natural numbers**: In this chapter, $\mathbb N=\{1,2,3,\ldots\}$.

> **Integers**: $\mathbb Z=\{\ldots,-2,-1,0,1,2,\ldots\}$.

> **Proof by induction**: A proof that establishes a starting statement and shows that the truth of a statement at one stage implies its truth at the next stage.

> **Induction hypothesis**: The assumption that the statement $P(k)$ is true, used to prove $P(k+1)$.

> **Prime**: A natural number $p\ge2$ whose only positive divisors are $1$ and $p$.

> **Composite**: An integer $n\ge2$ that is not prime; equivalently, $n=ab$ with $2\le a,b<n$.

> **Well-ordering principle / least integer principle**: Every nonempty subset $X\subseteq\mathbb N$ contains a least element: some $a\in X$ satisfies $a\le x$ for every $x\in X$.

Recognising a pattern suggests a statement; it does not prove that the statement always holds. For example:

| Number of odd terms | Sum | Result |
|---|---|---|
| $1$ | $1$ | $1^2$ |
| $2$ | $1+3$ | $2^2$ |
| $3$ | $1+3+5$ | $3^2$ |
| $4$ | $1+3+5+7$ | $4^2$ |

The $n$th odd positive integer is $2n-1$. The pattern suggests

$$
P(n):\quad 1+3+\cdots+(2n-1)=n^2.
$$

#### Ordinary and general induction

**Principle of mathematical induction**: If $P(1)$ is true and $P(k)\Rightarrow P(k+1)$ for every $k\ge1$, then $P(n)$ is true for every $n\ge1$.

Use this proof structure:

1. **Base step**: Check the first permitted value explicitly.
2. Assume $P(k)$ for an arbitrary permitted $k$.
3. Use that assumption to prove $P(k+1)$.
4. Conclude that induction establishes the statement for every permitted integer.

For the odd-number sum, the base case is $1=1^2$. Assume

$$
1+3+\cdots+(2k-1)=k^2.
$$

Adding the next odd integer gives

$$
\begin{aligned}
1+3+\cdots+(2k-1)+(2k+1)
&=k^2+2k+1\\
&=(k+1)^2.
\end{aligned}
$$

This proves $P(k+1)$, so the identity holds for all $n\ge1$.

**General principle of mathematical induction**: Start at an integer $m$ instead of $1$. If $P(m)$ holds and $P(k)\Rightarrow P(k+1)$ for all $k\ge m$, then $P(n)$ holds for every $n\ge m$.

To derive the version with $m\in\mathbb N$ from ordinary induction, set $T(j)=P(m+j-1)$ for $j\ge1$. Induction on $j$ gives precisely the statements starting at $m$. The same reindexing works for any integer starting point.

#### Strong induction

**Strong induction**: If $P(m)$ holds, and the simultaneous truth of $P(m),P(m+1),\ldots,P(k)$ implies $P(k+1)$ for every $k\ge m$, then $P(n)$ holds for all $n\ge m$.

| Feature | Ordinary induction | Strong induction |
|---|---|---|
| Assumption for the step | $P(k)$ | All of $P(m),\ldots,P(k)$ |
| What must be proved | $P(k+1)$ | $P(k+1)$ |
| Useful dependency | The immediately preceding case | Several earlier cases, possibly not adjacent |
| Logical strength | Equivalent to strong induction | Equivalent to ordinary induction |

Strong induction follows from general induction by applying it to

$$
T(n):\quad P(m),P(m+1),\ldots,P(n)\text{ are all true}.
$$

The base statement $T(m)$ is true. If $T(k)$ holds, the strong-induction assumption gives $P(k+1)$, so $T(k+1)$ holds.

**Prime-product existence**: Every integer $n\ge2$ is a product of one or more primes.

1. The base case is $n=2$, which is itself prime.
2. Assume every integer from $2$ through $k$ is a product of primes.
3. If $k+1$ is prime, its one-factor expression is enough.
4. If $k+1$ is composite, write $k+1=ab$ with $2\le a,b\le k$.
5. The hypothesis applies to both $a$ and $b$. Multiplying their prime products gives a prime product for $k+1$.

The first primes are $2,3,5,7,11,13,\ldots$. The integer $1$ is neither prime nor composite. At this point, the argument proves existence of prime factorisations; uniqueness needs a separate proof.

#### Equivalence with well-ordering

**Theorem 1.5**: Well-ordering, ordinary induction, and strong induction are equivalent.

**Well-ordering implies ordinary induction**:

1. Suppose the base and inductive steps hold, but some statements fail.
2. Form $X=\{n\ge1:P(n)\text{ is false}\}$ and choose its least element $m$.
3. Since $P(1)$ is true, $m>1$.
4. Minimality gives $P(m-1)$, so the inductive step gives $P(m)$.
5. This contradicts $m\in X$. Therefore $X$ is empty.

**Ordinary induction implies strong induction**: Use the cumulative statements $T(n)$ above.

**Strong induction implies well-ordering**: Let $X\subseteq\mathbb N$ be nonempty and define

$$
P(n):\quad n\in X\Rightarrow X\text{ has a least element}.
$$

The base case holds: if $1\in X$, it is the least element. Assume $P(1),\ldots,P(k)$ and suppose $k+1\in X$.

- If nothing in $X$ is smaller than $k+1$, it is the least element.
- Otherwise some $m\in X$ satisfies $m\le k$. Apply $P(m)$ to obtain a least element of $X$.

Strong induction proves every $P(n)$. Since $X$ is nonempty, choose some $n\in X$ and conclude that $X$ has a least element.

Well-ordering also holds for nonempty sets of nonnegative integers: if such a set contains $0$, that is its least element; otherwise apply the principle for $\mathbb N$.

### Division Algorithm

#### Definitions

> **Quotient and remainder**: For an integer $n$ and a positive integer $d$, the unique integers $q,r$ satisfying $n=qd+r$ and $0\le r<d$ are the quotient and remainder when dividing $n$ by $d$.

> **Floor**: $\lfloor x\rfloor$ is the largest integer less than or equal to $x$.

**Division algorithm**: For every $n\in\mathbb Z$ and $d\ge1$, there exist unique $q,r\in\mathbb Z$ such that

$$
n=qd+r,\qquad 0\le r<d.
$$

For example, $22=3\cdot7+1$: division by $7$ gives quotient $3$ and remainder $1$.

#### Proof of existence

Consider

$$
X=\{n-td:t\in\mathbb Z,\ n-td\ge0\}.
$$

1. If $n\ge0$, choose $t=0$, giving $n\in X$.
2. If $n<0$, choose $t=n$. Then $n-nd=n(1-d)\ge0$, so again $X$ is nonempty.
3. By well-ordering, choose the least element $r=n-qd\in X$. Thus $n=qd+r$ and $r\ge0$.
4. If $r\ge d$, then $r-d=n-(q+1)d$ is a smaller nonnegative element of $X$. This is impossible.

Therefore $0\le r<d$.

#### Proof of uniqueness

Suppose $n=qd+r=q'd+r'$ with both remainders between $0$ and $d-1$. Then

$$
(q'-q)d=r-r',\qquad |r-r'|<d.
$$

The only multiple of $d$ with absolute value less than $d$ is $0$. Hence $r=r'$ and then $q=q'$.

#### Computing the quotient and remainder

1. Compute $n/d$.
2. Take $q=\lfloor n/d\rfloor$.
3. Set $r=n-qd$ and check $0\le r<d$.

| Dividend and divisor | Division identity | Quotient | Remainder |
|---|---|---|---|
| $n=-17$, $d=5$ | $-17=(-4)\cdot5+3$ | $-4$ | $3$ |
| $n=4187$, $d=129$ | $4187=32\cdot129+59$ | $32$ | $59$ |

For a negative dividend, flooring matters: $\lfloor-17/5\rfloor=-4$. Truncating toward zero would produce a negative remainder, which does not satisfy this theorem.

### Greatest Common Divisor, Primes, and Coprime Integers

#### Definitions

> **Divisibility**: For integers $n,d$ with $d\ne0$, write $d\mid n$ if $n=qd$ for some $q\in\mathbb Z$. Then $d$ is a divisor of $n$, and $n$ is a multiple of $d$. Write $d\nmid n$ when this fails.

> **Linear combination**: An expression $xm+yn$ with integer coefficients $x,y$.

> **Common divisor**: A nonzero integer dividing both integers under consideration.

> **Greatest common divisor (gcd)**: For $m,n$ not both zero, $d=\gcd(m,n)$ is the positive integer satisfying $d\mid m$, $d\mid n$, and $k\mid d$ for every common divisor $k$ of $m,n$.

> **Coprime / relatively prime**: Integers $m,n$ satisfying $\gcd(m,n)=1$.

For example, $2\mid108$ because $108=2\cdot54$, whereas $5\nmid108$. Every integer is divisible by $1$, and every nonzero integer divides $0$.

For a positive divisor $d$, the division algorithm gives

$$
d\mid n\quad\Longleftrightarrow\quad\text{the remainder of }n\text{ on division by }d\text{ is }0.
$$

#### Divisibility properties and their proofs

**Theorem 1.10**:

| Property | Integer assumptions | Reason |
|---|---|---|
| $n\mid n$ | $n\ne0$ under the definition above | $n=1\cdot n$ |
| $d\mid m$ and $m\mid n\Rightarrow d\mid n$ | Divisors nonzero | $m=qd$, $n=q'm\Rightarrow n=(q'q)d$ |
| $d\mid n$ and $n\mid d\Rightarrow d=\pm n$ | $d,n\ne0$ | $n=qd$, $d=q'n\Rightarrow qq'=1$, so $q=q'=\pm1$ |
| $d\mid n$ and $d\mid m\Rightarrow d\mid(xn+ym)$ | $d\ne0$, $x,y\in\mathbb Z$ | $xn+ym=(xq+yq')d$ |

The last property is often used to eliminate an unknown integer from two expressions. If $d\ge1$ divides both $3k+5$ and $7k+2$, then

$$
d\mid\bigl(7(3k+5)-3(7k+2)\bigr)=29.
$$

Since $29$ is prime, $d=1$ or $d=29$.

#### Understanding the gcd

| Set | Positive divisors |
|---|---|
| Divisors of $36$ | $1,2,3,4,6,9,12,18,36$ |
| Divisors of $84$ | $1,2,3,4,6,7,12,14,21,28,42,84$ |
| Common divisors | $1,2,3,4,6,12$ |

Thus $\gcd(36,84)=12$. Every common divisor divides $12$; the definition requires this property as well as positivity and common divisibility.

Signs do not affect the positive common divisors: $\gcd(-9,15)=3$. Also $\gcd(9,16)=1$, so $9$ and $16$ are coprime even though neither is prime.

For $m\ne0$, $\gcd(m,0)=|m|$. The pair $(0,0)$ is excluded by this chapter's positive-gcd definition.

#### Bézout's lemma

**Bézout's lemma / identity**: For $m,n\in\mathbb Z$ not both zero, the gcd exists and can be written as

$$
\gcd(m,n)=xm+yn\qquad\text{for some }x,y\in\mathbb Z.
$$

**Proof**:

1. Form the set of positive linear combinations
   $$X=\{sm+tn:s,t\in\mathbb Z,\ sm+tn\ge1\}.$$
2. It is nonempty because $m^2+n^2\in X$.
3. Let its least element be $d=xm+yn\ge1$.
4. Every common divisor of $m,n$ divides $d$, by the linear-combination property.
5. Divide $n$ by $d$: $n=qd+r$ with $0\le r<d$. Then
   $$r=n-q(xm+yn)=(-qx)m+(1-qy)n.$$
6. If $r>0$, it is a smaller element of $X$, a contradiction. Hence $r=0$ and $d\mid n$.
7. The same argument with $m$ gives $d\mid m$. All three gcd requirements hold.

#### Consequences of Bézout's lemma

**Corollary 1.15**:

$$
\gcd(m,n)=1\quad\Longleftrightarrow\quad xm+yn=1\text{ for some }x,y\in\mathbb Z.
$$

The forward direction is Bézout. Conversely, the gcd divides the linear combination $1$, so its positivity forces it to equal $1$.

Consecutive integers are coprime because

$$
(-1)k+1(k+1)=1.
$$

**Corollary 1.16**: If $d=\gcd(m,n)$, then

$$
\gcd\left(\frac m d,\frac n d\right)=1.
$$

Indeed, divide a Bézout identity $d=xm+yn$ by $d$ to obtain a linear combination equal to $1$.

> [!warning] <span style="color: #ffc778">A linear combination alone does not identify the gcd</span>
> For example, $12=1\cdot4+1\cdot8$, but $\gcd(4,8)=4$. A positive linear combination is the gcd if it also divides both original integers; merely being a linear combination is insufficient.

**Theorem 1.17**: If $\gcd(m,n)=1$, then

$$
m\mid k,\ n\mid k\Rightarrow mn\mid k,
\qquad
m\mid kn\Rightarrow m\mid k.
$$

To prove the first implication, choose $xm+yn=1$ and write $k=qm=pn$. Then

$$
k=(xm+yn)k=xm(pn)+yn(qm)=(xp+yq)mn.
$$

For the second, write $nk=qm$. Then

$$
k=(xm+yn)k=xmk+y(qm)=(xk+yq)m.
$$

#### Euclid's lemma

**Euclid's lemma**: For a prime $p$,

$$
p\mid mn\Rightarrow p\mid m\text{ or }p\mid n.
$$

The positive divisor $\gcd(m,p)$ of $p$ is either $p$ or $1$. In the first case $p\mid m$. In the second, the coprime cancellation result gives $p\mid n$.

More generally,

$$
p\mid m_1m_2\cdots m_r\Rightarrow p\mid m_i\text{ for at least one }i.
$$

Prove this by induction on $r$: split the product into $(m_1\cdots m_{r-1})m_r$, apply the two-factor result, and use the hypothesis on the shorter product if necessary.

Primality is essential. For example, $6\mid3\cdot4$ but $6\nmid3$ and $6\nmid4$.

### Euclidean Algorithm

#### Definitions

> **Euclidean algorithm**: Repeated division with remainder, replacing a pair by the previous divisor and remainder, until the remainder is zero. The last nonzero remainder is the gcd.

> **Back-substitution / extended Euclidean method**: Reversing the remainder equations to express the gcd as an integer linear combination of the original pair.

**Proposition 1.18**: If $m=qn+r$, then

$$
\gcd(m,n)=\gcd(n,r).
$$

Every common divisor of $m,n$ divides $r=m-qn$. Conversely, every common divisor of $n,r$ divides $m=qn+r$. The two pairs have exactly the same common divisors, so their positive gcds coincide.

For example,

$$
140=6\cdot21+14,\qquad
\gcd(140,21)=\gcd(21,14)=7.
$$

#### Procedure and termination

1. Replace negative inputs by absolute values. If one input is zero, the gcd is the other positive input.
2. For two positive inputs, divide the first by the second.
3. Replace the pair by the divisor and remainder.
4. Repeat until the remainder is zero.
5. Return the last nonzero remainder.

The equations have the form

$$
\begin{aligned}
m&=q_1n+r_1,\\
n&=q_2r_1+r_2,\\
r_1&=q_3r_2+r_3,\\
&\ \vdots\\
r_{t-1}&=q_{t+1}r_t+0.
\end{aligned}
$$

The remainders strictly decrease:

$$
n>r_1>r_2>\cdots>r_t>0.
$$

A strictly decreasing sequence of nonnegative integers cannot continue indefinitely. Repeated use of Proposition 1.18 gives

$$
\gcd(m,n)=\gcd(n,r_1)=\cdots=\gcd(r_{t-1},r_t)=r_t.
$$

#### Computing a gcd and Bézout coefficients

For $268$ and $112$:

$$
\begin{aligned}
268&=2\cdot112+44,\\
112&=2\cdot44+24,\\
44&=1\cdot24+20,\\
24&=1\cdot20+4,\\
20&=5\cdot4+0.
\end{aligned}
$$

The last nonzero remainder is $4$, so $\gcd(268,112)=4$.

Start with the equation producing that remainder, then eliminate each earlier remainder:

$$
\begin{aligned}
4&=24-20\\
 &=24-(44-24)=2\cdot24-44\\
 &=2(112-2\cdot44)-44=2\cdot112-5\cdot44\\
 &=2\cdot112-5(268-2\cdot112)\\
 &=-5\cdot268+12\cdot112.
\end{aligned}
$$

Thus one pair of Bézout coefficients is $x=-5$, $y=12$.

### Prime Factorisation

#### Definitions

> **Prime factorisation**: An expression of an integer $n\ge2$ as a product of primes.

> **Prime power**: An integer $p^e$ with $p$ prime and $e\ge1$; it has only one distinct prime divisor.

> **Square-free integer**: An integer whose prime factorisation has every exponent equal to $1$.

> **Least common multiple (lcm)**: For positive integers $n_1,\ldots,n_r$, the positive common multiple that divides every other common multiple, denoted $\operatorname{lcm}(n_1,\ldots,n_r)$.

#### Prime factorisation theorem

Every integer $n\ge2$ is a product of primes, and the factorisation is unique up to the order of those primes. If

$$
n=p_1p_2\cdots p_r=q_1q_2\cdots q_s,
$$

then $r=s$, and the factors can be relabelled so that $p_i=q_i$ for every $i$.

Existence was proved by strong induction. For **uniqueness**, suppose there is a counterexample and choose the smallest such integer $m$ by well-ordering.

1. Write two different prime factorisations $m=p_1\cdots p_r=q_1\cdots q_s$.
2. Since $p_1\mid q_1\cdots q_s$, Euclid's lemma gives $p_1\mid q_j$ for some $j$.
3. Both are prime, so $p_1=q_j$. Relabel so that $j=1$.
4. Cancel this common prime. The integer $m/p_1<m$ still has two different prime factorisations.
5. This contradicts minimality. A prime itself cannot be a counterexample, so the cancellation concerns a smaller integer at least $2$.

Grouping equal primes gives the unique expression

$$
n=p_1^{e_1}p_2^{e_2}\cdots p_r^{e_r},
\qquad e_i\ge1,
$$

where the $p_i$ are distinct. Examples:

| Integer | Factorisation | Description |
|---|---|---|
| $60$ | $2^2\cdot3\cdot5$ | Three distinct prime divisors |
| $9$ | $3^2$ | Prime power |
| $8$ | $2^3$ | Prime power |
| $6$ | $2\cdot3$ | Square-free |
| $70$ | $2\cdot5\cdot7$ | Square-free |
| $504$ | $2^3\cdot3^2\cdot7$ | Unique factorisation up to order |

Every prime is square-free.

#### Listing positive divisors

**Theorem 1.22**: If $n=\prod_{i=1}^r p_i^{e_i}$, then its positive divisors are exactly

$$
d=\prod_{i=1}^r p_i^{f_i},\qquad 0\le f_i\le e_i.
$$

If the exponent conditions hold, then $n/d=\prod_i p_i^{e_i-f_i}$ is an integer, so $d\mid n$. Conversely, if $n=dc$, uniqueness of prime factorisation forces every prime in $d$ to occur in $n$, with an exponent no larger than its exponent in $n$.

For $12=2^2\cdot3$, choose the exponent of $2$ from $0,1,2$ and the exponent of $3$ from $0,1$:

| Exponent of $2$ | Exponent of $3$ | Divisor |
|---|---|---|
| $0$ | $0$ | $1$ |
| $1$ | $0$ | $2$ |
| $2$ | $0$ | $4$ |
| $0$ | $1$ | $3$ |
| $1$ | $1$ | $6$ |
| $2$ | $1$ | $12$ |

#### Gcd and lcm using prime exponents

Include every prime occurring in any input. Give a prime exponent $0$ where it is absent.

| Calculation | Exponent chosen for each prime | Why |
|---|---|---|
| Gcd | Minimum exponent across the inputs | A common divisor cannot exceed any input's exponent |
| Lcm | Maximum exponent across the inputs | A common multiple must contain every input's exponent |

For positive integers $a_j=\prod_{i=1}^r p_i^{e_{ij}}$, **Theorem 1.25** gives

$$
\gcd(a_1,\ldots,a_s)=\prod_{i=1}^r p_i^{\min_j e_{ij}},
\qquad
\operatorname{lcm}(a_1,\ldots,a_s)=\prod_{i=1}^r p_i^{\max_j e_{ij}}.
$$

These constructions have the required divisibility properties: every common divisor divides the minimum-exponent product, and the maximum-exponent product divides every common multiple.

For $12,20,18$:

| Input | Exponent of $2$ | Exponent of $3$ | Exponent of $5$ |
|---|---|---|---|
| $12=2^2\cdot3^1\cdot5^0$ | $2$ | $1$ | $0$ |
| $20=2^2\cdot3^0\cdot5^1$ | $2$ | $0$ | $1$ |
| $18=2^1\cdot3^2\cdot5^0$ | $1$ | $2$ | $0$ |
| Minimum | $1$ | $0$ | $0$ |
| Maximum | $2$ | $2$ | $1$ |

Hence

$$
\gcd(12,20,18)=2,
\qquad
\operatorname{lcm}(12,20,18)=2^2\cdot3^2\cdot5=180.
$$

**Corollary 1.26**: For two positive integers,

$$
\gcd(a,b)\operatorname{lcm}(a,b)=ab.
$$

For each prime, the minimum and maximum of two exponents add to their sum. Thus both sides have identical prime exponents.

The corresponding identity generally fails for three or more inputs. Here $2\cdot180=360$, whereas $12\cdot20\cdot18=4320$.

| Gcd method | Needed information | Additional result |
|---|---|---|
| Prime factorisation | Prime exponents of the inputs | Gcd and lcm follow from minimum and maximum exponents |
| Euclidean algorithm | Repeated integer division | Back-substitution gives Bézout coefficients; for two positive inputs use $\operatorname{lcm}(a,b)=ab/\gcd(a,b)$ |

#### Infinitely many primes

**Euclid's theorem**: There are infinitely many primes.

Suppose instead that the complete list is $p_1,\ldots,p_r$. Set

$$
M=1+p_1p_2\cdots p_r\ge2.
$$

Prime-product existence guarantees a prime divisor of $M$. It must be some listed $p_i$, which also divides $p_1\cdots p_r$. Therefore it divides their difference $1$, which is impossible.

The number $M$ need not itself be prime. The contradiction uses the existence of a prime divisor of $M$.

### Integers Modulo a Modulus

#### Definitions

> **Congruence modulo $n$**: For $n\ge2$, integers $a,b$ are congruent modulo $n$ if $n\mid(a-b)$. Write $a\equiv b\pmod n$.

> **Modulus**: The integer $n$ specifying the congruence relation.

> **Equivalence relation**: A relation that is reflexive, symmetric, and transitive.

> **Residue class / equivalence class modulo $n$**: $[a]_n=\{x\in\mathbb Z:x\equiv a\pmod n\}$.

> **Representative / generator of a residue class**: Any integer belonging to the class and used to name it. The source calls $a$ a generator of $[a]_n$.

> **Integers modulo $n$**: The set $\mathbb Z_n$ of all residue classes modulo $n$.

Congruence means equality of remainders, rather than equality of integers. Parity is the special case modulo $2$: two integers are congruent modulo $2$ exactly when they are both even or both odd.

| Congruence | Divisibility check |
|---|---|
| $2\equiv5\pmod3$ | $3\mid(2-5)$ |
| $21\equiv16\pmod5$ | $5\mid(21-16)$ |
| $-4\equiv2\pmod6$ | $6\mid(-4-2)$ |

For positive integers, congruence modulo $10$ means the same final digit. Congruence modulo $10^k$ means the same final $k$ digits, allowing leading zeros within those last digits. For example, $533\equiv1433\pmod{100}$.

Modulo $1$, all integers are congruent because $1$ divides every difference. If divisibility is extended by defining $0\mid c$ exactly when $c=0$, congruence modulo $0$ reduces to ordinary equality. The rest of this chapter uses $n\ge2$.

#### Clock interpretation

Starting at three o'clock, four hours later is seven, and seven hours later is ten. Ten hours later is one, since $3+10=13\equiv1\pmod{12}$; twenty-two hours later is also one, since $25\equiv1\pmod{12}$.

![A twelve-hour clock showing three o'clock](../../diagrams/MAM2013S-Introductory%20Algebra/01_Integers/modular-clock.svg)

*The clock recreates the starting position at three o'clock. Whole turns return to the same position, so times that differ by a multiple of twelve represent the same residue class.*

The label $12$ on an ordinary clock represents residue $0$ modulo $12$. A modular clock with $n$ positions represents congruence modulo $n$.

#### Congruence is an equivalence relation

**Theorem 1.32**:

| Property | Statement | Proof |
|---|---|---|
| Reflexive | $a\equiv a\pmod n$ | $n\mid(a-a)=0$ |
| Symmetric | $a\equiv b\pmod n\Rightarrow b\equiv a\pmod n$ | Negate the divisible difference: $b-a=-(a-b)$ |
| Transitive | $a\equiv b\pmod n$, $b\equiv c\pmod n\Rightarrow a\equiv c\pmod n$ | Add the divisible differences: $(a-b)+(b-c)=a-c$ |

#### Residue classes and standard representatives

Unpacking the definition gives

$$
x\in[a]_n
\Longleftrightarrow n\mid(x-a)
\Longleftrightarrow x=a+kn\text{ for some }k\in\mathbb Z.
$$

Thus

$$
[a]_n=\{a+kn:k\in\mathbb Z\}.
$$

Two classes satisfy

$$
[a]_n=[b]_n\quad\Longleftrightarrow\quad a\equiv b\pmod n.
$$

If $a\equiv b$, transitivity shows every member of $[a]_n$ belongs to $[b]_n$ and vice versa. Conversely, equality of the classes puts $a$ in $[b]_n$, giving the congruence.

**Theorem 1.34 and Corollary 1.35**: Every class has exactly one representative $r$ satisfying $0\le r<n$, and

$$
\mathbb Z_n=\{[0]_n,[1]_n,\ldots,[n-1]_n\},
\qquad |\mathbb Z_n|=n.
$$

To obtain the representative, divide $a$ by $n$: $a=qn+r$, so $a\equiv r\pmod n$. If two representatives $r,s$ in this range name the same class, then $n\mid(r-s)$ and $|r-s|<n$, forcing $r=s$.

> [!info] <span style="color: #66b3ff">An integer, a class, and a remainder</span>
> A class contains infinitely many integers, but $\mathbb Z_n$ contains only $n$ classes. An arbitrary representative $a$ may lie outside $0,\ldots,n-1$. The common remainder of the integers in $[a]_n$ is the standard representative $r$, which is not necessarily the integer $a$ itself.

For example,

$$
\mathbb Z_2=\{[0]_2,[1]_2\},
$$

where $[0]_2$ is the set of even integers and $[1]_2$ is the set of odd integers.

To identify $[48]_7$ and $[-16]_7$, compute

$$
48=6\cdot7+6,\qquad -16=(-3)\cdot7+5.
$$

Hence $[48]_7=[6]_7$ and $[-16]_7=[5]_7$.

### Modular Arithmetic

#### Definitions

> **Modular addition and multiplication**: Operations on residue classes defined by $[a]_n+[b]_n=[a+b]_n$ and $[a]_n[b]_n=[ab]_n$.

> **Well-defined operation**: An operation whose result does not depend on which representatives are chosen for the input classes.

> **Zero and unity**: The additive identity $\overline0$ and multiplicative identity $\overline1$ in $\mathbb Z_n$.

> **Additive inverse**: The class $-\overline a=\overline{-a}$ satisfying $\overline a+(-\overline a)=\overline0$.

> **Idempotent**: An element satisfying $x^2=x$.

> **Zero divisor**: A nonzero element that multiplies some nonzero element to give zero.

When the modulus is understood, write $\overline a$ instead of $[a]_n$. Bars represent residue classes, not ordinary integers.

#### Why the operations are well-defined

**Theorem 1.38**: If $a_1\equiv a_2\pmod n$ and $b_1\equiv b_2\pmod n$, then

$$
\begin{aligned}
a_1+b_1&\equiv a_2+b_2\pmod n,\\
a_1b_1&\equiv a_2b_2\pmod n,\\
a_1^m&\equiv a_2^m\pmod n\qquad(m\ge1).
\end{aligned}
$$

For addition, $n$ divides

$$
(a_1+b_1)-(a_2+b_2)=(a_1-a_2)+(b_1-b_2).
$$

For multiplication, it divides

$$
a_1b_1-a_2b_2=(a_1-a_2)b_1+a_2(b_1-b_2).
$$

Repeated use of the multiplication result proves the power result. These facts justify replacing any representative by a congruent integer during a computation.

For example, in $\mathbb Z_6$,

$$
[3]_6+[5]_6=[8]_6=[2]_6.
$$

Using $[9]_6=[3]_6$ gives the same answer:

$$
[9]_6+[5]_6=[14]_6=[2]_6.
$$

#### Addition and multiplication tables for the integers modulo six

Read the row element first and the column element second. Each entry is reduced to its standard representative.

| $+$ | $\overline0$ | $\overline1$ | $\overline2$ | $\overline3$ | $\overline4$ | $\overline5$ |
|---|---|---|---|---|---|---|
| $\overline0$ | $\overline0$ | $\overline1$ | $\overline2$ | $\overline3$ | $\overline4$ | $\overline5$ |
| $\overline1$ | $\overline1$ | $\overline2$ | $\overline3$ | $\overline4$ | $\overline5$ | $\overline0$ |
| $\overline2$ | $\overline2$ | $\overline3$ | $\overline4$ | $\overline5$ | $\overline0$ | $\overline1$ |
| $\overline3$ | $\overline3$ | $\overline4$ | $\overline5$ | $\overline0$ | $\overline1$ | $\overline2$ |
| $\overline4$ | $\overline4$ | $\overline5$ | $\overline0$ | $\overline1$ | $\overline2$ | $\overline3$ |
| $\overline5$ | $\overline5$ | $\overline0$ | $\overline1$ | $\overline2$ | $\overline3$ | $\overline4$ |

| $\times$ | $\overline0$ | $\overline1$ | $\overline2$ | $\overline3$ | $\overline4$ | $\overline5$ |
|---|---|---|---|---|---|---|
| $\overline0$ | $\overline0$ | $\overline0$ | $\overline0$ | $\overline0$ | $\overline0$ | $\overline0$ |
| $\overline1$ | $\overline0$ | $\overline1$ | $\overline2$ | $\overline3$ | $\overline4$ | $\overline5$ |
| $\overline2$ | $\overline0$ | $\overline2$ | $\overline4$ | $\overline0$ | $\overline2$ | $\overline4$ |
| $\overline3$ | $\overline0$ | $\overline3$ | $\overline0$ | $\overline3$ | $\overline0$ | $\overline3$ |
| $\overline4$ | $\overline0$ | $\overline4$ | $\overline2$ | $\overline0$ | $\overline4$ | $\overline2$ |
| $\overline5$ | $\overline0$ | $\overline5$ | $\overline4$ | $\overline3$ | $\overline2$ | $\overline1$ |

These operation tables are also called **Cayley tables**: their entries record every possible pairwise operation.

#### Reducing a large power

To find the remainder when $4^{119}$ is divided by $7$, first find a power that is congruent to $1$:

$$
4^2=16\equiv2\pmod7,\qquad
4^3\equiv2\cdot4=8\equiv1\pmod7.
$$

Divide the exponent by $3$:

$$
119=3\cdot39+2.
$$

Therefore

$$
4^{119}=(4^3)^{39}4^2\equiv1^{39}\cdot2=2\pmod7.
$$

The remainder is $2$. The cycle here is established by direct calculation; a general prime-modulus guarantee appears in [[#Fermat's Little Theorem|Fermat's Little Theorem]].

#### Algebraic laws

**Theorem 1.42**: For elements $\overline a,\overline b,\overline c\in\mathbb Z_n$:

| Law | Addition | Multiplication |
|---|---|---|
| Commutative | $\overline a+\overline b=\overline b+\overline a$ | $\overline a\overline b=\overline b\overline a$ |
| Associative | $\overline a+(\overline b+\overline c)=(\overline a+\overline b)+\overline c$ | $\overline a(\overline b\overline c)=(\overline a\overline b)\overline c$ |
| Identity | $\overline a+\overline0=\overline a$ | $\overline a\overline1=\overline a$ |
| Additive inverse | $\overline a+\overline{-a}=\overline0$ | A multiplicative inverse requires an additional condition |

Distributivity holds:

$$
\overline a(\overline b+\overline c)=\overline a\overline b+\overline a\overline c.
$$

These laws follow by applying the definitions to the corresponding integer identities. For example,

$$
\overline a(\overline b+\overline c)=\overline{a(b+c)}=\overline{ab+ac}=\overline{ab}+\overline{ac}.
$$

#### Differences from integer arithmetic

| Property | In $\mathbb Z$ | In $\mathbb Z_6$ |
|---|---|---|
| Solutions to $x^2=x$ | Only $0,1$, since $x(x-1)=0$ | Also $\overline3^2=\overline9=\overline3$ and $\overline4^2=\overline{16}=\overline4$ |
| Cancellation of a nonzero factor | $ab=ac$, $a\ne0\Rightarrow b=c$ | $\overline4\overline2=\overline4\overline5=\overline2$, although $\overline2\ne\overline5$ |
| Zero-product property | $ab=0\Rightarrow a=0$ or $b=0$ | $\overline2\overline3=\overline0$, although both factors are nonzero |

> [!warning] <span style="color: #ffc778">Check before cancelling</span>
> A nonzero modular element need not be invertible. Cancellation is valid for invertible factors; being nonzero alone is insufficient for a general modulus.

### Solving Linear Equations and Systems in Modular Arithmetic

#### Definitions

> **Multiplicative inverse**: An element $\overline b\in\mathbb Z_n$ such that $\overline a\overline b=\overline b\overline a=\overline1$; write $\overline a^{-1}=\overline b$.

> **Linear congruence**: An equation $ax\equiv c\pmod n$, equivalent to $\overline a\,\overline x=\overline c$ in $\mathbb Z_n$.

> **Simultaneous modular linear equations**: Equations in the same unknown classes, all of which must hold together.

The bar notation and congruence notation express the same conditions:

$$
\begin{cases}
\overline a\,\overline x+\overline b\,\overline y=\overline r,\\
\overline c\,\overline x+\overline d\,\overline y=\overline s
\end{cases}
\text{ in }\mathbb Z_n
\quad\Longleftrightarrow\quad
\begin{cases}
ax+by\equiv r\pmod n,\\
cx+dy\equiv s\pmod n.
\end{cases}
$$

For different moduli, statements about the class of the same integer correspond to simultaneous integer congruences, such as $x\equiv r\pmod n$ and $x\equiv s\pmod m$.

#### Existence and computation of inverses

**Theorem 1.45**:

$$
\overline a\text{ has an inverse in }\mathbb Z_n
\quad\Longleftrightarrow\quad
\gcd(a,n)=1.
$$

Indeed,

$$
\overline b\overline a=\overline1
\Longleftrightarrow ba\equiv1\pmod n
\Longleftrightarrow 1=ba+qn\text{ for some }q\in\mathbb Z.
$$

Bézout's lemma gives exactly the gcd condition. The coefficient of $a$ in an identity $1=ba+qn$ is an inverse representative.

To find an inverse:

1. Use the Euclidean algorithm on $a,n$.
2. If the gcd is not $1$, no inverse exists.
3. Otherwise back-substitute to obtain $1=ba+qn$.
4. Reduce $b$ modulo $n$.
5. Check that $ab\equiv1\pmod n$.

For $\overline{16}\in\mathbb Z_{35}$,

$$
35=2\cdot16+3,\qquad 16=5\cdot3+1,
$$

so

$$
1=16-5(35-2\cdot16)=11\cdot16-5\cdot35.
$$

Thus $\overline{16}^{-1}=\overline{11}$, verified by $16\cdot11=176\equiv1\pmod{35}$.

In $\mathbb Z_9$, an element is invertible exactly when its representative is not divisible by $3$:

| Element | Inverse |
|---|---|
| $\overline1$ | $\overline1$ |
| $\overline2$ | $\overline5$ |
| $\overline4$ | $\overline7$ |
| $\overline5$ | $\overline2$ |
| $\overline7$ | $\overline4$ |
| $\overline8$ | $\overline8$ |

The classes $\overline0,\overline3,\overline6$ have no inverses. The classes $\overline1,\overline8$ are **self-inverse**, meaning their inverses equal themselves.

#### Why prime moduli are special

**Theorem 1.48**: For $n\ge2$, the following are equivalent:

1. Every nonzero element of $\mathbb Z_n$ has an inverse.
2. A product is zero only when at least one factor is zero.
3. The modulus $n$ is prime.

**Proof of the implications**:

- From the first statement, if $\overline a\overline b=\overline0$ and $\overline a\ne\overline0$, multiply by $\overline a^{-1}$ to obtain $\overline b=\overline0$.
- If $n$ were composite, write $n=ab$ with $2\le a,b<n$. Then $\overline a,\overline b$ are nonzero but $\overline a\overline b=\overline n=\overline0$, contradicting the second statement.
- If $n$ is prime and $\overline a\ne\overline0$, then $n\nmid a$, so $\gcd(a,n)=1$. The inverse theorem proves the first statement.

#### Solving one equation

**Theorem 1.49**: If $\gcd(a,n)=1$, then for every integer $c$, the congruence

$$
ax\equiv c\pmod n
$$

has a unique solution class modulo $n$. If $ba\equiv1\pmod n$, then

$$
x\equiv bc\pmod n.
$$

For uniqueness, if $x_1,x_2$ solve the equation, then $n\mid a(x_1-x_2)$. Since $\gcd(a,n)=1$, coprime cancellation gives $n\mid(x_1-x_2)$.

**Corollary 1.50**: For a prime $p$, $ax\equiv c\pmod p$ is solvable whenever $p\nmid a$.

For $16x\equiv9\pmod{35}$, use the inverse $11$:

$$
x\equiv11\cdot9=99\equiv29\pmod{35}.
$$

There is one solution in $\mathbb Z_{35}$, namely $\overline{29}$. The integer solutions are $x=29+35k$, $k\in\mathbb Z$.

If the coefficient has no inverse, multiplication by an inverse is unavailable. Such an equation may still have solutions: for example, $2x\equiv2\pmod6$ has the two solution classes $\overline1,\overline4$. The equation $2x\equiv1\pmod6$ has none, since $2x-1$ is odd and cannot be a multiple of $6$.

#### Solving a system by elimination

Solve in $\mathbb Z_{11}$:

$$
\begin{cases}
5x+8y\equiv2\pmod{11},\\
3x+2y\equiv1\pmod{11}.
\end{cases}
$$

1. Multiply the second equation by $4$:
   $$12x+8y\equiv4\pmod{11}\quad\Longleftrightarrow\quad x+8y\equiv4\pmod{11}.$$
2. Subtract it from the first equation:
   $$4x\equiv-2\equiv9\pmod{11}.$$
3. Find the inverse of $4$. Since $11=2\cdot4+3$ and $4=3+1$,
   $$1=4-(11-2\cdot4)=3\cdot4-11.$$
   Thus $4^{-1}\equiv3\pmod{11}$ and $x\equiv3\cdot9=27\equiv5\pmod{11}$.
4. Substitute into the second equation:
   $$2y\equiv1-3\cdot5=-14\equiv8\pmod{11}.$$
5. Since $2^{-1}\equiv6\pmod{11}$,
   $$y\equiv6\cdot8=48\equiv4\pmod{11}.$$

The solution is $(\overline x,\overline y)=(\overline5,\overline4)$. Checking both equations gives $25+32=57\equiv2$ and $15+8=23\equiv1\pmod{11}$.

Every cancellation above is valid because the relevant nonzero coefficient is invertible modulo the prime $11$.

### Classical Chinese Remainder Theorem

#### Definitions

> **Simultaneous congruences**: Congruences that a single integer must satisfy at the same time, potentially with different moduli.

> **Classical Chinese remainder theorem (CRT)**: For coprime integers $m,n\ge2$, the system $x\equiv s\pmod m$, $x\equiv t\pmod n$ has a common solution, and any two solutions are congruent modulo $mn$.

#### The coprime-divisor lemma

**Lemma 1.53**: If $\gcd(a,b)=1$, $a\mid c$, and $b\mid c$, then $ab\mid c$.

Choose $as+bt=1$ and write $c=ak_1=bk_2$. Then

$$
\begin{aligned}
c&=(as+bt)c\\
 &=(as)(bk_2)+(bt)(ak_1)\\
 &=ab(sk_2+tk_1).
\end{aligned}
$$

The conclusion is $ab\mid c$. Coprimality matters: $4\mid12$ and $6\mid12$, but $24\nmid12$.

#### Existence, construction, and uniqueness

To solve

$$
\begin{cases}
x\equiv s\pmod m,\\
x\equiv t\pmod n,
\end{cases}
\qquad \gcd(m,n)=1,
$$

proceed as follows:

1. Write every solution of the first congruence as $x=s+mk$.
2. Substitute into the second: $mk\equiv t-s\pmod n$.
3. Since $\gcd(m,n)=1$, find the inverse of $m$ modulo $n$ and solve for $k$.
4. Substitute a representative for $k$ to obtain one solution $x_0$.
5. State all integer solutions as $x=x_0+mn\ell$, $\ell\in\mathbb Z$.

This proves existence. For uniqueness modulo $mn$, let $x,y$ be common solutions. Then both $m$ and $n$ divide $x-y$. The coprime-divisor lemma gives $mn\mid(x-y)$, so $x\equiv y\pmod{mn}$.

Conversely, adding a multiple of $mn$ to any solution preserves both congruences. Thus the displayed family gives all solutions.

#### Two direct congruences

Solve

$$
x\equiv7\pmod8,\qquad x\equiv11\pmod{15}.
$$

Since $\gcd(8,15)=1$, write $x=7+8k$. Substitution gives

$$
7+8k\equiv11\pmod{15}\quad\Rightarrow\quad8k\equiv4\pmod{15}.
$$

The identity $2\cdot8-15=1$ gives inverse $2$ for $8$ modulo $15$. Therefore $k\equiv8\pmod{15}$.

One solution is $x_0=7+8\cdot8=71$. All solutions are

$$
x=71+120\ell,\qquad \ell\in\mathbb Z.
$$

Check: $71=8\cdot8+7=15\cdot4+11$.

#### A congruence with a coefficient

Solve

$$
x\equiv2\pmod5,\qquad 3x\equiv5\pmod{13}.
$$

First, $3$ is invertible modulo $13$, so the second equation is equivalent to a direct congruence on $x$. The moduli $5,13$ are coprime, allowing CRT.

Write $x=5k+2$ and substitute:

$$
3(5k+2)\equiv5\pmod{13}
\quad\Rightarrow\quad
2k\equiv-1\pmod{13}.
$$

Since $7\cdot2-13=1$, the inverse of $2$ is $7$. Thus

$$
k\equiv-7\equiv6\pmod{13}.
$$

One solution is $x_0=5\cdot6+2=32$, and all solutions are

$$
x=32+65\ell,\qquad \ell\in\mathbb Z.
$$

Examples are $\ldots,-98,-33,32,97,162,\ldots$. Check that $32\equiv2\pmod5$ and $3\cdot32=96\equiv5\pmod{13}$.

### Fermat's Little Theorem

#### Definitions

> **Fermat's little theorem**: If $p$ is prime and $p\nmid a$, then $a^{p-1}\equiv1\pmod p$.

> **Factorial**: For a positive integer $r$, $r!=1\cdot2\cdots r$.

The theorem gives a guaranteed power congruent to $1$ when the modulus is prime and the base is nonzero modulo that prime.

#### Proof using multiplication of the nonzero classes

1. Since $\overline a\ne\overline0$ in $\mathbb Z_p$, it has an inverse.
2. Consider
   $$\overline a\,\overline1,\ \overline a\,\overline2,\ \ldots,\ \overline a\,\overline{p-1}.$$
3. These classes are nonzero: multiplying an equation $\overline a\,\overline r=\overline0$ by the inverse would give $\overline r=\overline0$.
4. They are distinct: $\overline a\,\overline r=\overline a\,\overline s$ implies $\overline r=\overline s$ by the same valid cancellation.
5. There are $p-1$ of them, so they are exactly all the nonzero classes in $\mathbb Z_p$, in a different order.
6. Multiply them all to obtain
   $$a^{p-1}(p-1)!\equiv(p-1)!\pmod p.$$
7. None of $1,2,\ldots,p-1$ is divisible by $p$. Euclid's lemma shows $p\nmid(p-1)!$, so its residue class is invertible.
8. Cancel that factorial to conclude $a^{p-1}\equiv1\pmod p$.

#### The power corollary

**Corollary 1.56**: For a prime $p$, every integer $a$, and every integer $k\ge1$,

$$
a^{p^k}\equiv a\pmod p.
$$

If $p\mid a$, both sides are zero modulo $p$. Otherwise Fermat gives $a^{p-1}\equiv1$, so $a^p\equiv a$.

Induct on $k$. The case $k=1$ has just been established. If $a^{p^{k-1}}\equiv a\pmod p$, raise both sides to the $p$th power:

$$
a^{p^k}=\left(a^{p^{k-1}}\right)^p\equiv a^p\equiv a\pmod p.
$$

#### Using the theorem and interpreting a test

If $p\nmid a$ and $e=q(p-1)+r$ with $0\le r<p-1$, then

$$
a^e=(a^{p-1})^q a^r\equiv a^r\pmod p.
$$

For example, $4^6\equiv1\pmod7$. Since $119=19\cdot6+5$, this gives $4^{119}\equiv4^5\equiv2\pmod7$, agreeing with the shorter cycle computed earlier.

> [!warning] <span style="color: #ffc778">A Fermat check can disprove primality</span>
> For a candidate $n\ge2$ and a base $a$ coprime to $n$, failure of $a^{n-1}\equiv1\pmod n$ proves that $n$ is composite. Passing the check alone does not prove primality. For the base $10$, the test requires $\gcd(10,n)=1$; primes $2$ and $5$ are excluded from that base's hypothesis.
