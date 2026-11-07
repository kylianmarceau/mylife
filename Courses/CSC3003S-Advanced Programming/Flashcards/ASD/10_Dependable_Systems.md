---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 10 — Dependable Systems And Software Quality"
---

# ASD 10 — Dependable Systems And Software Quality

**Source note:** [Dependable Systems And Software Quality](../../ASD/10_Dependable_Systems.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Quality Model|Quality Model]]
  - [[#Reliability|Reliability]]
  - [[#Other Characteristics|Other Characteristics]]
  - [[#Quality Assurance|Quality Assurance]]

## Core Content

### Quality Model

<!-- qard-id: ap-6adfbddc0061f7da891d -->
> [!qard]- What is ISO 25010?
> The international standard model breaking software product quality into characteristics and sub-characteristics.

<!-- qard-id: ap-05f883254928c2d5dba1 -->
> [!qard]- List the ISO 25010 quality characteristics.
> Functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, flexibility, safety.

<!-- qard-id: ap-f99161a8c2b64eff28a3 -->
> [!qard]- What does the lecturer add to ISO 25010?
> Information quality — accurate, usable and secure information.

<!-- qard-id: ap-59812962b0b9471cfe46 -->
> [!qard]- Functional versus non-functional quality?
> Functional directly affects users; non-functional may go unnoticed by users but affects business risk.

<!-- qard-id: ap-6db1e7dc04729a985c7a -->
> [!qard]- What are the sub-characteristics of functional suitability?
> Complete, correct, appropriate (no unneeded or harmful features).

<!-- qard-id: ap-328b93c700ad564a7fb0 -->
> [!qard]- What three aspects make up performance efficiency?
> Time (run time, latency), resources (storage, network, CPU), capacity.

<!-- qard-id: ap-07ad98aae6b80d8a0de9 -->
> [!qard]- Name four usability sub-characteristics.
> Recognisable, learnable, operable, protection from user error (plus aesthetics, accessibility).

### Reliability

<!-- qard-id: ap-52f209a54a50bb00d682 -->
> [!qard]- What are the reliability sub-characteristics?
> Available, faultless, fault tolerant, recoverable.

<!-- qard-id: ap-c422fac68981dc41a5ac -->
> [!qard]- Fault-free versus fault-tolerant?
> Fault-free: no internal errors. Fault-tolerant: keeps working despite outside failures.

<!-- qard-id: ap-c0ad81b48c08fa35e08d -->
> [!qard]- What downtime per year do 3, 4 and 5 nines allow?
> 99.9% ≈ 8 hours; 99.99% ≈ 1 hour; 99.999% ≈ 5 minutes.

<!-- qard-id: ap-32d6cfc0851fe765e1db -->
> [!qard]- Define MTTF, MTTD, MTTR and MTBF.
> Mean time to failure, to diagnose, to repair, and between failures: $\text{MTBF}=\text{MTTD}+\text{MTTR}+\text{MTTF}$.

<!-- qard-id: ap-c3eafbb95f56a359722a -->
> [!qard]- How is availability computed from these?
> $A=\text{MTTF}/\text{MTBF}$.

### Other Characteristics

<!-- qard-id: ap-e3a7ca349eb47fb04e9b -->
> [!qard]- Why is security the most important quality characteristic?
> Risk = cost × likelihood, and breaches are both likely and expensive.

<!-- qard-id: ap-b9021f8d38c67f7b6ba2 -->
> [!qard]- How is each risk-matrix quadrant treated?
> Cheap/unlikely: accept. Expensive/unlikely: transfer (insure). Cheap/likely: reduce. Expensive/likely: avoid.

<!-- qard-id: ap-e0239cff27aaf4f0b096 -->
> [!qard]- What makes software maintainable?
> Modular, low fan-out, reusable, analysable, modifiable, testable.

<!-- qard-id: ap-b4a6974c4da8b16c8d96 -->
> [!qard]- What does flexibility cover?
> Adaptable (portable), scalable, installable, replaceable.

<!-- qard-id: ap-94596f864785447547d1 -->
> [!qard]- What does safety cover?
> Safe operation, identified risks, fail-safe behaviour, hazard warnings, safe integration.

<!-- qard-id: ap-9df1301c8bb122cac8d3 -->
> [!qard]- What does compatibility cover?
> Co-existence with other software and interoperability.

### Quality Assurance

<!-- qard-id: ap-b4a4590b962e478060b7 -->
> [!qard]- Quality control versus quality assurance?
> Control is reactive — detecting problems by testing. Assurance is preventive — procedures, documentation and audit trails (ISO 9000).

<!-- qard-id: ap-f0e923bb79dd52806f35 -->
> [!qard]- Why is pure Agile hard to certify?
> Formal assurance assumes waterfall-style documents; Agile has minimal documentation.

<!-- qard-id: ap-be819fa62e421b601d7d -->
> [!qard]- Inside quality versus quality in use?
> Inside: the programmer's view of the product. Quality in use: the user's view in practice.

<!-- qard-id: ap-fdc2aedef50cb63bc759 -->
> [!qard]- What are Dromley's five evaluation steps?
> Pick quality metrics, list components, identify their quality-carrying properties, relate properties to metrics, evaluate and mitigate with a risk matrix.

<!-- qard-id: ap-2b3403fb8843e1d3822d -->
> [!qard]- Name three design flaws of Boeing's MCAS.
> Relied on a single AoA sensor, repeatedly re-activated with growing correction, and wasn't in training or checklists.

<!-- qard-id: ap-3b63aef6f67b1b1ca764 -->
> [!qard]- How do engineers' and accountants' views of quality differ?
> Engineers (ISO 25010) focus on models and processes — software as a machine. Accountants focus on information flows — software as an administrative system.
