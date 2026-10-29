---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 18 — Aspect-Oriented Programming And Design Patterns Recap"
---

# ASD 18 — Aspect-Oriented Programming And Design Patterns Recap

**Source note:** [Aspect-Oriented Programming And Design Patterns Recap](../../ASD/18_Aspect_Oriented_Programming.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Crosscutting Concerns|Crosscutting Concerns]]
  - [[#Weaving And Trade-offs|Weaving And Trade-offs]]
  - [[#Example: Capislack Bank|Example: Capislack Bank]]
  - [[#Pointcut Expressions|Pointcut Expressions]]
  - [[#Kinds Of Advice|Kinds Of Advice]]
  - [[#Design Patterns Recap: Behavioural (Lambda For The Win)|Design Patterns Recap: Behavioural (Lambda For The Win)]]
  - [[#Selecting Crosscutting Behaviour|Selecting Crosscutting Behaviour]]
  - [[#Advice Semantics|Advice Semantics]]
  - [[#Weaving, Testing And Architecture|Weaving, Testing And Architecture]]

## Core Content

### Crosscutting Concerns

<!-- qard-id: ap-df78d92ab2391294185f -->
> [!qard]- What is a crosscutting concern?
> A responsibility such as logging or access checks that applies at many places across otherwise separate modules.

<!-- qard-id: ap-b8524ec38eb197c4ce15 -->
> [!qard]- How can AOP reduce shotgun surgery?
> Put the shared intervention in one aspect and apply it at selected execution points rather than editing every affected method separately.

<!-- qard-id: ap-6341fe5deb0af8900e6d -->
> [!qard]- How do advice, pointcut and aspect relate?
> Advice is the inserted behaviour; a pointcut selects where it applies; an aspect combines that selection and behaviour.

<!-- qard-id: ap-12d625bb0b8f6d77701c -->
> [!qard]- What does “before” advice do compared with “around” advice?
> Before advice runs ahead of the selected operation. Around advice wraps it and can control whether/how the operation proceeds and process the result.

<!-- qard-id: ap-f9712ce50fa45d81fc2c -->
> [!qard]- How do after-returning and after-throwing advice differ?
> They run after normal completion and after exceptional completion respectively; select them according to the condition the intervention needs.

<!-- qard-id: ap-37016d94ef46d2b527d4 -->
> [!qard]- Why must pointcut selection be reviewed when method signatures or names change?
> Its matching rules may stop selecting required operations or begin selecting unintended ones, even if those methods still compile.

### Weaving And Trade-offs

<!-- qard-id: ap-4cf3f576944763b4c41f -->
> [!qard]- What does weaving do in AspectJ?
> Combines aspects with the selected application code, for example through an extra compilation/instrumentation step.

<!-- qard-id: ap-16d72a7c535faef9489c -->
> [!qard]- What is reflection, and how do static and dynamic forms differ in these notes?
> Inspection of program structure/behaviour; static mechanisms operate during compilation, while dynamic mechanisms operate at runtime.

<!-- qard-id: ap-7b6212c20a1d7434b843 -->
> [!qard]- What are AOP's main modularity benefits?
> Centralised reusable interventions reduce scattered duplication, separating a crosscutting responsibility from ordinary domain logic.

<!-- qard-id: ap-9321130896c323c20041 -->
> [!qard]- Why can AOP make debugging and comprehension harder?
> Visible method bodies no longer show all executed behaviour; overlapping advice and hidden matching rules require suitable tooling and careful reasoning.

<!-- qard-id: ap-fff75dd1044d2dab2536 -->
> [!qard]- When might AOP be useful in an existing system?
> A shared intervention must apply across many established classes without duplicating edits, and the team can reliably specify, inspect and test all intended join points.

<!-- qard-id: ap-b9ae53db7935a15d3ebd -->
> [!qard]- How do lambdas simplify several behavioural patterns?
> Store the varying action directly as a function value, e.g. callbacks for commands, subscriptions or handlers, instead of a separate class for every small behaviour.

### Example: Capislack Bank

<!-- qard-id: ap-e559d1d5b8cf847d12db -->
> [!qard]- How does the bank example use AOP to add checks without editing every transaction method?
> Select relevant loan/insurance/customer operations with a pointcut; before advice checks the client constraints and prevents invalid work. Verify the selector reaches every intended operation.

### Pointcut Expressions

<!-- qard-id: ap-10df57bc83092734f9b5 -->
> [!qard]- What does a pointcut expression match, and why are Boolean combinations useful?
> Selected execution/join-point properties such as class, method and signature; AND narrows a selection and OR combines alternatives. Framework pattern syntax is specialised, not necessarily arbitrary regular expressions.

### Kinds Of Advice

<!-- qard-id: ap-7ff9c5a2bcfdd4edcafd -->
> [!qard]- How does finally-style after advice differ from after-returning or after-throwing advice?
> It runs after completion regardless of normal return or exception, while the other two select one completion mode; choose the appropriate form for cleanup, results or failure logging.

### Design Patterns Recap: Behavioural (Lambda For The Win)

<!-- qard-id: ap-5c5bc6055d8bcf33d384 -->
> [!qard]- How do callbacks map onto the lecture's behavioural-pattern recap?
> A lambda can supply a command action, strategy choice, template step, observer subscription, chain handler or mediator endpoint. Keep the surrounding lifetime, ordering and ownership rules explicit even when no extra class is needed.

### Selecting Crosscutting Behaviour

<!-- qard-id: ap-22e4bd31e26375d78858 -->
> [!qard]- What makes a concern crosscutting rather than simply a large method?
> Its same responsibility is scattered across otherwise separate components/operations, so changing it requires coordinated interventions in many locations.

<!-- qard-id: ap-06ba51ffa82b1fe9fc96 -->
> [!qard]- How does a pointcut differ from the advice's business check?
> The pointcut chooses where advice runs; the advice examines conditions/performs behaviour there. Correct checking code is ineffective if the selector misses required sites.

<!-- qard-id: ap-6f10b92a3493c4f5a97f -->
> [!qard]- What information can a join-point object provide to advice in the lecture's example?
> Details of the selected invocation, such as its arguments, allowing checks to inspect the client ID before the underlying method proceeds.

<!-- qard-id: ap-eb2a92028b40312d46b1 -->
> [!qard]- Why must advice not blindly assume every matched argument has the expected runtime shape?
> Broad pointcuts may select signatures/values outside that assumption; validate the intended contract or narrow the selector to avoid incorrect casts/checks.

<!-- qard-id: ap-4d0162e2ac6ff87f40a7 -->
> [!qard]- How do AND and OR combinations affect a pointcut's selected set?
> AND requires both conditions and narrows the set; OR includes either and broadens it. Review the resulting set against the actual required operations.

### Advice Semantics

<!-- qard-id: ap-6650779923a590ede51d -->
> [!qard]- When is before advice suitable?
> A prerequisite, logging or validation must happen before the selected operation; a rejected prerequisite should stop work through the intended error mechanism.

<!-- qard-id: ap-24fb31af15eec32e1a00 -->
> [!qard]- When is after-returning advice preferable to finally-style after advice?
> It needs a successfully produced result or should run only after normal completion, rather than also when the operation throws.

<!-- qard-id: ap-a67143ce62f17d3dc139 -->
> [!qard]- When is after-throwing advice suitable?
> It handles or records exceptional completion for selected operations, without confusing normal results with failures.

<!-- qard-id: ap-4fbd9a64d2afdabb8126 -->
> [!qard]- What extra control does around advice have over the underlying operation?
> It can decide whether to proceed, how to pass control/results through, and what work surrounds the invocation; omitting proceed can prevent the original method from running.

### Weaving, Testing And Architecture

<!-- qard-id: ap-ce58ccf9023f16829c25 -->
> [!qard]- Why can compile-time weaving preserve the source method text yet change its executed behaviour?
> Instrumentation inserts selected advice into the compiled execution path; reading only the un-woven source omits that added behaviour.

<!-- qard-id: ap-5c9e6641908c7b9b4b67 -->
> [!qard]- Why should tests verify that advice was applied, not merely test the advice function alone?
> Matching, weaving and execution ordering can fail even when the isolated check works correctly.

<!-- qard-id: ap-bdcd660767be9df593a8 -->
> [!qard]- How can two individually sensible aspects interact badly?
> Both may alter the same execution, depend on different order/exception assumptions or duplicate effects; inspect and test combined advice semantics.

<!-- qard-id: ap-c76572d1ffee326f64c7 -->
> [!qard]- Why does AOP tooling matter for debugging?
> Developers need visibility into selected join points, advice order and the effective execution path, which may span files absent from the immediate method body.

<!-- qard-id: ap-4499c3595ecafdbdf06a -->
> [!qard]- How can a broadly matched aspect harm maintainability when names are refactored?
> A textual/signature selector can silently stop matching or match new operations, so refactoring needs selector/application checks in addition to typechecking.

<!-- qard-id: ap-5fa4ae47c70a215aa4e3 -->
> [!qard]- Why does AOP complement rather than remove the need for sound security architecture?
> It can centralise an intervention, but correctness still depends on complete boundaries, appropriate policy, data flow and verified application at every required point.
