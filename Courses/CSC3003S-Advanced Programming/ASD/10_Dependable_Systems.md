---
tags:
  - advanced-programming
---

# Dependable Systems

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD10 Dependable Systems - Copy.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD10%20Dependable%20Systems%20-%20Copy.pdf), Johan Bontes, University of Cape Town, PDF pages 1–30  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: ISO 25010 software quality, information quality, each quality characteristic, availability and failure metrics, security risk, quality in use, quality control versus assurance, and the Boeing 737 MAX MCAS case.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Ambiguity And Quality|Ambiguity And Quality]]
  - [[#ISO 25010 Software Quality|ISO 25010 Software Quality]]
  - [[#Information Quality|Information Quality]]
  - [[#Standards Are Made By People|Standards Are Made By People]]
  - [[#Functional Suitability, Performance And Usability|Functional Suitability, Performance And Usability]]
  - [[#Reliability And Availability|Reliability And Availability]]
  - [[#Functional Versus Non-Functional|Functional Versus Non-Functional]]
  - [[#Security: The Most Important Quality|Security: The Most Important Quality]]
  - [[#Maintainability, Flexibility, Safety, Compatibility|Maintainability, Flexibility, Safety, Compatibility]]
  - [[#Quality In Use|Quality In Use]]
  - [[#Quality Control Versus Quality Assurance|Quality Control Versus Quality Assurance]]
  - [[#Dromey's Quality Model|Dromey's Quality Model]]
  - [[#The Cost Of Poor Quality|The Cost Of Poor Quality]]
  - [[#Case Study: Boeing 737 MAX MCAS|Case Study: Boeing 737 MAX MCAS]]

---

## Core Content

### Ambiguity And Quality

The lecture opens with *Stairway to Heaven*: "'Cause you know sometimes words have two meanings." Requirements and quality terms are ambiguous, and different readers interpret them differently. Quality must therefore be broken into explicit, agreed characteristics.

### ISO 25010 Software Quality

#### Definitions

> **ISO 25010**: The international standard model of software product quality. It breaks quality into characteristics, each with sub-characteristics.

![ISO 25010 characteristics](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/10_Dependable_Systems/iso25010.svg)

*Functional characteristics directly affect users. Non-functional ones affect business risk. Security is singled out as the most important, and the lecturer adds information quality.*

| Characteristic | Sub-characteristics |
|---|---|
| **Suitable** (functional suitability) | Complete, correct, appropriate |
| **Efficient** (performance) | Time, resources, capacity |
| **Compatible** | Co-existence, interoperable |
| **Usable** | Recognisable, learnable, user-error protection, engagement, inclusivity, assistance, self-describing |
| **Reliable** | Fault-free, availability, fault tolerant, recoverability |
| **Secure** | Confidential, integrity, non-repudiation, accountability, authenticity, resistance |
| **Maintainable** | Modular, reusable, analysable, modifiable, testable |
| **Flexible** | Adaptable, scalable, installable, replaceable |
| **Safe** | Operations, identifying risks, fail-safe, hazard warning, safe integration |
| **+ Information quality** | Accurate, usable, secure |

### Information Quality

| Accurate | Usable | Secure |
|---|---|---|
| **Complete**: not too much (the whole truth) | **Legible**: can be read or deciphered (binary formats) | **Trustworthy**: believable; what is the source? |
| **Correct**: not too little (nothing but the truth) | **Relevant**: fits the information demand; not outdated | **Legally compliant**: violates no laws (e.g. VAT calculations) |
| **Timely**: correct timestamp ("robbing Peter to pay Paul") | **Understandable**: including its assumptions | **Ethical**: privacy, medical |
| **Mathematically accurate**: correct calculations (Excel sheets!) | **Comparable**: over time and against other data | **Authorised**: is the user allowed access? |
| | **Verified**: has it been, or can it be, checked? | |

### Standards Are Made By People

| ISO 25010 | Quality aspects of information |
|---|---|
| Made by engineers | Made by accountants |
| Focus on models and processes | Focus on information flows and procedures |
| Software as a machine | Software as an administrative system |

IT stands for *information* technology, yet information is only implied in quality standards, not explicit, much as security was a few years ago.

### Functional Suitability, Performance And Usability

**Functional suitability**:

- **Complete**: all needed features.
- **Correct**: all implemented correctly.
- **Appropriate**: no unneeded features and no harmful ones.

**Performance / efficiency**:

| Aspect | Examples |
|---|---|
| Time | Run time, latency, solution quality |
| Resources | Data storage, network usage, CPU required |
| Capacity | How much data it can process |

**Usability**:

- **Recognisable**: use standard UI patterns.
- **Learnable**.
- **Operable**.
- **Protection from user error**: no data loss and no "idiotic showstoppers" (see Cooper, *About Face*, ch. 12).
- **UI aesthetics**.
- **Accessible**: works for users with disabilities.

### Reliability And Availability

#### Definitions

> **Availability**: The probability that a system is "up".

> **Fault tolerance**: Continuing to work when outside hardware or software fails.

> **Recoverability**: After a fault, how long recovery takes and whether the system fully recovers.

Reliability covers being **available** (uptime), **faultless** (no internal errors), **fault tolerant** and **recoverable**.

Uptime is measured in "nines":

| Nines | Availability | Downtime per year |
|---|---|---|
| 2 | 99% | 3½ days |
| 3 | 99.9% | 8 hours |
| 4 | 99.99% | 1 hour |
| 5 | 99.999% | 5 minutes |
| 6 | 99.9999% | < 1 minute |

| Metric | Meaning |
|---|---|
| **MTTF** | Mean time **to** failure: correct behaviour until a failure |
| **MTTD** | Mean time to diagnose |
| **MTTR** | Mean time to repair |
| **MTBF** | Mean time **between** failures |

![Failure timeline](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/10_Dependable_Systems/mtbf-timeline.svg)

*After the first failure the system is diagnosed (MTTD), repaired (MTTR), then behaves correctly (MTTF) until the next failure. MTBF spans from one failure to the next.*

$$
\text{MTBF} = \text{MTTD} + \text{MTTR} + \text{MTTF}
$$

### Functional Versus Non-Functional

The distinction is somewhat blurry:

- **Functional**: directly affects users.
- **Non-functional**: users may not notice it, but it affects business risks.

### Security: The Most Important Quality

Security is the most important quality metric, because of risk:

$$
\text{Risk} = \text{cost} \times \text{likelihood}
$$

![Risk matrix](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/10_Dependable_Systems/risk-matrix.svg)

*Cheap and unlikely risks are accepted. Expensive but unlikely ones are transferred (insured). Likely but cheap ones are reduced. Likely and expensive ones must be avoided.*

| | Cheap | Expensive |
|---|---|---|
| **Unlikely** | Accept | Transfer (insure) |
| **Likely** | Reduce | Avoid |

This is the ARTA strategy (Accept, Reduce, Transfer, Avoid) from [Project Management](05A_Project_Management.md). Insecure software is likely and expensive, so it must be avoided.

### Maintainability, Flexibility, Safety, Compatibility

| Characteristic | Audience | Properties |
|---|---|---|
| **Maintainability** | Programmers | Modular, few connections (low fan-out), reusable, analysable, modifiable, testable |
| **Flexibility** | Implementers | Adaptable (portable), scalable, installable, replaceable |
| **Safety** | Everyone (not harmful) | Operations don't hurt people or the organisation; risks of harm identified; **fail-safe** ("plane does not crash"); **hazard warnings** ("Format disk: are you sure?"); safe integration |
| **Compatibility** | Other systems | **Co-existence** (does not misbehave alongside other software); **interoperability** (can exchange information) |

### Quality In Use

| Perspective | View | Model |
|---|---|---|
| **Inside quality** | The programmer's view | ISO 25010 product quality characteristics |
| **Outside quality** (quality in use) | The user's view | Effectiveness; efficiency; satisfaction (usefulness, trust, pleasure, comfort); freedom from risk (economic, health and safety, environmental risk mitigation); context coverage (completeness, flexibility) |

### Quality Control Versus Quality Assurance

#### Definitions

> **Quality control**: A **reactive** process that tries to detect quality problems through testing (unit, automated, functionality, stress, alpha/beta tests). It does not prescribe procedures or standardised documentation.

> **Quality assurance**: A **preventative** process that puts procedures in place to assure quality (the ISO 9000 series), with documentation showing after the fact that the procedures were followed.

| Quality control | Quality assurance |
|---|---|
| Reactive: detect problems | Preventative: procedures, checklists |
| Testing | Documented audit trail, useful for certification |
| No prescribed documentation | Formal assurance assumes **waterfall**: quality is checked against each stage's documents (who, what, why, where, when) |
| | Pure **Agile** grows the design organically, so it is hard to certify because documentation is minimal |

### Dromey's Quality Model

Every quality model breaks "quality" down differently. The course follows ISO 25010 but uses Dromey's five-step process (the slide spells it "Dromley"):

1. Pick high-level quality metrics to evaluate.
2. List the components of the system.
3. Identify the quality-carrying properties of each component.
4. Determine how each property affects the quality metrics.
5. Evaluate, identify weaknesses, and use a risk matrix to mitigate them.

### The Cost Of Poor Quality

The cost of poor quality is **exponential**. It comes from:

- errors in specification and development (communication and testing)
- verification and validation issues
- availability problems: the system goes down
- buggy systems
- security problems: costly risks and cyber attacks

**Design for recovery** from failures and attacks without loss of data.

### Case Study: Boeing 737 MAX MCAS

MCAS (the Maneuvering Characteristics Augmentation System) is an example of bad design that violates many quality characteristics:

| Flaw | Quality violated |
|---|---|
| Solved a trivial problem | Functional appropriateness |
| No training, just a bulletin; not on the "runaway stabiliser" checklist | Usability, learnability |
| Pilot had about 3 seconds to respond | Safety: protection from operator error |
| Had a hidden "cheat code", yet restarted every 5 seconds with a bigger correction each time, up to 90° nose-down | Safety, fail-safe |
| Depended on a **single** angle-of-attack sensor | Reliability, fault tolerance (no redundancy) |
| Used the tail stabiliser, a huge lever, so the pilot needed tens of kilograms of force, then tons, on the yoke | Safety, operability |
| Could only be switched off manually, after which the stabilisers were stuck | Recoverability |

Three controls act on the stabiliser:

- **MCAS**, with increasing trim speed
- the **trim switches**, at a fixed slow speed
- the **manual trim wheel**, which is awkward to use

The pilot works the **yoke** (the slide's pun is "Pilot Joke"). Flight-recorder data (BEA, Ethiopian Airlines ET302) shows pilots needing about **50 kg** of force on the yoke, later about 25 kg, to counter MCAS.
