---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 05A — Project Management"
---

# ASD 05A — Project Management

**Source note:** [Project Management](../../ASD/05A_Project_Management.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Scope And Complexity|Scope And Complexity]]
  - [[#Planning And Delivery|Planning And Delivery]]
  - [[#Useful Measurement|Useful Measurement]]
  - [[#Good Design Properties|Good Design Properties]]
  - [[#Design Levels|Design Levels]]
  - [[#Levels 2–5: Subsystems, Classes, Routines|Levels 2–5: Subsystems, Classes, Routines]]
  - [[#Supporting Plans And Management Activities|Supporting Plans And Management Activities]]
  - [[#KPIs, Velocity And Code-Quality Metrics|KPIs, Velocity And Code-Quality Metrics]]
  - [[#DORA Metrics|DORA Metrics]]
  - [[#Requirements And Design|Requirements And Design]]
  - [[#Plans And Evidence|Plans And Evidence]]

## Core Content

### Scope And Complexity

<!-- qard-id: ap-1606947c65a3e1253e04 -->
> [!qard]- How does a project differ from a routine process?
> A project has a bounded goal, start/end and uncertain work to create something; a process repeats known activities continuously with predictable inputs and outputs.

<!-- qard-id: ap-c621751a3eadac4b9255 -->
> [!qard]- What distinguishes essential from accidental complexity?
> Essential complexity belongs to the problem and requirements; accidental complexity comes from the chosen tools, implementation and organisation.

<!-- qard-id: ap-5e6a871a00622b37b5a2 -->
> [!qard]- How do decomposition, clean interfaces and loose coupling manage complexity?
> They limit how much must be understood at once and prevent internal changes spreading across the whole system.

<!-- qard-id: ap-9404f1d75e815bf6f272 -->
> [!qard]- What do high fan-in and low fan-out mean?
> High fan-in: many callers reuse a component. Low fan-out: a component depends directly on relatively few others, limiting coordination and reasoning demands.

<!-- qard-id: ap-59d2d60ab9189b85aacc -->
> [!qard]- What should a project's scope make explicit?
> Required functionality, inputs/outputs, quality targets, boundaries and constraints, based on stakeholder needs.

<!-- qard-id: ap-cd4e914fbafa5d33b2ed -->
> [!qard]- What does a feasibility assessment consider beyond money?
> Required skills and people, available time, hardware, tools and reusable components compared with the proposed scope.

<!-- qard-id: ap-30ce3ff2ac2354dd6b55 -->
> [!qard]- Why write requirements in a form stakeholders can review?
> It lets them check that the intended system meets real needs before implementation makes misunderstandings expensive.

### Planning And Delivery

<!-- qard-id: ap-0cff5c327c59a9d820b6 -->
> [!qard]- What makes a goal SMART in the course notes?
> Specific, Measurable, Agreed upon, Realistic and Time-based: clear enough to commit to and assess.

<!-- qard-id: ap-ac8fda75eecca48f4a25 -->
> [!qard]- How do an activity, milestone and deliverable differ?
> An activity consumes time; a milestone marks a measurable completion point; a deliverable is a verifiable result supplied to a stakeholder/customer.

<!-- qard-id: ap-4508f83011c912e2bdd8 -->
> [!qard]- Why is “coding 80% complete” a weak milestone?
> It has no independently verifiable output and can hide uncertainty; prefer a concrete result such as an accepted working capability.

<!-- qard-id: ap-c237bece79710ca0ab1d -->
> [!qard]- Why might adding people make a late project later?
> Onboarding, coordination and extra communication consume existing capacity, while some work cannot be parallelised.

<!-- qard-id: ap-14ed142967be9c7014a6 -->
> [!qard]- What responses are available when a schedule is unrealistic?
> Change the deadline, resources or scope, accounting for the costs and limits of each; prioritised scope reduction can preserve the most important outcome.

<!-- qard-id: ap-924bc1dc63d74944b70b -->
> [!qard]- What does ARTA mean in risk management?
> Accept, Reduce, Transfer or Avoid a risk, choosing a response appropriate to its likelihood and impact.

### Useful Measurement

<!-- qard-id: ap-ad2511078cbfcb9fc3dc -->
> [!qard]- Which four DORA measures are presented in the lecture?
> Change lead time, deployment frequency, change failure rate and time to restore service after a failure: delivery speed and operational stability.

<!-- qard-id: ap-2edcdb016f7d4bb8c863 -->
> [!qard]- Why are lines of code, commit count or hours worked weak productivity measures?
> They measure activity rather than useful outcomes and can reward waste or gaming; interpret metrics with quality and context.

<!-- qard-id: ap-786624f7a37f19b0f497 -->
> [!qard]- What is the risk of turning one metric into a target for ranking people?
> People optimise the metric at the expense of real goals, creating misleading results and harmful incentives.

### Good Design Properties

<!-- qard-id: ap-caed0b76da843b92adc5 -->
> [!qard]- Beyond low coupling, what makes a design easier to maintain and reuse?
> Minimal understandable complexity, extensibility, DRY shared behaviour, leanness, consistent abstraction levels and established conventions/patterns. Documentation and clear interfaces support those properties.

### Design Levels

<!-- qard-id: ap-be15ea051a6692261295 -->
> [!qard]- How do the notes' design levels move from project choice to implementation?
> Select a methodology; establish requirements/scope; divide into subsystems; identify classes; divide class responsibilities into routines; design routine data, contracts and implementation details. Iterate rather than assuming one perfect pass.

### Levels 2–5: Subsystems, Classes, Routines

<!-- qard-id: ap-f79406979cfcfc0f817f -->
> [!qard]- What should routine design settle before coding details?
> Its requirement, clear verb–object name, parameters/result, permitted mutation, preconditions/postconditions/invariants and dependencies; pseudocode helps expose the intended algorithm.

### Supporting Plans And Management Activities

<!-- qard-id: ap-454b357dff153f022c92 -->
> [!qard]- How do human-resource, communication and risk plans support the delivery schedule?
> Specify needed skills/roles and availability, who needs which updates, and identified risks with responses. Track people, product, process, project resources and price rather than treating scheduling as the only management task.

### KPIs, Velocity And Code-Quality Metrics

<!-- qard-id: ap-8c6c6db998813ae51039 -->
> [!qard]- What do cyclomatic complexity, defect density and code churn indicate?
> Independent control-flow paths, defects per amount of code, and frequency of changes. They can suggest testing/maintenance risks but do not establish quality without context.

<!-- qard-id: ap-91886c26f00991af4174 -->
> [!qard]- How do throughput, cycle time and rework illuminate different delivery problems?
> Throughput counts completed items; cycle time measures how long work takes end-to-end; rework shows effort revisiting earlier results. Interpret trends with scope and quality rather than ranking raw counts.

### DORA Metrics

<!-- qard-id: ap-c04e8928e2e27f331c89 -->
> [!qard]- Why do delivery-performance metrics need a separate business-risk assessment?
> Fast frequent changes can still create a dangerous or low-value product. Delivery speed/stability do not measure every consequence of a failure or the relevance of the delivered feature.

### Requirements And Design

<!-- qard-id: ap-5c806373bb59ce865b60 -->
> [!qard]- What is a stakeholder, and why is the customer not necessarily the only one?
> Anyone affected by or influencing the project, including users, operators, sponsors, the team and relevant external parties; their needs/constraints can differ.

<!-- qard-id: ap-5d7b27ef373374f4cbd0 -->
> [!qard]- How does a use case describe requirements from a different perspective than a component design?
> It follows a user's goal and interactions with the system, rather than internal classes, storage or implementation sequence.

<!-- qard-id: ap-cb4a2a7c65e639a02c7e -->
> [!qard]- How do scope boundaries protect a feasible project?
> They distinguish promised outcomes from adjacent possibilities, limiting unacknowledged work and making changes explicit decisions.

<!-- qard-id: ap-58261baa601ba88eeea3 -->
> [!qard]- What resource question makes feasibility broader than “we have a budget”?
> Whether the necessary skills, people, time, infrastructure, tools and reusable components are available when dependencies need them.

<!-- qard-id: ap-65c0f7627c7e8b86f924 -->
> [!qard]- Why divide work into subsystems with explicit interfaces before assigning teams?
> It establishes coherent units and coordination boundaries, allowing independent progress without unrestricted cross-dependencies.

<!-- qard-id: ap-e898a56ef91ac4e88c3c -->
> [!qard]- How does high fan-out increase change risk?
> A unit knows many other components, so more changes and interaction assumptions can affect it; a focused interface can reduce that burden.

<!-- qard-id: ap-c16ee15ce62378e62dd0 -->
> [!qard]- How do preconditions and postconditions make a routine's responsibility reviewable?
> They state its required starting domain and promised result/end state, allowing implementation and callers to be checked against the same contract.

### Plans And Evidence

<!-- qard-id: ap-b9b3c67ef4c3ef6f892c -->
> [!qard]- What makes a deliverable verifiable?
> A concrete result with an intended recipient, due point and quality/acceptance standard that can be independently assessed.

<!-- qard-id: ap-d85542cd91e1272e357f -->
> [!qard]- What is a precursor in a project schedule?
> An activity whose completion another activity depends on; dependency structure constrains ordering and potential parallelism.

<!-- qard-id: ap-f468db7e45aa8a7a04d8 -->
> [!qard]- Why does adding resources not shorten inherently sequential dependencies proportionally?
> Work requiring another result cannot start earlier merely because more people are present; onboarding and communication also consume time.

<!-- qard-id: ap-8343fde33f94c1ff83ea -->
> [!qard]- What should a communication plan specify?
> Who needs which information, through which channel and cadence, with timely visibility into decisions, progress, changes and problems.

<!-- qard-id: ap-20339db30bd3b2782e24 -->
> [!qard]- What does a KPI need to be useful rather than merely countable?
> A link to a real objective, a clear operational definition, appropriate context and an action the team can take when its trend changes.

<!-- qard-id: ap-f8d10b5e92cb93b0c8c8 -->
> [!qard]- Why is a metric's improvement over time often more useful than its absolute value?
> Different systems/tasks have different baselines; tracking a stable contextual measure can show whether a specific process is improving without invalid comparisons.
