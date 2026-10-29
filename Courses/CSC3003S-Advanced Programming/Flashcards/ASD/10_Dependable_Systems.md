---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 10 — Dependable Systems"
---

# ASD 10 — Dependable Systems

**Source note:** [Dependable Systems](../../ASD/10_Dependable_Systems.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Making Quality Concrete|Making Quality Concrete]]
  - [[#Reliability And Risk|Reliability And Risk]]
  - [[#Assuring Quality|Assuring Quality]]
  - [[#ISO 25010 Software Quality|ISO 25010 Software Quality]]
  - [[#Information Quality|Information Quality]]
  - [[#Standards Are Made By People|Standards Are Made By People]]
  - [[#Functional Suitability, Performance And Usability|Functional Suitability, Performance And Usability]]
  - [[#Reliability And Availability|Reliability And Availability]]
  - [[#Quality Control Versus Quality Assurance|Quality Control Versus Quality Assurance]]
  - [[#Dromey's Quality Model|Dromey's Quality Model]]
  - [[#Case Study: Boeing 737 MAX MCAS|Case Study: Boeing 737 MAX MCAS]]
  - [[#Maintainability, Flexibility, Safety, Compatibility|Maintainability, Flexibility, Safety, Compatibility]]
  - [[#Quality Characteristics|Quality Characteristics]]
  - [[#Risk And Assurance|Risk And Assurance]]

## Core Content

### Making Quality Concrete

<!-- qard-id: ap-fab36575202c3ae8dfd0 -->
> [!qard]- Why must “high quality” become explicit measurable requirements?
> Stakeholders interpret the phrase differently. Concrete characteristics and acceptance measures make trade-offs and verification possible.

<!-- qard-id: ap-673b95e1600af20ae1e6 -->
> [!qard]- How do functional and non-functional requirements differ?
> Functional requirements specify capabilities/behaviour; non-functional requirements constrain qualities such as latency, reliability, security and maintainability. Their boundary can be contextual.

<!-- qard-id: ap-954fb244ba7f447680d7 -->
> [!qard]- How do functional completeness, correctness and appropriateness differ?
> All needed features exist; the features produce correct results; the features fit the user's task without unnecessary or harmful functionality.

<!-- qard-id: ap-8b4a6871a7bfd794b9c0 -->
> [!qard]- How do performance's time, resource and capacity aspects differ?
> Response/run time; computing/storage/network resources consumed; and the workload volume the system can support.

<!-- qard-id: ap-883bbeddcad42ec74045 -->
> [!qard]- What does information quality add beyond working software?
> Outputs must be accurate, relevant, timely, understandable, verifiable and appropriately protected; a functioning program can still provide misleading information.

### Reliability And Risk

<!-- qard-id: ap-49f9bd18f95786db96ea -->
> [!qard]- How do availability, fault tolerance and recoverability differ?
> Being operational when needed; continuing service despite faults; restoring service and data after a failure.

<!-- qard-id: ap-ce521358de30e0dc2e4d -->
> [!qard]- What do MTTF, MTTD and MTTR measure in this lecture?
> Mean correct-running time to failure, time to diagnose a failure, and time to repair it. The lecture's MTBF cycle includes all three.

<!-- qard-id: ap-de5cb128205697fef8a5 -->
> [!qard]- How does the lecture's failure-cycle model relate availability to downtime?
> The cycle is MTTF + MTTD + MTTR; its available fraction is MTTF divided by that cycle. Faster diagnosis and repair reduce downtime. This fraction follows from the timeline model rather than being a separate formula stated in the note.

<!-- qard-id: ap-93d9017f29da3a91e346 -->
> [!qard]- How does the risk matrix guide ARTA responses?
> Low likelihood/low impact: accept; low likelihood/high impact: transfer; high likelihood/low impact: reduce; high likelihood/high impact: avoid or redesign the exposure.

<!-- qard-id: ap-a1597006056aa5b04a62 -->
> [!qard]- How do safety and security differ?
> Safety concerns avoiding harm from system behaviour; security concerns protecting assets and operations from unauthorised actions. A security failure can cause a safety failure.

<!-- qard-id: ap-6ca867663297486f7c49 -->
> [!qard]- How do maintainability, flexibility and compatibility differ?
> Ease of analysis/modification/testing; adaptation or replacement across contexts; and co-existence/interoperation with other systems.

### Assuring Quality

<!-- qard-id: ap-6132fdcdf7a22c0b2d03 -->
> [!qard]- How does quality assurance differ from quality control?
> QA puts preventive processes and evidence in place; QC inspects/tests the product to find defects. They complement one another.

<!-- qard-id: ap-4be81ce6e647453b227f -->
> [!qard]- How does quality in use differ from internal product quality?
> It evaluates real users' effectiveness, efficiency, satisfaction and risk in context, beyond the implementation's internal properties.

<!-- qard-id: ap-10f1fc38239c92fc7572 -->
> [!qard]- What general dependability lessons does the MCAS case illustrate in the course?
> Avoid unexamined single points of failure, make behaviour understandable to operators, assess safety constraints, and provide effective recovery mechanisms.

### ISO 25010 Software Quality

<!-- qard-id: ap-d3c1f14aa942fd0f6376 -->
> [!qard]- Which product-quality families does the course's model organise?
> Functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, flexibility and safety; the lecturer additionally emphasises information quality. Use them to state concrete requirements rather than a vague “good system”.

### Information Quality

<!-- qard-id: ap-25011942f37de9694a94 -->
> [!qard]- How can information be correct yet still unusable or untrustworthy?
> It may arrive too late, omit necessary context, be illegible/incomparable, lack provenance or be disclosed to an unauthorised audience. Quality includes usefulness, verification and appropriate protection as well as accurate arithmetic.

### Standards Are Made By People

<!-- qard-id: ap-0dfc4a79fb8e69f77630 -->
> [!qard]- Why compare engineers' product-quality models with accountants' information-quality models?
> Different professional goals highlight different risks: machinery/process structure versus trustworthy information flows. A standard is a selected perspective, so check what the actual system's stakeholders need beyond it.

### Functional Suitability, Performance And Usability

<!-- qard-id: ap-79f96a4d479d8660c4d2 -->
> [!qard]- What usability properties matter beyond an attractive interface?
> Recognisable interaction patterns, learnability, operability, accessibility and protection against consequential user errors; an appealing screen can still be difficult or unsafe to use.

### Reliability And Availability

<!-- qard-id: ap-6443345d3d757aad85a0 -->
> [!qard]- What does adding another “nine” of availability imply?
> The allowed downtime fraction falls by a factor of ten, so diagnosis/recovery and fault-tolerance demands become much stricter; a high percentage can still conceal meaningful annual outages.

### Quality Control Versus Quality Assurance

<!-- qard-id: ap-e1856b2e73470c6aaa15 -->
> [!qard]- Why can certification be harder with little documented process evidence?
> Assurance needs evidence that controls and quality procedures were followed; tests alone or undocumented working software may not supply that audit trail. Tailor documentation to the actual assurance obligation.

### Dromey's Quality Model

<!-- qard-id: ap-9be2dd866b991b308e7f -->
> [!qard]- What five steps does the course take from Dromey's quality-model process?
> Choose quality metrics, list system components, identify their quality-carrying properties, relate properties to the metrics, then evaluate weaknesses and mitigate them using risk analysis.

### Case Study: Boeing 737 MAX MCAS

<!-- qard-id: ap-658859cc37f80e252039 -->
> [!qard]- How does the course map MCAS's example failures to quality requirements?
> Single-sensor dependence challenges fault tolerance; poorly explained behaviour/training challenges learnability; repeated automatic corrections and limited operator recovery challenge safety, operability and recoverability. Assess the decisions against explicit requirements.

### Maintainability, Flexibility, Safety, Compatibility

<!-- qard-id: ap-3c558c1f3f846655b841 -->
> [!qard]- How do fail-safe behaviour, hazard warnings and safe integration address distinct safety risks?
> Fail-safe behaviour limits harm after a fault; warnings support informed action before a hazard; safe integration checks that interacting components do not create new hazards. Each complements rather than replaces prevention and recovery.

### Quality Characteristics

<!-- qard-id: ap-ef0dae45166c948205a0 -->
> [!qard]- How do functional completeness and correctness differ?
> Completeness asks whether all required capabilities exist; correctness asks whether the implemented capabilities produce the required results.

<!-- qard-id: ap-2432b523afdf27265593 -->
> [!qard]- What does functional appropriateness add to completeness?
> The functionality should suit the user's task without irrelevant or harmful features; implementing many unnecessary capabilities is not automatically better.

<!-- qard-id: ap-932c631a9949e888b47c -->
> [!qard]- How does capacity differ from response time as a performance requirement?
> Capacity limits supported workload/data/users; response time measures delay for an operation under specified conditions. A system may satisfy one and fail the other.

<!-- qard-id: ap-640ec6170923930bce78 -->
> [!qard]- How do co-existence and interoperability differ?
> Co-existence means working alongside other systems without harmful interference; interoperability means exchanging/using information through compatible interfaces.

<!-- qard-id: ap-98cda5adee28bef3efed -->
> [!qard]- How does learnability differ from accessibility?
> Ease of learning the system versus enabling use by people with differing abilities/needs; an interface may perform well on one and poorly on the other.

<!-- qard-id: ap-437e3ae9c3f9393e1f43 -->
> [!qard]- Why does user-error protection belong to software quality?
> Foreseeable mistakes should not cause avoidable data loss or harm; a system's design determines how easily such errors occur and how recoverable they are.

<!-- qard-id: ap-01a6df5bf7bb3d0a9186 -->
> [!qard]- How does availability differ from fault-free operation?
> A system may remain accessible while producing errors, or be correct when running but often down. Reliability needs more than a single uptime percentage.

<!-- qard-id: ap-c090453cd8c45869b42e -->
> [!qard]- How does fault tolerance differ from recovery after a fault?
> Tolerance maintains useful service despite the fault; recovery restores the required state/service after disruption. Both need explicit failure assumptions.

<!-- qard-id: ap-538bf06ba3145b80afef -->
> [!qard]- Why does recoverability include data integrity as well as time to restart?
> A fast restart with lost or corrupted state may fail the user's actual recovery requirement.

<!-- qard-id: ap-f4b1337367d1301d0c05 -->
> [!qard]- What maintainability properties make a component easier to change safely?
> Modularity, analysability, modifiability, reuse and testability, with limited dependencies and clear responsibilities.

<!-- qard-id: ap-fa0ed48cdef275269543 -->
> [!qard]- How do adaptability, scalability, installability and replaceability express flexibility?
> Suit a new context, handle changing scale, deploy successfully, and substitute a component/system respectively; they address distinct future changes.

### Risk And Assurance

<!-- qard-id: ap-04ce61bfa0deba0c3c5e -->
> [!qard]- Why assess likelihood and impact separately before choosing a risk response?
> A rare catastrophic event and a frequent minor event may have different controls and tolerances even if a simple product yields similar expected cost.

<!-- qard-id: ap-5b86e435ee14a5fe4671 -->
> [!qard]- What is the difference between documented QA compliance and demonstrated product fitness?
> The former shows a process/control was followed; the latter shows relevant outcomes meet needs. Neither alone automatically establishes the other.

<!-- qard-id: ap-5ab1467e9201cc90447a -->
> [!qard]- Why include operational users' context in quality evaluation?
> Correct internal properties do not ensure real users can achieve their goals safely, efficiently and satisfactorily in the actual environment.
