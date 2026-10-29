---
tags:
  - ai-systems
  - flashcards
qard-deck: "AI Systems"
qard-topic: "06 — Agent Architectures II: Emergence, Subsumption, Continuum Crowds, and Boids"
---

# 06 — Agent Architectures II: Emergence, Subsumption, Continuum Crowds, and Boids

**Source note:** [Agent Architectures II: Emergence, Subsumption, Continuum Crowds, and Boids](../06_Agent_Architectures_II.md)

Exam recall cards covering concepts, definitions, methods, and qualifications. Worked examples are omitted; general proof methods are retained.

## Contents

- [[#Core Content|Core Content]]
  - [[#Architecture overview and emergence|Architecture overview and emergence]]
  - [[#Deep learning, scale, and hallucinations|Deep learning, scale, and hallucinations]]
  - [[#Brooks’ subsumption architecture|Brooks’ subsumption architecture]]
  - [[#Continuum crowds|Continuum crowds]]
  - [[#Boids: local steering and collective patterns|Boids: local steering and collective patterns]]
  - [[#Stigmergy, combined models, and design limits|Stigmergy, combined models, and design limits]]

## Core Content

### Architecture overview and emergence

<!-- qard-id: ais-586d021986a69f41a86a -->
> [!qard]- What is emergent behavior?
> A global pattern arising from local components and environmental interactions rather than an explicit global instruction.

<!-- qard-id: ais-339ebb2cfd58a4882e63 -->
> [!qard]- What is a multi-agent system?
> A system containing multiple interacting agents.

<!-- qard-id: ais-a4d246d705ba362fc820 -->
> [!qard]- What is generalization?
> Applying learned behavior to inputs beyond the exact training examples.

<!-- qard-id: ais-cf6325b073428b98ec25 -->
> [!qard]- Which reactive and deliberative families are grouped in the lecture?
> Reactive: subsumption, Boids, continuum crowds, and stigmergy. Deliberative: BDI.

<!-- qard-id: ais-49abb79bd87aeac917a1 -->
> [!qard]- Why are the lecture’s architecture groupings not strict partitions?
> Categories can overlap; cognitive architectures need not all be purely neural, and names such as Brahms occur in multiple broad groupings.

<!-- qard-id: ais-aa86c056d23b08c8a119 -->
> [!qard]- Which cognitive architectures are named?
> AASMO, Soar, ACT-R, Brahms, LIDA, PreAct, Cougaar, PRODIGY, and FORR.

<!-- qard-id: ais-4a0777b957e717694510 -->
> [!qard]- Which hybrid architectures are named?
> 3T, AuRA, Brahms, GAIuS, GRL, ICARUS, InteRRaP, TinyCog, and TouringMachines.

<!-- qard-id: ais-dc3afb95b59b7b2d9c8b -->
> [!qard]- How does the lecture analogize BDI beliefs, desires, and intentions to LLM agents?
> Beliefs: context, retrieved memory, tool results. Desires: system/task objectives. Intentions: maintained current plan or task state.

<!-- qard-id: ais-5685902ca8e8d53e0891 -->
> [!qard]- Does a generated reasoning trace establish formal BDI intention management?
> No. The comparison is an analogy; committed-plan management requires actual mechanisms.

<!-- qard-id: ais-d839b04b692e3b59b6da -->
> [!qard]- Why do local rules not uniquely determine a global pattern?
> Parameters, component interactions, and environmental conditions also shape emergence.

### Deep learning, scale, and hallucinations

<!-- qard-id: ais-eefc115f65e5ac06c320 -->
> [!qard]- What are an ANN and deep learning?
> An ANN contains computational units connected by adjustable weights; deep learning uses models with multiple processing layers.

<!-- qard-id: ais-1e5bc236693c6b1edf2e -->
> [!qard]- What do designers specify, and what do learned weights determine?
> Designers choose architecture and training methods; learned weights jointly determine outputs through repeated transformations.

<!-- qard-id: ais-c78ddb1aac52f8ffb101 -->
> [!qard]- What does universal function approximation establish—and leave unproven?
> Representational capacity under assumptions; it does not prove a trained model will generalize correctly.

<!-- qard-id: ais-c2ff8d1632b1311462ba -->
> [!qard]- What qualitative model-scale patterns are illustrated?
> Three-digit addition shows a sharp exact-accuracy rise; multitask language understanding improves with size; program synthesis improves with a sharper rise near the largest model.

<!-- qard-id: ais-4ba4ae851f49213ba462 -->
> [!qard]- Does a sharp metric threshold prove an all-or-nothing internal ability?
> No. A visible threshold in task scores alone cannot establish that conclusion.

<!-- qard-id: ais-c68840f6c6d12c23bc62 -->
> [!qard]- What is a hallucination in the task context?
> Generated content false or unsupported relative to the factual or task requirements.

<!-- qard-id: ais-1ddcf2bbc32c623514a9 -->
> [!qard]- What instruction, context, and logical inconsistencies can appear in generated output?
> Performing the wrong requested operation, contradicting supplied source content, or reaching a result inconsistent with earlier reasoning.

<!-- qard-id: ais-4b92cad82e1e511dc3fd -->
> [!qard]- Why is failed generalization not a complete theory of hallucination?
> It is one proposed explanation; multiple mechanisms can produce unsupported or inconsistent output.

<!-- qard-id: ais-e287e7bcab3b7091ff58 -->
> [!qard]- Is intentional fantasy art automatically a hallucination?
> No. Judge against the task: invention can be desired in art but harmful in factual reporting.

### Brooks’ subsumption architecture

<!-- qard-id: ais-0f2bd321eb5a7f14725d -->
> [!qard]- What is subsumption architecture?
> Layered reactive task controllers suppress or override signals in other behavior paths.

<!-- qard-id: ais-3568411d04c2d9b365ce -->
> [!qard]- What is a behavior layer?
> A controller for a specific task using the relevant sensor information.

<!-- qard-id: ais-e5918ff2cb489a3aa42b -->
> [!qard]- What does situated or embodied intelligence mean?
> Intelligent behavior arising through interaction with an actual environment.

<!-- qard-id: ais-151e69eac0818af92321 -->
> [!qard]- What is Brooks’ central architectural thesis?
> Useful intelligent behavior can arise without a detailed symbolic model or theorem-proving system, using the world as continuing feedback.

<!-- qard-id: ais-4fa6eae271e018452d57 -->
> [!qard]- How is subsumption built incrementally?
> Lower layers establish primitive competence; added layers support broader tasks and can subsume existing signal paths.

<!-- qard-id: ais-d0ef84d5accf3148c35d -->
> [!qard]- Does being drawn higher in a hierarchy automatically establish safety priority?
> No. Collision and avoidance priorities must be designed explicitly.

<!-- qard-id: ais-f07069dd0d230bd3fbc4 -->
> [!qard]- How can local recovery, avoidance, and exploration yield maze traversal?
> Parallel controllers react to collisions, nearby obstacles, and movement objectives, with environmental feedback shaping the combined motion.

<!-- qard-id: ais-8580d8eb9de30f80d862 -->
> [!qard]- Does reactive maze traversal imply a symbolic maze concept or optimal-route guarantee?
> No. Traversal can emerge without those explicit concepts, and does not guarantee solving every maze or finding the best path.

<!-- qard-id: ais-113d51ca4874129a9a95 -->
> [!qard]- What benefits does basic subsumption offer?
> Modularity, responsiveness, incremental competence, and partial fault tolerance.

<!-- qard-id: ais-e8e2038c9966d95ded1a -->
> [!qard]- What limits those subsumption benefits?
> Layer interactions can be hard to debug, long-range planning is weak, new tasks need rules, and critical-layer failure can remain serious.

<!-- qard-id: ais-601218825cd799195c42 -->
> [!qard]- What abilities are limited in basic fixed-rule subsumption?
> Rich memory, learning, and abstract reasoning; learned-controller extensions can help but do not guarantee desired global behavior.

### Continuum crowds

<!-- qard-id: ais-1eb2f5ccb71dd32ca5e4 -->
> [!qard]- What is a continuum crowd model?
> A model guiding many agents through shared spatial fields accounting for movement costs.

<!-- qard-id: ais-eb2478191e13e68ff55a -->
> [!qard]- What is a discomfort field?
> A spatial function $g(x)$ describing how undesirable positions are.

<!-- qard-id: ais-553f98b7d7e2fa0a297f -->
> [!qard]- What do $G$, $f$, $g$, $x$, and $P$ denote in continuum crowds?
> Goal region, maximum feasible speed field, discomfort field, current position, and paths from that position to the goal.

<!-- qard-id: ais-33d8f42d322fc0a6516a -->
> [!qard]- What are the four continuum movement principles?
> Seek the goal, obey feasible speed, prefer lower discomfort, and choose paths considering length, travel time, and accumulated discomfort.

<!-- qard-id: ais-850364827045bfcbc1b4 -->
> [!qard]- What does $g(x)<g(x_0)$ tell you?
> Position $x$ is more desirable than $x_0$ on the discomfort criterion alone.

<!-- qard-id: ais-96a01b6cd1bbaffc0740 -->
> [!qard]- Why does a crowd-path comparison require explicit tradeoffs?
> Shorter paths, faster paths, and lower-discomfort paths can differ; an objective must specify how their costs are weighted.

<!-- qard-id: ais-2254b6caf80ee7d8e680 -->
> [!qard]- What supplementary crowd-path objective is given?
> $C(p)=\alpha L(p)+\beta T(p)+\gamma D(p)$ with nonnegative weights, then $p^*=\arg\min_{p\in P}C(p)$. The exact formula and weights are illustrative, not specified by the lecture.

<!-- qard-id: ais-e2b129791c1ef930a6dc -->
> [!qard]- What does the example discomfort heat-map encode?
> Red highest, purple high, orange low, green lowest; colors do not supply exact numerical costs.

<!-- qard-id: ais-886ce62d19f407bbc905 -->
> [!qard]- Which application domains use continuum crowd models?
> Graphics, games, and movies, modeling many moving agents in shared spatial environments.

### Boids: local steering and collective patterns

<!-- qard-id: ais-dec0d9b25df35c4442ea -->
> [!qard]- What are a Boid and its neighborhood?
> A Boid is a simulated flocking agent; its neighborhood consists of agents within selected distance and view angle.

<!-- qard-id: ais-73b0fc7c4ab2a7b97ee6 -->
> [!qard]- What is separation or repulsion?
> Steering away from nearby agents to avoid crowding.

<!-- qard-id: ais-0546a2a196ef463253e1 -->
> [!qard]- What is alignment or orientation?
> Steering toward neighbors’ average heading.

<!-- qard-id: ais-7627b7f9f8a37b90afb5 -->
> [!qard]- What is cohesion or attraction?
> Steering toward neighbors’ average position.

<!-- qard-id: ais-4bc0730ffbfe81faa9e1 -->
> [!qard]- What terminology correction matters for the Boids rules?
> Heading corresponds to alignment; position corresponds to cohesion. The introductory source list swaps these descriptions.

<!-- qard-id: ais-fa78ed5cdf9dbf5e284d -->
> [!qard]- Do Boids need a symbolic global flock plan?
> No. Collective motion can emerge from local neighbor reactions.

<!-- qard-id: ais-fba876db699ef0db12fd -->
> [!qard]- Why should “no internal state” not be read literally for a Boids simulation?
> Boids still have physical state such as position and velocity; they may lack a symbolic world model.

<!-- qard-id: ais-55aa9419406ff89911da -->
> [!qard]- What relationship between repulsion, orientation, and attraction radii is shown?
> $r_c\le r_o\le r_a$, with a later figure using $r_r$ for repulsion.

<!-- qard-id: ais-ade60f59cc4b0f89a5aa -->
> [!qard]- What roles do the inner, middle, outer, and blind zones serve?
> Inner avoids crowding, middle aligns headings, outer maintains cohesion, and the blind sector excludes neighbors outside the view angle.

<!-- qard-id: ais-7cfe28b3307bc69ea9e3 -->
> [!qard]- Why should a Boids implementation specify neighborhoods explicitly?
> The source’s interval wording is inconsistent with the illustrated middle zone; named effects are clearer than assuming one universal radius convention.

<!-- qard-id: ais-52c5d1560795f20866eb -->
> [!qard]- What collective patterns can parameter changes produce in the illustrated Boids model?
> Compact swarms, dispersion, toroidal/ring circulation, and elongated meteor-like groups.

<!-- qard-id: ais-6181b49823a8b1db5137 -->
> [!qard]- Do a particular parameter setting’s plotted patterns guarantee the same result in every environment?
> No. Other settings and environmental interactions also affect emergence.

### Stigmergy, combined models, and design limits

<!-- qard-id: ais-08210ff77b17817f2a39 -->
> [!qard]- What is stigmergy?
> Indirect coordination through modifications left in a shared environment.

<!-- qard-id: ais-0943d9abe596f00e2f1d -->
> [!qard]- How do Boids and stigmergy differ in their information source?
> Boids use direct local neighbor information; stigmergy uses environmental traces.

<!-- qard-id: ais-142d7ac5b619a693b7a0 -->
> [!qard]- How can continuum fields and Boids rules complement each other?
> Fields guide spatial movement, while Boids rules coordinate local group motion.

<!-- qard-id: ais-aab0141ba3cd2a5ca7b0 -->
> [!qard]- What is the central engineering challenge in emergence-based control?
> Choose local rules, layers, neighborhoods, and environmental interactions so the desired collective task is actually solved.

<!-- qard-id: ais-b8987fe2cd1e3914369e -->
> [!qard]- Does attractive collective motion alone demonstrate useful problem solving?
> No. The resulting behavior must be evaluated against the task objective.
