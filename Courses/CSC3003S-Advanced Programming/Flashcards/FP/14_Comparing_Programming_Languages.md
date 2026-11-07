---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 14 — Comparing Programming Languages"
---

# FP 14 — Comparing Programming Languages

**Source note:** [Comparing Programming Languages](../../FP/14_Comparing_Programming_Languages.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Paradigms|Paradigms]]
  - [[#Object-Oriented Variants|Object-Oriented Variants]]
  - [[#Logic Programming|Logic Programming]]

## Core Content

### Paradigms

<!-- qard-id: ap-9f6a88a9ff9a3f0237d1 -->
> [!qard]- What are the two broad families of programming languages?
> Imperative (procedural, object-oriented) and declarative (functional, logic).

<!-- qard-id: ap-7e5d959f523c0cf9bf7c -->
> [!qard]- What is procedural programming and its benefits?
> Code organised sequentially into procedures; abstraction, simplicity and performance.

<!-- qard-id: ap-e0e01e2c98aa0a001aa5 -->
> [!qard]- What is object-oriented programming and its benefits?
> Data and behaviour encapsulated in objects; reuse (inheritance, polymorphism), modularity, encapsulation, abstraction.

<!-- qard-id: ap-401ca47194230db30548 -->
> [!qard]- What is a domain-specific language? Give two examples.
> A language designed for one domain — e.g. Inform 7 (interactive fiction) and Qiskit (quantum programming).

<!-- qard-id: ap-f55569cee126eb93216d -->
> [!qard]- Do languages fit a single paradigm?
> Often not — e.g. Python is class-based OO, procedural and partly functional.

### Object-Oriented Variants

<!-- qard-id: ap-b38c14b62cb3ce5fda1c -->
> [!qard]- Class-based versus prototype-based OOP?
> Class-based: objects instantiate static compile-time classes; subclasses inherit. Prototype-based: objects are cloned and extended from other objects at run time, linked by a prototype chain.

<!-- qard-id: ap-6f3483fc51b686bfbb17 -->
> [!qard]- How does JavaScript find a property or method?
> It walks up the object's prototype chain until it finds the definition.

<!-- qard-id: ap-b1b58006a43ad3856578 -->
> [!qard]- Why is JavaScript called "the world's worst programming language"?
> Built in 10 days, its early flaws were kept for backward compatibility, and it became the web's only native scripting language.

### Logic Programming

<!-- qard-id: ap-b7ae7b57097ca3ea8239 -->
> [!qard]- What is logic programming?
> Declarative programming based on formal logic, using facts, rules and queries.

<!-- qard-id: ap-f436a056ad9e786949ae -->
> [!qard]- What are facts, rules and queries?
> Facts: unconditional statements. Rules: `head :- body` (head true if body true). Queries: questions answered from them.

<!-- qard-id: ap-df6a0e1f992ea40fd117 -->
> [!qard]- What are two benefits of logic programming?
> Separation of logic from control, and reversibility (relations can often be run both ways).

<!-- qard-id: ap-f06e0a9eff4881f55dee -->
> [!qard]- Give the Prolog meaning of `:-`, `,`, `;` and `\+`.
> If, AND, OR, NOT.

<!-- qard-id: ap-1536a939f60afb06a914 -->
> [!qard]- How are Prolog variables and atoms distinguished?
> Variables start with a capital or `_`; atoms start lowercase or are quoted.

<!-- qard-id: ap-8aa4a1bd7cd9ee014312 -->
> [!qard]- How does Prolog answer a query?
> Depth-first search using unification, resolution and backtracking.

<!-- qard-id: ap-39feee7a348deec827dd -->
> [!qard]- What are unification, resolution and backtracking?
> Unification: matching terms by binding variables. Resolution: replacing a goal by a matching rule's body. Backtracking: on failure, returning to the last choice point.
