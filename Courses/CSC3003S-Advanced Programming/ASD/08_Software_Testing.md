---
tags:
  - advanced-programming
---

# Software Testing

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD08 Software Testing.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD08%20Software%20Testing.pdf), Johan Bontes (with credit to Sarina Till), University of Cape Town, pages 1–45
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Defensive programming (const correctness, validation, assertions, error handling, resource management), automated testing (static analysis, sanitizers, fuzzing), unit tests, TDD and mocking, integration, regression and user acceptance testing, and security testing.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Types Of Software Testing|Types Of Software Testing]]
  - [[#Defensive Programming Overview|Defensive Programming Overview]]
  - [[#Const Correctness|Const Correctness]]
  - [[#Input Validation|Input Validation]]
  - [[#Assertions And Design By Contract|Assertions And Design By Contract]]
  - [[#Error Handling And Exceptions|Error Handling And Exceptions]]
  - [[#Resource Management And Compiler Warnings|Resource Management And Compiler Warnings]]
  - [[#Static Analysis|Static Analysis]]
  - [[#Code Sanitizers|Code Sanitizers]]
  - [[#Fuzzing|Fuzzing]]
  - [[#Unit Tests|Unit Tests]]
  - [[#Test-Driven Development|Test-Driven Development]]
  - [[#Mock Objects|Mock Objects]]
  - [[#Selecting Test Cases|Selecting Test Cases]]
  - [[#Integration Testing|Integration Testing]]
  - [[#Regression Testing|Regression Testing]]
  - [[#User Acceptance Testing|User Acceptance Testing]]
  - [[#Security Testing|Security Testing]]
  - [[#Traps And Pitfalls|Traps And Pitfalls]]

---

## Core Content

### Types Of Software Testing

There is no silver bullet: no single kind of testing catches everything.

![Types of software testing](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/08_Software_Testing/testing-types.svg)

*Functional testing checks what the system does; non-functional testing checks how well it does it.*

| Functional testing | Non-functional testing |
|---|---|
| Unit testing | Documentation testing |
| Integration testing | Installation testing |
| Interface testing | Performance testing — load, stress, scalability, volume |
| System testing | Reliability testing |
| Regression testing | Security testing |
| User acceptance testing | |

### Defensive Programming Overview

#### Definitions

> **Defensive programming**: Writing code that protects itself against misuse and bad input, so errors are caught early and close to their cause.

| Technique | Example |
|---|---|
| Const correctness | `void setName(const string& newName); string getName() const;` |
| Input validation | `if (uid >= size(Users)) {...}`, `if (newName == "") {...}` |
| Assertions | `assert(Users); assert(isValid(Users));` |
| Error handling | `try { internalSetName(uid, newName); } catch ...` |
| Resource management | `finally { file.close(); }` or RAII |

### Const Correctness

#### Definitions

> **Const correctness**: Marking what must not change (methods, objects, parameters) as constant so the compiler enforces it.

| Language | Mechanism |
|---|---|
| C++, Rust, etc. | `const` methods can't change their object; `const` objects can't be changed; `const` parameters are fixed in the body |
| Java | Annotations from JSR 305/308 with the Checker Framework: `@ReadOnly`, `@Immutable`, `@Mutable` |

```cpp
string Person::getName() const { return name; }

const auto person = new Person();
person.getName();        // succeeds
person.setName("test");  // does not compile

void doStuff(const int uid) {
    uid++;                  // does not compile
    auto nextId = uid + 1;  // fine
}
```

```java
public String getName(@ReadOnly Person this) { return name; }

@ReadOnly Person person = new Person();
person.getName();        // succeeds
person.setName("test");  // does not compile
```

### Input Validation

Input validation **must run in release code** — unlike assertions.

| Check | Example |
|---|---|
| Input within bounds | `if (id < size(P)) {...}` |
| Object valid | `if (P && P.isOpen()) {...}` |
| Container big enough | `if (size(A) >= size(input)) {...}` |
| No SQL injection | `sqlSafe = sanitize(sql);` — better, use **parameterised queries** |
| No HTML injection | `displayTxt = sanitize(userTxt);` |

- Never display raw user input; always sanitise display text.
- Escaping is hard: never roll your own; use standard solutions.

### Assertions And Design By Contract

#### Definitions

> **Assertion**: A check for a condition that should **never** occur in production code. It runs only in debug builds and can be as slow as you like.

> **Design by contract**: Specifying each routine's pre-conditions and post-conditions as checked assertions (Meyer, 1997; contracts are coming to C++26).

- Assertions are removed in release builds, so **never put action code in an assertion**: `assert(DoAction());` would stop calling `DoAction` in release.
- Use them for pre-conditions and post-conditions:

```text
func Velocity(lat, lon, height: float): float;
    assert(-90 <= lat and lat <= 90);          // pre
    assert(0 <= lon and lon < 360);
    assert(-500 <= height and height <= 75000);
    ...
    assert(0 < result and result <= 600);      // post
    return result;
```

A failing assertion can abort and lose the debug state. If so, wrap it in the same condition so a breakpoint preserves program state:

```text
#ifdef _DEBUG
if (not(-90 <= lat and lat <= 90)) {   // exactly the same condition
    assert(-90 <= lat and lat <= 90);   // breakpoint here keeps state
}
```

| | Input validation | Assertions |
|---|---|---|
| Runs in release? | Yes | No (debug only) |
| Guards against | Bad external input | Programmer errors — "impossible" states |
| Cost | Must be cheap | Can be slow |

### Error Handling And Exceptions

There are "2½ schools of thought":

| Approach | Happy path | Error path | Notes |
|---|---|---|---|
| Exceptions | Zero overhead | Lots of overhead | — |
| Error codes | Little overhead | Little overhead | Much harder to get right |
| Handle errors on the spot | — | — | Needs a crystal ball |

```java
try {
    a = file.getData();
    ...
} catch (SomeException e) {
    // never silently drop errors ("ignore it")
    // do something useful:
    editBox.textColor = clRed;
} finally {
    file.close();
}
```

- Never silently swallow errors.
- Don't leak exceptions to the user. Alan Cooper (*About Face*): error messages are idiotic and should never be used. Instead, **prevent users from making errors** in the first place — a slider cannot be in error, but a text box can.

### Resource Management And Compiler Warnings

Resources must be released even when errors occur:

```java
String readFile(String name) {
    File file = new File(name);
    try { /* do stuff with file */ }
    finally { file.close(); }
}
```

```cpp
void rF(const string& name) {
    auto file = ifstream(name);
    // do stuff with file
}   // RAII: ifstream destroyed, file closed automatically
```

#### Definitions

> **RAII (Resource Acquisition Is Initialisation)**: Tying a resource's lifetime to an object's scope, so the destructor releases it automatically.

**Bonus check: compiler warnings are your friend.** Enable all warnings:

| Language | Setting |
|---|---|
| C++ (MSVC) | `/W4` |
| C++ (Clang) | `-Wall -Wextra -Wpedantic -Weverything` |
| C++ (GCC) | `-Wall -Wextra` |
| Python | `import warnings; warnings.simplefilter('always')` |
| Java | IDE-specific, e.g. NetBeans: Project properties → Build → Compiling → Show warnings; Tools → Options → Java → Compiler → Warnings = All |

### Static Analysis

#### Definitions

> **Static analysis**: Automatically examining source code without running it.

> **Code smell**: A sign of bad programming practice (a known antipattern), e.g. duplicated or complex code, poor naming, global variables (Fowler, *Refactoring*, 1999).

**Lint** (S. Johnson, 1978) is the classic tool, and is especially useful for Python. Static analysers check for:

- **smells** — known antipatterns;
- **bugs** — code matching known bug patterns, such as infinite loops or division by zero.

Formal proofs of correctness are NP-hard, so they are rarely feasible.

### Code Sanitizers

#### Definitions

> **Sanitizer**: A run-time checker that instruments source code (or injects into compiled code) to detect classes of bugs as the program runs. Introduced by Google in 2012 with AddressSanitizer.

| Sanitizer | Detects |
|---|---|
| AddressSanitizer | Dangling pointers, reading past the end, use after free |
| MemorySanitizer | Uninitialised memory |
| UBSan | Undefined behaviour |
| LeakSanitizer | Memory allocated but never freed |
| ThreadSanitizer | Deadlocks, data races |

### Fuzzing

#### Definitions

> **Fuzzing**: Feeding randomised input into a program to check its error handling, see whether it misbehaves, and find security problems (Miller et al., 1990).

- Can be **black-box** (no knowledge of internals) or **white-box** (uses code structure).
- Tools exist for most languages: Python — `atheris`; Java — Jazzer; C++ — libFuzzer.

### Unit Tests

#### Definitions

> **Unit test**: A test of a small section of code — often a class or function — in isolation.

> **Test coverage**: How much is exercised by tests: all code (measurable automatically) or all possible inputs (hard).

- Frameworks: Java — JUnit; Python — `unittest`; C++ — Catch2.
- Tests live in a separate module, typically one test file per file under test.
- The goal is **100% test coverage**. Python's `coverage` tool measures it.

```cpp
#include <catch2/catch_test_macros.hpp>

unsigned factorial(const unsigned n) {
    assert(n < 13);                // 13! overflows a 32-bit unsigned
    if (n <= 1) { return n; }      // bug: 0! should be 1
    else return factorial(n) * n;  // code smell — should be factorial(n-1)
}

TEST_CASE("Factorials are computed", "[factorial]") {
    REQUIRE(factorial(1)  == 1);
    REQUIRE(factorial(2)  == 2);
    REQUIRE(factorial(3)  == 6);
    REQUIRE(factorial(10) == 3'628'800);
    REQUIRE(factorial(13) == 6'227'020'800);  // fails
}
```

A failed test reports the expression and its expansion:

```text
test.cpp:18: FAILED:
  REQUIRE( binary_search(arr, 176) == 0 )
with expansion:
  -1 == 0
test cases: 1 | 1 failed
assertions: 5 | 4 passed | 1 failed
```

### Test-Driven Development

#### Definitions

> **Test-driven development (TDD)**: Writing tests **before** the code they test, then writing just enough code to make them pass.

![TDD cycle](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/08_Software_Testing/tdd-cycle.svg)

*Stub the code, write a failing test, implement until it passes, then add tests before each new piece of code.*

1. Write the code's interface with no implementation:
```cpp
unsigned factorial(const unsigned n) { return n; }
```
2. Write a test for it — it fails:
```cpp
TEST_CASE("Do factorials", "[factorial]") {
    REQUIRE(factorial(1)  == 1);
    REQUIRE(factorial(2)  == 2);
    REQUIRE(factorial(3)  == 6);
    REQUIRE(factorial(10) == 3'628'800);
}
```
3. Implement the code so (more) tests pass:
```cpp
unsigned factorial(const unsigned n) {
    auto f = n;                              // as written this gives n * n!;
    for (auto i = 1; i <= n; i++) f *= i;    // starting from f = 1 is correct
    return f;
}
```
4. Before adding code, add tests — they fail:
```cpp
REQUIRE(factorial(13) == 6'227'020'800);
REQUIRE(factorial(21) == {});               // 21! overflows 64 bits
```
5. Add code so the tests pass:
```cpp
optional<uint64_t> factorial(const uint64_t n) {
    if (n > 20) { return {}; }   // empty result
    assert(n <= 20);             // defensive programming
    ...
}
```
6. Ask "do we have full coverage?" and make the tests comprehensive:
```cpp
for (unsigned i = 21; i < UINT32_MAX; i *= 2) {
    REQUIRE(factorial(i) == {});
}
```

### Mock Objects

#### Definitions

> **Mock object**: A stand-in for a component that isn't implemented yet (or is expensive), such as a dummy database or API, that records how it is called and returns programmed values.

Tools: Java — Mockito; Python — `unittest.mock`.

```python
from unittest.mock import Mock

json = Mock()
json.loads('{"key": "value"}')     # will magically work
json.loads.assert_called()
json.loads.assert_called_once()
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once_with('{"key": "value"}')
```

Mocks make non-deterministic code testable:

```python
from datetime import datetime
from unittest.mock import Mock

datetime = Mock()

def is_weekday(d):
    today = d.today()
    # Python's datetime treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

datetime.today.return_value = wednesday   # mock today() to return Wednesday
assert is_weekday(datetime)
datetime.today.return_value = sunday
assert not is_weekday(datetime)
```

### Selecting Test Cases

| Strategy | Approach |
|---|---|
| **Partition testing** | Group possible inputs and outputs into categories (partitions) and look for edge cases at their boundaries |
| **Guideline testing** | Choose test cases from known failure points (experience of where programs commonly fail) |

### Integration Testing

#### Definitions

> **Integration testing**: Testing the interactions between modules and classes — like unit testing, but at a higher level. Unit testing checks a class or function in isolation.

![Integration approaches](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/08_Software_Testing/integration-approaches.svg)

*Big-bang integrates everything at once; incremental approaches integrate in phases from the top, the bottom, or both.*

| Approach | How |
|---|---|
| **Big-bang** | Everything at once |
| **Incremental** | Tested in phases: |
| — Top-down | Higher-level modules first (lower ones stubbed) |
| — Bottom-up | Lower-level modules first (higher ones driven by test harnesses) |
| — Sandwich | Higher and lower levels together |

### Regression Testing

#### Definitions

> **Regression testing**: Re-running old tests after changes to make sure existing behaviour hasn't broken.

When you add new code:

1. Rerun all your old tests.
2. Fix any breakage.
3. Add new tests as needed.

![Types of regression testing](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/08_Software_Testing/regression-types.svg)

*Regression testing ranges from rerunning everything to selecting only the tests the change can affect.*

| Type | Scope |
|---|---|
| Corrective | Reuse existing tests when the specification hasn't changed |
| Retest-all | Rerun every test |
| Selective | Rerun only tests affected by the change |
| Progressive | New tests for changed specifications |
| Complete | Full retest after major changes |
| Partial | Test the changed part and its interactions |
| Unit | Rerun the unit tests of the changed unit only |

### User Acceptance Testing

#### Definitions

> **User acceptance testing (UAT)**: The testing phase that ensures software is ready for production — that it is what the user wanted, and is usable and user-friendly.

| Aspect | Check |
|---|---|
| Functional | Matches the user stories (Agile/XP) |
| Operational | The system can be used and maintained |

Alpha and beta tests are late, usable prototypes:

| | Alpha testing | Beta testing |
|---|---|---|
| Where / who | In the software house, or with "super users" | With end users of the system |

**Usability testing versus UAT**:

| | Usability testing | User acceptance testing |
|---|---|---|
| Purpose | Measure ease of access | Validate the requirements document from a real user's perspective |
| When | Middle to end of the SDLC | End of the SDLC |
| Focus | Behaviour, experience and goals | Functionality |
| Cost | Can be expensive | Not that expensive |
| Measures | Satisfaction, memorability, desirability, credibility | Compatibility, roadmap validation, test support processes |
| Shared | Errors, efficiency, learnability | (same) |

### Security Testing

Security must be built in from the start, for example:

- parameterised queries, not cut-and-paste SQL;
- never displaying unescaped HTML;
- salted password hashes, with a different salt per user ID;
- strong cryptographic functions (e.g. post-quantum Kyber rather than RSA);
- not keeping passwords in memory.

**OWASP Top 10 (2021):**

| Rank | Vulnerability (change) | Fix |
|---|---|---|
| A01 | Broken access control (↑5) | Deny by default |
| A02 | Cryptographic failures (=2) | Encrypt data in transit and at rest |
| A03 | Injection (↓1) | Safe APIs; whitelist input validation |
| A04 | Insecure design (new) | "Shift left" |
| A05 | Security misconfiguration (↑6) | Secure installation process |
| A06 | Vulnerable and outdated components (↑9) | Patch management; signed components |
| A07 | Identification and authentication failures (↓2) | Multi-factor authentication; no back doors |
| A08 | Software and data integrity failures (new) | Signed software |
| A09 | Security logging and monitoring failures (↑10) | Log everything and keep the logs |
| A10 | Server-side request forgery (new) | Sanitise and whitelist |

#### Definitions

> **Shift left**: Moving testing, security and quality earlier in the process — into design before code, and into code before test.

- Unit tests should also test for security and quality issues.
- Run sanitizers regularly (AddressSan, UBSan, MemSan, …) — cheap and easy.
- Security in particular is nearly impossible to fix in late stages.

> **Penetration testing (pen testing)**: Simulating attempts to breach security to discover vulnerabilities. MobSF is an open-source tool supporting it.

Security audits report vulnerabilities systematically. In continuous integration, GitHub integrates easily with **CodeQL** to analyse code for security flaws.

### Traps And Pitfalls

> "It is not enough to be busy; the question is, what are we busy about?" — Henry David Thoreau

More traps don't help if they target the wrong thing (a mouse that doesn't like cheese): test what actually matters.

> "Absence of proof is not proof of absence." — William Cowper

Passing tests don't prove there are no bugs — only that the tests didn't find any.
