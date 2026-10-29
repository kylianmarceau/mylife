---
tags:
  - reasoning-in-ai
---

# Contrastive Vision-Language Pretraining: CLIP and Related Models

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Vision-Language Models  
> **Source**: [Lecture2_CLIP_Contrastive_Pretraining.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/VLM%27s/Lecture2_CLIP_Contrastive_Pretraining.pdf), Prof Patrick Marais, slides 1-27 (primary papers: Radford et al. 2021; Jia et al. 2021; Zhai et al. 2023)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Motivation: overcoming the lack of labels|Motivation: overcoming the lack of labels]]
  - [[#The two-tower (dual-encoder) architecture|The two-tower (dual-encoder) architecture]]
  - [[#The alignment goal|The alignment goal]]
  - [[#Batches as self-labelling data|Batches as self-labelling data]]
  - [[#The N×N similarity matrix|The N×N similarity matrix]]
  - [[#Symmetric InfoNCE loss|Symmetric InfoNCE loss]]
  - [[#The role of temperature|The role of temperature]]
  - [[#CLIP in code|CLIP in code]]
  - [[#Why not just predict the caption|Why not just predict the caption]]
  - [[#Training CLIP: summary|Training CLIP: summary]]
  - [[#Zero-shot classification|Zero-shot classification]]
  - [[#Prompt engineering and ensembling|Prompt engineering and ensembling]]
  - [[#How well zero-shot works|How well zero-shot works]]
  - [[#Retrieval in both directions|Retrieval in both directions]]
  - [[#ALIGN: scaling without curation|ALIGN: scaling without curation]]
  - [[#SigLIP: sigmoid loss|SigLIP: sigmoid loss]]
  - [[#CLIP versus SigLIP|CLIP versus SigLIP]]
  - [[#Known failure modes|Known failure modes]]

---

## Core Content

### Motivation: overcoming the lack of labels

#### Definitions

> **CLIP (Contrastive Language-Image Pretraining)**: Training an image encoder and a text encoder on web image-text pairs with a contrastive loss so their embeddings share one space (Radford et al., 2021).

> **Alt-text**: Text attached to web images (captions, descriptions); noisy but plentiful human annotation.

Lecture 1 gave a ViT that turns an image into patch tokens and one vector via `[CLS]`/pooling. Now: how can a photo of a dog and the sentence "a photo of a dog" be encoded so they are **comparable**?

Supervised labels do not scale:

- ImageNet has 1.3M images and 1000 classes, behind about 25,000 annotator-years of curation.
- A fixed label set is very limited: the model can only output its 1000 classes.

The web is full of free supervision. CLIP uses **400M (image, text) pairs** scraped from the web (the **WIT** dataset) instead of curated labels.

| Benefit of natural-language supervision | Example |
|---|---|
| Open vocabulary | Anything describable in English is a potential "class" |
| Richer signal | "A golden retriever puppy asleep on a red sofa" vs class #207 |

The pretrained encoders directly enable a simple text-to-image retrieval pipeline.

### The two-tower (dual-encoder) architecture

#### Definitions

> **Dual encoder (two-tower)**: Separate image and text encoders whose outputs are projected into one shared embedding space, with no interaction between the towers.

> **L2 normalization**: Scaling a vector to unit length, so embeddings lie on a unit hypersphere and cosine similarity equals the dot product.

![CLIP dual encoder](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/02_CLIP_And_Contrastive_Pretraining/dual-encoder.svg)

*Images and captions are encoded separately, projected, and L2-normalized; their cosine similarity measures semantic match.*

| Tower | Encoder | Output |
|---|---|---|
| Image | ViT-L/14 → linear projection → L2-norm | $v \in \mathbb{R}^{512}$ |
| Text | 12-layer Transformer, features at `[EOS]` → linear projection → L2-norm | $t \in \mathbb{R}^{512}$ |

$$
\cos(v, t) = v \cdot t \quad \text{(since } \|v\| = \|t\| = 1\text{)}
$$

- The towers **never see the other input**: no cross-attention between image and text.
- So it is cheap: embeddings can be precomputed and indexed at inference time.
- Later fusion architectures consider image and text tokens together.
- **Text encoder**: 63M parameters, width 512, 8 heads, BPE vocabulary 49,152, max length 76, masked self-attention, features from `[EOS]`.

### The alignment goal

- **Before training**: the encoders' outputs are unrelated; nothing links $v_{\text{dog}}$ to $t_{\text{dog}}$.
- **Training goal**: pull each image towards its own caption and push it away from every other caption in reach.
- **Side effect**: similar concepts cluster (dog near cat, car near plane) because of shared captions and visual features.

"Dog" is never defined. The structure comes entirely from **co-occurrence**: which texts appear with which images.

### Batches as self-labelling data

Sample $N$ pairs $(I_1, T_1), \dots, (I_N, T_N)$. No annotators are needed. Each batch gives, for free:

| Pair type | Count | Assumption |
|---|---|---|
| Positive $(I_i, T_i)$ | $N$ | This caption accompanied this image |
| Negative $(I_i, T_j)$, $i \ne j$ | $N^2 - N$ | Almost certainly unrelated; with 400M pairs, collisions are rare |

This is a **self-labelling classification problem**: for each image, "which of these $N$ captions is yours?"

> [!info] <span style="color: #66b3ff">Why large batches</span>
> CLIP uses $N = 32{,}768$, so each positive is contrasted with $32{,}767$ negatives — about $32{,}768^2 \approx 10^9$ dot products per batch, which is very expensive. More negatives force the model to learn more complex associations between text and image embeddings.

### The N×N similarity matrix

Stack $v_1, \dots, v_N$ into $V$ and $t_1, \dots, t_N$ into $T$. All $N^2$ cosine similarities come from one matrix multiply, $VT^\top$.

![Similarity matrix](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/02_CLIP_And_Contrastive_Pretraining/similarity-matrix.svg)

*Every image is scored against every caption; the diagonal holds the matching pairs, which training pushes up while pushing everything else down.*

- Row $i$ scores image $i$ against every caption.
- Column $j$ scores caption $j$ against every image.
- Objective: **maximize the diagonal, minimize everything else**.

The matrix is **not symmetric**, and rows and columns answer different questions:

| Direction | Question |
|---|---|
| Image → text (row) | Out of all these descriptions, which fits this image best? |
| Text → image (column) | Out of all these images, which best represents this caption? |

Associations are one-to-many (many captions could fit an image and vice versa), so the loss must handle **both** query directions.

| Problem | Logits | Target | Loss |
|---|---|---|---|
| Image → text | Row $i$, over $N$ caption-classes | $i$ | One cross-entropy per row |
| Text → image | Column $j$, over $N$ image-classes | $j$ | One cross-entropy per column |

### Symmetric InfoNCE loss

#### Definitions

> **InfoNCE (information noise-contrastive estimation) loss**: A cross-entropy where the logit for each candidate is (similarity / $\tau$) and the target is the true pair (van den Oord, 2018). It maximizes a lower bound on the mutual information between image and text.

$$
\mathcal{L}_{\text{img}} = -\frac{1}{N}\sum_i \log \frac{\exp\big(\cos(v_i, t_i)/\tau\big)}{\sum_j \exp\big(\cos(v_i, t_j)/\tau\big)}
$$

$$
\mathcal{L}_{\text{txt}} = -\frac{1}{N}\sum_j \log \frac{\exp\big(\cos(v_j, t_j)/\tau\big)}{\sum_i \exp\big(\cos(v_i, t_j)/\tau\big)}
$$

$$
\mathcal{L} = \frac{\mathcal{L}_{\text{img}} + \mathcal{L}_{\text{txt}}}{2}
$$

- The **numerator** pulls matched pairs together.
- The **denominator** pushes all mismatches in the batch apart.
- **Gradient intuition**: the hardest negatives (highest wrong similarity) dominate the denominator's gradient, so the model spends capacity where it is most confused.

### The role of temperature

#### Definitions

> **Temperature $\tau$**: A scalar dividing the similarities before the softmax, controlling how sharp the resulting distribution is.

- Cosine similarities lie in $[-1, 1]$, too flat for a softmax to give robust probabilities.
- Dividing by $\tau < 1$ rescales them: $\tau = 0.07$ gives logits in $[-14, 14]$.
- Smaller $\tau$ → sharper distribution → higher penalties on hard negatives; too small causes training instability.
- In CLIP, $\tau$ is **learned** as a log-parameter (for stability), initialized at $0.07$, and capped so the scale $1/\tau \le 100$.

![Contrastive temperature](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/02_CLIP_And_Contrastive_Pretraining/contrastive-temperature.svg)

*With the same similarities, $\tau = 1$ gives a nearly flat distribution, $\tau = 0.3$ favours the match, and $\tau = 0.07$ puts almost all probability on it.*

### CLIP in code

The core method is about ten lines:

```python
# image_encoder - ResNet or Vision Transformer
# text_encoder  - CBOW or Text Transformer
# I[n, h, w, c] - minibatch of aligned images
# T[n, l]       - minibatch of aligned texts
# W_i[d_i, d_e] - learned projection of image to embedding
# W_t[d_t, d_e] - learned projection of text to embedding
# t             - learned temperature parameter

I_f = image_encoder(I)                       # [n, d_i]
T_f = text_encoder(T)                        # [n, d_t]

I_e = l2_normalize(np.dot(I_f, W_i), axis=1) # joint embedding [n, d_e]
T_e = l2_normalize(np.dot(T_f, W_t), axis=1)

logits = np.dot(I_e, T_e.T) * np.exp(t)      # scaled cosine similarities [n, n]

labels = np.arange(n)
loss_i = cross_entropy_loss(logits, labels, axis=0)
loss_t = cross_entropy_loss(logits, labels, axis=1)
loss = (loss_i + loss_t) / 2
```

Flow: encoders → normalize into the joint space → similarity matrix → diagonal labels → two cross-entropies → average. Everything else in the CLIP paper concerns data, scaling, and evaluation.

### Why not just predict the caption

The alternative is an image-conditioned LM that generates the caption word by word: encode the image, pair it with text in training, and generate autoregressively at inference.

| Objective | Zero-shot ImageNet learning efficiency |
|---|---|
| Transformer LM predicting exact captions | Slowest; poor accuracy |
| Predict a bag-of-words of the caption (order dropped) | $3\times$ more efficient |
| Contrastive matching (CLIP) | A further $4\times$ ($\approx 12\times$ vs the generative LM) |

**Why**: exact wording is mostly not predictable from the image. In "my dog Max at gran's, summer '19", the visual content cannot determine those words, so a generative LM wastes capacity modelling caption noise. Matching only asks: "is this text more compatible with this image than 32,767 others?" — a much less restrictive request, with no concern for grammar or phrasing.

### Training CLIP: summary

| Aspect | Value | Comment |
|---|---|---|
| Data | WIT: 400M web pairs, 500k query-balanced | Scale and diversity replace curation |
| Batch size | 32,768 | Negatives come from the batch; bigger is harder |
| Image towers | 5 ResNets + 3 ViTs (B/32 → L/14@336) | Scaling ViTs cut compute time |
| Text tower | 63M-parameter, 12-layer, width-512 Transformer | Text encoding need not be complex |
| Compute | Up to 18 days × 592 V100s (RN50x64); 12 days × 256 (ViT-L) | Large in 2021; current towers need far more |
| Epochs | 32 over 400M pairs | $\approx 13$B image-text examples seen |

### Zero-shot classification

#### Definitions

> **Zero-shot classification**: Classifying with zero task-specific examples; class names are turned into captions and the image is matched to the most similar one.

![Zero-shot classification](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/02_CLIP_And_Contrastive_Pretraining/zero-shot.svg)

*Class names fill a prompt template, the text encoder builds (and caches) one vector per class, and the image vector is compared with each to pick the argmax.*

1. Choose a label set, e.g. {house, farm, mountain, beach, street}.
2. Fill a template: "a photo of a {label}" → 5 captions.
3. Encode them with the text tower → $t_1, \dots, t_5$ (cache these).
4. Encode the image → $v$.
5. Predict $\arg\max_k \cos(v, t_k)$.

- No training step, no gradient, no labelled examples.
- The **text tower generates the classifier weights**: each $t_k$ is a class embedding. A new caption set is a new classifier.
- Zero-shot errors are usually **near-misses in meaning**, not random failures.

### Prompt engineering and ensembling

The caption (prompt) wording determines classification performance.

- A raw label like "boxer" is ambiguous (dog or athlete?). Training captions are full sentences, so single words are out of distribution.
- "A photo of a {label}." gives $+1.3\%$ ImageNet accuracy from phrasing alone.
- **Domain templates** help more: "a photo of a {label}, a type of pet." (Oxford Pets); "a satellite photo of {label}." (EuroSAT).

#### Definitions

> **Prompt ensembling**: Embedding each class through many templates (e.g. 80: "a sketch of...", "a close-up of...") and averaging the text embeddings.

Averaging happens in embedding space, so each class is still one vector with zero inference-time cost. Prompt engineering plus ensembling give about $+5\%$ on ImageNet, "free" because the model is untouched.

### How well zero-shot works

- Zero-shot CLIP reaches $\approx 76.2\%$ ImageNet top-1, matching the original supervised ResNet-50 with **no ImageNet labels**.
- Across 27 datasets it wins on 16 against a supervised ResNet-50 linear probe: strong on natural categories, weak on specialized or abstract tasks (satellite images, tumours, counting).
- **Robust to distribution shift**: supervised models collapse on sketches, renditions, and adversarial photos; CLIP barely moves. It never overfits ImageNet's photo distribution because its training distribution was the whole web.

> [!warning] <span style="color: #ff939b">Check per domain</span>
> Zero-shot is not universally good. CLIP's EuroSAT zero-shot accuracy was under $60\%$, while a trained linear probe gets about $98\%$.

### Retrieval in both directions

- **Text → image search**: embed the query once and find nearest neighbours among precomputed image embeddings. The image database is indexed offline; a query costs one text-encoder pass plus one k-NN lookup. Billion-image search engines use this pattern with approximate nearest neighbours.
- **Image → text**: score an image against candidate captions — the same operation as zero-shot classification (a label set is a tiny caption gallery).

Zero-shot classification, retrieval, deduplication, and clustering all reduce to **nearest-neighbour search in the joint space**. Benchmarks: Flickr30k and MS-COCO recall@K; zero-shot CLIP rivals fine-tuned systems on Flickr30k.

> [!tip] <span style="color: #5ad4b5">Key point</span>
> CLIP is not a classifier. It is a **similarity oracle** between images and sentences.

### ALIGN: scaling without curation

#### Definitions

> **ALIGN (A Large-scale ImaGe and Noisy-text embedding)**: A CLIP-style dual encoder trained on far more, far noisier web data (Jia et al., 2021).

Building WIT required costly cleanup and filtering. ALIGN made a different bet on data:

| | CLIP | ALIGN |
|---|---|---|
| Method | Dual encoder, contrastive, symmetric loss | Same |
| Data | 400M curated pairs | 1.8 **billion** alt-text pairs (4.5× CLIP), minimally processed |
| Filtering | Query curation | Frequency-based only |
| Towers | ViT / ResNet + Transformer | EfficientNet-L2 (image) + BERT-Large (text) |

ALIGN matches or exceeds CLIP on retrieval despite noisier text. At billion scale, noise matters little; curation is no longer the bottleneck. Open-source **LAION-400M/5B** datasets and **OpenCLIP** reproduced and extended this publicly.

### SigLIP: sigmoid loss

#### Definitions

> **SigLIP**: Contrastive pretraining that replaces the batch softmax with an independent sigmoid (binary "matched or not?") loss on every cell of the similarity matrix (Zhai et al., 2023).

CLIP's softmax compares every candidate to the whole batch (the denominator sums over all captions). So the loss depends on batch size, and very large batches need expensive **all-gather** communication across GPUs.

SigLIP treats every cell $(i, j)$ as its own binary problem, with learned scale $t$ and bias $b$:

$$
\mathcal{L} = -\frac{1}{N}\sum_i \sum_j \log \sigma\Big(z_{ij}\big(t \cdot \cos(v_i, t_j) + b\big)\Big), \qquad z_{ij} = \begin{cases} +1 & i = j \\ -1 & i \ne j \end{cases}
$$

- The bias deals with the massive imbalance: $N^2 - N$ negatives versus $N$ positives, each considered independently.
- $b$ is initialized at about $-10$ to start "pessimistic" and avoid a wall of early false-positive gradient.

Benefits:

- No cross-example normalization → stable across batch sizes; simpler multi-device training (no logits all-gather).
- Strong at moderate batches (saturates around 32k; still good when smaller, so faster training).
- SigLIP towers are the default vision encoder in many current open VLMs.

### CLIP versus SigLIP

| | CLIP (softmax InfoNCE) | SigLIP (sigmoid) |
|---|---|---|
| Unit of loss | One softmax per row and per column | One binary term per matrix element |
| Normalization | Across the whole batch (denominator) | None; each pair independent |
| Batch-size dependence | Strong: negatives = batch − 1 | Weak: good from ~4k, saturates ~32k |
| Distributed cost | All-gather of embeddings/logits | Pairwise chunks streamed device to device |
| Extra parameters | Temperature $t$ | Temperature $t$ + bias $b$ ($b \approx -10$ at init) |
| Class imbalance | Handled implicitly inside the softmax | Explicit; damped by the bias |

Both learn the same geometry — a shared image-text embedding space. Both ask "is this pair matched?" but normalize the answer against different things.

### Known failure modes

| Failure | Example | Cause |
|---|---|---|
| **Bag-of-words behaviour** | "A man in a red shirt next to a blue car" vs "a man in a blue shirt next to a red car" score nearly the same | Contrastive training seldom needs composition or order; nearest-neighbour matching is often enough. ARO/Winoground show VLMs near chance on relation/order tests while excelling at retrieval |
| **Counting and fine spatial relations** | "three dogs" vs "four dogs"; "left of" vs "right of" | Same as above |
| **Dense tasks** | Localization, OCR, multi-step reasoning | The whole image is compressed to 512 numbers; the patch tokens these tasks need are thrown away (addressed in later lectures) |
