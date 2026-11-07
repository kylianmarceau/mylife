---
tags:
  - advanced-programming
---

# Space And Time Trade-offs

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)
**Source**: [7 - TOA SpaceTime Tradeoffs.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/7%20-%20TOA%20SpaceTime%20Tradeoffs.pdf), Patrick Marais, University of Cape Town, pages 1–34
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Input enhancement: sorting by counting, Horspool's string matching, and Boyer–Moore with bad-symbol and good-suffix shifts.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Trading Space For Time|Trading Space For Time]]
  - [[#Sorting By Counting|Sorting By Counting]]
  - [[#Brute-Force String Matching Reminder|Brute-Force String Matching Reminder]]
  - [[#Horspool's Algorithm|Horspool's Algorithm]]
  - [[#Horspool's Four Mismatch Cases|Horspool's Four Mismatch Cases]]
  - [[#Building The Horspool Shift Table|Building The Horspool Shift Table]]
  - [[#Horspool Examples|Horspool Examples]]
  - [[#Boyer-Moore: Bad-Symbol Shift|Boyer-Moore: Bad-Symbol Shift]]
  - [[#Preprocessing Uses Only The Pattern|Preprocessing Uses Only The Pattern]]
  - [[#Boyer-Moore: Good-Suffix Shift|Boyer-Moore: Good-Suffix Shift]]
  - [[#The Boyer-Moore Algorithm And Examples|The Boyer-Moore Algorithm And Examples]]
  - [[#Horspool Versus Boyer-Moore|Horspool Versus Boyer-Moore]]

---

## Core Content

### Trading Space For Time

#### Definitions

> **Space–time trade-off**: Using more memory to reduce computation cost.

> **Input enhancement (preprocessing)**: Storing ancillary information about the problem instance so that solving it afterwards is faster. Examples: sorting by counting, Horspool's and Boyer–Moore's string matching.

> **Prestructuring**: An initial operation that makes access to the data faster. Examples: hashing, indexing with B-trees (covered elsewhere in CS).

Dynamic programming also fits this category but is treated separately.

The general lesson:

- Preprocess all or part of the instance to create an **acceleration data structure**.
- This is very effective if the structure is used repeatedly in the rest of the algorithm.
- The cost of preprocessing must be counted in the overall efficiency.

### Sorting By Counting

#### Definitions

> **Frequency table**: A table $D$ with $U - L + 1$ entries that counts how often each value in the range $[L, U]$ occurs.

> **Distribution table**: Running totals of the frequencies. Entry $D[j]$ gives one past the last position where value $L + j$ belongs in the sorted output.

> **Stable sort**: A sort that keeps equal keys in their original relative order.

Sorting by counting (distribution counting) sorts a list whose elements fall in a restricted integer range $[L \dots U]$:

- It moves the original elements into their correct positions in a new list $S$.
- Extra data can be attached to each element, so it can sort complex records by key.
- It is stable.

```text
// A[0..n-1] with values in [L..U]; output S[0..n-1]
for j ← 0 to U-L do D[j] ← 0                    // initialise frequencies
for i ← 0 to n-1 do D[A[i]-L] ← D[A[i]-L] + 1   // count frequencies
for j ← 1 to U-L do D[j] ← D[j-1] + D[j]        // distribution (running sums)
for i ← n-1 downto 0 do
    j ← A[i] - L
    S[D[j]-1] ← A[i]
    D[j] ← D[j] - 1
return S
```

Scanning $A$ from right to left and decrementing $D[j]$ after each placement keeps the sort stable.

**Example**: $A = [13, 11, 12, 13, 12, 12]$, range $[11, 13]$.

| Array value | 11 | 12 | 13 |
|---|---|---|---|
| Frequency | 1 | 3 | 2 |
| Distribution | 1 | 4 | 6 |

Placing elements from right to left ($D$ shown before each placement):

| Element | $D[0]$ | $D[1]$ | $D[2]$ | Placed at |
|---|---|---|---|---|
| $A[5] = 12$ | 1 | **4** | 6 | $S[3]$ |
| $A[4] = 12$ | 1 | **3** | 6 | $S[2]$ |
| $A[3] = 13$ | 1 | 2 | **6** | $S[5]$ |
| $A[2] = 12$ | 1 | **2** | 5 | $S[1]$ |
| $A[1] = 11$ | **1** | 1 | 5 | $S[0]$ |
| $A[0] = 13$ | 0 | 1 | **5** | $S[4]$ |

Result: $S = [11, 12, 12, 12, 13, 13]$.

Time efficiency is $\Theta(n)$ — the best sort so far — but only for highly restricted inputs and applications (small integer key ranges).

### Brute-Force String Matching Reminder

Brute force aligns the pattern with the start of the text, checks it until a mismatch, then shifts one place right.

Searching for `GECKO` in `THE_CAT_ATE_THE_GECKO'S_TAIL` takes 17 shifts of one position each before the match is found.

### Horspool's Algorithm

#### Definitions

> **Shift table $T$**: A table with one entry per alphabet character $c$, giving how far to shift the pattern when text character $c$ is aligned with the **last** character of the pattern. The maximum shift is $m$, the pattern length.

Horspool's principle:

- Start matching from the **end** of the pattern.
- On a mismatch, shift the pattern by more than one position, using the precomputed table $T$.

The same `GECKO` search takes only 5 shifts with Horspool versus 17 with brute force.

Algorithm:

1. Construct the shift table $T$ from the pattern.
2. Align the pattern with the beginning of the text.
3. Repeat until a match is found or the pattern passes the end of the text:
   1. Starting with the last pattern character, compare corresponding characters right to left until all $m$ match or a mismatch is found.
   2. On a mismatch, let $c$ be the text character aligned with the **last** pattern character. Shift the pattern right by $T(c)$.

Only the text character under the last pattern position decides the shift. For random texts, Horspool's algorithm can be shown to run in $\Theta(n)$ on average.

### Horspool's Four Mismatch Cases

In every case the shift is determined by the text character $c$ aligned with the last pattern character.

| Case | Situation | Example | Shift |
|---|---|---|---|
| 1 | $c$ is not in the pattern | `A_CAT` vs `GECKO`: T not in GECKO | Move the whole pattern past $c$: shift $m$ |
| 2 | Last letters match, and $c$ does not occur elsewhere in the pattern | `HE_FOUND` vs `GECKO`: O only at the end | Shift $m$ (same as case 1) |
| 3 | $c$ is in the pattern, but not at the end | `THE_C` vs `GECKO`: C is in GECKO | Align $c$ with its rightmost occurrence in the pattern: $T(c) = m - 1 - \text{pos}(c)$ |
| 4 | Last letters match and $c$ occurs elsewhere in the pattern | `ENDURING` vs `ENGAGING`: G occurs earlier | Align with the rightmost occurrence of $c$, ignoring the last character (same as case 3) |

![Horspool four cases](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/07_Space_Time_Tradeoffs/horspool-cases.svg)

*The character under the pattern's last position either does not occur in the first $m-1$ positions (shift $m$) or is aligned with its rightmost earlier occurrence.*

### Building The Horspool Shift Table

$$
T(c) =
\begin{cases}
m - 1 - (\text{index of rightmost } c \text{ among the first } m-1 \text{ pattern characters}) & \text{if such a } c \text{ exists} \\
m & \text{otherwise}
\end{cases}
$$

Example: `ENGAGING`, $m = 8$, with 5 unique letters.

| Character | Rightmost index (excluding last position) | Shift $T(c)$ |
|---|---|---|
| E | 0 | $8 - 1 - 0 = 7$ |
| N | 6 | $8 - 1 - 6 = 1$ |
| I | 5 | $8 - 1 - 5 = 2$ |
| G | 4 | $8 - 1 - 4 = 3$ |
| A | 3 | $8 - 1 - 3 = 4$ |
| All others | — | $m = 8$ |

The final G at index 7 is ignored, which is why $T(G) = 3$ (from the G at index 4).

### Horspool Examples

All use pattern `ENGAGING` and the table above.

| Text | Steps |
|---|---|
| `IT_WAS_ENGAGING` | Character under the last position is E (it occurs earlier in the pattern): shift $T(E) = 7$ → match |
| `IT_WAS_VERY_ENGAGING` | Under the last position is V: shift $T(V) = 8$ (any character not in the pattern). Then A: shift $T(A) = 4$ → match |
| `IT_WAS_NOT_ENGAGING` | N: shift 1; O: shift 8; I: shift 2 → match |
| `IT_WAS_GOING_ENGAGINGLY` | G: shift 3; N: shift 1; G: shift 3; N: shift 1; G: shift 3; I: shift 2 → match |

![Horspool traces](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/07_Space_Time_Tradeoffs/horspool-traces.svg)

*Each row is an alignment; the shift is looked up from the text character under the pattern's last position.*

### Boyer-Moore: Bad-Symbol Shift

Boyer–Moore uses the same two ideas as Horspool — compare right to left, and precompute shifts from the pattern — but adds a second table.

#### Definitions

> **Bad-character (bad-symbol) rule**: Use the Horspool table $T$, but look up the shift of the **rightmost mismatched** text character $c$, not the character at the end of the pattern.

Let $k$ be the number of characters matched from the end before the mismatch, and $c$ the mismatched text character:

$$
d_1 = \max\big(T(c) - k,\ 1\big)
$$

$T(c) - k$ can be less than 1, hence the $\max$: we can always shift at least one position, as in brute force.

Table for `BARBER` ($m = 6$):

| $c$ | A | B | C | D | E | F | … | R | … | Z | _ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $T(c)$ | 4 | 2 | 6 | 6 | 1 | 6 | 6 | 3 | 6 | 6 | 6 |

**Example**: text `…SER`, pattern `BARBER`. "ER" matches ($k = 2$), then S mismatches.

| Algorithm | Shift |
|---|---|
| Horspool | Uses R (under the last position): $T(R) = 3$ |
| Boyer–Moore | S is not in BARBER, so move the pattern past S: $\max(T(S) - 2, 1) = \max(6 - 2, 1) = 4$ |

Neither rule is always better:

| Text | Boyer–Moore $d_1$ | Horspool | Winner |
|---|---|---|---|
| `TANSER` | $\max(T(S) - 2, 1) = 4$ | $T(R) = 3$ | Boyer–Moore |
| `MY AEROPLANE` (A mismatches after `ER` matches) | $\max(T(A) - 2, 1) = 2$ | $T(R) = 3$ | Horspool |

### Preprocessing Uses Only The Pattern

Before searching, we know everything about the pattern and nothing about the text.

- Shift tables are built only from the pattern.
- Both algorithms extract information from the pattern in advance to maximise the shift on each mismatch.
- The shift tables depend solely on properties of the pattern, not the text. This is key to understanding the good-suffix rule.

### Boyer-Moore: Good-Suffix Shift

#### Definitions

> **$\text{suff}(k)$**: The suffix of length $k$ of the pattern — the $k$ characters that matched at the end before a mismatch.

> **Good-suffix table $G(k)$**: A table giving the shift $d_2$ to use after $k$ characters matched, based on where else $\text{suff}(k)$ (or part of it) occurs in the pattern.

Boyer–Moore takes whichever is larger: the good-suffix shift or the bad-symbol shift. Three cases arise when building $G(k)$:

**Case 1 — $\text{suff}(k)$ does not occur elsewhere in the pattern.**

- Text `…ABAB…`, pattern `MAOBAB`. For $k = 3$ the suffix `BAB` has no earlier occurrence, so $G(3) = m = 6$.
- But not always: check case 3 first, because part of the suffix might occur at the start. Don't stop just because $\text{suff}(k)$ isn't found earlier.

**Case 2 — $\text{suff}(k)$ occurs earlier in the pattern, preceded by a different character.**

- Search right to left in the pattern for another instance. Instances may overlap.
- The position just left of the pattern counts as a "match anything" character: in `(x)BABOBAB`, the initial `BAB` qualifies.
- An earlier instance preceded by the **same** character is useless — the same mismatch would recur. Pattern `OBABOBAB` with text `…ABAB…`: the earlier `BAB` is also preceded by O, so shift past it: $G(3) = 8$.
- Pattern `ABABOBAB`: the earlier `BAB` is preceded by A (different from O), so align it with the matched suffix: $G(3) = 4$.

**Case 3 — part of $\text{suff}(k)$ occurs at the beginning of the pattern.**

- If the whole suffix cannot be matched earlier, look for the longest **prefix** of the pattern that matches the end of $\text{suff}(k)$. The prefix may overlap the suffix.
- Pattern `ABCBAB`, text `…ABAB…`, $k = 3$: `BAB` does not occur earlier, but the prefix `AB` matches the end of `BAB`. Shift to align them: $G(3) = 4$.

![Good-suffix alignments](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/07_Space_Time_Tradeoffs/good-suffix.svg)

*The shift aligns an earlier copy of the matched suffix (with a different preceding character), or else the longest prefix matching the suffix's end, or else moves the whole pattern.*

Algorithm for building $G(k)$:

```text
// Scan from right to left; pattern length = m; k = matched chars
// suff(k) is the k matching characters at the end of the pattern
if (suff(k) is present earlier in pattern)
    if (an instance exists whose preceding character is different, or empty)
        shift to align this earlier instance with suff(k)
        return shift
if (a prefix matches the end of suff(k))
    shift to align the longest such prefix with the end of suff(k)
    return shift
shift = m
return shift
```

### The Boyer-Moore Algorithm And Examples

1. Build tables $T$ and $G$ from the pattern.
2. When a mismatch occurs after $k$ matches, with $c$ the mismatched text character:
   - Bad-symbol shift ($k \ge 0$): $d_1 = \max(T(c) - k, 1)$.
   - Good-suffix shift (only if $k > 0$): $d_2 = G(k)$.
3. Shift by
$$
d = \begin{cases} d_1 & k = 0 \\ \max(d_1, d_2) & k > 0 \end{cases}
$$

#### Example 1: `BAOBAB`

Bad-symbol table:

| $c$ | A | B | C | D | … | O | … | Z | _ |
|---|---|---|---|---|---|---|---|---|---|
| $t_1(c)$ | 1 | 2 | 6 | 6 | 6 | 3 | 6 | 6 | 6 |

Good-suffix table:

| $k$ | Matched suffix | $d_2$ |
|---|---|---|
| 1 | B | 2 |
| 2 | AB | 5 |
| 3 | BAB | 5 |
| 4 | OBAB | 5 |
| 5 | AOBAB | 5 |

Search in `BESS_KNEW_ABOUT_BAOBABS`:

| Alignment | Mismatch | Shift |
|---|---|---|
| 1 | K vs B, $k = 0$ | $d_1 = t_1(K) - 0 = 6$ |
| 2 | `_` after matching `AB`, $k = 2$ | $d_1 = t_1(\_) - 2 = 4$, $d_2 = 5$ → $d = 5$ |
| 3 | `_` after matching `B`, $k = 1$ | $d_1 = t_1(\_) - 1 = 5$, $d_2 = 2$ → $d = 5$ |
| 4 | full match of `BAOBAB` | done |

#### Example 2: 1000 zeros, pattern `10000`

How many comparisons does Boyer–Moore make on $S = 000\dots0$ (1000 zeros) with $P = 10000$?

| Bad-symbol $c$ | 0 | 1 |
|---|---|---|
| $t_1(c)$ | 1 | 4 |

| $k$ | Matched suffix | $d_2$ |
|---|---|---|
| 1 | 0 | 3 |
| 2 | 00 | 2 |
| 3 | 000 | 1 |
| 4 | 0000 | 5 |

1. At each alignment the four 0s match and the 1 fails: 5 comparisons.
2. With $k = 4$: $d_1 = \max(t_1(0) - 4, 1) = 1$ and $d_2 = 5$, so the shift is $\max(1, 5) = 5$.
3. The same failure pattern repeats until the text is exhausted.
4. There are $1000/5 = 200$ alignments, so $200 \times 5 = 1000$ comparisons.

### Horspool Versus Boyer-Moore

Their performance is asymptotically the same; Horspool's approach is simpler and at least as efficient on average. To choose, look at how each opts out early:

| Algorithm | Best for | Why | Example |
|---|---|---|---|
| Horspool | Large alphabets, natural language | A mismatch is often caused by a character not in the pattern, giving the maximum shift | English word matching |
| Boyer–Moore | Small alphabets with very long, repetitive text | The good-suffix table exploits repeating sub-patterns when shifting | DNA matching (G, T, A, C) |
