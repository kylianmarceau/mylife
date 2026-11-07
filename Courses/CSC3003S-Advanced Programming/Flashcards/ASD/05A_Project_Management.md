---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 05A — Project Management"
---

# ASD 05A — Project Management

**Source note:** [Project Management](../../ASD/05A_Project_Management.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Projects And Complexity|Projects And Complexity]]
  - [[#Design Levels|Design Levels]]
  - [[#Planning|Planning]]
  - [[#Milestones And Metrics|Milestones And Metrics]]

## Core Content

### Projects And Complexity

<!-- qard-id: ap-dd9f009244ba3c823dac -->
> [!qard]- How do projects differ from processes?
> Projects are ad hoc with fixed start/end, uncertain tasks and ~50% success; processes are routine and continuous with >99% success.

<!-- qard-id: ap-cff4a7021a59c3ba4246 -->
> [!qard]- What is project management?
> Ensuring software is delivered on time, within budget and to requirements.

<!-- qard-id: ap-e72105df4293c0ddf991 -->
> [!qard]- What is Brooks's "No Silver Bullet" claim?
> No single technique fixes the inherent complexity of software development.

<!-- qard-id: ap-886b27a508ecff3f5f3a -->
> [!qard]- Essential versus accidental problems?
> Essential: from requirements and scope. Accidental: from process, tools and people.

<!-- qard-id: ap-54cc4c4ed15b7f9b16cf -->
> [!qard]- How should complexity be managed, per Dijkstra?
> Minimise essential complexity held at once (decomposition, loose coupling, clean interfaces) and stop accidental complexity spreading.

<!-- qard-id: ap-e4c9cda0e467e22ce10a -->
> [!qard]- Name five good design properties.
> Minimal complexity, maintainability, loose coupling, extensibility, reusability (DRY), high fan-in/low fan-out, leanness, standard patterns.

### Design Levels

<!-- qard-id: ap-df3c6d62d7c40bf19556 -->
> [!qard]- List the six design levels.
> 0 methodology; 1 project (requirements, architecture); 2 subsystems; 3 classes/packages; 4 routines; 5 routine design and code.

<!-- qard-id: ap-4766a7dfdd38cbaa3b2a -->
> [!qard]- What do project requirements cover?
> Features, input/output data, content shown to users, and bounding constraints such as performance, interfaces and reliability.

<!-- qard-id: ap-cfd1b1c103102ea9c667 -->
> [!qard]- Why make requirements explicit?
> The client can review them (not code), late changes are expensive, and stable requirements avoid cost overruns.

<!-- qard-id: ap-67b2465426a07bcebd5a -->
> [!qard]- What is a use case?
> A scenario-based description of a user's interaction with the software, from the user's view.

<!-- qard-id: ap-4ea7c7af3f1ed0c886ff -->
> [!qard]- What are the "complete" and "correct" requirement checks?
> Complete: missing info noted, realistic, acceptance assured. Correct: users' language, no conflicts, consistent detail, testable, understood by coders.

<!-- qard-id: ap-5fc5ea9c08549643a196 -->
> [!qard]- How should subsystems be planned (level 2)?
> As self-contained units with rule-based, hierarchical interactions and low fan-out; decide buy versus build.

<!-- qard-id: ap-55b1fa16c450059d9c2a -->
> [!qard]- What should routine design (level 5) include?
> Good `verbObject` names, documentation, parameter and return design, pre/post-conditions and assertions, and pseudocode.

### Planning

<!-- qard-id: ap-6c6a2ae2ffa58829cceb -->
> [!qard]- What is a stakeholder?
> Anyone impacted by the project — sponsor, client, users, managers and team.

<!-- qard-id: ap-b8bdf6b12717885babb7 -->
> [!qard]- What resources does a feasibility check consider?
> People, hardware and tools, reusable components, time and money.

<!-- qard-id: ap-789def3df04f17c178bd -->
> [!qard]- What do SMART goals stand for?
> Specific, measurable, agreed upon, realistic, time-based.

<!-- qard-id: ap-a28d51046f118c3927ba -->
> [!qard]- What makes a good deliverable?
> Verifiable, specific, needed by a stakeholder, dated, with quality standards.

<!-- qard-id: ap-bf15a5c7c339f3d921dc -->
> [!qard]- What are the three options if a schedule is unrealistic?
> Delay the deadline, add resources (expensive and limited by the mythical man-month), or reduce scope.

<!-- qard-id: ap-5deb3dc926fafe037ad6 -->
> [!qard]- What is the mythical man-month?
> Adding people lowers each person's productivity through communication overhead, so beyond a point it lengthens the project.

<!-- qard-id: ap-586199f9163ef1186d09 -->
> [!qard]- What do the human resource, communication and risk management plans cover?
> Staff skills and roles; who is informed and how; identifying risks and treating them by ARTA (accept, reduce, transfer, avoid).

### Milestones And Metrics

<!-- qard-id: ap-d363cca1111c433b2bba -->
> [!qard]- What is a milestone?
> The completion of an activity with a formal, measurable output ("80% coded" doesn't count).

<!-- qard-id: ap-fa60ecb8031bc6bf275a -->
> [!qard]- Name the four DORA metrics.
> Change lead time, deployment frequency, change failure rate, mean time to recovery.

<!-- qard-id: ap-1d53c74f4ab0216e8d6d -->
> [!qard]- What are DORA's limitations?
> It can't compare different teams and doesn't capture business risk.

<!-- qard-id: ap-7cd7c54b293b700f7119 -->
> [!qard]- Give two KPI, two velocity and two code-quality metrics.
> KPI: throughput, cycle time. Velocity: story points per sprint, rework percentage. Quality: code coverage, defect density (or cyclomatic complexity, churn).

<!-- qard-id: ap-cdfef9f7f83a4ff37134 -->
> [!qard]- Name four metric pitfalls.
> Non-metrics (LOC, hours), over-measurement, stack ranking, ignoring context.

<!-- qard-id: ap-90f890d889f19e3ae6dc -->
> [!qard]- Why are metrics best treated as relative?
> Absolute values may be meaningless; improvement over time matters, and wrong incentives cause gaming (moral hazard).

<!-- qard-id: ap-6d730e6a3591095d79d8 -->
> [!qard]- Define activity, precursor and deliverable.
> Activity: a task taking time, with duration and due date. Precursor: an activity others depend on. Deliverable: a project result handed to the customer.

<!-- qard-id: ap-f6489dee5da1dd6d529b -->
> [!qard]- What is the SDLC?
> The software development life cycle — the phases a methodology follows (e.g. waterfall: requirements, analysis, design, code, test, deploy).
