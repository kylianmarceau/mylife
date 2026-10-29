---
tags:
  - advanced-programming
---

# Security

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD16 Security.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD16%20Security.pdf), Johan Bontes, University of Cape Town, PDF pages 1–29  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: security as a quality and a risk, the three main security problems (memory safety, code injection, authentication), and the specific mitigation for each.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Security As Quality And Risk|Security As Quality And Risk]]
  - [[#Security Must Be Built In|Security Must Be Built In]]
  - [[#Three Main Security Problems|Three Main Security Problems]]
  - [[#Never Roll Your Own Fix|Never Roll Your Own Fix]]
  - [[#Memory Safety|Memory Safety]]
  - [[#Code Injection: Never Trust Input Or Output|Code Injection: Never Trust Input Or Output]]
  - [[#Security Lingo|Security Lingo]]
  - [[#SQL Injection|SQL Injection]]
  - [[#Cross-Site Scripting (XSS)|Cross-Site Scripting (XSS)]]
  - [[#Whitelists Versus Blacklists|Whitelists Versus Blacklists]]
  - [[#OS, Code And Command Injection|OS, Code And Command Injection]]
  - [[#Authentication: Storing Passwords|Authentication: Storing Passwords]]
  - [[#Session Management|Session Management]]
  - [[#Improper, Missing Or Hardcoded Authentication|Improper, Missing Or Hardcoded Authentication]]

---

## Core Content

### Security As Quality And Risk

Security is one of the ISO 25010 quality characteristics. Its sub-characteristics are confidentiality, integrity, non-repudiation, accountability, authenticity and resistance (see [Dependable Systems](10_Dependable_Systems.md)).

It is the most important characteristic because:

$$
\text{Risk} = \text{cost}\times\text{likelihood}
$$

Insecure software is both likely to be attacked and expensive when it is, which puts it in the **avoid** quadrant of the risk matrix (accept, transfer, reduce, avoid).

### Security Must Be Built In

Security must be built in from the start:

- It is complex and subtle. You cannot roll your own; use standard solutions.
- In a hodge-podge system, the **weakest link** determines security.
- You need a security architecture that follows a standard.
- It is a **moving target**: solutions secure in 2023 are not in 2025. For example, RSA public-key encryption is no longer considered secure.
- Security design patterns (e.g. Lester Nichols' *Cybersecurity Architect's Handbook*; Schumacher et al.'s *Security Patterns*) are **out of scope** for ASD.

### Three Main Security Problems

| Problem | Includes |
|---|---|
| **Memory safety** | Reading or writing forbidden data; rights escalation; arbitrary code execution |
| **Code injection** | SQL injection; command injection; XSS |
| **Authentication** | Passwords; session management |

### Never Roll Your Own Fix

- Always use a **known good** security pattern.
- Every security problem has its own very specific fix. SQL injection and XSS are both code injection, but their fixes are completely different, with zero overlap.
- **Do not use outdated fixes.** SQL injection cannot be fixed by escaping, whatever a 2001 website says.
- **80% secure is not secure.**

### Memory Safety

#### Definitions

> **Buffer overrun (out-of-bounds read/write)**: Reading or writing past either end of an intended buffer.

> **Invalid buffer operation**: Misusing memory within bounds, e.g. writing through a read-only pointer.

![Buffer overrun](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/16_Security/buffer-overrun.svg)

*Out-of-bounds or invalid writes can crash, give unexpected results, execute arbitrary code, or leak unauthorised data.*

| Where | Why it's dangerous |
|---|---|
| **Stack** | Stores local data, so an overrun changes program state. It also stores the function **return address**; overwriting it allows arbitrary code execution. |
| **Heap** | Objects (code + data) are nearly always read-write with no protection. Overwriting a **virtual method table pointer** allows arbitrary code execution. Many objects sit side by side, so an out-of-bounds write is unlikely to raise an exception. |

**Mitigations**:

- **Secure languages**: Rust, Java.
- **Insecure languages, used with modern techniques**: C++23 ("constexpr all the things"). C should be avoided: "it is and always will be a 1970s language".
- **Compiler hardening flags**, e.g. stack canaries.
- **Code sanitisers** (see [Software Testing](08_Software_Testing.md)).

### Code Injection: Never Trust Input Or Output

- If code is text and input is text, then **input can be code**. **Never trust input.**
- If output is text, then **output can be code**. **Never trust output.**

### Security Lingo

| Name | Role |
|---|---|
| Alice, Bob, Charlie | Normal users, assumed to be novices |
| **Eve** | Eavesdropper (read-only); a man-in-the-middle if read and write |
| **Mallory** | Malicious actor, often a bot |
| **Trudy** | Thief, trying to steal money or credentials |

### SQL Injection

#### Definitions

> **SQL injection**: Attacker input is pasted into a SQL string and executed as SQL.

![SQL injection](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/16_Security/sql-injection.svg)

*Trudy's search text closes the string literal and appends a `UNION` query that dumps usernames and passwords. `--` comments out the rest.*

**There is only one fix**:

- You **cannot** sanitise or escape SQL; it is impossible.
- Use **parameterised queries** and never copy-paste SQL.
- If you must build SQL dynamically (e.g. dynamic table names), use a **whitelist**.

```python
safe_query   = "SELECT * FROM users WHERE username = ?"           # parameterised
unsafe_query = f"SELECT * FROM users WHERE username = '{user_input}'"   # impossible to fix
```

### Cross-Site Scripting (XSS)

#### Definitions

> **Cross-site scripting (XSS)**: An attacker stores script in content that the site later shows to other users, whose browsers execute it. This is a failure to distrust **output**.

![XSS](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/16_Security/xss.svg)

*Mallory posts `<script>BOMB</script>`. When the site shows Alice the post, her browser runs the script.*

It is mitigated by **HTML sanitation** and **HTML whitelisting** (allowing only a safe subset).

### Whitelists Versus Blacklists

In current terminology these are **allow lists** and **deny lists**.

| Blacklist (deny list) | Whitelist (allow list) |
|---|---|
| Fundamentally broken: you can't list every bad thing in an infinite universe | Safe: only a known-safe subset is allowed |
| | Still non-trivial to get right |

### OS, Code And Command Injection

![Command injection](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/16_Security/command-injection.svg)

*A script builds `LIST /home/ + userName`. A user name of `;DELETE ALL FILES` turns it into two commands.*

Echoing verbose error messages to Trudy is very helpful to an attacker. The mitigations are:

- use parameterised calls
- escape and sanitise all input
- never copy-paste input into commands
- do not echo error messages to users

### Authentication: Storing Passwords

#### Definitions

> **Salt**: A strong random value, different per user, combined with the password before hashing.

> **One-way (cryptographic) hash**: A function that is easy to compute but infeasible to invert.

> **Rainbow table**: A precomputed table of hashes for common passwords. Per-user salts make it useless.

The database fields:

```text
user_id:  007
username: Bont, Johan Bont(es)
salt:     strong_random_number(user_id)
passhash: crypto_one_way_hash(password + salt)
```

![Salted password hashing](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/16_Security/password-hash.svg)

*Only the salt and the hash are stored. At login, the entered password is salted and hashed again and compared.*

- **Never store passwords in a database.**
- Strengthen with **slower, stronger hashes**; slower is better. Use a different number of rounds depending on the salt.
- Even so, individual weak passwords are very likely to be cracked eventually.

### Session Management

HTTP is stateless, so tracking an authenticated user is non-trivial. There are exactly three methods; pick one and implement it **exactly as prescribed**, using a known good library.

```python
from flask_session import Session
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False    # sessions expire when the browser closes
app.config["SESSION_TYPE"] = "filesystem"  # store session data on the server
Session(app)
```

```java
import jakarta.servlet.http.*;   // known good solution
if (user + password + 2FA == OK) {
  HttpSession oldSession = request.getSession(false);   // erase any existing session
  if (oldSession != null) { oldSession.invalidate(); }
  HttpSession newSession = request.getSession(true);    // clean, secure new session
  newSession.setAttribute("user", "role");              // user state kept on the server
  response.sendRedirect("page.html");
} else {
  response.sendRedirect("login.html?error=invalid");
}
```

The old session is invalidated and a fresh one created on login to prevent **session fixation**.

### Improper, Missing Or Hardcoded Authentication

| Problem | Mitigation |
|---|---|
| **Weak, missing or hardcoded password, or a user ID in the URL**: Mallory claims "I'm Alice" and gets Alice's private data | Force a change of the default password after install; never put in backdoors; two-factor authentication; a standard, known-secure authentication scheme |
| **All users are superusers**, often combined with injection: a guest can "Delete DATABASE" as easily as say "Hello World" | "Switch on brain (1960 is no more)": always disable guest users; sandbox untrusted visitors |

The authentication xkcd: "I lost the server password." "How do I know it's really you? I bet we can construct a cool proof-of-identity protocol…" "Oh good, it's you, here's the password." Social engineering often beats technical protocols.
