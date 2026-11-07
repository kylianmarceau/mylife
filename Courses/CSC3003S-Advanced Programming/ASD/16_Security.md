---
tags:
  - advanced-programming
---

# Security

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD16 Security.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD16%20Security.pdf), Johan Bontes, University of Cape Town, pages 1–29
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Security as a built-in quality, the three main security problem areas — memory safety, code injection (SQL, XSS, command) and authentication (password storage, sessions, access control) — and their standard fixes.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Security As A Quality And A Risk|Security As A Quality And A Risk]]
  - [[#Security Must Be Built In|Security Must Be Built In]]
  - [[#The Three Main Security Problems|The Three Main Security Problems]]
  - [[#Never Roll Your Own|Never Roll Your Own]]
  - [[#Memory Safety|Memory Safety]]
  - [[#Stack And Heap Attacks|Stack And Heap Attacks]]
  - [[#Code Injection|Code Injection]]
  - [[#Security Cast Of Characters|Security Cast Of Characters]]
  - [[#SQL Injection|SQL Injection]]
  - [[#Cross-Site Scripting (XSS)|Cross-Site Scripting (XSS)]]
  - [[#Whitelists Versus Blacklists|Whitelists Versus Blacklists]]
  - [[#OS And Command Injection|OS And Command Injection]]
  - [[#Storing Passwords|Storing Passwords]]
  - [[#Session Management|Session Management]]
  - [[#Improper, Missing Or Hard-Coded Authentication|Improper, Missing Or Hard-Coded Authentication]]

---

## Core Content

### Security As A Quality And A Risk

Security is one of the ISO 25010 quality characteristics (confidentiality, integrity, non-repudiation, accountability, authenticity, resistance) — see [Dependable Systems](10_Dependable_Systems.md).

$$
\text{Risk} = \text{cost} \times \text{likelihood}
$$

| | Cheap | Expensive |
|---|---|---|
| **Unlikely** | Accept | Transfer (insure) |
| **Likely** | Reduce | Avoid |

Security breaches are likely and expensive, so they must be avoided.

### Security Must Be Built In

Security must be built in **from the start**:

- It is complex and subtle.
- You cannot roll your own; you must use standard solutions.
- In a hodge-podge system, the **weakest link** determines the security.
- Have a security architecture and follow the standard.
- It is a **moving target**: solutions secure in 2023 are not in 2025 (e.g. RSA public-key encryption is no longer considered secure).
- Secure software design patterns exist but are out of scope for ASD.

### The Three Main Security Problems

| Area | Threats |
|---|---|
| **Memory safety** | Reading or writing forbidden data; rights escalation; code execution |
| **Code injection** | SQL injection; command injection (and XSS) |
| **Authentication** | Passwords; session management |

### Never Roll Your Own

- Always use a known good security pattern.
- Every security problem has its own very specific fix. SQL injection and XSS are both code injection, but their fixes are completely different, with zero overlap.
- Don't use outdated fixes. SQL injection **cannot be escaped**, no matter what your 2001 website says.
- 80% secure is **not** secure.

### Memory Safety

#### Definitions

> **Buffer overrun (out-of-bounds read/write)**: Accessing memory past either end of an intended buffer.

> **Invalid buffer operation**: e.g. using a read-only pointer to write, or overwriting neighbouring data.

![Buffer overrun](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/16_Security/buffer-overrun.svg)

*Reading or writing past a buffer, or writing through a read-only pointer, can crash, give unexpected results, leak data or execute arbitrary code.*

Mitigations:

| Mitigation | Detail |
|---|---|
| Secure languages | Rust, Java |
| Modern techniques in insecure languages | C++: use the 2023 standard — "constexpr all the things". C: stop using it; it is and always will be a 1970s language |
| Compiler hardening flags | Stack canaries, etc. |
| Code sanitizers | AddressSanitizer and friends (see [Software Testing](08_Software_Testing.md#Code%20Sanitizers)) |

### Stack And Heap Attacks

| | Stack | Heap |
|---|---|---|
| Contents | Local data **and** function return addresses | Objects (code + data) |
| Attack | A buffer overrun changes state; overwriting the **return address** allows arbitrary code execution | Object data is nearly always read-write with no protection; overwriting a **VMT pointer** allows arbitrary code execution |
| Detection | — | Many objects sit side by side in the same data segment, so out-of-bounds writes are unlikely to trigger an exception |

### Code Injection

#### Definitions

> **Code injection**: An attack in which input is interpreted as code.

- If code is text, and input is text, then **input can be code** — never trust input.
- If output is text, then **output can be code** — never trust output.

### Security Cast Of Characters

| Name | Role |
|---|---|
| Alice, Bob, Charlie | Normal users, assumed to be "noobs" |
| Eve | Eavesdropper (read-only); a man-in-the-middle if she can also write |
| Mallory | Malicious actor, often a bot |
| Trudy | Thief, trying to steal money or credentials |

### SQL Injection

Trudy types this into a product search box:

```sql
' union select username, password from users --
```

The site pastes it into its query:

```sql
select * from products where name like ''
union select username, password from users -- '
```

The `'` closes the string, `union` appends a second query returning every username and password, and `--` comments out the rest.

![SQL injection](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/16_Security/sql-injection.svg)

*Trudy's search text becomes part of the SQL, turning a product search into a password dump.*

**There is only one fix: parameterised queries.**

- You cannot sanitise or escape SQL — it's impossible.
- Never copy-paste (string-build) SQL.
- If you must build SQL dynamically (e.g. dynamic table names), use a **whitelist**.

```python
# safe
safe_query = "SELECT * FROM users WHERE username = ?"

# impossible to fix (e.g. W3Schools-style code)
unsafe_query = f"SELECT * FROM users WHERE username = '{user_input}'"
```

### Cross-Site Scripting (XSS)

#### Definitions

> **Cross-site scripting (XSS)**: An attack where stored or reflected input is output to other users' browsers, where it runs as code.

Mallory posts a message containing `<script>BOMB</script>`. The website stores it and later shows Alice "Hello Alice! Mallory posted: <script>…", and Alice's browser runs the script.

![Cross-site scripting](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/16_Security/xss.svg)

*Input stored by the site is replayed to another user as executable code.*

Mitigated by:

- **HTML sanitation**;
- **HTML whitelisting** — only allow a safe subset.

### Whitelists Versus Blacklists

| | Whitelist (allow list) | Blacklist (deny list) |
|---|---|---|
| Approach | Only allow a known safe subset | Block known bad inputs |
| Safety | Safe (though still non-trivial) | Fundamentally broken — you can't be complete in an infinite universe |

### OS And Command Injection

A script runs `LIST /home/ + userName`. Trudy enters the user name `";DELETE ALL FILES"`, so the command becomes `LIST /home/;DELETE ALL FILES`.

![Command injection](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/16_Security/command-injection.svg)

*Input pasted into a shell command adds a second command; echoed error messages help the attacker refine it.*

Echoing verbose error messages back to Trudy is very helpful to an attacker.

Mitigated by:

- using parameterised calls;
- escaping and sanitising all input;
- never copy-pasting input into commands;
- never echoing error messages to users.

### Storing Passwords

**Never store passwords in a database.** Store a salted one-way hash instead:

| Field | Content |
|---|---|
| `user_id` | e.g. 007 |
| `username` | e.g. "Bont, Johan" |
| `salt` | `strong_random_number(user_id)` — random, different per user |
| `passhash` | `crypto_one_way_hash(password + salt)` |

![Salted password hashing](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/16_Security/password-hash.svg)

*The password plus a per-user random salt goes through a slow one-way hash; only the salt and hash are stored.*

#### Definitions

> **Rainbow table**: A precomputed table of hashes of common passwords, used to reverse unsalted hashes quickly.

> **Salt**: Random data added to each password before hashing, so identical passwords hash differently and precomputed tables are useless.

- A per-user salt defeats rainbow tables.
- **Slower hashes are better**: they make brute force expensive. Strengthen further with a slower/stronger hash and a different number of rounds depending on the salt.
- Even so, individual (weak) passwords are still very likely to be cracked.

### Session Management

HTTP is **stateless**, so tracking an authenticated user is non-trivial. There are exactly three standard methods — pick one and implement it **exactly as prescribed**, using a known good library.

Python (Flask):

```python
from flask_session import Session
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False     # sessions expire when the browser closes
app.config["SESSION_TYPE"] = "filesystem"   # store session data on the filesystem
Session(app)
```

Java (Jakarta servlets):

```java
import jakarta.servlet.http.*;   // known good solution

if (user + password + 2FA == OK) {
    // erase any existing session
    HttpSession oldSession = request.getSession(false);
    if (oldSession != null) { oldSession.invalidate(); }
    // generate a clean, secure new session
    HttpSession newSession = request.getSession(true);
    newSession.setAttribute("user", "role");   // store user state on the server
    response.sendRedirect("page.html");
} else {
    response.sendRedirect("login.html?error=invalid");
}
```

Invalidating the old session on login prevents **session fixation** (an attacker planting a known session ID before the victim logs in).

### Improper, Missing Or Hard-Coded Authentication

| Problem | Mitigation |
|---|---|
| Weak, missing or hard-coded passwords, or a user ID in the URL | Force a change of the default password after installation; never put in back doors; two-factor authentication; use a standard (known secure) authentication scheme |
| All users are superusers (often combined with injection) | "Switch on brain — 1960 is no more"; always disable guest users; sandbox untrusted visitors |
