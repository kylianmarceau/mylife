---
tags:
  - reasoning-in-ai
---

# LLM Preference Alignment and Reasoning

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Large Language Models  
> **Source**: [7-Alignment.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/LLM%27s/7-Alignment.pdf), Dr Jan Buys, slides 1-29 (slides from Jurafsky and Martin, Tatsunori Hashimoto, others as cited)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
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

---

## Core Content

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

![RLHF loop](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/07_Preference_Alignment_And_Reasoning/rlhf-loop.svg)

*Human preference pairs train a reward model. The policy samples responses to prompts; the reward model scores them; PPO updates the policy, with a KL penalty against a reference LM.*

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

### KL penalty and the full RLHF system

Optimizing purely for reward can produce nonsensical text that exploits the reward model. The full reward subtracts a **KL divergence** term to stay close to the pretrained model:

$$
R(s) = RM_\phi(s) - \beta \log\!\left(\frac{p_\theta^{RL}(s)}{p^{PT}(s)}\right)
$$

$\beta$ controls how strongly the policy is pulled back towards the pretrained (reference) model $p^{PT}$.

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

![Verifiable rewards](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/07_Preference_Alignment_And_Reasoning/verifiable-rewards.svg)

*For each problem, sample a group of solutions, verify the final answers, and use group-relative rewards to update the policy.*

In GRPO's standard form, the advantage of solution $i$ in a group with rewards $r_1, \dots, r_G$ is its reward normalized within the group:

$$
\hat{A}_i = \frac{r_i - \text{mean}(r_1, \dots, r_G)}{\text{std}(r_1, \dots, r_G)}
$$

![GRPO response length](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/07_Preference_Alignment_And_Reasoning/grpo-length.svg)

*During DeepSeek-R1-Zero training, the average response length rises steadily (with fluctuations): the model learns to "think" longer.*

### Test-time scaling

#### Definitions

> **Test-time scaling**: Improving performance by letting the model generate more reasoning ("thinking") tokens at inference time.

The longer the model "thinks" during inference, the more performance improves.

![Test-time scaling](../../../diagrams/CSC3043S-Reasoning%20in%20AI/LLMs/07_Preference_Alignment_And_Reasoning/test-time-scaling.svg)

*For Qwen3-235B-A22B, thinking mode improves on AIME'24, AIME'25, LiveCodeBench v5, and GPQA Diamond as the thinking budget grows (1K to 32K tokens), while non-thinking mode stays flat.*
