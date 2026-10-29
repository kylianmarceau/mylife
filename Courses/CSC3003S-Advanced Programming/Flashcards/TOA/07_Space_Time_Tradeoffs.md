---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 07 — Space And Time Tradeoffs"
---

# TOA 07 — Space And Time Tradeoffs

**Source note:** [Space And Time Tradeoffs](../../TOA/07_Space_Time_Tradeoffs.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Input Enhancement And Prestructuring|Input Enhancement And Prestructuring]]
  - [[#Stable Counting Sort|Stable Counting Sort]]
  - [[#Horspool Shift Tables And Four Cases|Horspool Shift Tables And Four Cases]]
  - [[#Horspool Search Mechanics|Horspool Search Mechanics]]
  - [[#Boyer–Moore Bad-Symbol Rule|Boyer–Moore Bad-Symbol Rule]]
  - [[#Boyer–Moore Good-Suffix Rule|Boyer–Moore Good-Suffix Rule]]
  - [[#Combined Boyer–Moore Search Mechanics|Combined Boyer–Moore Search Mechanics]]
  - [[#Performance And Preprocessing Choices|Performance And Preprocessing Choices]]
  - [[#Horspool Search And Source Traces|Horspool Search And Source Traces]]
  - [[#Combined Boyer–Moore And Worked Traces|Combined Boyer–Moore And Worked Traces]]
  - [[#Table Construction And Search Boundaries|Table Construction And Search Boundaries]]

## Core Content

### Input Enhancement And Prestructuring

<!-- qard-id: ap-5dc43b1981336e3001a8 -->
> [!qard]- What is input enhancement?
> Precompute and store auxiliary information about an instance to accelerate its subsequent processing.

<!-- qard-id: ap-9722f3babd3e92ecb05f -->
> [!qard]- What is prestructuring?
> Organise data in a structure supporting faster access.

<!-- qard-id: ap-bd1e3588eab1315666e3 -->
> [!qard]- How do preprocessing and reuse determine whether a space–time trade-off pays off?
> Include table construction, later queries/searches and extra memory. Shift tables/frequencies enhance input; hashing or B-tree indexes prestructure it; DP reuses stored subproblem results.

### Stable Counting Sort

<!-- qard-id: ap-e2c79707985ba30bbff1 -->
> [!qard]- What key-domain condition does counting sort require?
> A known integer range $[L,U]$ with $r=U-L+1$ possible keys.

<!-- qard-id: ap-76eabbe9cce9360b7966 -->
> [!qard]- What are the stages of stable counting sort?
> Zero the frequency table, count keys, form cumulative counts, scan input backwards to place records, and decrement each used count.

<!-- qard-id: ap-9c2b30bf1e0e1ab75ae3 -->
> [!qard]- Why scan the input backwards for stable counting sort?
> Later equal-key records go into later available positions, preserving their original relative order.

<!-- qard-id: ap-99150d40fe41ac1b73b4 -->
> [!qard]- What are stable counting sort's time and extra-space costs?
> $\Theta(n+r)$ time and $\Theta(n+r)$ extra space including output.

<!-- qard-id: ap-c40d1b55123fd2e54246 -->
> [!qard]- Why does linear counting sort not contradict comparison-sorting lower bounds?
> It is not a comparison sort; it exploits integer-key range information.

<!-- qard-id: ap-8d32d35ffbb8299b1be6 -->
> [!qard]- How do cumulative counts determine a stable counting-sort placement?
> Map key $x$ to $j=x-L$. Place the entire record at output $D[j]-1$, decrement $D[j]$, and scan input backwards. The cumulative loop starts at one to avoid index $-1$.

<!-- qard-id: ap-c035983382a3bf91fa1d -->
> [!qard]- When is counting sort linear in input length, and when is it unattractive?
> Its $\Theta(n+r)$ cost is linear in $n$ if range size $r=O(n)$. A huge sparse range wastes time and memory even for few input keys.

### Horspool Shift Tables And Four Cases

<!-- qard-id: ap-e08bfcf889be94b093c5 -->
> [!qard]- What is Horspool's string-matching algorithm?
> Compare the pattern right to left and shift using the text character aligned with the pattern's last position.

<!-- qard-id: ap-3b6f7087c89addf84160 -->
> [!qard]- How is Horspool's shift $T(c)$ defined for a pattern of length $m$?
> If $j$ is the rightmost occurrence of $c$ in $P[0\ldots m-2]$, $T(c)=m-1-j$; if none exists, $T(c)=m$.

<!-- qard-id: ap-e88b53a871f4f8415251 -->
> [!qard]- Why exclude the last pattern position when building Horspool's table?
> Including it could give a zero shift. If the last-aligned text character occurs only there, or nowhere, shift $m$; otherwise align its rightmost earlier occurrence, even if the final characters matched.

<!-- qard-id: ap-8f32213e617c7b6f9fc7 -->
> [!qard]- How does Horspool initialise its aligned end, recognise a complete match and return the match position?
> Set the aligned end to $m-1$, compare right-to-left, and return $\mathrm{end}-m+1$ when all $m$ characters match. After failure, shift using the final-aligned text character; stop when the end leaves the text.

### Horspool Search Mechanics

<!-- qard-id: ap-c179a401d881dc749c13 -->
> [!qard]- How does Horspool update its aligned end after a mismatch?
> Add $T(c)$, where $c$ is the text character at the current final-aligned index.

<!-- qard-id: ap-3f2a68520c59f47ff0a8 -->
> [!qard]- What are Horspool's preprocessing time and table space?
> $\Theta(\lvert\Sigma\rvert+m)$ time and $\Theta(\lvert\Sigma\rvert)$ storage for alphabet $\Sigma$.

<!-- qard-id: ap-008ae91c14d0015fdadd -->
> [!qard]- What is Horspool's worst-case search bound?
> $O(mn)$.

### Boyer–Moore Bad-Symbol Rule

<!-- qard-id: ap-02f4e4829cd7b34528c5 -->
> [!qard]- What is the course's Boyer–Moore bad-symbol shift?
> $d_1=\max(T(c)-k,1)$, using the Horspool-style table, actual mismatching character $c$, and matched count $k$.

<!-- qard-id: ap-1c053716a4f962084d6a -->
> [!qard]- How do Horspool and Boyer–Moore choose their character lookups?
> Horspool uses the final-aligned text character; Boyer–Moore's bad-symbol rule uses the actual mismatching character.

### Boyer–Moore Good-Suffix Rule

<!-- qard-id: ap-d92b56fa207e47fc9c5d -->
> [!qard]- What does the Boyer–Moore good-suffix rule try to align?
> After a suffix matches, align it with a suitable earlier occurrence; if none exists, align the longest matching pattern prefix with the suffix's end. If neither exists, shift the full pattern length.

<!-- qard-id: ap-4f779d8404a0879c2477 -->
> [!qard]- What makes an earlier full-suffix occurrence suitable?
> Its preceding pattern character differs from the original mismatch-position character, or it starts at the pattern boundary.

<!-- qard-id: ap-9931c81c45cb5af25220 -->
> [!qard]- What fallback is used when no suitable earlier full-suffix occurrence exists?
> Align the longest pattern prefix matching the end of the matched suffix.

<!-- qard-id: ap-39583d214ace4b302aee -->
> [!qard]- What does good-suffix preprocessing need to check, and what does the simple construction cost?
> Test overlap agreement and reject a repeated preceding mismatch character; allow overlaps and prefix fallback. The notes' exhaustive construction is up to $O(m^3)$, separate from search; specialised constructions are faster.

### Combined Boyer–Moore Search Mechanics

<!-- qard-id: ap-4de6e31f57a8c39a59fe -->
> [!qard]- How are Boyer–Moore's bad-symbol and good-suffix shifts combined?
> After $k>0$ suffix matches, use $\max(d_1,G(k))$; if $k=0$, use the bad-symbol shift alone.

<!-- qard-id: ap-0766ba8d4e48ad46fcec -->
> [!qard]- Why is taking the maximum of the two Boyer–Moore shifts safe?
> Each rule excludes all earlier alignments up to its safe shift; the larger skips more positions already ruled out.

### Performance And Preprocessing Choices

<!-- qard-id: ap-d8efeb59dcf09dcaf6f3 -->
> [!qard]- Is basic Boyer–Moore guaranteed linear worst-case searching?
> No. Basic variants can be $O(mn)$; stronger guarantees depend on the exact variant and refinements.

<!-- qard-id: ap-365a9a0a16075665571f -->
> [!qard]- When might Horspool's simplicity or Boyer–Moore's extra suffix information pay off?
> Large alphabets and frequent absent characters often suit Horspool; repetitive text/small alphabets may benefit from good-suffix shifts. Compare preprocessing, memory and reuse as well as search; neither is universally faster.

### Horspool Search And Source Traces

<!-- qard-id: ap-02a62c29e2acb8ce460c -->
> [!qard]- Why is the number of attempted string-matching alignments usually one more than the shifts made before a match?
> The first alignment is attempted before any shift; each later attempt follows a shift. Count comparisons, alignments and movements separately rather than using the labels interchangeably.

### Combined Boyer–Moore And Worked Traces

<!-- qard-id: ap-558fade02091a1d3ab5b -->
> [!qard]- Why can good-suffix information help on repetitive text when the bad-symbol shift is small?
> A long matched suffix can rule out several overlapping alignments even when the mismatching character gives only a one-position bad-symbol shift. Take the larger safe shift; repetition alone does not establish a universal speed guarantee.

### Table Construction And Search Boundaries

<!-- qard-id: ap-e072cb079fa2aeb12b9e -->
> [!qard]- Why does counting sort move the whole record rather than just its key?
> Attached payloads must stay associated with their keys; stability concerns equal-key records, not merely a sorted list of bare numbers.

<!-- qard-id: ap-ec805aff936460c38728 -->
> [!qard]- What information does a counting-sort cumulative entry represent before output placement?
> The number of input records whose keys are at most that entry's key, giving the one-past-last output index for that key group.

<!-- qard-id: ap-a26e89a68fed093ae6f1 -->
> [!qard]- Why does Horspool use a pattern-only table rather than recomputing shifts from the text?
> It encodes safe alignment distances based on pattern occurrences and can be reused at every alignment or with another text.

<!-- qard-id: ap-946c509379a311ee567c -->
> [!qard]- Why does the bad-symbol shift subtract the number of already matched suffix characters?
> The actual mismatch is that many positions left of the final aligned position; adjust the Horspool-style distance to that mismatch location, then require at least one step.

<!-- qard-id: ap-4c52cadf741782cb51c1 -->
> [!qard]- Why reject a good-suffix occurrence preceded by the same pattern character as the original mismatch position?
> The known mismatching text character would meet that same pattern character again, so the alignment is already ruled out.

<!-- qard-id: ap-c755c22efaaf053c7684 -->
> [!qard]- What is the role of the longest prefix fallback in good-suffix shifting?
> If the whole matched suffix has no suitable earlier occurrence, retain possible overlap by matching its ending portion to a pattern prefix rather than skipping a valid alignment.

<!-- qard-id: ap-3451feffa0332e8167f2 -->
> [!qard]- What boundary cases do the notes' string matchers handle before an ordinary comparison loop?
> Return zero for an empty pattern; a nonempty pattern longer than the text has no valid alignment. Bounds must prevent comparing outside either string.
