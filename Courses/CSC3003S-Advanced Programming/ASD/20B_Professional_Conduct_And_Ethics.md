---
tags:
  - advanced-programming
---

# Professional Conduct And Ethics

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD20-Ethics.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD20-Ethics.pdf), Johan Bontes, University of Cape Town, pages 1–22
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> How software development compares with regulated professions, the ACM and IEEE codes of ethics, principle-based versus rule-based ethics, licensing, the Boeing MCAS and Meta LLM cases, intellectual property and copyleft, legal versus ethical, software licences, and plagiarism.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Regulated Professions Versus Software Developers|Regulated Professions Versus Software Developers]]
  - [[#ACM Code Of Ethics (2018)|ACM Code Of Ethics (2018)]]
  - [[#IEEE Code Of Ethics (2020)|IEEE Code Of Ethics (2020)]]
  - [[#Don't Lawyerise The Code Of Ethics|Don't Lawyerise The Code Of Ethics]]
  - [[#Should Software Developers Be Licensed?|Should Software Developers Be Licensed?]]
  - [[#Case: Boeing MCAS|Case: Boeing MCAS]]
  - [[#Case: Generative AI And Meta's LLM|Case: Generative AI And Meta's LLM]]
  - [[#Intellectual Property And Copyleft|Intellectual Property And Copyleft]]
  - [[#Sci-Hub And Civil Disobedience|Sci-Hub And Civil Disobedience]]
  - [[#Legal Versus Ethical|Legal Versus Ethical]]
  - [[#Common Software Licences|Common Software Licences]]
  - [[#Plagiarism And Authorship|Plagiarism And Authorship]]

---

## Core Content

### Regulated Professions Versus Software Developers

Chartered accountants (requirements vary by country; the lecturer's example):

- 4 years undergraduate;
- 3 years postgraduate (comparable to a master's);
- 3 years apprenticeship under a chartered accountant (concurrent with postgrad);
- 7 years of university-level study in total;
- compulsory membership of a professional oversight body;
- permanent continuing-education requirements;
- disciplinary hearings for violations of the code of ethics;
- subject to legal requirements codified in law.

The same holds for medical doctors, architects and lawyers. For software developers: nothing — a "nullptr exception".

| Requirement | Chartered accountant | Software developer |
|---|---|---|
| University-level education | 7 years (4 UG + 3 PG) | None required |
| Apprenticeship | 3 years | None |
| Certification / licensing | Yes | None |
| Compulsory professional body | Yes | None |
| Continuing education | Yes | None |
| Disciplinary mechanism | Yes | None |
| Code of ethics | Enforced in law | Voluntary only |

![Regulated professions versus developers](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/20B_Professional_Conduct_And_Ethics/professions.svg)

*Every safeguard regulated professions have is absent for software developers.*

### ACM Code Of Ethics (2018)

**1. General ethical principles**

1. Contribute to society and to human well-being, acknowledging that all people are stakeholders in computing.
2. Avoid harm.
3. Be honest and trustworthy.
4. Be fair and take action not to discriminate.
5. Respect the work required to produce new ideas, inventions, creative works and computing artefacts.
6. Respect privacy.
7. Honour confidentiality.

**2. Professional responsibilities**

1. Strive for high quality in both the processes and products of professional work.
2. Maintain high standards of professional competence, conduct and ethical practice.
3. Know and respect existing rules pertaining to professional work.
4. Accept and provide appropriate professional review.
5. Give comprehensive and thorough evaluations of computer systems and their impacts, including analysis of possible risks.
6. Perform work only in areas of competence.
7. Foster public awareness and understanding of computing, related technologies and their consequences.
8. Access computing and communication resources only when authorised or when compelled by the public good.
9. Design and implement systems that are robustly and usably secure.

**3. Professional leadership principles**

1. Ensure the public good is the central concern during all professional computing work.
2. Articulate, encourage acceptance of, and evaluate fulfilment of social responsibilities by members of the organisation or group.
3. Manage personnel and resources to enhance the quality of working life.
4. Articulate, apply and support policies and processes that reflect the principles of the Code.
5. Create opportunities for members of the organisation or group to grow as professionals.
6. Use care when modifying or retiring systems.
7. Recognise and take special care of systems that become integrated into the infrastructure of society.

**4. Compliance with the Code**

1. Uphold, promote and respect the principles of the Code.
2. Treat violations of the Code as inconsistent with membership in the ACM.

### IEEE Code Of Ethics (2020)

"To uphold the highest standards of integrity, responsible behaviour and ethical conduct in professional activities":

1. Hold paramount the safety, health and welfare of the public; strive to comply with ethical design and sustainable development practices; protect others' privacy; promptly disclose factors that might endanger the public or the environment.
2. Improve individual and societal understanding of the capabilities and societal implications of conventional and emerging technologies, including intelligent systems.
3. Avoid real or perceived conflicts of interest whenever possible, and disclose them to affected parties when they exist.
4. Avoid unlawful conduct in professional activities, and reject bribery in all its forms.
5. Seek, accept and offer honest criticism of technical work; acknowledge and correct errors; be honest and realistic in stating claims or estimates based on available data; credit properly the contributions of others.
6. Maintain and improve technical competence, and undertake technological tasks for others only if qualified by training or experience, or after full disclosure of pertinent limitations.
7. Treat all persons fairly and with respect, without discrimination based on race, religion, gender, disability, age, national origin, sexual orientation, gender identity or gender expression.
8. Do not engage in harassment of any kind, including sexual harassment or bullying.
9. Avoid injuring others, their property, reputation or employment by false or malicious actions, rumours or any other verbal or physical abuse.
10. Support colleagues in following this code, strive to ensure it is upheld, and do not retaliate against individuals reporting a violation.

### Don't Lawyerise The Code Of Ethics

| American legal system | European legal system |
|---|---|
| Exceptionally detailed; every eventuality captured in clauses | Mostly derived from Roman law (449 BC – 526 AD) |
| Feels secure, but encourages **gaming the system**: "if it's not explicitly forbidden, it must be allowed" | **Principle-based** |
| Forces an ever-increasing level of detail | ***Fraus legis***: applying the letter of the law fraudulently is itself illegal — acts are legal only if they comply with the **intent** of the law |

A code of ethics should be read like the European system: follow its intent, not search for loopholes.

### Should Software Developers Be Licensed?

The ACM opposes licensing. Its arguments and the lecturer's responses:

| ACM argument | Response |
|---|---|
| It is premature | Seems a weak argument |
| Computing pervades all aspects of modern life | — |
| Licensing would not be effective in improving software quality and reliability | Debatable: centres of excellence aside, a certified minimum level of training and experience would improve quality and reliability |

Licensing would also bring **enforceable** codes of ethics and professionalism, giving the public a means to hold professionals to account — though it obviously wouldn't stop all violations.

### Case: Boeing MCAS

Was the behaviour of the programmers who built the 737 MAX's MCAS ethical? (See [Dependable Systems](10_Dependable_Systems.md#Case%20Study%3A%20Boeing%20737%20MAX%20MCAS) for the design.) Questions to ask, from the codes:

| Code principle | Question |
|---|---|
| Avoid harm | Did the design avoid harm? |
| Competence | Was the work within their competence? |
| High quality | Was it high-quality work? |
| Honesty | Were risks honestly disclosed? |
| Lawful conduct | Was it FAA-compliant? |
| Care when modifying systems | Was enough care taken when modifying the aircraft's system? |

### Case: Generative AI And Meta's LLM

- Meta downloaded every book on the pirate site libgen.is, via BitTorrent, to train its LLM.
- It claimed this was "legal" because it didn't enable sharing of the torrented data (leeching only).
- This is a clear violation of the ACM and IEEE codes of ethics — but software developers have no legally enforceable code of ethics, unlike accountants, lawyers and architects.
- Generative AI threatens to put content creators out of work: artists, writers, film makers — and programmers too.

### Intellectual Property And Copyleft

#### Definitions

> **Intellectual property (IP)**: Legal rights over creations of the mind — copyright, patents and licensing terms — within an international framework. Not all countries respect IP (e.g. Russia disregards copyright entirely).

> **Copyleft (GPL)**: Using copyright law to **preserve** the right to use, modify and distribute free software, by requiring derivatives to carry the same freedoms.

**Richard Stallman** (Free Software Foundation):

- Created copyleft via the GPL licence.
- Argues copyright, patents and digital restrictions management (DRM) are misused to lock information away from users and programmers indefinitely ("Defective by Design" campaign).
- Advocates **boycott, not piracy**.

### Sci-Hub And Civil Disobedience

Pirate Bay, LibGen and **Sci-Hub** (Alexandra Elbakyan) — Sci-Hub has been paused since 2020 due to an Indian lawsuit.

- Goal: "to provide free and unrestricted access to all scientific knowledge."
- Elbakyan argues it is legal under the right to science and culture in Article 27 of the Universal Declaration of Human Rights.
- Others argue Sci-Hub is a moral imperative (**civil disobedience**), and that IP law should be changed rather than Sci-Hub banned.

### Legal Versus Ethical

Law is a **balance of interests**:

- That doesn't mean the balance is just or fair — "legal" does not mean "good".
- Laws can be captured by special interests.
- Apartheid laws were legal; the NSDAP (Nazi party) complied fully with German law.

The lecturer's take: if you join an organisation, either subscribe to its core tenets or resign — your power to change it from within is very limited.

### Common Software Licences

| Type | Examples |
|---|---|
| Open source | GPL, LGPL, Apache, MIT |
| Proprietary | Vendor-specific licences |

### Plagiarism And Authorship

| Why it's unethical for scholars | Why it's unethical for developers |
|---|---|
| Reputations are built on original research | Violates intellectual property |
| Undermines meritocracy | Makes it impossible to track the source of code |
| Dishonest | You can't research its limitations or issues |
| | Makes you look like a fraud |

As a risk: probability high and cost high, so **avoid** it (see the risk matrix in [Dependable Systems](10_Dependable_Systems.md#Security%20And%20The%20Risk%20Matrix)).
