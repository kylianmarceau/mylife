---
tags:
  - ai-systems
---

# LLM Scaling Laws

**Subject**: CSC3044S AI Systems
**Source**: `LLM Agents 1_ LLM Scaling Laws.pdf`, Dr Francois Meyer (LLM Agents Topic 1, based on Xiao & Zhu, *Foundations of LLMs*), pages 1-41. Prescribed reading is Section 2.2.4 of Xiao & Zhu, *Foundations of Large Language Models*.
**Generated**: 2026-11-08

---

## Contents

- [[#Core Content|Core Content]]
  - [[#From Language Models To LLM Agents|From Language Models To LLM Agents]]
  - [[#LLM Training Recap And The Scale Of Pretraining|LLM Training Recap And The Scale Of Pretraining]]
  - [[#How To Scale Pretraining|How To Scale Pretraining]]
  - [[#What Scaling Laws Describe|What Scaling Laws Describe]]
  - [[#The Power-Law Form|The Power-Law Form]]
  - [[#Kaplan Scaling Laws|Kaplan Scaling Laws]]
  - [[#Improved Scaling Laws With Irreducible Error|Improved Scaling Laws With Irreducible Error]]
  - [[#Limitations And Uses Of Scaling Laws|Limitations And Uses Of Scaling Laws]]
  - [[#Scale Model Size And Data Together|Scale Model Size And Data Together]]
  - [[#Optimising For Compute|Optimising For Compute]]
  - [[#Applying The Compute Formula|Applying The Compute Formula]]
  - [[#Optimising For Data|Optimising For Data]]
  - [[#Architecture Matters Less Than Scale|Architecture Matters Less Than Scale]]
  - [[#Extrapolating Scaling Laws|Extrapolating Scaling Laws]]
  - [[#Loss Is Not Downstream Capability|Loss Is Not Downstream Capability]]
  - [[#Emergent Capabilities|Emergent Capabilities]]

---

## Core Content

### From Language Models To LLM Agents

#### Definitions

> **LLM Agent**: A system that wraps a large language model in a framework that lets it gather context, take actions (using files and tools), and verify results in a loop, rather than only producing one reply. Examples include Claude Code, OpenAI Codex and OpenClaw, alongside chat products such as ChatGPT, Claude and Gemini.

> **Agentic Loop**: The repeated cycle of gather context, take action and verify results that an agent runs until a task is done.

> **Test-Time Scaling**: Spending more computation during the generation (inference) phase, rather than during training, to improve answers.

The LLM Agents unit traces how systems moved from chatbots producing simple answers (for example, a recipe) to agent systems announced as tackling frontier maths problems a few years later.

The starting point is a plain **GPT-style decoder**: input tokens are embedded, passed through stacked transformer blocks with causal attention, and an unembedding head predicts the next token at every position.

![GPT decoder stack](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/01_LLM_Scaling_Laws/gpt_decoder_stack.svg)
*A decoder-only GPT: each position predicts the next token ("So" → "long", "long" → "and", ...) using only itself and earlier positions.*

An agent such as Claude Code wraps that model in an agentic loop. The user can interrupt, steer or add context at any point.

![Agentic loop](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/01_LLM_Scaling_Laws/agentic_loop.svg)
*The agentic loop: a prompt drives repeated gather–act–verify cycles until the task is done, with the user able to intervene.*

Building an agent like Claude Code from scratch takes four steps. This note covers step 1.

1. **Scale the LLM pretraining phase.**
2. Scale the LLM generation phase (test-time scaling).
3. Enable the LLM to use files and tools.
4. Wrap the LLM in an agentic framework.

### LLM Training Recap And The Scale Of Pretraining

#### Definitions

> **Pretraining**: Training an LLM on a very large corpus of raw text to predict the next token; it produces a pretrained (base) LLM.

> **Instruction Tuning**: Fine-tuning a pretrained LLM on instruction–response data (e.g. label sentiment, summarise, translate) to produce an instruction-tuned LLM.

> **Preference Alignment**: Further training on preference data (preferred vs rejected responses) to produce an aligned LLM.

> **Token**: The unit of text an LLM reads and predicts; dataset sizes are measured in tokens.

LLM training has three stages. Scaling laws concern the first.

![LLM training pipeline](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/01_LLM_Scaling_Laws/llm_training_pipeline.svg)
*The three LLM training stages; pretraining (highlighted) is where scaling laws apply.*

Key facts about pretraining:

- It is the **most computationally expensive** part of developing an LLM.
- LLMs are now typically pretrained on **trillions of tokens**, because scaling pretraining improves performance.
- Pretraining corpora mix many sources, e.g. the Pile groups its data into academic, internet, prose, dialogue and miscellaneous text.

![Pile dataset composition](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/01_LLM_Scaling_Laws/pile_dataset_composition.svg)
*Treemap of a pretraining corpus (the Pile); each area is roughly that source's share of the data, showing how varied pretraining text is.*

Two examples show the scale involved:

| Model | Transformer blocks | Parameters | Training / context | Compute |
|---|---|---|---|---|
| Llama 3.1 | 126 stacked blocks | 405B | 15T+ tokens seen during training | 16,000 NVIDIA H100s in parallel for 80 days, i.e. 30.84M GPU-hours on the 405B model alone |
| Kimi K3 | 93 stacked blocks | 2.8T total, of which 104B are **active** on any single token | 1M-token context window (amount the model can read at once) | — |

### How To Scale Pretraining

Pretraining can be scaled along three axes:

| Axis | How to scale it |
|---|---|
| **Data** | Use larger pretraining datasets |
| **Model size** | Increase the number of parameters |
| **Compute** | Train for more GPU hours |

These factors depend on each other:

- More data requires bigger models and longer training.
- Bigger models need more data to avoid **over-fitting**.

So you cannot scale one in isolation. Scaling laws tell you how to scale them together.

### What Scaling Laws Describe

#### Definitions

> **LLM Scaling Laws**: Relationships between performance (measured as test-set loss) and model size, pretraining data size, and pretraining compute.

> **Test Loss**: The model's loss (typically cross-entropy) on held-out test data; lower is better.

> **Irreducible Error**: The floor on loss that no amount of scaling removes.

As pretraining data grows, error goes through three regions:

1. **Small data region**: error stays near the best-guess error, so improvements are slow.
2. **Power-law region**: performance improves rapidly and steadily. Error falls along a straight line on log-log axes. **Scaling laws apply here.**
3. **Irreducible error region**: improvement slows again as error approaches its floor.

![Scaling regions](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/01_LLM_Scaling_Laws/scaling_regions.svg)
*Generalisation error versus training data size on log-log axes. Scaling laws model only the middle, power-law region.*

### The Power-Law Form

#### Definitions

> **Power Law**: A relationship $L(x) = a x^{b}$ where one quantity varies as a fixed power of another.

Let $x$ be the variable of interest (e.g. number of parameters) and $L(x)$ the model's loss given $x$ (e.g. cross-entropy on test data). Model the relationship as:

$$
L(x) = a x^{b}
$$

- $a$ and $b$ are estimated **empirically** by training many models of different sizes and tracking their loss.
- For LLMs, $a > 0$ and $b < 0$, so loss falls as $x$ grows.

The same idea shows up when you vary data and model size together. Each model size follows its own curve, and small models plateau early because they lack the capacity to use more data.

![Loss vs model and dataset size](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/01_LLM_Scaling_Laws/loss_vs_model_and_dataset_size.svg)
*Loss against tokens for models from 393.2K to 708M parameters. Larger models keep benefiting from more data, while small ones flatten out.*

**Why scaling feels like diminishing returns.** With $b < 0$:

- Loss falls as $x$ (parameters or data) grows.
- Multiplying $x$ by 10 **always** multiplies loss by $10^{b}$, the same proportion whether you go from 1M to 10M parameters or from 10B to 100B:

$$
\frac{L(10x)}{L(x)} = \frac{a(10x)^{b}}{a x^{b}} = 10^{b}
$$

- But each $10\times$ step costs $10\times$ more than the last, and the **absolute** gains shrink.
- So improvements are constant in proportion but come at increasing cost.

Taking logs turns the power law into a straight line, which is why scaling plots use log-log axes:

$$
L(x) = a x^{b} \iff \log L(x) = \log a + b \log x
$$

On log-log axes the slope is $b$ and the intercept is $\log a$.

![Power law on linear vs log-log axes](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/01_LLM_Scaling_Laws/power_law_linear_vs_loglog.svg)
*$L(x) = 100x^{-0.5}$: a steep drop then a long flat tail on linear axes, but a straight line of slope $-0.5$ on log-log axes.*

Example: if $b = -0.05$, then $10^{-0.05} \approx 0.89$, so every $10\times$ scaling cuts loss by about 11%. But 11% of a small loss is worth much less than 11% of a large one.

### Kaplan Scaling Laws

#### Definitions

> **$N$**: Model size, the number of parameters.

> **$D$**: Dataset size, the number of training tokens.

Kaplan et al. (2020) trained Transformer LMs from 768M to 1.5B parameters on datasets of 22M to 23B tokens. They showed that performance improves predictably as a power law of $N$ or $D$:

$$
L(N) = \left(\frac{N}{8.8 \times 10^{13}}\right)^{-0.076}
\qquad
L(D) = \left(\frac{D}{5.4 \times 10^{13}}\right)^{-0.095}
$$

Both laws have the form $a x^{b}$, with a negative exponent: $b = -0.076$ for parameters and $b = -0.095$ for data.

![Kaplan power laws](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/01_LLM_Scaling_Laws/kaplan_power_laws.svg)
*Test loss against parameters (left) and dataset size (right). The trained models lie close to straight fitted lines on log-log axes.*

### Improved Scaling Laws With Irreducible Error

#### Definitions

> **Irreducible Error ($E$)**: The minimum loss attainable, even with an infinitely large model trained on infinite data.

Loss can never reach zero. Language is inherently **stochastic**, so no model can perfectly predict a language-modelling test set. Adding a constant floor gives:

$$
L(x) = a x^{b} + E
$$

A scaling law can combine model-size and data-size terms:

$$
L(N, D) = a N^{b} + c D^{d} + E
$$

**Chinchilla scaling laws** (Hoffmann et al., 2022) were fitted by training over 400 models, from 70M to 16B parameters, on 5B to 500B tokens:

$$
\mathcal{L}(N, D) = \underbrace{\frac{406.4}{N^{0.34}}}_{\text{model scaling}} + \underbrace{\frac{410.7}{D^{0.28}}}_{\text{dataset scaling}} + \underbrace{1.69}_{\text{irreducible error}}
$$

| Term | Meaning |
|---|---|
| $\dfrac{406.4}{N^{0.34}}$ | Loss reducible by adding parameters ($a = 406.4$, $b = -0.34$) |
| $\dfrac{410.7}{D^{0.28}}$ | Loss reducible by adding training tokens ($c = 410.7$, $d = -0.28$) |
| $1.69$ | Irreducible error $E$: the loss floor |

### Limitations And Uses Of Scaling Laws

Scaling "laws" are not universal like laws of mathematics or physics. They are **regularities based on empirical observations**, and many confounding factors affect them:

| Confounding factor | Examples |
|---|---|
| **Hyperparameters** | Learning rate, batch size, optimisers (e.g. SGD, Adam) |
| **Tokenisation** | Tokenisation decisions |
| **Data** | Data quality and repetition; some scaling laws assume no repeated data |

- Alternative scaling laws have been developed to account for these factors.
- Laws inferred from experiments on **small models are not guaranteed to hold for larger models**.

Even so, scaling laws guide decisions during LLM development:

1. Given $X$ available compute, how should we prioritise **data vs model size**?
2. Given $Y$ amount of data, **how big** should the model be?
3. If we scale the model or data, **how much improvement** should we expect?

Even large labs such as OpenAI and Anthropic want to optimise resource usage. Scaling laws reduce reliance on trial and error.

### Scale Model Size And Data Together

#### Definitions

> **$C$**: Compute budget, the number of training FLOPs.

> **FLOP**: A floating-point operation; training compute is counted in total FLOPs.

**Takeaway 1.** Loss follows power laws in model size, dataset size, and compute. For optimal performance, **scale them together**: scale parameters and tokens in equal proportions. If you double model size, double the training tokens too.

Training compute can be estimated from model and dataset size:

$$
C \approx 6 \times N \times D
$$

- About $2ND$ FLOPs come from forward passes.
- About $4ND$ FLOPs come from backward passes.

So, given a fixed compute budget $C$, the question becomes how to choose $N$ and $D$.

### Optimising For Compute

#### Definitions

> **Compute-Optimal**: The choice of $N$ and $D$ that minimises loss for a fixed compute budget $C$.

> **Parameter–Token Ratio**: The ratio $N : D$ of parameters to training tokens.

> **Undertrained Model**: A model trained on too few tokens for its parameter count, i.e. one that lies above the compute-optimal line.

With fixed compute, model size and data size trade off against each other. Because $C \approx 6ND$, increasing one means decreasing the other.

![Fixed compute trade-off](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/01_LLM_Scaling_Laws/fixed_compute_tradeoff.svg)
*Every point on the line costs the same compute. The balanced split between the extremes gives roughly the lowest loss.*

The goal is to find the parameter–token ratio that minimises loss. A fitted law such as the Chinchilla law can be used to derive the performance-optimal ratio under a fixed budget. For the Chinchilla laws it is about **1 : 20**:

$$
D \approx 20N \quad \text{(about 20 training tokens per parameter)}
$$

Consequences:

- On a budget of about $10^{23}$ FLOPs, train a **70B-parameter model on 1.4T tokens**. Check with $C \approx 6ND$: $6 \times 7\times10^{10} \times 1.4\times10^{12} \approx 5.9 \times 10^{23}$ FLOPs, i.e. order $10^{23}$.
- This showed that **most LLMs were undertrained**.
- Chinchilla (70B) outperformed Gopher (280B) under the same compute budget, despite being $4\times$ smaller.

![Compute-optimal frontier](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/01_LLM_Scaling_Laws/compute_optimal_frontier.svg)
*Estimated compute-optimal scaling ($D \approx 20N$) with iso-compute points from $10^{20}$ to $10^{25}$ FLOPs. Chinchilla sits on the line, while GPT-3, Gopher and Megatron-Turing NLG sit well above it (too many parameters for their ~300B tokens).*

| Model | Parameters | Training tokens (approx.) | Position relative to optimal line |
|---|---|---|---|
| Megatron-Turing NLG | 530B | ~270B | Far above (undertrained) |
| Gopher | 280B | ~300B | Above (undertrained) |
| GPT-3 | 175B | ~300B | Above (undertrained) |
| Chinchilla | 70B | 1.4T | On the line |

### Applying The Compute Formula

Assume the optimal ratio is 1 parameter : 20 tokens and that a UCT A100 GPU does about $10^{14}$ FLOPs per second. Questions: (a) what should you train with one A100 for a one-hour tutorial slot, and (b) with one A100 for 24 hours?

(The original problem statement writes the ratio as "20:1"; the intended meaning, used in the solution, is 20 tokens per parameter.)

General derivation:

1. Start from $C = 6ND$.
2. Substitute the optimal ratio $D = 20N$: $C = 6N(20N) = 120N^{2}$.
3. Solve for $N$:

$$
N = \sqrt{\frac{C}{120}}, \qquad D = 20N
$$

| | (a) One A100, one hour | (b) One A100, 24 hours |
|---|---|---|
| Seconds | $3600$ s | $86{,}400$ s |
| Compute $C$ | $3600 \times 10^{14} = 3.6 \times 10^{17}$ FLOPs | $86{,}400 \times 10^{14} \approx 8.6 \times 10^{18}$ FLOPs |
| $C/120$ | $3.0 \times 10^{15}$ | $7.2 \times 10^{16}$ |
| $N = \sqrt{C/120}$ | $\approx 55\text{M}$ parameters | $\approx 270\text{M}$ parameters |
| $D = 20N$ | $\approx 1.1\text{B}$ tokens | $\approx 5.4\text{B}$ tokens |

Note that $24\times$ more compute buys only about $\sqrt{24} \approx 4.9\times$ more parameters (and tokens), because $N \propto \sqrt{C}$.

### Optimising For Data

If **data** is the limiting factor rather than compute, scaling laws show which model size minimises loss for that fixed amount of data.

![Data-constrained model size](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/01_LLM_Scaling_Laws/data_constrained_model_size.svg)
*Loss is U-shaped in model size. Too small lacks capacity, too big cannot use its capacity, and the minimum is the model the data fully supports.*

| Region | What happens |
|---|---|
| Too small ($\tfrac12\times$ params, $2\times$ tokens) | More tokens are shown, but the model doesn't have enough capacity |
| Just right | Enough tokens are shown for the model to fully use its capacity |
| Too big ($2\times$ params, $\tfrac12\times$ tokens) | Fewer tokens are shown, so the model can't fully use its expanded capacity |

**Example: MzansiLM.** The aim was a multilingual LM for all 11 official written languages of South Africa. The main constraint was **data, not compute**.

The first step was building **MzansiText**, a web-scraped dataset for all 11 languages:

| Language | Train tokens |
|---|---|
| Afrikaans | 2,475,913,822 |
| English | 740,994,679 |
| isiNdebele | 818,549 |
| Sepedi (Northern Sotho) | 6,697,358 |
| Sesotho | 97,558,939 |
| siSwati | 1,932,989 |
| Setswana | 10,082,930 |
| Xitsonga | 3,013,408 |
| Tshivenda | 1,852,481 |
| isiXhosa | 152,212,403 |
| isiZulu | 320,224,015 |
| **Total** | **3,811,301,573** |

Steps to size the model:

1. Downsample Afrikaans (which dominates the corpus) to balance training across languages, giving a training set of **2.5B tokens**.
2. Apply the 1 : 20 parameter–token ratio:

$$
N = \frac{D}{20} = \frac{2.5 \times 10^{9}}{20} = 125\text{M parameters}
$$

3. The released model is `uctnlp/mzansilm-125m`, alongside the `uctnlp/mzansi-text` datasets.

Why this size matters:

- Training a **larger** model wastes compute on parameters the data can't support.
- Training a **smaller** model leaves performance on the table.

This calculation is an approximation. It ignores that the model is trained for **multiple epochs**, and repeating data gives diminishing returns, which complicates scaling laws. The laws covered here (Kaplan et al., Chinchilla) assume no data is repeated.

### Architecture Matters Less Than Scale

**Takeaway 2.** Architectural details matter less than sheer scale.

- For Transformers, model **width** (dimensions) and **depth** (number of layers) have small effects compared with how much compute, data and parameters are used.
- This matches Rich Sutton's **"The Bitter Lesson"**: general methods that exploit more computation tend to win over hand-crafted design.

### Extrapolating Scaling Laws

Suppose your company has lots of data but limited compute. Is scaling further worth the cost, and how much loss improvement should you expect?

Fit scaling laws to many cheap small-scale runs, then **extrapolate** the fitted line to a much larger budget:

1. Train a set of small models at different compute budgets and record the compute-optimal $N$ and $D$ for each.
2. Fit a power law (a straight line on log-log axes) of $N$ against $C$, and of $D$ against $C$.
3. Read off the predicted optimal $N$ and $D$ (and expected loss) at the target budget.

![Compute extrapolation](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/01_LLM_Scaling_Laws/compute_extrapolation.svg)
*Fits from runs between about $10^{18}$ and $10^{21}$ FLOPs, extrapolated to about $5.8\times10^{23}$ FLOPs, predict about 63B parameters and 1.4T tokens.*

The limitation from earlier still applies: laws fitted on small models are not guaranteed to hold at large scale.

### Loss Is Not Downstream Capability

#### Definitions

> **Downstream Task**: A specific end-user task or application that uses a pretrained LLM to solve a real-world problem.

**Takeaway 3.** Scaling laws predict **loss**, not **downstream capability**.

- They tell us nothing directly about performance on real-world tasks.
- Pretraining loss correlates with performance on some tasks, but not reliably or predictably.

### Emergent Capabilities

#### Definitions

> **Emergent Capabilities**: Skills or behaviours that do not exist in smaller LMs but appear suddenly and unpredictably when a model reaches a threshold of scale, parameter count and training data.

> **Phase Transition**: A sudden, discontinuous jump in performance on a skill once a scale threshold is crossed.

Example: GPT-3's few-shot arithmetic accuracy stays near zero up to 6.7B parameters, then jumps.

![Arithmetic emergence](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/01_LLM_Scaling_Laws/emergence_arithmetic.svg)
*Two-digit addition and subtraction jump from about 13% to over 50% at 13B parameters and to nearly 100% at 175B. Harder tasks (three- to five-digit operations, multiplication) emerge only at 175B.*

| Task (few-shot) | Behaviour with scale |
|---|---|
| Two-digit addition / subtraction | Near zero until 6.7B, about 55% at 13B, about 100% at 175B |
| Three-digit addition / subtraction | Near zero until 13B, then 80–94% at 175B |
| Four- / five-digit addition / subtraction | Near zero until 13B, then about 25% (four-digit) and 10% (five-digit) at 175B |
| Two-digit multiplication, single-digit three ops | Slow rise to about 20–30% at 175B |

Different tasks obey different laws (Wei et al., 2022):

- Some capabilities only emerge after a given scale of model size, data size or compute.
- Some skills show **phase transitions**: performance sits at the random baseline, then jumps sharply.

![Emergence across tasks](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/01_LLM_Scaling_Laws/emergence_tasks.svg)
*Eight tasks plotted against training FLOPs for LaMDA, GPT-3, Gopher, Chinchilla and PaLM. Each sits near random (dashed) until roughly $10^{22}$–$10^{24}$ FLOPs, then rises sharply.*

| Task | Metric | Emergence pattern |
|---|---|---|
| (A) Modular arithmetic | Accuracy | GPT-3 and LaMDA jump above about $10^{22}$ FLOPs |
| (B) IPA transliterate | BLEU | Rises sharply above about $10^{22}$ FLOPs |
| (C) Word unscramble | Exact match | LaMDA rises near $10^{23}$–$10^{24}$ FLOPs |
| (D) Persian QA | Exact match | Flat at random (~25%) until PaLM at its largest scale (~45%) |
| (E) TruthfulQA | Accuracy | Gopher rises above random only at its largest scale |
| (F) Grounded mappings | Accuracy | GPT-3 below random until a jump at its largest scale |
| (G) Multi-task NLU | Accuracy | Gopher, Chinchilla and GPT-3 jump well above 25% random at large scale |
| (H) Word in context | Accuracy | At 50% random for all models until PaLM's largest scale (~63%) |

Emergence is why smooth pretraining-loss curves do not translate into predictable downstream abilities.
