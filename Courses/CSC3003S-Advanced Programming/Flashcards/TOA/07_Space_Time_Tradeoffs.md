---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 07 — Space And Time Trade-offs"
---

# TOA 07 — Space And Time Trade-offs

**Source note:** [Space And Time Trade-offs](../../TOA/07_Space_Time_Tradeoffs.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Trade-offs|Trade-offs]]
  - [[#Sorting By Counting|Sorting By Counting]]
  - [[#Horspool|Horspool]]
  - [[#Boyer–Moore|Boyer–Moore]]

## Core Content

### Trade-offs

<!-- qard-id: ap-4d99f2c66a77bb69075e -->
> [!qard]- What is a space–time trade-off?
> Using more memory to reduce computation time.

<!-- qard-id: ap-5d59f896648669246ef6 -->
> [!qard]- Distinguish input enhancement from prestructuring.
> Input enhancement precomputes information about the instance (counting sort, Horspool, Boyer–Moore). Prestructuring organises data for faster access (hashing, B-trees).

<!-- qard-id: ap-829e0c8bf4c902d67186 -->
> [!qard]- When does building an acceleration structure pay off?
> When it is reused enough to outweigh its preprocessing cost.

### Sorting By Counting

<!-- qard-id: ap-3b9d6ec0751b1f835a06 -->
> [!qard]- When can sorting by counting be used and what does it cost?
> When keys are integers in a small range $[L,U]$; $\Theta(n)$ time.

<!-- qard-id: ap-afd16ad37161571c2a29 -->
> [!qard]- What are the frequency and distribution tables in counting sort?
> Frequency: count of each value. Distribution: running totals, giving where each value's block ends.

<!-- qard-id: ap-5a2b76e8a848b24fd007 -->
> [!qard]- Why does counting sort scan the input right to left?
> Placing each element at $D[j]-1$ then decrementing keeps equal keys in order — a stable sort.

### Horspool

<!-- qard-id: ap-66bf00d98b4bbe042680 -->
> [!qard]- What are the two ideas behind Horspool's algorithm?
> Compare the pattern right to left, and on a mismatch shift by a precomputed amount instead of 1.

<!-- qard-id: ap-8505d9ecaf6fec09cb42 -->
> [!qard]- Which text character determines Horspool's shift?
> The text character aligned with the pattern's last position.

<!-- qard-id: ap-b9d18b3642def47c843a -->
> [!qard]- How is Horspool's shift table $T(c)$ computed?
> $T(c)=m-1-$(index of the rightmost $c$ among the first $m-1$ pattern characters); $T(c)=m$ if $c$ doesn't occur there.

<!-- qard-id: ap-8120ec942e9598a9a6cc -->
> [!qard]- Why is the pattern's last character ignored when building $T$?
> A last-position match would give shift 0; using earlier occurrences guarantees progress.

<!-- qard-id: ap-3fe7d7256132b13497d9 -->
> [!qard]- What is Horspool's efficiency on random text?
> $\Theta(n)$ on average (worst case still $\Theta(nm)$).

### Boyer–Moore

<!-- qard-id: ap-4805948b6c8cd0224517 -->
> [!qard]- How does Boyer–Moore's bad-symbol shift differ from Horspool's shift?
> It uses the actual mismatched text character $c$ after $k$ matches: $d_1=\max(T(c)-k,1)$.

<!-- qard-id: ap-2eedd2904a5ae72a9353 -->
> [!qard]- What is $\text{suff}(k)$ and the good-suffix table $G(k)$?
> $\text{suff}(k)$ is the $k$ matched characters at the pattern's end; $G(k)$ is the shift $d_2$ to apply after $k$ matches.

<!-- qard-id: ap-8c68a744ff7678193ff3 -->
> [!qard]- How is $G(k)$ determined?
> Align the rightmost earlier occurrence of $\text{suff}(k)$ preceded by a different character; else align the longest pattern prefix matching the end of the suffix; else shift $m$.

<!-- qard-id: ap-c95a3421272690d4baf9 -->
> [!qard]- What shift does Boyer–Moore use after a mismatch?
> $d_1$ if $k=0$; otherwise $\max(d_1,d_2)$.

<!-- qard-id: ap-b66592d8effc0f4a814e -->
> [!qard]- What information are the shift tables built from?
> Only the pattern — nothing about the text is known in advance.

<!-- qard-id: ap-1f525b4a21af79360aed -->
> [!qard]- When is Horspool better and when is Boyer–Moore better?
> Horspool: large alphabets like natural language (often a full $m$ shift), and it's simpler. Boyer–Moore: small alphabets and repetitive text like DNA.
