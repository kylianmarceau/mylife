---
tags:
  - advanced-programming
---

# Professional Conduct And Ethics

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD20-Ethics.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD20-Ethics.pdf), Johan Bontes, University of Cape Town, PDF pages 1–22  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: how software compares with regulated professions, the ACM and IEEE codes of ethics, principle-based versus rule-based ethics, licensing, the MCAS and Meta LLM cases, intellectual property, legal versus philosophical ethics, licences, and plagiarism.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Regulated Professions Versus Software|Regulated Professions Versus Software]]
  - [[#ACM Code Of Ethics (2018)|ACM Code Of Ethics (2018)]]
  - [[#IEEE Code Of Ethics (2020)|IEEE Code Of Ethics (2020)]]
  - [[#Don't Lawyerise A Code Of Ethics|Don't Lawyerise A Code Of Ethics]]
  - [[#Licensing Of Software Professionals?|Licensing Of Software Professionals?]]
  - [[#Case: Boeing MCAS|Case: Boeing MCAS]]
  - [[#Case: Generative AI And Meta's LLM|Case: Generative AI And Meta's LLM]]
  - [[#Intellectual Property|Intellectual Property]]
  - [[#Stallman, Copyleft And Sci-Hub|Stallman, Copyleft And Sci-Hub]]
  - [[#Legal Versus Philosophical Ethics|Legal Versus Philosophical Ethics]]
  - [[#Common Software Licences|Common Software Licences]]
  - [[#Plagiarism And Authorship|Plagiarism And Authorship]]

---

## Core Content

### Regulated Professions Versus Software

#### Definitions

> **Profession** (regulated): An occupation with formal education, apprenticeship, compulsory membership of an oversight body, continuing education, disciplinary hearings for ethics violations, and legal requirements codified in law.

Chartered accountants (the lecturer's example; accreditation varies by country) need:

- 4 years undergraduate plus 3 years postgraduate (comparable to a Master's), with a 3-year apprenticeship under a chartered accountant running concurrently: 7 years at university level in total
- compulsory membership of a professional oversight body
- continuing education requirements
- disciplinary hearings on violations of the code of ethics
- compliance with legal requirements codified in law

Medical doctors, architects and lawyers are similar.

![Professions comparison](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/20B_Professional_Conduct_And_Ethics/professions.svg)

*Software development has none of a regulated profession's safeguards ("nullptr exception"): no licensing, formal education, apprenticeship, compulsory body or discipline, only a voluntary code of ethics.*

### ACM Code Of Ethics (2018)

| Section | Principles |
|---|---|
| **1. General ethical principles** | 1.1 Contribute to society and human well-being, acknowledging that all people are stakeholders in computing. 1.2 **Avoid harm.** 1.3 Be honest and trustworthy. 1.4 Be fair and take action not to discriminate. 1.5 Respect the work required to produce new ideas, inventions, creative works and computing artefacts. 1.6 Respect privacy. 1.7 Honour confidentiality. |
| **2. Professional responsibilities** | 2.1 Strive for high quality in processes and products. 2.2 Maintain high standards of competence, conduct and ethical practice. 2.3 Know and respect rules pertaining to professional work. 2.4 Accept and provide appropriate professional review. 2.5 Give comprehensive evaluations of systems and their impacts, including risks. 2.6 Work only in areas of competence. 2.7 Foster public awareness of computing and its consequences. 2.8 Access resources only when authorised or compelled by the public good. 2.9 Design and implement systems that are robustly and usably secure. |
| **3. Professional leadership** | 3.1 Make the public good the central concern. 3.2 Articulate, encourage and evaluate social responsibilities in the organisation. 3.3 Manage people and resources to enhance quality of working life. 3.4 Support policies reflecting the Code. 3.5 Create opportunities for members to grow professionally. 3.6 Use care when modifying or retiring systems. 3.7 Take special care of systems integrated into society's infrastructure. |
| **4. Compliance** | 4.1 Uphold, promote and respect the Code. 4.2 Treat violations as inconsistent with ACM membership. |

### IEEE Code Of Ethics (2020)

The overarching aim is to uphold the highest standards of integrity, responsible behaviour and ethical conduct.

1. Hold paramount the **safety, health and welfare of the public**; follow ethical design and sustainable development; protect privacy; promptly disclose factors that might endanger the public or environment.
2. Improve understanding of the capabilities and societal implications of conventional and emerging technologies, including intelligent systems.
3. Avoid real or perceived **conflicts of interest**, and disclose them when they exist.
4. Avoid unlawful conduct and reject **bribery** in all its forms.
5. Seek, accept and offer honest criticism; acknowledge and correct errors; be honest and realistic in claims and estimates; credit others' contributions.
6. Maintain technical competence; undertake tasks only if qualified or after full disclosure of limitations.
7. Treat all persons fairly, without discrimination (race, religion, gender, disability, age, national origin, sexual orientation, gender identity or expression).
8. Do not engage in harassment, including sexual harassment or bullying.
9. Avoid injuring others, their property, reputation or employment by false or malicious actions or rumours.
10. Support colleagues in following the code, and do not retaliate against people reporting violations.

### Don't Lawyerise A Code Of Ethics

| American legal system | European legal system |
|---|---|
| Exceptionally detailed: every eventuality written into clauses | Mostly derived from Roman law (449 BC – 526 AD) |
| Feels secure, but encourages **gaming the system** | **Principle-based** |
| "If it's not explicitly forbidden, it must be allowed" | **Fraus legis**: fraudulent application of the letter of the law. Acts are legal only if they comply with the **intent** of the law. |
| Forces ever-increasing detail | |

A code of ethics should be read like the European model, by its principles and intent, not searched for loopholes.

### Licensing Of Software Professionals?

The ACM opposes licensing. The lecturer weighs its arguments:

| ACM argument | Lecturer's response |
|---|---|
| Premature | Seems a weak argument: computing pervades all of modern life |
| Would not improve software quality and reliability | Debatable. Centres of excellence aside, a certified minimum of training and experience would improve quality and reliability. |
| — | Enforceable codes of ethics would let the public hold professionals to account, though they won't stop all violations |

### Case: Boeing MCAS

Was the programmers' behaviour ethical? Test it against the codes (see [Dependable Systems](10_Dependable_Systems.md) for the technical failures):

| Code principle | Question for MCAS |
|---|---|
| Avoid harm (ACM 1.2; IEEE 1) | The system caused fatal crashes |
| Competence (ACM 2.6; IEEE 6) | Were the developers qualified for flight-critical control? |
| High quality (ACM 2.1) | A single-sensor dependency; escalating, repeated corrections |
| Honesty (ACM 1.3; IEEE 5) | The system was hidden from pilots' training and checklists |
| Lawful conduct (IEEE 4) | FAA compliance? |
| Care when modifying systems (ACM 3.6) | It was added to an existing airframe design |

### Case: Generative AI And Meta's LLM

- Meta downloaded every book on the pirate site libgen.is via BitTorrent to train an LLM.
- It claimed this was "legal" because it only downloaded (leeching) and did not enable sharing.
- This is a **clear violation of the ACM/IEEE codes** (e.g. ACM 1.5, respecting creative work). But software developers have no legally enforceable code of ethics, unlike accountants, lawyers and architects.
- Generative AI threatens to put content creators out of work: artists, writers, film-makers, "and yes, programmers too".

### Intellectual Property

#### Definitions

> **Intellectual property (IP)**: Legal rights over creations of the mind: copyright, patents and licensing terms.

IP sits within an international framework, but not all countries respect it; for example, Russia disregards copyright entirely.

### Stallman, Copyleft And Sci-Hub

#### Definitions

> **Copyleft** (e.g. the GPL): Uses copyright law to preserve the right to use, modify and distribute free software, by requiring derivatives to keep the same freedoms.

**Richard Stallman** (Free Software Foundation) argues:

- copyright, patents and DRM ("digital restrictions management") are misused to lock information away from users and programmers indefinitely
- he advocates **boycott, not piracy** ("Defective by Design")

**Sci-Hub** (Alexandra Elbakyan) aims "to provide free and unrestricted access to all scientific knowledge". It has been paused since 2020 because of an Indian lawsuit.

- Elbakyan argues it is legal under the right to science and culture (Article 27 of the Universal Declaration of Human Rights).
- Others see it as a moral imperative (civil disobedience): IP law should be changed, not Sci-Hub banned.

### Legal Versus Philosophical Ethics

The law is a **balance of interests**:

- That balance is not necessarily just or fair, and "legal" does not mean "good".
- Laws can be captured by special interests. Apartheid laws were legal, and the NSDAP (Nazi party) complied fully with German law.

The lecturer's take: if you join an organisation, either subscribe to its core tenets or resign. Your power to change it is very limited.

### Common Software Licences

| Open source | Proprietary |
|---|---|
| GPL (strong copyleft), LGPL (weaker copyleft for libraries), Apache (permissive, with a patent grant), MIT (permissive) | Vendor licences restricting use, copying and modification |

The source names these licences only. The short descriptions in brackets are standard characterisations added for context.

### Plagiarism And Authorship

| Why it is unethical for scholars | Why it is unethical for developers |
|---|---|
| Reputations are built on original research | Violates intellectual property |
| Undermines meritocracy | Makes it impossible to trace where code came from, so its limitations and issues can't be researched |
| Dishonest | Makes you look like a fraud |
| | As a risk it is high probability and high cost, so **avoid** it |

See also the UCT GenAI policy in [Artificial Intelligence](20A_Artificial_Intelligence.md).
