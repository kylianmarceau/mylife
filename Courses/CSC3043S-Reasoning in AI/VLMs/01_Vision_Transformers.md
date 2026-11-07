---
tags:
  - reasoning-in-ai
---

# Introduction and Vision Transformers

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Vision-Language Models  
> **Source**: [Lecture1_Vision_Transformers.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/VLM%27s/Lecture1_Vision_Transformers.pdf), Prof Patrick Marais, slides 1-30 (primary papers: Dosovitskiy et al. 2020; Touvron et al. 2021)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Why vision and language|Why vision and language]]
  - [[#Module overview|Module overview]]
  - [[#The text pipeline and what must change|The text pipeline and what must change]]
  - [[#Why not attend over pixels|Why not attend over pixels]]
  - [[#Patches as tokens|Patches as tokens]]
  - [[#Patch embedding: flatten and project|Patch embedding: flatten and project]]
  - [[#ViT-B/16 at a glance|ViT-B/16 at a glance]]
  - [[#The CLS token and the input sequence|The CLS token and the input sequence]]
  - [[#The complete Vision Transformer|The complete Vision Transformer]]
  - [[#Text transformer versus ViT|Text transformer versus ViT]]
  - [[#Why position matters for patches|Why position matters for patches]]
  - [[#Sinusoidal versus learned position embeddings|Sinusoidal versus learned position embeddings]]
  - [[#What learned position embeddings discover|What learned position embeddings discover]]
  - [[#Changing resolution by interpolation|Changing resolution by interpolation]]
  - [[#Relative and rotary positions|Relative and rotary positions]]
  - [[#Inductive biases: CNN versus ViT|Inductive biases: CNN versus ViT]]
  - [[#Data scale: why ViT needs data|Data scale: why ViT needs data]]
  - [[#Interlude: ResNet|Interlude: ResNet]]
  - [[#Local heads emerge inside ViTs|Local heads emerge inside ViTs]]
  - [[#Model sizes and patch size|Model sizes and patch size]]
  - [[#DeiT: closing the data gap with distillation|DeiT: closing the data gap with distillation]]
  - [[#Where ViTs appear later|Where ViTs appear later]]

---

## Core Content

### Why vision and language

#### Definitions

> **Vision-language model (VLM)**: A model that jointly processes images (or video) and text; the core of image/video-to-text systems and a subset of multimodal ML models (video, audio, ...).

| Modality | Typical model | Role |
|---|---|---|
| Images | CNNs and image models | Perception: what is in this image? |
| Text | Transformers / LLMs (GPT etc.) | Language: describe, reason, answer, follow instructions |

Many useful tasks need both:

| Task | Capability |
|---|---|
| "What is the man in the red shirt holding?" | Question answering from image pixels |
| "Read this receipt and total the amounts" | OCR plus reasoning |
| "Find the moment the goal is scored" | Temporal analysis of video frames |
| "A watercolor fox in the snow" | Text as the interface to image generation |

The module also covers generative models, mainly text-to-image.

### Module overview

- **Assumed known**: Transformers (encoder/decoder, self-attention, embeddings), GPT-style LLMs, CNNs, core ML, standard (non-variational) autoencoders.
- **New architectures**: Vision Transformers; VAEs, GANs, and diffusion models (mainly for image generation); architectures built on these. The focus is on concepts more than mathematical formalism.
- **Assessment**: Lab 1 and Lab 2 notebooks (done in the Senior Lab), plus a two-week open prac building and evaluating a simple vision-language understanding application.
- **Resources**: Bishop (*Deep Learning: Foundations and Concepts*) as a technical reference, plus papers and online material.

The lecture has three parts: from words to patches; positional encoding for image tokens; ViT versus CNN. The guiding question is: **what must change to move a Transformer from text to images, and what can stay the same?**

### The text pipeline and what must change

The text pipeline is: raw text "the cat sat" → tokenizer → token IDs `[464, 3797, 3332]` → embedding lookup → $3 \times D$ vectors → add positional encoding → Transformer encoder $\times L$.

The Transformer core is **modality-agnostic**:

- Self-attention only sees "a set of $D$-dimensional vectors with positional information".
- Nothing in $QK^\top/\sqrt{d}$, softmax, MLP blocks, LayerNorm, or residuals mentions text.

So to process images we "only" replace the front of the pipeline, answering two questions:

1. What plays the role of a **token**? (Part I)
2. What plays the role of **position**? (Part II)

![Text versus image pipeline](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/text-vs-image-pipeline.svg)

*Images reuse the whole Transformer; only the front changes: patchify and project instead of tokenize and look up.*

### Why not attend over pixels

The simplest idea is one pixel per token. It fails on cost and meaning.

| Problem | Detail |
|---|---|
| Cost | A $224 \times 224$ image has $50{,}176$ positions. Self-attention is $O(n^2)$, giving $50{,}176^2 \approx 2.5 \times 10^9$ scores per head per layer, versus $\approx 2.6 \times 10^5$ for a 512-token sentence — about $25{,}000\times$ more expensive, before counting memory |
| Meaning | One RGB triple carries almost no meaning, unlike a word. Meaning exists in local groups of pixels — edges, textures, parts. Colour may not even be needed (greyscale images still have structure) |

We need a coarser token: big enough to mean something, cheap enough to compute. The ViT idea is to use $16 \times 16$ patches, reducing $50{,}176$ tokens to $196$.

### Patches as tokens

#### Definitions

> **Vision Transformer (ViT)**: A Transformer encoder applied to a sequence of image patches ("an image is worth 16×16 words").

> **Patch**: A non-overlapping $P \times P$ block of pixels; each patch becomes one token.

> **Raster order**: Reading the patch grid row by row into a 1D sequence, like words in a sentence.

Reading patches in raster order **throws away spatial layout**; positional encodings must put it back.

![Patchify and raster order](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/patchify.svg)

*A $224 \times 224$ image with $P = 32$ becomes a $7 \times 7$ grid of patches, read row by row into a sequence of 49 tokens.*

### Patch embedding: flatten and project

#### Definitions

> **Patch embedding**: Flattening each patch to a vector and mapping it with one shared learned matrix $E$ to the model width $D$.

1. Cut the image into patches.
2. Flatten each $16 \times 16 \times 3$ patch into a $768$-vector.
3. Multiply by one shared learned matrix $E \in \mathbb{R}^{(P^2 C) \times D}$.

The "visual tokenizer" is a **single linear layer** learned during training.

| | Text | Images |
|---|---|---|
| Input values | Discrete vocabulary IDs | Continuous pixel values |
| Embedding | Lookup table | **Projection** replaces lookup |

Projection by $E$ is equivalent to a `Conv2d` with kernel $E$ and stride $P$.

![Patch embedding](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/patch-embedding.svg)

*A $16 \times 16 \times 3$ patch flattens to 768 values and one shared learned matrix $E$ projects it to a $D$-dimensional token, the analogue of an embedding lookup.*

### ViT-B/16 at a glance

"B/16" means the Base model with patch size 16.

| Step | Expression | ViT-B/16 at 224 px |
|---|---|---|
| Input image | $H \times W \times C$ | $224 \times 224 \times 3$ |
| Number of patches | $N = HW / P^2$ | $224 \cdot 224 / 16^2 = 196$ |
| Flattened patch | $P^2 \cdot C$ | $16 \cdot 16 \cdot 3 = 768$ |
| Projection matrix $E$ | $(P^2 C) \times D$ | $768 \times 768$ |
| Sequence to encoder | $(N + 1) \times D$ ($+1$ for `[CLS]`) | $197 \times 768$ |
| Attention cost per head per layer | $O((N + 1)^2)$ | $197^2 \approx 3.9 \times 10^4$ |

- For ViT-L/16, $E$ maps $768 \rightarrow 1024$.
- ViT parameter counts are large: Q, K, V for each of several heads, MLP layers, all depending on $D$ and $N$.

### The CLS token and the input sequence

#### Definitions

> **`[CLS]` token ($x_{\text{class}}$)**: An extra learned vector prepended to the patch sequence, borrowed from BERT. It is not computed from the image; it is the same for every input.

> **Vision tower**: The network branch of a VLM that handles images.

- Through $L$ layers of self-attention, `[CLS]` aggregates information from all patches.
- Its final-layer state $z_0^L$ is "the image representation" fed to the classification head.
- Alternative used by many later models: no `[CLS]`; **mean-pool** all patch outputs. Performance is similar, and this is used in several VLM vision towers.

$$
z_0 = \big[\,x_{\text{class}};\; x_p^1 E;\; x_p^2 E;\; \dots;\; x_p^N E\,\big] + E_{\text{pos}}, \qquad E \in \mathbb{R}^{(P^2 C) \times D}, \quad E_{\text{pos}} \in \mathbb{R}^{(N+1) \times D}
$$

This is essentially the difference between BERT's input and ViT's input.

### The complete Vision Transformer

![Vision Transformer architecture](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/vit-architecture.svg)

*Projected patches plus a learned `[CLS]`, each with a position embedding, pass through $L$ pre-norm encoder blocks; the final `[CLS]` feeds an MLP classification head.*

- Each encoder block is **identical to the text encoder**: multi-head self-attention + MLP, LayerNorm, residuals.
- Every patch attends to every patch from layer 1: a **global receptive field immediately**. A CNN needs many layers to see the whole image.
- Original training: supervised classification on large datasets (ImageNet-21k: 14M images; JFT-300M: 303M), Adam, strong regularization.
- Attention maps show the ViT attending to semantically relevant regions of the image.

The core ViT here targets **image classification**, not object detection or segmentation; later variants address those.

### Text transformer versus ViT

| Component | Text transformer (BERT-style) | Vision Transformer | Status |
|---|---|---|---|
| Tokenization | Subword vocabulary (~30-50k discrete IDs) | $P \times P$ patch grid, continuous, no vocabulary | Changed |
| Embedding | Lookup table (vocab $\times D$) | Shared linear projection $E$, $(P^2C) \times D$ | Changed |
| Position | 1D sinusoidal or learned | Learned 1D over patch index (2D structure emerges) | Adapted |
| `[CLS]` | Learned summary token | Learned summary token | Same |
| Encoder blocks | MSA + MLP, LayerNorm, residuals | Same | Same |
| Attention | Bidirectional, all pairs | Bidirectional, all pairs | Same |
| Training | MLM / next-sentence (self-supervised) | Supervised classification (originally) | Changed |

> [!tip] <span style="color: #5ad4b5">Key point</span>
> Only the **interface** changed; the computation is untouched. That is why one architecture can later host text and images in the same sequence (VLMs).

### Why position matters for patches

#### Definitions

> **Permutation equivariance**: Reordering the input tokens reorders the outputs identically and changes nothing else. Self-attention has this property.

Without positions a ViT sees a **bag of patches**: a scrambled image and the original are the same input.

![Bag of patches](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/bag-of-patches.svg)

*Shuffling the patches gives exactly the same set of tokens, so a position-free Transformer cannot tell the two images apart.*

- In text, losing order is problematic ("dog bites man").
- In vision, spatial arrangement contains all the information. Pixel-level shuffling destroys it; patch-level shuffling is less severe but still loses accuracy.

Design question: patches lie on a 2D grid but the sequence is 1D. Encode "patch #37" or "row 5, column 2"? ViT's answer: just "patch #37", and let the model work out the grid.

### Sinusoidal versus learned position embeddings

The original Transformer used fixed sinusoidal encodings:

$$
PE(pos, 2i) = \sin\!\left(\frac{pos}{10000^{2i/D}}\right), \qquad PE(pos, 2i+1) = \cos\!\left(\frac{pos}{10000^{2i/D}}\right)
$$

They are fixed (not learned), give each position a unique multi-frequency fingerprint, and relative shifts correspond to linear transforms. Attractions for text:

- In principle, extrapolate to unseen lengths.
- No parameters to learn.
- Relative token positions can be learned.

ViT tested these and found **learned embeddings work just as well**. Since $N$ is fixed per resolution, ViT learns $E_{\text{pos}}$ as free parameters.

#### Definitions

> **Learned 1D position embeddings**: A matrix $E_{\text{pos}}$ with $N + 1$ rows (including `[CLS]`), one $D$-vector per sequence slot, randomly initialized and trained by backpropagation.

- Row $i$ is **added** (not concatenated) to token $i$'s embedding, as in BERT.
- "1D" means the matrix knows only the raster index $0 \dots N$; it is told nothing about rows, columns, or a grid.
- **Why adding works**: in high dimensions (e.g. $D = 768$), content and position can occupy near-orthogonal subspaces, so the information stays roughly disentangled.

In a 14-wide grid, patches 13 and 14 are adjacent in the sequence, but 14 and 27 are vertical neighbours. Can the model recover 2D adjacency it was never told?

### What learned position embeddings discover

Comparing each of the $7 \times 7$ learned position embeddings to all 49 (cosine similarity) reveals three properties learned **without supervision**:

| Property | Observation |
|---|---|
| Locality | Nearest 2D neighbours have the most similar embeddings |
| Row/column structure | Same-row and same-column patches are similar (a bright cross through each cell) |
| Smooth distance decay | Similarity falls off gradually with 2D distance |

![Position embedding similarity](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/position-similarity.svg)

*Each small square shows one position embedding's similarity to all 49: brightest at its own location, high along its row and column, and fading with distance (schematic).*

The model infers grid geometry from image statistics. Hand-designed 2D encodings gain almost nothing, so the simple 1D embedding is used.

### Changing resolution by interpolation

$E_{\text{pos}}$ has exactly $N$ rows. A larger image gives more patches with no embeddings — the same issue text has with longer sequences.

1. Reshape the learned embeddings into their spatial grid (excluding `[CLS]`), e.g. $7 \times 7 \times D$.
2. Treat them as samples of a smooth 2D function and **bicubically interpolate** to the new grid, e.g. $10 \times 10 \times D$.
3. Flatten back to a sequence and restore `[CLS]`.

![Position embedding interpolation](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/position-interpolation.svg)

*The learned $7 \times 7$ position grid is bicubically interpolated to $10 \times 10$ for a higher-resolution input, with no retraining.*

- It works because of the learned locality and smoothness. It is the standard trick for fine-tuning ViTs at higher resolution.
- Interpolation shifts effective patch geometry; a short fine-tune at the new resolution recovers (and usually improves) accuracy.

### Relative and rotary positions

| Scheme | Core idea | What it buys for vision | Seen in |
|---|---|---|---|
| Absolute learned | One vector per position added to the input | Simple; good at fixed resolution; interpolates OK | ViT, CLIP's vision tower |
| Relative bias (not covered) | Attention logit gets a learned offset depending on $(\Delta\text{row}, \Delta\text{col})$ | Translation-aware; resolution-robust; windowed variants scale to large images | Swin Transformer |
| 2D RoPE | Rotate Q/K by angles $\propto$ position; relative offsets appear in $QK^\top$; factorized per axis ($x$, $y$, and $t$ for video) | Native dynamic resolution, no interpolation; extends to time | Qwen-VL ("M-RoPE"), most current VLM vision towers |

Every scheme answers: how should attention between two patches depend on their spatial relationship? Absolute schemes use **where each patch is**; relative and rotary schemes use **the offset between them**, which generalizes across resolutions. Native dynamic resolution matters for tasks like reading small text in documents.

### Inductive biases: CNN versus ViT

#### Definitions

> **Inductive bias**: An assumption built into an architecture about the structure of the data.

> **Translation equivariance**: Shifting the input shifts the features correspondingly.

| Bias | CNN | ViT |
|---|---|---|
| Locality | Baked in: kernels see small neighbourhoods | None: any patch can attend to any patch from layer 1 |
| Translation | Weight sharing gives translation-equivariant features for free | Must be learned |
| Scale hierarchy | Built in: pooling/stride builds a coarse-to-fine pyramid | Single resolution throughout (Swin-style models add hierarchy) |
| Receptive field | Grows slowly; global only near the last layers | Global immediately |

### Data scale: why ViT needs data

![ViT versus CNN data scale](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/data-scale.svg)

*On ImageNet alone the BiT ResNets win; at JFT-300M scale large ViTs overtake them (approximate values).*

**BiT** is a very deep ResNet (convolutional) vision model.

| Data | Winner | Why |
|---|---|---|
| Small (ImageNet-1k only) | ResNets | CNN inductive biases act as regularization |
| Large (JFT-300M) | ViT-H/14 overtakes | Learned structure beats built-in structure with enough data |

ViT is also $2$-$4\times$ cheaper to pre-train at matched accuracy. So modality-agnostic Transformers plus huge web-scale image-text pairs enable useful pretraining for language-vision tasks, leading to CLIP.

### Interlude: ResNet

#### Definitions

> **ResNet (Residual Network)**: An architecture of stacked convolution-based residual blocks.

> **Residual block**: A block computing $x' = x + F(x)$, where $F(x)$ is the output of the convolution block (with batch/layer norm etc.).

![Residual block](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/residual-block.svg)

*The input skips around the convolution block and is added to its output, so the block can fall back to the identity.*

- Stacking residual blocks lets exceptionally deep CNNs train stably with great expressive power.
- The skip connection makes it easy to learn an **identity map**: capacity is only used when needed.
- It helps avoid vanishing gradients: errors compound with depth, but the identity path always adds gradient back.

### Local heads emerge inside ViTs

#### Definitions

> **Mean attention distance**: How far (in pixels) a head looks on average; a "receptive field size" for attention.

| Depth | Behaviour |
|---|---|
| Early layers | Heads split: some act like small conv kernels (local), others are already global |
| Deep layers | All heads are global |

![Mean attention distance](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/attention-distance.svg)

*In early layers some heads look locally (CNN-like) and others globally; by the deep layers every head is global (schematic).*

Locality is useful, so ViT learns it where needed but is never limited by it. The CNN inductive bias is a special case ViT can discover.

### Model sizes and patch size

| Model | Layers | Width $D$ | Heads | Params | Tokens at 224 px |
|---|---|---|---|---|---|
| ViT-Base/16 | 12 | 768 | 12 | 86M | $196 + 1$ |
| ViT-Large/16 | 24 | 1024 | 16 | 307M | $196 + 1$ |
| ViT-Huge/14 | 32 | 1280 | 16 | 632M | $256 + 1$ ($P = 14$) |

Patch size $P$ is a resolution/compute dial independent of model size. Token count scales as $1/P^2$:

| $P$ | Tokens at 224 px | Trade-off |
|---|---|---|
| 32 | 49 | Cheap, coarse; fine detail lost inside patches |
| 16 | 196 | Standard operating point |
| 8 | 784 | Fine-grained; $16\times$ the attention cost of $P = 32$ |

Reading model names: "ViT-L/14 @ 336px" is a Large model, patch size 14, 336-pixel input → $(336/14)^2 = 576$ patch tokens. This exact configuration is CLIP's image tower.

### DeiT: closing the data gap with distillation

#### Definitions

> **Knowledge distillation**: Training a student model to match a teacher model's predictions.

> **Distillation token (`[DIST]`)**: An extra learned token, alongside `[CLS]`, trained to predict a pretrained CNN teacher's (hard) labels.

Goal: train a competitive ViT on ImageNet-1k only (1.3M images), on one machine, in about 3 days — versus 300M images for the original ViT.

1. **Aggressive augmentation and regularization**: RandAugment, Mixup, CutMix, random erasing, stochastic depth. Synthetic diversity substitutes for a massive unique dataset.
2. **Learn the missing inductive bias from a CNN teacher**: add `[DIST]` to the input patch embeddings; train with a ground-truth cross-entropy loss on the `[CLS]` prediction plus a distillation loss on the `[DIST]` prediction (teacher vs ViT student).

![DeiT distillation](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/deit-distillation.svg)

*The `[CLS]` output learns from ground-truth labels, while the `[DIST]` output learns from a pretrained CNN teacher, transferring its inductive biases.*

- The CNN's locality and translation knowledge transfers into the ViT through this loss.
- **Result**: DeiT-B reaches $\approx 83.4\%$ ImageNet top-1 with no external data, making ViT training practical for many more groups.
- ViT's "data hunger" can be worked around with augmentation plus teacher knowledge instead of more images.
- In some domains, such as medicine, augmentation may be a problem.

> [!info] <span style="color: #66b3ff">Summary of the three ideas</span>
> **Tokens**: patches are the words of vision — crop, flatten, one shared linear projection; the Transformer itself is untouched. **Position**: learned 1D embeddings discover 2D structure and can be interpolated; modern towers use factorized 2D RoPE. **Biases and scale**: ViT trades CNN biases for data; DeiT closes the gap with augmentation and distillation.

### Where ViTs appear later

| Lecture | Use of ViT |
|---|---|
| 2: CLIP | The image encoder; its `[CLS]`/pooled output is matched against text embeddings with a contrastive loss |
| 3: Flamingo, BLIP-2, LLaVA | A (frozen) ViT produces patch tokens mapped into LLM embeddings |
| 4: Production VLMs | ViT towers with 2D RoPE and native resolution |
| 5: Video models | Patches plus a time axis → spatiotemporal tubelets; factorized space-time attention |
| 7: Diffusion Transformers (DiT) | Image generators are ViTs too: denoising operates on patch tokens of a latent image |
