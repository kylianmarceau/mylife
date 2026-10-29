---
tags:
  - ai-systems
  - flashcards
qard-deck: "AI Systems"
qard-topic: "04 — Agent Architectures: Deductive Control, Hybrid Layers, and Grounding"
---

# 04 — Agent Architectures: Deductive Control, Hybrid Layers, and Grounding

**Source note:** [Agent Architectures: Deductive Control, Hybrid Layers, and Grounding](../04_Agent_Architectures.md)

Exam recall cards covering concepts, definitions, methods, and qualifications. Worked examples are omitted; general proof methods are retained.

## Contents

- [[#Core Content|Core Content]]
  - [[#Architecture as modules and interactions|Architecture as modules and interactions]]
  - [[#Deductive action selection|Deductive action selection]]
  - [[#General principles from symbolic execution|General principles from symbolic execution]]
  - [[#Limits of symbolic control and real-world sensing|Limits of symbolic control and real-world sensing]]
  - [[#Hybrid control and layer organization|Hybrid control and layer organization]]
  - [[#TouringMachines and coordination|TouringMachines and coordination]]
  - [[#Embodiment and the symbol-grounding problem|Embodiment and the symbol-grounding problem]]

## Core Content

### Architecture as modules and interactions

<!-- qard-id: ais-f0012c5f2181a62fdca7 -->
> [!qard]- What is an agent architecture?
> Components and their interaction methodology determining actions and future internal state from sensors and current state.

<!-- qard-id: ais-5244e641906f2ee3dfb2 -->
> [!qard]- Why must an architecture describe more than its component list?
> Data flow, control flow, and coordination between components determine behavior; Maes’ methodological and Kaelbling’s module-based definitions are complementary.

<!-- qard-id: ais-b8028ff184669339d80f -->
> [!qard]- How do reactive and deliberative control differ?
> Reactive control tightly couples observations to action; deliberative control represents the world and plans or reasons before selecting actions.

<!-- qard-id: ais-4d3a5da4ef6700c18c17 -->
> [!qard]- What components distinguish typical reactive and deliberative paths?
> Reactive: sensors, condition-action behavior, effectors. Deliberative: sensors, world model, planner, executor, effectors.

<!-- qard-id: ais-d5ab8d87bffd81d0ccd0 -->
> [!qard]- How do hybrid, neural/cognitive, and multi-agent families differ?
> Hybrid combines control styles; neural/cognitive uses learned perception or decisions; multi-agent concerns interaction among several agents.

<!-- qard-id: ais-ba72b70317cb775c813f -->
> [!qard]- Does choosing a neural, hybrid, or other family establish rational behavior?
> No. Decision quality depends on information, objectives, and the controller’s actual performance.

<!-- qard-id: ais-89252c5d7ba89ea436a1 -->
> [!qard]- What can a modern harness combine with model decisions?
> Deterministic validation, context assembly, tools, permissions, and action routing; this does not imply every LLM product has identical internals.

### Deductive action selection

<!-- qard-id: ais-1ac00aff6fac64008f82 -->
> [!qard]- What is a deductive agent?
> An agent selecting actions by proving logical statements from world facts and action rules.

<!-- qard-id: ais-8cef9206b084b8be7262 -->
> [!qard]- What are the logical database, theory, and predicate?
> Database $\Delta$ contains current facts; theory $p$ contains inference rules; predicates express properties or relations.

<!-- qard-id: ais-3dd238b0a427ff69b130 -->
> [!qard]- What do $Ac$, $\Delta\vdash_p\Phi$, and $\operatorname{Do}(a)$ mean?
> Available actions, provability of $\Phi$ from facts/rules, and prescription of action $a$ respectively.

<!-- qard-id: ais-66e0b96b1ba7e8628709 -->
> [!qard]- How does the deductive controller select an action?
> Search for a provably prescribed action; otherwise search for an action without provable prohibition; if none qualifies, return null.

<!-- qard-id: ais-0b0962bb25e0e55f78e3 -->
> [!qard]- What distinguishes the two formal action-selection tests?
> First require $\Delta\vdash_p\operatorname{Do}(a)$; second require $\Delta\nvdash_p\neg\operatorname{Do}(a)$, merely absence of a prohibition proof.

<!-- qard-id: ais-acec27c7484f02ea1739 -->
> [!qard]- Why does the fallback action-selection test not guarantee safety?
> Missing knowledge or incomplete inference can prevent proving a prohibition even when an action is unsafe or unhelpful.

<!-- qard-id: ais-c4abbaa36f5f08ecdf83 -->
> [!qard]- Why does action iteration order matter when several actions qualify?
> The algorithm returns the first qualifying action rather than optimizing among all qualifying choices.

### General principles from symbolic execution

<!-- qard-id: ais-f6a0e55dabec8afe190c -->
> [!qard]- Why must a rule-based controller specify goal-achieving actions as well as movement?
> Rules supporting only partial behavior do not establish completion of the full task; all required goal effects must be represented.

<!-- qard-id: ais-2aac9082296b94baaf27 -->
> [!qard]- Why are priorities and post-action database updates essential?
> Priorities resolve competing prescriptions; updates ensure future decisions reflect action effects rather than obsolete facts.

<!-- qard-id: ais-55aa8ed3a71e6463275a -->
> [!qard]- How should alternative branches in a transition sketch be interpreted?
> As possible transitions, rather than necessarily one mandatory sequential execution.

### Limits of symbolic control and real-world sensing

<!-- qard-id: ais-ac3942c2930fdbd061d2 -->
> [!qard]- What is needed before a logical controller can reason from images?
> Perception must identify relevant features or objects and transduce them into facts and uncertainty estimates.

<!-- qard-id: ais-3531ad5d98f90edf1df1 -->
> [!qard]- What is the perception-to-action pipeline for symbolic control?
> Capture observations, identify relevant content, translate to facts/uncertainty, update the model, then reason and act before that model becomes stale.

<!-- qard-id: ais-e584e484b9bc0cc32c0d -->
> [!qard]- What limits symbolic control in real environments?
> Difficult transduction, changing conditions, and inference cost.

<!-- qard-id: ais-9af57b608d8fe334337b -->
> [!qard]- What is the status of general first-order validity and unrestricted proof search?
> General first-order validity is undecidable; unrestricted proof search is not guaranteed to terminate for every input.

<!-- qard-id: ais-505c3bfa4022a6ed5864 -->
> [!qard]- How are general propositional SAT and entailment classified?
> SAT is NP-complete and entailment is coNP-complete, without implying every small rule check has that complexity.

<!-- qard-id: ais-2b67e70c8d10689fa342 -->
> [!qard]- Why might continuous sensor feedback be preferable to unrestricted logical reasoning for some robot behaviors?
> Distance, cliff, and bump feedback can support timely local reactions; maps and planning can be added when appropriate.

### Hybrid control and layer organization

<!-- qard-id: ais-4820d79b355676e2d397 -->
> [!qard]- What is a hybrid architecture?
> An architecture combining deliberative and reactive components with coordination between them.

<!-- qard-id: ais-9cb017e7ffa4e77d9b77 -->
> [!qard]- What roles do hybrid deliberative and reactive components serve?
> Deliberation uses symbolic or learned reasoning for longer-term choices; reactive control handles events without waiting for expensive reasoning.

<!-- qard-id: ais-e1c690b9fb2411cdf919 -->
> [!qard]- What is horizontal layering?
> Several layers receive sensor information in parallel and can propose actions directly.

<!-- qard-id: ais-70792b940ddd2d8ebb54 -->
> [!qard]- What is vertical layering?
> Information or control passes through layers sequentially, potentially with upward processing and a downward action path.

<!-- qard-id: ais-348ee040c409fdee6a62 -->
> [!qard]- What is the main coordination issue in horizontal layering?
> Multiple layers can propose conflicting actions, requiring arbitration.

<!-- qard-id: ais-ed664eaf3ca98f8f7f4d -->
> [!qard]- What is the main coordination issue in vertical layering?
> Serial dependencies and processing delays; variants use one-pass or two-pass sensor/action flow.

<!-- qard-id: ais-efe4f1a8bda28628559c -->
> [!qard]- Do horizontal and vertical refer simply to diagram placement?
> No. They describe information and control routing between layers.

### TouringMachines and coordination

<!-- qard-id: ais-fb7bcdfd784a5225618f -->
> [!qard]- What is TouringMachines?
> Ferguson’s hybrid architecture with modeling, planning, and reactive layers inside a shared control framework.

<!-- qard-id: ais-b82a637561be630a4ce5 -->
> [!qard]- What does a mediator or control framework do?
> Decide how layer outputs influence the agent’s behavior and resolve competing proposals.

<!-- qard-id: ais-8dff99af50498fc22dd7 -->
> [!qard]- What is the modeling layer’s role in a mobile-robot hybrid?
> Represent and update the environment and relevant agents, including changed obstacles.

<!-- qard-id: ais-e8405d299d6ff3cb998c -->
> [!qard]- What is the planning layer’s role in a mobile-robot hybrid?
> Select routes or other actions for achieving longer-term transport goals.

<!-- qard-id: ais-869dceec425752b063a8 -->
> [!qard]- What is the reactive layer’s role in a mobile-robot hybrid?
> Respond to imminent local hazards, such as stopping or turning to avoid a collision.

<!-- qard-id: ais-c9a89c52ddfa9ade6875 -->
> [!qard]- How should planning and collision avoidance interact?
> Immediate avoidance can interrupt route following, followed by model updates and replanning when necessary.

<!-- qard-id: ais-d37932ef588b7b306381 -->
> [!qard]- Which TouringMachines application domains are listed?
> Autonomous robots, traffic simulations, automated factories, and distributed problem solving.

<!-- qard-id: ais-3a2c947db184442f2d5a -->
> [!qard]- How do individual proposal count and joint-combination count differ for $n$ layers with $m$ alternatives each?
> There are $mn$ individual candidate proposals; considering all joint choices can require $m^n$ combinations.

<!-- qard-id: ais-bc031e0632ceea054884 -->
> [!qard]- What failures can poor centralized mediation cause?
> Bottlenecks, oscillation, delayed emergency responses, and contradictory actions.

### Embodiment and the symbol-grounding problem

<!-- qard-id: ais-901a26612e8a94eea2af -->
> [!qard]- What is computational functionalism?
> The position that cognition depends on information-processing organization rather than a particular physical substrate.

<!-- qard-id: ais-c1de367ae1cceb769915 -->
> [!qard]- What is embodied cognition?
> The position that cognition depends importantly on bodily interaction with the environment.

<!-- qard-id: ais-673ba472943620664145 -->
> [!qard]- What is symbol grounding?
> Connecting symbols to their meanings through perceptual or other world-related capacities rather than only relations to other symbols.

<!-- qard-id: ais-2153ccf1342111340d58 -->
> [!qard]- How do functionalist and embodied views differ in emphasis?
> Functionalism emphasizes computation and permits nonbiological reasoning; embodiment emphasizes situated action and perception as contributors to meaning and competence.

<!-- qard-id: ais-8fc9c1f69f769cff42ef -->
> [!qard]- What viewpoints are associated with Brooks and Dreyfus?
> Brooks argues useful intelligence can emerge from situated reactive interaction; Dreyfus emphasizes humans’ involvement in situations.

<!-- qard-id: ais-f45dc41aa8ae4f8234f5 -->
> [!qard]- Does an LLM’s fluent answer settle whether physical embodiment is necessary for general intelligence?
> No. These are theoretical positions, and fluent behavior alone does not resolve the question.

<!-- qard-id: ais-a9e346cbf5281358872e -->
> [!qard]- Why do plausible text and recognizable generated-image objects not establish grounded understanding?
> Their causal, spatial, physical, and operational consistency still require checking.

<!-- qard-id: ais-14628d954086181b7ce4 -->
> [!qard]- What evidence supports evaluating grounded embodied action?
> Actual sensor-environment interactions and observed outcomes supporting the selected actions.
