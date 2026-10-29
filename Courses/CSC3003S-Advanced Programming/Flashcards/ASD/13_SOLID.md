---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 13 — SOLID Design Principles"
---

# ASD 13 — SOLID Design Principles

**Source note:** [SOLID Design Principles](../../ASD/13_SOLID.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Focused Responsibilities And Extension|Focused Responsibilities And Extension]]
  - [[#Substitutability And Contracts|Substitutability And Contracts]]
  - [[#Interfaces And Dependency Direction|Interfaces And Dependency Direction]]
  - [[#What Is A Responsibility?|What Is A Responsibility?]]
  - [[#Extension Mechanisms|Extension Mechanisms]]
  - [[#L — Liskov Substitution Principle|L — Liskov Substitution Principle]]
  - [[#Design By Contract|Design By Contract]]
  - [[#No God Classes|No God Classes]]
  - [[#I — Interface Segregation Principle|I — Interface Segregation Principle]]
  - [[#Applying The Principles|Applying The Principles]]

## Core Content

### Focused Responsibilities And Extension

<!-- qard-id: ap-27148c704d01d4f28a0f -->
> [!qard]- What is the Single Responsibility Principle?
> A component should have one reason to change: gather behaviour that changes together and separate independent responsibilities.

<!-- qard-id: ap-a2b57f30bd406f573eb7 -->
> [!qard]- Why can a class that both draws a rectangle and computes its area violate SRP?
> Presentation and geometry change for different reasons; entangling them couples independent clients and risks unrelated breakage.

<!-- qard-id: ap-31e7c1de93ebcdd137df -->
> [!qard]- What does the Open–Closed Principle recommend?
> Allow anticipated new behaviour through extension points rather than repeatedly modifying stable existing logic.

<!-- qard-id: ap-529e9c699c8b455d0bcc -->
> [!qard]- How can interfaces and composition support OCP?
> Add another implementation behind an existing abstraction or compose another behaviour, allowing client logic to stay unchanged.

### Substitutability And Contracts

<!-- qard-id: ap-cb46eb6ad2d9d8521d11 -->
> [!qard]- What does the Liskov Substitution Principle require?
> A subtype must honour the base type's behavioural contract so callers using the base abstraction remain correct without special cases.

<!-- qard-id: ap-56b22e9d3fca4dd247eb -->
> [!qard]- Why can mutable Square-as-Rectangle violate LSP?
> A Rectangle client may change width and height independently; a Square must keep them equal, so it cannot preserve that contract for those setters.

<!-- qard-id: ap-4f5432f45c3739fbc352 -->
> [!qard]- Does mathematical “is a” automatically justify implementation inheritance?
> No. Substitutability depends on supported operations, invariants and observable behaviour, not just a mathematical classification.

<!-- qard-id: ap-c90c1aec887f68a0cbd4 -->
> [!qard]- How do preconditions and postconditions constrain a behavioural subtype?
> It must not require stronger preconditions or promise weaker postconditions than the base contract; it must preserve required invariants.

<!-- qard-id: ap-9d877839a056c4139f21 -->
> [!qard]- When should HAS-A composition replace inheritance?
> When a component uses or delegates to another rather than being a valid behavioural substitute for it.

### Interfaces And Dependency Direction

<!-- qard-id: ap-806618939fc2b386d12c -->
> [!qard]- What is the Interface Segregation Principle?
> Clients should not depend on operations they do not use; provide small interfaces aligned with client needs.

<!-- qard-id: ap-1c974b53a1e821c159ca -->
> [!qard]- How does splitting an ATM's large UI interface help transactions?
> Deposit, withdrawal and transfer clients depend only on their own operations, reducing accidental coupling and the impact of unrelated changes.

<!-- qard-id: ap-d9f7ee0cf8bb8404f397 -->
> [!qard]- What is the Dependency Inversion Principle?
> High-level policy and low-level details both depend on abstractions; details implement those abstractions rather than dictate the policy's dependencies.

<!-- qard-id: ap-8d96bd9a5f23da38fa0e -->
> [!qard]- How does a copy routine using Reader and Writer abstractions apply DIP?
> The copy policy depends on reading/writing contracts; keyboard, file and printer details implement them, so devices can change without rewriting the policy.

<!-- qard-id: ap-4498bba38fcfa553497e -->
> [!qard]- How do ISP and DIP solve different dependency problems?
> ISP narrows which operations a client depends on; DIP changes the dependency's target from a concrete detail to an abstraction.

### What Is A Responsibility?

<!-- qard-id: ap-00e945c50bafc69e56c4 -->
> [!qard]- How does the modem example separate responsibilities without requiring two physical devices?
> Connection control (`dial`, `hangup`) and data transfer (`send`, `receive`) get separate interfaces; one implementation may supply both, while each client depends only on what it uses.

### Extension Mechanisms

<!-- qard-id: ap-f8f1f357703e491e0ea4 -->
> [!qard]- How do interface implementations and message handlers allow extension without device-specific branches everywhere?
> New implementations satisfy existing contracts; new handlers receive defined messages. Clients use the abstraction/message rather than growing concrete-type tests. The course excludes advanced compile-time mixin/CRTP details.

### L — Liskov Substitution Principle

<!-- qard-id: ap-9288911983579974add5 -->
> [!qard]- Why can a function switching on every concrete subtype violate both LSP's intent and OCP?
> It cannot operate through the base contract alone and must change when a new subtype is added. Push the supported operation behind the appropriate abstraction rather than hard-coding a closed list of class identities.

### Design By Contract

<!-- qard-id: ap-4accbf18ca15565cbbe4 -->
> [!qard]- Why are contracts not a proof that the whole program is correct?
> They express/check selected assumptions and guarantees, possibly only on executed paths. Missing specifications, unchecked paths and other logical errors remain; valid error recovery is distinct from violating a promised contract.

### No God Classes

<!-- qard-id: ap-b7fec9d2743a7d26f3bd -->
> [!qard]- Which combination of symptoms identifies the lecture's god-class problem?
> High functional complexity, low cohesion and direct use of many other classes' attributes: too many responsibilities and dependencies accumulate in one place.

### I — Interface Segregation Principle

<!-- qard-id: ap-4ecb06ceca08a85a3292 -->
> [!qard]- How does the TimedDoor adapter avoid burdening every Door with timer behaviour?
> Keep ordinary door operations in `IDoor`; only a timed door owns or implements a timer-client adapter that forwards timeout events. Plain doors need not depend on unused timer methods.

### Applying The Principles

<!-- qard-id: ap-72b54987df3d907c8420 -->
> [!qard]- Does SRP mean every class must contain exactly one method?
> No. Methods supporting one coherent reason for change can belong together; unrelated change drivers indicate multiple responsibilities.

<!-- qard-id: ap-f23ae8ac6ff8b896e5cc -->
> [!qard]- Why can splitting an interface improve SRP without splitting its one implementation into several objects?
> Clients' dependency surfaces and implementation storage are separate choices. One concrete object may implement several focused roles.

<!-- qard-id: ap-eff8e1d11f941c100b8d -->
> [!qard]- Does OCP mean existing code must never be corrected?
> No. It guides adding anticipated behaviour through stable abstractions; bug fixes and mistaken abstraction/design changes still require deliberate edits.

<!-- qard-id: ap-35ded87493dcbdcaefda -->
> [!qard]- Why should an OCP extension point be chosen around plausible variation?
> Generalising every imagined future need creates speculative complexity. Preserve stable policy and expose variation supported by the real requirements.

<!-- qard-id: ap-774404eef019f6ed3809 -->
> [!qard]- How can a subtype strengthen a precondition and thereby break LSP?
> It rejects inputs the base contract allowed, so a previously valid base-type caller can fail when given the subtype.

<!-- qard-id: ap-c101c8656c9bc25a79c7 -->
> [!qard]- How can a subtype weaken a postcondition and thereby break LSP?
> It returns less than the base contract promised, invalidating callers relying on that guarantee even if input types still match.

<!-- qard-id: ap-01a1f230516014a3936e -->
> [!qard]- Why is preserving a subtype's own invariant insufficient for LSP?
> It must also preserve the base abstraction's client-visible contract; keeping a square square can still break a mutable rectangle client's independent-dimension expectations.

<!-- qard-id: ap-237ae3103f889c8028f8 -->
> [!qard]- How does composition express a HAS-A relationship differently from subtype inheritance?
> A component owns/uses another and delegates selected operations without claiming it can substitute for that component's full interface.

<!-- qard-id: ap-50ad34fb8a21b5fea3fd -->
> [!qard]- How does a timer capability forced into every Door violate ISP?
> Plain door clients/implementations depend on methods they do not need, so unrelated timer changes or obligations affect them.

<!-- qard-id: ap-4922500b29b9ce00c4e3 -->
> [!qard]- Why can many small interfaces still be implemented by one concrete UI?
> Interface segregation limits what each client knows, not necessarily the number of implementation objects.

<!-- qard-id: ap-2c367d8d0ab89e74c227 -->
> [!qard]- What distinguishes dependency inversion from simply inserting another concrete wrapper?
> The high-level policy must depend on a stable abstraction; details implement it. More layers with the same wrong concrete dependency direction do not supply DIP.

<!-- qard-id: ap-4ea2e82bc28d8ad0a09d -->
> [!qard]- Who should determine the useful shape of Reader/Writer contracts in the copy example?
> The policy's required operations, rather than accidental device details, so different devices can satisfy the same reusable need.

<!-- qard-id: ap-06db08a0d0284a38d753 -->
> [!qard]- Why does a growing switch on printer/disk/output types undermine the copy routine's reuse?
> Each new device modifies high-level logic and embeds low-level knowledge; an output abstraction moves those differences behind implementations.

<!-- qard-id: ap-ac8025275abd1e3946d5 -->
> [!qard]- How can SOLID principles reinforce one another in an extension?
> Focused responsibilities and small interfaces define stable abstractions; substitutable implementations then add behaviour without concrete-type branches or broad client changes.

<!-- qard-id: ap-653d02b7c42e08c8725d -->
> [!qard]- Why must a design still consider the cost of indirection after applying SOLID?
> Extra boundaries can add complexity/dispatch/coordination overhead; choose abstractions that reduce meaningful change risk without unnecessary layers.
