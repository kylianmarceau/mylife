---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 16 — Security"
---

# ASD 16 — Security

**Source note:** [Security](../../ASD/16_Security.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Trust Boundaries|Trust Boundaries]]
  - [[#Injection|Injection]]
  - [[#Authentication And Sessions|Authentication And Sessions]]
  - [[#Security As Quality And Risk|Security As Quality And Risk]]
  - [[#Security Lingo|Security Lingo]]
  - [[#OS, Code And Command Injection|OS, Code And Command Injection]]
  - [[#Session Management|Session Management]]
  - [[#Improper, Missing Or Hardcoded Authentication|Improper, Missing Or Hardcoded Authentication]]
  - [[#Memory And Trust Boundaries|Memory And Trust Boundaries]]
  - [[#Injection-Specific Controls|Injection-Specific Controls]]
  - [[#Passwords And Sessions|Passwords And Sessions]]

## Core Content

### Trust Boundaries

<!-- qard-id: ap-8d82ea745a5f7600a12e -->
> [!qard]- Why must security be designed across the system rather than added as isolated patches?
> Attackers can exploit the weakest boundary, and authentication, data handling and access control depend on consistent architecture.

<!-- qard-id: ap-cf0f21db1e109de85bdf -->
> [!qard]- Which three broad security problem areas does this lecture emphasise?
> Memory safety, code injection and authentication/session management.

<!-- qard-id: ap-800ddf0753e776812cb4 -->
> [!qard]- Why prefer established security libraries and patterns to custom fixes?
> The problems have subtle, context-specific failure modes; a plausible-looking partial fix may leave the vulnerability intact.

<!-- qard-id: ap-8867bc17d298a1aec3ea -->
> [!qard]- How can an out-of-bounds write become more than a crash?
> It may corrupt control data such as a return address or function pointer, change program state or expose unauthorised information.

<!-- qard-id: ap-e9540ff3953ba39c6577 -->
> [!qard]- How do memory-safe languages, hardening and sanitisers complement each other?
> Language/runtime rules prevent classes of misuse; hardening limits exploitation; sanitisers detect faults during exercised executions.

### Injection

<!-- qard-id: ap-1f3354bd4b080faa32a1 -->
> [!qard]- What causes SQL injection, and what is the primary defence for data values?
> Combining untrusted data with SQL syntax lets input alter the query. Bind data through parameterised queries rather than string concatenation.

<!-- qard-id: ap-265a603353024febfed8 -->
> [!qard]- How should dynamic SQL identifiers such as table names be selected?
> Map trusted choices to an explicit allow list of known identifiers; data placeholders generally do not substitute for SQL syntax/identifiers.

<!-- qard-id: ap-f803927eb4cadff16210 -->
> [!qard]- How does XSS differ from SQL injection?
> XSS makes untrusted content execute in a user's browser; SQL injection changes database commands. Defences must fit the output/interpreter context.

<!-- qard-id: ap-a44ad3feaf07ea59c3f1 -->
> [!qard]- How should untrusted text or permitted HTML be displayed?
> Use context-appropriate output encoding for text; if markup is intentionally allowed, use a trusted HTML sanitiser with a safe allow list.

<!-- qard-id: ap-1df2a652b4ca4a6d0b2a -->
> [!qard]- Why prefer an allow list to trying to enumerate every bad input?
> A defined safe subset is easier to reason about than a deny list that attackers may bypass with unanticipated forms. It still needs correct contextual use.

<!-- qard-id: ap-1bdcc14aaa5e5ff5fcc5 -->
> [!qard]- How can a program avoid shell command injection?
> Keep untrusted data out of shell syntax; use APIs with separate arguments, validate permitted values and avoid assembling commands by concatenation.

### Authentication And Sessions

<!-- qard-id: ap-2be8429d2efeb6f6ecfc -->
> [!qard]- What should be stored instead of a plaintext password?
> A per-user random salt and the result of a suitable slow password-hashing scheme; verify by deriving a hash from the submitted password and comparing through the library.

<!-- qard-id: ap-83461adc08ae0fd91fea -->
> [!qard]- Why use a different random salt for each password hash?
> Equal passwords need not have equal stored hashes, and precomputed lookup tables cannot be reused unchanged across accounts.

<!-- qard-id: ap-6d3ddfc0476a9e2bf2a5 -->
> [!qard]- Why renew the authenticated session after login?
> It prevents an attacker-controlled pre-login session identifier from remaining valid after authentication, addressing session fixation.

<!-- qard-id: ap-ef88032c9b4c8e4b1f17 -->
> [!qard]- Why is a claimed user ID insufficient authentication or authorisation?
> Attackers can supply someone else's ID. Verify identity through a trusted mechanism and check permission for each protected operation/resource.

<!-- qard-id: ap-f00cc39422958b3cbc44 -->
> [!qard]- What is the risk of giving every account administrative privileges?
> Any compromised account or injection flaw gains excessive authority; grant only permissions needed for the intended operation.

### Security As Quality And Risk

<!-- qard-id: ap-d5a502001f3940d0443d -->
> [!qard]- How do confidentiality, integrity, authenticity, accountability and non-repudiation differ?
> Protecting secrecy; protecting data from improper change; establishing genuine identities/origins; attributing actions; and providing evidence against false denial. Resistance concerns withstanding attack; each needs concrete controls.

### Security Lingo

<!-- qard-id: ap-fb693a0750f1a629c493 -->
> [!qard]- What roles do Alice/Bob, Eve, Mallory and Trudy play in the lecture's security examples?
> Ordinary participants, an eavesdropper, a malicious actor, and a thief seeking money/credentials respectively; the names label threat roles, not special algorithms.

### OS, Code And Command Injection

<!-- qard-id: ap-d0589894c55ed9dccb9a -->
> [!qard]- Why should detailed internal error messages not be exposed directly to an attacker?
> They can reveal queries, paths, implementation or account information that helps refine an attack. Keep useful diagnostic evidence internally while giving users an appropriate controlled response.

### Session Management

<!-- qard-id: ap-1409410d9e94d184f1be -->
> [!qard]- Why does HTTP need an explicit mechanism for authenticated session state?
> Requests are otherwise independent. A trusted session implementation binds later requests to authenticated server-side state or a correctly protected token, with renewal/expiry rather than trusting a claimed identity in the URL.

### Improper, Missing Or Hardcoded Authentication

<!-- qard-id: ap-b01fcb058ebb3177fc4a -->
> [!qard]- Why are default credentials, backdoors and incomplete access checks dangerous even with strong password hashing?
> They bypass or weaken the intended authentication/authorisation boundary. Require appropriate credential setup, avoid hidden bypasses and validate permissions rather than treating possession of any account as full access.

### Memory And Trust Boundaries

<!-- qard-id: ap-cfdffa65edd95b6f22a9 -->
> [!qard]- How can an out-of-bounds read threaten confidentiality without changing any data?
> It may return adjacent memory containing information the caller was not authorised to access.

<!-- qard-id: ap-dac8781268f8048a7916 -->
> [!qard]- How does an out-of-bounds write differ from a valid-index write through a forbidden pointer?
> The first leaves the intended buffer range; the second violates permitted access even within an addressable region. Both can corrupt or expose protected state.

<!-- qard-id: ap-eeba73dbe7a56ffc09de -->
> [!qard]- Why is overwriting a function return address or dispatch pointer particularly dangerous?
> It can redirect later control flow, potentially causing attacker-chosen code execution rather than only corrupting ordinary values.

<!-- qard-id: ap-61ec385ea9278d75bff9 -->
> [!qard]- Why does a memory-safe language not automatically solve SQL injection or missing authorisation?
> Those are higher-level trust/interpretation and permission failures, independent of ordinary pointer bounds/lifetime safety.

<!-- qard-id: ap-b961d231178021918070 -->
> [!qard]- What does compiler hardening such as a stack canary attempt to detect?
> Certain corruptions of protected stack/control regions before returning; it reduces some exploitation opportunities without fixing every underlying memory bug.

### Injection-Specific Controls

<!-- qard-id: ap-1f706405eba671cb50c6 -->
> [!qard]- Why does binding SQL parameters keep supplied values from becoming query syntax?
> The query structure and data are passed separately through the database API, so a value is interpreted in its data role rather than concatenated as executable SQL.

<!-- qard-id: ap-ca0ca680d25c267d44fd -->
> [!qard]- Why is escaping for HTML not interchangeable with protecting a SQL query?
> The interpreters and syntactic contexts differ. Each boundary needs its own correct mechanism; a generic “sanitised” label is insufficient.

<!-- qard-id: ap-9e243a7696249cf9153f -->
> [!qard]- Why is safe plain-text output different from intentionally permitting user-supplied HTML?
> Text should be encoded for its output context; permitted markup must additionally be parsed/sanitised to a controlled safe subset rather than executed wholesale.

<!-- qard-id: ap-4d51bd38b67bc10426f1 -->
> [!qard]- Why can verbose authentication errors leak useful information?
> Distinguishing unknown accounts, wrong secrets or internal states can help attackers narrow their guesses; give appropriately controlled responses while retaining internal diagnostics.

<!-- qard-id: ap-ff740345eaafa165ab6f -->
> [!qard]- Why should a shell-free argument API be preferred to concatenating user text into a command?
> It avoids exposing shell metacharacters as executable structure; still validate what operation and argument values the application permits.

### Passwords And Sessions

<!-- qard-id: ap-1fc31fce09980a6fae44 -->
> [!qard]- How does a one-way password hash differ from reversible password encryption?
> Verification derives and compares a protected representation rather than recovering the original secret. If decryption is possible, stealing the key can expose every stored password.

<!-- qard-id: ap-3c942b0d6176e0eaef95 -->
> [!qard]- Why are salts not required to be secret like passwords?
> Their job is uniqueness against shared precomputation/equal-hash linkage; the password-hashing scheme's resistance must not depend on hiding the salt.

<!-- qard-id: ap-490f6fbb67e348e80f67 -->
> [!qard]- Why use a deliberately costly password-hashing scheme rather than a fast generic hash?
> Each offline guess becomes more expensive for an attacker, while legitimate verification remains feasible. Use the established library's intended design.

<!-- qard-id: ap-706babe25b58a7185994 -->
> [!qard]- What is a rainbow-table attack trying to reuse?
> Precomputed password-to-hash matches. Independent random salts make one shared table ineffective across all users' salted representations.

<!-- qard-id: ap-cca881d6cf3dab5523d9 -->
> [!qard]- How does authenticating a session differ from authorising one request?
> Authentication identifies the principal; authorisation checks whether that principal may perform the requested action on the specific resource. Both boundaries are needed.
