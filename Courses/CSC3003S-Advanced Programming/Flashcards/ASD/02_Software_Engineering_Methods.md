---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 02 — Software Engineering Methods"
---

# ASD 02 — Software Engineering Methods

**Source note:** [Software Engineering Methods](../../ASD/02_Software_Engineering_Methods.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Why Projects Fail|Why Projects Fail]]
  - [[#Waste And Entropy|Waste And Entropy]]
  - [[#Naïve Approaches|Naïve Approaches]]
  - [[#Iterative Development|Iterative Development]]

## Core Content

### Why Projects Fail

<!-- qard-id: ap-99dac328fbe2a23510a2 -->
> [!qard]- What is the most common problem in software projects?
> Estimation, not construction — cost and schedule targets are wrong, often set by those least able to judge.

<!-- qard-id: ap-83f1ea300df7f48b9cd4 -->
> [!qard]- What does "faster, better, cheaper: pick two" mean?
> Time, scope/quality and cost can't all be optimised; fixing two determines the third.

<!-- qard-id: ap-74b2de61b63568c53ef9 -->
> [!qard]- What is the single biggest success factor for software projects?
> Limiting size and complexity — small projects succeed far more often than large ones.

<!-- qard-id: ap-5074b0a17aac6d17da61 -->
> [!qard]- How does Agile compare with waterfall in the CHAOS data?
> Agile: 39% successful, 9% failed. Waterfall: 11% successful, 29% failed.

<!-- qard-id: ap-ca8917a4639cb958d443 -->
> [!qard]- What is the main criticism of the Standish CHAOS figures?
> Their data has unknown forecasting biases, so aggregates may be unreliable.

<!-- qard-id: ap-e078e26d2e72b0cadf41 -->
> [!qard]- What share of features are rarely or never used?
> About two thirds (45% never, 19% rarely).

### Waste And Entropy

<!-- qard-id: ap-40361f92274968d2f58e -->
> [!qard]- What is YAGNI?
> "You ain't gonna need it": build only what's needed now, avoiding speculative development.

<!-- qard-id: ap-022b70f8a9e7300dcf24 -->
> [!qard]- What is gold plating?
> Adding features or polish beyond what's required.

<!-- qard-id: ap-1d3d9a7fda88b263b553 -->
> [!qard]- Why does software cost grow exponentially with features?
> Communication costs (Brooks); returns grow linearly, so beyond some point ROI turns negative.

<!-- qard-id: ap-762ab2a4f7ec2d645447 -->
> [!qard]- What is software entropy, and how is it cured?
> Code complexity that grows over time through fixes and features (technical debt). Cure: YAGNI at the start and refactoring as you go.

<!-- qard-id: ap-81b16a65f9d4f6c52af0 -->
> [!qard]- What is yak shaving?
> Pointless work only tangentially related to the goal.

<!-- qard-id: ap-2728db3c121afd497b99 -->
> [!qard]- What is crunch, and what does it cause?
> Sustained overtime caused by other problems (bad estimates, too-short schedules); it leads to burnout.

### Naïve Approaches

<!-- qard-id: ap-8514a2f9ddde31d28373 -->
> [!qard]- What is code and fix?
> No methodology: dive into code and react to bugs; can end in a "death spiral".

<!-- qard-id: ap-6402e59c956bd8b6db55 -->
> [!qard]- What is the waterfall method?
> Sequential phases — requirements, analysis, design, implementation, testing, operation — each completed before the next.

<!-- qard-id: ap-630c22874031e869ba51 -->
> [!qard]- When does waterfall work?
> When the problem is fully understood, changes are rare and costly, and standard patterns apply (e.g. building construction).

<!-- qard-id: ap-2e6e4b1816e6b2a458fa -->
> [!qard]- Why can pure waterfall not work for software?
> Each phase must be perfect, but software is infinitely changeable and coding, testing and user issues often require redesign.

<!-- qard-id: ap-9b02ee589da910212c35 -->
> [!qard]- What is a wicked problem?
> An unknown unknown — it can't be anticipated and only appears late (implementation, testing or operation).

<!-- qard-id: ap-33a3f7e68e9eae17e979 -->
> [!qard]- How should each cell of the problem matrix be handled?
> Known known: standard solution. Unknown known: refactor. Known unknown: fix in requirements/analysis. Unknown unknown: go back to the start.

<!-- qard-id: ap-15e699b5c63a931cb3ec -->
> [!qard]- How does the cost of a change grow with time?
> Exponentially — a late change can cost up to 1000× an early one.

### Iterative Development

<!-- qard-id: ap-eed56696d7ab2f9ba789 -->
> [!qard]- What is iterative development?
> Reaching the goal through a series of ever-improving delivery cycles: plan, develop, test, release, feedback.

<!-- qard-id: ap-796f86c4247dd8890561 -->
> [!qard]- What does iterative development need from the team?
> Working close together and with the customer, agreeing quickly, releasing every 2–4 weeks.

<!-- qard-id: ap-f17965028aa0e2de27c7 -->
> [!qard]- What is the main danger of iterative development?
> Tight focus on high-priority features can miss alternatives, iterating to a small success instead of a bigger opportunity.

<!-- qard-id: ap-c75babadc9c13cf7eb03 -->
> [!qard]- Name four iterative methods and a key feature of each.
> Agile (mini projects, face to face), RAD (voice of customer, rigid schedule), XP (pair programming, unit tests, refactoring), Scrum (sprints, empirical process).

<!-- qard-id: ap-8985cad87a35f54e4238 -->
> [!qard]- What is the "skateboard" approach?
> Build only what's required first, then design for change and grow it.

<!-- qard-id: ap-8ac70dd21c0edc9fa11a -->
> [!qard]- What is prototyping, and what is RAD?
> Prototyping cycles requirements → prototype → tests to learn early. RAD (Rapid Application Development) cycles requirements, design, develop, deploy and reflect quickly with heavy customer input.
