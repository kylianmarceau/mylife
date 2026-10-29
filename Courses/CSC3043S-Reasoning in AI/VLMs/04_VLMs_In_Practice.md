---
tags:
  - reasoning-in-ai
---

# VLMs for Image Understanding in Practice

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Vision-Language Models  
> **Source**: [Lecture4_VLMs_in_Practice.pptx](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/VLM%27s/Lecture4_VLMs_in_Practice.pptx), Prof Patrick Marais, slides 1-27 (primary reports: Qwen2.5-VL, Bai et al. 2025; InternVL3, Zhu et al. 2025; POPE, Li et al. 2023)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Components of production VLMs|Components of production VLMs]]
  - [[#The three-stage training pipeline|The three-stage training pipeline]]
  - [[#The visual SFT portfolio|The visual SFT portfolio]]
  - [[#Preference tuning with vision|Preference tuning with vision]]
  - [[#Capability 1: open visual question answering|Capability 1: open visual question answering]]
  - [[#Capability 2: grounding as text tokens|Capability 2: grounding as text tokens]]
  - [[#Capability 3: OCR and document understanding|Capability 3: OCR and document understanding]]
  - [[#Image resolution: fixed versus native|Image resolution: fixed versus native]]
  - [[#Capability 4: charts, tables, and diagrams|Capability 4: charts, tables, and diagrams]]
  - [[#Capabilities 5 and 6: multi-image reasoning and GUI agents|Capabilities 5 and 6: multi-image reasoning and GUI agents]]
  - [[#The capability frontier|The capability frontier]]
  - [[#Common VLM benchmarks|Common VLM benchmarks]]
  - [[#Three ways scores mislead|Three ways scores mislead]]
  - [[#What hallucination looks like|What hallucination looks like]]
  - [[#Why hallucination happens|Why hallucination happens]]
  - [[#Measuring hallucination with POPE|Measuring hallucination with POPE]]
  - [[#Mitigating hallucination|Mitigating hallucination]]
  - [[#Practical guidance|Practical guidance]]

---

## Core Content

### Components of production VLMs

#### Definitions

> **Merger / projector**: The small MLP connecting the vision tower to the LLM — the "bridge" of lecture 3, under the name used in VLM papers.

> **M-RoPE (multimodal RoPE)**: Rotary position encoding factorized over (time, height, width), used in the LLM decoder so every token has a spatial-temporal position.

![Production VLM stack](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/04_VLMs_In_Practice/production-stack.svg)

*A native-resolution ViT with 2D positions feeds a 2×2 patch merger and projector into an LLM decoder, which outputs text, boxes, points, or JSON.*

| Component | Production version |
|---|---|
| Vision tower | Contrastively/natively pretrained ViT with lecture 1's upgrades: 2D rotary positions, variable input size, windowed attention for large images |
| Merger / projector | Small MLP (scaled-up LLaVA design). Common trick: aggregate $2 \times 2$ neighbouring patch features → $4\times$ fewer tokens at little cost |
| LLM | Open decoder (Qwen, InternLM, ...) with M-RoPE, fine-tuned |
| Output | Text, including coordinates, JSON, structured answers |

Two VLM families share this blueprint:

| Family | Approach |
|---|---|
| **Qwen-VL** | Tower + merger + LLM, then joint training |
| **InternVL** | Adds native multimodal pretraining: vision and language trained together from early on, not bolted on later |

### The three-stage training pipeline

![VLM training stages](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/04_VLMs_In_Practice/training-stages.svg)

*The LLM pipeline (pretrain → SFT → preference tuning) with visual data at every stage.*

| Stage | Data | Teaches |
|---|---|---|
| 1. Multimodal pretraining | Billions of image-text tokens: captions, interleaved web, OCR pairs | Raw visual-linguistic knowledge |
| 2. Visual SFT | Millions of curated (image, instruction, response) samples | Tasks, formats, conversation |
| 3. Preference tuning | DPO/RLHF on chosen vs rejected responses, incl. anti-hallucination | Judgement, honesty, style |

This maps directly to the LLM stack (pretrain → SFT → RLHF/DPO). The algorithms are the same; **the data is where vision is integrated**.

- Stage 1's scale dwarfs LLaVA's 595K pairs: hundreds of billions of multimodal tokens mixing captions, interleaved documents, OCR, grounding, and synthetic data.
- Stage 2 is SFT against a **capability portfolio**, not a single dataset.
- Stage 3 adds a vision-specific objective: penalize confident descriptions of things not in the image.
- Tower, merger, and LLM are all unfrozen at some phase. The "frozen capital" idea is dropped at production scale (models costing hundreds of millions to a billion dollars to train).

### The visual SFT portfolio

| Data type | Teaches | Example |
|---|---|---|
| Captioning / description | Grounded, fluent description | "Describe this image in detail." → paragraph |
| VQA (natural + academic) | Question answering, short-form accuracy | "What colour is the umbrella?" → "red" |
| Grounding / referring | Localization; binding language to space | "Find the man in the red shirt" → box coordinates |
| OCR and documents | Reading text, layout, forms, receipts | "What is the invoice total?" → "R 228.13" |
| Charts / tables / diagrams | Structured visual reasoning | "Which quarter grew fastest?" → analysis |
| Multi-image / interleaved | Comparison, narrative across images | "What changed between these photos?" |
| GUI / screenshots (agentic) | UI understanding and action grounding | "Click the export button" → coordinates |
| Text-only mixture | Preserving pure language ability | Prevents forgetting |

> [!info] <span style="color: #66b3ff">Capabilities are curated</span>
> If a VLM has a capability, someone probably made data for it. Supposedly "emergent" visual skills are mostly curated ones. Remember this when a model seems magical, or when yours lacks a skill.

### Preference tuning with vision

The text mechanics are the same as for LLMs: collect (prompt, chosen, rejected) tuples and optimize with DPO or an RLHF reward model. Vision adds new kinds of pairs (informal names):

| Pair type | Chosen | Rejected |
|---|---|---|
| Faithfulness | Describes only what is visible | Plausible but adds a non-existent object (classic hallucination) |
| Precision | Reads the actual number/text off a chart | Estimates from prior knowledge |
| Refusal | Says "the image doesn't show this" when it doesn't | Answers anyway |

**Why SFT alone cannot fix hallucination**: SFT maximizes the likelihood of good answers and never shows the model a bad answer to move away from. Preference tuning provides a **negative signal**. Examples in the literature: LLaVA-RLHF, RLHF-V, plus in-house preference phases in production reports (often vaguely described).

### Capability 1: open visual question answering

The most basic capability: any question, grounded in the image, answered in language.

| Kind | Example |
|---|---|
| Perception | "What breed is the dog?" · "What does the sign say?" |
| Reasoning | "Why might the road be wet?" · "What happens next?" |
| Knowledge fusion | "What landmark is this, and when was it built?" — pixels select the entity; the LLM's world knowledge supplies the facts |

VQA is deceptively hard to evaluate:

- Open-ended answers have many valid phrasings, so benchmarks force short answers or use LLM judges.
- Many questions are answerable from **language priors** alone ("What colour is the grass?"). A model can score well while barely looking, which affects benchmarking and hallucination.

### Capability 2: grounding as text tokens

#### Definitions

> **Grounding**: Producing a localization (bounding box or point) for an object or element in the image.

> USER: Find every coffee cup. Report boxes as JSON.
> MODEL: `[{"label":"coffee cup","bbox":[712,418,864,590]}, {"label":"coffee cup","bbox":[1024,388,1189,566]}]`

- Boxes and points are emitted as **ordinary text tokens** (numbers). There is no detection head or special architecture.
- This works because M-RoPE anchors positions to absolute image coordinates: the model knows where each patch is in pixels.
- Current models ground in absolute pixel coordinates at native resolution, without fixed resizing.

| Variant | Output |
|---|---|
| Referring | "the man in red" → box |
| Pointing | Single click coordinates |
| Dense / open-vocabulary | "every vehicle" → many boxes |

An answer with coordinates is **checkable**. Grounding is used to combat hallucination and enables action selection for GUI agents.

### Capability 3: OCR and document understanding

The range runs from "what does the sign say?" to full document parsing:

- **Reading**: scene text, handwriting, multilingual, rotated/curved text (e.g. scanned pages).
- **Structure**: forms, invoices, tables → key-value extraction, often directly as JSON/HTML/markdown.
- **Long documents**: multi-page contracts and papers, answering with the page/region the answer came from.

Why this was the hardest capability:

- Characters are tiny relative to the image: a 10 px character inside one 14 px patch is at the edge of resolvability.
- BLIP-2's 32-token bottleneck destroys this detail; LLaVA's fixed 336 px often does too.
- It was solved with **data and resolution**: huge OCR corpora in pretraining plus native-resolution towers.

"Document AI" (receipts, invoices, forms) is a flagship commercial use case, measured by **DocVQA**.

### Image resolution: fixed versus native

**Fixed resizing destroys information.** A receipt's total that is legible at full resolution is unrecoverable at 224 px; no model can read pixels that no longer exist. Fixed-resolution ViTs (224/336 defaults) were designed for "what object is this?", not "what does line 9 say?".

#### Definitions

> **Native dynamic resolution**: Patchifying each image at its native resolution and aspect ratio, so the token count varies per image under a budget cap.

> **AnyRes tiling**: The predecessor approach (LLaVA-NeXT): cut a large image into fixed-size tiles plus a thumbnail.

![Dynamic resolution](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/04_VLMs_In_Practice/dynamic-resolution.svg)

*A landscape photo, a tall receipt, and a small icon get differently shaped token grids (48, 40, and 16 here), preserving aspect ratio and spending tokens where needed.*

Native resolution needs:

1. **2D RoPE** — no interpolation step; relative offsets generalize.
2. **Windowed attention** — keeps $O(n^2)$ affordable on pages of about 3000 tokens.
3. **A $2 \times 2$ patch merger** — reduces the sequence length.

AnyRes is simpler but has tile seams and redundant tokens; native patching won.

> [!tip] <span style="color: #5ad4b5">Rule of thumb</span>
> If the task involves reading, use the highest image resolution your budget allows. Resolution is the cheapest accuracy you can buy.

### Capability 4: charts, tables, and diagrams

This differs from OCR: the marks are machine-readable, but meaning lies in **layout geometry and chart conventions**.

| Task | Example |
|---|---|
| Read exact values | Bar heights, axis labels, legends — must be accurate |
| Analyze | "Which region grew fastest 2023→2025?" = read, convert, recover numbers, subtract, compare |
| Convert | Chart → data table / JSON; flowchart → steps; schematic → explanation |

![Chart reading example](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/04_VLMs_In_Practice/chart-reading-example.svg)

*Answering a question about this chart means reading the exact series values (e.g. the visible peak of 83), not guessing what such charts usually show.*

- **Common failure**: "priors over pixels" — the model knows what typical charts look like and hallucinates an answer.
- **Benchmark**: ChartQA. Its machine-generated vs human-written split exposes template overfitting.
- For scientific data extraction from figures, verify: ask the model to output the raw table and spot-check it.

### Capabilities 5 and 6: multi-image reasoning and GUI agents

**Multi-image / interleaved input** (Flamingo's format, now standard):

- Compare: spot the differences, before/after, best-of-N product photos.
- Aggregate: answer questions whose evidence spans several images or pages.
- Images are treated like **video frames**, and M-RoPE's time axis tells the model which image each patch came from, so it can reason coherently across images and text.

#### Definitions

> **GUI agent (computer-using agent)**: A VLM in a control loop that reads screenshots and grounds actions on the interface.

![GUI agent loop](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/04_VLMs_In_Practice/gui-loop.svg)

*Screenshot → decide and ground the next action → execute → new screenshot.*

- Skills: recognize widgets, read state, ground the next action ("click here" is pointing, capability 2).
- A VLM in a control loop **is** an agent.

### The capability frontier

| Reliable today | Usable with care | Still unreliable |
|---|---|---|
| Describing scenes; common-object VQA | Precise counting beyond ~5-10 | Fine-grained spatial relations ("third from the left, behind...") |
| Printed-text OCR at native resolution | Handwriting; dense multi-column layouts | Very long documents end-to-end without retrieval help |
| Single-object grounding / referring | Exhaustive detection of many instances | Pixel-perfect boxes rivalling specialist detectors |
| Chart reading with visible values | Multi-step numeric reasoning over charts | Inferring values that need interpolation without hallucinating |
| 2-8 image comparison | Dozens of images / long interleaving | Consistent object identity across many images |

This is a mid-2026 snapshot; items migrate left over time. Place your task in this table before trusting outputs.

### Common VLM benchmarks

| Benchmark | Probes | What it misses | Mitigation |
|---|---|---|---|
| VQAv2 (2017) | Everyday perception QA | Many questions guessable from language alone ("grass is green") | Pairs each question with two images with different answers; now near saturation |
| MMMU (2024) | College-level multimodal reasoning across 6 disciplines | Many items answerable from general knowledge and elimination | Compare against a text-only "blind" model; the gap shows how much the image mattered |
| DocVQA (2021) | Document reading and layout | Tests extraction, not reasoning; scored by text similarity (ANLS) | Read a high score as "can locate a field" |
| ChartQA (2022) | Chart values and composition | Half the questions are templated and pattern-matchable | Compare human-written and machine-generated splits separately |
| MMBench / MMStar | Broad skill batteries | Answer-letter bias; questions not needing the image | MMBench rotates choices (circular evaluation); MMStar filters image-free questions |
| POPE (2023) | Object hallucination | Only object presence, not attributes or relations | Use alongside a broader hallucination benchmark |

Choose benchmarks by use case: a document-AI product cares about DocVQA, a tutor about MMMU, and **everyone** should care about POPE.

### Three ways scores mislead

1. **Blind solvability — the image isn't needed.**
   - Diagnostic: give the questions to a strong text-only LLM. On many "multimodal" benchmarks it still answers a large share correctly.
   - Fix 1: drop any question a text-only LLM gets right (how MMStar was built from MMBench).
   - Fix 2: balance answers, as VQAv2 does with paired images, so ignoring the image is wrong half the time.
2. **Contamination — the test set is in the training set.**
   - Web-scale crawls increasingly contain benchmark images and questions, sometimes with answers. The model scores by memory, not skill.
   - Mitigations: decontamination filters for near-duplicates; private or refreshed test sets; human-written splits that are harder to scrape.
3. **Format gaming — multiple-choice position bias and prompt sensitivity.**
   - Some models default to a particular letter (e.g. always "C"). **Circular evaluation** (MMBench) asks the same question with shuffled choices and counts it correct only if every ordering is right.
   - Exact-match scoring can mark correct answers wrong for phrasing ("2" vs "two").

When a model "beats humans" on a benchmark, check whether one of these is inflating the score.

### What hallucination looks like

#### Definitions

> **Object hallucination**: Confidently describing an object that is not in the image; the most widely studied kind.

> **Attribute hallucination**: Wrong colour, count, or size.

> **Relation hallucination**: Wrong spatial or interaction claims.

Image: a kitchen counter with a kettle and two mugs (no people, no food).

> USER: Describe the image.
> MODEL: A cozy kitchen scene. A kettle sits on the counter beside two mugs, with a plate of cookies nearby, ready for an afternoon break.

"A plate of cookies" is consistent, plausible, and contextually fitting — and **not in the image**.

Hallucinations badly damage trust because they are confident and plausible, exactly the errors a reviewer skims past. Obvious failures are manageable; these are not.

| Not hallucination | Why |
|---|---|
| Refusing ("I can't tell", "nothing like that is visible") | Declined rather than asserted |
| Hedging ("it might be a cookie, hard to tell") | Flagged its own uncertainty |
| Misreading genuinely ambiguous pixels (blurry, occluded, low-res) | Something real was there; this is a perception error |

### Why hallucination happens

The language prior wins.

| Cause | Mechanism |
|---|---|
| 1. Asymmetric priors | The LLM carries billions of tokens of "how scenes usually are"; the visual evidence is a few hundred tokens. Under uncertainty, generation follows the stronger prior: kettles come with cookies |
| 2. Co-occurrence in training data | Captions mention objects together (kitchen → food, street → cars). The model learns $P(\text{mention} \mid \text{context})$, not $P(\text{present} \mid \text{pixels})$ |
| 3. SFT never says no | Likelihood training on good captions rewards "fluent completeness"; there is no gradient against adding a plausible extra object |
| 4. Attention dilution | Late in long descriptions, attention to image tokens decays and the model conditions on its own text ("snowballing") |

This predicts hallucination is worst for objects that **frequently co-occur with the scene but are absent** — exactly what POPE's adversarial split tests.

### Measuring hallucination with POPE

#### Definitions

> **POPE (Polling-based Object Probing Evaluation)**: A benchmark that asks only yes/no questions, "Is there a <object> in the image?", half about present objects and half about absent ones.

> **CHAIR (Caption Hallucination Assessment with Image Relevance)**: A metric for hallucination in generated captions.

Three ways to choose the absent objects:

| Split | Absent objects |
|---|---|
| Random | Any object |
| Popular | Frequent dataset objects |
| Adversarial | Objects that co-occur with what is present (cookies for kitchens) |

![POPE comparison](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/04_VLMs_In_Practice/pope-comparison.svg)

*Schematic: accuracy drops from random to popular to adversarial negatives; balanced/preference-tuned models drop less than caption-tuned ones.*

Findings:

- **Accuracy falls as negatives get harder**: random → popular → adversarial.
- **Contextual failure**: the model is not worse everywhere, only where denying an object means overriding a strong contextual expectation.
- **"Yes" bias**: even on random negatives, models answer "yes" more often than an unbiased, pixel-driven model should.

Yes/no polling isolates perception-based assertions from caption fluency, length, and phrasing, making it simple to interpret. **H-POPE** gives a more nuanced evaluation.

### Mitigating hallucination

| Lever | Idea | Cost / limits |
|---|---|---|
| Data balance | Include negatives ("no cookies here"), counterexamples that break co-occurrence, refusal samples | Curation effort; must cover the prior's blind spots |
| Preference tuning | Chosen = faithful, rejected = hallucinated; RLHF-V-style fine-grained corrections | Needs good pairs; can over-suppress and make answers timid |
| Decoding-time fixes (no retraining) | Contrastive decoding against a distorted-image run (VCD); penalizing attention-decay patterns (OPERA) | Inference overhead (multiple passes); treats symptoms |
| Grounded output formats | Require support for claims: not just "a laptop on the table" but its bounding box; extract chart values explicitly | A model can still confidently box a non-existent object, so downstream verification is needed; only works for spatially localizable claims ("looks like a birthday party" can't be boxed) |

Hallucination is **mitigated, not solved**. The language prior is also what makes the model smart, so it cannot simply be deleted. Best practice uses all four levers and reports POPE/CHAIR alongside capability scores.

### Practical guidance

1. **Maximize input resolution** for any task involving reading.
2. **Make claims checkable**: ask for boxes, coordinates, or verbatim quotes with locations. A claim you can't localize is a claim you can't trust.
3. **Separate perception from reasoning**: first "list exactly what you can see", then reason over that list. Merging them lets the language prior fill gaps.
4. **Interrogate absences directly**: "Is there X? Answer only from visible evidence; say no if absent." This is your own tiny POPE.
5. **Ask twice, differently**: rephrase and check consistency; hallucinations are often unstable across phrasings.
6. **Match the task to the frontier table**: "usable with care" means checking outputs.
