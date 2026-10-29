---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 08 — Software Testing"
---

# ASD 08 — Software Testing

**Source note:** [Software Testing](../../ASD/08_Software_Testing.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Prevention And Detection|Prevention And Detection]]
  - [[#Designing Tests|Designing Tests]]
  - [[#Testing Levels And Purpose|Testing Levels And Purpose]]
  - [[#Types Of Testing And No Silver Bullet|Types Of Testing And No Silver Bullet]]
  - [[#Const Correctness|Const Correctness]]
  - [[#Error Handling And Exceptions|Error Handling And Exceptions]]
  - [[#Resource Management And Compiler Warnings|Resource Management And Compiler Warnings]]
  - [[#Code Sanitisers And Fuzzing|Code Sanitisers And Fuzzing]]
  - [[#Unit Tests And Coverage|Unit Tests And Coverage]]
  - [[#Selecting Test Cases|Selecting Test Cases]]
  - [[#Regression Testing|Regression Testing]]
  - [[#User Acceptance Testing|User Acceptance Testing]]
  - [[#Security Testing|Security Testing]]
  - [[#Defensive Programming And Failure|Defensive Programming And Failure]]
  - [[#Test Evidence|Test Evidence]]

## Core Content

### Prevention And Detection

<!-- qard-id: ap-e9248c3f55101f51b734 -->
> [!qard]- Why combine reviews, static analysis and several testing techniques?
> They expose different defect classes; passing one kind of check cannot establish that the system is correct.

<!-- qard-id: ap-d4860b7c2e4fe9f282b1 -->
> [!qard]- How does defensive programming protect a component?
> Validate external input, enforce appropriate invariants, handle errors and manage resources so misuse does not silently corrupt state.

<!-- qard-id: ap-f284d78d8e6a960765c2 -->
> [!qard]- How do input validation and assertions differ?
> Validation handles potentially invalid external input and must work in production. Assertions check programmer assumptions/invariants and may be disabled.

<!-- qard-id: ap-cb9152b152843edeb48d -->
> [!qard]- Why must an assertion not contain essential actions?
> If assertions are disabled, the expression may not run, silently removing required program behaviour.

<!-- qard-id: ap-f35198eb85d935f4eb7c -->
> [!qard]- What do preconditions, postconditions and invariants specify?
> Valid starting inputs/state, promised results/end state, and properties that must remain true at the relevant program points.

<!-- qard-id: ap-a221624de9db298e4d8c -->
> [!qard]- How do RAII or guaranteed cleanup help error handling?
> They release resources on all relevant exits, including exceptional ones, rather than relying on every caller remembering manual cleanup.

<!-- qard-id: ap-9c4fef85c39e6c6e941b -->
> [!qard]- How does static analysis differ from a runtime sanitiser?
> Static analysis examines code without executing it. A sanitiser instruments execution to detect issues on exercised paths, such as invalid memory access.

<!-- qard-id: ap-1f69e2d63f72312fa49c -->
> [!qard]- What does fuzzing test?
> Behaviour under many generated or mutated inputs, seeking crashes, violated properties and security flaws, especially in input and error handling.

### Designing Tests

<!-- qard-id: ap-62bb142b41b7d99b0b01 -->
> [!qard]- What does a unit test isolate, and when is a mock useful?
> A small function/component. A mock substitutes a dependency such as a clock, database or API so behaviour and interactions can be controlled and observed.

<!-- qard-id: ap-3ebdc5fc19dbb521b7b9 -->
> [!qard]- Why does high code coverage not prove correctness?
> Execution of a line or branch does not establish a correct assertion or exercise every input combination and failure mode.

<!-- qard-id: ap-4b104fc3d17d06551ed7 -->
> [!qard]- What is the TDD cycle?
> Write a test that fails for missing behaviour, implement enough to pass, then refactor while retaining passing tests; repeat for the next behaviour.

<!-- qard-id: ap-94b2eeb4a15d760a9a9c -->
> [!qard]- How does partition testing guide test selection?
> Divide inputs into behaviourally distinct categories, choose representatives, and test boundaries where classifications change.

<!-- qard-id: ap-e8f5b0ff45518a8763ac -->
> [!qard]- Why include empty, minimum, maximum and just-outside-boundary inputs?
> Off-by-one errors, missing base cases and representation limits commonly appear there even when normal examples work.

### Testing Levels And Purpose

<!-- qard-id: ap-2faaadf65c6390e8227c -->
> [!qard]- Why are integration tests needed when unit tests pass?
> Correct isolated parts can still disagree on interfaces, sequencing, data formats or assumptions when connected.

<!-- qard-id: ap-17521db2d5bb41674b76 -->
> [!qard]- What are big-bang, top-down and bottom-up integration?
> Assemble everything at once; progressively integrate higher-level modules using stand-ins below; or progressively integrate lower-level modules using drivers above.

<!-- qard-id: ap-8db3bd693676feb68ba3 -->
> [!qard]- What is regression testing?
> Re-run relevant existing tests after changes to catch broken previously working behaviour, and add a test for each fixed failure where useful.

<!-- qard-id: ap-0583fc7f3a258e104065 -->
> [!qard]- What does user acceptance testing establish?
> Whether the delivered system meets user needs and agreed requirements in its intended use, including practical operational readiness.

<!-- qard-id: ap-e8ef1fd93c7c39402794 -->
> [!qard]- How do alpha and beta testing differ in the notes?
> Alpha testing uses late prototypes internally or with selected experienced users; beta testing exposes the system to end users.

<!-- qard-id: ap-4d5b929254305728cf74 -->
> [!qard]- What does “shift left” mean for quality and security?
> Address risks earlier in requirements, design and implementation, using early checks rather than relying on final-stage testing.

### Types Of Testing And No Silver Bullet

<!-- qard-id: ap-ca1b652ded6902953247 -->
> [!qard]- How do functional, load, stress, scalability and volume tests ask different questions?
> Functional: correct behaviour; load: behaviour at expected workload; stress: beyond expected limits; scalability: behaviour as resources/workload grow; volume: handling large amounts of data.

### Const Correctness

<!-- qard-id: ap-37ec1fbf448c7d5d5bf5 -->
> [!qard]- What does const correctness make explicit, and why is it not automatically full immutability?
> Which binding/object operations may modify state through an interface. A fixed reference, such as Java `final`, does not by itself make all reachable objects immutable; respect the language's actual guarantees.

<!-- qard-id: ap-56ee52e4177f639de8dc -->
> [!qard]- What does a C++ const member function promise about ordinary object state?
> It cannot modify ordinary non-mutable members through its const `this` interface. That constraint is narrower than a universal promise of no external effects or deep immutability of every referenced object.

<!-- qard-id: ap-a229e789204038d4b53b -->
> [!qard]- How does a const-qualified input interface help distinguish a query from an update?
> It lets callers and the compiler enforce that the operation does not modify state through that interface, making permitted mutation explicit rather than relying on naming or comments alone.

### Error Handling And Exceptions

<!-- qard-id: ap-99b3ae239fcca36b6582 -->
> [!qard]- How do exception-based and error-code approaches differ in design, beyond syntax?
> Exceptions separate failure propagation from the ordinary path; error results make failure explicit at call sites. Either needs consistent handling, cleanup and meaningful recovery; never silently discard an unresolved error.

### Resource Management And Compiler Warnings

<!-- qard-id: ap-7db82d9a442094972a66 -->
> [!qard]- Why use strong compiler warnings during development?
> They surface suspicious conversions, unused values and other likely defects before runtime. Investigate warnings rather than assuming successful compilation establishes correct behaviour.

### Code Sanitisers And Fuzzing

<!-- qard-id: ap-efa2900714c6b4817f4f -->
> [!qard]- Which defect classes do AddressSanitizer, MemorySanitizer, UBSan and ThreadSanitizer target?
> Invalid memory accesses/use-after-free; uninitialised-value use; supported undefined behaviours; and data races respectively. Leak checks target unreleased allocations; no tool detects every fault or unexecuted path.

### Unit Tests And Coverage

<!-- qard-id: ap-b65bcdbc4b6e4c3be262 -->
> [!qard]- Which three faults does the notes' factorial example illustrate?
> Returning `n` for `n<=1` makes `0!` wrong; calling `factorial(n)` instead of `factorial(n-1)` fails to progress; too-small integer types overflow. Test base cases, recursion and representable limits separately.

### Selecting Test Cases

<!-- qard-id: ap-e29d47659e119e526a98 -->
> [!qard]- How does guideline testing complement partition/boundary testing?
> It chooses cases based on known defect patterns and past failures, not just the current input partitions; use both to cover likely mistakes and structurally different behaviours.

### Regression Testing

<!-- qard-id: ap-b52cf56ced6eb927a832 -->
> [!qard]- How do retest-all, test selection and prioritisation differ after a change?
> Retest-all runs the whole suite; selection chooses tests related to affected behaviour; prioritisation orders tests so likely or serious regressions are detected earlier.

### User Acceptance Testing

<!-- qard-id: ap-c435708467ababa37b47 -->
> [!qard]- How does usability testing differ in emphasis from UAT?
> Usability measures how effectively/easily people interact with the product; UAT validates that it meets their agreed needs and is operationally acceptable. Either may reveal issues invisible in unit tests.

### Security Testing

<!-- qard-id: ap-c44ac0f594ec1c96bf91 -->
> [!qard]- How do vulnerability scanning, penetration testing and a security audit differ?
> Automated scanning looks for recognised weaknesses; penetration testing attempts realistic exploitation; an audit examines controls, design and evidence against requirements. None replaces building secure boundaries from the start.

### Defensive Programming And Failure

<!-- qard-id: ap-2e6d776a70e692489e7c -->
> [!qard]- What is a code smell compared with a demonstrated bug?
> A sign that design/code may be problematic, such as duplication or excessive complexity; it prompts investigation but does not alone prove incorrect output.

<!-- qard-id: ap-9368e0675b6c1ce8ca3e -->
> [!qard]- Why is external-input rejection different from an internal invariant failure?
> External invalid data is an anticipated boundary condition needing production handling; an invariant failure suggests a violated programming assumption or defect.

<!-- qard-id: ap-185e775f1e8320a99c98 -->
> [!qard]- Why should resource cleanup work when an exception interrupts the normal path?
> Open files/locks/memory otherwise remain allocated or held precisely in failure conditions; scope-bound cleanup or guaranteed-finalisation constructs cover those exits.

<!-- qard-id: ap-1474b4b78d5451a3704c -->
> [!qard]- How can interface design prevent a user error rather than merely report it?
> Restrict choices to valid values/actions or clearly constrain input, reducing avoidable invalid states; still validate untrusted input at the actual boundary.

### Test Evidence

<!-- qard-id: ap-bb8f25f43ec5884304d4 -->
> [!qard]- How does a mock differ from using the actual remote dependency in a unit test?
> It controls expected outputs/failures and records interactions locally, making isolation and repeatability possible; it does not prove the real integration works.

<!-- qard-id: ap-969adba21abbdfc2bd8b -->
> [!qard]- What should an interaction assertion check when the dependency call itself is the behaviour under test?
> The intended method, arguments and relevant call count/order, rather than merely that a mock accepted some arbitrary call.

<!-- qard-id: ap-bca208fdccdeee8560da -->
> [!qard]- Why test a partition's boundaries on both sides?
> Incorrect comparison operators and off-by-one limits often misclassify values exactly at or just outside the transition.

<!-- qard-id: ap-c6f9f0ec099d97978cfa -->
> [!qard]- What is the limitation of testing only “happy path” examples?
> It can miss invalid inputs, empty cases, resource failure, boundary values and interactions, which often need different handling.

<!-- qard-id: ap-e5d54e3579e5af43e815 -->
> [!qard]- How does a failing-first TDD test show that a test is meaningful?
> It demonstrates that the check detects the currently missing behaviour; a test already passing for unrelated reasons may not constrain the intended change.

<!-- qard-id: ap-690a8688378bafe7a93d -->
> [!qard]- Why refactor after tests pass rather than allow each patch to accumulate?
> Improve structure while the behavioural checks protect existing functionality, controlling duplication and complexity introduced during incremental implementation.

<!-- qard-id: ap-45dd8829f61c7857f63d -->
> [!qard]- What does a runtime sanitiser need in order to detect a path-specific failure?
> An execution/input that exercises the relevant operation plus instrumentation for that fault class; untouched paths remain untested.

<!-- qard-id: ap-70d55fe49814c3054588 -->
> [!qard]- How do black-box and white-box fuzzing differ in available guidance?
> Black-box generation observes external behaviour; white-box/coverage-guided approaches can use internal structure or execution feedback to explore new paths.

<!-- qard-id: ap-d883d45a1a0562f64d76 -->
> [!qard]- Why can integration fail through assumptions even if each module's unit tests are correct?
> Each module may have been tested against different data formats, ordering, units, timing or error contracts than the other actually provides.

<!-- qard-id: ap-e2e9c52b0f3b8087024c -->
> [!qard]- Why include regression checks for a fixed defect?
> They preserve the discovered failing condition as future evidence, preventing a later change from quietly reintroducing it.
