---
tags:
  - ai-systems
---

# Introduction III: Model, Harness, Benchmarks, and Deductive Agents

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3044S Artificial Intelligence: AI Systems  
> **Source**: [2026-CSC3044S-Lecture 3-Introduction (III).pdf](../../Sources/CSC3044S%20-%20AI%20Systems/2026-CSC3044S-Lecture%203-Introduction%20%28III%29.pdf), Geoff Nitschke, slides 1-58  
> **Generated**: 2026-10-01  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#From generated content to action|From generated content to action]]
  - [[#Harness components and control flow|Harness components and control flow]]
  - [[#What benchmark scores measure|What benchmark scores measure]]
  - [[#Goodhart effects, contamination, and context gaps|Goodhart effects, contamination, and context gaps]]
  - [[#Architecture families|Architecture families]]
  - [[#Deductive action selection|Deductive action selection]]
  - [[#Vacuum world: facts, rules, and execution|Vacuum world: facts, rules, and execution]]
  - [[#Limits of symbolic control and real-world sensing|Limits of symbolic control and real-world sensing]]

---

## Core Content

### From generated content to action

#### Definitions

> **Model**: A computational component that maps inputs to predictions or generated outputs.

> **Agentic loop**: Repeated model decisions, action execution, observation, and context updates until a stopping condition is reached.

> **Harness**: The infrastructure that gives a model tools, execution control, memory, permissions, and observation of results.

A restaurant booking example specifies a role, concise friendly speech, reservation time, party size, and preferences. Generating a booking script produces content; operating a phone interface and verifying a reservation adds action and feedback.

An autonomous vehicle likewise needs an observation-action loop for safe pickup and drop-off. A ride-request app is a narrower interface, even if its code was AI-generated.

The modern model-based view is “agent = model + harness.” This is an architectural shorthand, not a claim that all historical agents require an LLM.

| Model label in the lecture | Expansion | Typical role |
|---|---|---|
| LLM | Large language model | Process/generate language |
| VLM | Vision-language model | Combine image and language input |
| SLM | Small language model | Language tasks with a smaller model |
| MLM | Masked language model | Predict masked text |
| LAM | Large action model | Model actions or action-oriented outputs |
| LCM | Latent consistency model | Generative-model family named in the overview |
| SAM | Segment Anything Model | Image segmentation |
| MoE | Mixture of experts | Architecture routing computation among experts |

A fixed chain can call several models and tools while remaining developer-scripted. In the course's narrower modern usage, an agent chooses its next action inside the loop. A one-off browsing answer need not satisfy that definition.

### Harness components and control flow

#### Definitions

> **Context assembly**: Selecting and organizing information supplied to the model.

> **Tool**: An external operation exposed to the model through the harness.

> **Observability**: Making execution stages and results inspectable.

| Component | Responsibility |
|---|---|
| Context assembly | Curate data, queries, events, retrieved memories, prior results |
| Tool access | Manage definitions, credentials, connections, execution |
| Loop | Invoke model, handle actions, append outcomes, invoke again |
| Memory | Carry relevant state across iterations or sessions |
| Output validation | Check outputs before actions |
| Action routing | Execute, request review, or escalate according to rules |
| Permissions | Bound allowed operations |
| Observability | Record decisions, actions, outputs, failures |

![Harness components and control flow: model harness control flow](../../diagrams/CSC3044S-AI%20Systems/03_Introduction_III/model_harness_control_flow.svg)

*The harness surrounds the model with context, managed tools, validation, routing, and observation of execution.*

The model proposes a tool call; the harness performs it. Tool outputs then become observations for the next decision. Reliable execution depends on both components, along with prompts, tool definitions, context management, and evaluation.

```pseudocode
context = assemble_initial_context(task)
while budget_remains:
    decision = model(context)
    if decision requests completion:
        verify_completion()
        stop if complete
    validate_and_route(decision)
    result = execute_allowed_action(decision)
    context = update_context(context, decision, result)
```

This is a study reconstruction of the loop, with explicit budget and completion checks added to make failure handling clear. The lecture's engine/car analogy assigns response generation to the engine and execution control to the surrounding vehicle.

### What benchmark scores measure

#### Definitions

> **Benchmark**: A defined collection of tasks and a scoring procedure used to evaluate a capability.

> **Proxy**: A measurable stand-in for a broader quality of interest.

> **Saturation**: A condition in which scores become too high or compressed to distinguish systems usefully.

> **Selection bias**: Drawing conclusions from tests selected to favor a system or viewpoint.

> **State of the art (SOTA)**: The best reported performance under specified evaluation conditions.

> [!important] <span style="color: #b89aff">Compare the whole evaluation setup</span>
> A benchmark score belongs to a **model-harness-task configuration**. Comparing scores requires model version, agent/harness, prompts, tool access, task set, time/compute budget, scoring rules, and run variability.  

| Benchmark in the lecture | Capability emphasized |
|---|---|
| Terminal-Bench | Multi-step terminal work |
| FrontierMath | Research-level mathematics |
| GPQA Diamond | Difficult graduate-level scientific questions |
| SWE-bench Verified | Fixing existing repository issues |
| AIME | Competition mathematics |
| MCP-Atlas | Tool workflows across MCP servers |
| HLE, Humanity's Last Exam | Broad expert-level questions |
| Codeforces | Competitive programming, reported using ratings |
| ProgramBench | Building software artifacts from scratch |

The snapshot table associates examples such as FrontierMath $89.0\%$, GPQA $95.3\%$, SWE-bench Verified $95.0\%$, AIME $99.2\%$, MCP-Atlas $88.1\%$, and HLE $65.0\%$ with different systems. These are lecture examples, not interchangeable measures or verified current rankings.

Other screenshot examples report roughly $58.2\%$ for a leading Terminal-Bench setup, $76.80\%$ for a SWE-bench example, and $4.5\%$ for a ProgramBench example. They use different tasks, dates, and configurations. In particular, the two SWE-bench numbers should not be silently treated as the same experiment.

The SWE-bench Verified set has 500 human-filtered instances. A score reports the fraction of tested issues resolved; it does not certify unrestricted software design. ProgramBench targets from-scratch artifacts. [Official SWE-bench descriptions](https://www.swebench.com/).

| Failure of interpretation | Why it matters | Better comparison |
|---|---|---|
| $90\%$ on one task set assumed equal to $90\%$ on another | Tasks differ | Inspect tasks and scoring |
| High score assumed to imply every capability | Evaluation is narrow | Test the actual target workflow |
| Saturation ignored | Ceiling obscures distinctions | Harder or more discriminating tasks |
| Favorable benchmark selected alone | Weaknesses are hidden | Diverse relevant evaluations |
| Harness omitted | Tools and execution affect scores | Hold setup fixed or report differences |

A score above roughly $90\%$ is a lecture warning about saturation, not a universal statistical cutoff.

### Goodhart effects, contamination, and context gaps

#### Definitions

> **Goodhart effect**: A measure may become less useful as a proxy when optimized as a target.

> **Benchmark contamination**: Evaluation questions or solutions overlap with information used during training or tuning.

> **Distribution shift**: A difference between development/evaluation conditions and deployment conditions.

Goodhart's familiar formulation is: “When a measure becomes a target, it ceases to be a good measure.” Benchmark success is evidence about measured tasks; its broader meaning depends on test design and overlap with training.

![Goodhart effects, contamination, and context gaps: benchmark goodhart feedback](../../diagrams/CSC3044S-AI%20Systems/03_Introduction_III/benchmark_goodhart_feedback.svg)

*Optimizing a benchmark can raise a score without an equivalent improvement in the broader capability.*

Popular examples at risk of exposure include MMLU, AIME, GSM8K, and HumanEval. Online availability is a risk factor; it is not proof that a particular model memorized every solution.

| Mitigation | Mechanism | Remaining issue |
|---|---|---|
| Held-out problems | Keep evaluation material separate from training | Access and tuning history must be controlled |
| Refreshed benchmarks | Add harder questions or answer choices, as in MMLU-Pro | New material can eventually become public |
| Dynamic benchmarks | Add new tasks over time, as in LatestEval | Difficulty and comparability must be maintained |
| Deployment tests | Include realistic workflows and unusual cases | Requires representative cases and reliable scoring |
| Local-context evaluation | Test relevant languages, infrastructure, domain constraints | Broad benchmark averages may hide subgroup failures |

The FrontierMath example describes new unpublished problems and an explicitly held-out subset. The key principle is separation from training and tuning, rather than reliance on a fixed historical problem count.

The African/low-resource gap concerns relevance: evaluation may miss local languages, data scarcity, infrastructure, and context. Likewise, a VRP optimizer may excel on known maps but fail on unseen customer patterns.

### Architecture families

#### Definitions

> **Agent architecture**: A decomposition into modules and interactions specifying how observations and internal state determine actions and future state.

Maes emphasizes methodology and interactions; Kaelbling emphasizes concrete modules and their data/control flow. Both require more than a list of algorithms.

| Family | Main mechanism | Examples |
|---|---|---|
| Reactive | Tight perception-action coupling | Subsumption, Boids, stigmergy |
| Deliberative | World model and reasoning/planning | BDI, agent-oriented programming, deductive agents |
| Neural/cognitive | Learned representations and decisions | ANN-based agents |
| Hybrid | Combine control styles | Model plus harness; layered controllers |
| Multi-agent | Several interacting decision-makers | Cooperative/adversarial systems |

Multi-agent describes composition, and rationality describes decision quality. Neither is a competing single-agent control style.

![Architecture families: architecture families](../../diagrams/CSC3044S-AI%20Systems/03_Introduction_III/architecture_families.svg)

*The architecture overview spans control mechanisms and multi-agent composition; rationality must be assessed separately.*

### Deductive action selection

#### Definitions

> **Deductive agent**: An agent selecting actions by proving statements from a logical description of the world and action rules.

> **Logical database**: A set of facts describing the current world, denoted $\Delta$.

> **Theory**: The rules used for inference, denoted $p$.

> **Predicate**: A logical expression describing a property or relation.

| Symbol | Meaning |
|---|---|
| $\Delta$ | Current-world facts |
| $p$ | Action-selection rules |
| $Ac$ | Available actions |
| $\Delta\vdash_p\Phi$ | Statement $\Phi$ is provable using the facts and rules |
| $\operatorname{Do}(a)$ | Action $a$ is prescribed |
| $\Delta\nvdash_p\neg\operatorname{Do}(a)$ | Prohibition of $a$ is not provable |

The controller first tries to find an explicitly prescribed action. If none is found, it tries an action not ruled out. If both searches fail, it returns no action.

```pseudocode
for each action in available_actions:
    if prescribed(action) is provable:
        return action
for each action in available_actions:
    if prohibited(action) is not provable:
        return action
return null
```

Formally, the two tests are $\Delta\vdash_p\operatorname{Do}(a)$ and $\Delta\nvdash_p\neg\operatorname{Do}(a)$. The second is **not** a proof that the action is safe or beneficial. Action iteration order can influence the returned choice when several actions qualify.

### Vacuum world: facts, rules, and execution

The robot must remove all dirt in a three-by-three grid.

| $y\backslash x$ | $0$ | $1$ | $2$ |
|---|---|---|---|
| $2$ | Dirt | Dirt | Clean |
| $1$ | Clean | Clean | Clean |
| $0$ | Robot, facing north | Clean | Clean |

*The initial grid has dirt at $(0,2)$ and $(1,2)$, with the robot at $(0,0)$.*

| Predicate/action | Meaning |
|---|---|
| $\operatorname{In}(x,y)$ | Robot occupies position $(x,y)$ |
| $\operatorname{Dirt}(x,y)$ | Dirt is at $(x,y)$ |
| $\operatorname{Facing}(d)$ | Robot faces direction $d$ |
| $\operatorname{turn}$ | Turn right |
| $\operatorname{forward}$ | Move forward |
| $\operatorname{suck}$ | Remove dirt at the current cell |

$$
Ac=\{\operatorname{turn},\operatorname{forward},\operatorname{suck}\}.
$$

The illustrated positional rules are:

$$
\begin{aligned}
\operatorname{In}(0,0)\land\operatorname{Facing}(\mathrm{north})\land\neg\operatorname{Dirt}(0,0)
&\to\operatorname{Do}(\operatorname{forward}),\\
\operatorname{In}(0,1)\land\operatorname{Facing}(\mathrm{north})\land\neg\operatorname{Dirt}(0,1)
&\to\operatorname{Do}(\operatorname{forward}),\\
\operatorname{In}(0,2)\land\operatorname{Facing}(\mathrm{north})\land\neg\operatorname{Dirt}(0,2)
&\to\operatorname{Do}(\operatorname{turn}),\\
\operatorname{In}(0,2)\land\operatorname{Facing}(\mathrm{east})
&\to\operatorname{Do}(\operatorname{forward}).
\end{aligned}
$$

The source also gives a reset instruction at $(0,2)$. Taken literally without a condition, resetting there conflicts with continuing east. It is an underspecified part of the example, rather than a complete coverage algorithm.

A natural **supplementary cleaning rule**, needed to connect the dirt-removal goal with the pictured suction action, is:

$$
\operatorname{In}(x,y)\land\operatorname{Dirt}(x,y)
\to\operatorname{Do}(\operatorname{suck}).
$$

Give cleaning suitable priority and update the database after each action. The displayed four rules alone do not establish cleaning of the full grid.

![Vacuum world: facts, rules, and execution: vacuum world transitions](../../diagrams/CSC3044S-AI%20Systems/03_Introduction_III/vacuum_world_transitions.svg)

*The vacuum-world transition sketch branches into northward and eastward actions. Only suction at a dirty cell changes the dirt set.*

The alternative branches in the example are possible transitions, rather than one mandatory sequential plan. Suction removes the dirt fact at the current location but leaves other dirt facts unchanged.

### Limits of symbolic control and real-world sensing

A logical controller needs accurate facts before reasoning begins. Converting a camera image to $\operatorname{Dirt}(0,1)$ requires perception, not just a theorem prover.

1. Capture observations.
2. Identify relevant features or objects.
3. Translate them into facts and uncertainty estimates.
4. Update the world model.
5. Reason and act before that model becomes stale.

Key problems include difficult transduction, changing environments, and inference cost. General first-order validity is undecidable; unrestricted proof search is not guaranteed to terminate on all inputs. Propositional **SAT** is NP-complete, while propositional entailment in general is coNP-complete. This does not mean every small condition-action rule check is NP-complete.

Vacuum robots provide a practical alternative using continuous feedback from distance, cliff, and bump sensors. Some also use maps and planning. The architecture should match the sensing and task requirements rather than force all raw observations into unrestricted logic.
