---
tags:
  - reasoning-in-ai
---

# Text Generation with Language Models

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Large Language Models  
> **Source**: [5-Generation.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/LLM%27s/5-Generation.pdf), Dr Jan Buys, slides 1-23 (some slides from Antoine Bosselut and Yejin Choi)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Autoregressive generation|Autoregressive generation]]
  - [[#Training versus decoding|Training versus decoding]]
  - [[#Directed and open-ended generation|Directed and open-ended generation]]
  - [[#Greedy decoding|Greedy decoding]]
  - [[#Beam search|Beam search]]
  - [[#Problems with maximization-based decoding|Problems with maximization-based decoding]]
  - [[#Sampling-based decoding|Sampling-based decoding]]
  - [[#Top-k sampling|Top-k sampling]]
  - [[#Top-p (nucleus) sampling|Top-p (nucleus) sampling]]
  - [[#Softmax temperature|Softmax temperature]]

---

## Core Content

### Autoregressive generation

#### Definitions

> **Logits**: The vector of unnormalized scores $S \in \mathbb{R}^{|V|}$ the model computes for every vocabulary token at a time step.

At each time step $t$, an autoregressive LM takes the previous tokens $y_{<t}$ as input and outputs a new token $\hat{y}_t$, which is appended to the input for the next step.

The model $f$ computes logits, which a softmax turns into a distribution over $w \in V$:

$$
S = f(y_{<t}; \theta), \qquad P(y_t = w \mid y_{<t}) = \frac{\exp(S_w)}{\sum_{w' \in V} \exp(S_{w'})}
$$

### Training versus decoding

#### Definitions

> **Teacher forcing**: During training, feeding the observed (gold) next token as input at each step rather than the model's own prediction.

> **Decoding algorithm**: The function $g$ that selects a token from the model's next-token distribution at inference time.

| Phase | Objective / rule |
|---|---|
| Training | Minimize $\mathcal{L}_t = -\log P(y_t^* \mid y_{<t}^*)$, summed over the sequence, with teacher forcing |
| Inference | $\hat{y}_t = g\big(P(y_t \mid y_{<t})\big)$ |

### Directed and open-ended generation

The best decoding algorithm depends partly on how much uncertainty there is in the output.

| Type | Example | Output uncertainty |
|---|---|---|
| **Directed generation** | Machine translation — the content is in the input | Low |
| **Open-ended generation** | Creative writing — the model must invent the content | High |

Open-ended generation produces a word sequence $\mathbf{x}$ given a context $\mathcal{Y}$:

$$
P(\mathbf{x} \mid \mathcal{Y}) = \prod_i P(x_i \mid \mathbf{x}_1^{i-1}, \mathcal{Y})
$$

For example, continuing a news article opening ("An unprecedented number of mostly young whales have become stranded on the West Australian coast since 2008.") into a full story.

### Greedy decoding

#### Definitions

> **Greedy decoding**: At each time step, choose the highest-probability word.

$$
\hat{y}_t = \arg\max_{w \in V} P(w \mid x, y_1 \dots y_{t-1})
$$

Greedy decoding is simple but **not guaranteed to find the globally highest-scoring output**.

![Decoding tree](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/05_Text_Generation/decoding-tree-dark.svg)

*At $t_1$: ok $0.4$, yes $0.5$, end $0.1$. Each branch continues with its own conditional probabilities at $t_2$, then ends.*

![Greedy counterexample](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/05_Text_Generation/greedy-counterexample.svg)

*Greedy takes "yes" ($0.5$) first and finishes at $0.5 \times 0.4 = 0.20$, but "ok ok" scores $0.4 \times 0.7 = 0.28$. The locally best first token leads to a worse full sequence.*

| Sequence | Probability |
|---|---|
| ok ok EOS | $0.4 \times 0.7 = 0.28$ (best) |
| yes yes EOS | $0.5 \times 0.4 = 0.20$ (greedy's choice) |
| yes ok EOS | $0.5 \times 0.3 = 0.15$ |
| ok yes EOS | $0.4 \times 0.2 = 0.08$ |

### Beam search

#### Definitions

> **Beam search**: An approximate search that keeps the $k$ best partial hypotheses (the beam) at each step, ranked by cumulative score.

> **Beam size $k$**: The number of hypotheses retained at each step.

1. **First step**: take the $k$ highest-scoring tokens from the first softmax as initial hypotheses.
2. **Each later step $t$**:
   1. Compute the next-token softmax for each current hypothesis.
   2. This gives $k \cdot |V|$ expanded hypotheses.
   3. Prune back to the $k$ best by **cumulative score** (sum of log-probabilities).
3. Stop when hypotheses end; return the best complete one.

![Beam search](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/05_Text_Generation/beam-search.svg)

*Keep the top-$k$ prefixes, expand each over the vocabulary, score the full prefixes, and keep the top-$k$ overall.*

With beam size 2, the beam might hold "arrived" and "the" at $t_1$, then "the green" and "the witch" at $t_2$, discarding other expansions.

### Problems with maximization-based decoding

- Maximization-based decoding (greedy, beam search) does **not** generate high-quality open-ended text in practice. It tends to produce **repetitive** phrases.
- It may not reflect how language works. Beam search keeps the per-token probability near 1, while human text constantly includes lower-probability tokens.

### Sampling-based decoding

#### Definitions

> **Ancestral sampling**: At each step, sample the next token from the full next-word distribution, $\hat{y}_t \sim P(y_t = w \mid y_{<t})$.

Sampling is random, so any token may be chosen. "He wanted to go to the ___" might yield grocery, store, airport, pub, bathroom, beach, doctor, or hospital.

> [!warning] <span style="color: #ff939b">The long tail</span>
> Sampling makes every vocabulary token an option. Even when most mass is on a few tokens, the tail can be very long. Many tail tokens are irrelevant, and together there is a high chance one gets sampled somewhere in the output.

The solution is **truncated sampling**: only sample from the top of the distribution.

### Top-k sampling

#### Definitions

> **Top-k sampling**: Sample only from the $k$ most probable next tokens (renormalized), ignoring everything else (Fan et al., 2018).

| Choice | Effect |
|---|---|
| Larger $k$ | More diverse / risky outputs |
| Smaller $k$ | More generic / safe outputs |

A fixed $k$ fails in both directions:

| Distribution | Example | Failure |
|---|---|---|
| **Flat** | "She said, 'I never ___'" — thought, knew, had, saw, did, said, ... all similar | Cuts off **too quickly**, excluding reasonable options |
| **Peaked** | "I ate the pizza while it was still ___" — "hot" has $\approx 0.8$ | Cuts off **too slowly**, admitting unreasonable options |

### Top-p (nucleus) sampling

#### Definitions

> **Top-p (nucleus) vocabulary $V^{(p)}$**: The smallest set $V^{(p)} \subset V$ whose cumulative probability reaches $p$.

$$
\sum_{x \in V^{(p)}} P(x \mid x_{1:i-1}) \ge p
$$

Let $p' = \sum_{x \in V^{(p)}} P(x \mid x_{1:i-1})$. Sample from the renormalized distribution:

$$
P'(x \mid x_{1:i-1}) =
\begin{cases}
P(x \mid x_{1:i-1}) / p' & \text{if } x \in V^{(p)} \\
0 & \text{otherwise}
\end{cases}
$$

The number of candidate words varies with the distribution's shape:

- Flat distribution → many words in the nucleus.
- Peaked distribution → few words.

This adapts to both of top-$k$'s failure cases.

### Softmax temperature

#### Definitions

> **Temperature $\tau$**: A hyperparameter that divides the logits before the softmax, changing the distribution's shape.

$$
P_t(y_t = w) = \frac{\exp(S_w / \tau)}{\sum_{w' \in V} \exp(S_{w'} / \tau)}
$$

| Temperature | Distribution | Output |
|---|---|---|
| $\tau > 1$ | More uniform | More diverse (mass spread over vocabulary) |
| $\tau < 1$ | More spiky | Less diverse (mass concentrated on top words); $\tau \to 0$ approaches greedy |

Temperature is **not a decoding algorithm on its own**. It is applied together with a decoding algorithm, such as sampling or top-$p$.

Example with logits all $= 1.2$, the $= 0.9$, your $= 0.1$, that $= -0.5$:

| Token | Logit | $\tau = 0.1$ | $\tau = 0.5$ | $\tau = 1$ | $\tau = 10$ | $\tau = 100$ |
|---|---|---|---|---|---|---|
| all | 1.2 | 0.95 | 0.59 | 0.44 | 0.27 | 0.25 |
| the | 0.9 | 0.05 | 0.32 | 0.33 | 0.26 | 0.25 |
| your | 0.1 | 0.00 | 0.07 | 0.15 | 0.24 | 0.25 |
| that | -0.5 | 0.00 | 0.02 | 0.08 | 0.23 | 0.25 |

![Temperature effect](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/05_Text_Generation/temperature-probabilities.svg)

*The same four logits become nearly greedy at $\tau = 0.1$, normal at $\tau = 1$, and nearly uniform at $\tau = 10$.*
