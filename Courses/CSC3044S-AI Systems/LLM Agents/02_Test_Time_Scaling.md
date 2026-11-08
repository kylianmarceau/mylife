---
tags:
  - ai-systems
---

# Test-Time Scaling

**Subject**: CSC3044S AI Systems
**Source**: `LLM Agents 2_ Test-Time Scaling.pdf`, Dr Francois Meyer (LLM Agents Topic 2), pages 1-55
**Generated**: 2026-11-08

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Where Test-Time Scaling Fits|Where Test-Time Scaling Fits]]
  - [[#LLM Evaluation|LLM Evaluation]]
  - [[#Pretraining and Autoregressive Inference|Pretraining and Autoregressive Inference]]
  - [[#Decoding Strategies and Decoding as Search|Decoding Strategies and Decoding as Search]]
  - [[#Scaling the Context With In-Context Learning|Scaling the Context With In-Context Learning]]
  - [[#Chain-of-Thought Prompting|Chain-of-Thought Prompting]]
  - [[#Scaling Generation - Output Length and Search Space|Scaling Generation - Output Length and Search Space]]
  - [[#Parallel Scaling and Self-Consistency|Parallel Scaling and Self-Consistency]]
  - [[#Verifiers|Verifiers]]
  - [[#Best-of-N|Best-of-N]]
  - [[#Combining Search Algorithms and Verifiers|Combining Search Algorithms and Verifiers]]
  - [[#Learning to Reason Through Training|Learning to Reason Through Training]]
  - [[#Reinforcement Learning With Verifiable Rewards (RLVR)|Reinforcement Learning With Verifiable Rewards (RLVR)]]
  - [[#DeepSeek R1-Zero|DeepSeek R1-Zero]]
  - [[#From Self-Consistency to RLVR|From Self-Consistency to RLVR]]

---

## Core Content

### Where Test-Time Scaling Fits

#### Definitions

> **Pretraining**: Training an LLM on a large raw-text corpus to predict the next token; the most computationally expensive part of developing an LLM.

> **Scaling Laws**: Empirical relationships showing that performance improves as a function of pretraining data size, model size and compute.

> **Instruction Tuning**: Post-training that teaches the model to answer questions and format answers (makes it a chatbot).

> **Alignment (Preference Alignment)**: Post-training that refines behaviour and safety based on human preferences (makes it a *good* chatbot).

> **Test-Time Scaling**: Spending more compute at inference to get better answers.

> **Reasoning**: Working through a problem step by step rather than answering immediately.

The course builds a coding agent (in the style of Claude Code) from scratch in four steps:

1. Scale the LLM pretraining phase.
2. **Scale the LLM generation phase (test-time scaling)**, which is this topic.
3. Enable the LLM to use files and tools.
4. Wrap the LLM in an agentic framework.

Pretraining is already scaled as far as it practically goes. The question here is: given a large pretrained LM, how do we get the most out of it?

![LLM training pipeline](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/llm_training_pipeline.svg)
*Pretraining produces a pretrained LLM; the post-training phase then applies instruction tuning and preference alignment. Post-training was covered in CSC3043F but is still used alongside test-time scaling.*

| Stage | What it does | Informal goal |
|---|---|---|
| Instruction tuning | Teaches the model to answer questions and format answers | Make it a chatbot |
| Alignment | Refines behaviour and safety based on preferences | Make it a *good* chatbot |
| Test-time scaling | Spends more compute at inference | Make it reason |

Test-time scaling **enables reasoning**. It unlocks new capabilities, letting the model solve complex tasks that need reasoning, such as maths and coding.

![Three scaling laws](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/three_scaling_laws.svg)
*"From one to three scaling laws": intelligence keeps rising with compute as pretraining scaling is followed by post-training scaling and then test-time scaling ("long thinking"). Each dashed line shows the slower gain from staying on the previous curve.*

OpenAI's o1 was the model that showed test-time compute behaves like a new scaling axis. On the AIME maths competition, pass@1 accuracy rose steadily with both training compute and test-time compute (both on log scales).

![o1 compute scaling](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/o1_compute_scaling.svg)
*o1 AIME pass@1 accuracy grows roughly linearly in log train-time compute (about 33% to 69%) and log test-time compute (about 20% to 75%). Values are read approximately from the source plot.*

### LLM Evaluation

#### Definitions

> **Evaluation Dataset**: A collection of questions with correct answers used to measure how capable an LLM is.

> **Benchmark**: A collection of datasets that quantifies model performance across different tasks or capabilities.

> **Benchmark Saturation**: When models quickly reach about 100% accuracy on a new dataset, so it stops distinguishing between models.

> **Training Data Contamination**: When public benchmark data ends up in the pretraining corpus, so models may memorise answers instead of learning the capability.

We know how capable an LLM is by testing it on evaluation datasets of questions and correct answers.

| Task type | What it tests | Example |
|---|---|---|
| Factual knowledge | Answering without access to external data | "What is the capital city of Ghana?" → Accra |
| Multiple choice questions | Commonsense and reading comprehension | "Hat-trick-hero Salah helps Liverpool to 5-0 win over United. How many goals did Salah score?" A) 0 B) 1 C) 2 D) 3 → D) 3 |

Multiple-choice datasets such as MMLU store each item as a question, a subject, a list of choices and an answer label:

| question (abridged) | subject | choices | answer |
|---|---|---|---|
| Find all zeros in the indicated finite field of the given polynomial… | abstract_algebra | `["0", "1", "0,1", "0,4"]` | 3 (D) |
| Statement 1: A factor group of a non-Abelian group is non-Abelian… | abstract_algebra | True/False pairs | 1 (B) |
| Find the product of the given polynomials in the given polynomial ring… | abstract_algebra | four polynomials | 1 (B) |

More advanced capabilities are tested with question-answer pairs that require reasoning, such as maths word problems. For example:

- **Problem**: Mary's vacuum battery lasts ten minutes. Each room takes four minutes. She has three bedrooms, a kitchen and a living room. How many times must she charge the vacuum to clean the whole house?
- **Solution**: $3+1+1=5$ rooms, $4 \times 5 = 20$ minutes, $20/10 = 2$ charges.
- **Final answer**: $2$.

Reasoning tasks include:

- Maths exam problems
- Commonsense reasoning
- Symbolic reasoning
- Hard science questions
- **Coding tasks**, which can be scored automatically by whether unit tests pass

![Evaluating against ground truth](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/evaluation_ground_truth.svg)
*Each expected input has a ground-truth answer; a model's new response is compared against it to decide whether it is correct.*

Evaluation matters because it is how the field tracks AI progress, which is what benchmark leaderboards report. But it is getting harder:

| Difficulty | Why it is a problem |
|---|---|
| Benchmarks saturate | The field moves so fast that models reach 100% on a new dataset before long |
| Training data contamination | Public benchmarks leak into pretraining data, so scores may reflect memorisation |
| Complex capabilities are hard to evaluate | Open-ended tasks have no simple right/wrong answer, e.g. "is this a good research summary?" or "did the agent handle the customer well?" |

Strong models can still fail on simple-looking variants of tasks, which shows a benchmark score does not guarantee a general capability. GPT-4 examples:

| Task | Succeeds on | Fails on |
|---|---|---|
| Counting letters | A string of 30 i's → 30 | A string of 29 i's → answers 30 |
| Article swapping (swap each *a/an/the* with the word before it) | Repairs a sentence correctly | Rewrites the scrambled sentence into a different, fluent sentence |
| Shift ciphers | Shift of 13 (ROT13, common online) decoded correctly | Shift of 12 decoded as an unrelated sentence |
| Linear functions | Multiply by $9/5$ and add $32$ (Celsius to Fahrenheit): $328 \to 622.4$ | Multiply by $7/5$ and add $31$: answers $457.6$ instead of $490.2$ |

### Pretraining and Autoregressive Inference

#### Definitions

> **Teacher Forcing**: Training where the ground-truth previous tokens, not the model's own predictions, are fed as input at every position.

> **Inference (Test Time)**: Using a trained model to generate output for a new input.

> **Autoregressive Generation**: Generation where each predicted token becomes input for the next step.

LLM pretraining has four parts:

| Part | Description |
|---|---|
| Dataset | Large dataset of raw text (e.g. a web-scraped corpus) |
| Batch | Continuous text sequences sampled from the dataset |
| Task | Predict the next word given all preceding words (with teacher forcing) |
| Loss | Cross-entropy loss summed over all tokens in a sequence |

With teacher forcing, every position is trained in parallel. The loss for a sequence $w_1,\dots,w_T$ is

$$
\mathcal{L} = -\sum_{i=1}^{T-1} \log P_\theta\left(w_{i+1} \mid w_1,\dots,w_i\right)
$$

![Pretraining with teacher forcing](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/pretraining_teacher_forcing.svg)
*Inputs "So long and thanks for" are embedded (E plus position), passed through causal transformer layers and unembedded (U) into a softmax that predicts the next token at every position: "long and thanks for all".*

At inference, the model instead generates one token at a time. Given tokens $w_1,\dots,w_i$:

1. Run the full forward pass to get $\hat{\mathbf{y}}_i = \operatorname{softmax}(\mathbf{u}_i)$, where $\mathbf{u}_i$ are the logits.
2. Greedily select $\arg\max \hat{\mathbf{y}}_i$, or sample the next token $w_{i+1}$ from this distribution.
3. Append $w_{i+1}$ to the sequence and repeat.

![Autoregressive generation](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/autoregressive_generation.svg)
*Starting from "the dog", step 1 predicts "sat", which is fed back in; step 2 predicts "down"; step 3 predicts EOS, giving "the dog sat down".*

### Decoding Strategies and Decoding as Search

#### Definitions

> **Decoding**: The process of selecting the next word or token based on the probability distribution produced by a language model.

> **Greedy Decoding**: Picking the most probable token at every step.

> **Sampling**: Drawing the next token from the probability distribution instead of always taking the top one.

> **Decoding as Search**: Viewing each generation as a path in a search tree whose nodes are prefixes and whose edges are next tokens.

Greedy decoding picks, at each step $t$,

$$
y_t = \arg\max_{w} P\left(w \mid x_1,\dots,x_n,\, y_1,\dots,y_{t-1}\right)
$$

where $x_1,\dots,x_n$ is the input and $y_1,\dots,y_{t-1}$ are the tokens generated so far. Sampling instead draws

$$
y_t \sim P\left(\cdot \mid x_1,\dots,x_n,\, y_1,\dots,y_{t-1}\right)
$$

![Greedy decoding versus sampling](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/greedy_vs_sampling.svg)
*From the same softmax distribution, greedy always takes "cat"; sampling can produce "cat", "dog" or even a low-probability token like "bird" on different runs.*

| Property | Greedy decoding | Sampling |
|---|---|---|
| Rule | Take the most probable token | Draw a token from the distribution |
| Behaviour | Deterministic: same seed ⇒ same output | Stochastic: many runs ⇒ different outputs |
| Strength | Simple | More diverse text |
| Weakness | Repetitive text and loops such as "the the the…" | A low-probability token can derail the sentence |

In the search view, each edge weight is the log-probability of a token given its prefix, and a full path is scored by summing them:

$$
\text{score}(y_1,\dots,y_T) = \sum_{t=1}^{T} \log P\left(y_t \mid y_{<t}\right)
$$

![Decoding as search](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/decoding_search_tree.svg)
*Each next-token distribution supplies the edge weights below a node. The highlighted path "The end <eos>" scores $-2.1 + (-1.8) = -3.9$. Greedy always takes the highest-probability branch ("end", then "is" at $-1.2$); sampling follows a different path each run.*

### Scaling the Context With In-Context Learning

#### Definitions

> **Few-Shot Prompting**: Prompting with input-output examples so the model learns the expected behaviour for a task without any parameter updates.

> **In-Context Learning (ICL)**: An LLM learning and performing a new task from examples in its prompt, without changing any internal parameters.

> **Zero-Shot / One-Shot / Few-Shot**: Prompts with no examples, one example, or several examples of the task.

The first way to scale inference is to **scale the context (input)**. The goal is to condition the generation $y$ on more information in the input or context $x$ to improve task performance.

Example few-shot prompt for sentiment analysis:

```text
You are an AI assistant who can decode emotion analysis.
Example 1: This movie is great, I had a great time watching it.
Result 1: Positive
Example 2: I've never seen a worse movie, it was a waste of time.
Result 2: Negative
Example 3: The food is bad and the service should be improved
→ model output: Negative
```

How many examples are necessary depends on the task.

![Zero-shot, one-shot and few-shot](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/zero_one_few_shot.svg)
*The same translation task as a zero-shot instruction, a one-shot prompt with one example, and a few-shot prompt with several examples.*

In-context learning **emerges** only when pretraining is sufficiently scaled.

- Few-shot prompting can improve performance over zero-shot prompting.
- For many tasks, more examples improve performance, up to a point.

![Few-shot scaling by model size](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/few_shot_scaling.svg)
*GPT-3 accuracy against the number of in-context examples $k$. Gains flatten as $k$ grows, and larger models gain much more (175B goes from 62% to 90%, 125M only from 35% to 44%).*

### Chain-of-Thought Prompting

#### Definitions

> **Chain-of-Thought (CoT) Prompting**: Few-shot prompting where the in-context examples include intermediate problem-solving steps, so the answer is generated only after an explanation of the reasoning steps needed to reach it.

> **Task-Specific Finetuning**: Training an LLM's parameters for one specific task.

CoT scales the context further: the examples now show *how* to solve the problem, not just the answer.

![Standard versus chain-of-thought prompting](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/cot_vs_standard_prompting.svg)
*With a plain exemplar the model answers the cafeteria question wrongly (27). With a worked exemplar it writes intermediate steps ($23-20=3$, $3+6=9$) and answers correctly (9).*

The goal is to encourage the model to reason by producing intermediate reasoning steps. This helps because:

- The model can **break down complex tasks** into simpler subtasks, improving performance on hard tasks.
- The model can **learn the reasoning steps** needed to solve a task.
- No parameters are updated, so this is learning without "training".

Findings:

- CoT prompting **emerges with scale**: it only works for models with more than about 100B parameters.
- The biggest benefit over standard prompting is on **complex tasks**, e.g. GSM8K maths word problems.
- It can even **outperform task-specific finetuning**, without any parameter updates.

![CoT emergence with scale](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/cot_emergence_with_scale.svg)
*Solve rate against model size for LaMDA, GPT and PaLM on GSM8K, SVAMP and MAWPS. CoT only pulls ahead at the largest sizes, and PaLM 540B with CoT reaches or beats the prior supervised best. Points are approximate.*

Limitations, and what they motivate:

| Limitation | Fix |
|---|---|
| The model generates a single chain of thought, so one wrong reasoning step derails the whole sequence | Sample multiple chains of thought |
| We cannot tell whether the reasoning trace is right, so we cannot judge reasoning quality | Introduce verifiers that assess answers or reasoning |

### Scaling Generation - Output Length and Search Space

#### Definitions

> **Scaling Output Length**: Increasing the number of tokens generated during inference (more tokens per attempt, e.g. chain of thought).

> **Scaling Search Space**: Expanding the set of candidate output sequences considered during search, so that higher-quality outputs can be found.

Few-shot prompting scales the model's *input*. Generation can be scaled in two ways:

![Ways to scale generation](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/scaling_generation.svg)
*Baseline: one short output. Scaling output length: more reasoning steps per attempt. Scaling search space: several candidate attempts, then one is selected.*

| Approach | What grows | Output |
|---|---|---|
| Baseline | Nothing | One short answer |
| Scale output length | Tokens per attempt | One long attempt (steps, then answer) |
| Scale search space | Number of candidate attempts | Many attempts; a selection step picks the answer |

Search-space scaling relies on decoding as search: sampling gives a different path through the token tree on every run.

### Parallel Scaling and Self-Consistency

#### Definitions

> **Parallel Scaling**: For a given prompt $x$, sampling multiple reasoning paths $z$.

> **Chain-of-Thought Rollout**: One sampled reasoning path for a prompt.

> **Self-Consistency**: Sampling multiple chain-of-thought rollouts and returning the most common final answer (majority voting).

Each token in each path is sampled, so the paths differ and produce several candidate answers $\hat{y}^1, \hat{y}^2, \dots$, some of which are the same.

![Parallel scaling](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/parallel_scaling.svg)
*From one prompt $x$, three reasoning paths are sampled. At every step, one token (amber) is drawn from the distribution, so paths diverge and end in answers $\hat{y}^1,\hat{y}^2,\hat{y}^3$.*

Parallel scaling leaves the question of how to pick one final answer. Self-consistency picks by majority vote.

**Motivation**: if multiple reasoning paths lead to the same answer, that answer is likely correct. Many approaches converging on one answer gives confidence.

The process:

1. Send the same question to the LLM $N$ times with temperature $> 0$.
2. Each rollout produces a reasoning path $z^i$ and final answer $\hat{y}^i$.
3. Discard (marginalise out) the reasoning paths and keep only the answers.
4. Return the most common answer.

$$
\hat{y} = \arg\max_{a} \sum_{i=1}^{N} \mathbb{1}\left[\hat{y}^i = a\right]
$$

```text
function SELF_CONSISTENCY(x, N):
    answers ← []
    for i ← 1 to N:
        z_i, y_i ← SAMPLE_COT(LLM, x)     # temperature > 0
        answers.append(y_i)
    return MOST_COMMON(answers)
```

Worked source example: Janet's ducks lay 16 eggs a day. She eats 3 for breakfast and bakes muffins with 4. She sells the rest at \$2 per egg. How much does she make per day?

![Self-consistency](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/self_consistency.svg)
*Greedy CoT gives one wrong path (\$14). Self-consistency samples diverse paths giving \$18, \$26 and \$18, and the majority vote returns the correct \$18.*

| Advantages | Disadvantages |
|---|---|
| Scales the search space, increasing the chance of finding a good solution | Only usable for short-answer tasks (maths, MCQs); majority voting over long free-form answers is not trivial |
| Avoids relying on one CoT that an invalid step could derail | The model can reach the **wrong answer through multiple reasoning paths** |
| Adds reasoning diversity without any further training | The model can reach the **right answer with invalid reasoning paths** |

The disadvantages show we need a way to evaluate the quality of answers or reasoning steps. This is what verifiers do.

### Verifiers

#### Definitions

> **Verifier**: A model or function that evaluates the quality, correctness or utility of each candidate solution generated by the search algorithm.

> **Reward Model**: A model trained on question-answer data (answers scored by humans) to assign a score to each candidate answer.

> **LLM-as-Verifier**: Using another LLM, prompted to assess answer quality, as the verifier.

> **Coverage**: Whether any of the generated samples is a correct solution.

> **Precision**: Whether the verifier can identify a correct solution among the samples.

> **Step-Level Verifier / Process Reward Model (PRM)**: A verifier that scores every step of a reasoning chain, rather than just the final answer.

A verifier scores each candidate answer, so candidates can be ranked and the best selected.

![Verifier scoring](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/verifier_scoring.svg)
*The LLM produces several thought-then-answer candidates; the verifier scores them (0.7, 0.3, 0.1) so the top one can be chosen.*

Verifying the final answer is simpler than verifying a whole reasoning path. Two families of verifiers do this:

| Verifier type | Examples |
|---|---|
| Off-the-shelf tools | Proof checkers for maths; compilers and unit tests for code |
| Verifier models | A trained reward model; another LLM prompted to judge the answer |

![Coverage and precision](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/coverage_and_precision.svg)
*Repeated sampling ("Large Language Monkeys", Brown et al. 2024): step 1 generates many candidate programs, step 2 uses a verifier (unit tests, proof checkers, majority voting) to pick one. Coverage and precision are two separate problems.*

Verifiers can also work at step level. A **process reward model** scores each intermediate step. This enables **step-level search**: the verifier guides a step-based search algorithm by keeping good partial paths and pruning bad ones.

![PRM step-level search](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/prm_step_search.svg)
*Every step is scored by the PRM (dashed box). Only high-scoring steps (teal) are expanded, and low-scoring ones (coral) are pruned until final-answer steps (squares) reach the answer.*

| Verifier granularity | Scores | Enables |
|---|---|---|
| Outcome (answer-level) | Only the final answer | Ranking complete candidates, e.g. best-of-N |
| Process (step-level, PRM) | Every reasoning step | Guiding a step-by-step search |

### Best-of-N

#### Definitions

> **Best-of-N**: Generating $N$ candidate outputs for an input, scoring each with a verifier's reward model, and returning the highest-scoring one.

> **Beam Search**: A search algorithm that keeps a fixed number of best partial sequences at each step (one possible generator for best-of-N candidates).

The process:

1. For input $x$, the LLM generates $N$ different output sequences $\{\hat{y}^1,\dots,\hat{y}^N\}$. Any search algorithm can produce them, e.g. sampling or beam search.
2. The verifier scores each answer with its reward model $r$ and selects the best one as the final answer:

$$
\hat{y} = \arg\max_{\hat{y}^i \in \{\hat{y}^1,\dots,\hat{y}^N\}} r\left(x, \hat{y}^i\right)
$$

```text
function BEST_OF_N(x, N, r):
    candidates ← [SAMPLE(LLM, x) for i ← 1 to N]
    return argmax over y in candidates of r(x, y)
```

![Best-of-N](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/best_of_n.svg)
*Three sampled paths end in $\hat{y}^1,\hat{y}^2,\hat{y}^3$ with rewards 0.91, 0.34 and 0.12; the argmax returns $\hat{y}^1$. The generator never learns: selection happens entirely at inference.*

| | Self-consistency | Best-of-N |
|---|---|---|
| Selection rule | Most common answer | Highest verifier score |
| Needs a verifier | No | Yes (reward model $r$) |
| Works for long free-form answers | Not easily | Yes, if the verifier can score them |
| Training of the generator | None | None |

### Combining Search Algorithms and Verifiers

#### Definitions

> **Search Algorithm**: The strategy used to explore the space of possible output sequences and generate a set of candidates; it can be simple sampling or a more sophisticated search technique.

> **Diverse Verifier Tree Search (DVTS)**: Running several independent PRM-guided tree searches (each from the question) and combining their final answers, which keeps the candidates diverse.

Test-time search has two components:

| Component | Role |
|---|---|
| Search algorithm | Explores the output space and generates candidates (sampling, beam search, tree search) |
| Verifier | Scores the candidates (tools, reward models, LLM judges, PRMs) |

These can be mixed and matched:

![Search strategies with PRM](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/search_strategies.svg)
*Best-of-N samples complete solutions and the PRM scores only the final steps. Beam search scores every step and expands only the selected ones. Diverse verifier tree search runs separate PRM-guided subtrees and combines their answers.*

| Strategy | When the PRM scores | Pruning |
|---|---|---|
| Best-of-N | Only complete solutions | None during generation; pick the best at the end |
| Beam search | Every intermediate step | Keep the top-scoring steps and expand those |
| Diverse verifier tree search | Every step, within each independent subtree | Per subtree, so different subtrees explore different paths |

Scaling test-time search improves performance on reasoning tasks. Coverage (pass@k, the fraction of problems where at least one of $k$ samples is correct) keeps rising as $k$ grows.

![Repeated sampling coverage](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/repeated_sampling_coverage.svg)
*On SWE-bench Lite, DeepSeek-Coder-V2 coverage rises from about 0.16 to 0.56 as samples grow to about 250, overtaking single-attempt GPT-4o (0.25) and single-attempt state of the art (0.43). Smaller Llama-3 models with many samples also beat single-attempt GPT-4o on MiniF2F, CodeContests, MATH and GSM8K. Curves are approximate.*

### Learning to Reason Through Training

#### Definitions

> **Supervised Finetuning (SFT) on Reasoning Traces**: Finetuning the model on reasoning traces written by humans.

> **Rejection Sampling**: Generating outputs, keeping only those the verifier accepts, finetuning on them, and repeating, so the LLM generates its own training data.

> **Reinforcement Learning (RL) for Reasoning**: Generating outputs, scoring every attempt with a verifier and continuously updating the model.

Inference-time search makes us choose a search algorithm and a verifier. The alternative is to **let the model learn how to reason**.

**Motivation**:

- Train the model to find good reasoning paths itself, so it *learns* what the search plus verifier did for us.
- Ideally, reduce reliance on multiple samples so that one sample is good enough.

| Training option | Data source | Learns from |
|---|---|---|
| SFT | Human-written reasoning traces | Human demonstrations |
| Rejection sampling | Model's own outputs that the verifier accepts | **Successes** only |
| RL | Every model attempt, scored by the verifier | Successes **and failures** |

### Reinforcement Learning With Verifiable Rewards (RLVR)

#### Definitions

> **RLVR (Reinforcement Learning with Verifiable Rewards)**: RL where the model generates its own attempts, each attempt is scored by a verifier, and the weights are updated to make high-scoring attempts more likely and low-scoring attempts less likely.

> **Verifiable Reward**: A reward computed by a program (e.g. unit tests or an answer checker), not by a learned model.

> **Policy $\pi_\theta$**: The LLM with parameters $\theta$, viewed as a distribution over next tokens.

> **Advantage**: How much better a rollout's reward is than the group's average reward.

RLVR only works when correctness can be checked by a program. That is why LLMs are so strong at maths and coding.

Generation is framed as an RL problem:

| RL concept | In LLM generation |
|---|---|
| State | Prompt plus the tokens generated so far |
| Action | Next token |
| Episode | One complete generation |
| Reward | Sparse, given only at the end |

![RLVR loop](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/rlvr_loop.svg)
*A prompt $x \sim D$ goes to the policy, which samples $G$ rollouts. The verifier gives rewards 1, 0, 1. Advantages relative to the mean (+0.33, −0.67, +0.33) drive a policy-gradient update.*

One RLVR update:

1. Sample a prompt $x \sim D$ from the training data.
2. Sample $G$ rollouts $z^i \to \hat{y}^i$ from the policy $\pi_\theta$.
3. Score each with the verifier (run the tests or check the answer) to get $r_i \in \{0,1\}$.
4. Compute each advantage relative to the group mean.
5. Apply a policy-gradient update: raise the probability of tokens in rollouts with $A_i > 0$ and lower it for $A_i < 0$.

$$
\bar{r} = \frac{1}{G}\sum_{j=1}^{G} r_j, \qquad A_i = r_i - \bar{r}
$$

With rewards $(1, 0, 1)$: $\bar{r} = 2/3 \approx 0.67$, giving $A = (+0.33,\ -0.67,\ +0.33)$.

```text
repeat:
    x ← SAMPLE(D)
    for i ← 1 to G:
        z_i, y_i ← ROLLOUT(π_θ, x)
        r_i ← VERIFIER(x, y_i)            # program: 0 or 1
    r_mean ← mean(r_1..r_G)
    for i ← 1 to G:
        A_i ← r_i − r_mean
        increase log π_θ(tokens of rollout i) in proportion to A_i
```

Properties of credit assignment:

- There is one reward for the whole attempt, with no per-step labels.
- Every token shares credit equally, including some useless tokens.
- Across millions of updates, useful reasoning steps still get rewarded.
- So the model **learns to reason by learning which steps lead to correct answers**.

### DeepSeek R1-Zero

#### Definitions

> **Accuracy Reward**: Reward for a correct final answer: the boxed answer is extracted and matched against the correct answer, or for code, compiled and run against test cases.

> **Format Reward**: Reward for placing the reasoning inside designated tags.

DeepSeek R1-Zero is RLVR applied with almost no human reasoning data:

1. Start from a pretrained model with **no instruction tuning or reasoning examples**.
2. For each problem, sample several CoT rollouts.
3. Apply RLVR using an accuracy reward and a format reward.

No human wrote a single reasoning trace. The reward is one bit from a program:

$$
r \in \{0, 1\}, \quad 0 = \text{wrong}, \; 1 = \text{right}
$$

What emerged:

- Response length grew during training, reaching thousands of tokens.
- Sophisticated reasoning strategies such as **backtracking, self-verification and re-deriving a result a second way** appeared without any demonstrations, simply because they correlate with being correct.
- It was the first time the o1 recipe was described openly and reproducibly, which is rare for this type of work.

The "aha moment" example. Question: if $a > 1$, find the sum of the real solutions of

$$
\sqrt{a - \sqrt{a + x}} = x
$$

Inside `<think>`, the model squares both sides, $a - \sqrt{a+x} = x^2$, then isolates and squares again:

$$
(a - x^2)^2 = a + x \;\Longrightarrow\; x^4 - 2ax^2 - x + (a^2 - a) = 0
$$

It then writes *"Wait, wait. Wait. That's an aha moment I can flag here."* and re-evaluates step by step from the original equation. That is learned self-verification and backtracking.

### From Self-Consistency to RLVR

The methods build on each other:

![From self-consistency to RLVR](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/02_Test_Time_Scaling/method_progression.svg)
*Adding a verifier turns self-consistency into best-of-N; adding training turns best-of-N into RLVR, moving reasoning from inference-time search into the weights.*

RLVR is how frontier LLM agents are trained:

- The **verifier is still used**, but as the RL training reward rather than an inference-time filter.
- **Reasoning is in the weights**, so one sample can produce a good reasoning trace.
- Self-consistency and best-of-N can still improve performance, but are not as necessary.

| Method | Verifier used for | Model updated? | Samples needed at inference |
|---|---|---|---|
| Self-consistency | None (majority vote) | No | Many |
| Best-of-N | Inference-time filter | No | Many |
| RLVR | Training reward | Yes | One can suffice |

Prescribed reading: Section 5.3 of *Foundations of Large Language Models* (Xiao & Zhu, arXiv 2501.09223). Optional: Chapter 6 of the same book and Lilian Weng's post on thinking (lilianweng.github.io/posts/2025-05-01-thinking/).
