---
tags:
  - ai-systems
  - flashcards
qard-deck: "AI Systems"
qard-topic: "03 — Introduction III: Model, Harness, Benchmarks, and Deductive Agents"
---

# 03 — Introduction III: Model, Harness, Benchmarks, and Deductive Agents

**Source note:** [Introduction III: Model, Harness, Benchmarks, and Deductive Agents](../03_Introduction_III.md)

Exam recall cards covering concepts, definitions, methods, and qualifications. Worked examples are omitted; general proof methods are retained.

## Contents

- [[#Core Content|Core Content]]
  - [[#From generated content to action|From generated content to action]]
  - [[#Harness components and control flow|Harness components and control flow]]
  - [[#What benchmark scores measure|What benchmark scores measure]]
  - [[#Goodhart effects, contamination, and context gaps|Goodhart effects, contamination, and context gaps]]
  - [[#Architecture families|Architecture families]]
  - [[#Deductive action selection|Deductive action selection]]
  - [[#General principles from symbolic execution|General principles from symbolic execution]]
  - [[#Limits of symbolic control and real-world sensing|Limits of symbolic control and real-world sensing]]

## Core Content

### From generated content to action

<!-- qard-id: ais-4d0c3fe7da983efd6df3 -->
> [!qard]- What is a model in an agent system?
> A computational component mapping inputs to predictions or generated outputs.

<!-- qard-id: ais-ddbc74087db189cb535d -->
> [!qard]- What is an agentic loop?
> Repeated model decisions, action execution, observation, and context updates until a stopping condition.

<!-- qard-id: ais-944e18230eb1f90a36d0 -->
> [!qard]- What is a harness?
> Infrastructure providing tools, execution control, memory, permissions, and observation of results around a model.

<!-- qard-id: ais-6c38e2dab22830686c7c -->
> [!qard]- What distinguishes generating a task script from carrying out the task?
> Execution adds actions in the real interface and feedback verifying the resulting state; producing the script alone supplies content.

<!-- qard-id: ais-88ea0af7fce828a7120c -->
> [!qard]- What does “agent = model + harness” mean, and what is its scope?
> A shorthand for modern model-based agent architecture; it does not mean every historical agent requires an LLM.

<!-- qard-id: ais-9808a7f4c3bccb4f877e -->
> [!qard]- Can a multi-model tool chain still be developer-scripted rather than agentic?
> Yes. In the course’s narrower modern usage, an agent chooses its next action within the loop; a fixed chain or one-off browsing answer need not do so.

<!-- qard-id: ais-dde0bf8fcf7e2d6441f3 -->
> [!qard]- What do LLM, VLM, and SLM stand for?
> Large language model, vision-language model, and small language model; they process language, combine image/language, and use smaller language models respectively.

<!-- qard-id: ais-75fdf1432782b4e09986 -->
> [!qard]- What do MLM and LAM stand for in this lecture?
> Masked language model predicts masked text; large action model models actions or action-oriented outputs.

<!-- qard-id: ais-107d58a1f1a8bec20d67 -->
> [!qard]- What do LCM, SAM, and MoE stand for in this lecture?
> Latent consistency model, Segment Anything Model, and mixture of experts; a generative family, image segmentation model, and expert-routing architecture respectively.

### Harness components and control flow

<!-- qard-id: ais-c028be51b814b24b17d4 -->
> [!qard]- What is context assembly?
> Selecting and organizing information supplied to the model, such as data, queries, events, memories, and prior results.

<!-- qard-id: ais-f16933d3212b32d291fe -->
> [!qard]- What is a tool in an agent harness?
> An external operation exposed to the model; the harness manages definitions, credentials, connections, and execution.

<!-- qard-id: ais-ef0599d45f6cd4de89c1 -->
> [!qard]- What is observability?
> Making execution stages and results inspectable by recording decisions, actions, outputs, and failures.

<!-- qard-id: ais-9718ae37db53894b5203 -->
> [!qard]- What does the harness loop component do?
> Invoke the model, handle selected actions, append outcomes, and invoke the model again as needed.

<!-- qard-id: ais-9ce53df90e1b2b4d3edd -->
> [!qard]- What is the role of memory in a harness?
> Carry relevant state across iterations or sessions.

<!-- qard-id: ais-7129845568fcf363d671 -->
> [!qard]- How do output validation, action routing, and permissions differ?
> Validation checks outputs before acting; routing executes, requests review, or escalates according to rules; permissions bound allowed operations.

<!-- qard-id: ais-f1f97717fe0a65a4cbbe -->
> [!qard]- Does the model itself execute its proposed tool call?
> The model proposes it; the harness performs the operation and returns results as observations for the next decision.

<!-- qard-id: ais-45fd70784b1aec4bb793 -->
> [!qard]- What factors jointly determine reliable agent execution?
> Model and harness, prompts, tool definitions, context management, and evaluation.

<!-- qard-id: ais-07a1d3a275214c9d9ef9 -->
> [!qard]- What budget and completion checks are included in the reconstructed agent loop?
> Continue while budget remains, verify claimed completion, validate and route actions, execute allowed actions, and update context with outcomes.

<!-- qard-id: ais-5a6a6e26a31b8ee889fd -->
> [!qard]- Why verify completion instead of trusting a completion request?
> The requested outcome may not actually exist; execution-based evidence should determine whether the task is finished.

### What benchmark scores measure

<!-- qard-id: ais-215972b14a66cf3db2f5 -->
> [!qard]- What is a benchmark?
> A defined task collection and scoring procedure evaluating a capability.

<!-- qard-id: ais-ed311c90be58ad4fcf43 -->
> [!qard]- What is a proxy?
> A measurable stand-in for a broader quality of interest.

<!-- qard-id: ais-35832c6705810413f443 -->
> [!qard]- What is benchmark saturation?
> Scores become too high or compressed to distinguish systems usefully.

<!-- qard-id: ais-62e6a7e0684864bea466 -->
> [!qard]- What is selection bias in benchmark reporting?
> Drawing conclusions from tests selected to favor a system or viewpoint.

<!-- qard-id: ais-353bacc253b4f5c05de1 -->
> [!qard]- What does state of the art mean?
> Best reported performance under specified evaluation conditions.

<!-- qard-id: ais-9d8bb3991ef40408bab5 -->
> [!qard]- What configuration details are needed to compare agent benchmark scores?
> Model version, harness, prompts, tool access, task set, time/compute budget, scoring, and variability across runs.

<!-- qard-id: ais-d23639588f5a00eed026 -->
> [!qard]- What does Terminal-Bench emphasize?
> Multi-step terminal work.

<!-- qard-id: ais-83d4aa7be2885ccb6aa4 -->
> [!qard]- What do FrontierMath, AIME, and GPQA Diamond emphasize?
> Research-level mathematics, competition mathematics, and difficult graduate-level scientific questions respectively.

<!-- qard-id: ais-f8180e3b9806376b5e50 -->
> [!qard]- How do SWE-bench Verified and ProgramBench differ?
> SWE-bench Verified tests fixing existing repository issues; ProgramBench tests building software artifacts from scratch.

<!-- qard-id: ais-7995e857e1d4d20fb2bd -->
> [!qard]- What do MCP-Atlas, HLE, and Codeforces measure?
> Tool workflows across MCP servers, broad expert-level questions, and competitive programming reported through ratings respectively.

<!-- qard-id: ais-f42625cab067e210a2cf -->
> [!qard]- What does a SWE-bench Verified score establish?
> Fraction of tested issues resolved among a set of $500$ human-filtered instances; it does not certify unrestricted software-design ability.

<!-- qard-id: ais-5a2366d955b2c24f0d3f -->
> [!qard]- Why are equal percentages on different benchmarks not interchangeable?
> Tasks, scoring, dates, and configurations differ; a percentage measures success only under its specific setup.

<!-- qard-id: ais-059378de5247ad5588ab -->
> [!qard]- Why should different SWE-bench screenshot numbers not be merged into one experiment?
> They may use different systems, dates, and configurations despite a similar benchmark name.

<!-- qard-id: ais-9d17b7949f5890ebecb1 -->
> [!qard]- Why can a high benchmark score fail to establish broad capability?
> Evaluation may be narrow or saturated, selected favorably, or aided by a particular harness; test the actual target workflow.

<!-- qard-id: ais-08336c2a4ba022438f69 -->
> [!qard]- Is roughly $90\%$ a universal statistical threshold for saturation?
> No. It is a warning used in the lecture; saturation depends on the task set and score distribution.

### Goodhart effects, contamination, and context gaps

<!-- qard-id: ais-6c76b68b50bbcadf9ce3 -->
> [!qard]- What is a Goodhart effect?
> Optimizing a measure as a target can make it less useful as a proxy for the broader desired quality.

<!-- qard-id: ais-492a7abf7b8b71d03a0d -->
> [!qard]- How can benchmark optimization improve scores without equivalent general improvement?
> Training or tuning can specialize behavior to measured tasks and their shortcuts rather than the wider deployment capability.

<!-- qard-id: ais-16add1ea6abf98cbde33 -->
> [!qard]- What is benchmark contamination?
> Evaluation questions or solutions overlap with material used in training or tuning.

<!-- qard-id: ais-9d6282e5ea44382eab54 -->
> [!qard]- What is distribution shift?
> Development or evaluation conditions differ from deployment conditions.

<!-- qard-id: ais-ac7a89a89de962169f2e -->
> [!qard]- Does public availability prove a model memorized all benchmark solutions?
> No. It creates exposure risk; memorization requires additional evidence.

<!-- qard-id: ais-d0eef42dcb3060f1e10b -->
> [!qard]- Which publicly available benchmark examples are listed as exposure risks?
> MMLU, AIME, GSM8K, and HumanEval.

<!-- qard-id: ais-2ccb1f73b30b57e3a7c1 -->
> [!qard]- What is the principle behind held-out evaluation?
> Keep evaluation problems separate from training and tuning, controlling access and tuning history.

<!-- qard-id: ais-c7955be152bbc08a3e80 -->
> [!qard]- How do refreshed and dynamic benchmarks address contamination?
> Refreshed benchmarks add harder/new material, such as MMLU-Pro; dynamic benchmarks add tasks over time, such as LatestEval. Exposure and comparability still require management.

<!-- qard-id: ais-1190168498a0bcd95d92 -->
> [!qard]- What do realistic deployment tests add beyond generic benchmarks?
> Representative workflows and unusual cases under reliable scoring.

<!-- qard-id: ais-b4d8fbd5bc1bd995fda0 -->
> [!qard]- Why evaluate local languages, infrastructure, and domain constraints?
> Broad averages can hide failures relevant to African or low-resource settings and other local contexts.

<!-- qard-id: ais-1aaff5816127c6fc2cde -->
> [!qard]- Why is known-map success insufficient to evaluate a VRP optimizer?
> Unseen customer patterns can expose distribution shift and weak generalization.

### Architecture families

<!-- qard-id: ais-4ff1ba0f6cc3ba30a0d6 -->
> [!qard]- What is an agent architecture?
> A decomposition into modules and interactions specifying how observations and internal state determine actions and future state.

<!-- qard-id: ais-43f5b347aed5a67d430e -->
> [!qard]- How do Maes and Kaelbling’s architectural emphases complement each other?
> Maes emphasizes methodology and interactions; Kaelbling emphasizes concrete modules and data/control flow. An architecture needs both.

<!-- qard-id: ais-0f68f919536cf760393b -->
> [!qard]- What mechanisms define reactive, deliberative, and neural/cognitive families?
> Reactive tightly couples perception and action; deliberative uses a world model and reasoning/planning; neural/cognitive learns representations and decisions.

<!-- qard-id: ais-286c3a6a7b13024331b5 -->
> [!qard]- What are hybrid and multi-agent architectures?
> Hybrid combines control styles; multi-agent has several interacting decision-makers, potentially cooperative or adversarial.

<!-- qard-id: ais-72be69f19ee038f01e82 -->
> [!qard]- Are multi-agent composition and rationality competing control styles?
> No. Multi-agent describes composition, while rationality describes decision quality; neither is a single-agent control mechanism.

### Deductive action selection

<!-- qard-id: ais-007239dddc672d536168 -->
> [!qard]- What is a deductive agent?
> An agent selecting actions by proving statements from logical world facts and action-selection rules.

<!-- qard-id: ais-cbe1c832ad8c03099834 -->
> [!qard]- What do $\Delta$, $p$, $Ac$, and a predicate denote?
> $\Delta$: current-world facts; $p$: inference/action rules; $Ac$: available actions; a predicate: a logical property or relation.

<!-- qard-id: ais-5cddafba4c4ee69d78df -->
> [!qard]- What does $\Delta\vdash_p\Phi$ mean?
> Statement $\Phi$ is provable from database $\Delta$ using theory $p$.

<!-- qard-id: ais-fd517eeead57f0e649ad -->
> [!qard]- What does $\operatorname{Do}(a)$ express?
> The action $a$ is prescribed.

<!-- qard-id: ais-1dfc65b729a51c68cd38 -->
> [!qard]- What is the two-pass deductive action-selection procedure?
> First return an action with provable $\operatorname{Do}(a)$; if none, return an action whose prohibition is not provable; if neither pass succeeds, return null.

<!-- qard-id: ais-3a7d21934790cd59d4aa -->
> [!qard]- What formal tests are used in the two deductive-selection passes?
> $\Delta\vdash_p\operatorname{Do}(a)$, then $\Delta\nvdash_p\neg\operatorname{Do}(a)$.

<!-- qard-id: ais-b73ef6f997ef46fee98e -->
> [!qard]- Why is failure to prove prohibition not proof of safety?
> Lack of a prohibition proof does not establish that an action is safe or beneficial; facts or rules may be incomplete.

<!-- qard-id: ais-761aac3c604ba984b345 -->
> [!qard]- Why can action iteration order influence deductive selection?
> The procedure returns the first qualifying action when several actions meet a test.

### General principles from symbolic execution

<!-- qard-id: ais-ff1ecfb9936a71a44737 -->
> [!qard]- What must a logical controller update after executing an action?
> Its database must reflect the resulting world state; otherwise later reasoning can rely on stale facts.

<!-- qard-id: ais-016891e27b8699e3f585 -->
> [!qard]- Why do condition-action rules need priorities and complete goal coverage?
> Multiple rules can conflict, and a partial rule sketch need not achieve the full goal; priorities and action effects must be specified.

<!-- qard-id: ais-dc18efc7e3f681c58729 -->
> [!qard]- Why should possible transition branches not automatically be read as one sequential plan?
> A transition diagram can represent alternatives; an actual execution follows selected actions and updated states.

### Limits of symbolic control and real-world sensing

<!-- qard-id: ais-b7c6fadb97253dc70441 -->
> [!qard]- Why does a theorem prover alone not turn camera input into correct world facts?
> Perception and transduction must identify relevant features and convert them into factual and uncertainty representations first.

<!-- qard-id: ais-44495694a650dfe087ec -->
> [!qard]- What observation-to-symbolic-action pipeline is described?
> Capture observations, identify features/objects, translate into facts and uncertainty estimates, update the model, then reason and act before it becomes stale.

<!-- qard-id: ais-0054e1e0b7cf1fd6a04d -->
> [!qard]- What are key limits of symbolic control?
> Difficult transduction, changing environments, and inference cost.

<!-- qard-id: ais-cdc83040751b27fde220 -->
> [!qard]- What undecidability qualification applies to general first-order reasoning?
> General first-order validity is undecidable; unrestricted proof search need not terminate on every input.

<!-- qard-id: ais-361a1a9daaecd5071c12 -->
> [!qard]- How do general propositional SAT and entailment differ in complexity?
> SAT is NP-complete; general propositional entailment is coNP-complete. This does not classify every small condition-action check as NP-complete.

<!-- qard-id: ais-01158bb1a95a5e20902a -->
> [!qard]- What alternative can continuous sensor feedback offer?
> Reactive sensing can handle distance, cliffs, and collisions, optionally combined with maps/planning; architecture should match sensing and task needs.
