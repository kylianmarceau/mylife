---
tags:
  - reasoning-in-ai
---

# Bridging Vision and Language: Fusion Architectures

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Vision-Language Models  
> **Source**: [Lecture3_Fusion_Architectures.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/VLM%27s/Lecture3_Fusion_Architectures.pdf), Prof Patrick Marais, slides 1-31 (primary papers: Alayrac et al. 2022; Li et al. 2023; Liu et al. 2023)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What is missing: the bridge|What is missing: the bridge]]
  - [[#Components to optimize over|Components to optimize over]]
  - [[#Design axis 1: where vision enters|Design axis 1: where vision enters]]
  - [[#Design axis 2: what gets trained|Design axis 2: what gets trained]]
  - [[#The token-budget problem|The token-budget problem]]
  - [[#Flamingo: few-shot learning with vision|Flamingo: few-shot learning with vision]]
  - [[#Perceiver Resampler|Perceiver Resampler]]
  - [[#Gated cross-attention|Gated cross-attention]]
  - [[#Flamingo summary|Flamingo summary]]
  - [[#BLIP-2 and the Q-Former|BLIP-2 and the Q-Former]]
  - [[#Inside the Q-Former|Inside the Q-Former]]
  - [[#BLIP-2 two-stage pretraining|BLIP-2 two-stage pretraining]]
  - [[#BLIP-2 summary|BLIP-2 summary]]
  - [[#LLaVA: core architecture|LLaVA: core architecture]]
  - [[#Manufactured instruction data|Manufactured instruction data]]
  - [[#LLaVA two-stage training|LLaVA two-stage training]]
  - [[#Why the simplest bridge won|Why the simplest bridge won]]
  - [[#The three bridges compared|The three bridges compared]]
  - [[#Native multimodality|Native multimodality]]
  - [[#How the field evolved and which design to use|How the field evolved and which design to use]]

---

## Core Content

### What is missing: the bridge

| Side | Strength | Missing |
|---|---|---|
| Image (CLIP) | Matches text to images | Cannot say anything fine-grained; one 512-d vector per image; can only rank candidate sentences you supply. "What is unusual about this image?" has no candidate list — it needs open-ended generation |
| Text (LLM) | Generates, reasons, follows instructions | No access to image understanding |

We have a vision encoder and an LLM, both expensive, pretrained, and frozen. How can the LLM condition its text generation on pixels?

#### Definitions

> **Bridge (connector / adapter)**: A component that maps visual embeddings into a representation resembling a text-embedding sequence that the LLM can parse and reason about.

![Projection bridge](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/projection.svg)

*The image passes through a vision encoder ($D_v$-dimensional features); the bridge maps $D_v \rightarrow D_t$ so the LLM can generate text from them.*

### Components to optimize over

| Component | What it gives | Interface | Cost to retrain |
|---|---|---|---|
| Vision encoder (ViT, CLIP/SigLIP-pretrained) | Semantically rich patch tokens, already language-adjacent from contrastive pretraining | $N \times D_v$ tokens, e.g. $576 \times 1024$ for ViT-L/14@336 | High |
| LLM (GPT-style decoder) | Generation, world knowledge, reasoning, instruction following | Sequences of $D_t$-dim token embeddings | Very high (weeks × thousands of GPUs) |
| Bridge | Maps vision tokens into LLM input | $D_v \rightarrow D_t$, possibly $N \rightarrow$ fewer | **Low** — the part we can afford to train |

- Retraining the vision and text components is very costly, so connect them with the fewest new parameters.
- CLIP-style pretraining helps: its features already correlate with language.
- The bridge works with rich image features, not raw pixels.

### Design axis 1: where vision enters

#### Definitions

> **Concatenation ("visual tokens as words")**: Projecting image tokens into the LLM's embedding space and placing them in the same sequence as text tokens.

> **Cross-attention ("vision on the side")**: Adding new layers between LM blocks in which text queries attend to visual features as keys/values; vision never enters the token sequence.

| | Option A: concatenation | Option B: cross-attention |
|---|---|---|
| LLM | Unmodified; vision arrives as "foreign words" | New layers inserted between frozen LM blocks |
| Attention | Standard self-attention over everything; every layer sees vision and text | Text queries attend to vision in inserted layers |
| Strength | Simplest to implement (LLaVA, most modern VLMs) | LLM context is not used by image tokens — good for many interleaved images (Flamingo) |
| Cost | Image tokens occupy context (576 per image adds up fast) | New parameters at every insertion; more invasive LM changes |

> [!info] <span style="color: #66b3ff">Which image features?</span>
> Concatenation does **not** use CLIP's single pooled embedding. It uses the full set of per-patch ViT output tokens from before pooling.

### Design axis 2: what gets trained

| Approach | Vision encoder | Bridge | LLM | Trainable share | Used by |
|---|---|---|---|---|---|
| Bridge only | Frozen | Trained | Frozen | ~1-3% | Flamingo, BLIP-2, LLaVA stage 1 |
| Bridge + LLM | Frozen | Trained | Fine-tuned | 95-98% | LLaVA stage 2 |
| Everything | Trained | Trained | Trained | 100% | Native multimodal models |

#### Definitions

> **Catastrophic forgetting**: Loss of previously learned abilities when a model is fine-tuned on new data.

Why freezing was favoured:

- **Compute**: training 1-3% of parameters fits research budgets.
- **Context preservation**: fine-tuning an LLM on small multimodal datasets risks catastrophic forgetting of language ability; freezing retains its reasoning skills.
- **Data**: web image-text pairs were plentiful, but high-quality multimodal data was scarce (until LLaVA created it).

### The token-budget problem

- ViT-L/14@336 gives **576 patch tokens per image**.
- A webpage with 8 images ≈ **4,600 visual tokens**, before any text.
- With 2022 context limits around 2k tokens, this was not viable.
- This motivated **compressing** the visual token stream with a learned module.

By 2024+, contexts grew to millions of tokens, so keeping all (or many more) tokens became viable, enabling fine-grained image-text interaction.

### Flamingo: few-shot learning with vision

#### Definitions

> **Flamingo**: A VLM that extends GPT-3-style few-shot prompting to interleaved image-text prompts, using a frozen LLM (Chinchilla, up to 70B) plus small new modules (Alayrac et al., 2022).

The input is an interleaved sequence: e.g. four (photo, caption) examples, then a fifth photo, and the model continues with its caption.

The design must:

1. Handle many images per prompt.
2. Not disturb the frozen pretrained LLM.

Two new modules, both small relative to the LM:

- **Perceiver Resampler**: compresses an image's (or video frames') features into 64 tokens.
- **Gated cross-attention layers**: inserted between frozen LM blocks; text attends to vision.

Result (2022): one model, 32-shot prompted, beat or matched fine-tuned task-specific SOTA on 6 of 16 benchmarks.

![Flamingo architecture](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/flamingo.svg)

*Images/frames pass through a frozen NFNet-F6 encoder and a trainable resampler (64 latent queries). Gated cross-attention layers (text as Q, vision as K/V) are interleaved with frozen LM blocks processing the interleaved text.*

### Perceiver Resampler

#### Definitions

> **Perceiver Resampler**: Cross-attention in which the queries are a fixed set of **learned latent vectors** (parameters, not from data) and the keys/values are visual features, producing a fixed-size output from variable-size input.

1. Take the vision encoder features (any number of frames × patches).
2. Use 64 learned latent queries.
3. Apply $L$ layers of cross-attention: queries = latents, keys/values = visual features.
4. Output: always 64 visual tokens.

- Output length equals the number of queries, regardless of input length: 1 image or 30 video frames in, 64 tokens out.
- Each query learns to "ask for" a kind of content (objects, layout, text, ...) — a learned fixed-size summary.
- Flamingo needs it because interleaved prompts contain many images; 64 tokens per image keeps cross-attention cheap and uniform.

The idea of learned queries compressing a modality reappears in BLIP-2's Q-Former and in video models.

### Gated cross-attention

#### Definitions

> **Gated cross-attention (`tanh` gate)**: A residual update scaled by $\tanh(\alpha)$, where $\alpha$ is a learned scalar initialized to $0$.

$$
z \leftarrow z + \tanh(\alpha) \cdot \text{XAttn}(\text{text}, \text{vision}), \qquad z \leftarrow z + \tanh(\alpha) \cdot \text{FFW}(z), \qquad \alpha_{\text{init}} = 0
$$

At initialization $\tanh(0) = 0$, so the new layers are invisible and the network is **exactly the original frozen LM**. Training opens each gate only as fast as it proves useful; different layers open differently.

![Tanh gate](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/tanh-gate.svg)

*$\tanh(\alpha)$ starts at zero and smoothly allows positive or negative visual contributions as $\alpha$ is learned.*

**Why gating is needed:**

| Without gating | With gating |
|---|---|
| An untrained cross-attention layer in a 70B LM outputs random values that corrupt every downstream activation, damaging language ability before learning starts | Added layers compute the identity at step 0. The model starts as a "fully functional blind LM" and moves continuously towards "vision-enabled LM", never passing through a broken state |
| | Early gradients flow into the resampler/bridge while LM behaviour stays intact, so the training signal is clean |

> [!tip] <span style="color: #5ad4b5">General principle</span>
> "Initialize new additions to identity/zero" recurs across the field: zero-init projections, LoRA's zero-init $B$ matrix, ControlNet's zero-convolutions. Gating solves a **training dynamics** problem: integrating new data stably while preserving frozen knowledge.

### Flamingo summary

| Aspect | Flamingo-80B (2022) |
|---|---|
| Language model | Chinchilla-70B, frozen |
| Vision model | Contrastively pretrained NFNet-F6 (in-house CLIP-style; not a ViT — the approach is encoder-agnostic) |
| New parameters | ~10B (resampler + gated layers) |
| Training data | Interleaved web pages (M3W) + image/video-text pairs; no human labels |
| Result | Few-shot prompting beats fine-tuned SOTA on 6/16 tasks; strong VQA/captioning with 32 examples |

Limits:

- Closed weights and enormous: nobody outside DeepMind could build on it directly.
- Few-shot prompting is not conversation: it completes patterns but does not follow instructions.
- Open-source reproductions followed: **OpenFlamingo** and **IDEFICS** (Hugging Face), 2023.

### BLIP-2 and the Q-Former

#### Definitions

> **BLIP-2 (Bootstrapping Language-Image Pretraining)**: A VLM whose bridge is itself a small pretrained model, the Q-Former, connecting a frozen image encoder to a frozen LLM (Li et al., 2023).

> **Q-Former (Querying Transformer)**: A BERT-sized (~188M) Transformer with 32 learned query tokens that extract language-relevant visual features.

"Bootstrapping" means building good general image-language performance from many examples, on top of frozen components.

![BLIP-2 pipeline](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/blip2.svg)

*Frozen EVA-CLIP patch features → Q-Former (32 learned queries) → linear projection to LLM width → frozen OPT / FlanT5.*

Two-stage training of the Q-Former:

1. **Stage 1**: learn vision-language alignment against the frozen image encoder using three objectives. No LLM is involved.
2. **Stage 2**: feed the 32 output tokens (through one linear layer) into a frozen LLM (OPT or FlanT5) and further train the Q-Former to produce image-conditioned prompts. Works with decoder or encoder-decoder LLMs.

Intuition: the Q-Former is an interpreter between two "language experts" — it first learns the vision language (stage 1), then how to phrase things for the LLM (stage 2).

### Inside the Q-Former

The Q-Former is a BERT-base-initialized Transformer with two input streams:

| Stream | Content | Interaction |
|---|---|---|
| 1 | 32 learned query embeddings (768-d) | Cross-attend to image features (cross-attention inserted every other block) |
| 2 | Text tokens | Share the same self-attention layers as the queries |

- **Attention masks** switch the mode: queries only, queries ↔ text, or causal text. Three losses are computed jointly.
- **Output**: exactly 32 tokens of 768-d — a large compression of the ViT's token stream.
- Similar to the Perceiver Resampler (learned queries as a fixed-size bottleneck), but the queries are also trained to be **relevant to text**, not just compact.

> [!warning] <span style="color: #ff939b">Bottleneck limits</span>
> 32 well-chosen "visual sentences" suffice for most language tasks about an image, but not for OCR or documents, where detail is lost in the bottleneck.

### BLIP-2 two-stage pretraining

**Stage 1 losses:**

| Loss | Task | Attention mask |
|---|---|---|
| **ITC** — image-text contrastive | Align query outputs with the text embedding (best of 32 similarities) | Unimodal: queries and text attend only to themselves |
| **ITM** — image-text matching | Binary classification: does this pair match? (with hard negatives) | Bidirectional: all queries attend to all text |
| **ITG** — image-grounded generation | Generate the caption conditioned on the queries | Causal on text; text sees queries |

Contrastive gives global alignment, matching adds fine discrimination, and generation forces completeness. The queries must satisfy all three, which makes 32 tokens descriptive enough to pass to an LLM.

**Stage 2:**

1. Connect the stage-1 Q-Former to a small projection (only 1-2M parameters) mapping to the LLM's token dimension.
2. Adjust the Q-Former and projection weights for text generation (language modelling loss).
3. No text enters the Q-Former here — only the frozen LLM receives text.

### BLIP-2 summary

Compared with Flamingo:

- **54× fewer** trainable parameters.
- **+8.7%** on VQAv2.

What it showed (early 2023):

- You do not need 10B new parameters; a good 188M bridge suffices.
- Frozen instruction-tuned LLMs (FlanT5) pass their zero-shot instruction skills through the bridge.
- Compute is university-scale: under 9 days on 16 A100s. The open-VLM wave (LLaVA, InstructBLIP, MiniGPT-4) built on this.

Where it still failed:

- Real conversation and instruction following were weak: the LLM was frozen and the data was captions, not dialogues.
- Only one image plus text questions.

### LLaVA: core architecture

#### Definitions

> **LLaVA (Large Language and Vision Assistant)**: A VLM that connects a frozen CLIP ViT to an open chat LLM (Vicuna) with a simple projection and trains on GPT-4-generated visual instruction data (Liu et al., 2023).

> **Visual instruction tuning**: Fine-tuning a VLM on (image, instruction, response) data so it can converse about images.

![LLaVA](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/llava.svg)

*Frozen CLIP produces 576 patch tokens; a linear/MLP projector maps them into Vicuna, which is tuned in stage 2 to respond to image + instruction.*

Input format: `<image tokens> USER: What is unusual about this image? ASSISTANT: ...` — vision enters as ordinary sequence tokens (axis 1, option A).

| Model | Bridge |
|---|---|
| Flamingo | ~10B parameters of gated layers |
| BLIP-2 | 188M Q-Former pretrained with a complex loss |
| LLaVA | A projection matrix $W$ (v1: linear; v1.5: 2-layer MLP) |

- All **576 tokens are kept** — no compression. Fine detail survives, at the cost of context.
- The LLM is open (Vicuna) and is **fine-tuned in stage 2**, abandoning the "never touch the LM" doctrine.

So where does the capability come from, if not the architecture? **The data.**

### Manufactured instruction data

In 2023, no dataset of (image, instruction, good response) triples existed. LLaVA's insight: have **text-only GPT-4** write it.

1. Give GPT-4 the **symbolic descriptions** of a COCO image (captions + object bounding boxes). It never sees pixels.
2. Prompt it to produce three output types (158K samples total):

| Type | Count | Content |
|---|---|---|
| Conversations | 58K | Multi-turn Q&A about the scene |
| Detailed descriptions | 23K | Dense paragraph captions |
| Complex reasoning | 77K | Questions needing inference ("What challenges might these people face?") |

This is **knowledge distillation across modalities**: a blind strong model teaches a sighted small one how to talk about scenes. Synthetic instruction data now underpins most open VLM training.

### LLaVA two-stage training

| | Stage 1: feature alignment | Stage 2: visual instruction tuning |
|---|---|---|
| Data | 595K filtered image-text pairs (CC3M) | 158K GPT-4-generated instructions |
| Trained | Projection $W$ only (ViT and LLM frozen) | $W$ + the **whole LLM** (ViT frozen) |
| Goal | "Teach $W$ to speak Vicuna's embedding dialect" | "Learn to converse about what you see" |

- **Why stage 1**: if $W$ is random, LLM fine-tuning wastes its budget repairing garbled inputs. Align the interface first, cheaply.
- **Why stage 2 fine-tunes the LLM**: instruction following about images is a new skill; a frozen LM can imitate formats but not integrate vision deeply. Forgetting is limited because stage-2 data is conversational, close to the LM's home distribution.
- **Cost**: LLaVA-1.5 trains in about 1 day on 8 A100s, versus thousands of TPU-days for Flamingo and ~16 A100s × 9 days for BLIP-2.
- **LLaVA-1.5** made small changes (MLP instead of linear, 336 px input, academic VQA data mixed in) and reached SOTA on 11 benchmarks with a trivial architecture.

### Why the simplest bridge won

1. **The components were already well trained.** CLIP aligned visual features to language; Vicuna's instruction tuning made the LM conversational. The gap between them was small enough for an MLP.
2. **Data quality beats architecture.** 158K on-distribution instruction dialogues taught reasoning and conversation; BLIP-2's architecture with caption data still could not chat.
3. **Fine-tuning the LLM simplified integration.** Frozen-LM designs limit how deeply vision can affect reasoning; careful fine-tuning removes that limit.
4. **Simple is easy to extend.** Fewer components made reproduction, ablation, and extension easy; the community iterated on LLaVA rapidly while Flamingo could not be iterated on at all.

> [!tip] <span style="color: #5ad4b5">Design lesson</span>
> When expensive pretrained components are already capable, the interface can be simple. Focus on more and better data and well-engineered losses instead.

### The three bridges compared

| | Flamingo (2022) | BLIP-2 (2023) | LLaVA / 1.5 (2023) |
|---|---|---|---|
| Bridge | Perceiver Resampler + gated cross-attention | Q-Former (BERT-sized, 3-objective pretrained) | Linear → 2-layer MLP projection |
| Where vision enters | Cross-attention every few LM blocks | 32 prompt tokens (concatenation) | 576 sequence tokens (concatenation) |
| Tokens per image | 64 | 32 | 576 — detail preserved |
| LLM | Frozen (Chinchilla-70B) | Frozen (OPT / FlanT5) | Fine-tuned (Vicuna) in stage 2 |
| Main data | Interleaved web pages (M3W) | Web image-text pairs | GPT-4-written instruction dialogues |
| Good at | Few-shot, multi-image, video in prompt | Parameter efficiency (188M trained) | Conversation and instruction following |
| Bad at | Closed, huge, no chat | Bottleneck destroys detail; weak dialogue | Context cost; single image (v1) |

### Native multimodality

#### Definitions

> **Early fusion (native multimodality)**: Merging image and text into one token stream before a single Transformer sees them, trained on mixed tokens from the start, with no frozen parts or adapter.

> **Late fusion**: Using existing separate towers to produce image and text tokens, then combining them.

> **Vector quantizer (VQ) tokenizer**: A learned tokenizer that maps images to discrete codebook IDs in the same vocabulary as text.

| Image token type | Example | How |
|---|---|---|
| Continuous | Fuyu | Patch embeddings go straight into the decoder; Fuyu deletes the vision encoder — a linear layer on raw patches is the "vision model" (like ViT's first layer) |
| Discrete | Chameleon | A VQ tokenizer maps images to codebook IDs; images can be **generated** with the same next-token loop |

- **Benefit**: one set of weights handles any interleaving, plus both understanding and generation.
- **Cost**: full-scale pretraining from scratch, plus real training-stability problems (the Chameleon paper covers many tricks).

### How the field evolved and which design to use

- Production open VLMs (Qwen-VL, InternVL) did **not** go fully early-fusion. They scaled up the LLaVA shape: strong ViT tower + MLP projector + fine-tuned LLM, with native resolution, M-RoPE, and massive joint training.
- Compression modules shrank or vanished for images (contexts grew; detail matters), but the **resampler idea is still needed for video**, where token counts explode.
- Early fusion dominates the unified understanding-and-generation frontier.

| If you need... | Choose... | Because... |
|---|---|---|
| Search / retrieval / deduplication at scale | Two-tower CLIP/SigLIP | Embeddings precompute and index; no fusion needed |
| Chat about single images with fine detail (OCR, docs) | Projector + instruction-tuned LLM (LLaVA type) | All tokens kept; conversation from instruction data |
| Many images / video in one prompt, compact context | Resampler/Q-Former compression (or cross-attention) | Fixed small token cost per image |
| Cheapest adaptation of existing models | Frozen everything + small bridge (BLIP-2 type) | ~1% trainable parameters; days of compute |
