---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 08 — Software Testing"
---

# ASD 08 — Software Testing

**Source note:** [Software Testing](../../ASD/08_Software_Testing.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Defensive Programming|Defensive Programming]]
  - [[#Automated Testing|Automated Testing]]
  - [[#Unit Testing And TDD|Unit Testing And TDD]]
  - [[#Higher-Level Testing|Higher-Level Testing]]
  - [[#Security Testing|Security Testing]]

## Core Content

### Defensive Programming

<!-- qard-id: ap-702c413af2d22a184d7a -->
> [!qard]- Name five defensive programming techniques.
> Const correctness, input validation, assertions, error handling, resource management.

<!-- qard-id: ap-b16c6fede06c4a1c4397 -->
> [!qard]- What is const correctness?
> Marking methods, objects and parameters that mustn't change, so the compiler enforces it.

<!-- qard-id: ap-d79bba8e60fb7a4777af -->
> [!qard]- Input validation versus assertions?
> Validation guards against bad external input and must run in release code. Assertions catch impossible states, run only in debug, and may be slow.

<!-- qard-id: ap-063750273b7c7960284f -->
> [!qard]- Why must you never put action code inside an assertion?
> Assertions are removed in release builds, so the action would stop running.

<!-- qard-id: ap-8bc3e0479cb862ccec3d -->
> [!qard]- What is design by contract?
> Declaring each routine's pre-conditions and post-conditions as checked assertions.

<!-- qard-id: ap-2b0237fa91ca3d1296df -->
> [!qard]- Exceptions versus error codes?
> Exceptions: zero overhead on the happy path, heavy on errors. Error codes: little overhead either way but much harder to get right.

<!-- qard-id: ap-da3f0402b14a642eb798 -->
> [!qard]- How should errors be handled for users?
> Never silently swallow them, don't leak exceptions to users, and prevent errors in the UI where possible.

<!-- qard-id: ap-e7352c1ac7d90d370dc6 -->
> [!qard]- What is RAII?
> Resource Acquisition Is Initialisation: a resource is released automatically when its owning object goes out of scope.

### Automated Testing

<!-- qard-id: ap-f2016c67aba288d7168e -->
> [!qard]- What is static analysis?
> Checking source code without running it for smells and known bug patterns (e.g. lint).

<!-- qard-id: ap-4071c7370681dd364e82 -->
> [!qard]- What is a code smell?
> A sign of bad practice — duplication, complexity, poor names, globals.

<!-- qard-id: ap-350db5737bb3e4100ee3 -->
> [!qard]- What are code sanitizers? Name three.
> Run-time instrumentation detecting bugs: AddressSanitizer (bad pointers, overflow), MemorySanitizer (uninitialised reads), UBSan, LeakSan, ThreadSan.

<!-- qard-id: ap-e1baae6ff729db225542 -->
> [!qard]- What is fuzzing?
> Feeding randomised input to a program to find crashes, bad error handling and security flaws.

### Unit Testing And TDD

<!-- qard-id: ap-351a44c149030023b9b5 -->
> [!qard]- What is a unit test?
> A test of a small piece of code (a function or class) in isolation, ideally aiming for full coverage.

<!-- qard-id: ap-46f961390072db3f1888 -->
> [!qard]- What are the TDD steps?
> Stub the code, write a failing test, implement until it passes, add a new failing test before each new feature, then make tests comprehensive.

<!-- qard-id: ap-732b5992a0cb1c3cd0de -->
> [!qard]- What is a mock object?
> A stand-in for an unavailable or non-deterministic dependency that records calls and returns programmed values.

<!-- qard-id: ap-b811393a639a900ca5f0 -->
> [!qard]- Partition testing versus guideline testing?
> Partition: group inputs into categories and test their edges. Guideline: choose tests from known common failure points.

### Higher-Level Testing

<!-- qard-id: ap-f2edcd13db238bf58f52 -->
> [!qard]- Unit testing versus integration testing?
> Unit tests check a component alone; integration tests check interactions between modules.

<!-- qard-id: ap-1cb73fba9a411f3abfc7 -->
> [!qard]- Name the integration testing approaches.
> Big-bang (all at once) or incremental: top-down, bottom-up, or sandwich.

<!-- qard-id: ap-346066dd03cf3b629a74 -->
> [!qard]- What is regression testing?
> Re-running existing tests after changes to ensure nothing broke, adding tests as needed.

<!-- qard-id: ap-cade5fe31086b9bc22a4 -->
> [!qard]- What is user acceptance testing?
> Testing that the system is what users wanted, usable and operable, before production.

<!-- qard-id: ap-125fc877edeaba7c9567 -->
> [!qard]- Alpha versus beta testing?
> Alpha: in-house or with super users. Beta: with real end users.

<!-- qard-id: ap-cf30497016dfbd557b39 -->
> [!qard]- Usability testing versus UAT?
> Usability measures ease of use mid-development; UAT validates requirements against functionality at the end.

### Security Testing

<!-- qard-id: ap-4962ccbc4f1687ea1408 -->
> [!qard]- What does "shift left" mean?
> Move testing, quality and security earlier — into design and coding — because late security fixes are nearly impossible.

<!-- qard-id: ap-2b014f672ce99f6cecc0 -->
> [!qard]- What is the top 2021 OWASP vulnerability and its fix?
> Broken access control — deny by default.

<!-- qard-id: ap-9114fba1497d770b1136 -->
> [!qard]- What is penetration testing?
> Simulating attacks to discover security vulnerabilities.

<!-- qard-id: ap-42895708db04bbd1c011 -->
> [!qard]- What does "absence of proof is not proof of absence" mean for testing?
> Passing tests don't prove there are no bugs.

<!-- qard-id: ap-cb3147725c2dcd677ece -->
> [!qard]- What are TDD's main benefits?
> Tests exist before code, so every feature is tested, failures show exactly what's missing, and coverage grows with the code.
