---
tags:
  - reasoning-in-ai
---

# Tokenization

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Large Language Models  
> **Source**: [2-Tokenization.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/LLM%27s/2-Tokenization.pdf), Dr Jan Buys, slides 1-25 (based on Jurafsky and Martin Ch. 2; some slides from Stanford CS336)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What tokenization does|What tokenization does]]
  - [[#Character and byte tokenizers|Character and byte tokenizers]]
  - [[#Word tokenizers|Word tokenizers]]
  - [[#Subword tokenization|Subword tokenization]]
  - [[#Byte-pair encoding (BPE)|Byte-pair encoding (BPE)]]
  - [[#Pre-tokenization and word boundaries|Pre-tokenization and word boundaries]]
  - [[#BPE toy corpus example|BPE toy corpus example]]
  - [[#The BPE segmenter|The BPE segmenter]]
  - [[#Best practices|Best practices]]

---

## Core Content

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

![Applying BPE](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/02_Tokenization/bpe-pipeline.svg)

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

![BPE merges on the toy corpus](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/02_Tokenization/bpe-merges.svg)

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
