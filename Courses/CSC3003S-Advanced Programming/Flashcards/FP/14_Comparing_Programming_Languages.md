---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 14 — Comparing Programming Languages"
---

# FP 14 — Comparing Programming Languages

**Source note:** [Comparing Programming Languages](../../FP/14_Comparing_Programming_Languages.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Programming Paradigms|Programming Paradigms]]
  - [[#Logic Programming|Logic Programming]]
  - [[#Imperative: Procedural And Object-Oriented|Imperative: Procedural And Object-Oriented]]
  - [[#JavaScript: Prototypes And Flaws|JavaScript: Prototypes And Flaws]]
  - [[#Prolog Example: Lineage|Prolog Example: Lineage]]
  - [[#Prolog Syntax: Penguins Example|Prolog Syntax: Penguins Example]]
  - [[#Purpose|Purpose]]
  - [[#Comparing Paradigms|Comparing Paradigms]]
  - [[#Prolog Terms And Clauses|Prolog Terms And Clauses]]

## Core Content

### Programming Paradigms

<!-- qard-id: ap-bc973d01f8c6fd9d196d -->
> [!qard]- How do procedural, object-oriented, functional and logic programming organise a solution?
> Procedures and explicit state changes; objects combining state and behaviour; function application/composition; facts and rules queried by an inference engine.

<!-- qard-id: ap-b9efef6c38dab56e08ab -->
> [!qard]- How does prototype-based OO differ from class-based OO?
> Prototype-based objects delegate to other objects along a prototype chain; class-based objects are instances of classes with declared inheritance relationships.

<!-- qard-id: ap-df89d56aa7aea8530b88 -->
> [!qard]- What happens when a JavaScript property is missing on an object?
> Lookup continues along its prototype chain until the property is found or the chain ends.

<!-- qard-id: ap-f85409e280b91f5ba2db -->
> [!qard]- Why can a language belong to several paradigms?
> Languages may support several styles; Python, for example, supports procedural, class-based OO and functional constructs.

### Logic Programming

<!-- qard-id: ap-e1b6b7c281e67aa16ccd -->
> [!qard]- What are facts, rules and queries in Prolog?
> Facts assert relationships; rules infer a head from a body; queries ask the engine to find proofs and variable bindings.

<!-- qard-id: ap-221eab1d788b1ed5bb52 -->
> [!qard]- What do `:-`, `,`, `;` and `.` mean in Prolog?
> “If”, conjunction, disjunction, and clause termination respectively.

<!-- qard-id: ap-87cbdb5a42af9d26adfa -->
> [!qard]- How are Prolog variables distinguished from atoms?
> Variables begin uppercase or with `_`; atoms generally begin lowercase or are single-quoted.

<!-- qard-id: ap-29dc96c5d63ebe16ebd8 -->
> [!qard]- What is unification?
> Finding consistent substitutions for variables that make two terms match.

<!-- qard-id: ap-7215e1fe9f37dfc107c3 -->
> [!qard]- How does Prolog use resolution and backtracking?
> Match a goal to a clause, replace it with the clause's subgoals, and search depth-first. On failure, return to a choice point and try another alternative.

<!-- qard-id: ap-0da4e38b56d1ac666d92 -->
> [!qard]- Why can clause and goal order affect a Prolog program?
> The search is depth-first, so an unproductive branch may delay or prevent finding another valid solution.

<!-- qard-id: ap-4b93ea8f507da7637bde -->
> [!qard]- What does `\+ Goal` mean in Prolog?
> Negation as failure: it succeeds when the attempted goal cannot be proved, rather than establishing classical logical negation.

### Imperative: Procedural And Object-Oriented

<!-- qard-id: ap-bed4313ad5c15fbec642 -->
> [!qard]- What benefits do procedural and OO styles emphasise, and what state issue distinguishes them from pure FP?
> Procedures organise reusable steps; objects group data and behaviour for modularity, encapsulation and polymorphism. Both commonly permit mutable state, unlike pure functional transformations.

### JavaScript: Prototypes And Flaws

<!-- qard-id: ap-fbc1c6ac62e37c47adbc -->
> [!qard]- What does JavaScript's default numeric-sort example illustrate?
> Default array sorting compares string forms, so `10` may precede `2`; a numeric comparison function is needed. A language's default semantics can surprise a programmer applying another language's assumptions.

### Prolog Example: Lineage

<!-- qard-id: ap-c12572dd258a4e6adb57 -->
> [!qard]- How do Prolog rules express siblings and grandmothers?
> Siblings share a parent and are distinct: `parent(Z,X), parent(Z,Y), X \= Y`. A grandmother satisfies `parent(X,Z), parent(Z,Y), female(X)`; queries can leave variables free to find matching relatives.

### Prolog Syntax: Penguins Example

<!-- qard-id: ap-189f7798cef2f203f03d -->
> [!qard]- How does the penguin example derive `is_penguin(kowalski)`?
> Use `is_penguin(X) :- is_bird(X), can_swim(X)` and `is_bird(X) :- has_feathers(X)`. Kowalski satisfies both facts; a feathered bird without swimming evidence does not satisfy this rule.

### Purpose

<!-- qard-id: ap-9a745fe5fcd0f34c3565 -->
> [!qard]- How do a general-purpose paradigm and a domain-specific language differ?
> A paradigm is a broad way of organising computation; a DSL offers specialised vocabulary/constructs for a particular domain, such as Inform 7's story worlds or quantum-circuit tools.

### Comparing Paradigms

<!-- qard-id: ap-61a9f14b588350f39504 -->
> [!qard]- What does OO encapsulation protect?
> A representation and its invariants behind a chosen interface, allowing clients to use behaviour without depending on every internal field.

<!-- qard-id: ap-adcec02dd6c4f366fc26 -->
> [!qard]- How do inheritance and delegation differ as reuse mechanisms?
> Inheritance uses a declared type/class relationship; delegation forwards an operation to another object, including a prototype, to provide behaviour.

<!-- qard-id: ap-2572d5512843dca9a17d -->
> [!qard]- Can a prototype chain be changed at runtime in the JavaScript model described here?
> Yes. Dynamic links/property changes can alter where inherited behaviour is found; this flexibility affects reasoning about object behaviour.

<!-- qard-id: ap-d3f2684b380e181c48d2 -->
> [!qard]- Why does a language's classification not imply every program in it follows that style?
> A multi-paradigm language supplies several constructs; the programmer's chosen organisation and discipline determine the actual style.

### Prolog Terms And Clauses

<!-- qard-id: ap-56a5ea8d3cd1b8ff535d -->
> [!qard]- How does a Prolog fact differ syntactically from a rule with subgoals?
> A fact is an unconditional clause such as `parent(a,b).`; a rule uses `Head :- Body.` to make the head depend on proving its body.

<!-- qard-id: ap-c1923c79393614c85931 -->
> [!qard]- What distinguishes a query with a concrete term from one with a variable?
> The first asks whether that relationship can be proved; the second can request substitutions making it true, possibly with several answers.

<!-- qard-id: ap-62507cd1a775eb0e0fa5 -->
> [!qard]- How does Prolog's comma affect proof obligations?
> All conjunctive subgoals must succeed with consistent variable bindings; the same variable name connects their constraints within the clause/query.

<!-- qard-id: ap-c4fdb90b405335cb4c4d -->
> [!qard]- How does Prolog's semicolon affect search?
> It offers alternative goals; a solution may come from either branch, with backtracking exploring alternatives as needed.

<!-- qard-id: ap-72f0116d658c9fffa76f -->
> [!qard]- What does resolving a goal against a rule do after unification?
> Replace the matched goal with the rule body's required subgoals under the resulting consistent substitution.

<!-- qard-id: ap-2dc5f3990e1d56da20a9 -->
> [!qard]- What information must backtracking restore?
> The choice point and bindings dependent on the failed alternative, so the next alternative can be explored without incompatible leftover assignments.

<!-- qard-id: ap-56d8f0d2ee6d39ed2b71 -->
> [!qard]- Why does depth-first search create a termination risk for an otherwise answerable Prolog query?
> An infinite or unproductive earlier branch can prevent reaching a later successful alternative; logical expressiveness alone does not fix search order.

<!-- qard-id: ap-d8ad865c08d9e10ea1f8 -->
> [!qard]- What does “reversibility” mean for a relation compared with an ordinary input/output function?
> Different argument positions may be left unknown and solved through the same relation, subject to the program's operational behaviour and termination.

<!-- qard-id: ap-15b14c5a1b61d1259c70 -->
> [!qard]- How does the sibling rule avoid identifying a person as their own sibling?
> It requires a shared parent plus a distinctness condition on the two people, not shared parentage alone.
