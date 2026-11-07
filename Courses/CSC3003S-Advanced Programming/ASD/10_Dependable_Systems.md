---
tags:
  - advanced-programming
---

# Dependable Systems And Software Quality

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD10 Dependable Systems - Copy.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD10%20Dependable%20Systems%20-%20Copy.pdf), Johan Bontes, University of Cape Town, pages 1–30
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Software quality according to ISO 25010 plus information quality, functional and non-functional characteristics (reliability and the "nines", security risk, maintainability, flexibility, safety, compatibility), quality in use, quality control versus assurance, and the Boeing 737 MAX MCAS as a case of bad design.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Quality Has Two Meanings|Quality Has Two Meanings]]
  - [[#ISO 25010 Software Quality Model|ISO 25010 Software Quality Model]]
  - [[#Information Quality|Information Quality]]
  - [[#Standards Are Made By People|Standards Are Made By People]]
  - [[#Functional Suitability|Functional Suitability]]
  - [[#Performance Efficiency|Performance Efficiency]]
  - [[#Usability|Usability]]
  - [[#Reliability And Availability|Reliability And Availability]]
  - [[#Functional Versus Non-Functional|Functional Versus Non-Functional]]
  - [[#Security And The Risk Matrix|Security And The Risk Matrix]]
  - [[#Maintainability, Flexibility, Safety And Compatibility|Maintainability, Flexibility, Safety And Compatibility]]
  - [[#Quality In Use|Quality In Use]]
  - [[#Quality Control Versus Quality Assurance|Quality Control Versus Quality Assurance]]
  - [[#Dromley's Quality Model|Dromley's Quality Model]]
  - [[#The Cost Of Poor Quality|The Cost Of Poor Quality]]
  - [[#Case Study: Boeing 737 MAX MCAS|Case Study: Boeing 737 MAX MCAS]]

---

## Core Content

### Quality Has Two Meanings

The lecture opens with *Stairway to Heaven*: "'Cause you know sometimes words have two meanings." "Quality" is such a word — the programmer and the user mean different things by it, so it must be broken into well-defined characteristics.

### ISO 25010 Software Quality Model

#### Definitions

> **ISO 25010 (2011)**: The international standard model of software product quality, splitting quality into characteristics and sub-characteristics.

![ISO 25010 quality characteristics](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/10_Dependable_Systems/iso25010.svg)

*Functional suitability is the functional characteristic; the rest are non-functional. The lecturer adds information quality, and treats security as the most important.*

| Characteristic | Sub-characteristics |
|---|---|
| Functionally suitable | Complete, correct, appropriate |
| Performance efficient | Time, resources, capacity |
| Compatible | Co-existence, interoperable |
| Usable | Recognisable, learnable, operable, user-error protection, engagement (aesthetics), inclusivity (accessibility), user assistance, self-describing |
| Reliable | Fault-free, availability, fault tolerant, recoverability |
| Secure | Confidential, integrity, non-repudiation, accountability, authenticity, resistance |
| Maintainable | Modular, reusable, analysable, modifiable, testable |
| Flexible | Adaptable, scalable, installable, replaceable |
| Safe | Operations, identifying risks, fail-safe, hazard warning, safe integration |
| **+ Information quality** (lecturer's addition) | Accurate, usable, secure |

(Sub-characteristics follow Lew et al., 2010, and the updated ISO 25010.)

### Information Quality

The lecturer adds **information quality** — whether the information the software handles is fit for purpose.

| Group | Aspect | Meaning |
|---|---|---|
| Accurate | Complete | Not too little — "the whole truth" |
| | Correct | Not too much — "and nothing but the truth" |
| | Timely | Correct timestamp (no "robbing Peter to pay Paul") |
| | Mathematically accurate | Correct calculations (Excel sheets!) |
| Usable | Legible | Can be read/deciphered (e.g. binary file formats can't) |
| | Relevant | Fits the information demand; not outdated |
| | Understandable | Including its assumptions |
| | Comparable | Over time and against other data |
| Secure | Verified | Has it been, or can it be, checked? |
| | Trustworthy | Believable — what is the source? |
| | Legally compliant | Violates no laws (e.g. VAT calculations) |
| | Ethical | Privacy, medical data |
| | Authorised | Is the user allowed access? |

### Standards Are Made By People

| ISO 25010 (engineers) | Information quality (accountants) |
|---|---|
| Focus on models and processes | Focus on information flows and procedures |
| Software as a machine | Software as an administrative system |

IT means *information* technology, yet information quality is only implied in quality standards, not explicit — much as security was a few years ago.

### Functional Suitability

| Sub-characteristic | Meaning |
|---|---|
| Complete | All needed features |
| Correct | All features implemented correctly |
| Appropriate | No unneeded or harmful features |

### Performance Efficiency

| Aspect | Examples |
|---|---|
| Time | Run time, latency, solution quality |
| Resources | Data storage, network usage, CPU required |
| Capacity | How much data it can process |

### Usability

| Sub-characteristic | Meaning |
|---|---|
| Recognisable | Uses standard UI patterns |
| Learnable | Easy to learn |
| Operable | Easy to operate |
| Protection from user error | No data loss; no idiotic showstoppers (see Cooper, *About Face*, ch. 12) |
| UI aesthetics | Pleasant to use |
| Accessible | Works for users with disabilities |

### Reliability And Availability

| Sub-characteristic | Meaning |
|---|---|
| Available | Uptime |
| Faultless | No errors inside the software |
| Fault tolerant | Keeps working despite outside errors (hardware or other software failing) |
| Recoverable | If a fault occurs: how long recovery takes, and whether it fully recovers |

#### Definitions

> **Availability**: The probability that a system is "up". Uptime is quoted in "nines".

| Nines | Availability | Downtime per year |
|---|---|---|
| 2 | 99% | ~3½ days |
| 3 | 99.9% | ~8 hours |
| 4 | 99.99% | ~1 hour |
| 5 | 99.999% | ~5 minutes |
| 6 | 99.9999% | < 1 minute |

Downtime per year is $(1 - A) \times 365 \times 24$ hours, e.g. $(1 - 0.999) \times 8760 \approx 8.8$ hours.

> **MTTF (mean time to failure)**: Average time the system behaves correctly before failing.

> **MTTD (mean time to diagnose)**: Average time from failure until repair begins.

> **MTTR (mean time to repair)**: Average time to complete the repair.

> **MTBF (mean time between failures)**: Average time from one failure to the next.

$$
\text{MTBF} = \text{MTTD} + \text{MTTR} + \text{MTTF}, \qquad A = \frac{\text{MTTF}}{\text{MTBF}}
$$

![MTTF, MTTD, MTTR and MTBF](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/10_Dependable_Systems/mtbf-timeline.svg)

*After a failure the system is diagnosed and repaired, then runs correctly until the next failure; MTBF spans the whole cycle.*

### Functional Versus Non-Functional

The distinction is somewhat blurry:

| Functional | Non-functional |
|---|---|
| Directly affects users | Users may not notice, but it affects business risk |

### Security And The Risk Matrix

Security is the **most important** quality characteristic. Why? Because

$$
\text{Risk} = \text{cost} \times \text{likelihood}
$$

and insecure software is both likely to be attacked and expensive when it is.

| | Cheap | Expensive |
|---|---|---|
| **Unlikely** | Accept | Transfer (insure) |
| **Likely** | Reduce | Avoid |

![Risk matrix](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/10_Dependable_Systems/risk-matrix.svg)

*Each risk is treated according to its cost and likelihood: accept, reduce, transfer or avoid (ARTA).*

### Maintainability, Flexibility, Safety And Compatibility

**Maintainability** — for programmers:

- modular, with few connections (low fan-out);
- reusable;
- analysable;
- modifiable;
- testable.

**Flexibility** — for implementers:

- adaptable (portable);
- scalable;
- installable;
- replaceable.

**Safety** — not harmful:

| Sub-characteristic | Meaning |
|---|---|
| Operations | Doesn't hurt people or the organisation |
| Identify risks | Risks of harm are known |
| Fail-safe | "The plane does not crash" |
| Hazard warning | "Format disk: are you sure?" |
| Safe integration | Integrates with other systems without creating hazards |

**Compatibility**:

| Sub-characteristic | Meaning |
|---|---|
| Co-existence | Doesn't misbehave alongside other software |
| Interoperable | Can exchange information with other software |

### Quality In Use

| Perspective | Whose view |
|---|---|
| Inside quality | The programmer's view (the product's internal and external characteristics) |
| Outside quality (quality in use) | The user's view (how well it serves them in practice) |

### Quality Control Versus Quality Assurance

#### Definitions

> **Quality control**: A **reactive** approach that tries to detect quality problems, mainly by testing.

> **Quality assurance**: A **preventive** approach that puts procedures in place to assure quality (e.g. the ISO 9000 series) and documents the work done.

| | Quality control | Quality assurance |
|---|---|---|
| Nature | Reactive: detect problems | Preventive: procedures |
| Methods | Unit tests, automated tests, functionality tests, stress tests, alpha/beta tests | Documentation of work, checklists, an audit trail (who, what, why, where, when) |
| Prescribes procedures? | No | Yes |
| Certification | Not by itself | Useful for quality certification |

Formal assurance assumes a **waterfall** model: quality is checked against documentation, especially requirements and analysis, and each stage has its own documents. Pure Agile assumes the design grows organically, so it is hard to certify because of minimal documentation.

### Dromley's Quality Model

Every quality model (including Dromley's) breaks quality into different sub-components; the course sticks with ISO 25010's breakdown but uses Dromley's 5-step process:

1. Pick the high-level quality metrics to evaluate.
2. List the components in the system.
3. Identify the quality-carrying properties of each component.
4. Determine how each property affects the quality metric.
5. Evaluate, identify weaknesses, and use a risk matrix to mitigate.

### The Cost Of Poor Quality

The cost of poor quality is **exponential**. Sources include:

- errors in specification and development (communication and testing);
- verification and validation issues;
- availability problems — the system goes down;
- a buggy system;
- security problems — costly risks and cyber-attacks.

Design for recovery from failures and attacks **without loss of data**.

### Case Study: Boeing 737 MAX MCAS

The **MCAS** (Manoeuvring Characteristics Augmentation System) shows how bad design kills.

| Design flaw | Consequence |
|---|---|
| Solved a trivial problem | Added risk for little benefit |
| No training, just a bulletin | Pilots didn't know it existed |
| Pilot has 3 seconds to respond | Little margin for error |
| Has a hidden "cheat code" (pilot trim interrupts it) but restarts every 5 seconds | Repeated activation |
| Not on the runaway-stabiliser checklist | Pilots followed the wrong procedure |
| Depends on a **single** angle-of-attack (AoA) sensor | One faulty sensor triggers it — no redundancy |
| Bigger correction on every restart, up to 90° nose down | Escalating danger |
| Uses the tail, a huge lever | Pilot must exert tens of kg, then tons, to overcome it |
| Can only be switched off manually, and then the stabilisers are stuck | The fallback is a slow, awkward manual trim wheel |

MCAS drove the trim at increasing speed, while the pilot's only alternative was a slow, awkward manual trim wheel. The force needed on the control yoke was around 25–50 kg. It violates the safety characteristics above: no fail-safe, no hazard warning, unidentified risks, and unsafe integration.
