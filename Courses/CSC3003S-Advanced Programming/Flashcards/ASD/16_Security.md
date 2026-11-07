---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 16 — Security"
---

# ASD 16 — Security

**Source note:** [Security](../../ASD/16_Security.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Principles|Principles]]
  - [[#Memory Safety|Memory Safety]]
  - [[#Injection|Injection]]
  - [[#Authentication|Authentication]]

## Core Content

### Principles

<!-- qard-id: ap-72d48508a6c2c804fb5d -->
> [!qard]- Why must security be built in from the start?
> It's complex and subtle, the weakest link decides, and it can't be bolted on later.

<!-- qard-id: ap-10fa5c7bebd76e6a24a7 -->
> [!qard]- Why should you never roll your own security fix?
> Each problem has a specific known fix; home-made or outdated fixes leave gaps — 80% secure is not secure.

<!-- qard-id: ap-5fbf20115f39ebe5fdec -->
> [!qard]- Name the three main security problem areas.
> Memory safety, code injection, authentication.

<!-- qard-id: ap-c70113b3ba692fc6c86d -->
> [!qard]- Why is security a moving target?
> Solutions secure a few years ago (e.g. RSA) may no longer be.

### Memory Safety

<!-- qard-id: ap-c0476650384a09e5a947 -->
> [!qard]- What is a buffer overrun?
> Reading or writing past the end of a buffer.

<!-- qard-id: ap-e25ca10ef04ba27ae831 -->
> [!qard]- Why are stack overruns dangerous?
> They can overwrite the return address, allowing arbitrary code execution.

<!-- qard-id: ap-276e615cb41595cb5a9e -->
> [!qard]- Why are heap overruns dangerous?
> They can overwrite object data or VMT pointers (arbitrary code execution) and rarely trigger exceptions.

<!-- qard-id: ap-6ab75d22cf6da0cdc549 -->
> [!qard]- How is memory safety mitigated?
> Safe languages (Rust, Java), modern C++, compiler hardening flags (stack canaries), sanitizers.

### Injection

<!-- qard-id: ap-70cbf06a45a2efb580b6 -->
> [!qard]- What is the root cause of code injection?
> Text input (or output) gets interpreted as code — never trust input or output.

<!-- qard-id: ap-f479b09d16e235785893 -->
> [!qard]- How does SQL injection work?
> Input containing SQL (e.g. `' union select …`) is pasted into a query and executed.

<!-- qard-id: ap-6267be56048a807874d4 -->
> [!qard]- What is the only fix for SQL injection?
> Parameterised queries — SQL can't be safely escaped (use a whitelist if SQL must be built dynamically).

<!-- qard-id: ap-bd2e087ad6987811e346 -->
> [!qard]- What is cross-site scripting and its mitigation?
> Stored input is shown to other users and runs in their browsers. Mitigate with HTML sanitisation and whitelisting.

<!-- qard-id: ap-6036af01df3fdffd5d57 -->
> [!qard]- Why are whitelists safer than blacklists?
> Blacklists can never list every bad input; whitelists allow only a known safe subset.

<!-- qard-id: ap-7dece2ae8e7464b3b535 -->
> [!qard]- How is command injection mitigated?
> Parameterise calls, escape/sanitise input, never paste input into commands, don't echo errors to users.

### Authentication

<!-- qard-id: ap-b6dde90248cc8cf4ad43 -->
> [!qard]- How should passwords be stored?
> Never in plain form — store a random per-user salt and a slow cryptographic one-way hash of password + salt.

<!-- qard-id: ap-5ec9dc9cc3cc8fa6a6c3 -->
> [!qard]- Why salt password hashes?
> Identical passwords hash differently and precomputed rainbow tables become useless.

<!-- qard-id: ap-ec4296d333a7c0af2966 -->
> [!qard]- Why are slow hash functions better for passwords?
> They make brute-force guessing expensive.

<!-- qard-id: ap-c4f206f35febda33295b -->
> [!qard]- How should web sessions be managed?
> Use a standard library exactly as prescribed; invalidate the old session and create a new one on login.

<!-- qard-id: ap-80d9920125e50de93603 -->
> [!qard]- How is weak or hard-coded authentication mitigated?
> Force default password changes, no back doors, two-factor authentication, standard schemes.

<!-- qard-id: ap-baa0e579dcf0bb9ba394 -->
> [!qard]- How is "all users are superusers" mitigated?
> Disable guest users and sandbox untrusted visitors.

<!-- qard-id: ap-aff80e1a310ff0477085 -->
> [!qard]- Name the security cast: Eve, Mallory and Trudy.
> Eve: eavesdropper (man-in-the-middle if writing). Mallory: malicious actor. Trudy: thief after money or credentials.

<!-- qard-id: ap-8340e1a58a79d726ce9d -->
> [!qard]- What is an invalid buffer operation?
> Misusing a buffer, e.g. writing through a read-only pointer or overwriting neighbouring data.
