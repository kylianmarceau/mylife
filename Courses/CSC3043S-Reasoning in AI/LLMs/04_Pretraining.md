---
tags:
  - reasoning-in-ai
---

# Large Language Model Pretraining

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Large Language Models  
> **Source**: [4-Pretraining - Copy.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/LLM%27s/4-Pretraining%20-%20Copy.pdf), Dr Jan Buys, slides 1-34 (slides from Jurafsky and Martin, Tatsunori Hashimoto, others as cited)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Pretraining as self-supervised learning|Pretraining as self-supervised learning]]
  - [[#Pretraining data|Pretraining data]]
  - [[#Data preparation and cleaning|Data preparation and cleaning]]
  - [[#Issues with web-scraped data|Issues with web-scraped data]]
  - [[#Language model evaluation|Language model evaluation]]
  - [[#Perplexity|Perplexity]]
  - [[#LLM training efficiency|LLM training efficiency]]
  - [[#Floating point representations|Floating point representations]]
  - [[#Optimization: SGD and Adam|Optimization: SGD and Adam]]
  - [[#Batching and memory requirements|Batching and memory requirements]]
  - [[#Gradient accumulation|Gradient accumulation]]
  - [[#Multi-GPU training|Multi-GPU training]]

---

## Core Content

### Pretraining as self-supervised learning

#### Definitions

> **Pretraining**: The first stage of LLM training, where a Transformer LM learns from large amounts of text before being fine-tuned for instruction following.

> **Self-supervised learning**: Learning where labels come from the data itself; next-word prediction uses the next word as the label.

> **Language modelling head**: The final layer that maps the last hidden state to a distribution over the next word.

> **Weight tying**: Sharing parameters between the token embedding matrix $E$ and the LM head ("unembedding" layer $E^\top$).

Pretraining is stage 1 of the three training stages (pretraining → instruction tuning → preference alignment).

The LM head computes logits $u = h_N^L E^\top$ from the final hidden state, then $y = \text{softmax}(u)$ over the vocabulary. Training minimizes the cross-entropy (negative log-likelihood) of the actual next token:

$$
\mathcal{L} = -\sum_i \log P(w_i \mid w_{1:i-1})
$$

![Language modelling head](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/04_Pretraining/lm-head.svg)

*The final hidden state $h_N$ is multiplied by the unembedding $E^\top$ to give logits over the vocabulary; a softmax gives next-word probabilities. With weight tying, $E^\top$ reuses the input embedding matrix.*

### Pretraining data

#### Definitions

> **Scaling laws**: Empirical relationships showing that model performance is a function of pretraining data size, model size, and training time.

> **Common Crawl**: Public web crawls of publicly available websites; the usual starting point for open pretraining datasets.

Pretraining data is the basis of LLM development. Large open LLMs are now trained on **trillions of tokens**.

1. Start from Common Crawl dumps.
2. Filter and preprocess to extract text in the target language(s).

Early datasets were mostly English; multilingual efforts are growing. Examples: mC4, CC100, Glot500, CulturaX, Fineweb2, HPLT (HPLT 3.0 has 13T tokens).

**The Pile** mixes several domains:

| Domain | Example sources |
|---|---|
| Academic | PubMed Central, ArXiv, FreeLaw, USPTO, PhilPapers, NIH |
| Web | Pile-CC, OpenWebText2, StackExchange, Wikipedia |
| Books | Bibliotik, PG-19, BookCorpus2 |
| Code / maths | GitHub, DM Mathematics |
| Dialog | Subtitles, IRC, EuroParl, HackerNews, YouTube |

**Typical open-source data mix (OLMo 3):**

| Source | Type | 6T mix share |
|---|---|---|
| Common Crawl | Web pages | $76.1\%$ |
| olmOCR science PDFs | Academic documents | $13.6\%$ |
| StackEdu (rebalanced) | GitHub code | $6.89\%$ |
| FineMath 3+ | Math web pages | $2.56\%$ |
| arXiv | Papers with LaTeX | $0.86\%$ |
| Wikipedia and Wikibooks | Encyclopedic | $0.04\%$ |

### Data preparation and cleaning

Data preparation removes boilerplate, filters for quality, removes unsafe/adult content, and deduplicates.

![Data cleaning pipeline](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/04_Pretraining/data-cleaning.svg)

*Collect and language-filter web data, apply heuristic filters, deduplicate, then apply semantic, topic, and safety filters. About 90% of the data is discarded.*

A representative pipeline (Yi):

1. **Data collection** → raw web data → language filtering.
2. **Heuristic filtering**: text metric filtering, repetitive document removal, rule-based correction, perplexity filtering.
3. **Deduplication**: exact deduplication, MinHash (near-duplicate) deduplication, paragraph deduplication, document quality filtering.
4. **Semantic filtering**: semantic, topic, and safety filtering.

> [!info] <span style="color: #66b3ff">Scale of filtering</span>
> Data cleaning typically discards about $90\%$ of the crawled data.

### Issues with web-scraped data

| Issue | Problem |
|---|---|
| Copyright | Much of the text is copyrighted; legal usage is an open question |
| Data consent | Website owners can indicate they do not want their site crawled |
| Privacy | Pages can contain private IP addresses and phone numbers |
| Skew | Text is disproportionately written by US authors, likely skewing topics and opinions |

### Language model evaluation

#### Definitions

> **Extrinsic evaluation**: Comparing models by fine-tuning each on downstream task(s), running the task, and comparing accuracies.

> **Intrinsic evaluation**: Evaluating the LM directly, typically with perplexity on held-out text.

Extrinsic evaluation is expensive and slow, so LM development first uses **intrinsic** evaluation.

- A good LM assigns higher probability to real or frequent sentences than to ungrammatical or rare ones.
- Train on a training set; evaluate on a test set with **no overlap**; use a metric to score test performance.

**The Shannon game** — how well can we predict the next word?

- When I eat pizza, I wipe off the ___
- Many children are allergic to ___
- I saw a ___

A better LM assigns higher probability to the word that actually occurs.

### Perplexity

#### Definitions

> **Perplexity (PPL)**: The inverse probability of the test set, normalized by the number of words.

The best LM assigns the highest probability to an unseen test set.

$$
\text{PPL}(W) = P(w_1 w_2 \dots w_N)^{-\frac{1}{N}} = \sqrt[N]{\frac{1}{P(w_1 w_2 \dots w_N)}} = \sqrt[N]{\prod_{i=1}^{N} \frac{1}{P(w_i \mid w_1 \dots w_{i-1})}}
$$

Equivalently, using the per-word log-likelihood (base 2):

$$
\ell = \frac{1}{N}\sum_{i=1}^{N} \log_2 p(w_i \mid w_{1:i-1}), \qquad \text{PPL}(W) = 2^{-\ell}
$$

**Minimizing perplexity is the same as maximizing probability.**

Perplexity can be read as a **weighted branching factor**:

| Task | Perplexity |
|---|---|
| Recognizing digits 0-9, all equally likely | $10$ |
| Recognizing one of $30{,}000$ equally likely names | $30{,}000$ |

**Wall Street Journal perplexity over time:**

| Model | Perplexity |
|---|---|
| Uniform distribution | 10,000 |
| Bigram | 600 |
| Trigram | 200 |
| 5-gram + tricks | 140 |
| Early Markov (fixed-window) neural networks | ~140 |
| Early non-Markov (recurrent) neural networks | 100 |

![WSJ perplexity](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/04_Pretraining/wsj-perplexity.svg)

*On a log scale: from 10,000 (uniform) to 600 (bigram), 200 (trigram), about 140 (5-gram and early fixed-window neural nets), and 100 (early recurrent nets).*

Perplexity was first found to correlate strongly with translation quality, and later with essentially every downstream capability.

### LLM training efficiency

Most of the cost of developing an LLM goes into pretraining, so performance must be optimized and hardware used fully.

1. Optimize performance on a single GPU.
2. Scale to multiple GPUs using forms of parallelism.

#### Definitions

> **Tensor**: The basic structure storing data, parameters, gradients, optimizer states, and activations. Its **rank** is its number of dimensions; elements are generally floating-point numbers.

The floating-point representation affects both speed and memory.

### Floating point representations

#### Definitions

> **Floating-point number**: A sign bit, exponent bits (determining the range of representable numbers), and mantissa/significand bits (determining precision, the spacing between representable numbers).

> **Mixed precision**: Using low precision for most tensors and full precision where numerics are sensitive.

> **Quantization**: Converting a trained model to lower precision to increase inference efficiency.

| Format | Bits (sign / exponent / fraction) | Range | Precision | Notes |
|---|---|---|---|---|
| fp32 (single) | 1 / 8 / 23 | Full | High | Default, but more precision than needed |
| fp16 (half) | 1 / 5 / 10 | Limited | Medium | Halves memory but limited dynamic range |
| bf16 (brain float) | 1 / 8 / 7 | Same as fp32 | Lower | Same memory as fp16; less instability than fp16, though some risk remains |

![Floating-point formats](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/04_Pretraining/float-formats.svg)

*fp32 has 8 exponent and 23 fraction bits; fp16 has 5 and 10; bf16 keeps fp32's 8 exponent bits (same range) with only 7 fraction bits.*

**Mixed precision in practice:**

| bf16 | fp32 |
|---|---|
| Parameters, activations, gradients | Optimizer states; numerically sensitive ops (RMSNorm, softmax, loss); master copy of weights |

Even lower precisions exist (8-bit, 4-bit). Trained models are often quantized to these for inference.

### Optimization: SGD and Adam

#### Definitions

> **Mini-batch stochastic gradient descent (SGD)**: Updating parameters using the gradient of the loss on a random mini-batch.

> **Adam**: An optimizer that keeps moving averages of the gradient and squared gradient to adapt the step size per parameter.

> **AdamW**: A variant of Adam that changes (decouples) the weight decay behaviour.

LLMs are trained with some version of mini-batch SGD. Enhancements to vanilla SGD give finer control over the learning rate. Adam generally improves on SGD and is widely used.

Adam update for gradient $g = -\nabla E(w)$ with decay rates $\beta_1, \beta_2$, learning rate $\eta$, and stabilizer $\delta$:

$$
\begin{aligned}
s &\leftarrow \beta_1 s + (1 - \beta_1)\,g && \text{first moment} \\
r &\leftarrow \beta_2 r + (1 - \beta_2)\,g \odot g && \text{second moment} \\
\hat{s} &= \frac{s}{1 - \beta_1^{\,\tau}}, \quad \hat{r} = \frac{r}{1 - \beta_2^{\,\tau}} && \text{bias correction} \\
\Delta w &= -\eta\,\frac{\hat{s}}{\sqrt{\hat{r}} + \delta} && \text{elementwise} \\
w &\leftarrow w + \Delta w
\end{aligned}
$$

Dividing $s$ elementwise by $\sqrt{r}$ adapts the effective step size of each parameter.

### Batching and memory requirements

1. View the tokenized data as **one long sequence** of concatenated documents, separated by an end-of-document token.
2. Split it into subsequences of length $M$, the Transformer's context length.
3. The targets are the inputs **shifted by one position**.
4. Sample mini-batches of size $B$.

For single-GPU training, GPU memory (VRAM) limits $M$ and $B$.

![Batching](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/04_Pretraining/batching.svg)

*Documents are concatenated with `<eod>` separators and cut into length-$M$ chunks; each target sequence is its input shifted by one token.*

**Memory estimate** for $L$ layers, model dimension $D$, and $a$ attention heads:

| Component | Memory |
|---|---|
| Number of parameters | $\approx 12\,L\,D^2$ |
| Parameters (bf16) | 2 bytes / parameter |
| Gradients (bf16) | 2 bytes / parameter |
| Optimizer states (fp32 first and second moments) | 8 bytes / parameter |
| **Total** | **12 bytes / parameter + activation memory** |

Activation memory:

$$
L\,S\,M\,B\left(34 + 5\,\frac{aM}{D}\right)
$$

Here $S$ is the per-token hidden size (the model dimension $D$ in the standard derivation). Activation memory can be reduced by **activation recomputation**: recompute forward activations during the backward pass instead of storing them all.

### Gradient accumulation

#### Definitions

> **Gradient accumulation**: Summing gradients over several mini-batches before a single optimizer step, to simulate a larger batch than fits in memory.

By default, weights update after each mini-batch. Large batches often work better for LLMs.

1. Compute gradients for a mini-batch and add them to a running total.
2. Repeat for $A$ accumulation steps.
3. Take one optimizer step using the **average** accumulated gradient.
4. Reset the accumulator to zero for the next effective batch.

This simulates an update on $B \times A$ samples.

![Gradient accumulation](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/04_Pretraining/gradient-accumulation.svg)

*Four microbatches add their gradients to a running total; one optimizer step then uses the average.*

### Multi-GPU training

Large-scale training needs several kinds of parallelism (details are outside the scope of the course):

- Batch parallelism
- Data parallelism
- Fully sharded data parallelism
- Tensor parallelism
- Pipeline parallelism
