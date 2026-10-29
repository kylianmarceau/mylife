---
tags:
  - advanced-programming
---

# Space And Time Tradeoffs

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)  
**Source**: [7 - TOA SpaceTime Tradeoffs.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/7%20-%20TOA%20SpaceTime%20Tradeoffs.pdf), Patrick Marais, University of Cape Town, PDF pages 1–34  
**Generated**: 2026-10-02

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes. Examples and corrections appear beside the relevant concept.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Input Enhancement And Prestructuring|Input Enhancement And Prestructuring]]
  - [[#Stable Counting Sort|Stable Counting Sort]]
  - [[#Horspool Shift Tables And Four Cases|Horspool Shift Tables And Four Cases]]
  - [[#Horspool Search And Source Traces|Horspool Search And Source Traces]]
  - [[#Boyer–Moore Bad-Symbol Rule|Boyer–Moore Bad-Symbol Rule]]
  - [[#Boyer–Moore Good-Suffix Rule|Boyer–Moore Good-Suffix Rule]]
  - [[#Combined Boyer–Moore And Worked Traces|Combined Boyer–Moore And Worked Traces]]
  - [[#Performance And Preprocessing Choices|Performance And Preprocessing Choices]]

---

## Core Content

### Input Enhancement And Prestructuring

#### Definitions

> **Space–time tradeoff**: Use additional storage to reduce the amount of repeated computation.

> **Input enhancement**: Precompute and store auxiliary information about an instance to accelerate the subsequent algorithm.

> **Prestructuring**: Organise data in a structure supporting faster access.

| Approach | Examples | Stored information |
|---|---|---|
| Input enhancement | Counting sort; Horspool; Boyer–Moore | Frequencies, positions or legal shifts |
| Prestructuring | Hashing; B-tree indexing | Lookup structure |
| Dynamic programming | Cached subproblem answers | Results reused by later subproblems |

Count both preprocessing and later use. A structure pays off when it saves enough work, especially when reused repeatedly.

### Stable Counting Sort

#### Definitions

> **Counting sort**: Sort integer-keyed records by counting key frequencies and using cumulative counts to determine output positions.

> **Distribution table**: Cumulative frequencies, giving the number of records with key at most each table key.

Keys lie in a known integer range $[L,U]$, with $r=U-L+1$ possible keys. Map key $x$ to table index $x-L$.

1. Initialise a frequency table of size $r$ to zero.
2. Count each input key.
3. Replace frequencies with cumulative counts.
4. Scan the input backwards, placing each record at its key's last unfilled position.
5. Decrement that key's cumulative count after placement.

```pseudo
CountingSort(A, L, U):
    r = U - L + 1
    D[0 .. r - 1] = all zeros
    for i = 0 to length(A) - 1:
        D[key(A[i]) - L] = D[key(A[i]) - L] + 1
    for j = 1 to r - 1:
        D[j] = D[j - 1] + D[j]
    for i = length(A) - 1 downto 0:
        j = key(A[i]) - L
        S[D[j] - 1] = A[i]
        D[j] = D[j] - 1
    return S
```

> [!warning] <span style="color:#ffc778">Source index corrections</span>
> The frequency loop must use its actual loop index. The cumulative loop starts at one, preventing access to the entry before the table. The pseudocode above corrects both errors.

For the source array $13,11,12,13,12,12$:

| Key | Frequency | Initial distribution |
|---|---:|---:|
| $11$ | $1$ | $1$ |
| $12$ | $3$ | $4$ |
| $13$ | $2$ | $6$ |

| Input index processed | Key | Output position | Distribution after placement |
|---:|---:|---:|---|
| $5$ | $12$ | $3$ | $(1,3,6)$ |
| $4$ | $12$ | $2$ | $(1,2,6)$ |
| $3$ | $13$ | $5$ | $(1,2,5)$ |
| $2$ | $12$ | $1$ | $(1,1,5)$ |
| $1$ | $11$ | $0$ | $(0,1,5)$ |
| $0$ | $13$ | $4$ | $(0,1,4)$ |

Output is $11,12,12,12,13,13$. Reverse scanning places later equal-key records in later positions, preserving stability and attached record data.

Time is $\Theta(n+r)$ and extra storage is $\Theta(n+r)$ including the output. The lecture's linear-in-input claim assumes a sufficiently small range, such as $r=O(n)$. A huge sparse key range makes the table unattractive. Counting sort is not a comparison sort, so it does not contradict comparison-sorting lower bounds.

### Horspool Shift Tables And Four Cases

#### Definitions

> **Horspool's algorithm**: Compare pattern characters right to left, then shift according to the text character aligned with the pattern's last position.

> **Shift table**: A table assigning each alphabet character a positive safe shift distance.

For pattern $P$ of length $m$, define:

$$
T(c)=\begin{cases}
m-1-j,&j\text{ is the rightmost position of }c\text{ in }P[0\ldots m-2],\\
m,&c\text{ does not occur in }P[0\ldots m-2].
\end{cases}
$$

Exclude the final pattern position: including it would give a zero shift and fail to make progress. The table is determined entirely by the pattern.

| Situation for the last-aligned text character | Shift action |
|---|---|
| Character absent from the pattern | Shift the full pattern length |
| Character appears only at the last pattern position | Shift the full pattern length |
| Character appears before the last position | Align with its rightmost earlier occurrence |
| Last character matches and also appears earlier | Ignore its final occurrence; align the rightmost earlier one |

The shift lookup uses the character at the final aligned text position, even when the actual mismatch is further left.

For `ENGAGING`, $m=8$:

| Character | $E$ | $N$ | $G$ | $A$ | $I$ | Other |
|---|---:|---:|---:|---:|---:|---:|
| Shift | $7$ | $1$ | $3$ | $4$ | $2$ | $8$ |

For `GECKO`, the earlier-position shifts are $T(G)=4,T(E)=3,T(C)=2,T(K)=1$; $T(O)=5$ and absent characters also shift five.

![Horspool four shift cases](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/07_Space_Time_Tradeoffs/horspool-cases.svg)

*The four source cases depend on the final aligned text character, with earlier pattern occurrences deciding the shift.*

### Horspool Search And Source Traces

```java
BuildShift(P, alphabet):
    m = length(P)
    for each c in alphabet: T[c] = m
    for j = 0 to m - 2: T[P[j]] = m - 1 - j
    return T

Horspool(Txt, P):
    if length(P) == 0: return 0
    shift = BuildShift(P, alphabet)
    end = length(P) - 1
    while end < length(Txt):
        k = 0
        while k < length(P) and P[length(P) - 1 - k] == Txt[end - k]:
            k = k + 1
        if k == length(P): return end - length(P) + 1
        end = end + shift[Txt[end]]
    return -1
```

For `THE_CAT_ATE_THE_GECKO’S_TAIL`, the pattern `GECKO` starts at index sixteen:

| Start | Last-aligned text character | Shift / result |
|---:|---|---|
| $0$ | $C$ | $2$ |
| $2$ | $T$ | $5$ |
| $7$ | `_` | $5$ |
| $12$ | $G$ | $4$ |
| $16$ | $O$ | Match |

That is four shifts and five attempted alignments; brute force uses sixteen shifts and seventeen alignments. The PDF labels the alignment counts as shifts.

![GECKO and ENGAGING source alignment traces](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/07_Space_Time_Tradeoffs/horspool-traces.svg)

*Precomputed shifts skip text positions without skipping a possible match.*

| Text, pattern `ENGAGING` | Alignment starts | Shift sequence before match |
|---|---|---|
| `IT_WAS_ENGAGING` | $0,7$ | $7$ |
| `IT_WAS_VERY_ENGAGING` | $0,8,12$ | $8,4$ |
| `IT_WAS_NOT_ENGAGING` | $0,1,9,11$ | $1,8,2$ |
| `IT_WAS_GOING_ENGAGINGLY` | $0,3,4,7,8,11,13$ | $3,1,3,1,3,2$ |

Preprocessing takes $\Theta(\lvert\Sigma\rvert+m)$ time and $\Theta(\lvert\Sigma\rvert)$ table storage for alphabet $\Sigma$. Worst-case search remains $O(mn)$; expected linear-in-text behaviour assumes an appropriate random-text model, commonly with fixed pattern length.

### Boyer–Moore Bad-Symbol Rule

#### Definitions

> **Bad symbol**: The text character at the position where right-to-left comparison fails.

> **Matched suffix**: The final $k$ pattern characters that have already matched before the mismatch.

Boyer–Moore uses information about the mismatch and the matched suffix. For the course's bad-symbol rule, reuse the Horspool-style table:

$$
d_1=\max(T(c)-k,1),
$$

where $c$ is the actual mismatching text character and $k$ is the number of successful comparisons from the end. This differs from Horspool, which looks up the final-aligned text character.

For `BARBER`, $T(B)=2,T(A)=4,T(R)=3,T(E)=1$, with all other characters assigned six.

| Source example | Matched suffix | Bad symbol | Boyer–Moore bad shift | Horspool shift |
|---|---|---|---|---|
| `TANSER` aligned with `BARBER` | `ER`, $k=2$ | $S$ | $\max(6-2,1)=4$ | $T(R)=3$ |
| `MY_AEROPLANE`, initial alignment | `ER`, $k=2$ | $A$ | $\max(4-2,1)=2$ | $T(R)=3$ |

The bad-symbol rule alone does not always beat Horspool. Boyer–Moore's final shift also considers the good-suffix rule.

### Boyer–Moore Good-Suffix Rule

#### Definitions

> **Good-suffix table**: A pattern-only table $G(k)$ giving a safe shift after matching the final $k>0$ characters and then failing.

> **Prefix**: A substring beginning at the start of the pattern.

1. Search backwards for an earlier occurrence of the entire matched suffix.
2. Prefer the rightmost occurrence preceded by a different character from the original pattern mismatch position, or by the start boundary.
3. If none exists, align the longest pattern prefix that matches the end of the matched suffix.
4. If neither exists, shift by the full pattern length.

An earlier occurrence with the same preceding pattern character would repeat the known mismatch. Overlapping occurrences and overlapping prefix/suffix matches are allowed.

| Pattern | Matched suffix | Reason | $G(3)$ |
|---|---|---|---:|
| `MAOBAB` | `BAB` | No earlier suffix or matching prefix | $6$ |
| `OBABOBAB` | `BAB` | Earlier suffix has the same preceding character; no useful prefix | $8$ |
| `ABABOBAB` | `BAB` | Earlier occurrence has a different preceding character | $4$ |
| `ABCBAB` | `BAB` | Prefix `AB` matches the end of the suffix | $4$ |
| `BABOBAB` | `BAB` | Earlier occurrence at the start has no preceding character | $4$ |

![Good-suffix source cases](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/07_Space_Time_Tradeoffs/good-suffix.svg)

*Full-suffix alignment, different preceding characters and prefix fallback determine safe good-suffix shifts.*

A transparent, though inefficient, construction tests each possible positive shift:

```java
BuildGoodSuffix(P):
    m = length(P)
    G[0] = 1
    for k = 1 to m - 1:
        mismatchIndex = m - k - 1
        for shift = 1 to m:
            valid = true
            for q = mismatchIndex + 1 to m - 1:
                if q - shift >= 0 and P[q - shift] != P[q]:
                    valid = false
            if mismatchIndex - shift >= 0:
                if P[mismatchIndex - shift] == P[mismatchIndex]:
                    valid = false
            if valid:
                G[k] = shift
                break
    return G
```

The overlap tests enforce agreement with known matched text; the preceding-character test rejects shifts that necessarily repeat the mismatch. This simple construction costs up to $O(m^3)$ time; efficient implementations use more specialised preprocessing. Table construction cost is separate from search cost.

### Combined Boyer–Moore And Worked Traces

For a mismatch after $k$ matches:

$$
\text{shift}=\begin{cases}
d_1,&k=0,\\
\max(d_1,G(k)),&k>0.
\end{cases}
$$

Each rule supplies a safe lower bound on how far the pattern can move. The larger avoids more positions already ruled out.

```java
BoyerMoore(Txt, P):
    if length(P) == 0: return 0
    T = BuildShift(P, alphabet)
    G = BuildGoodSuffix(P)
    start = 0
    while start <= length(Txt) - length(P):
        k = 0
        while k < length(P) and P[length(P) - 1 - k] == Txt[start + length(P) - 1 - k]:
            k = k + 1
        if k == length(P): return start
        c = Txt[start + length(P) - 1 - k]
        bad = max(T[c] - k, 1)
        good = G[k] if k > 0 else 1
        start = start + max(bad, good)
    return -1
```

For source pattern `BAOBAB`:

| Bad-symbol character | $A$ | $B$ | $O$ | Other |
|---|---:|---:|---:|---:|
| $T(c)$ | $1$ | $2$ | $3$ | $6$ |

| Matched count $k$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---:|---:|---:|---:|---:|
| $G(k)$ | $2$ | $5$ | $5$ | $5$ | $5$ |

For `BESS_KNEW_ABOUT_BAOBABS`:

| Start | $k$ | Actual bad symbol | $d_1$ | $d_2$ | Shift / result |
|---:|---:|---|---:|---:|---|
| $0$ | $0$ | $K$ | $6$ | Not used | $6$ |
| $6$ | $2$ | `_` | $4$ | $5$ | $5$ |
| $11$ | $1$ | `_` | $5$ | $2$ | $5$ |
| $16$ | $6$ | None | — | — | Match |

For a thousand zero characters and pattern `10000`, each attempt matches four zeros, then fails on the initial one. The bad-symbol shift is one; the good-suffix shift is five. Starts are $0,5,\ldots,995$: two hundred alignments, five comparisons each, giving exactly one thousand comparisons. Brute force would perform $5(1000-5+1)=4980$ comparisons on this instance.

### Performance And Preprocessing Choices

| Aspect | Horspool | Boyer–Moore |
|---|---|---|
| Lookup on mismatch | Last-aligned text character | Actual bad symbol and matched suffix |
| Stored tables | Bad-character-style table | Bad-symbol and good-suffix tables |
| Implementation | Simpler | More preprocessing and logic |
| Often useful setting | Large alphabets, frequent absent characters | Repetitive text and small alphabets, such as DNA |
| Basic variant worst case | $O(mn)$ | Can also be $O(mn)$; stronger guarantees depend on the exact variant |

The lecture's expected-linear performance comparisons assume text models and omit variant-specific refinements. Actual performance depends on patterns, alphabet size, repetitions and reuse of tables. Consider preprocessing overhead and memory, rather than treating either method as universally faster.
