---
tags:
  - reasoning-in-ai
---

# Introduction to (Large) Language Models

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Large Language Models  
> **Source**: [1-Introduction - Copy.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/LLM%27s/1-Introduction%20-%20Copy.pdf), Dr Jan Buys, slides 1-47  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
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

---

## Core Content

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

![Schematic 2D embedding projection](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/01_Introduction_To_Language_Models/embedding-neighborhoods.svg)

*A 2D (t-SNE) projection of word embeddings: function words cluster together, as do negative-sentiment and positive-sentiment words.*

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

- Even in a very large corpus, **most possible n-grams never appear**. A bigram count table over a small vocabulary is mostly zeros.
- Models must still assign non-zero probability to every n-gram.
- Complex formulas interpolate between n-gram sizes and smooth the distribution. **Modified Kneser-Ney smoothing** was state of the art.

| Strength | Weakness |
|---|---|
| Very computationally efficient; fast to train on large data | Sparsity prevents effective use of long contexts, even with $> 1$ trillion training tokens |
| Can score many candidate sequences, e.g. in statistical machine translation | |

### Neural language model architectures

![Fixed-window and recurrent language models](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/01_Introduction_To_Language_Models/sequence-models.svg)

*A fixed-window feedforward LM sees only a few previous words. A recurrent LM carries a hidden state across the whole sequence.*

| Architecture | Context | Notes |
|---|---|---|
| Feedforward neural LM | Fixed small window | Shares many n-gram limitations |
| Recurrent neural network (RNN) | No explicit length limit | **LSTM** RNNs were the first widely used deep-learning LMs |
| **Transformer** | Full sequence via attention | More scalable than LSTMs; now dominant |

### Three topologies for LLMs

![Decoder, encoder, and encoder-decoder topologies](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/01_Introduction_To_Language_Models/model-topologies.svg)

*Decoders predict the next token from a prefix. Encoders build bidirectional representations of the full input. Encoder-decoders encode an input and decode an output through cross-attention.*

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

**T5** frames every task as text-to-text: the encoder reads the task name and input, and the decoder generates the output (e.g. "translate English to German: That is good." → "Das ist gut."). It is pretrained on denoising objectives:

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

![Three stages of LLM training](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/01_Introduction_To_Language_Models/training-stages.svg)

*Pretraining learns general text patterns, instruction tuning learns to respond to tasks, and preference alignment shapes behaviour towards preferred responses.*

| Stage | Data | Result |
|---|---|---|
| 1. Pretraining | Large text corpora | Pretrained LLM |
| 2. Instruction tuning | Instruction-response pairs (e.g. label sentiment, summarize, translate) | Instruction-tuned LLM |
| 3. Preference alignment | Preference data: preferred vs dispreferred responses (e.g. refusing to help with embezzlement) | Aligned LLM |
