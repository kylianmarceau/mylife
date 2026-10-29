---
tags:
  - ai-systems
  - flashcards
qard-deck: "AI Systems"
qard-topic: "02 — Introduction II: Reactive, Deliberative, and Learning Agents"
---

# 02 — Introduction II: Reactive, Deliberative, and Learning Agents

**Source note:** [Introduction II: Reactive, Deliberative, and Learning Agents](../02_Introduction_II.md)

Exam recall cards covering concepts, definitions, methods, and qualifications. Worked examples are omitted; general proof methods are retained.

## Contents

- [[#Core Content|Core Content]]
  - [[#Rationality and control styles|Rationality and control styles]]
  - [[#Reactive stimulus-response architectures|Reactive stimulus-response architectures]]
  - [[#Deliberation and representation|Deliberation and representation]]
  - [[#Learning architectures|Learning architectures]]
  - [[#Braitenberg vehicles and vacuum robots|Braitenberg vehicles and vacuum robots]]
  - [[#Computer-use agents and OSWorld|Computer-use agents and OSWorld]]
  - [[#Generative AI, assistants, and agentic execution|Generative AI, assistants, and agentic execution]]

## Core Content

### Rationality and control styles

<!-- qard-id: ais-036d0c018f3c9e482df6 -->
> [!qard]- What is a reactive agent?
> An agent tightly coupling sensed information to actions with little or no explicit planning.

<!-- qard-id: ais-7e0abe4689169c614f10 -->
> [!qard]- What is a deliberative agent?
> An agent using a world representation and reasoning or planning to select actions.

<!-- qard-id: ais-1b942fa7afc742658c42 -->
> [!qard]- What is a learning agent?
> An agent whose behavior changes or improves through experience or data.

<!-- qard-id: ais-83dffa304a2f556f8397 -->
> [!qard]- Do reactive, deliberative, or learning designs guarantee rationality?
> No. They describe how behavior is produced; rationality concerns maximizing expected utility with available information.

### Reactive stimulus-response architectures

<!-- qard-id: ais-a0c167a5e5695b579a35 -->
> [!qard]- What is a condition-action rule?
> A rule selecting an action when a specified condition holds.

<!-- qard-id: ais-d7e20787da55202b8b53 -->
> [!qard]- What is a simple reflex agent?
> A controller using current percepts without a stored world model.

<!-- qard-id: ais-0e7958cebee4614fe9e0 -->
> [!qard]- What mathematical mapping describes a simple reactive policy?
> $\operatorname{action}:S\to A$, mapping sensed states to available actions.

<!-- qard-id: ais-3a793b3432ec1f9fe2de -->
> [!qard]- How can a simple reflex controller have a target without explicit goal reasoning?
> The desired target can be encoded in condition-action rules rather than reasoned about as a goal.

<!-- qard-id: ais-07c21ab9eab9b63a508c -->
> [!qard]- Why must parallel sense-act modules coordinate outputs?
> They can propose incompatible actions; concurrent computation does not permit conflicting motor commands to execute together.

<!-- qard-id: ais-14a800ac8b157c66ab6b -->
> [!qard]- Which concurrent behavior modules are illustrated?
> Identify objects, monitor changes, explore, wander, and avoid objects, feeding coordinated action control.

<!-- qard-id: ais-73a4f77b92de6f5a0ff3 -->
> [!qard]- What are reactive control’s main benefits?
> Fast response, simple modules, continual environmental feedback, and avoiding a complex symbolic world model.

<!-- qard-id: ais-eef983ac13a3494f6f0f -->
> [!qard]- What are reactive control’s main limitations?
> Limited explicit long-term planning, handcrafted-rule tuning, task-specific redesign, and problems with hidden state or ambiguous observations.

<!-- qard-id: ais-b17cd9a2d2a0b8f74f38 -->
> [!qard]- Are all reactive controllers memoryless?
> No. The simplest reflex controller is memoryless, but model-based reflex control can retain internal state while remaining reactive.

### Deliberation and representation

<!-- qard-id: ais-221ca1bde7c548912a9f -->
> [!qard]- What is a world model?
> An internal representation of the environment and how actions affect it.

<!-- qard-id: ais-21ddcd8fa227a2d27788 -->
> [!qard]- What is a plan?
> A course of action intended to achieve a goal.

<!-- qard-id: ais-be36e986378851f45f52 -->
> [!qard]- What is the transduction problem?
> Converting observations into representations suitable for reasoning.

<!-- qard-id: ais-ed538c004f40b9dce183 -->
> [!qard]- What is the representation problem?
> Choosing how to encode knowledge, tasks, and data for an agent.

<!-- qard-id: ais-2493dc6a8d21825e0f66 -->
> [!qard]- What steps does deliberative control follow?
> Receive percepts, update the world model, predict candidate-action effects, compare with goals, select and execute an action or plan, then observe and revise.

<!-- qard-id: ais-3d249a9345991bb32911 -->
> [!qard]- What is the benefit and cost of search look-ahead?
> It considers possible moves and responses, adding decision information while increasing computation.

<!-- qard-id: ais-cb2541b8949035af16fb -->
> [!qard]- What must knowledge, problem, and data representations encode?
> Knowledge: facts, rules, causality, time. Problem: states, goals, actions, constraints. Data: usable structures from raw text, images, or audio.

<!-- qard-id: ais-9e3280ae0eeaed985e95 -->
> [!qard]- Why can deliberation struggle in rapidly changing environments?
> The represented world can become stale before planning finishes; large search spaces and difficult representations also limit scalability.

<!-- qard-id: ais-d8dbb1dd90bfa1155551 -->
> [!qard]- Do those limitations show all deliberative systems fail in real environments?
> No. They are design-dependent challenges rather than a universal impossibility result.

### Learning architectures

<!-- qard-id: ais-db4f39ffd35c35c4b0f1 -->
> [!qard]- What is the performance element of a learning agent?
> The component selecting its external actions.

<!-- qard-id: ais-f334b53f2211eddd1839 -->
> [!qard]- What is the critic?
> A component evaluating behavior against a performance standard.

<!-- qard-id: ais-e9254170c9054bb5001d -->
> [!qard]- What is the learning element?
> A component modifying the performance element using feedback.

<!-- qard-id: ais-1261035478c40011479c -->
> [!qard]- What is the problem generator?
> A component proposing exploratory actions that may yield useful experience.

<!-- qard-id: ais-d053d2f5e38aa014e0ff -->
> [!qard]- How do labeled supervision and reinforcement learning train a controller?
> Supervision uses labeled examples; RL uses reward feedback after actions to learn a policy favoring useful future outcomes.

<!-- qard-id: ais-a13007790a416a2f7a1c -->
> [!qard]- Does a learning architecture necessarily require look-ahead?
> No. Its learned policy or reasoning components can be reactive or deliberative.

<!-- qard-id: ais-f2b20c6848c5cbe9a1d0 -->
> [!qard]- How do fixed reactive rules, fixed deliberative models, and learning designs adapt?
> Fixed designs require an added adaptation mechanism; learning designs include one. Their key challenges are rule tuning, representation/compute, and data/feedback/generalization respectively.

### Braitenberg vehicles and vacuum robots

<!-- qard-id: ais-b74684187644b5adb9c9 -->
> [!qard]- What is a Braitenberg vehicle?
> A vehicle with sensor-to-motor wiring that produces apparently purposeful behavior without explicit goal reasoning.

<!-- qard-id: ais-9f7cbff3db7d2946a5ab -->
> [!qard]- What does an excitatory light-sensor connection do?
> More light makes its connected wheel turn faster.

<!-- qard-id: ais-c48d40ba9b3222d6a83b -->
> [!qard]- Why does same-side excitatory wiring make a Braitenberg vehicle avoid light?
> The wheel on the brighter side speeds up, turning the vehicle away; this is vehicle 2a.

<!-- qard-id: ais-d5e7329b24897e5b04b0 -->
> [!qard]- Why does crossed excitatory wiring make a Braitenberg vehicle approach light?
> The opposite wheel speeds up, turning toward the brighter side; this is vehicle 2b.

<!-- qard-id: ais-3bd8a5c14fd3fecb41e5 -->
> [!qard]- Do “approach” and “avoid” prove that a Braitenberg controller represents goals or learns?
> No. They describe observable reactive behavior produced by the wiring.

<!-- qard-id: ais-f3a4459f79a2ff0b8f40 -->
> [!qard]- What sensing and actuation support a vacuum robot?
> Infrared, bump, and cliff sensors support obstacle handling; wheels provide movement and brushes/suction provide cleaning. Some designs add maps and planning.

<!-- qard-id: ais-4c0ce9618ee5898b7bdf -->
> [!qard]- Can a vacuum-robot brand name determine its architecture?
> No. Different implementations can combine reactive sensing, maps, and planning differently.

### Computer-use agents and OSWorld

<!-- qard-id: ais-dfa79790fee74ef938c4 -->
> [!qard]- What is a computer-use agent?
> An agent acting through graphical or operating-system interfaces.

<!-- qard-id: ais-c5ef01ea5419d66cfd3e -->
> [!qard]- What is execution-based evaluation?
> Check the resulting system state after actions rather than only judging generated answers or claims of completion.

<!-- qard-id: ais-51a4aacc72b803870823 -->
> [!qard]- Does an OS with an integrated assistant equal an OS wholly controlled by AI?
> No. Assistants, recognition, and optimization can be features without complete AI control.

<!-- qard-id: ais-e659bf986f5928bc8767 -->
> [!qard]- What does original OSWorld evaluate?
> $369$ tasks covering real applications, OS operations, and cross-application workflows, with task setup and result evaluation mechanisms.

<!-- qard-id: ais-d9aa19e64558fcc0bf87 -->
> [!qard]- Why are historical computer-use leaderboard scores configuration-dependent?
> Success depends on model, harness, settings, and task version, so screenshots are not universal capability guarantees.

### Generative AI, assistants, and agentic execution

<!-- qard-id: ais-9fafae3286c55acbcf68 -->
> [!qard]- What is generative AI?
> AI generating content such as text, images, audio, video, or code.

<!-- qard-id: ais-d40925b9cfab9b3cfce0 -->
> [!qard]- What is an LLM?
> A model trained to process and generate language using patterns learned from data.

<!-- qard-id: ais-f99b12b893507022cdba -->
> [!qard]- What is a harness?
> Software managing the model’s tools, context, execution, and permissions.

<!-- qard-id: ais-ba0bf039fdc04f543533 -->
> [!qard]- What is autonomy?
> The degree of independent choice an agent has while carrying out a task.

<!-- qard-id: ais-653b298999b7a107bd64 -->
> [!qard]- How do generative interaction, prompt-driven assistance, and agentic execution differ?
> Generation produces content; an assistant performs a requested function; agentic execution repeatedly selects steps toward a multi-step goal, inspecting outcomes and revising.

<!-- qard-id: ais-207ae8b0096a951711e2 -->
> [!qard]- What design features distinguish broader agentic execution?
> Tools, memory, repeated interaction, and task-directed decisions; persistence and learning must be inspected rather than assumed from product names.

<!-- qard-id: ais-5590e706d403eb31f8c6 -->
> [!qard]- Is remembering context automatically weight learning?
> No. Maintaining context or state differs from updating model parameters, and not every agent retrains during use.

<!-- qard-id: ais-d4735df316d5493e9782 -->
> [!qard]- How can a scripted assistant differ from a broader goal-driven agent?
> The script follows a specified flow; a broader agent can choose alternatives and revise when attempts fail.

<!-- qard-id: ais-816221cf260bde03c9b4 -->
> [!qard]- Does generating an application’s code with AI make that application autonomous?
> No. Autonomy depends on the application’s observation-action and decision mechanisms, not how its code was produced.
