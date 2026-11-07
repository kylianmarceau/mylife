---
tags:
  - reasoning-in-ai
---

# CSC3043S Reasoning in AI: Complete Notes

> [!abstract] <span style="color: #b89aff">About this note</span>
> All 19 CSC3043S lecture notes combined into one: Bayesian Networks (Dr Jan Buys, 5 lectures), Large Language Models (Dr Jan Buys, 7 lectures) and Vision-Language Models (Prof Patrick Marais, 7 lectures). Each lecture keeps its source reference.

## Contents

- [[#Part I: Bayesian Networks|Part I: Bayesian Networks]]
  - [[#1. Introduction to Probabilistic Reasoning|1. Introduction to Probabilistic Reasoning]]
    - [[#Uncertainty and probabilistic models|Uncertainty and probabilistic models]]
    - [[#Bayesian networks and module structure|Bayesian networks and module structure]]
    - [[#Random variables|Random variables]]
    - [[#Probability distributions|Probability distributions]]
    - [[#Joint distributions|Joint distributions]]
    - [[#Events|Events]]
    - [[#Marginal distributions|Marginal distributions]]
    - [[#Conditional probability|Conditional probability]]
    - [[#The normalization trick|The normalization trick]]
    - [[#Product rule and chain rule|Product rule and chain rule]]
    - [[#Independence|Independence]]
    - [[#Conditional independence|Conditional independence]]
  - [[#2. Bayesian Networks: Graphical Models|2. Bayesian Networks: Graphical Models]]
    - [[#Probabilistic inference|Probabilistic inference]]
    - [[#Inference by enumeration|Inference by enumeration]]
    - [[#Complexity of enumeration|Complexity of enumeration]]
    - [[#What a Bayesian network is|What a Bayesian network is]]
    - [[#Graphical model notation|Graphical model notation]]
    - [[#Example networks|Example networks]]
    - [[#Probabilities in Bayesian networks|Probabilities in Bayesian networks]]
    - [[#Why the product defines a valid joint|Why the product defines a valid joint]]
    - [[#Worked network examples|Worked network examples]]
    - [[#Bayesian networks and causality|Bayesian networks and causality]]
    - [[#Size and uses of a Bayesian network|Size and uses of a Bayesian network]]
  - [[#3. Bayesian Networks: Inference|3. Bayesian Networks: Inference]]
    - [[#Inference queries on the alarm network|Inference queries on the alarm network]]
    - [[#Inference by enumeration in a Bayesian network|Inference by enumeration in a Bayesian network]]
    - [[#Why enumeration is intractable|Why enumeration is intractable]]
    - [[#Factors|Factors]]
    - [[#Operation 1: join|Operation 1: join]]
    - [[#Operation 2: eliminate|Operation 2: eliminate]]
    - [[#Enumeration versus variable elimination|Enumeration versus variable elimination]]
    - [[#Handling evidence|Handling evidence]]
    - [[#General variable elimination procedure|General variable elimination procedure]]
    - [[#Alarm network with variable elimination|Alarm network with variable elimination]]
    - [[#Elimination order|Elimination order]]
  - [[#4. Bayesian Networks: Representation and D-Separation|4. Bayesian Networks: Representation and D-Separation]]
    - [[#Conditional independence in a Bayesian network|Conditional independence in a Bayesian network]]
    - [[#Implied independences: a chain example|Implied independences: a chain example]]
    - [[#The three canonical triples|The three canonical triples]]
    - [[#Case 1: causal chain|Case 1: causal chain]]
    - [[#Case 2: common cause|Case 2: common cause]]
    - [[#Case 3: common effect (v-structure)|Case 3: common effect (v-structure)]]
    - [[#Active and inactive paths|Active and inactive paths]]
    - [[#The d-separation algorithm|The d-separation algorithm]]
    - [[#D-separation examples|D-separation examples]]
  - [[#5. Decision Networks and Value of Information|5. Decision Networks and Value of Information]]
    - [[#Rationality and expected utility|Rationality and expected utility]]
    - [[#Utility-based agents and utilities|Utility-based agents and utilities]]
    - [[#Decision networks|Decision networks]]
    - [[#Node types|Node types]]
    - [[#Maximum expected utility|Maximum expected utility]]
    - [[#Action selection procedure|Action selection procedure]]
    - [[#Umbrella example|Umbrella example]]
    - [[#Information links and decision tables|Information links and decision tables]]
    - [[#Machine repair example|Machine repair example]]
    - [[#Value of perfect information|Value of perfect information]]
- [[#Part II: Large Language Models|Part II: Large Language Models]]
  - [[#1. Introduction to (Large) Language Models|1. Introduction to (Large) Language Models]]
    - [[#Course organization|Course organization]]
    - [[#Natural language|Natural language]]
    - [[#Natural language processing|Natural language processing]]
    - [[#Representations in NLP|Representations in NLP]]
    - [[#NLP tasks and why NLP is hard|NLP tasks and why NLP is hard]]
    - [[#Brief history of NLP and LLMs|Brief history of NLP and LLMs]]
    - [[#Language modelling|Language modelling]]
    - [[#Classical and modern views of language models|Classical and modern views of language models]]
    - [[#N-gram language models|N-gram language models]]
    - [[#Neural language model architectures|Neural language model architectures]]
    - [[#Three topologies for LLMs|Three topologies for LLMs]]
    - [[#Using decoder LLMs for tasks|Using decoder LLMs for tasks]]
    - [[#Three stages of LLM training|Three stages of LLM training]]
  - [[#2. Tokenization|2. Tokenization]]
    - [[#What tokenization does|What tokenization does]]
    - [[#Character and byte tokenizers|Character and byte tokenizers]]
    - [[#Word tokenizers|Word tokenizers]]
    - [[#Subword tokenization|Subword tokenization]]
    - [[#Byte-pair encoding (BPE)|Byte-pair encoding (BPE)]]
    - [[#Pre-tokenization and word boundaries|Pre-tokenization and word boundaries]]
    - [[#BPE toy corpus example|BPE toy corpus example]]
    - [[#The BPE segmenter|The BPE segmenter]]
    - [[#Best practices|Best practices]]
  - [[#3. Transformer Architecture for Large Language Models|3. Transformer Architecture for Large Language Models]]
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
  - [[#4. Large Language Model Pretraining|4. Large Language Model Pretraining]]
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
  - [[#5. Text Generation with Language Models|5. Text Generation with Language Models]]
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
  - [[#6. LLM Instruction Following|6. LLM Instruction Following]]
    - [[#Language models as assistants|Language models as assistants]]
    - [[#Alignment|Alignment]]
    - [[#Supervised instruction fine-tuning|Supervised instruction fine-tuning]]
    - [[#Instruction data|Instruction data]]
    - [[#Scaling instruction fine-tuning|Scaling instruction fine-tuning]]
    - [[#Instruction fine-tuning for safety|Instruction fine-tuning for safety]]
    - [[#Limitations of supervised instruction fine-tuning|Limitations of supervised instruction fine-tuning]]
    - [[#Prompting|Prompting]]
    - [[#Zero-shot prompting|Zero-shot prompting]]
    - [[#Prompt engineering|Prompt engineering]]
    - [[#Few-shot prompting and in-context learning|Few-shot prompting and in-context learning]]
  - [[#7. LLM Preference Alignment and Reasoning|7. LLM Preference Alignment and Reasoning]]
    - [[#Why preference alignment|Why preference alignment]]
    - [[#Optimizing for human preferences|Optimizing for human preferences]]
    - [[#RLHF pipeline|RLHF pipeline]]
    - [[#Reward modelling|Reward modelling]]
    - [[#Imitation versus optimization|Imitation versus optimization]]
    - [[#Policy gradient and PPO|Policy gradient and PPO]]
    - [[#KL penalty and the full RLHF system|KL penalty and the full RLHF system]]
    - [[#Direct preference optimization (DPO)|Direct preference optimization (DPO)]]
    - [[#Limitations of RLHF|Limitations of RLHF]]
    - [[#Reasoning with rationales|Reasoning with rationales]]
    - [[#Chain-of-thought prompting|Chain-of-thought prompting]]
    - [[#Reinforcement learning from verifiable rewards (RLVR)|Reinforcement learning from verifiable rewards (RLVR)]]
    - [[#Test-time scaling|Test-time scaling]]
- [[#Part III: Vision-Language Models|Part III: Vision-Language Models]]
  - [[#1. Introduction and Vision Transformers|1. Introduction and Vision Transformers]]
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
  - [[#2. Contrastive Vision-Language Pretraining: CLIP and Related Models|2. Contrastive Vision-Language Pretraining: CLIP and Related Models]]
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
  - [[#3. Bridging Vision and Language: Fusion Architectures|3. Bridging Vision and Language: Fusion Architectures]]
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
  - [[#4. VLMs for Image Understanding in Practice|4. VLMs for Image Understanding in Practice]]
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
  - [[#5. Video Understanding|5. Video Understanding]]
    - [[#From image to video|From image to video]]
    - [[#Which frames to sample|Which frames to sample]]
    - [[#Frame tokens versus tubelet tokens|Frame tokens versus tubelet tokens]]
    - [[#Telling the model when each token is|Telling the model when each token is]]
    - [[#Why video breaks quadratic attention|Why video breaks quadratic attention]]
    - [[#Fix 1: factorized space-time attention|Fix 1: factorized space-time attention]]
    - [[#Fix 2: pooling and resampling|Fix 2: pooling and resampling]]
    - [[#Video foundation models versus video-LLMs|Video foundation models versus video-LLMs]]
    - [[#The context wall|The context wall]]
    - [[#Scaling to long video|Scaling to long video]]
    - [[#The cheapest information is not visual|The cheapest information is not visual]]
    - [[#Taxonomy of video tasks|Taxonomy of video tasks]]
    - [[#Temporal grounding|Temporal grounding]]
    - [[#Is the model using time at all?|Is the model using time at all?]]
    - [[#Common video benchmarks|Common video benchmarks]]
  - [[#6. Generative Foundations: VAEs, GANs, and Diffusion|6. Generative Foundations: VAEs, GANs, and Diffusion]]
    - [[#From understanding to generating|From understanding to generating]]
    - [[#Recap: the autoencoder|Recap: the autoencoder]]
    - [[#Why a plain autoencoder cannot generate|Why a plain autoencoder cannot generate]]
    - [[#Variational autoencoders|Variational autoencoders]]
    - [[#The reparameterization trick|The reparameterization trick]]
    - [[#KL divergence|KL divergence]]
    - [[#The VAE objective|The VAE objective]]
    - [[#VAE strengths and weaknesses|VAE strengths and weaknesses]]
    - [[#GANs: a forger versus a detective|GANs: a forger versus a detective]]
    - [[#The GAN objective|The GAN objective]]
    - [[#GAN strengths and weaknesses|GAN strengths and weaknesses]]
    - [[#Diffusion: the core idea|Diffusion: the core idea]]
    - [[#Why many small steps|Why many small steps]]
    - [[#Training: predict the noise|Training: predict the noise]]
    - [[#The noise schedule and ᾱₜ|The noise schedule and ᾱₜ]]
    - [[#The diffusion loss|The diffusion loss]]
    - [[#Generating an image step by step|Generating an image step by step]]
    - [[#Comparison of image generators|Comparison of image generators]]
  - [[#7. Text-to-Image Generation|7. Text-to-Image Generation]]
    - [[#The cost of diffusion in pixel space|The cost of diffusion in pixel space]]
    - [[#Latent diffusion|Latent diffusion]]
    - [[#The control problem: conditioning on text|The control problem: conditioning on text]]
    - [[#Text conditioning with cross-attention|Text conditioning with cross-attention]]
    - [[#Classifier-free guidance|Classifier-free guidance]]
    - [[#The Stable Diffusion pipeline|The Stable Diffusion pipeline]]
    - [[#Diffusion Transformers (DiT)|Diffusion Transformers (DiT)]]
    - [[#Evaluation: two separate questions|Evaluation: two separate questions]]
    - [[#FID|FID]]
    - [[#CLIPScore|CLIPScore]]

---

# Part I: Bayesian Networks

## 1. Introduction to Probabilistic Reasoning

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Bayesian Networks  
> **Source**: [1-Probabilities.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/Bayesian%20Networks/1-Probabilities.pdf), Dr Jan Buys, slides 1-35 (based in part on Klein and Abbeel, CS188 UC Berkeley)  
> **Generated**: 2026-10-29  

### Uncertainty and probabilistic models

#### Definitions

> **Systematic uncertainty**: Uncertainty from observing only finite datasets; more data allows better predictions.

> **Intrinsic uncertainty**: Uncertainty because only partial information about the world is observable, so not every factor influencing a prediction can be modelled.

> **Probabilistic model**: A model that uses probabilities to describe the relationship between multiple variables that each have some degree of uncertainty.

> **Evidence (observed variables)**: Variables whose values are known, such as sensor readings or symptoms.

> **Unobserved variables**: Variables we must reason about, such as an object's location or which disease is present.

> **Probabilistic reasoning**: Using probabilistic models to manage beliefs and reason about unknown variables given evidence. There may or may not be actual randomness in the world.

Dealing with uncertainty is a central problem in AI. Probability theory quantifies and reasons about uncertainty.

| Framework | Comparison with probability |
|---|---|
| Logic-based frameworks | Probability is more flexible |
| Fuzzy logic and other degree-of-truth methods | Probability is more principled |

A probabilistic model's environment has three parts:

1. **Observed variables** — what we know about the state of the world.
2. **Unobserved variables** — what we need to infer.
3. **The model** — a description of how the known and unknown variables relate to each other.

Models describe how a portion of the world works. They are always simplifications and may omit variables or interactions. "All models are wrong; but some are useful." — George E. P. Box.

Two kinds of reasoning appear throughout the module:

| Reasoning type | Direction | Example |
|---|---|---|
| **Diagnostic reasoning** (explanation) | From effects back to causes | Symptoms → which disease? |
| **Causal reasoning** (prediction) | From causes forward to effects | Rain → will traffic be heavy? |

> [!info] <span style="color: #66b3ff">Why not just deep learning?</span>
> Deep learning models are powerful at predicting one variable from input features, but they cannot reason directly about the relationships between different variables. Probabilistic models make those relationships explicit.

### Bayesian networks and module structure

#### Definitions

> **Bayesian network**: A framework for probabilistic models that represents knowledge and enables reasoning under uncertainty.

The motivating example is web-service fault diagnosis. Possible faults (database failure, network outage, traffic spike) cause intermediate symptoms (query errors, server overload), which affect whether the service is up.

![Web-service fault diagnosis network](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/01_Probabilistic_Reasoning/web-service-faults.svg)

*Faults (database failure, network outage, traffic spike) cause symptoms (query errors, server overload), which determine whether the service is up. Observing that the service is down lets us reason backwards to the most likely fault.*

| Week | Topics |
|---|---|
| Week 1 | Probability; BN graphical models; BN inference; tutorial |
| Week 2 | BN conditional independence; BN approximate inference; DBNs/HMMs; decision networks; tutorial |

The assignment is a closed practical on applying Bayesian networks. Every later topic builds on random variables, distributions, marginals, conditionals, and (conditional) independence.

### Random variables

#### Definitions

> **Random variable**: A variable representing some aspect of the world about which we may be uncertain.

> **Domain**: The set of values a random variable can take.

| Variable | Meaning | Domain |
|---|---|---|
| $R$ | Is it raining? | $\{\text{true}, \text{false}\}$, written $\{+r, -r\}$ |
| $T$ | Is it hot or cold? | $\{\text{hot}, \text{cold}\}$ |
| $D$ | How long will it take to drive to campus? | $[0, \infty)$ |

- Capital letters denote random variables ($R$, $T$).
- Lower-case letters denote specific values or variables ranging over values ($r$, $t$).
- This module works mainly with **discrete (categorical)** variables.

### Probability distributions

#### Definitions

> **Probability distribution**: An association of each value in a variable's domain with a probability. For a discrete variable it is a table of probability values.

> **Probability**: A single number $P(X = x)$ satisfying non-negativity and summing to one over the domain.

Unobserved random variables have distributions.

| $T$ | $P$ |
|---|---|
| hot | 0.5 |
| cold | 0.5 |

| $W$ | $P$ |
|---|---|
| sun | 0.6 |
| rain | 0.1 |
| fog | 0.3 |
| meteor | 0.0 |

A probability must satisfy:

$$
\forall x \;\; P(X = x) \ge 0 \qquad\qquad \sum_x P(X = x) = 1
$$

For example, $P(W = \text{rain}) = 0.1$. When every domain value is unique across variables, the shorthand $P(\text{rain}) = P(W = \text{rain})$ is used.

### Joint distributions

#### Definitions

> **Joint distribution**: A specification of a real number for each possible assignment to a set of random variables $X_1, X_2, \dots, X_n$.

> **Outcome**: A complete assignment to all variables in the joint distribution.

Notation:

$$
P(X_1 = x_1, X_2 = x_2, \dots, X_n = x_n) \quad\text{or}\quad P(x_1, x_2, \dots, x_n)
$$

A joint distribution must satisfy:

$$
P(x_1, x_2, \dots, x_n) \ge 0 \qquad\qquad \sum_{(x_1, x_2, \dots, x_n)} P(x_1, x_2, \dots, x_n) = 1
$$

The running example $P(T, W)$:

| $T$ | $W$ | $P$ |
|---|---|---|
| hot | sun | 0.4 |
| hot | rain | 0.1 |
| cold | sun | 0.2 |
| cold | rain | 0.3 |

Key properties:

- A probabilistic model *is* a joint distribution over a set of random variables.
- The joint says how likely each outcome is.
- A joint over $n$ variables with domain size $d$ has $d^n$ entries.

> [!warning] <span style="color: #ff939b">Exponential size</span>
> Because the table grows as $d^n$, full joint tables quickly become unmanageable. Bayesian networks are the better representation developed in this module.

### Events

#### Definitions

> **Event**: A set of outcomes $E$.

The probability of an event is the sum over all outcomes consistent with it:

$$
P(E) = \sum_{(x_1, \dots, x_n) \in E} P(x_1, \dots, x_n)
$$

Given a joint distribution, the probability of any event can be calculated. Using the $P(T, W)$ table:

| Event | Matching outcomes | Probability |
|---|---|---|
| Hot AND sunny | (hot, sun) | $0.4$ |
| Hot | (hot, sun), (hot, rain) | $0.4 + 0.1 = 0.5$ |
| Hot OR sunny | (hot, sun), (hot, rain), (cold, sun) | $0.4 + 0.1 + 0.2 = 0.7$ |

The events we usually care about are **partial assignments**, such as $P(T = \text{hot})$.

### Marginal distributions

#### Definitions

> **Marginal distribution**: A distribution over a subset of the variables in a joint distribution.

> **Marginalization**: Computing a marginal by summing the probabilities of all assignments to the variables being eliminated ("summing out").

Marginals are sub-tables: collapse rows that agree on the kept variables and add their probabilities.

$$
P(t) = \sum_w P(t, w) \qquad\qquad P(w) = \sum_t P(t, w)
$$

| $T$ | $P$ |
|---|---|
| hot | $0.4 + 0.1 = 0.5$ |
| cold | $0.2 + 0.3 = 0.5$ |

| $W$ | $P$ |
|---|---|
| sun | $0.4 + 0.2 = 0.6$ |
| rain | $0.1 + 0.3 = 0.4$ |

### Conditional probability

#### Definitions

> **Conditional probability**: The probability of $a$ given $b$, defined as $P(a \mid b) = \dfrac{P(a, b)}{P(b)}$.

> **Evidence**: The observed variable(s) being conditioned on.

> **Conditional distribution**: A probability distribution over some variables given fixed values of others.

The intuition is: what does observing $b$ tell us about $a$? Conditioning restricts attention to the region where $b$ holds and rescales it to total probability one.

![Conditioning restricts to the evidence](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/01_Probabilistic_Reasoning/conditional-events.svg)

*Observing $b$ discards everything outside $b$ and treats $b$ as the new universe; $P(a \mid b)$ is the share of $b$'s mass that also lies in $a$.*

Example from the $P(T, W)$ table:

$$
P(W = \text{sun} \mid T = \text{cold}) = \frac{P(\text{sun}, \text{cold})}{P(\text{cold})} = \frac{0.2}{0.2 + 0.3} = 0.4
$$

Conditioning on each value of $T$ gives a family of conditional distributions:

| $W$ | $P(W \mid T = \text{hot})$ | $P(W \mid T = \text{cold})$ |
|---|---|---|
| sun | $0.4/0.5 = 0.8$ | $0.2/0.5 = 0.4$ |
| rain | $0.1/0.5 = 0.2$ | $0.3/0.5 = 0.6$ |

Together, these tables form the **full conditional distribution** $P(W \mid T)$. Each column sums to one; the table as a whole does not.

### The normalization trick

A more efficient way to compute a conditional distribution avoids computing $P(\text{evidence})$ separately.

1. **Select** the joint entries consistent with the evidence, giving $P(X_1, x_2)$ from $P(X_1, X_2)$.
2. **Normalize** the selection:
   1. Compute the sum of all selected entries, $Z = \sum_{x_1} P(x_1, x_2)$.
   2. Divide every entry by $Z$.

The sum $Z$ is exactly the probability of the evidence.

![Normalization trick](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/01_Probabilistic_Reasoning/normalization-trick.svg)

*Select the joint rows matching $T = \text{cold}$ ($0.2$, $0.3$), sum them to get $Z = 0.5 = P(\text{cold})$, then divide each by $Z$ to get $P(W \mid \text{cold}) = (0.4, 0.6)$.*

$$
P(w \mid c) = \frac{P(w, c)}{P(c)} = \frac{P(w, c)}{\sum_{w'} P(w', c)}
$$

Example: compute $P(W \mid T = c)$.

| Step | $W = \text{sun}$ | $W = \text{rain}$ |
|---|---|---|
| Select rows with $T = \text{cold}$ | $0.2$ | $0.3$ |
| $Z = 0.2 + 0.3 = 0.5 = P(c)$ | — | — |
| Divide by $Z$ | $0.4$ | $0.6$ |

### Product rule and chain rule

#### Definitions

> **Product rule**: The joint distribution written as a marginal times a conditional, $P(x, y) = P(y)\,P(x \mid y)$.

> **Chain rule**: Any joint distribution written as an incremental product of conditional distributions.

The product rule is a rearrangement of the definition of conditional probability. Example with weather $W$ and dryness $D$:

| $W$ | $P(W)$ |
|---|---|
| sun | 0.8 |
| rain | 0.2 |

| $D$ | $W$ | $P(D \mid W)$ | $P(D, W) = P(W)P(D \mid W)$ |
|---|---|---|---|
| wet | sun | 0.1 | $0.8 \times 0.1 = 0.08$ |
| dry | sun | 0.9 | $0.8 \times 0.9 = 0.72$ |
| wet | rain | 0.7 | $0.2 \times 0.7 = 0.14$ |
| dry | rain | 0.3 | $0.2 \times 0.3 = 0.06$ |

The chain rule generalizes this to $n$ variables:

$$
P(x_1, x_2, \dots, x_n) = P(x_1)\,P(x_2 \mid x_1)\,P(x_3 \mid x_1, x_2) \cdots = \prod_{i=1}^{n} P(x_i \mid x_1, \dots, x_{i-1})
$$

The chain rule holds for any ordering of variables. However, with many variables the later conditional tables (conditioned on all previous variables) become unmanageably large.

### Independence

#### Definitions

> **Independence**: $X$ and $Y$ are independent if $\forall x, y : P(x, y) = P(x)\,P(y)$. Notation: $X \perp\!\!\!\perp Y$.

The joint over two independent variables factors into a product of two simpler distributions. An equivalent definition:

$$
\forall x, y : P(x \mid y) = P(x)
$$

**Example: $n$ fair independent coin flips.** Each $P(X_i)$ is $H = 0.5$, $T = 0.5$. The joint $P(X_1, \dots, X_n)$ has $2^n$ entries, but independence means it is fully described by $n$ small tables.

**Testing independence** — check whether $P(t, w) = P(t)P(w)$ for *every* assignment. Both tables below have marginals $P(\text{hot}) = P(\text{cold}) = 0.5$, $P(\text{sun}) = 0.6$, $P(\text{rain}) = 0.4$.

| $T$ | $W$ | $P_1(t, w)$ | $P_2(t, w)$ | $P(t)P(w)$ |
|---|---|---|---|---|
| hot | sun | 0.4 | 0.3 | 0.3 |
| hot | rain | 0.1 | 0.2 | 0.2 |
| cold | sun | 0.2 | 0.3 | 0.3 |
| cold | rain | 0.3 | 0.2 | 0.2 |

- $P_1$: $0.4 \ne 0.3$, so $T$ and $W$ are **not** independent.
- $P_2$: every entry matches, so $T$ and $W$ **are** independent.

### Conditional independence

#### Definitions

> **Conditional independence**: $X$ is conditionally independent of $Y$ given $Z$ if and only if $\forall x, y, z : P(x, y \mid z) = P(x \mid z)\,P(y \mid z)$. Notation: $X \perp\!\!\!\perp Y \mid Z$.

Full independence is usually too strong an assumption. Conditional independence expresses independence that holds only once some other variable is known.

The equivalent definition is:

$$
\forall x, y, z : P(x \mid z, y) = P(x \mid z)
$$

**Toothache example.** Consider Boolean variables $P(\text{Toothache}, \text{Cavity}, \text{Detect})$. If you have a cavity, whether a probe detects it does not depend on whether you have toothache:

$$
P(+\text{detect} \mid +\text{toothache}, +\text{cavity}) = P(+\text{detect} \mid +\text{cavity})
$$

The same holds without a cavity:

$$
P(+\text{detect} \mid +\text{toothache}, -\text{cavity}) = P(+\text{detect} \mid -\text{cavity})
$$

So $\text{Detect} \perp\!\!\!\perp \text{Toothache} \mid \text{Cavity}$. These statements are all equivalent:

- $P(\text{Detect} \mid \text{Toothache}, \text{Cavity}) = P(\text{Detect} \mid \text{Cavity})$
- $P(\text{Toothache} \mid \text{Detect}, \text{Cavity}) = P(\text{Toothache} \mid \text{Cavity})$
- $P(\text{Toothache}, \text{Detect} \mid \text{Cavity}) = P(\text{Toothache} \mid \text{Cavity})\,P(\text{Detect} \mid \text{Cavity})$

> [!tip] <span style="color: #5ad4b5">Key point</span>
> Unconditional (absolute) independence is very rare. Conditional independence is our most basic and robust form of knowledge about uncertain environments.

More examples:

| Variables | Conditional independence | Reason |
|---|---|---|
| Traffic, Umbrella, Raining | $\text{Traffic} \perp\!\!\!\perp \text{Umbrella} \mid \text{Raining}$ | Rain causes both; once rain is known, umbrellas tell us nothing more about traffic |
| Fire, Smoke, Alarm | $\text{Alarm} \perp\!\!\!\perp \text{Fire} \mid \text{Smoke}$ | The alarm reacts to smoke; once smoke is known, fire adds nothing |

**Conditional independence and the chain rule.** The chain rule always gives:

$$
P(\text{Traffic}, \text{Rain}, \text{Umbrella}) = P(\text{Rain})\,P(\text{Traffic} \mid \text{Rain})\,P(\text{Umbrella} \mid \text{Rain}, \text{Traffic})
$$

With the assumption $\text{Umbrella} \perp\!\!\!\perp \text{Traffic} \mid \text{Rain}$, the last factor simplifies:

$$
P(\text{Traffic}, \text{Rain}, \text{Umbrella}) = P(\text{Rain})\,P(\text{Traffic} \mid \text{Rain})\,P(\text{Umbrella} \mid \text{Rain})
$$

Each factor now conditions on fewer variables, so the tables are smaller. Bayesian networks are a way of expressing exactly these conditional independence assumptions.

## 2. Bayesian Networks: Graphical Models

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Bayesian Networks  
> **Source**: [2-BayesianNetworks-GraphicalModels.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/Bayesian%20Networks/2-BayesianNetworks-GraphicalModels.pdf), Dr Jan Buys, slides 1-23 (based in part on Klein and Abbeel, CS188 UC Berkeley)  
> **Generated**: 2026-10-29  

### Probabilistic inference

#### Definitions

> **Probabilistic inference**: Computing a desired probability from other known probabilities, most commonly a conditional probability computed from joint or other conditional probabilities.

> **Belief**: A conditional probability representing what the agent believes given the evidence it conditions on.

> **Query variable**: The variable $Q$ whose distribution we want.

> **Hidden variables**: Variables $H_1, \dots, H_r$ that are neither query nor evidence.

Beliefs change as new evidence arrives:

| Evidence | Belief |
|---|---|
| No reported accidents | $P(\text{on time} \mid \text{no accidents}) = 0.9$ |
| + it is 5 a.m. | $P(\text{on time} \mid \text{no accidents}, \text{5 a.m.}) = 0.95$ |
| + it is raining | $P(\text{on time} \mid \text{no accidents}, \text{5 a.m.}, \text{raining}) = 0.80$ |

The general inference setup has three kinds of variables:

- **Evidence variables**: $E_1, \dots, E_k = e_1, \dots, e_k$.
- **Query variable**: $Q$.
- **Hidden variables**: $H_1, \dots, H_r$.

The goal is to compute $P(Q \mid e_1, \dots, e_k)$.

### Inference by enumeration

#### Definitions

> **Inference by enumeration**: Computing a query by selecting joint entries consistent with evidence, summing out hidden variables, and normalizing.

1. **Select** the entries consistent with the evidence: $P(Q, H_1, \dots, H_r, e_1, \dots, e_k)$.
2. **Marginalize** the hidden variables:

$$
P(Q, e_1, \dots, e_k) = \sum_{h_1, \dots, h_r} P(Q, h_1, \dots, h_r, e_1, \dots, e_k)
$$

3. **Normalize**:

$$
Z = \sum_q P(q, e_1, \dots, e_k) \qquad P(Q \mid e_1, \dots, e_k) = \frac{1}{Z}\,P(Q, e_1, \dots, e_k)
$$

**Example** — joint over season $S$, temperature $T$, weather $W$:

| $S$ | $T$ | $W$ | $P$ |
|---|---|---|---|
| summer | hot | sun | 0.30 |
| summer | hot | rain | 0.05 |
| summer | cold | sun | 0.10 |
| summer | cold | rain | 0.05 |
| winter | hot | sun | 0.10 |
| winter | hot | rain | 0.05 |
| winter | cold | sun | 0.15 |
| winter | cold | rain | 0.20 |

| Query | Computation | Result |
|---|---|---|
| $P(W)$ | $P(W) = \sum_{s,t} P(s, t, W)$ | sun $0.65$, rain $0.35$ |
| $P(W \mid \text{winter})$ | $P(W, \text{winter}) = \sum_t P(\text{winter}, t, W)$, then $Z = \sum_w P(\text{winter}, w) = 0.5$ | sun $0.25/0.5 = 0.5$, rain $0.5$ |
| $P(W \mid \text{winter}, \text{hot})$ | $Z = \sum_w P(\text{winter}, \text{hot}, w) = 0.15$, then $\frac{1}{Z}P(\text{winter}, \text{hot}, W)$ | sun $2/3$, rain $1/3$ |

### Complexity of enumeration

For a joint over $n$ variables with domain size $d$:

| Resource | Cost |
|---|---|
| Worst-case time | $O(d^n)$ |
| Space to store the joint | $O(d^n)$ |

This is intractable for many variables. However, not all variables interact directly, so we make **(conditional) independence assumptions** to shrink the model.

### What a Bayesian network is

#### Definitions

> **Bayesian network (BN)**: A framework for describing complex joint distributions using simple, local distributions (conditional probability distributions). Also called a **directed probabilistic graphical model**.

- BNs describe how variables interact **locally**.
- Local interactions chain together to produce global, indirect interactions.

A real example is a car-insurance cost network, with variables such as age, socio-economic status, risk aversion, driving skill, vehicle properties, accidents, and the resulting costs.

![Car insurance Bayesian network](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/02_Bayesian_Networks_And_Graphical_Models/insurance-network.svg)

*The car-insurance network has 27 variables and 52 arcs: observable driver and car attributes (blue) feed hidden factors (violet) that determine the costs (amber). Each node only needs a CPT over its few parents, not over all 26 other variables.*

### Graphical model notation

#### Definitions

> **Node**: A random variable. It can be assigned (observed) or unassigned (unobserved); observed nodes are shaded.

> **Arc**: A directed edge representing an interaction between variables. Intuitively it indicates direct influence; formally it encodes (the lack of) conditional independence.

- Arcs are directed. It helps to imagine they indicate direct causation, but in general they do not.
- Missing arcs are what carry information: they encode independence assumptions.

![Graphical model notation](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/02_Bayesian_Networks_And_Graphical_Models/cavity-network.svg)

*Weather has no arcs, so it is independent of the rest. Cavity is a common parent of Toothache and Detect, so the two symptoms are independent once Cavity is known.*

### Example networks

![Coin flips and two traffic models](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/02_Bayesian_Networks_And_Graphical_Models/simple-networks.svg)

*Coin flips have no arcs (absolute independence). For traffic, model 1 assumes rain and traffic are independent; model 2 adds the arc $R \rightarrow T$.*

**$N$ independent coin flips.** Nodes $X_1, \dots, X_n$ with no arcs, so there is no interaction: absolute independence.

**Traffic with two variables** ($R$: it rains, $T$: there is traffic):

| Model | Graph | Assumption |
|---|---|---|
| Model 1: independence | $R$ and $T$, no arc | Rain and traffic are independent |
| Model 2: rain causes traffic | $R \rightarrow T$ | Traffic depends on rain |

**Extended traffic** — $T$: traffic, $R$: rain, $L$: low pressure, $D$: roof drips, $S$: sports match, $C$: cavity.

![Extended traffic network](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/02_Bayesian_Networks_And_Graphical_Models/traffic-model.svg)

*Low pressure causes rain; rain causes roof drips and traffic; a sports match also causes traffic. Cavity is unrelated to everything else, so it has no arcs.*

**Alarm network** — $B$: burglary, $E$: earthquake, $A$: alarm goes off, $J$: John calls, $M$: Mary calls.

![Alarm network](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/02_Bayesian_Networks_And_Graphical_Models/alarm-network.svg)

*Burglary and earthquake can each set off the alarm; the alarm prompts John and Mary to call. Each node stores one CPT over its parents.*

### Probabilities in Bayesian networks

#### Definitions

> **Directed acyclic graph (DAG)**: A directed graph with no directed cycles. In a BN each node represents a random variable $X$.

> **Parents**: The nodes $A_1, \dots, A_n$ with incoming edges to $X$.

> **Conditional probability table (CPT)**: The local distribution $P(X \mid A_1, \dots, A_n)$: one distribution $P(X \mid a_1, \dots, a_n)$ for each combination of parent values.

A Bayesian network consists of:

1. A DAG, with one node per random variable.
2. A local conditional distribution for each node given its parents, stored as a CPT.

A CPT can be thought of as describing a noisy "causal" process from parents to child.

![A node and its CPT](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/02_Bayesian_Networks_And_Graphical_Models/cpt-node.svg)

*Node $X$ with parents $A_1, \dots, A_n$ stores one distribution $P(X \mid a_1, \dots, a_n)$ for every combination of parent values.*

BNs **implicitly** encode the joint as the product of local conditionals. To get the probability of a full assignment, multiply the relevant conditional probabilities:

$$
P(x_1, x_2, \dots, x_n) = \prod_{i=1}^{n} P(x_i \mid \text{parents}(X_i))
$$

Example on the Cavity network ($\text{Cavity} \rightarrow \text{Toothache}$, $\text{Cavity} \rightarrow \text{Detect}$):

$$
P(+\text{cavity}, +\text{detect}, -\text{toothache}) = P(+\text{cavity})\,P(-\text{toothache} \mid +\text{cavity})\,P(+\text{detect} \mid +\text{cavity})
$$

### Why the product defines a valid joint

1. The chain rule holds for **all** distributions:

$$
P(x_1, \dots, x_n) = \prod_{i=1}^{n} P(x_i \mid x_1, \dots, x_{i-1})
$$

2. Order the nodes **topologically** (parents before children) and assume the BN's conditional independences — each variable depends only on its parents among its predecessors:

$$
P(x_i \mid x_1, \dots, x_{i-1}) = P(x_i \mid \text{parents}(X_i))
$$

3. Substituting gives the BN product:

$$
P(x_1, \dots, x_n) = \prod_{i=1}^{n} P(x_i \mid \text{parents}(X_i))
$$

> [!warning] <span style="color: #ff939b">Topology restricts what a BN can represent</span>
> Not every BN can represent every joint distribution. The topology enforces certain conditional independences, so a BN can only represent distributions consistent with them.

### Worked network examples

**Coin flips** — no arcs, each $P(X_i)$ is $h = 0.5$, $t = 0.5$:

$$
P(h, h, t, h) = 0.5 \cdot 0.5 \cdot 0.5 \cdot 0.5 = 0.0625
$$

**Alarm network CPTs:**

| $B$ | $P(B)$ |
|---|---|
| $+b$ | 0.001 |
| $-b$ | 0.999 |

| $E$ | $P(E)$ |
|---|---|
| $+e$ | 0.002 |
| $-e$ | 0.998 |

| $B$ | $E$ | $P(+a \mid B, E)$ | $P(-a \mid B, E)$ |
|---|---|---|---|
| $+b$ | $+e$ | 0.95 | 0.05 |
| $+b$ | $-e$ | 0.94 | 0.06 |
| $-b$ | $+e$ | 0.29 | 0.71 |
| $-b$ | $-e$ | 0.001 | 0.999 |

| $A$ | $P(+j \mid A)$ | $P(-j \mid A)$ |
|---|---|---|
| $+a$ | 0.9 | 0.1 |
| $-a$ | 0.05 | 0.95 |

| $A$ | $P(+m \mid A)$ | $P(-m \mid A)$ |
|---|---|---|
| $+a$ | 0.7 | 0.3 |
| $-a$ | 0.01 | 0.99 |

For example, the probability of a burglary with no earthquake, the alarm going off, and both calling:

$$
P(+b, -e, +a, +j, +m) = P(+b)\,P(-e)\,P(+a \mid +b, -e)\,P(+j \mid +a)\,P(+m \mid +a) = 0.001 \times 0.998 \times 0.94 \times 0.9 \times 0.7
$$

**Traffic, $R \rightarrow T$:**

| $R$ | $P(R)$ |
|---|---|
| $+r$ | $1/4$ |
| $-r$ | $3/4$ |

| $R$ | $P(+t \mid R)$ | $P(-t \mid R)$ |
|---|---|---|
| $+r$ | $3/4$ | $1/4$ |
| $-r$ | $1/2$ | $1/2$ |

Multiplying gives the joint, e.g. $P(+r, -t) = \frac{1}{4} \cdot \frac{1}{4} = \frac{1}{16}$:

| $R$ | $T$ | $P(R, T)$ |
|---|---|---|
| $+r$ | $+t$ | $3/16$ |
| $+r$ | $-t$ | $1/16$ |
| $-r$ | $+t$ | $6/16$ |
| $-r$ | $-t$ | $6/16$ |

**Different topology, same joint ($T \rightarrow R$):**

| $T$ | $P(T)$ |
|---|---|
| $+t$ | $9/16$ |
| $-t$ | $7/16$ |

| $T$ | $P(+r \mid T)$ | $P(-r \mid T)$ |
|---|---|---|
| $+t$ | $1/3$ | $2/3$ |
| $-t$ | $1/7$ | $6/7$ |

Multiplying these out gives exactly the same four joint entries.

![Two topologies, same joint](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/02_Bayesian_Networks_And_Graphical_Models/same-joint-topologies.svg)

*$R \rightarrow T$ and $T \rightarrow R$ use different CPTs but produce the identical joint $P(R, T)$: arc direction is not causality.* Two networks with different arc directions can represent the same distribution.

### Bayesian networks and causality

- Arc direction does **not** necessarily imply causality.
- When BNs reflect the true causal patterns they are often simpler, easier to reason with, and easier to elicit from experts.
- In domains without causality, the arrows reflect correlation.
- The topology really encodes **conditional independence**, which may happen to correspond to causal structure.

### Size and uses of a Bayesian network

| Representation | Size for $N$ Boolean variables |
|---|---|
| Full joint distribution | $2^N$ |
| BN with up to $k$ parents per node | $O(N \cdot 2^{k+1})$ |

Each node's CPT has $2^k$ parent combinations, each with 2 values of the node itself, giving $2^{k+1}$ entries per node.

Advantages over the full joint:

- Substantial space saving.
- Local CPTs are easier to elicit.
- Inference is also faster.

A BN is an efficient encoding of a probabilistic model of a domain. Three questions organize the rest of the module:

| Task | Question |
|---|---|
| **Inference** | Given a fixed BN, what is $P(X \mid e)$? |
| **Representation** | Given a BN graph, what kinds of distributions can it encode? |
| **Modelling** | What BN is most appropriate for a given domain? |

When modelling a domain, understand which assumptions the BN design is making.

## 3. Bayesian Networks: Inference

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Bayesian Networks  
> **Source**: [3-BayesianNets-Inference.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/Bayesian%20Networks/3-BayesianNets-Inference.pdf), Dr Jan Buys, slides 1-20 (based on Klein and Abbeel, CS188 UC Berkeley)  
> **Generated**: 2026-10-29  

### Inference queries on the alarm network

The alarm network has CPTs $P(B)$, $P(E)$, $P(A \mid B, E)$, $P(J \mid A)$, and $P(M \mid A)$.

![Alarm network query](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/03_Bayesian_Network_Inference/alarm-query.svg)

*For $P(B \mid +j, +m)$, $B$ is the query, $J$ and $M$ are observed evidence (shaded), and $E$ and $A$ are hidden variables to sum out.*

Typical queries:

- $P(M)$ — a marginal with no evidence.
- $P(B \mid E)$ — a causal-direction query between two root causes.
- $P(B \mid M)$ — a diagnostic query from an effect back to a cause.

### Inference by enumeration in a Bayesian network

The three enumeration steps from the previous lecture apply directly.

1. **Select** entries consistent with the evidence.
2. **Marginalize** the hidden variables.
3. **Normalize** by $\frac{1}{Z}$.

In a BN, the joint is not stored; each joint entry is built from the CPTs. For $P(B \mid +j, +m)$, with hidden variables $E$ and $A$:

$$
\begin{aligned}
P(B \mid +j, +m) &\propto_B P(B, +j, +m) \\
&= \sum_{e, a} P(B, e, a, +j, +m) \\
&= \sum_{e, a} P(B)\,P(e)\,P(a \mid B, e)\,P(+j \mid a)\,P(+m \mid a)
\end{aligned}
$$

Expanding the sum gives four full products, one for each $(e, a)$ combination:

$$
\begin{aligned}
&P(B)P(+e)P(+a \mid B, +e)P(+j \mid +a)P(+m \mid +a) + P(B)P(+e)P(-a \mid B, +e)P(+j \mid -a)P(+m \mid -a) \\
+\;&P(B)P(-e)P(+a \mid B, -e)P(+j \mid +a)P(+m \mid +a) + P(B)P(-e)P(-a \mid B, -e)P(+j \mid -a)P(+m \mid -a)
\end{aligned}
$$

The result is then multiplied by $\frac{1}{Z}$ to normalize over $B$.

### Why enumeration is intractable

- In a network with many variables (for example the car-insurance network, querying $P(\text{Antilock} \mid \text{observed variables})$), enumeration is not tractable.
- The whole joint is computed ("joined up") **before** the hidden variables are summed out.
- It is more efficient to **interleave** joining and marginalizing.

### Factors

#### Definitions

> **Factor**: Any quantity (table) based on a probability distribution. The initial factors are the local CPTs.

Inference by enumeration can be reframed as operations on factors. The running example is a chain $R \rightarrow T \rightarrow L$ (rain, traffic, late).

*The chain is $R \rightarrow T \rightarrow L$: rain influences traffic, which influences whether you are late ($L$).*

| $R$ | $P(R)$ |
|---|---|
| $+r$ | 0.1 |
| $-r$ | 0.9 |

| $R$ | $T$ | $P(T \mid R)$ |
|---|---|---|
| $+r$ | $+t$ | 0.8 |
| $+r$ | $-t$ | 0.2 |
| $-r$ | $+t$ | 0.1 |
| $-r$ | $-t$ | 0.9 |

| $T$ | $L$ | $P(L \mid T)$ |
|---|---|---|
| $+t$ | $+l$ | 0.3 |
| $+t$ | $-l$ | 0.7 |
| $-t$ | $+l$ | 0.1 |
| $-t$ | $-l$ | 0.9 |

### Operation 1: join

#### Definitions

> **Join**: Combine all factors that mention a joining variable into one new factor over the union of their variables. Each entry is a pointwise product. It works like a database join.

1. Get all factors over the joining variable.
2. Build a new factor over the union of the variables involved.
3. Fill each entry with the product of the matching entries.

**Join on $R$**: $P(R) \times P(T \mid R) \rightarrow P(R, T)$, e.g. $P(+r, +t) = 0.1 \times 0.8 = 0.08$.

| $R$ | $T$ | $P(R, T)$ |
|---|---|---|
| $+r$ | $+t$ | 0.08 |
| $+r$ | $-t$ | 0.02 |
| $-r$ | $+t$ | 0.09 |
| $-r$ | $-t$ | 0.81 |

**Then join on $T$**: $P(R, T) \times P(L \mid T) \rightarrow P(R, T, L)$.

| $R$ | $T$ | $L$ | $P(R, T, L)$ |
|---|---|---|---|
| $+r$ | $+t$ | $+l$ | 0.024 |
| $+r$ | $+t$ | $-l$ | 0.056 |
| $+r$ | $-t$ | $+l$ | 0.002 |
| $+r$ | $-t$ | $-l$ | 0.018 |
| $-r$ | $+t$ | $+l$ | 0.027 |
| $-r$ | $+t$ | $-l$ | 0.063 |
| $-r$ | $-t$ | $+l$ | 0.081 |
| $-r$ | $-t$ | $-l$ | 0.729 |

### Operation 2: eliminate

#### Definitions

> **Eliminate**: Take a factor and sum out (marginalize) a variable. This shrinks the factor and is a projection operation.

Summing $R$ out of $P(R, T)$:

| $T$ | $P(T)$ |
|---|---|
| $+t$ | $0.08 + 0.09 = 0.17$ |
| $-t$ | $0.02 + 0.81 = 0.83$ |

**Multiple elimination** from $P(R, T, L)$: sum out $R$ to get $P(T, L)$, then sum out $T$ to get $P(L)$.

| $T$ | $L$ | $P(T, L)$ |
|---|---|---|
| $+t$ | $+l$ | 0.051 |
| $+t$ | $-l$ | 0.119 |
| $-t$ | $+l$ | 0.083 |
| $-t$ | $-l$ | 0.747 |

| $L$ | $P(L)$ |
|---|---|
| $+l$ | $0.051 + 0.083 = 0.134$ |
| $-l$ | $0.119 + 0.747 = 0.866$ |

### Enumeration versus variable elimination

#### Definitions

> **Variable elimination (VE)**: An inference algorithm that interleaves join and eliminate operations, so that large joint factors are never built unnecessarily.

| Method | Order of operations | Largest factor in the $R \rightarrow T \rightarrow L$ example |
|---|---|---|
| Inference by enumeration | All joins first, then all eliminations | $P(R, T, L)$, 8 entries |
| Variable elimination | Join on a variable, eliminate it, repeat | $P(R, T)$ or $P(T, L)$, 4 entries |

![Enumeration versus variable elimination](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/03_Bayesian_Network_Inference/enumeration-vs-ve.svg)

*Enumeration joins everything into the 8-entry $P(R, T, L)$ before summing. Variable elimination joins and sums out one variable at a time, so no factor exceeds 4 entries.*

VE on the chain:

1. Join $R$: $P(R) \times P(T \mid R) \rightarrow P(R, T)$.
2. Sum out $R$: $P(R, T) \rightarrow P(T)$ $= (0.17, 0.83)$.
3. Join $T$: $P(T) \times P(L \mid T) \rightarrow P(T, L)$ $= (0.051, 0.119, 0.083, 0.747)$.
4. Sum out $T$: $P(T, L) \rightarrow P(L)$ $= (0.134, 0.866)$.

### Handling evidence

If there is evidence, first **select** it in the initial factors, then eliminate every hidden variable, then normalize.

**Example: $P(L \mid +r)$.** With no evidence the initial factors are $P(R)$, $P(T \mid R)$, $P(L \mid T)$. With $+r$ observed they become:

| Factor | Entries kept |
|---|---|
| $P(+r)$ | $+r$: 0.1 |
| $P(T \mid +r)$ | $+t$: 0.8, $-t$: 0.2 |
| $P(L \mid T)$ | unchanged (no $R$ in it) |

1. Eliminate the only hidden variable, $T$: join everything and sum out $T$.
2. The result is a selected joint of query and evidence, $P(+r, L)$: $+l$: $0.026$, $-l$: $0.074$.
3. Normalize: $Z = 0.1$, giving $P(+l \mid +r) = 0.26$ and $P(-l \mid +r) = 0.74$.

### General variable elimination procedure

For a query $P(Q \mid E_1 = e_1, \dots, E_k = e_k)$:

1. Start with initial factors: the local CPTs instantiated with the evidence.
2. While there are still hidden variables (not $Q$ or evidence):
   1. Pick a hidden variable $H$.
   2. Join all factors mentioning $H$.
   3. Eliminate (sum out) $H$.
3. Join all remaining factors and normalize.

```text
VariableElimination(Q, evidence e, BN):
    factors ← CPTs of BN, each restricted to e
    for each hidden variable H (in chosen order):
        F_H ← all factors mentioning H
        f   ← join(F_H)
        f'  ← sum out H from f
        factors ← (factors − F_H) ∪ {f'}
    f ← join(factors)
    return normalize(f)
```

### Alarm network with variable elimination

Query: $P(B \mid j, m) \propto P(B, j, m)$. Initial factors: $P(B)$, $P(E)$, $P(A \mid B, E)$, $P(j \mid A)$, $P(m \mid A)$.

1. **Choose $A$.** Join $P(A \mid B, E)$, $P(j \mid A)$, $P(m \mid A)$ into $P(j, m, A \mid B, E)$, then sum out $A$ to get $P(j, m \mid B, E)$.
2. Remaining factors: $P(B)$, $P(E)$, $P(j, m \mid B, E)$.
3. **Choose $E$.** Join $P(E)$ and $P(j, m \mid B, E)$ into $P(j, m, E \mid B)$, then sum out $E$ to get $P(j, m \mid B)$.
4. Remaining factors: $P(B)$, $P(j, m \mid B)$.
5. **Finally $B$.** Join into $P(j, m, B)$ and normalize to get $P(B \mid j, m)$.

![Variable elimination on the alarm network](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/03_Bayesian_Network_Inference/ve-alarm.svg)

*Eliminating $A$ produces $f_1(B, e, j, m)$; eliminating $E$ produces $f_2(B, j, m)$; joining with $P(B)$ and normalizing gives the answer.*

The same computation in equations:

$$
\begin{aligned}
P(B \mid j, m) &\propto P(B, j, m) \\
&= \sum_{e, a} P(B, j, m, e, a) && \text{marginal from joint by summing out} \\
&= \sum_{e, a} P(B)P(e)P(a \mid B, e)P(j \mid a)P(m \mid a) && \text{BN joint expression} \\
&= \sum_{e} P(B)P(e) \sum_{a} P(a \mid B, e)P(j \mid a)P(m \mid a) && x(y + z) = xy + xz \\
&= \sum_{e} P(B)P(e)\,f_1(B, e, j, m) && \text{join on } a\text{, sum out gives } f_1 \\
&= P(B) \sum_{e} P(e)\,f_1(B, e, j, m) && x(y + z) = xy + xz \\
&= P(B)\,f_2(B, j, m) && \text{join on } e\text{, sum out gives } f_2
\end{aligned}
$$

> [!tip] <span style="color: #5ad4b5">Why VE is faster</span>
> All VE does is exploit the distributive law, e.g. $uwy + uwz + uxy + uxz + vwy + vwz + vxy + vxz = (u + v)(w + x)(y + z)$. Pushing sums inside products avoids repeated multiplications.

### Elimination order

The elimination order changes the computational cost. Complexity depends critically on the size of the **largest factor** generated (its number of table entries).

**Example query** $P(X_3 \mid Y_1 = y_1, Y_2 = y_2, Y_3 = y_3)$, where $Z$ is the parent of $X_1, X_2, X_3$ and each $X_i$ has an observed child $Y_i$:

| Order | Effect |
|---|---|
| $X_1, X_2, Z$ | Every generated factor has one variable, size 2 |
| $Z$ first | Joining on $Z$ connects its children, giving a factor of size 4 |

![Elimination order](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/03_Bayesian_Network_Inference/elimination-order.svg)

*$Z$ is shared by every $X_i$. Eliminating $Z$ first creates one factor over all its children ($2^{n+1}$ entries); eliminating the $X_i$ first keeps every factor at 2 variables.*

**General query** $P(X_n \mid y_1, \dots, y_n)$ on the same structure:

| Order | Largest factor |
|---|---|
| $Z, X_1, \dots, X_{n-1}$ | $n + 1$ variables, $2^{n+1}$ entries |
| $X_1, \dots, X_{n-1}, Z$ | 2 variables, $2^2$ entries |

> [!warning] <span style="color: #ff939b">No guarantee of a good order</span>
> In general, there may be no ordering that only produces small factors.

## 4. Bayesian Networks: Representation and D-Separation

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Bayesian Networks  
> **Source**: [4-BayesianNetworks-Representation.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/Bayesian%20Networks/4-BayesianNetworks-Representation.pdf), Dr Jan Buys, slides 1-14 (based on Klein and Abbeel, CS188 UC Berkeley)  
> **Generated**: 2026-10-29  

### Conditional independence in a Bayesian network

#### Definitions

> **Conditional independence**: $X$ is conditionally independent of $Y$ given $Z$ when $\forall x, y, z : P(x \mid z, y) = P(x \mid z)$, written $X \perp\!\!\!\perp Y \mid Z$.

Conditional independence is a property of a **distribution**. Defining a BN makes one assumption per node — each variable depends only on its parents given its predecessors in a topological order:

$$
P(x_i \mid x_1, \dots, x_{i-1}) = P(x_i \mid \text{parents}(X_i))
$$

There may be **additional** conditional independences in the distribution beyond these. D-separation reads them off the graph.

### Implied independences: a chain example

Consider the chain $X \rightarrow Y \rightarrow Z \rightarrow W$. Compare the chain rule with the BN joint:

$$
P(X)P(Y \mid X)P(Z \mid X, Y)P(W \mid X, Y, Z) = P(X)P(Y \mid X)P(Z \mid Y)P(W \mid Z)
$$

![Chain X to W](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/04_Representation_And_D_Separation/chain-example.svg)

*In the chain $X \rightarrow Y \rightarrow Z \rightarrow W$, each node depends only on its immediate predecessor.*

Matching factors gives independences directly from the BN definition:

- $Z \perp\!\!\!\perp X \mid Y$
- $W \perp\!\!\!\perp X, Y \mid Z$

An additional implied independence, not stated directly by any single factor:

- $W \perp\!\!\!\perp X \mid Y$

### The three canonical triples

#### Definitions

> **D-separation**: A procedure for deriving conditional independences from a Bayesian network graph.

D-separation considers variable triples and decides whether they are (conditionally) independent. Any graph can be analyzed using three cases.

![Canonical triples](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/04_Representation_And_D_Separation/canonical-triples.svg)

*The three lecture examples: a causal chain (low pressure → rain → traffic), a common cause (project due → forums busy, lab full), and a common effect (raining, sports match → traffic).*

| Case | Structure | Without evidence on $Y$ | Given $Y$ |
|---|---|---|---|
| Causal chain | $X \rightarrow Y \rightarrow Z$ | Dependence possible | $X \perp\!\!\!\perp Z \mid Y$ |
| Common cause | $X \leftarrow Y \rightarrow Z$ | Dependence possible | $X \perp\!\!\!\perp Z \mid Y$ |
| Common effect | $X \rightarrow Z \leftarrow Y$ | $X \perp\!\!\!\perp Y$ | Dependence possible |

### Case 1: causal chain

$X$: low pressure → $Y$: rain → $Z$: traffic. The joint is $P(x, y, z) = P(x)P(y \mid x)P(z \mid y)$.

- We **cannot** guarantee that $X$ is independent of $Z$.
- We **can** say $X$ is independent of $Z$ given $Y$:

$$
P(z \mid x, y) = \frac{P(x, y, z)}{P(x, y)} = \frac{P(x)P(y \mid x)P(z \mid y)}{P(x)P(y \mid x)} = P(z \mid y)
$$

Evidence along the chain "blocks" the influence.

### Case 2: common cause

$Y$: project due is the parent of $X$: forums busy and $Z$: lab full. The joint is $P(x, y, z) = P(y)P(x \mid y)P(z \mid y)$.

- We **cannot** guarantee that $X$ is independent of $Z$.
- We **can** say $X$ and $Z$ are independent given $Y$:

$$
P(z \mid x, y) = \frac{P(x, y, z)}{P(x, y)} = \frac{P(y)P(x \mid y)P(z \mid y)}{P(y)P(x \mid y)} = P(z \mid y)
$$

Observing the cause blocks the influence between the effects.

### Case 3: common effect (v-structure)

#### Definitions

> **V-structure (collider)**: A triple $X \rightarrow Z \leftarrow Y$ where two arcs meet head-to-head at $Z$.

$X$: raining and $Y$: sports match are both parents of $Z$: traffic. The joint is $P(x, y, z) = P(x)P(y)P(z \mid x, y)$.

- $X$ **is** independent of $Y$: $P(x \mid y) = P(x)$.
- $X$ and $Y$ are **not** conditionally independent given $Z$.

This is backwards from the other two cases. Observing an effect activates influence between its possible causes, because they are **two competing explanations**. If traffic is heavy and you learn there is a sports match, rain becomes less likely.

### Active and inactive paths

#### Definitions

> **Active path**: An undirected path between two nodes along which influence can flow given the evidence. A path is active only if **every** triple on it is active.

> **Inactive (blocked) path**: A path containing at least one inactive triple. A single inactive segment blocks the whole path.

To ask whether $X$ and $Y$ are conditionally independent given evidence $Z$, shade the evidence nodes and consider all undirected paths from $X$ to $Y$. **No active paths means independence.**

> [!warning] <span style="color: #ff939b">A blocked-by-shading rule is not enough</span>
> A first attempt — "two nodes are independent if every path is blocked by an observed node" — works for chains and forks but fails for v-structures, where observing the middle node *opens* the path. Paths must be checked triple by triple.

![Active and inactive triples](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/04_Representation_And_D_Separation/active-inactive-triples.svg)

*Chains and forks are active only when the middle node is unobserved. A v-structure is the opposite: it becomes active when the middle node or any descendant is observed (shaded).*

| Triple type | Active when | Inactive when |
|---|---|---|
| Causal chain $A \rightarrow B \rightarrow C$ (either direction) | $B$ unobserved | $B$ observed |
| Common cause $A \leftarrow B \rightarrow C$ | $B$ unobserved | $B$ observed |
| Common effect $A \rightarrow B \leftarrow C$ | $B$ **or one of its descendants** observed | $B$ and all its descendants unobserved |

### The d-separation algorithm

Query: $X_i \perp\!\!\!\perp X_j \mid \{X_{k_1}, \dots, X_{k_n}\}$?

1. Shade the evidence nodes $X_{k_1}, \dots, X_{k_n}$.
2. Enumerate all (undirected) paths between $X_i$ and $X_j$.
3. For each path, check every consecutive triple against the active/inactive table.
4. If one or more paths are active, independence is **not guaranteed**.
5. If **all** paths are inactive, independence **is guaranteed**.

Running d-separation over all queries gives a complete list of conditional independences for a BN. That list determines the set of probability distributions the BN can represent.

### D-separation examples

**Example 1** — $R \rightarrow T \leftarrow B$, $T \rightarrow T'$.

![D-separation example 1](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/04_Representation_And_D_Separation/dsep-example-1.svg)

*With a collider at $T$, $R$ and $B$ are independent until $T$ or its descendant $T'$ is observed.*

| Query | Answer | Reason |
|---|---|---|
| $R \perp\!\!\!\perp B$ | Yes | Collider at $T$ is unobserved |
| $R \perp\!\!\!\perp B \mid T$ | No | Observing the collider activates it |
| $R \perp\!\!\!\perp B \mid T'$ | No | Observing a descendant of the collider activates it |

**Example 2** — add $L \rightarrow R$ and $R \rightarrow D$ to example 1.

![Extended traffic network](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/04_Representation_And_D_Separation/extended-traffic.svg)

*$L \rightarrow R$, $R \rightarrow D$, $R \rightarrow T \leftarrow B$, $T \rightarrow T'$. The collider at $T$ connects $R$ and $B$ when $T$ or $T'$ is observed, but observing $R$ blocks the chain from $L$.*

| Query | Answer | Reason |
|---|---|---|
| $L \perp\!\!\!\perp T' \mid T$ | Yes | Chain $R \rightarrow T \rightarrow T'$ blocked by observed $T$ |
| $L \perp\!\!\!\perp B$ | Yes | Collider at $T$ unobserved |
| $L \perp\!\!\!\perp B \mid T$ | No | Collider at $T$ observed; chain $L \rightarrow R \rightarrow T$ active |
| $L \perp\!\!\!\perp B \mid T'$ | No | Descendant of collider observed |
| $L \perp\!\!\!\perp B \mid T, R$ | Yes | Observed $R$ blocks the chain $L \rightarrow R \rightarrow T$ |

**Example 3** — $R$: raining, $T$: traffic, $D$: roof drips, $S$: I'm sad. $R \rightarrow T$, $R \rightarrow D$, $T \rightarrow S$, $D \rightarrow S$.

![Rain, traffic, drips, and sadness](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/04_Representation_And_D_Separation/rain-traffic-drips.svg)

*There are two paths between $T$ and $D$: a fork through $R$ and a collider through $S$. Each query depends on which of these is open.*

| Query | Answer | Reason |
|---|---|---|
| $T \perp\!\!\!\perp D$ | No | Fork through unobserved $R$ is active |
| $T \perp\!\!\!\perp D \mid R$ | Yes | Fork blocked by $R$; collider at $S$ unobserved |
| $T \perp\!\!\!\perp D \mid R, S$ | No | Observing $S$ activates the collider path |

## 5. Decision Networks and Value of Information

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Bayesian Networks  
> **Source**: [5-DecisionNetworks.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/Bayesian%20Networks/5-DecisionNetworks.pdf), Dr Jan Buys, slides 1-31 (based on Klein and Abbeel, CS188 UC Berkeley; some slides from Deshen Moodley)  
> **Generated**: 2026-10-29  

### Rationality and expected utility

#### Definitions

> **Rational**: Maximally achieving pre-defined goals. Rationality concerns only which decisions are made, not the thought process behind them.

> **Expected utility**: The probability-weighted average utility of an action's possible outcomes.

The goal of AI can be defined as building agents that act rationally. Goals are expressed as the **utility** of outcomes, so being rational means **maximizing expected utility**.

Many AI problems can be framed as decision making. A rational agent chooses actions that maximize its expected utility given its knowledge. This raises two questions:

- Where do utilities come from?
- How can Bayesian networks be extended to choose actions that maximize expected utility?

### Utility-based agents and utilities

#### Definitions

> **Utility function**: A measure of success or happiness at a given state; it can measure the degree to which a goal is achieved.

> **Utilities**: Functions from outcomes to real numbers that describe an agent's preferences. They summarize "what the agent wants" as a preference ranking over outcomes.

A utility-based agent:

- Can trade off conflicting goals.
- Can weigh the likelihood of success against the importance of a goal.
- Selects the action with the highest expected utility — the action most likely to lead to a future state closest to the desired goal.

Properties of utilities:

- **Rational preferences** are defined by axioms of rationality. These can be shown to be consistent with maximizing expected utility.
- The standard approach is to set utilities manually and let behaviour emerge from maximizing expected utility.

### Decision networks

#### Definitions

> **Decision network (influence diagram)**: A Bayesian network with added nodes for actions and utility, used to calculate the expected utility of actions.

**Example**: decide whether to take an umbrella when going outside. What is the utility of taking an umbrella if it rains, versus if it is sunny?

![Umbrella decision network](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/05_Decision_Networks_And_Value_Of_Information/umbrella-network.svg)

*Weather (chance) influences the forecast and the utility; the Umbrella decision (rectangle) also feeds the utility (diamond). The forecast is observed; the weather is not.*

### Node types

| Node | Shape | Represents | Rules |
|---|---|---|---|
| **Chance node** | Ellipse | Observed or unobserved random variables, as in a BN | Has a CPT given its parents |
| **Action / decision node** | Rectangle | A decision; acts as observed evidence | Chance-node parents mean their evidence is available at decision time. Action-node parents represent the order of decisions |
| **Utility node** | Diamond | A utility function quantifying how desirable outcomes are | Depends on action and chance nodes; cannot have children |

### Maximum expected utility

#### Definitions

> **Principle of maximum expected utility (MEU)**: Choose the action that maximizes the expected utility given the evidence.

The network designer must define the utility function. Utilities can be analogous to money, with caveats:

- They have no units, only a scale distinguishing best, neutral, and worst outcomes.
- They are best read in relative terms: $20$ is twice as desirable as $10$; $-20$ is as undesirable as $20$ is desirable; $0$ is usually neutral.

For action $a$, evidence $E = e$, hidden parent(s) $S$ of the utility node, and utility $U(s, a)$:

$$
\text{EU}(a, e) = \mathbb{E}_{P(S \mid e)}\big[U(s, a)\big] = \sum_s P(s \mid e)\,U(s, a)
$$

$$
\text{MEU}(e) = \max_a \text{EU}(a, e)
$$

### Action selection procedure

1. Instantiate all the evidence $e$.
2. For each possible value $a$ of the action node:
   1. Compute the posterior $P(S \mid a, e)$ over the unobserved parents $S$ of the utility node — ordinary BN inference with those parents as query variables.
   2. Compute $\text{EU}(a, e)$.
3. Choose the action with the maximum expected utility.

### Umbrella example

| $W$ | $P(W)$ |
|---|---|
| sun | 0.7 |
| rain | 0.3 |

| $A$ | $W$ | $U(A, W)$ |
|---|---|---|
| leave | sun | 100 |
| leave | rain | 0 |
| take | sun | 20 |
| take | rain | 70 |

**No evidence:**

$$
\text{EU}(\text{leave}) = 0.7(100) + 0.3(0) = 70 \qquad \text{EU}(\text{take}) = 0.7(20) + 0.3(70) = 35
$$

$\text{MEU}(\varnothing) = 70$, so the optimal decision is **leave**.

**With evidence $F = \text{bad}$:** inference gives $P(W \mid F = \text{bad})$: sun $0.34$, rain $0.66$.

$$
\text{EU}(\text{leave} \mid \text{bad}) = 0.34(100) + 0.66(0) = 34 \qquad \text{EU}(\text{take} \mid \text{bad}) = 0.34(20) + 0.66(70) = 53
$$

$\text{MEU}(F = \text{bad}) = 53$, so the optimal decision is **take**.

### Information links and decision tables

#### Definitions

> **Information link**: An arc from a chance node to a decision node, indicating that the chance node's value is known when the decision is made. It has no parameters and is not part of the basic evaluation.

> **Decision table (policy)**: A table of optimal actions conditioned on the relevant states of affairs, i.e. on the values of the decision node's parents.

With an information link, evaluation is extended to say explicitly which decision to make for each value of that chance node. This adds an outer loop to action selection:

1. Instantiate any observed evidence.
2. For each combination of values of the decision node's parents:
   1. Compute the expected utility of each action as before.
   2. Record the action with maximum expected utility.

### Machine repair example

A factory machine has a hidden fault with probability $0.2$.

- A faulty machine that is not repaired breaks down mid-production, costing $1000$.
- A repair costs $100$, whether or not the fault was there.
- A diagnostic test reports positive for $90\%$ of faulty machines and $10\%$ of healthy ones.

Questions: should the engineer repair? Should the engineer test first, and what is the test worth?

| $F$ | $P(F)$ |
|---|---|
| faulty | 0.2 |
| ok | 0.8 |

| $F$ | $P(T = \text{pos} \mid F)$ | $P(T = \text{neg} \mid F)$ |
|---|---|---|
| faulty | 0.9 | 0.1 |
| ok | 0.1 | 0.9 |

| $F$ | $D$ | $U(F, D)$ |
|---|---|---|
| faulty | repair | $-100$ |
| ok | repair | $-100$ |
| faulty | don't | $-1000$ |
| ok | don't | $0$ |

**No information.** Act on the prior alone:

$$
\text{EU}(\text{repair}) = 0.2(-100) + 0.8(-100) = -100 \qquad \text{EU}(\text{don't}) = 0.2(-1000) + 0.8(0) = -200
$$

$\text{MEU} = -100$: with no information, always repair.

**Add the information link $T \rightarrow D$.** The link only says $T$ will be known when deciding. The answer becomes a decision table.

![Repair network with information link](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/05_Decision_Networks_And_Value_Of_Information/repair-network.svg)

*Fault influences the test result and the utility; Repair also affects utility. The dashed information link means the test result is known before choosing.*

**Case $T = \text{pos}$:**

$$
P(\text{pos}) = 0.2(0.9) + 0.8(0.1) = 0.26 \qquad P(\text{faulty} \mid \text{pos}) = \frac{0.18}{0.26} = 0.692
$$

$\text{EU}(\text{repair} \mid \text{pos}) = -100$; $\text{EU}(\text{don't} \mid \text{pos}) = 0.692(-1000) = -692$. So $\pi(\text{pos}) = \text{repair}$.

**Case $T = \text{neg}$:**

$$
P(\text{neg}) = 0.2(0.1) + 0.8(0.9) = 0.74 \qquad P(\text{faulty} \mid \text{neg}) = \frac{0.02}{0.74} = 0.027
$$

$\text{EU}(\text{repair} \mid \text{neg}) = -100$; $\text{EU}(\text{don't} \mid \text{neg}) = 0.027(-1000) = -27$. So $\pi(\text{neg}) = \text{don't repair}$. The observation reverses the decision.

| $T$ | $P(T)$ | $P(\text{faulty} \mid T)$ | EU(repair) | EU(don't) | $\pi(T)$ |
|---|---|---|---|---|---|
| pos | 0.26 | 0.692 | $-100$ | $-692$ | repair |
| neg | 0.74 | 0.027 | $-100$ | $-27$ | don't repair |

Compare this with the no-information answer, "always repair".

**The policy is a threshold.** With $p = P(\text{faulty} \mid T)$, repair is optimal exactly when

$$
-100 > -1000\,p \iff p > 0.1
$$

The two observations ($0.692$ and $0.027$) fall on opposite sides of $0.1$.

![Repair threshold](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/05_Decision_Networks_And_Value_Of_Information/repair-threshold.svg)

*Repair is optimal when $P(\text{faulty} \mid T) > 0.1$. A negative test ($0.027$) falls below the threshold and a positive test ($0.692$) above it, so the test changes the decision.*

**What is the test worth?** Average the MEU of each branch over $P(T)$:

$$
\text{MEU}_{\text{test}} = 0.26(-100) + 0.74(-27) = -46 \qquad \text{MEU}_{\text{no test}} = -100
$$

The expected gain is $-46 - (-100) = 54$. It is worth paying up to $54$ to run the test.

> [!warning] <span style="color: #ff939b">Information does not always help</span>
> If repair is cheap, $U(F, \text{repair}) = -5$, the threshold becomes $-5 > -1000\,p \iff p > 0.005$. Both $0.692$ and $0.027$ exceed it, so the policy is "repair" either way and MEU is $-5$ with or without the test. Information has value only when it can change what you do.

### Value of perfect information

#### Definitions

> **Value of perfect information (VPI)**: The expected gain in MEU from observing a variable $E'$ before acting, compared with acting now.

The expected MEU after observing $E'$:

$$
\text{MEU}(E', e) = \mathbb{E}_{P(E' \mid e)}\big[\text{MEU}(e', e)\big] = \sum_{e'} P(e' \mid e)\,\text{MEU}(e', e)
$$

$$
\text{VPI}(E' \mid e) = \text{MEU}(E', e) - \text{MEU}(e)
$$

VPI is **non-negative**: on average, observing more can never hurt a rational decision maker.

**Umbrella example.** $P(F)$: good $0.59$, bad $0.41$.

| Situation | Best action | MEU |
|---|---|---|
| No evidence | leave | $70$ |
| Forecast bad | take | $53$ |
| Forecast good | leave | $95$ |

$$
\text{MEU}(F) = \sum_f P(f)\,\text{MEU}(f) = 0.59 \cdot 95 + 0.41 \cdot 53 = 77.8
$$

$$
\text{VPI}(F) = \text{MEU}(F) - \text{MEU}(\varnothing) = 77.8 - 70 = 7.8
$$

![VPI of the forecast](../../diagrams/CSC3043S-Reasoning%20in%20AI/Bayesian%20Networks/05_Decision_Networks_And_Value_Of_Information/vpi-forecast.svg)

*Observing the forecast first gives MEU 95 (good, leave) or 53 (bad, take); weighted by $P(F)$ that is $77.8$, versus $70$ without it, so $\text{VPI}(F) = 7.8$.*

---

# Part II: Large Language Models

## 1. Introduction to (Large) Language Models

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Large Language Models  
> **Source**: [1-Introduction - Copy.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/LLM%27s/1-Introduction%20-%20Copy.pdf), Dr Jan Buys, slides 1-47  
> **Generated**: 2026-10-29  

### Course organization

| Role | Person |
|---|---|
| Convenor | Dr Jan Buys (jan.buys@uct.ac.za) |
| TA | Christopher Allpass-Jackson (ALLCHR011@myuct.ac.za) |

Prerequisites: CSC2001F, CSC2041F, CSC2042S, CSC3042F. Lectures run in the third term only.

| Topic (2 weeks each) | Lecturer |
|---|---|
| Large language models | Dr Jan Buys |
| Vision language models and visual generative models | Prof Patrick Marais |
| Bayesian networks | Dr Jan Buys |

| Week | Mon | Tue | Wed | Thu | Fri |
|---|---|---|---|---|---|
| 27 Jul | Introduction to LLMs | Tokenization | Transformer architecture for LLMs | LLM training optimization | Tutorial: LLM training implementation |
| 3 Aug | LLM inference | Instruction fine-tuning | LLM alignment | Reasoning and test-time scaling | Tutorial: post-training |

The assignment is training a (small) language model from scratch.

The module covers the **technical fundamentals** of modern language models, not how to use LLMs for applications. It touches NLP concepts but is not an NLP course. The ultimate goal is to understand how LLMs have become AI reasoning models. The main text is Jurafsky and Martin, *Speech and Language Processing* (3rd ed. draft).

### Natural language

#### Definitions

> **Human language**: A system specifically constructed to convey the speaker's or writer's meaning; a discrete, symbolic, categorical signalling system.

> **Morphology**: The rules determining how words are formed.

> **Syntax**: The rules determining which word sequences are valid sentences, regardless of meaning.

> **Semantics**: The meaning of sentences.

> **Distributional hypothesis**: "You shall know a word by the company it keeps." Words occurring in similar contexts have similar meanings.

- Language symbols are categorical ("rocket", "violin"), with minor exceptions for expressive signalling ("I loooove it").
- Symbols can be encoded as sound, gesture, or images (writing); the symbol is invariant across encodings.
- Language consists of sequences of words organized into sentences.

| Level | Example |
|---|---|
| Morphology | "dogs" = "dog" + "s"; isiXhosa "Ndiyabulela" = "Ndi" + "ya" + "bulela" (I am grateful) |
| Syntax | "Colorless green ideas sleep furiously" is valid but meaningless; "Furiously sleep ideas green colorless" is invalid |
| Semantics | Traditionally represented with logics or graphs |

"The best representation of natural language is natural language."

### Natural language processing

#### Definitions

> **Natural language processing (NLP)**: The study of systems that process human language and enable computers to perform useful tasks involving it. The goal is deep understanding of general-purpose language, not just string processing or keyword matching.

> **Representation $\mathcal{R}$**: A form useful for a computer; it may or may not be interpretable by humans or grounded in scientific theory.

Main components of NLP:

| Component | Direction |
|---|---|
| Analysis / understanding | $\text{NL} \rightarrow \mathcal{R}$ |
| Generation | $\mathcal{R} \rightarrow \text{NL}$ |
| Acquisition | Learning $\mathcal{R}$ from knowledge and data |

- Traditional NLP used explicit linguistic representations: parts of speech, syntactic trees, semantic graphs.
- Current approaches use **vector representations** of letters, words, or passages.

### Representations in NLP

#### Definitions

> **Word vectors (embeddings)**: Dense vectors representing words, where similar words lie close together.

> **Contextualized word representations**: Vectors produced by a sequence model (such as a Transformer text encoder) where a word's vector depends on its surrounding context.

![Word embeddings in 2D](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/01_Introduction_To_Language_Models/embedding-projection.svg)

*A 2D (t-SNE) projection of word vectors: function words, negative-sentiment words, and positive-sentiment words each form their own cluster.*

- **Multilingual** embeddings place words from several languages in one space, so translations (e.g. English "money" and German "Geld") lie near each other.
- **Contextual** representations in LLMs give the same word different vectors in different sentences.

### NLP tasks and why NLP is hard

| Understanding | Generation |
|---|---|
| Sentiment analysis | Machine translation |
| Topic classification | Summarization |
| Named entity recognition | Data-to-text generation |
| Question answering | |

Separate models were traditionally built per task. LLMs now handle all of these, plus tasks not traditionally considered NLP, such as code generation and mathematical reasoning.

#### Definitions

> **Ambiguity**: Words and sentences can have many syntactic analyses and meanings, depending on context.

> **Sparsity**: A few words are very frequent, but most are rare, and many valid combinations never occur even in web-scale corpora.

NLP was hard (at least before LLMs) because of:

- **Ambiguity**.
- **Unscalable rules** — formalizing linguistic rules did not scale due to complex structure and a long tail of exceptions.
- **Sparsity**.
- Richness and diversity of language, robustness, and algorithm scalability.

### Brief history of NLP and LLMs

| Period | Dominant approach |
|---|---|
| Before 1990s | Rule-based systems |
| 1990s-2000s | Machine learning, but still pipelines of intermediate linguistic analyses using linguistic resources |
| 2010s | Neural (deep learning) "end-to-end" systems trained on large datasets without intermediate linguistic predictions |
| 2020s | **Large language models**: Transformer neural networks trained on very large corpora to learn general text patterns |

LLMs now form the basis of much of AI beyond traditional NLP.

### Language modelling

#### Definitions

> **Language model**: A probabilistic model of a document, $P(w_1, w_2, \dots, w_n; \theta)$, over word tokens drawn from a vocabulary $V$ of word types.

> **Autoregressive language model**: A language model that predicts the next token conditioned on the previous tokens.

Language models predict the next word in a sequence. Using the chain rule:

$$
P(w_1 w_2 \dots w_n) = \prod_i P(w_i \mid w_1 w_2 \dots w_{i-1})
$$

To **generate**, sample one word at a time:

$$
x_1 \sim p(x_1), \quad x_2 \sim p(x_2 \mid x_1), \quad \dots, \quad x_T \sim p(x_T \mid x_1, \dots, x_{T-1})
$$

LM training learns many kinds of knowledge from next-word prediction:

| Prompt | Knowledge type |
|---|---|
| Stanford University is located in ___, California. | Trivia |
| I put ___ fork down on the table. | Syntax |
| The woman walked across the street, checking for traffic over ___ shoulder. | Coreference |
| I went to the ocean to see the fish, turtles, seals, and ___. | Lexical semantics / topic |
| ...the value I got was the sum total of the popcorn and the drink. The movie was ___. | Sentiment |
| Iroh went into the kitchen to make tea. Standing next to Iroh, Zuko pondered his destiny. Zuko left the ___. | Some reasoning (harder) |
| 1, 1, 2, 3, 5, 8, 13, 21, ___ | Basic arithmetic |

### Classical and modern views of language models

**Classical view**: LMs model **fluency** and are one component of an NLP system, applied through Bayes' rule:

$$
P(\text{output} \mid \text{input}) \propto P(\text{input} \mid \text{output})\,P(\text{output})
$$

| Application | LM preference |
|---|---|
| Machine translation | $P(\text{"high winds tonight"}) > P(\text{"large winds tonight"})$ |
| Spell correction | $P(\text{"about fifteen minutes from"}) > P(\text{"about fifteen minuets from"})$ |
| Speech recognition | $P(\text{"recognize speech"}) > P(\text{"wreck a nice beach"})$; $P(\text{"I saw a van"}) \gg P(\text{"eyes awe of an"})$ |

**Modern view**: LMs

- generate text directly;
- recall factual knowledge from training data;
- perform reasoning;
- execute instructions when prompted;
- condition on multimodal inputs (e.g. images) and generate code, commands, and more.

### N-gram language models

#### Definitions

> **N-gram model**: A count-based LM that conditions on a fixed sliding window of the previous $N - 1$ tokens. A 5-gram model predicts the 5th word from the previous 4.

> **Smoothing**: Adjusting count-based estimates so unseen n-grams get non-zero probability.

The sliding window is used both to build training data and to score n-grams.

![N-gram sliding window](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/01_Introduction_To_Language_Models/ngram-window.svg)

*Sliding a window across "Thou shalt not make a machine…" turns each position into a training example: two input words predict the next.*

- Even in a very large corpus, **most possible n-grams never appear**. A bigram count table over a small vocabulary is mostly zeros.
- Models must still assign non-zero probability to every n-gram.
- Complex formulas interpolate between n-gram sizes and smooth the distribution. **Modified Kneser-Ney smoothing** was state of the art.

| Strength | Weakness |
|---|---|
| Very computationally efficient; fast to train on large data | Sparsity prevents effective use of long contexts, even with $> 1$ trillion training tokens |
| Can score many candidate sequences, e.g. in statistical machine translation | |

### Neural language model architectures

![Feedforward language model](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/01_Introduction_To_Language_Models/feedforward-lm.svg)

*A feedforward LM concatenates embeddings of a fixed window of previous words, so like an n-gram model it only sees a short context.*

![Recurrent language model](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/01_Introduction_To_Language_Models/rnn-lm.svg)

*An RNN LM carries a hidden state along the whole sequence, predicting the next word (and computing a loss) at every step.*

| Architecture | Context | Notes |
|---|---|---|
| Feedforward neural LM | Fixed small window | Shares many n-gram limitations |
| Recurrent neural network (RNN) | No explicit length limit | **LSTM** RNNs were the first widely used deep-learning LMs |
| **Transformer** | Full sequence via attention | More scalable than LSTMs; now dominant |

### Three topologies for LLMs

![Three LLM topologies](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/01_Introduction_To_Language_Models/model-topologies.svg)

*Decoders attend only to earlier positions; encoders attend in both directions; encoder-decoders encode the input bidirectionally and decode the output causally with cross-attention to the encoder.*

#### Definitions

> **Causal mask**: An attention mask that lets each token condition only on past tokens.

> **Masked language modelling (MLM)**: Pretraining by re-predicting a random subset of masked tokens using context on both sides.

> **Cross-attention**: Attention in which the decoder attends to the encoder's outputs.

| Topology | Example | How it works | Use |
|---|---|---|---|
| **Decoder** | GPT-style LLMs | Autoregressive next-token prediction with a causal mask | Most LLMs, but not the only option |
| **Encoder** | BERT (Devlin et al., 2018) | Bidirectional; pretrained with MLM (randomly mask $15\%$ of tokens) | Encodes rather than generates; fine-tuned with a classification head |
| **Encoder-decoder** | Original Transformer (Vaswani et al., 2017); T5 (Raffel et al., 2019) | Encoder reads input; decoder generates output via cross-attention | Translation; multi-task text-to-text |

**BERT** was the first work to show that pretraining a Transformer on a large corpus beats task-specific training alone. For a downstream task, the model is trained as a classifier with parameters initialized from pretraining.

![BERT masked language modelling](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/01_Introduction_To_Language_Models/bert-mlm.svg)

*BERT replaces about 15% of input tokens with [MASK] and re-predicts them using context from both sides.*

**T5** frames every task as text-to-text: the encoder reads the task name and input, and the decoder generates the output (e.g. "translate English to German: That is good." → "Das ist gut."). It is pretrained on denoising objectives:

![T5 text-to-text](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/01_Introduction_To_Language_Models/t5-text-to-text.svg)

*T5 handles translation, acceptability, similarity, and summarization with one model: the task prefix and input go in, the answer comes out as text.*

| Part | Text |
|---|---|
| Original | Thank you for inviting me to your party last week. |
| Input | Thank you `<X>` me to your party `<Y>` week. |
| Target | `<X>` for inviting `<Y>` last `<Z>` |

### Using decoder LLMs for tasks

Decoder LMs can do text-to-text tasks by predicting the output as a **continuation** of the input.

- Summarization: append "TL;DR:" after the text.
- Question answering: build a prompt and let the model continue.
- Fine-tuning on many tasks (as with T5), at large scale, lets the model **follow instructions for new tasks** not seen during fine-tuning.

### Three stages of LLM training

![Three stages of LLM training](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/01_Introduction_To_Language_Models/training-stages.svg)

*Pretraining on text gives a pretrained LLM; instruction tuning gives an instruction-tuned LLM; preference alignment gives an aligned LLM.*

| Stage | Data | Result |
|---|---|---|
| 1. Pretraining | Large text corpora | Pretrained LLM |
| 2. Instruction tuning | Instruction-response pairs (e.g. label sentiment, summarize, translate) | Instruction-tuned LLM |
| 3. Preference alignment | Preference data: preferred vs dispreferred responses (e.g. refusing to help with embezzlement) | Aligned LLM |

## 2. Tokenization

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Large Language Models  
> **Source**: [2-Tokenization.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/LLM%27s/2-Tokenization.pdf), Dr Jan Buys, slides 1-25 (based on Jurafsky and Martin Ch. 2; some slides from Stanford CS336)  
> **Generated**: 2026-10-29  

### What tokenization does

#### Definitions

> **Token**: An element $w_i$ of the sequence $w_1, w_2, \dots, w_n$ a language model processes. Each token comes from the model's vocabulary, $w_i \in V$, and is represented as an index into the vocabulary list.

> **Tokenization**: Converting a string of text into a sequence of token indices.

> **Compression ratio**: The number of bytes of raw text per token.

A good tokenizer produces a relatively **compact** sequence of tokens without making the **vocabulary too large**. Both affect efficiency and model expressiveness.

There are four kinds of tokenizer: character, byte, word, and subword.

### Character and byte tokenizers

#### Definitions

> **Code point**: The integer assigned to a Unicode character.

> **UTF-8**: The most common Unicode encoding; some characters take one byte, others several.

| Tokenizer | Vocabulary | Compression ratio | Problem |
|---|---|---|---|
| **Character** | Unicode code points, about 150K characters, many very rare | Low | Inefficient use of the vocabulary |
| **Byte** | 256 byte values (0-255) | Exactly 1 | Sequences are very long |

### Word tokenizers

Traditional NLP splits strings into words. Words are separated by spaces, but punctuation and special characters need handling.

- Generally separate punctuation from words.
- Exceptions where punctuation belongs to the word:
  - abbreviations: km/h, Ph.D., AT&T
  - prices: R45,55
  - dates: 05-04-2021
  - clitics: we're
  - multi-word expressions: \$37-a-share
- The simplest rule keeps alphanumeric characters together and separates everything else; traditional tokenizers use more complex regular expressions.

#### Definitions

> **UNK token**: A special token traditionally used to represent any word not in the vocabulary.

| Advantages | Disadvantages |
|---|---|
| Each token is meaningful | Vocabulary can be huge |
| Good compression ratio | A fixed vocabulary always risks unseen words; `UNK` removes information and limits the model |
| | Word complexity varies by language (e.g. isiZulu vs Sesotho) |

### Subword tokenization

#### Definitions

> **Subword tokenizer**: A tokenizer trained on raw text to build a vocabulary tailored to the data, instead of using fixed rules for what a token is.

> **Subword tokens**: Sub-parts of whole words, chosen so that any string can be split into subwords in $V$.

- The vocabulary size is a **hyperparameter**, and it determines the compression ratio.
- Intuition: common byte sequences (common words) become a single token; rare sequences are represented by many tokens.

Example: "This is a newly spoken sentence." → `Th is is a new ly spok en se ntence .`

Why subwords?

- **Unknown words** become sequences of known subwords: `newwebsite.com` → `new website .com` instead of `[UNK]`.
- **Compositional meaning**: if "dog" was seen only in the singular but "-s" was seen on other plurals, "dogs" = "dog" + "s".
- **Morphological complexity**: subwords may correspond to morphemes, helping morphologically rich languages.

### Byte-pair encoding (BPE)

#### Definitions

> **Byte-pair encoding (BPE)**: A subword algorithm that repeatedly merges the most frequent pair of adjacent symbols in the training corpus.

> **Type learner**: The part that takes a raw training corpus and induces a vocabulary (a set of types).

> **Token segmenter**: The part that tokenizes a raw test sentence using that vocabulary.

BPE lets the data decide how to tokenize, ideally adapting to the language automatically.

| Algorithm | Reference | Notes |
|---|---|---|
| **BPE** | Sennrich et al., 2016 | Most widely used. First proposed for data compression (Gage 1994), then adapted to neural MT, now standard in LLMs |
| **Unigram LM tokenization** | Kudo, 2018 | Can perform better in some cases |
| **WordPiece** | Schuster and Nakajima, 2012 | |

**Type learner:**

1. Start with a vocabulary of all individual characters, $V = \{A, B, C, D, \dots, a, b, c, d, \dots\}$, and represent the corpus with them.
2. Repeat until $k$ merges have been done:
   1. Choose the two symbols most frequently adjacent in the corpus, say `A` `B`.
   2. Add the merged symbol `AB` to the vocabulary.
   3. Replace every adjacent `A` `B` in the corpus with `AB`.

```text
function BYTE-PAIR-ENCODING(strings C, number of merges k) returns vocab V
    V ← all unique characters in C          # initial tokens are characters
    for i = 1 to k do                       # merge tokens k times
        tL, tR ← most frequent pair of adjacent tokens in C
        tNEW ← tL + tR                      # concatenate into a new token
        V ← V + tNEW                        # update the vocabulary
        replace each occurrence of tL, tR in C with tNEW   # update the corpus
    return V
```

### Pre-tokenization and word boundaries

#### Definitions

> **Pre-tokenization**: The first step of tokenization — typically split on spaces, separate punctuation, and possibly normalize text encoding — before BPE runs on the resulting initial tokens.

> **Start-of-word symbol `_`**: A special symbol added after spaces so BPE can represent boundaries between tokens (alternatively, an end-of-word marker is used).

Pre-tokenization allows more efficient data structures for BPE.

![Applying BPE](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/02_Tokenization/bpe-pipeline.svg)

*Raw text is pre-tokenized with start-of-word markers, then learned merges split it into subword tokens such as `_new ly` and `_spok en`.*

| Stage | Text |
|---|---|
| Raw | This is a newly spoken sentence. |
| Add boundary symbols | `_This _is _a _newly _spoken _sentence .` |
| Apply BPE | `_Th is _is _a _new ly _spok en _se ntence .` |

### BPE toy corpus example

The corpus uses end-of-word `_`. Initial vocabulary: `_, d, e, i, l, n, o, r, s, t, w`.

| Count | Word |
|---|---|
| 5 | `l o w _` |
| 2 | `l o w e s t _` |
| 6 | `n e w e r _` |
| 3 | `w i d e r _` |
| 2 | `n e w _` |

| Merge | Why | Vocabulary added |
|---|---|---|
| 1. `e r` → `er` | Most frequent pair ($6 + 3 = 9$) | `er` |
| 2. `er _` → `er_` | | `er_` |
| 3. `n e` → `ne` | | `ne` |
| 4. `ne w` → `new` | | `new` |
| 5. `l o` → `lo` | | `lo` |
| 6. `lo w` → `low` | | `low` |
| 7. `new er_` → `newer_` | | `newer_` |
| 8. `low _` → `low_` | | `low_` |

Final vocabulary: `_, d, e, i, l, n, o, r, s, t, w, er, er_, ne, new, lo, low, newer_, low_`.

![BPE merges on the toy corpus](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/02_Tokenization/bpe-merges.svg)

*Each merge joins the most frequent adjacent pair and adds one symbol; after eight merges "newer_" and "low_" are single tokens.*

### The BPE segmenter

On data other than the training corpus, run each learned merge **greedily, in the order learned**. Test-set frequencies play no role.

1. Merge every `e r` to `er`.
2. Then merge every `er _` to `er_`.
3. Continue through the merge list.

| Test word | Result |
|---|---|
| `n e w e r _` | One token: `newer_` |
| `l o w e r _` | Two tokens: `low er_` |

Properties in practice:

- The most frequent words are in the vocabulary as single tokens; rare words are split.
- Subwords may or may not correspond to morphemes.
- There is no out-of-vocabulary problem: any word can be tokenized as long as its characters/bytes are in the vocabulary. E.g. `_jskbnckajs` → `_j sk b n ck a j s`.

### Best practices

- Perform as few lossy normalizations as possible. For most tasks, do **not** lowercase or remove punctuation.
- To support a wide range of characters, use Unicode normalization or **byte-level** encoding.
- Subword tokenization is standard. BPE is most common; Unigram has performed better in some cases.
- Widely used libraries: Hugging Face **Tokenizers** and OpenAI **tiktoken**.
- For large-scale tokenization, use a library with an efficient C++ or Rust implementation.

## 3. Transformer Architecture for Large Language Models

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Large Language Models  
> **Source**: [3-TransformersForLLMs - Copy.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/LLM%27s/3-TransformersForLLMs%20-%20Copy.pdf), Dr Jan Buys, slides 1-40 (slides from Tatsu Hashimoto, Stanford CS336; figures from Jurafsky and Martin)  
> **Generated**: 2026-10-29  

### Original versus modern Transformer

The Transformer is the dominant LLM architecture. There is no single standard version, but several choices that differ from the original have become standard.

| Component | Original (Vaswani et al., 2017) | Modern LLM variant |
|---|---|---|
| Attention | Multi-head attention (MHA) | Grouped-query attention (GQA) with a KV cache |
| Position | Fixed sine/cosine positional embeddings | Rotary position embeddings (RoPE) |
| Feedforward | ReLU FFN per position | SwiGLU FFN, no bias terms |
| Normalization | LayerNorm **after** attention/FFN (post-norm) with residuals | RMSNorm **before** attention/FFN (pre-norm) |

Modern models also make particular hyperparameter choices. The best references are the tech reports of open-weight models: Llama 3, Qwen 2.5, Gemma 2, OLMo 2.

![Original versus modern block](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/original-vs-modern.svg)

*The original block normalizes after each residual add and uses sinusoidal positions and ReLU; the modern block normalizes before causal GQA with RoPE and a SwiGLU FFN.*

### Token embedding

#### Definitions

> **Embedding matrix $E$**: A matrix of dimension $|V| \times d$ storing one $d$-dimensional embedding vector per vocabulary entry.

After tokenization, each token is mapped to an input embedding. The lookup is implemented by representing each token index as a one-hot vector and multiplying by $E$:

$$
X = \text{OneHot}(w_{1:N})\,E, \qquad \text{OneHot}(w_{1:N}) \in \{0, 1\}^{N \times |V|}, \quad X \in \mathbb{R}^{N \times d}
$$

![Token embedding lookup](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/token-embedding.svg)

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

![Self-attention for one output](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/self-attention.svg)

*Query $q_3$ is compared with keys $k_1, k_2, k_3$; the softmax weights combine $v_1, v_2, v_3$ into output $y_3$.*

### Self-attention as matrix operations

Self-attention across all time steps is computed with matrix multiplication. Stack the inputs in $X \in \mathbb{R}^{N \times d}$:

$$
Q = X W^Q, \qquad K = X W^K, \qquad V = X W^V
$$

![Q, K and V projections](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/qkv-projections.svg)

*The same three weight matrices are applied to every input row, giving one query, key, and value per token.*

$$
\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}} + M\right) V
$$

#### Definitions

> **Causal mask $M$**: An $N \times N$ matrix with $0$ on and below the diagonal and $-\infty$ above it, so after the softmax each position attends only to itself and earlier positions.

In a decoder model the attention is masked, because the model must not see future tokens when predicting the next one.

![Masked attention as matrix operations](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/masked-attention.svg)

*$QK^\top$ gives all pairwise scores; the mask sets future entries to $-\infty$; a row-wise softmax and multiplication by $V$ give the outputs $A$.*

### Multi-head self-attention

#### Definitions

> **Attention head**: One attention computation with its own query, key, and value parameters.

> **Multi-head attention (MHA)**: Several attention heads run in parallel to capture multiple relations between elements; their outputs are concatenated and linearly projected.

$$
\text{head}_i = \text{Attention}(XW_i^Q, XW_i^K, XW_i^V), \qquad \text{MHA}(X) = (\text{head}_1 \oplus \dots \oplus \text{head}_h)\,W^O
$$

Set $d_q = d_k = d_v = d/h$. The concatenation then has dimension $d$, and the total parameters and computation stay similar to a single head of size $d$.

![Multi-head attention](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/multi-head-attention.svg)

*Four heads each produce an $N \times d_v$ output; these are concatenated and projected by $W^O$ back to $N \times d$.*

### KV cache

#### Definitions

> **KV cache**: Stored keys and values from previous time steps, reused during generation so they are not recomputed.

During inference, the context grows by one token each step, so attention would have to be recomputed over the whole prefix. Caching keys and values avoids this.

1. A new token arrives and computes its own $q$, $k$, $v$.
2. Its $k$ and $v$ are appended to the layer's cache.
3. The new query attends to all cached keys.
4. The output is the weighted sum of cached values.

![KV cache](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/kv-cache.svg)

*Without a cache, step 4 recomputes keys and values for all four tokens. With a cache, only token 4's query, key, and value are computed; earlier keys and values are read from memory.*

### Grouped-query attention (GQA)

#### Definitions

> **Multi-query attention (MQA)**: Attention with a single key head and a single value head shared by all query heads; queries stay separate per head.

> **Grouped-query attention (GQA)**: Attention with several key/value heads, each shared by a group of query heads.

Using a KV cache requires many memory operations, which limits computational efficiency. Sharing keys and values across heads reduces how many key/value heads must be read from the cache.

![MHA, GQA and MQA](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/mha-gqa-mqa.svg)

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

![RoPE rotation](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/rope-rotation.svg)

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

![ReLU, GELU and Swish](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/activation-functions.svg)

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

![Post-norm versus pre-norm](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/03_Transformer_Architecture/pre-norm-vs-post-norm.svg)

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

## 4. Large Language Model Pretraining

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Large Language Models  
> **Source**: [4-Pretraining - Copy.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/LLM%27s/4-Pretraining%20-%20Copy.pdf), Dr Jan Buys, slides 1-34 (slides from Jurafsky and Martin, Tatsunori Hashimoto, others as cited)  
> **Generated**: 2026-10-29  

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

![Language modelling head](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/04_Pretraining/lm-head.svg)

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

![Data cleaning pipeline](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/04_Pretraining/data-cleaning.svg)

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

![WSJ perplexity](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/04_Pretraining/wsj-perplexity.svg)

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

![Floating-point formats](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/04_Pretraining/float-formats.svg)

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

![Batching](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/04_Pretraining/batching.svg)

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

![Gradient accumulation](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/04_Pretraining/gradient-accumulation.svg)

*Four microbatches add their gradients to a running total; one optimizer step then uses the average.*

### Multi-GPU training

Large-scale training needs several kinds of parallelism (details are outside the scope of the course):

- Batch parallelism
- Data parallelism
- Fully sharded data parallelism
- Tensor parallelism
- Pipeline parallelism

## 5. Text Generation with Language Models

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Large Language Models  
> **Source**: [5-Generation.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/LLM%27s/5-Generation.pdf), Dr Jan Buys, slides 1-23 (some slides from Antoine Bosselut and Yejin Choi)  
> **Generated**: 2026-10-29  

### Autoregressive generation

#### Definitions

> **Logits**: The vector of unnormalized scores $S \in \mathbb{R}^{|V|}$ the model computes for every vocabulary token at a time step.

At each time step $t$, an autoregressive LM takes the previous tokens $y_{<t}$ as input and outputs a new token $\hat{y}_t$, which is appended to the input for the next step.

![Autoregressive generation](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/05_Text_Generation/autoregressive.svg)

*The model reads the tokens so far and outputs $\hat{y}_t$, which is appended to the input for the next step.*

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

![Greedy decoding tree](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/05_Text_Generation/greedy-tree.svg)

*Greedy takes "yes" ($0.5$) then "yes" ($0.4$) for $0.20$, but "ok ok" scores $0.4 \times 0.7 = 0.28$: the locally best first token leads to a worse sequence.*

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

![Beam search](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/05_Text_Generation/beam-search.svg)

*With $k = 2$, every kept prefix is expanded, all expansions are scored by cumulative score, and only the two best (teal) survive to the next step.*

With beam size 2, the beam might hold "arrived" and "the" at $t_1$, then "the green" and "the witch" at $t_2$, discarding other expansions.

### Problems with maximization-based decoding

- Maximization-based decoding (greedy, beam search) does **not** generate high-quality open-ended text in practice. It tends to produce **repetitive** phrases.
- It may not reflect how language works. Beam search keeps the per-token probability near 1, while human text constantly includes lower-probability tokens.

![Beam search versus human text](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/05_Text_Generation/beam-vs-human.svg)

*Per-token probability over 100 timesteps: beam search stays close to 1, while human text swings widely between likely and unlikely words.*

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

![Top-k on flat and peaked distributions](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/05_Text_Generation/topk-flat-peaked.svg)

*With a fixed $k = 5$, the flat distribution loses plausible words (too quick), while the peaked one keeps unlikely words (too slow).*

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

![Top-p sampling](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/05_Text_Generation/top-p.svg)

*With $p = 0.7$, the nucleus holds 5 tokens for a medium distribution, 7 for a flat one, and only 1 for a peaked one.*

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

![Softmax temperature](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/05_Text_Generation/temperature.svg)

*The same four logits become nearly greedy at $\tau = 0.1$, the ordinary softmax at $\tau = 1$, and nearly uniform at $\tau = 10$.*

## 6. LLM Instruction Following

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Large Language Models  
> **Source**: [6-InstructionFollowing.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/LLM%27s/6-InstructionFollowing.pdf), Dr Jan Buys, slides 1-24 (slides from Tatsunori Hashimoto, others as cited)  
> **Generated**: 2026-10-29  

### Language models as assistants

Instruction tuning is stage 2 of LLM training (pretraining → **instruction tuning** → preference alignment). It turns a pretrained LM into an assistant that performs many tasks when prompted, e.g. "I need to throw a dinner party for 6 vegetarians — suggest a 3-course menu with a chocolate dessert."

A pretrained LM alone is not enough. It has no goal; it just generates high-probability words. This leads to:

- Factually incorrect outputs.
- Obscene, biased, or harmful statements.
- No control over how specific or sensible the output is.
- Failing to "understand" a request because it never appeared in that format in training data.

### Alignment

#### Definitions

> **Aligned AI**: An AI that is **helpful, honest, and harmless** (Askell et al., 2020).

Pretrained LMs are not aligned with human values. Prompting can still steer them. Given "It is unethical for hiring decisions to depend on genders. Therefore, if we were to pick a CEO among Amy and Adam, our pick will be ___", a desirable completion is "neither, as we don't know much about their background or experience" (Zhao et al., 2021).

### Supervised instruction fine-tuning

#### Definitions

> **Instruction fine-tuning (SFT)**: Collecting (instruction, output) pairs across many tasks and continuing to train a pretrained LM on them.

> **Loss masking**: Computing the loss only over the response tokens; predictions over the instruction (input) tokens are masked out.

> **Midtraining**: A training stage mixing instruction data with high-quality pretraining data, used by most large models.

![Instruction fine-tuning](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/06_Instruction_Following/instruction-tuning.svg)

*Many instruction-response tasks fine-tune one model, which is then tested on unseen tasks such as answering with a rationale.*

- Training starts from the pretrained parameters.
- It works exactly like pretraining, except for **loss masking**: only the response contributes to the loss.

For instruction $x$ and response $y$:

$$
\mathcal{L}_{\text{SFT}} = -\sum_{t=1}^{|y|} \log P_\theta(y_t \mid x, y_{<t})
$$

![SFT loss masking](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/06_Instruction_Following/loss-masking.svg)

*Instruction tokens are masked out of the loss; only the response tokens are trained on.*

**FLAN-T5 example** (Chung et al., 2022). Training tasks include "What is the boiling point of nitrogen?" → "−320.4F" and a step-by-step arithmetic question ("The cafeteria had 23 apples... used 20... bought 6 more" → "23 − 20 = 3, 3 + 6 = 9"). The model is then evaluated on **unseen tasks**, such as "Can Geoffrey Hinton have a conversation with George Washington? Give the rationale before answering."

**Before vs after instruction tuning** (disambiguation QA): asked which noun the pronoun in "The reporter and the chef will discuss their favorite dishes" refers to, the base model just continues with variants of the sentence and **doesn't answer**. After instruction tuning it explains that the sentence does not indicate whose dishes, so the answer is (C) ambiguous.

### Instruction data

#### Definitions

> **Self-instruct**: Generating synthetic instruction-following examples with an LLM, starting from a small set of seed tasks.

> **Templates**: Patterns that rewrite an existing labelled dataset as instructions.

Training data is the key ingredient of SFT.

| Dataset | Scale | Notes |
|---|---|---|
| SuperNaturalInstructions | 1.6K tasks, 3M+ examples | Classification, sequence tagging, rewriting, translation, QA |
| Flan-T5 | 1.8K additional tasks | T5 encoder-decoder fine-tuned; collections include Muffin, T0-SF, Natural Instructions v2, CoT (reasoning) |
| OpenAssistant | Human-written responses | Example of later high-quality human-annotated data |

The data sources evolved:

1. Mostly existing NLP datasets restructured as instructions using templates.
2. Synthetic data from self-instruct.
3. High-quality human-annotated data.

Example templates:

| Task | Template |
|---|---|
| Sentiment | `{{text}} How does the reviewer feel about the movie?` |
| Extractive QA | `{{context}} From the passage, {{question}}` |
| NLI | `Suppose {{premise}} Can we infer that {{hypothesis}}? Yes, no, or maybe?` |

> [!warning] <span style="color: #ff939b">Data style and hallucination</span>
> Instruction datasets vary in length and style; human evaluators prefer longer responses. Fine-tuning on facts the model does not already know risks **hallucination**. If a response contains a citation, should the model learn that specific reference, or just learn to output citations when asked?

### Scaling instruction fine-tuning

![Scaling instruction fine-tuning](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/06_Instruction_Following/instruction-scaling.svg)

*Held-out accuracy rises with the number of fine-tuning tasks (0 to 1,836) and is much higher for larger models (8B, 62B, 540B).*

From Chung et al. (2022):

- Instruction fine-tuning improves performance by a large margin over no fine-tuning.
- More fine-tuning tasks improves performance.
- An order-of-magnitude larger model (8B → 62B, 62B → 540B) improves performance substantially, both with and without fine-tuning.

### Instruction fine-tuning for safety

#### Definitions

> **Violation rate**: The rate at which unsafe prompts get answered.

> **False refusal rate**: The rate at which the model refuses when answering would be safe.

Models deployed to end users need safety controls. Safety tuning must balance a low violation rate against a low false refusal rate.

![Safety trade-off](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/06_Instruction_Following/safety-tradeoff.svg)

*For Llama 3 8B and 70B, pushing the violation rate down raises the false refusal rate.*

- Collect real unsafe prompts from users (e.g. the **WildChat** dataset), covering categories like unsafe requests, privacy violations, and copyright violations.
- Relatively few examples (about **500**) give significant safety improvements.

### Limitations of supervised instruction fine-tuning

- Annotations are expensive to collect.
- Some tasks, such as open-ended creative generation, have no single right answer.
- Some errors are worse than others, but the LM objective treats all tokens equally.

This motivates explicitly optimizing for human preferences (the next lecture).

### Prompting

#### Definitions

> **Zero-shot prompting**: Giving the model only a text specification of the task, with no examples.

> **Few-shot prompting**: Including a few input-output examples in the prompt.

LLMs can handle many tasks just from incidental exposure in pretraining. For instance, "tl;dr" ("too long; didn't read") signals a summary in web text.

### Zero-shot prompting

Given an unlabelled datapoint $x$, predict label $y$ by wrapping $x$ in a template:

> Review: The movie's acting could've been better, but the visuals and directing were top-notch.
> On a 1 to 4 star scale, the reviewer would probably give this movie

| Classification option | How | Issue |
|---|---|---|
| 1. Generate and read off | Let the model continue and parse the answer | No guarantee it outputs what was asked (e.g. a star number) |
| 2. Compare class probabilities | Score only the valid labels and pick the highest | Always returns a valid class |

### Prompt engineering

#### Definitions

> **Prompt engineering**: Finding prompts that improve task performance.

The prompt can have a large impact. Across many paraphrases of a topic-classification prompt, accuracy ranges from about $0.3$ to $0.7$; lower-perplexity prompts (e.g. "In which section of the newspaper would you expect to find this article?") tend to do better than odd ones ("What's going on?"). Automatic prompt search exists but is not always better than manual engineering.

### Few-shot prompting and in-context learning

#### Definitions

> **In-context learning**: Learning a task from examples in the context, without any parameter update.

Give a few input-output examples, then the new input for the model to complete.

![Few-shot prompt](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/06_Instruction_Following/few-shot-prompt.svg)

*Example input-output pairs specify the task in the context; the model completes the answer for the new input without any weight change.*

- Performance varies with **which** examples are chosen, and even with their **order**.
- More examples generally improve performance.

## 7. LLM Preference Alignment and Reasoning

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Large Language Models  
> **Source**: [7-Alignment.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/LLM%27s/7-Alignment.pdf), Dr Jan Buys, slides 1-29 (slides from Jurafsky and Martin, Tatsunori Hashimoto, others as cited)  
> **Generated**: 2026-10-29  

### Why preference alignment

Preference alignment is stage 3 of LLM training. An AI is **aligned** if it is helpful, honest, and harmless (Askell et al., 2020).

Supervised instruction fine-tuning is not enough because:

- Annotators don't always *write* what they would *prefer* as LM output.
- It is easier to collect **ratings** of outputs, or **preferences** between outputs.
- SFT does not control output length and style well enough.

### Optimizing for human preferences

#### Definitions

> **Reward $R(s)$**: A human-assigned score for an LM output sample $s$; higher is better.

Example — summarizing a news article about a magnitude 4.2 earthquake in San Francisco:

| Summary | Reward |
|---|---|
| $s_1$: "An earthquake hit San Francisco. There was minor property damage, but no injuries." | $R(s_1) = 8.0$ |
| $s_2$: "The Bay Area has good weather but is prone to earthquakes and wildfires." | $R(s_2) = 1.2$ |

The goal is to train the LM to produce outputs with high reward.

### RLHF pipeline

#### Definitions

> **Reinforcement learning from human feedback (RLHF)**: Training an LM (the **policy**) with RL to maximize a reward model trained on human preferences.

> **Policy**: The LLM being optimized, viewed as a distribution over responses given a prompt.

1. **Supervised fine-tuning**: collect instruction/response data and train a supervised policy.
2. **Reward model**: collect human preference data that ranks or scores several responses to each instruction, and train a reward model to emulate those judgements.
3. **RL optimization**: repeatedly
   1. generate responses with the current policy,
   2. score them with the reward model,
   3. update the policy with RL.

![RLHF pipeline](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/07_Preference_Alignment_And_Reasoning/rlhf-pipeline.svg)

*Step 1 fine-tunes on labeller-written answers; step 2 trains a reward model on ranked outputs; step 3 repeatedly samples, scores, and updates the policy with PPO.*

In InstructGPT (Ouyang et al., 2022): a prompt and several model outputs are sampled, a labeller ranks them best to worst, and this trains the reward model. Then a new prompt is sampled, the policy generates an output, the reward model scores it, and the reward updates the policy using PPO.

### Reward modelling

Keeping a human in the loop for every sample is expensive. Instead, model human preferences as a separate problem:

- Train a **reward model** LM $RM_\phi$ to predict human preferences from an annotated dataset.
- Use RL to optimize the policy against the reward model.
- **Pairwise comparisons** are more reliable than direct ratings.

Pairwise (Bradley-Terry) loss, where $s^w$ is the "winning" (preferred) sample and $s^l$ the "losing" one:

$$
J_{RM}(\phi) = -\mathbb{E}_{(s^w, s^l) \sim D}\Big[\log \sigma\big(RM_\phi(s^w) - RM_\phi(s^l)\big)\Big]
$$

The loss pushes $s^w$ to score higher than $s^l$. Check that the reward model's predictions are accurate enough before using it.

![Reward model training](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/07_Preference_Alignment_And_Reasoning/reward-model.svg)

*The reward model scores a preferred and a dispreferred summary; the pairwise loss pushes $RM(s^w)$ above $RM(s^l)$.*

### Imitation versus optimization

| | Supervised fine-tuning | RLHF |
|---|---|---|
| Goal | **Imitation**: fit $\hat{p}(y \mid x) \approx p^*(y \mid x)$ for a reference distribution $p^*$ | **Optimization**: find $\hat{p}(y \mid x)$ maximizing $\mathbb{E}_{\hat{p}}[R(y, x)]$ |
| Needs | Samples from the reference policy | A reward function we can measure |
| View of LM | Generative model | A **policy**, not a mode of some distribution |

The expected reward is **non-differentiable** with respect to the sampled text, so RL is needed.

### Policy gradient and PPO

#### Definitions

> **REINFORCE (policy gradient)**: Estimating the gradient of expected reward with the log-derivative trick and Monte Carlo samples.

> **Proximal policy optimization (PPO)**: A policy-gradient algorithm that clips the probability ratio between new and old policies to keep updates small and stable.

REINFORCE update with $m$ samples:

$$
\theta_{t+1} = \theta_t + \alpha \frac{1}{m}\sum_{i=1}^{m} R(s_i)\,\nabla_{\theta_t} \log p_{\theta_t}(s_i)
$$

REINFORCE's variance is too high, so RLHF uses PPO, which optimizes:

$$
L(s, a, \theta_k, \theta) = \min\!\left(\frac{\pi_\theta(a \mid s)}{\pi_{\theta_k}(a \mid s)} A^{\pi_{\theta_k}}(s, a),\;\; \text{clip}\!\left(\frac{\pi_\theta(a \mid s)}{\pi_{\theta_k}(a \mid s)}, 1 - \epsilon, 1 + \epsilon\right) A^{\pi_{\theta_k}}(s, a)\right)
$$

- $\pi_\theta / \pi_{\theta_k}$ is the probability ratio between the new and old policy.
- $A^{\pi_{\theta_k}}(s, a)$ is the **advantage**: how much better action $a$ is than average in state $s$.
- Clipping to $[1 - \epsilon, 1 + \epsilon]$ stops the policy changing too much in one update.

![PPO clipped objective](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/07_Preference_Alignment_And_Reasoning/ppo-clip.svg)

*For $A > 0$ the objective stops rising once the ratio passes $1 + \epsilon$; for $A < 0$ it stops falling below $1 - \epsilon$, so large policy moves earn nothing extra.*

### KL penalty and the full RLHF system

Optimizing purely for reward can produce nonsensical text that exploits the reward model. The full reward subtracts a **KL divergence** term to stay close to the pretrained model:

$$
R(s) = RM_\phi(s) - \beta \log\!\left(\frac{p_\theta^{RL}(s)}{p^{PT}(s)}\right)
$$

$\beta$ controls how strongly the policy is pulled back towards the pretrained (reference) model $p^{PT}$.

![RL fine-tuning with a KL penalty](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/07_Preference_Alignment_And_Reasoning/rlhf-kl.svg)

*The frozen initial LM and the RL policy both answer the prompt; the reward model scores the policy's answer, a KL penalty compares the two, and PPO updates the policy.*

The full PPO-based system combines:

| Component | Role |
|---|---|
| SFT model $\pi^{SFT}$ | Reference for the KL penalty |
| Reward model $r(x, y)$ | Scores responses |
| Value model $V_\phi(s_t)$ | Estimates expected return, for the advantage (trained with MSE loss) |
| GAE (generalized advantage estimation) | Computes advantages from TD errors $\delta_t = r(s_t, a_t) + \gamma V(s_{t+1}) - V(s_t)$ |
| Policy LM $\pi^{RL}_\theta$ | Trained with the PPO-clip loss, optionally plus an LM loss on pretraining data |
| Experience buffer | Stores sampled trajectories from the old policy |

**Stylistic effect.** For "What are the five most common causes of stress?", an SFT-only model (Alpaca, 10k examples) gives one short sentence. After PPO it gives a longer, structured numbered list with explanations.

### Direct preference optimization (DPO)

#### Definitions

> **Direct preference optimization (DPO)**: Learning directly from preference pairs, without a separate reward model or RL, by increasing the log-likelihood of preferred responses and decreasing it (weighted) for dispreferred ones.

The RLHF goal is:

$$
\max_{\pi_\theta} \mathbb{E}_{x \sim \mathcal{D},\, y \sim \pi_\theta(y \mid x)}\big[r_\phi(x, y)\big] - \beta\,\mathbb{D}_{\text{KL}}\big[\pi_\theta(y \mid x) \,\|\, \pi_{\text{ref}}(y \mid x)\big]
$$

Its optimal policy implies a reward:

$$
r(x, y) = \beta \log \frac{\pi_r(y \mid x)}{\pi_{\text{ref}}(y \mid x)} + \beta \log Z(x)
$$

Substituting into the pairwise preference loss ($Z(x)$ cancels) gives the DPO objective:

$$
\mathcal{L}_{\text{DPO}}(\pi_\theta; \pi_{\text{ref}}) = -\mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}}\left[\log \sigma\!\left(\beta \log \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} - \beta \log \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)}\right)\right]
$$

The gradient, with implied reward $\hat{r}_\theta(x, y) = \beta \log \frac{\pi_\theta(y \mid x)}{\pi_{\text{ref}}(y \mid x)}$:

$$
\nabla_\theta \mathcal{L}_{\text{DPO}} = -\beta\,\mathbb{E}\Big[\underbrace{\sigma\big(\hat{r}_\theta(x, y_l) - \hat{r}_\theta(x, y_w)\big)}_{\text{higher weight when reward estimate is wrong}}\big(\underbrace{\nabla_\theta \log \pi(y_w \mid x)}_{\text{increase likelihood of } y_w} - \underbrace{\nabla_\theta \log \pi(y_l \mid x)}_{\text{decrease likelihood of } y_l}\big)\Big]
$$

The update scales the difference between the winning and losing gradients by the "prediction error" of the implied reward model.

| | RLHF (PPO) | DPO |
|---|---|---|
| Reward model | Separately trained | Implicit in the policy |
| Optimization | RL, sampling during training | Supervised-style loss on fixed preference pairs |
| Complexity | Several models, unstable RL | Simpler |

![RLHF versus DPO](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/07_Preference_Alignment_And_Reasoning/rlhf-vs-dpo.svg)

*RLHF trains a reward model and runs RL with sampling; DPO turns the same preference pairs directly into a supervised-style loss on the policy.*

### Limitations of RLHF

- Chatbots are rewarded for responses that **seem** authoritative and helpful, regardless of truth. This can cause made-up facts and hallucinations.
- Human preferences are unreliable; models of human preferences even more so.
- Optimizing for reward can **overfit** (reward hacking).
- Over time, RLHF has been shown to make the underlying model worse.
- Whose values are being modelled?

### Reasoning with rationales

#### Definitions

> **Text rationale**: A natural-language explanation of a model's behaviour or prediction.

- LMs often work better when rationales are included.
- Rationales can guide the model to reason its way to a solution.

| Example | Rationale |
|---|---|
| **E-SNLI**: Premise "An adult dressed in black holds a stick." Hypothesis "An adult is walking away, empty-handed." Label: contradiction | "Holds a stick implies using hands so it is not empty-handed." |
| **Math word problem**: two cards drawn from 52; probability both are kings? | $n(S) = \binom{52}{2} = 1326$, $n(E) = \binom{4}{2} = 6$, $P(E) = 6/1326 = 1/221$; answer C |

### Chain-of-thought prompting

#### Definitions

> **Chain-of-thought (CoT) prompting**: Few-shot prompting where in-context examples include explanations, so the model "talks through" its reasoning before giving the answer.

> **Zero-shot chain-of-thought**: Adding "Let's think step by step" to the prompt with no examples.

CoT uses natural language as a scaffold for "reasoning":

| Domain | How CoT helps |
|---|---|
| Math | LLMs can do single arithmetic steps reasonably well; CoT chains them into multi-step solutions |
| QA | Decomposes questions, e.g. "capital of the country where Aristotle lived" → find country, then ask its capital |
| Other tasks | Captures the behaviour written in rationales |

**Few-shot CoT** (Wei et al., 2022). The prompt example says "Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11." For the new question about 10 dogs at 0.5 hours a day, the model outputs "10 × .5 = 5 hours a day. 5 × 7 = 35 hours a week. The answer is 35 hours a week."

**Zero-shot CoT.** "A juggler can juggle 16 balls. Half are golf balls, and half of the golf balls are blue. How many blue golf balls? A: Let's think step by step." → "16 balls... 8 golf balls... 4 blue golf balls."

### Reinforcement learning from verifiable rewards (RLVR)

#### Definitions

> **RLVR**: RL where rewards come from an automatic **verifier** (e.g. checking a maths answer) rather than human feedback.

> **Group relative policy optimization (GRPO)**: An RL algorithm that samples a group of solutions per problem and scores each relative to the group, rather than using a learned value model.

RLHF can train a chat model but does not produce the capabilities of recent models. RLVR is the main way to improve further.

- Through RL, the model learns to generate **long outputs with multiple "reasoning" steps** that help it reach the correct final answer.
- Standard RL at first did not succeed. **GRPO** proved more suitable, especially for scaling to longer sequences.

![RLVR with GRPO](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/07_Preference_Alignment_And_Reasoning/rlvr-grpo.svg)

*For each problem, a group of solutions is sampled and checked by a verifier; group-relative rewards push the policy towards above-average solutions.*

In GRPO's standard form, the advantage of solution $i$ in a group with rewards $r_1, \dots, r_G$ is its reward normalized within the group:

$$
\hat{A}_i = \frac{r_i - \text{mean}(r_1, \dots, r_G)}{\text{std}(r_1, \dots, r_G)}
$$

![R1-Zero response length](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/07_Preference_Alignment_And_Reasoning/r1-length.svg)

*During DeepSeek-R1-Zero RL training, average response length rises steadily (with fluctuations): the model learns to "think" longer.*

### Test-time scaling

#### Definitions

> **Test-time scaling**: Improving performance by letting the model generate more reasoning ("thinking") tokens at inference time.

The longer the model "thinks" during inference, the more performance improves.

![Test-time scaling](../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/07_Preference_Alignment_And_Reasoning/test-time-scaling.svg)

*For Qwen3-235B-A22B, thinking-mode scores climb as the thinking budget grows from 1K to 32K tokens, while non-thinking mode (dashed) stays flat.*

---

# Part III: Vision-Language Models

## 1. Introduction and Vision Transformers

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Vision-Language Models  
> **Source**: [Lecture1_Vision_Transformers.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/VLM%27s/Lecture1_Vision_Transformers.pdf), Prof Patrick Marais, slides 1-30 (primary papers: Dosovitskiy et al. 2020; Touvron et al. 2021)  
> **Generated**: 2026-10-29  

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

![Text versus image pipeline](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/text-vs-image-pipeline.svg)

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

![Patchify and raster order](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/patchify.svg)

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

![Patch embedding](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/patch-embedding.svg)

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

![Vision Transformer architecture](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/vit-architecture.svg)

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

![Bag of patches](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/bag-of-patches.svg)

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

![Position embedding similarity](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/position-similarity.svg)

*Each small square shows one position embedding's similarity to all 49: brightest at its own location, high along its row and column, and fading with distance (schematic).*

The model infers grid geometry from image statistics. Hand-designed 2D encodings gain almost nothing, so the simple 1D embedding is used.

### Changing resolution by interpolation

$E_{\text{pos}}$ has exactly $N$ rows. A larger image gives more patches with no embeddings — the same issue text has with longer sequences.

1. Reshape the learned embeddings into their spatial grid (excluding `[CLS]`), e.g. $7 \times 7 \times D$.
2. Treat them as samples of a smooth 2D function and **bicubically interpolate** to the new grid, e.g. $10 \times 10 \times D$.
3. Flatten back to a sequence and restore `[CLS]`.

![Position embedding interpolation](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/position-interpolation.svg)

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

![ViT versus CNN data scale](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/data-scale.svg)

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

![Residual block](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/residual-block.svg)

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

![Mean attention distance](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/attention-distance.svg)

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

![DeiT distillation](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/01_Vision_Transformers/deit-distillation.svg)

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

## 2. Contrastive Vision-Language Pretraining: CLIP and Related Models

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Vision-Language Models  
> **Source**: [Lecture2_CLIP_Contrastive_Pretraining.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/VLM%27s/Lecture2_CLIP_Contrastive_Pretraining.pdf), Prof Patrick Marais, slides 1-27 (primary papers: Radford et al. 2021; Jia et al. 2021; Zhai et al. 2023)  
> **Generated**: 2026-10-29  

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

![CLIP dual encoder](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/02_CLIP_And_Contrastive_Pretraining/dual-encoder.svg)

*Images and captions are encoded separately, projected, and L2-normalized into one 512-d space where cosine similarity measures semantic match.*

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

![Alignment before and after](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/02_CLIP_And_Contrastive_Pretraining/alignment-before-after.svg)

*Before training, image and text embeddings are unrelated; after contrastive training each image sits next to its own caption.*

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

![Similarity matrix](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/02_CLIP_And_Contrastive_Pretraining/similarity-matrix.svg)

*The six-pair batch from the lecture: matched pairs on the diagonal score 0.84-0.93, while mismatches stay low.*

- Row $i$ scores image $i$ against every caption.
- Column $j$ scores caption $j$ against every image.
- Objective: **maximize the diagonal, minimize everything else**.

The matrix is **not symmetric**, and rows and columns answer different questions:

| Direction | Question |
|---|---|
| Image → text (row) | Out of all these descriptions, which fits this image best? |
| Text → image (column) | Out of all these images, which best represents this caption? |

Associations are one-to-many (many captions could fit an image and vice versa), so the loss must handle **both** query directions.

![Row and column softmaxes](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/02_CLIP_And_Contrastive_Pretraining/row-column-softmax.svg)

*Image→text is a softmax over each row; text→image is a softmax over each column. Both target the diagonal.*

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

![Contrastive temperature](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/02_CLIP_And_Contrastive_Pretraining/contrastive-temperature.svg)

*With the same similarities, $\tau = 1$ gives the match 0.26, $\tau = 0.3$ gives 0.57, and $\tau = 0.07$ puts almost all probability on it.*

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

![Caption prediction versus contrastive](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/02_CLIP_And_Contrastive_Pretraining/caption-vs-contrastive.svg)

*Predicting a bag of words is 3× more efficient than generating exact captions, and contrastive matching a further 4× (≈12× overall).*

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

![Zero-shot classification](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/02_CLIP_And_Contrastive_Pretraining/zero-shot.svg)

*Class names fill a prompt template, the text encoder caches one vector per class, and the image is assigned to the closest one.*

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

![Robustness under distribution shift](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/02_CLIP_And_Contrastive_Pretraining/robustness.svg)

*Both models score 76% on ImageNet, but the supervised ResNet-101 collapses on shifted test sets (down to 2% on ImageNet-A) while zero-shot CLIP stays high.*

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

![CLIP versus SigLIP](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/02_CLIP_And_Contrastive_Pretraining/clip-vs-siglip.svg)

*CLIP normalizes each row and column with a softmax over the whole batch; SigLIP scores every cell independently as matched (+1) or not (−1).*

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

## 3. Bridging Vision and Language: Fusion Architectures

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Vision-Language Models  
> **Source**: [Lecture3_Fusion_Architectures.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/VLM%27s/Lecture3_Fusion_Architectures.pdf), Prof Patrick Marais, slides 1-31 (primary papers: Alayrac et al. 2022; Li et al. 2023; Liu et al. 2023)  
> **Generated**: 2026-10-29  

### What is missing: the bridge

| Side | Strength | Missing |
|---|---|---|
| Image (CLIP) | Matches text to images | Cannot say anything fine-grained; one 512-d vector per image; can only rank candidate sentences you supply. "What is unusual about this image?" has no candidate list — it needs open-ended generation |
| Text (LLM) | Generates, reasons, follows instructions | No access to image understanding |

We have a vision encoder and an LLM, both expensive, pretrained, and frozen. How can the LLM condition its text generation on pixels?

#### Definitions

> **Bridge (connector / adapter)**: A component that maps visual embeddings into a representation resembling a text-embedding sequence that the LLM can parse and reason about.

![The bridge problem](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/bridge-problem.svg)

*A frozen vision encoder and a frozen LLM need a bridge that turns patch features into tokens the LLM can read.*

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

![Where vision enters](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/where-vision-enters.svg)

*Concatenation puts projected image tokens in the LLM sequence; cross-attention keeps them outside and adds layers where text attends to them.*

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

![Tokens per image](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/token-budget.svg)

*Raw ViT-L/14@336 gives 576 tokens per image (LLaVA keeps them all); Flamingo's resampler gives 64 and BLIP-2's Q-Former 32.*

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

![Flamingo architecture](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/flamingo.svg)

*Each image goes through a frozen encoder and a trainable Perceiver Resampler; gated cross-attention layers inserted between frozen LM blocks let the interleaved text attend to them.*

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

![Perceiver Resampler](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/perceiver-resampler.svg)

*64 learned latent queries cross-attend to any number of visual features and always return 64 visual tokens.*

The idea of learned queries compressing a modality reappears in BLIP-2's Q-Former and in video models.

### Gated cross-attention

#### Definitions

> **Gated cross-attention (`tanh` gate)**: A residual update scaled by $\tanh(\alpha)$, where $\alpha$ is a learned scalar initialized to $0$.

$$
z \leftarrow z + \tanh(\alpha) \cdot \text{XAttn}(\text{text}, \text{vision}), \qquad z \leftarrow z + \tanh(\alpha) \cdot \text{FFW}(z), \qquad \alpha_{\text{init}} = 0
$$

At initialization $\tanh(0) = 0$, so the new layers are invisible and the network is **exactly the original frozen LM**. Training opens each gate only as fast as it proves useful; different layers open differently.

![Tanh gate](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/tanh-gate.svg)

*$\tanh(\alpha)$ is zero at initialization, so the added layers start invisible and open only as training finds them useful.*

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

![BLIP-2 pipeline](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/blip2.svg)

*A frozen EVA-CLIP ViT feeds a trained 188M Q-Former whose 32 output tokens are linearly projected into a frozen LLM.*

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

![Q-Former objectives](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/qformer-objectives.svg)

*Queries cross-attend to the image and share self-attention with text; three attention masks give the ITC, ITM, and ITG losses.*

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

![LLaVA](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/llava.svg)

*LLaVA keeps all 576 CLIP patch tokens, maps them with a simple projection, and feeds them to Vicuna as ordinary sequence tokens.*

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

![LLaVA two-stage training](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/llava-stages.svg)

*Stage 1 trains only the projection on 595K pairs; stage 2 trains the projection and the whole LLM on 158K GPT-4 instructions.*

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

![Early fusion](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/03_Vision_Language_Fusion_Architectures/early-fusion.svg)

*Native multimodal models interleave image and text tokens in one stream for a single Transformer trained from scratch.*

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

## 4. VLMs for Image Understanding in Practice

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Vision-Language Models  
> **Source**: [Lecture4_VLMs_in_Practice.pptx](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/VLM%27s/Lecture4_VLMs_in_Practice.pptx), Prof Patrick Marais, slides 1-27 (primary reports: Qwen2.5-VL, Bai et al. 2025; InternVL3, Zhu et al. 2025; POPE, Li et al. 2023)  
> **Generated**: 2026-10-29  

### Components of production VLMs

#### Definitions

> **Merger / projector**: The small MLP connecting the vision tower to the LLM — the "bridge" of lecture 3, under the name used in VLM papers.

> **M-RoPE (multimodal RoPE)**: Rotary position encoding factorized over (time, height, width), used in the LLM decoder so every token has a spatial-temporal position.

![Production VLM stack](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/04_VLMs_In_Practice/production-stack.svg)

*A native-resolution ViT tower, a merger that combines $2 \times 2$ patches, and an LLM decoder with M-RoPE that outputs text, boxes, or JSON.*

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

![VLM training stages](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/04_VLMs_In_Practice/training-stages.svg)

*Multimodal pretraining, visual SFT, then preference tuning: the LLM pipeline with visual data at every stage.*

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

![Grounding as text](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/04_VLMs_In_Practice/grounding-json.svg)

*The model answers a grounding request with JSON whose bounding boxes are ordinary number tokens.*

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

![Fixed versus native resolution](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/04_VLMs_In_Practice/fixed-vs-native.svg)

*Fixed resizing squashes a receipt until its text is unreadable; native resolution gives each image a token grid shaped to its aspect ratio.*

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

![GUI agent loop](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/04_VLMs_In_Practice/gui-loop.svg)

*Screenshot → decide and ground an action → execute → new screenshot.*

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

![POPE](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/04_VLMs_In_Practice/pope.svg)

*Accuracy drops from random to popular to adversarial absent objects; a balanced or preference-tuned model drops less (schematic).*

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

## 5. Video Understanding

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Vision-Language Models  
> **Source**: [Lecture5_Video_Understanding.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/VLM%27s/Lecture5_Video_Understanding.pdf), Prof Patrick Marais, slides 1-23 (primary papers: ViViT, Arnab et al. 2021; TimeSformer; Qwen2-VL; Video-MME)  
> **Generated**: 2026-10-29  

### From image to video

The image VLM flow is: ViT tokenizes an image → CLIP aligns it with text → a projector feeds an LLM → production VLM answers. A video is "just a sequence of images", so what changes?

| Change | Detail |
|---|---|
| **Scale** | 1 minute at 24 fps = 1,440 frames. Naively $1{,}440 \times 576 \approx 830{,}000$ tokens per minute — impossible with quadratic attention |
| **Time** | Motion, causality, order, before/after — not visible in any single frame |
| **New questions** | "What happened just before the crash?" · "Did she pick up the cup or put it down?" · "When does the goal happen?" |

A practical design must **shrink the token stream**.

![Video token explosion](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/05_Video_Understanding/token-explosion.svg)

*One minute at 24 fps is 1,440 frames; at 576 tokens each that is about 830,000 tokens.*

### Which frames to sample

The common first step is **frame down-sampling**.

| Strategy | How | Trade-off |
|---|---|---|
| Uniform | Every $k$-th frame | Simple and standard, but ignores content: fast events between samples vanish; static scenes waste tokens |
| FPS-based | Fixed frames per second | Token count scales with duration |
| Scene-change / keyframe | Pick frames where content changes | Adapts to content |
| Query-aware | Pick frames relevant to the question | Needs the question up front |

![Uniform frame sampling](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/05_Video_Understanding/frame-sampling.svg)

*Keeping every 6th frame is cheap, but a fast event that falls between samples is lost.*

### Frame tokens versus tubelet tokens

#### Definitions

> **Frame tokens**: Patchify each sampled frame independently (as for a single image) and concatenate the frames' tokens in order.

> **Tubelet**: A token spanning a $P \times P$ patch across $\tau$ consecutive frames, embedded with a 3D convolution / linear projection over $t \times h \times w$.

| | Frame tokens | Tubelet tokens |
|---|---|---|
| Time information | Only in sequence order + position encoding (a time/frame embedding is added to each patch's position) | Short-term motion is inside each token |
| Token count | Higher | Fewer for the same clip |
| Used by | Most video-LLMs | ViViT, VideoMAE |

![Frame versus tubelet tokens](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/05_Video_Understanding/frame-vs-tubelet.svg)

*Frame tokens patchify each frame separately; a tubelet token spans the same patch across several frames, so it carries motion.*

### Telling the model when each token is

Self-attention is permutation-invariant, so position must be injected — now on three axes: height, width, and time.

#### Definitions

> **M-RoPE (Multimodal RoPE)**: Rotary position encoding factorized over $(t, h, w)$, introduced in Qwen2-VL.

> **Absolute timestamps**: Injecting each frame's real time (seconds) so "when" questions can be answered in real units.

How M-RoPE works:

1. **2D RoPE** splits the token embedding in half, applying 1D RoPE by $x$ to one half and by $y$ to the other.
2. **M-RoPE** splits the embedding three ways — $x$, $y$, $t$ — and rotates each part by its own coordinate.
3. Tokens close in space get similar positional encodings, and so do tokens close in time.
4. One scheme handles 1D, 2D, and 2D+T: text tokens have $h = w = 0$ with only $t$ changing; image tokens have $h, w$ with $t = 0$.

Why temporal position matters more than for images:

- For a static image, slightly inaccurate patch positions degrade understanding.
- For video, confusing frame order **destroys causality** ("picked up" vs "put down").

$$
\text{video token} = \text{embed}(\text{patch/tubelet content}) + \text{embed}(\text{where: } h, w;\ \text{when: } t)
$$

![M-RoPE axes](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/05_Video_Understanding/mrope-axes.svg)

*M-RoPE splits each embedding into $t$, $h$, and $w$ parts: text varies only in $t$, image patches in $h$ and $w$, and video patches in all three.*

The Transformer core is still completely unchanged.

### Why video breaks quadratic attention

For video, sequence length $n = T \cdot S$, with $T$ sampled frames and $S$ tokens per frame (e.g. 256-576). Attention costs $O(n^2) = O((T S)^2)$.

- 32 frames × 256 tokens = 8,192 tokens → $8{,}192^2 \approx 67$ million attention scores per head per layer.
- Doubling the frames → $4\times$ the cost.

Three mitigations:

| Approach | Idea |
|---|---|
| Factorize attention | Never attend over all $T \cdot S$ tokens at once |
| Pool / resample | Shrink $S$ or $T$ with a fixed or learned reducer (Perceiver-style) |
| Sparsify | Attend to a subset (windows, keyframes); useful for long video |

### Fix 1: factorized space-time attention

#### Definitions

> **Factorized space-time attention**: Replacing one attention over all $T \cdot S$ tokens with a temporal attention (each spatial position attends across frames) followed by a spatial attention (tokens attend within their own frame).

1. **Temporal attention**: each patch attends only to the same spatial location in other frames; everything else is masked.
2. **Spatial attention**: take those time-aware tokens and attend across all patches within each frame; other frames are masked.
3. Implement both with tensor reshaping so standard Transformer attention blocks can be reused.

$$
O\big((T \cdot S)^2\big) \;\longrightarrow\; O\big(T^2 \cdot S + T \cdot S^2\big)
$$

![Factorized attention](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/05_Video_Understanding/factorized-attention.svg)

*Joint attention links a token to every frame and position; spatial attention only within its frame; temporal attention only at its location across frames.*

**Trade-off**: factorization can miss correlations that are jointly spatial and temporal, but it is usually worth it (ViViT, TimeSformer).

### Fix 2: pooling and resampling

Many production video-VLMs reduce the token count before the LLM sees it.

| Method | Reduces | How |
|---|---|---|
| Spatial pooling | $S$ | Reshape ViT tokens to a grid (196 → $14 \times 14$), average $2 \times 2$ blocks → $7 \times 7$ (25% of the tokens) |
| Temporal pooling | $T$ | Average the corresponding token across nearby frames (e.g. sets of 4 consecutive frames) |
| Learned resampling | Whole clip | A Perceiver Resampler / Q-Former maps a clip to a fixed number of tokens regardless of length — learned queries as a bottleneck over space-time. Flamingo's resampler was designed for this: many frames in, 64 tokens out |

![Spatial and temporal pooling](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/05_Video_Understanding/pooling.svg)

*Averaging $2 \times 2$ patches cuts tokens per frame to 25%; averaging across 4 frames cuts the frame count; a resampler maps a clip to a fixed number of tokens.*

> [!warning] <span style="color: #ff939b">Compression loses detail</span>
> Every pool or resample step throws away temporal or spatial detail. Pool too much and you can no longer tell "picked up" from "put down". Video-VLMs differ mostly in **how they compress**, not in the Transformer core.

### Video foundation models versus video-LLMs

| | Video foundation models | Video-LLMs / VLMs (image VLM + time) |
|---|---|---|
| Examples | ViViT, TimeSformer, VideoMAE, VideoMamba | Video-ChatGPT, Video-LLaVA, VideoLLaMA, Qwen2.5-VL, InternVL (video mode) |
| Goal | Strong video representations (classification, retrieval, action recognition) | Open-ended video chat, QA, captioning, grounding |
| Time handling | Tubelets + factorized attention, trained end-to-end | Sample frames → per-frame ViT → compress → LLM reasons over time |
| Relation to images | Extends ViT into 3D | Extends align, bridge, instruction-tune with a temporal front-end |

### The context wall

- Even at 1 fps and only 256 tokens per frame, a 1-hour video needs about **920k tokens** — beyond most context windows.
- But 1 fps already loses most motion; real understanding needs **more** frames, not fewer.

So long-video understanding is fundamentally a **compression and retrieval** problem.

![The context wall](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/05_Video_Understanding/context-wall.svg)

*At 1 fps and 256 tokens per frame, token counts cross a 128k context within minutes and reach about 920k for an hour.*

### Scaling to long video

| Strategy | Idea | Cost / limitation |
|---|---|---|
| Keyframe selection | Score frames for relevance (to the query or by scene change) and keep the informative ones | A bad selector discards the answer; query-aware selection needs the question first |
| Memory / hierarchical | Summarize chunks into compact memory tokens; reason over summaries ("read the video like chapters") | Lossy; errors compound across chunks |
| Streaming / online | Process video as it arrives with a running state | No global lookback unless stored; "earlier" questions are harder |
| Other modalities | Fuse audio and subtitles, which carry much information at almost no visual-token cost | Not always present or accurate; can leak answers in evaluation |

None of these is solved. Watching a 2-hour film and answering a question about minute 12 is still an open problem.

### The cheapest information is not visual

In lectures, news, and tutorials, most meaning is in the **speech**, not the pixels.

#### Definitions

> **ASR (automatic speech recognition)**: Converting speech audio into a text transcript.

- Subtitles / ASR transcripts are already text: almost free for the LLM and slot straight into the sequence.
- Audio events (doorbell, crash, applause) disambiguate visually ambiguous scenes.
- Design pattern: interleave frame tokens with transcript text on the same timeline, aligned by timestamps.

This reframes many video benchmarks: a model can score well by reading subtitles and barely watching. Production "video understanding" is usually **multimodal** (vision + audio + text); vision-only understanding is much harder.

### Taxonomy of video tasks

| Task | Question form | Temporal reasoning needed |
|---|---|---|
| Action recognition | "What action is this?" (classification) | Low-medium; a few frames often suffice |
| Video captioning | "Describe what happens." | Medium; must order events and describe change |
| Video QA | "Why did X do Y?" "What happened after Z?" | Medium-high; causal, before/after, counting over time |
| Temporal grounding | "When does event E occur?" → time span | High; must localize in time |
| Dense video captioning | Caption every event with its timestamp | High; detect, localize, and describe jointly |

A model can be good at a low-temporal task and weak at a demanding one, which is why benchmarks separate them.

### Temporal grounding

#### Definitions

> **Temporal grounding**: Answering "when in the video?" with a time span — the temporal analogue of spatial grounding's "where in the image?" → box.

![Temporal grounding](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/05_Video_Understanding/temporal-grounding.svg)

*For "when does the player score the goal?", the model outputs the span 0:47–0:59 as text.*

- The output is just tokens: the model emits timestamps as text, enabled by absolute-time positions.
- It is hard because "when" cannot be answered from one frame or a global summary. The model must align language to the timeline and inspect frames at fine granularity.

### Is the model using time at all?

| Shortcut | Problem | Diagnostic |
|---|---|---|
| **Single-frame bias** | Many "video" questions are answerable from one good frame ("What sport is this?"); a model ignoring motion can top the leaderboard | Feed a single frame or shuffle frame order; if the score barely drops, the benchmark is not testing time |
| **Subtitle/audio shortcut** | With transcripts, a model can read rather than watch | Evaluate with and without subtitles / with audio muted |

How benchmarks counter this:

- **Video-MME** covers short to long clips and reports results with and without subtitles.
- **TempCompass** and similar suites build questions a single frame or shuffled order cannot answer.

When a video model "wins", ask: would it still win on one frame, on shuffled frames, or with audio muted?

### Common video benchmarks

| Benchmark | Probes | Why it exists |
|---|---|---|
| MSR-VTT / ActivityNet-QA | Open-ended captioning and QA | Classic general-purpose video QA |
| NExT-QA | Causal and temporal QA ("why", "before/after") | Forces reasoning beyond recognition |
| Charades-STA / ActivityNet-Captions | Temporal grounding and dense captioning | Localize events in time |
| Video-MME | Short/medium/long, with and without subtitles | Exposes the subtitle shortcut; tests length |
| TempCompass / Vinoground | Temporal-only skills; frame-order sensitivity | Built so single/shuffled frames fail |
| EgoSchema / LongVideoBench | Long-form understanding (minutes+) | Tests the long-video context wall |

Choose benchmarks that reflect your application's priorities.

## 6. Generative Foundations: VAEs, GANs, and Diffusion

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Vision-Language Models  
> **Source**: [Lecture6_Generative_Foundations.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/VLM%27s/Lecture6_Generative_Foundations.pdf), Prof Patrick Marais, slides 1-25 (primary papers: Kingma and Welling 2014; Goodfellow et al. 2014; Ho et al. 2020)  
> **Generated**: 2026-10-29  

### From understanding to generating

Everything so far was **understanding**: image/video in → text out (describe, answer, ground, locate). Now the direction flips: something in → a **new image** out.

#### Definitions

> **Generation**: Producing new samples that look as if they came from the training distribution, rather than copying training images (which is memorization).

Example: train on 10,000 face photos and produce a realistic face of someone who never existed.

The core question: how do you learn the "look" (distribution) of a whole category of images well enough to synthesize convincing new members?

The lecture has three parts: autoencoders → VAEs (make the latent space sampleable); GANs (learn to generate by competition); diffusion (add noise, then learn to remove it).

### Recap: the autoencoder

#### Definitions

> **Autoencoder (AE)**: An encoder that maps input $x$ to a small latent code $z$, and a decoder that maps $z$ back to a reconstruction $\hat{x} \approx x$.

> **Bottleneck**: The small latent code, which forces the network to keep only what matters.

![Autoencoder](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/autoencoder.svg)

*An image is compressed to a small latent code $z$ and decoded back to $\hat{x} \approx x$.*

The AE is self-supervised. Its loss is reconstruction error, e.g. mean-squared error:

$$
\mathcal{L}_{\text{AE}} = \|x - \hat{x}\|^2
$$

### Why a plain autoencoder cannot generate

In theory, pick a random $z$ and decode it. In practice this **fails**:

- The AE only learned to decode the specific codes its training images mapped to.
- The space between and around those codes was never trained. If $(1, 1)$ and $(10, 10)$ are encoded training examples, what does $(5, 5)$ decode to?
- So a random $z$ usually decodes to noise or garbage.

![Latent gaps](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/latent-gaps.svg)

*Plain autoencoder codes are scattered with gaps, so a random code decodes to garbage; VAE codes fill a region around $\mathcal{N}(0, I)$ that is safe to sample.*

### Variational autoencoders

#### Definitions

> **Variational autoencoder (VAE)**: An autoencoder whose encoder outputs a probability distribution over codes rather than a single code, regularized towards a fixed prior so the latent space can be sampled (Kingma and Welling, 2014).

> **Approximate posterior $q(z \mid x)$**: The encoder's Gaussian $\mathcal{N}(\mu(x), \sigma(x)^2 I)$ — given this image, where could its code plausibly lie?

> **Prior $p(z)$**: The fixed target distribution $\mathcal{N}(0, I)$ shared by every image.

1. For each image $x$, the encoder predicts a mean $\mu(x)$ and standard deviation $\sigma(x)$, defining $q(z \mid x) = \mathcal{N}(\mu, \sigma^2 I)$.
2. During training, sample $z \sim q(z \mid x)$ and decode it. The decoder must handle a **region** of latent space, not an isolated point.
3. Pull every posterior towards the same prior $p(z) = \mathcal{N}(0, I)$. The posteriors then overlap and together cover the region sampled later. Without this pull, the encoder could place posteriors anywhere and the gaps return.

![Variational autoencoder](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/vae.svg)

*The encoder outputs $\mu$ and $\sigma$ defining $q(z \mid x)$; a sample is decoded; the KL term pulls $q$ towards the prior.*

**Generation** is cheap: keep only the decoder, draw $z \sim \mathcal{N}(0, I)$, and decode it into a new image.

### The reparameterization trick

**Problem**: training needs $\partial \mathcal{L}/\partial \mu$ and $\partial \mathcal{L}/\partial \sigma$, but "draw a random sample" is not differentiable. With sampling inside the network, no gradient reaches the encoder.

**Fix**: sample parameter-free noise and build $z$ from it.

$$
\epsilon \sim \mathcal{N}(0, I), \qquad z = \mu + \sigma \odot \epsilon
$$

The distribution of $z$ is unchanged, but $z$ is now a differentiable function of $\mu$ and $\sigma$, so gradients flow to the encoder. This makes the VAE trainable end-to-end.

![Reparameterization trick](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/reparameterization.svg)

*Sampling inside the network blocks gradients; drawing $\epsilon$ from outside and setting $z = \mu + \sigma \odot \epsilon$ lets gradients reach the encoder.*

### KL divergence

#### Definitions

> **KL divergence $\text{KL}(q \,\|\, p)$**: A measure of the gap between a distribution $q$ and a reference $p$. It is never negative, is zero only when $q = p$, and is **not symmetric**.

Here we always measure the encoder's posterior against the prior. Per latent dimension, for $q = \mathcal{N}(\mu, \sigma^2)$ and $p = \mathcal{N}(0, 1)$:

$$
\text{KL} = \tfrac{1}{2}\left(\mu^2 + \sigma^2 - 1 - \ln \sigma^2\right)
$$

| Term | Penalizes |
|---|---|
| $\mu^2$ | Being off-centre |
| $\sigma^2 - 1 - \ln \sigma^2$ | Being too wide or too narrow; zero exactly at $\sigma = 1$ |

![Gaussian KL](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/gaussian-kl.svg)

*A matched posterior has KL $0.02$; a shifted mean gives $2.43$; a posterior that is too wide gives $1.51$.*

The KL term is the **only** thing tying each image's posterior to the distribution sampled at generation time.

### The VAE objective

#### Definitions

> **ELBO (evidence lower bound)**: A lower bound on the data log-likelihood. The VAE loss is the negative ELBO; maximizing the ELBO and minimizing the negative ELBO are the same.

> **Posterior collapse**: When $q(z \mid x) = \mathcal{N}(0, I)$ for every image, so the code carries no information about $x$.

$$
\mathcal{L}_{\text{VAE}} = \underbrace{\mathbb{E}_{q(z \mid x)}\big[\text{reconstruction error}\big]}_{\text{rebuild } x \text{ from a sampled code}} + \underbrace{\text{KL}\big(q(z \mid x) \,\|\, p(z)\big)}_{\text{keep the posterior near the prior}}
$$

- For images, the reconstruction term usually reduces to a simple MSE between generated and input images.
- **β-VAE** weights the KL term by $\beta$ for more control.

The two terms pull in opposite directions:

| Regime | Result |
|---|---|
| Reconstruction only | $\sigma \rightarrow 0$ and posteriors drift apart: back to a plain AE with gaps |
| KL only | Posterior collapse: perfect prior match, useless reconstruction |
| Balanced | Posteriors close enough to the prior to sample from, distinct enough to rebuild each image |

### VAE strengths and weaknesses

A VAE is an autoencoder whose encoder outputs a distribution, regularized so the posteriors together match a sampleable prior.

| Strengths | Weakness |
|---|---|
| Stable, simple training (one network pair, one clear objective) | Samples tend to be **blurry**: the reconstruction term averages over everything the posterior could encode, smoothing fine detail |
| Smooth, structured latent space; nearby codes decode to similar images, enabling interpolation and editing | |

VAEs rarely generate final images today, but the **VAE encoder is a core part of Stable Diffusion**, compressing images so diffusion runs cheaply.

### GANs: a forger versus a detective

#### Definitions

> **Generative adversarial network (GAN)**: Two networks trained together with opposing objectives — a generator and a discriminator (Goodfellow et al., 2014).

> **Generator $G$**: Takes random noise $z$ and tries to produce a realistic fake image (the forger).

> **Discriminator $D$**: Takes one image and outputs the probability that it is real rather than generated (the detective).

![GAN](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/gan.svg)

*The generator turns noise into a fake image; the discriminator judges real versus fake, and its feedback trains both.*

- Noise is the seed for **diversity**; a fixed input would always map to the same output.
- The discriminator is trained to catch fakes; the generator is trained to fool it. As one improves, the other must too — an **arms race**.
- At the end, keep only the generator.

### The GAN objective

$$
\min_G \max_D \; \mathbb{E}_{x \sim p_{\text{data}}}\big[\log D(x)\big] + \mathbb{E}_{z \sim p(z)}\big[\log\big(1 - D(G(z))\big)\big]
$$

- $D$ is trained to **maximize** its output on real data (and minimize it on fakes).
- $G$ is simultaneously trained to **minimize** $\log(1 - D(G(z)))$.
- This is a two-player **minimax** game, a well-studied optimization problem.

Intuition:

1. The discriminator sees a real photo and says 0.9 "real" (correct), then sees a fake and says 0.8 "real" (fooled). It adjusts to score that fake lower.
2. The generator is told "the discriminator still flagged 30% of your fakes" and adjusts to push those towards "real".
3. Repeat millions of times until fakes are indistinguishable from real.

Why training is notoriously hard:

- It is a **moving target**: both networks change at once (in practice they often alternate).
- If the discriminator gets too good too fast, the generator gets no useful signal ("you're always wrong" teaches nothing).
- Balancing them is the whole art; failures include **mode collapse** and instability.

### GAN strengths and weaknesses

| Strengths | Weaknesses |
|---|---|
| **Sharp**, detailed images — competition rewards crisp detail, no blurry averaging | Unstable, finicky training |
| **Fast** sampling: one generator forward pass per image | **Mode collapse**: producing only a few kinds of image |
| | No well-structured latent space or likelihood; harder to control and evaluate |

GANs dominated image generation around 2016-2021, with many variants (conditional GANs, CycleGAN, style control). Diffusion then matched their sharpness with far more stable training and greater diversity. GANs are still used for fast generation, and the discriminator idea appears in other networks.

### Diffusion: the core idea

#### Definitions

> **Diffusion model**: A generator that learns to reverse a fixed process which gradually adds noise to images (Ho et al., 2020, DDPM).

> **Forward process**: Repeatedly add a little random noise to a real image until only noise remains. It is fixed — no learning.

> **Reverse process**: A trained network that undoes one noise step, run many times starting from pure noise.

![Diffusion forward and reverse](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/diffusion-forward-reverse.svg)

*The fixed forward process adds noise until only noise remains; the learned reverse process removes it step by step to produce a new image.*

### Why many small steps

- Generating a whole image from pure noise in one shot is extremely hard; that is essentially the GAN's difficulty.
- Diffusion solves a small, easy problem instead: "this image is slightly noisy; make it slightly less noisy".
- Each denoising step is a small, well-behaved **regression** the network can learn reliably.
- Chaining hundreds of easy steps accomplishes what one giant leap cannot.

Analogy: you cannot sculpt a statue in one strike, but you can remove one chip at a time.

"Many easy steps beat one hard step" is why diffusion trains stably where GANs struggle, and why its images are both sharp and diverse.

### Training: predict the noise

The network is **never asked to make an image**. It is asked to guess the noise that was added — a plain regression.

1. Take a clean image $x_0$.
2. Pick a random step $t$ and random noise $\epsilon \sim \mathcal{N}(0, I)$.
3. Construct the noisy image directly with the fixed schedule:

$$
x_t = \sqrt{\bar{\alpha}_t}\,x_0 + \sqrt{1 - \bar{\alpha}_t}\,\epsilon
$$

4. The network predicts the noise: $\hat{\epsilon} = \epsilon_\theta(x_t, t)$.
5. Loss $= \|\epsilon - \hat{\epsilon}\|^2$; backpropagate to update $\theta$.

![Diffusion training](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/noise-prediction.svg)

*Pick a clean image, a random step and noise, build $x_t$ directly, predict the noise, and minimize the squared error.*

No likelihood, no adversary — one clean regression.

### The noise schedule and ᾱₜ

#### Definitions

> **$\bar{\alpha}_t$ ("alpha-bar at step $t$")**: A number between 0 and 1 giving how much of the clean image survives at step $t$. It is the cumulative product of a **fixed noise schedule** chosen in advance; the network never learns it.

- $\bar{\alpha}_t \approx 1$ early (mostly clean image); $\bar{\alpha}_t \approx 0$ late (almost pure noise).
- So $\sqrt{\bar{\alpha}_t}\,x_0$ fades out while $\sqrt{1 - \bar{\alpha}_t}\,\epsilon$ fades in, smoothly turning an image into noise.

![Noise schedule](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/alpha-bar.svg)

*$\bar{\alpha}_t$ falls from 1 to 0 while $1 - \bar{\alpha}_t$ rises, so $x_t$ turns smoothly from image into noise.*

### The diffusion loss

$$
\mathcal{L} = \big\|\,\epsilon - \epsilon_\theta(x_t, t)\,\big\|^2
$$

| Symbol | Meaning |
|---|---|
| $\epsilon$ | The random noise added to the clean image; known exactly because we chose it |
| $x_t$ | The noisy image at step $t$, built with $\bar{\alpha}_t$; the network's input |
| $\epsilon_\theta(x_t, t)$ | The network's noise prediction given the noisy image and step $t$ ($\theta$ = weights) |
| $\|\cdot\|^2$ | Squared difference: standard regression error |

| Model | What its loss asks |
|---|---|
| VAE | Reconstruct accurately **and** keep the latent space sampleable |
| GAN | Fool an adversary — a complicated, often unstable moving target |
| Diffusion | Predict the noise — a simple regression |

### Generating an image step by step

1. Start from pure random noise (like the VAE, generation begins with noise).
2. Ask the network "what noise is in this?" and subtract a bit of it → a slightly cleaner image.
3. Repeat 50-1000 times → a fully formed, novel image emerges.

![Sampling loop](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/sampling-loop.svg)

*Start from pure noise, predict the noise, subtract a little, and repeat many times.*

| Pros | Cons |
|---|---|
| Excellent quality and diversity — why diffusion won | **Slow**: VAEs and GANs need one pass; diffusion needs many. Fast samplers (e.g. DDIM) cut 1000 steps to about 4 |

For high-resolution images, pixel-space diffusion is too expensive. Running diffusion in a VAE's compressed latent space gives **Stable Diffusion** (next lecture).

### Comparison of image generators

| | VAE | GAN | Diffusion |
|---|---|---|---|
| Machinery | Encoder → $z \sim \mathcal{N}(\mu, \sigma)$ → decoder → $\hat{x}$ | Generator: noise → $\hat{x}$; discriminator: real or fake? | Add noise (fixed); network removes noise, $\times T$ |
| Loss | Reconstruct + KL | The two networks compete | Predict the noise (MSE) |
| Training | One network pair, stable | Tricky | Stable |
| Samples | Smooth latent, blurry images | Sharp, one-pass | Best quality and diversity, slow |

Many GAN variants exist, but all suffer from diversity or stability issues. Diffusion is now the dominant image-generation approach, and the basis of every modern generator: it turned a very complex problem into many easy steps.

![Generator comparison](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/generator-comparison.svg)

*VAE, GAN, and diffusion side by side: their machinery, losses, and characteristic strengths.*

## 7. Text-to-Image Generation

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Vision-Language Models  
> **Source**: [Lecture7_Text_to_Image_Generation.pdf](../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/VLM%27s/Lecture7_Text_to_Image_Generation.pdf), Prof Patrick Marais, slides 1-17 (primary papers: Rombach et al. 2022; Ho and Salimans 2022; Peebles and Xie 2023)  
> **Generated**: 2026-10-29  

### The cost of diffusion in pixel space

Standard (DDPM) diffusion generates every pixel directly. For a $512 \times 512$ image:

$$
512 \times 512 \times 3 = 786{,}432 \text{ numbers per image, per denoising step}
$$

- The denoiser reads and rewrites all 786k numbers for each of its ~1000 timesteps, for every image generated.
- The cost is not amortized: training **and** inference both pay it repeatedly.
- Pixel-space diffusion works, but at scale it needs a cluster, not a laptop or single GPU.

Can the same diffusion process run more economically? Yes — in a low-dimensional latent space.

### Latent diffusion

#### Definitions

> **Latent diffusion**: Running the whole diffusion process (forward noising and reverse denoising) inside a VAE's compressed latent space, then decoding once at the end (Rombach et al., 2022).

![Latent diffusion](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/07_Text_To_Image_Generation/latent-cost.svg)

*A frozen VAE encodes $512 \times 512 \times 3$ pixels (786,432 numbers) into a $64 \times 64 \times 4$ latent (16,384), diffusion runs there, and the VAE decoder maps back.*

$$
\frac{512 \times 512 \times 3}{64 \times 64 \times 4} = \frac{786{,}432}{16{,}384} = 48\times \text{ fewer numbers}
$$

- The VAE encoder/decoder is **trained once, separately, then frozen**. It handles accurate, efficient encoding of image characteristics (perception); diffusion handles generation.
- **Inference**: choose a random seed in latent space, run denoising there, and decode the final latent to an image with the VAE decoder.

This is cheap and the basis of **Stable Diffusion**.

### The control problem: conditioning on text

The diffusion denoiser maps (noisy latent, timestep) → predicted noise. There is **no text anywhere**, so it can only produce *some* plausible image, never one dictated by a prompt.

The prompt must condition **every** one of the ~50 denoising steps, not just influence the start. Two sub-problems:

1. **Encode the words**: use CLIP's text encoder, which already maps prompts into a space aligned with image content. Use **all** CLIP text tokens (usually 77), not just the pooled output.
2. **Condition the denoiser**: use cross-attention, with the latent supplying queries and the text supplying keys and values.

### Text conditioning with cross-attention

![Text conditioning](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/07_Text_To_Image_Generation/cross-attention-conditioning.svg)

*Prompt tokens from the CLIP text encoder supply keys and values; noisy-latent patches supply queries; cross-attention appears at many layers at every step.*

$$
Q = \text{latent features} \cdot W^Q, \qquad K = \text{text tokens} \cdot W^K, \qquad V = \text{text tokens} \cdot W^V
$$

$$
\text{CrossAttn}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right) V
$$

- Each patch of the noisy latent "asks" the prompt what it should depict.
- Cross-attention is injected at **many layers** of the denoiser, at **every step**, so guidance persists throughout denoising.

### Classifier-free guidance

#### Definitions

> **Classifier-free guidance (CFG)**: Steering generation by extrapolating from the model's unconditioned noise prediction towards its prompt-conditioned prediction, controlled by a guidance scale (Ho and Salimans, 2022).

> **Guidance scale $w$**: How strongly to follow the direction the prompt pulls the image.

$$
\hat{\epsilon} = \epsilon_\theta(z_t, t, \varnothing) + w \cdot \big[\epsilon_\theta(z_t, t, c) - \epsilon_\theta(z_t, t, \varnothing)\big]
$$

The bracket is **"what the prompt changed"**; the scale amplifies it. The result is a modified noise prediction, which is then subtracted from the current latent to get a less noisy latent.

![Classifier-free guidance](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/07_Text_To_Image_Generation/cfg.svg)

*The guided prediction starts at the unconditional prediction and moves $w$ times along the direction the prompt pulls it.*

| Scale | Effect |
|---|---|
| $w = 0$ | Prompt ignored (unconditional) |
| $w = 1$ | Ordinary conditioning |
| $w = 7.5$ | Follow the prompt direction $7.5\times$ as hard (Stable Diffusion default) |
| Well above typical range | Over-saturation and artifacts |

Example: "An oil painting of a collie in a top hat" with the same model, prompt, and seed. As the scale rises, prompt adherence improves, but contrast increases too.

- **Why "classifier-free"**: earlier methods steered with a separate image classifier; CFG uses only the model's own with/without-prompt predictions.
- **Cost**: two denoiser passes per step, roughly doubling generation time. A very common, worthwhile trade.
- **Training**: the prompt is randomly dropped during training, so one model learns both the conditioned and unconditioned predictions.

### The Stable Diffusion pipeline

![Stable Diffusion pipeline](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/07_Text_To_Image_Generation/stable-diffusion.svg)

*The prompt is encoded by CLIP; random latent noise is denoised by a guided U-Net or DiT for $T$ steps; the VAE decoder makes the image.*

1. **Encode the prompt** with the CLIP text encoder into token embeddings.
2. **Sample** a random latent $z_T$ (e.g. $64 \times 64 \times 4$).
3. **For each step** $t = T, \dots, 1$:
   1. Predict the noise with and without the prompt (cross-attention to text tokens).
   2. Combine them with classifier-free guidance.
   3. The **scheduler** uses the guided prediction to compute a less noisy latent $z_{t-1}$.
4. **Decode** the final latent $z_0$ with the VAE decoder into pixels.

### Diffusion Transformers (DiT)

#### Definitions

> **U-Net**: The convolutional encoder-decoder architecture used as the denoiser in the original Stable Diffusion.

> **Diffusion Transformer (DiT)**: A denoiser that cuts the latent into patches like a ViT and uses a Transformer to predict the noise over those patch tokens (Peebles and Xie, 2023).

![Diffusion Transformer](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/07_Text_To_Image_Generation/dit.svg)

*DiT patchifies the noisy latent like a ViT and uses Transformer blocks to predict the noise.*

| | U-Net denoiser | DiT denoiser |
|---|---|---|
| Architecture | Convolutional | Transformer over latent patch tokens (ViT-style tokenization) |
| Text conditioning | Cross-attention | Cross-attention or conditioning tokens |
| Guidance | CFG | Unchanged |
| Scaling | Works well | Scales better with data and compute |

DiTs are behind most current top-tier image and video generators — the ViT from lecture 1, now used for generation.

### Evaluation: two separate questions

A good generation must be both **realistic** and **faithful to the prompt**. These fail independently: an amazing photo of the wrong thing, or an on-prompt but ugly mess. So they are measured separately.

| Question | Metric |
|---|---|
| Is it realistic? | FID |
| Does it match the prompt? | CLIPScore |

### FID

#### Definitions

> **Fréchet Inception Distance (FID)**: The distance between the feature distributions of real and generated images, as seen by a pretrained Inception network (Heusel et al., 2017). Lower is better.

1. Extract Inception features for a set of real images and a set of generated images.
2. Fit a Gaussian (mean and covariance) to each set.
3. Measure the distance between the two Gaussians.

The standard Fréchet distance between the fitted Gaussians $(\mu_r, \Sigma_r)$ and $(\mu_g, \Sigma_g)$ is:

$$
\text{FID} = \|\mu_r - \mu_g\|^2 + \text{Tr}\!\left(\Sigma_r + \Sigma_g - 2\big(\Sigma_r \Sigma_g\big)^{1/2}\right)
$$

![FID and CLIPScore](../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/07_Text_To_Image_Generation/fid-clipscore.svg)

*FID compares the feature distributions of real and generated sets; CLIPScore checks each image against its prompt (0.82 on-prompt vs 0.24 off-prompt).*

| Measures | Does not measure | Limits |
|---|---|---|
| Realism and diversity of the generated **set** | Whether any single image matches the prompt; a model can have excellent FID while ignoring prompts | Needs a fairly large sample; sensitive to the reference set |

### CLIPScore

#### Definitions

> **CLIPScore**: The cosine similarity between CLIP embeddings of the generated image and its prompt (Hessel et al., 2021).

$$
\text{CLIPScore}(I, c) \propto \cos\big(E_{\text{img}}(I), E_{\text{txt}}(c)\big)
$$

A high value means image and text sit close together in CLIP's shared space, so the image is on-prompt. It is the same similarity used for zero-shot classification, pointed at generation.

> [!warning] <span style="color: #ff939b">Use both metrics</span>
> A model can have good FID while ignoring the prompt (realistic but wrong), or good CLIPScore while producing a garbled mess that contains the right concepts. They catch different failures. Neither replaces a human judging the image; they are cheap automatic proxies used at scale during development.
