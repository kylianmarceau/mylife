---
tags:
  - advanced-programming
---

# Software Testing

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD08 Software Testing.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD08%20Software%20Testing.pdf), Johan Bontes (with credit to Sarina Till), University of Cape Town, PDF pages 1–45  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: defensive programming, automated testing (static analysis, sanitisers, fuzzing), unit tests and TDD, mocking, integration, regression, user acceptance, and security testing.

> [!note] <span style="color:#b89aff">Not examinable</span>
> The OWASP Top 10 slide has a purple title and is marked not examinable. It is included as a table for reference.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Types Of Testing And No Silver Bullet|Types Of Testing And No Silver Bullet]]
  - [[#Defensive Programming Overview|Defensive Programming Overview]]
  - [[#Const Correctness|Const Correctness]]
  - [[#Input Validation|Input Validation]]
  - [[#Assertions And Design By Contract|Assertions And Design By Contract]]
  - [[#Error Handling And Exceptions|Error Handling And Exceptions]]
  - [[#Resource Management And Compiler Warnings|Resource Management And Compiler Warnings]]
  - [[#Automated Testing: Static Analysis|Automated Testing: Static Analysis]]
  - [[#Code Sanitisers And Fuzzing|Code Sanitisers And Fuzzing]]
  - [[#Unit Tests And Coverage|Unit Tests And Coverage]]
  - [[#Test-Driven Development|Test-Driven Development]]
  - [[#Mocking Dependencies|Mocking Dependencies]]
  - [[#Selecting Test Cases|Selecting Test Cases]]
  - [[#Integration Testing|Integration Testing]]
  - [[#Regression Testing|Regression Testing]]
  - [[#User Acceptance Testing|User Acceptance Testing]]
  - [[#Security Testing|Security Testing]]

---

## Core Content

### Types Of Testing And No Silver Bullet

![Types of software testing](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/08_Software_Testing/testing-types.svg)

*Functional testing checks what the system does. Non-functional testing checks how well it does it; performance testing splits into load, stress, scalability and volume testing.*

No single technique finds most defects. Defect-detection rates (*Code Complete*, Table 20-2, after Jones and Shull et al.):

| Removal step | Lowest | Modal | Highest |
|---|---:|---:|---:|
| Informal design reviews | 25% | 35% | 40% |
| Formal design inspections | 45% | 55% | 65% |
| Informal code reviews | 20% | 25% | 35% |
| **Formal code inspections** | 45% | 60% | **70%** |
| **Modelling or prototyping** | 35% | 65% | **80%** |
| Personal desk-checking of code | 20% | 40% | 60% |
| Unit test | 15% | 30% | 50% |
| New function (component) test | 20% | 30% | 35% |
| Integration test | 25% | 35% | 40% |
| Regression test | 15% | 25% | 30% |
| System test | 25% | 40% | 55% |
| Low-volume beta test (<10 sites) | 25% | 35% | 40% |
| **High-volume beta test (>1000 sites)** | 60% | 75% | **85%** |

Combine several techniques; each catches a different share of defects.

### Defensive Programming Overview

#### Definitions

> **Defensive programming**: Writing code that protects itself against misuse and invalid state, using const correctness, input validation, assertions, error handling and resource management.

| Technique | Example |
|---|---|
| **Const correctness** | `void setName(const string& newName); string getName() const;` |
| **Input validation** | `if (uid >= size(Users)) …`, `if (newName == "") …`, `if (size(newName) < 2) …` |
| **Assertions** | `assert(Users); assert(isValid(Users));` (sanity checks in debug builds) |
| **Error handling** | `try { internalSetName(uid, newName); } catch …` |
| **Resource management** | Java `try … finally { file.close(); }`; C++ RAII: `auto file = ifstream(name);` is closed automatically when destroyed |

`assert(newName != nullptr)` is wrong. This check must run at run time in release builds, so it belongs in input validation, not an assertion.

### Const Correctness

#### Definitions

> **Const correctness**: Marking what may not change, so the compiler enforces it.

In C++, Rust and similar languages:

- `const` methods cannot change their object.
- `const` objects cannot be changed.
- `const` parameters are fixed inside the function body.

Java has no built-in equivalent, but JSR 305 and 308 annotations (`@Readonly`, `@Immutable`, `@Mutable`) work with a checker.

```cpp
string Person::getName() const { return name; }

const auto person = new Person();
person.getName();        // succeeds
person.setName("test");  // does not compile

void doStuff(const int uid) {
  uid++;                 // does not compile
  auto nextId = uid + 1; // fine
}
```

```java
@ReadOnly Person person = new Person();
person.getName();        // succeeds
person.setName("test");  // does not compile
public String getName(@ReadOnly Person this) { return name; }
```

### Input Validation

Input validation **must run in release code**. That is what makes it different from assertions.

| Check | Example |
|---|---|
| Input within bounds | `if (id < size(P)) …` |
| Object valid | `if (P && P.isOpen()) …` |
| Container big enough | `if (size(A) >= size(input)) …` |
| No SQL injection | `sqlSafe = sanitize(sql);`, or better, **parameterised queries** |
| No HTML injection | `displayTxt = sanitize(userTxt);` |

- Never display raw user input; always sanitise display text.
- Escaping is hard. Never roll your own; use standard solutions.

### Assertions And Design By Contract

#### Definitions

> **Assertion**: A check for a condition that should **never** occur in production code. It runs only in debug builds and may be as slow as needed.

> **Design by contract** (Meyer, 1997; contracts in C++26): Stating pre-conditions and post-conditions for each routine and checking them with assertions.

```pseudo
func Velocity(lat, lon, height: float): float;
  assert(-90 <= lat and lat <= 90);          // pre-conditions
  assert(0 <= lon and lon < 360);
  assert(-500 <= height and height <= 75000);
  ...
  assert(0 < result and result <= 600);      // post-condition
  return result;
```

- **Don't put action code in assertions**: `assert(DoAction());` disappears in release builds, taking the action with it.
- Assertions can break the debug state when they fire. If so, wrap the same condition in an `if` under `#ifdef _DEBUG` and set a **breakpoint**, which preserves program state:

```cpp
#ifdef _DEBUG
if (not(-90 <= lat and lat <= 90)) {   // exactly the same condition
  assert(-90 <= lat and lat <= 90);    // breakpoint here
}
#endif
```

### Error Handling And Exceptions

There are "2½ schools of thought":

| Approach | Happy path | Error path | Notes |
|---|---|---|---|
| **Exceptions** | Zero overhead | Lots of overhead | |
| **Error codes** | Little overhead | Little overhead | Much harder to get right |
| **Handle errors on the spot** | — | — | Needs a crystal ball |

```java
try { a = file.getData(); ... }
catch (SomeException e) {
  // never silently drop errors: do something useful
  editBox.textColor = clRed;
} finally {
  file.close();
}
```

- **Never silently drop errors**.
- **Don't leak exceptions to the user.** Alan Cooper (*About Face*): error messages are idiotic and should never be used.
- Instead, **prevent users from making errors**. A slider cannot be in error; a text box can.

### Resource Management And Compiler Warnings

- **Resource management**: release resources deterministically, with `finally` in Java or **RAII** in C++, where the destructor runs at scope exit.
- **Compiler warnings are your friend.** Compile with full warnings:

| Language | Setting |
|---|---|
| C++ MSVC | `/W4` |
| C++ Clang | `-Wall -Wextra -Wpedantic -Weverything` |
| C++ GCC | `-Wall -Wextra` |
| Python | `import warnings; warnings.simplefilter('always')` |
| Java | IDE-specific, e.g. NetBeans: Show warnings = true; Warnings = All |

### Automated Testing: Static Analysis

#### Definitions

> **Static analysis**: Examining code without running it. **Lint** (Johnson, 1978) is the classic tool and is especially useful for Python.

> **Code smell**: A sign of bad programming practice, i.e. a known antipattern (Fowler, *Refactoring*): duplicated or complex code, poor naming, global variables.

Static analysis checks for:

- **smells** (bad practice)
- **bugs**: code matching known bug patterns, such as infinite loops or division by zero

Formal proofs of correctness are NP-hard, so they are rarely feasible.

### Code Sanitisers And Fuzzing

#### Definitions

> **Code sanitiser**: A tool that instruments source or compiled code to detect errors at run time. Google's AddressSanitizer appeared in 2012.

> **Fuzzing**: Feeding randomised input into a program to see whether it misbehaves, testing error handling and security (Miller et al., 1990).

| Sanitiser | Detects |
|---|---|
| AddressSanitizer | Dangling pointers, reads past the end, use after free |
| MemorySanitizer | Uninitialised memory |
| UBSan | Undefined behaviour |
| LeakSan | Memory allocated but never freed |
| ThreadSan | Deadlocks, data races |

Fuzzing can be **black-box** or **white-box**. Tools exist for most languages: Python `atheris`, Java `jazzer`, C++ `libFuzzer`.

### Unit Tests And Coverage

#### Definitions

> **Unit test**: A test of a small section of code (often a class or function) in isolation.

> **Test coverage**: How much is exercised by tests: all code (measurable automatically) or all possible inputs (hard).

- Frameworks: Java JUnit; Python `unittest`; C++ Catch2.
- Tests go in a separate module, usually one test file per source file.
- The goal is 100% coverage; Python's `coverage` tool measures it.

```cpp
#include <catch2/catch_test_macros.hpp>
unsigned factorial(const unsigned n) {
  assert(n < 13);                  // why this assert?
  if (n <= 1) { return n; }
  else return factorial(n) * n;    // code smell
}

TEST_CASE("Factorials are computed", "[factorial]") {
  REQUIRE(factorial( 1) == 1);
  REQUIRE(factorial( 2) == 2);
  REQUIRE(factorial( 3) == 6);
  REQUIRE(factorial(10) == 3'628'800);
  REQUIRE(factorial(13) == 6'227'020'800);  // fail
}
```

- The `assert(n < 13)` is there because $13! = 6\,227\,020\,800$ overflows a 32-bit unsigned (max about $4.29\times10^9$).
- The recursion `factorial(n) * n` should be `factorial(n - 1) * n`; as written it never terminates.
- `n <= 1` returning `n` makes `factorial(0) = 0`, but $0! = 1$.

A failing Catch2 run reports the expression and its expansion, e.g. `REQUIRE( binary_search(arr, 176) == 0 )` with expansion `-1 == 0`, then a summary: `test cases: 1 | 1 failed`, `assertions: 5 | 4 passed | 1 failed`.

### Test-Driven Development

#### Definitions

> **Test-driven development (TDD)**: Writing a failing test before the code that makes it pass.

![TDD cycle](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/08_Software_Testing/tdd-cycle.svg)

*Stub, write a failing test, implement until it passes, and repeat for each new behaviour. Finally make the tests comprehensive.*

1. Write code with no implementation: `unsigned factorial(const unsigned n) { return n; }`
2. Write tests, which will fail.
3. Implement until (more) tests pass:

```cpp
unsigned factorial(const unsigned n) {
  auto f = n;                      // should start at 1, or f ends up n * n!
  for (auto i = 1; i <= n; i++) f *= i;
  return f;
}
```

4. Before adding code, add tests (which fail): `REQUIRE(factorial(13) == 6'227'020'800); REQUIRE(factorial(21) == {});`
5. Add code so the tests pass: `optional<uint64_t> factorial(const uint64_t n) { if (n > 20) return {}; assert(n <= 20); … }`. $20!$ is the largest factorial that fits in 64 bits.
6. Ask "do we have full coverage?" and make the tests comprehensive, e.g. loop over `i = 21, 42, 84, …` checking `factorial(i) == {}`.

### Mocking Dependencies

#### Definitions

> **Mock object**: A stand-in for a component that is not yet implemented or is hard to use in tests (a dummy database or API). It records how it was called.

Tools: Java Mockito; Python `unittest.mock`.

```python
from unittest.mock import Mock
json = Mock()
json.loads('{"key": "value"}')          # "magically" works
json.loads.assert_called()
json.loads.assert_called_once()
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once_with('{"key": "value"}')
```

Mocking makes time-dependent code testable:

```python
from unittest.mock import Mock
datetime = Mock()

def is_weekday(d):
    today = d.today()
    return (0 <= today.weekday() < 5)   # Monday = 0 … Sunday = 6

datetime.today.return_value = wednesday
assert is_weekday(datetime)
datetime.today.return_value = sunday
assert not is_weekday(datetime)
```

### Selecting Test Cases

#### Definitions

> **Partition testing**: Group possible inputs and outputs into categories (partitions) and test each, looking especially for **edge cases** at partition boundaries.

> **Guideline testing**: Choose test cases based on known failure points.

### Integration Testing

#### Definitions

> **Integration testing**: Testing the interactions between modules and classes. It is the same idea as unit testing at a higher level; unit tests test a class or function in isolation.

A unit test can pass for each part while the assembled whole fails, like a door latch that works but is mounted where it cannot reach the frame.

![Integration approaches](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/08_Software_Testing/integration-approaches.svg)

*Big-bang tests everything at once. Incremental approaches test in phases: top-down, bottom-up, or sandwich (both together).*

### Regression Testing

#### Definitions

> **Regression testing**: After adding code, rerun all the old tests, fix any breakage, and add new tests as needed.

Three steps from the source: **retest all**, **regression test selection**, and **prioritisation of test cases**.

![Regression testing types](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/08_Software_Testing/regression-types.svg)

*Seven types: corrective, retest-all, selective, progressive, complete, partial and unit regression testing.*

### User Acceptance Testing

#### Definitions

> **User acceptance testing (UAT)**: The testing phase that ensures software is ready for production. It checks that the software is what the user wanted, is usable, matches user stories (functional), and can be used and maintained (operational).

> **Alpha testing**: Testing late prototypes in the software house or with "super users".

> **Beta testing**: Testing with end users of the system.

| Usability testing | User acceptance testing |
|---|---|
| Measures ease of access | Validates the requirements document from a real user's perspective |
| Done towards the middle and end of the SDLC | Done at the end of the SDLC |
| Focuses on behaviour, experience and goals | Focuses on functionality |
| Can be expensive | Not that expensive |
| Satisfaction, memorability, desirability, credibility | Compatibility, roadmap validation, test-support processes |

Both cover errors, efficiency and learnability.

### Security Testing

Kinds of security testing include vulnerability scanning, security scanning, penetration testing, risk assessment, security auditing, ethical hacking and posture assessment.

**Security must be built in from the start**:

- parameterised queries, not cut-and-paste SQL
- never display unescaped HTML
- salted password hashes, with a different salt per user ID
- strong cryptographic functions (post-quantum Kyber rather than RSA)
- do not keep passwords in memory

#### Definitions

> **Shift left**: Moving testing, security and quality earlier in the process: into design before code, and into code before test.

> **Penetration testing**: Simulating attempts to breach security to discover vulnerabilities. MobSF is an open-source pen-testing tool, shown in the source auditing an Android APK.

- Unit tests should also test for security and quality issues.
- Run sanitisers regularly (AddressSan, UBSan, MemSan); it is cheap and easy.
- Security in particular is nearly impossible to fix in late stages.
- **Continuous integration** on GitHub can run **CodeQL** to analyse code for security flaws.

OWASP Top 10 (2021), not examinable:

| Problem | Fix |
|---|---|
| A01 Broken access control | Deny by default |
| A02 Cryptographic failures | Encrypt data in transit and at rest |
| A03 Injection | Safe APIs; input whitelisting |
| A04 Insecure design (new) | "Shift left" |
| A05 Security misconfiguration | Secure installation process |
| A06 Vulnerable and outdated components | Patch management; signed components |
| A07 Identification and authentication failures | Multi-factor authentication; no backdoors |
| A08 Software and data integrity failures (new) | Signed software |
| A09 Security logging and monitoring failures | Log everything and keep the logs |
| A10 Server-side request forgery (new) | Sanitise and whitelist |

> [!warning] <span style="color:#ffc778">Traps and pitfalls</span>
> "It is not enough to be busy; the question is what are we busy about?" (Thoreau). Many tests that never exercise the real failure are like mousetraps without cheese. "Absence of proof is not proof of absence" (Cowper): passing tests do not prove there are no bugs.
