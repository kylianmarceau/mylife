---
tags:
  - reasoning-in-ai
---

# Transformer Architecture for Large Language Models

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Large Language Models  
> **Source**: [3-TransformersForLLMs - Copy.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/LLM%27s/3-TransformersForLLMs%20-%20Copy.pdf), Dr Jan Buys, slides 1-40 (slides from Tatsu Hashimoto, Stanford CS336; figures from Jurafsky and Martin)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Original versus modern Transformer|Original versus modern Transformer]]
  - [[#Token embedding|Token embedding]]
  - [[#Self-attention|Self-attention]]
  - [[#Self-attention as matrix operations|Self-attention as matrix operations]]
  - [[#Multi-head self-attention|Multi-head self-attention]]
  - [[#KV cache|KV cache]]
  - [[#Grouped-query attention (GQA)|Grouped-query attention (GQA)]]
  - [[#Positional embeddings|Positional embeddings]]
  - [[#Rotary position embeddings (RoPE)|Rotary position embeddings (RoPE)]]
  - [[#Feedforward layers|Feedforward layers]]
  - [[#Gated activations|Gated activations]]
  - [[#Feedforward hyperparameters|Feedforward hyperparameters]]
  - [[#Transformer block and pre-norm|Transformer block and pre-norm]]
  - [[#LayerNorm and RMSNorm|LayerNorm and RMSNorm]]
  - [[#Other architecture options|Other architecture options]]

---

## Core Content

### Original versus modern Transformer

The Transformer is the dominant LLM architecture. There is no single standard version, but several choices that differ from the original have become standard.

| Component | Original (Vaswani et al., 2017) | Modern LLM variant |
|---|---|---|
| Attention | Multi-head attention (MHA) | Grouped-query attention (GQA) with a KV cache |
| Position | Fixed sine/cosine positional embeddings | Rotary position embeddings (RoPE) |
| Feedforward | ReLU FFN per position | SwiGLU FFN, no bias terms |
| Normalization | LayerNorm **after** attention/FFN (post-norm) with residuals | RMSNorm **before** attention/FFN (pre-norm) |

Modern models also make particular hyperparameter choices. The best references are the tech reports of open-weight models: Llama 3, Qwen 2.5, Gemma 2, OLMo 2.

![Original versus modern block](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/original-vs-modern.svg)

*The original block normalizes after each residual add and uses sinusoidal positions and ReLU; the modern block normalizes before causal GQA with RoPE and a SwiGLU FFN.*

### Token embedding

#### Definitions

> **Embedding matrix $E$**: A matrix of dimension $|V| \times d$ storing one $d$-dimensional embedding vector per vocabulary entry.

After tokenization, each token is mapped to an input embedding. The lookup is implemented by representing each token index as a one-hot vector and multiplying by $E$:

$$
X = \text{OneHot}(w_{1:N})\,E, \qquad \text{OneHot}(w_{1:N}) \in \{0, 1\}^{N \times |V|}, \quad X \in \mathbb{R}^{N \times d}
$$

![Token embedding lookup](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/token-embedding.svg)

*Each one-hot row selects exactly one row of $E$, so the lookup is a matrix multiply.*

### Self-attention

#### Definitions

> **Self-attention**: The core Transformer operation, where each position computes a weighted average of value vectors from the sequence, weighted by how well its query matches each key.

> **Query, key, value**: Three projections of each input vector $x_i$: the query $q_i$ asks what to look for, keys $k_j$ are compared with it, and values $v_j$ are what gets combined.

1. Project each input: $q_i = x_i W^Q$, $k_i = x_i W^K$, $v_i = x_i W^V$.
2. Compare query $q_i$ with every key $k_j$ using a scaled dot product.
3. Pass the scores through a softmax.
4. Output a weighted average of the values.

$$
\text{score}(x_i, x_j) = \frac{q_i \cdot k_j}{\sqrt{d_k}}, \qquad \alpha_{ij} = \text{softmax}_j\big(\text{score}(x_i, x_j)\big), \qquad a_i = \sum_j \alpha_{ij}\,v_j
$$

Dividing by $\sqrt{d_k}$ keeps dot products from growing with dimension, which would push the softmax into saturation.

![Self-attention for one output](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/self-attention.svg)

*Query $q_3$ is compared with keys $k_1, k_2, k_3$; the softmax weights combine $v_1, v_2, v_3$ into output $y_3$.*

### Self-attention as matrix operations

Self-attention across all time steps is computed with matrix multiplication. Stack the inputs in $X \in \mathbb{R}^{N \times d}$:

$$
Q = X W^Q, \qquad K = X W^K, \qquad V = X W^V
$$

![Q, K and V projections](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/qkv-projections.svg)

*The same three weight matrices are applied to every input row, giving one query, key, and value per token.*

$$
\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}} + M\right) V
$$

#### Definitions

> **Causal mask $M$**: An $N \times N$ matrix with $0$ on and below the diagonal and $-\infty$ above it, so after the softmax each position attends only to itself and earlier positions.

In a decoder model the attention is masked, because the model must not see future tokens when predicting the next one.

![Masked attention as matrix operations](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/masked-attention.svg)

*$QK^\top$ gives all pairwise scores; the mask sets future entries to $-\infty$; a row-wise softmax and multiplication by $V$ give the outputs $A$.*

### Multi-head self-attention

#### Definitions

> **Attention head**: One attention computation with its own query, key, and value parameters.

> **Multi-head attention (MHA)**: Several attention heads run in parallel to capture multiple relations between elements; their outputs are concatenated and linearly projected.

$$
\text{head}_i = \text{Attention}(XW_i^Q, XW_i^K, XW_i^V), \qquad \text{MHA}(X) = (\text{head}_1 \oplus \dots \oplus \text{head}_h)\,W^O
$$

Set $d_q = d_k = d_v = d/h$. The concatenation then has dimension $d$, and the total parameters and computation stay similar to a single head of size $d$.

![Multi-head attention](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/multi-head-attention.svg)

*Four heads each produce an $N \times d_v$ output; these are concatenated and projected by $W^O$ back to $N \times d$.*

### KV cache

#### Definitions

> **KV cache**: Stored keys and values from previous time steps, reused during generation so they are not recomputed.

During inference, the context grows by one token each step, so attention would have to be recomputed over the whole prefix. Caching keys and values avoids this.

1. A new token arrives and computes its own $q$, $k$, $v$.
2. Its $k$ and $v$ are appended to the layer's cache.
3. The new query attends to all cached keys.
4. The output is the weighted sum of cached values.

![KV cache](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/kv-cache.svg)

*Without a cache, step 4 recomputes keys and values for all four tokens. With a cache, only token 4's query, key, and value are computed; earlier keys and values are read from memory.*

### Grouped-query attention (GQA)

#### Definitions

> **Multi-query attention (MQA)**: Attention with a single key head and a single value head shared by all query heads; queries stay separate per head.

> **Grouped-query attention (GQA)**: Attention with several key/value heads, each shared by a group of query heads.

Using a KV cache requires many memory operations, which limits computational efficiency. Sharing keys and values across heads reduces how many key/value heads must be read from the cache.

![MHA, GQA and MQA](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/mha-gqa-mqa.svg)

*With eight query heads: MHA has eight K/V heads, GQA has four (each shared by two queries), and MQA has one shared by all.*

| Variant | K/V heads | Memory traffic | Expressiveness |
|---|---|---|---|
| MHA | One per query head | Highest | Highest |
| GQA | One per group of queries | Reduced | Controlled by key-query ratio |
| MQA | One | Lowest | Lowest |

- The **key-query ratio** controls expressiveness.
- GQA may cause a small performance drop (and has fewer K/V parameters for a given dimension) but increases inference speed.

### Positional embeddings

Neither attention nor any other Transformer component encodes the position of input vectors. Several positional embeddings have been proposed:

| Type | How it works | Used in |
|---|---|---|
| Fixed sinusoidal | Sine/cosine formula | Original Transformer |
| Absolute | Learn one embedding vector per position | Early LLMs |
| Relative | Add a vector to the attention computation encoding the key-query distance | — |
| **RoPE** | Variant of relative embeddings using rotations | Most current LLMs |

### Rotary position embeddings (RoPE)

#### Definitions

> **Relative position embedding**: An embedding $f(x, i)$ of vector $x$ at position $i$ such that inner products depend only on the relative offset: $\langle f(x, i), f(y, j) \rangle = g(x, y, i - j)$.

RoPE rotates vectors by an angle that depends on their absolute position. Inside attention, queries and keys are rotated; their inner product then depends only on relative position.

This works because inner products are invariant to a shared rotation:

$$
\langle Rx, Ry \rangle = \langle x, y \rangle
$$

Rotating $q$ by $m\theta$ and $k$ by $n\theta$ is the same as rotating by a common angle and then by $(m - n)\theta$, so only the difference matters.

In 2D, with absolute position $m$ and hyperparameter $\theta$:

$$
R_m = \begin{pmatrix} \cos m\theta & -\sin m\theta \\ \sin m\theta & \cos m\theta \end{pmatrix}
$$

For a $d$-dimensional vector, take coordinate pairs and rotate each in 2D with its own frequency:

$$
\theta_i = b^{-2i/d}
$$

where $b$ is a base hyperparameter (commonly $10000$).

![RoPE rotation](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/rope-rotation.svg)

*Each coordinate pair is rotated by $m\theta$ for position $m$; the query-key inner product then depends only on the offset $m - n$.*

- RoPE is applied to **queries and keys, not values**, before attention.
- It is applied at **every layer**, reinforcing positional information throughout the model.

### Feedforward layers

#### Definitions

> **Position-wise feedforward network (FFN)**: A two-layer MLP applied independently at each position, sharing parameters across positions.

- In large LLMs, FFNs **dominate** the compute (FLOPs) and parameter count, more than attention.
- The original FFN uses ReLU.
- Standard practice now drops bias terms: this saves memory lookups (faster) and improves training stability.
- Activations used include ReLU and GELU.

![ReLU, GELU and Swish](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/activation-functions.svg)

*ReLU is exactly zero for negative input; GELU and Swish are smooth and dip slightly below zero before becoming approximately linear.*

### Gated activations

#### Definitions

> **Gated activation (GLU variant)**: An FFN hidden layer in which the activation is multiplied elementwise by a second linear projection (a gate), adding an extra parameter matrix $V$.

> **Swish**: $\text{swish}(x) = x\,\sigma(x)$.

Most LLMs now use gated activations.

| FFN | Formula (no bias) | Used in |
|---|---|---|
| ReLU | $\text{FF}(x) = \max(0, xW_1)\,W_2$ | Original Transformer |
| ReGLU | $\text{FF}(x) = \big(\max(0, xW_1) \otimes xV\big)\,W_2$ | — |
| GeGLU | $\text{FF}(x) = \big(\text{GELU}(xW_1) \otimes xV\big)\,W_2$ | Gemma |
| SwiGLU | $\text{FF}(x) = \big(\text{Swish}(xW_1) \otimes xV\big)\,W_2$ | Llama and other recent models |

### Feedforward hyperparameters

| FFN type | Hidden dimension |
|---|---|
| Standard (2 matrices) | $d_{ff} = 4d$ |
| Gated (3 matrices) | $d_{ff} = \frac{2}{3} \cdot 4d = \frac{8}{3}d$ |

Gated FFNs scale the hidden size down by $2/3$ to keep the parameter count similar. These are heuristics, not absolute rules.

### Transformer block and pre-norm

#### Definitions

> **Transformer block**: Multi-head attention and a feedforward network, each connected with a residual connection and layer normalization.

> **Residual stream**: The path carrying $x$ through the block, to which each sublayer adds its output.

> **Pre-norm**: Applying layer normalization before MHA and the FFN, inside each branch and outside the residual stream.

Most LLMs reorder the original block's operations. Pre-norm gives more stable training for large networks.

![Post-norm versus pre-norm](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/pre-norm-vs-post-norm.svg)

*In post-norm the residual stream itself passes through LayerNorm; in pre-norm the norm sits inside each branch and the residual (amber) bypasses it.*

| Order | Post-norm (original) | Pre-norm (current) |
|---|---|---|
| Attention sublayer | $\text{LN}(x + \text{MHA}(x))$ | $x + \text{MHA}(\text{LN}(x))$ |
| FFN sublayer | $\text{LN}(h + \text{FFN}(h))$ | $h + \text{FFN}(\text{LN}(h))$ |

Pre-norm block equations:

$$
\begin{aligned}
t_1 &= \text{LayerNorm}(x) \\
t_2 &= \text{MultiHeadAttention}(t_1) \\
t_3 &= t_2 + x \\
t_4 &= \text{LayerNorm}(t_3) \\
t_5 &= \text{FFN}(t_4) \\
h &= t_5 + t_3
\end{aligned}
$$

### LayerNorm and RMSNorm

#### Definitions

> **LayerNorm**: Normalizes the mean and variance across the vector's dimensions, then applies a learned scale $\gamma$ and bias $\beta$.

> **RMSNorm**: Normalizes by the root mean square only, without subtracting the mean or adding a bias.

$$
\text{LayerNorm}(x) = \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}}\,\gamma + \beta, \qquad \mu = \frac{1}{d}\sum_{i=1}^{d} x_i, \quad \sigma^2 = \frac{1}{d}\sum_{i=1}^{d}(x_i - \mu)^2
$$

$$
\text{RMSNorm}(x) = \frac{x}{\sqrt{\frac{1}{d}\sum_{i=1}^{d} x_i^2 + \epsilon}}\,\gamma
$$

Most current LLMs use RMSNorm:

- Faster, mainly due to less data movement.
- Observed to give more stable training.
- Same principle as dropping FFN bias terms.

**Additional LayerNorms** further improve stability. It is common to normalize queries and keys before attention (**QK norm**).

### Other architecture options

| Option | Idea | Trade-off |
|---|---|---|
| Sliding window attention | Do not attend to the full context at every layer | Cheaper attention, local context per layer |
| Linear attention / state space models | Sub-quadratic sequence mixing | Used inside hybrid architectures in large models |
| Mixture of Experts (MoE) | Route each token to a few expert FFNs | More expressive and faster at inference (fewer active parameters), but more complex to train |
