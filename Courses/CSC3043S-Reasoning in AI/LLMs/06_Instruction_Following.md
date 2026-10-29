---
tags:
  - reasoning-in-ai
---

# LLM Instruction Following

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Large Language Models  
> **Source**: [6-InstructionFollowing.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/LLM%27s/6-InstructionFollowing.pdf), Dr Jan Buys, slides 1-24 (slides from Tatsunori Hashimoto, others as cited)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
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

---

## Core Content

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

![Instruction training](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/06_Instruction_Following/instruction-training.svg)

*Pretrained parameters are trained on diverse instruction-response pairs with a response-only prediction loss, giving an instruction-tuned model.*

- Training starts from the pretrained parameters.
- It works exactly like pretraining, except for **loss masking**: only the response contributes to the loss.

For instruction $x$ and response $y$:

$$
\mathcal{L}_{\text{SFT}} = -\sum_{t=1}^{|y|} \log P_\theta(y_t \mid x, y_{<t})
$$

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

![Instruction scaling](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/06_Instruction_Following/instruction-scaling.svg)

*Held-out task performance rises with the number of fine-tuning tasks, and is higher for larger models (8B, 62B, 540B).*

From Chung et al. (2022):

- Instruction fine-tuning improves performance by a large margin over no fine-tuning.
- More fine-tuning tasks improves performance.
- An order-of-magnitude larger model (8B → 62B, 62B → 540B) improves performance substantially, both with and without fine-tuning.

### Instruction fine-tuning for safety

#### Definitions

> **Violation rate**: The rate at which unsafe prompts get answered.

> **False refusal rate**: The rate at which the model refuses when answering would be safe.

Models deployed to end users need safety controls. Safety tuning must balance a low violation rate against a low false refusal rate.

![Safety trade-off](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/06_Instruction_Following/safety-tradeoff.svg)

*For Llama 3 8B and 70B, reducing violations comes at the cost of more false refusals.*

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

![Few-shot prompt](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/06_Instruction_Following/few-shot-prompt.svg)

*Example input-answer pairs specify the task; the model generates the answer for the new input without any weight change.*

- Performance varies with **which** examples are chosen, and even with their **order**.
- More examples generally improve performance.
