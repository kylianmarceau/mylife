---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 20A — Artificial Intelligence In Software Development"
---

# ASD 20A — Artificial Intelligence In Software Development

**Source note:** [Artificial Intelligence In Software Development](../../ASD/20A_Artificial_Intelligence.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Kinds Of AI|Kinds Of AI]]
  - [[#Limits|Limits]]
  - [[#Developers, Learning And Security|Developers, Learning And Security]]

## Core Content

### Kinds Of AI

<!-- qard-id: ap-f382b1307aeee5fd3215 -->
> [!qard]- What are the three families of AI?
> Knowledge representation, reasoning, perception.

<!-- qard-id: ap-69bb02d9e863348b6b64 -->
> [!qard]- What is knowledge representation, and why did it fade?
> Hand-built knowledge bases and ontologies; exact but doesn't scale, effectively killed by perception AI.

<!-- qard-id: ap-af7786cf26bd07ab7adf -->
> [!qard]- Exact versus defeasible reasoning?
> Exact: a precise mathematical model (often NP-hard — SAT, ILP, TSP). Defeasible: exact plus "maybe", allowing revisable conclusions.

<!-- qard-id: ap-33b7d796d7dd449a4227 -->
> [!qard]- What is perception AI built from?
> Neural networks — all of generative AI — computed with matrix multiply-add.

<!-- qard-id: ap-9b5d41d67f3c3a223df6 -->
> [!qard]- Why do neural networks suit GPUs?
> Matrix multiplication is almost embarrassingly parallel: $O(n^2)$ memory but $O(n^3)$ work.

<!-- qard-id: ap-2cf17d92bcfe5d280691 -->
> [!qard]- Why was AlexNet (2012) a watershed?
> A deep convolutional network trained on GPUs that far outperformed shallow networks.

<!-- qard-id: ap-5b3e1549b9420a59f497 -->
> [!qard]- Why are smaller number formats (fp8, fp4) a trade-off?
> Faster and smaller but less precise, and they require new hardware.

### Limits

<!-- qard-id: ap-e7bdf5fcc00138409f55 -->
> [!qard]- What does AI scaling show?
> Diminishing returns — each 10× compute buys smaller improvements (poor but predictable scaling).

<!-- qard-id: ap-68bff464163f4e5e77ed -->
> [!qard]- Why can't current AI combine perception and reasoning?
> Perception is fuzzy with unknown knowledge representation; reasoning is rigid and exact — no known algorithm merges them.

<!-- qard-id: ap-894f24503c336d6d2b2b -->
> [!qard]- What do $x\times0$ and $x\times\infty$ imply for neural networks?
> Zeroed information is lost for good; infinite values can't be recovered (possibly causing confabulation).

<!-- qard-id: ap-548f99b79ddf7227d384 -->
> [!qard]- How does pattern matching distort content?
> Extreme patterns get amplified and subtle ones (nuance) vanish into noise.

<!-- qard-id: ap-30ae7248c2476871106f -->
> [!qard]- Name the five stages of the Gartner hype cycle.
> Technology trigger, peak of inflated expectations, trough of disillusionment, slope of enlightenment, plateau of productivity.

### Developers, Learning And Security

<!-- qard-id: ap-bae95dcd695871f053dd -->
> [!qard]- What did the 2025 Stack Overflow survey find about AI use and trust?
> 84% use or plan to use AI tools, but only about a third trust their accuracy.

<!-- qard-id: ap-efe1a778caa5c8ccc392 -->
> [!qard]- What is developers' top frustration with AI tools?
> Solutions that are almost right but not quite (66%).

<!-- qard-id: ap-423ed6e421f23017291c -->
> [!qard]- Summarise UCT CS's generative AI policy.
> Undeclared use is plagiarism; no GenAI in first year; declared, mostly-human work allowed later; 80% of marks from controlled exams.

<!-- qard-id: ap-a9a4fe1f79316ec66c41 -->
> [!qard]- What does research say about AI and student learning?
> Inconclusive: it aids ideas and interaction but can hinder critical thinking; meta-analyses show positive short-term effects with publication-bias caveats.

<!-- qard-id: ap-24aaf4a20f57a9f1e0eb -->
> [!qard]- What fraction of AI-generated code is insecure (Veracode 2025)?
> About 45% contains a known security flaw.

<!-- qard-id: ap-9b4eecb910c551e5c160 -->
> [!qard]- Has AI-generated code security improved with newer models?
> No — syntax improved, security stayed flat, and larger models aren't significantly better.

<!-- qard-id: ap-65beeda80c669fc5f939 -->
> [!qard]- Which weaknesses does AI-generated code handle worst?
> XSS (~13% secure) and log injection (~12%).

<!-- qard-id: ap-e93a0d66c1c0c40f1b1d -->
> [!qard]- Why may GenAI not increase productivity?
> It shifts effort from writing code (~5% of effort) to finding and fixing bugs (~50%).

<!-- qard-id: ap-edf29230867a905e569e -->
> [!qard]- List Bloom's taxonomy from lower to higher order.
> Remember, understand, apply, analyse, evaluate, create.
