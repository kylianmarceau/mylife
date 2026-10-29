---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 15 — Interactive Fiction And Inform 7"
---

# FP 15 — Interactive Fiction And Inform 7

**Source note:** [Interactive Fiction And Inform 7](../../FP/15_Interactive_Fiction.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Inform 7 And World Modelling|Inform 7 And World Modelling]]
  - [[#Rules And Fair Play|Rules And Fair Play]]
  - [[#Flavours Of IF|Flavours Of IF]]
  - [[#How To Play|How To Play]]
  - [[#Inform 7 And Its Design Philosophy|Inform 7 And Its Design Philosophy]]
  - [[#Source Text Structure|Source Text Structure]]
  - [[#Devices, Vehicles And People|Devices, Vehicles And People]]
  - [[#Designing Interactive Fiction|Designing Interactive Fiction]]
  - [[#World Representation And Rules|World Representation And Rules]]

## Core Content

### Inform 7 And World Modelling

<!-- qard-id: ap-18f46cc4f5921d205ffb -->
> [!qard]- What is interactive fiction, and why is Inform 7 domain-specific?
> IF is a narrative/puzzle world controlled through text commands. Inform 7 provides English-like declarations and rules tailored to modelling and interacting with that world.

<!-- qard-id: ap-08275f23e74d152d248b -->
> [!qard]- What two main jobs does Inform 7 source text perform?
> Declare objects, relationships and initial state; define rules that govern actions and changes.

<!-- qard-id: ap-0d0e38aa3c932959020e -->
> [!qard]- How is an Inform 7 map a graph?
> Rooms are nodes and directional exits are edges. Connections are normally reciprocal, but can be rewired or made one-way.

<!-- qard-id: ap-404691f57df26aa2b435 -->
> [!qard]- How does `nowhere` affect a map connection?
> It removes an exit in a specified direction, allowing one-way movement or overriding an inferred connection.

<!-- qard-id: ap-1e2ca73bc5cf057dc1db -->
> [!qard]- What is a region used for?
> Group rooms so shared rules and organisation apply to them. Regions may nest but must not overlap.

<!-- qard-id: ap-b10440b2c4d36179bfbd -->
> [!qard]- What are kinds and either/or properties?
> Kinds classify objects, such as rooms, containers or devices; either/or properties encode alternatives such as open/closed or portable/fixed.

<!-- qard-id: ap-f1506756e536213774e2 -->
> [!qard]- How do a container and a supporter differ?
> A container holds things inside; a supporter holds things on top. Their supported actions and properties differ.

<!-- qard-id: ap-fb180185932132add667 -->
> [!qard]- Why explicitly declare a named connection to be a door?
> Otherwise directional assertions can make Inform infer it is a room. A door connects two sides and may be openable, lockable and matched to a key.

<!-- qard-id: ap-8705b1c9358f23449135 -->
> [!qard]- How do initial appearance, description and printed name differ?
> Initial appearance introduces an object; description is shown when examined; printed name controls the displayed object name, including listings.

### Rules And Fair Play

<!-- qard-id: ap-8eda0553b5e511ede605 -->
> [!qard]- What does a scene's begin/end condition express?
> A rule-defined phase of play triggered or completed when world-state conditions hold; its start/end rules can produce effects or narrative.

<!-- qard-id: ap-f234eda24d3cc3c776c9 -->
> [!qard]- What makes an interactive-fiction puzzle fair?
> Consistent rules, understandable hints and warnings before lethal or irreversible consequences, without requiring knowledge from future events or previous failed lives.

### Flavours Of IF

<!-- qard-id: ap-77013c00be562717f187 -->
> [!qard]- How do text adventures, MUDs and choose-your-own-adventure fiction differ?
> Text adventures interpret commands in a simulated world; MUDs add networked multiplayer interaction; branching books/games present choices leading to predefined next passages.

### How To Play

<!-- qard-id: ap-cd72cef0965408a0f27c -->
> [!qard]- Which command families help a player investigate and manipulate an IF world?
> Movement (`N`, `GO WEST`, `UP`), observation (`LOOK`, `EXAMINE`), inventory, taking/dropping, searching, opening/locking, conversation and waiting. Inspecting objects and feedback is part of solving the puzzle.

### Inform 7 And Its Design Philosophy

<!-- qard-id: ap-4bd1ee43598b687ef7b1 -->
> [!qard]- What trade-off does Inform 7's natural-language design seek?
> Economical, readable declarations whose effects a casual reader can often infer, while still obeying precise language rules and relying on author-supplied context rather than unrestricted English understanding.

### Source Text Structure

<!-- qard-id: ap-648bd072b679525fab5f -->
> [!qard]- How do punctuation and `Test ... with ...` support Inform 7 authoring?
> Full stops end declarations; quoted text supplies descriptions; square brackets serve comments/substitutions depending on context. A named test string runs a scripted sequence of player commands for repeatable checks.

### Devices, Vehicles And People

<!-- qard-id: ap-a400039708ba33841fb9 -->
> [!qard]- What behaviours do Inform 7's device, vehicle and person kinds provide?
> Devices have switched-on/off state; vehicles are enterable containers for movement; people participate as characters, with more specific kinds such as animals. Descriptions/rules may depend on their state.

### Designing Interactive Fiction

<!-- qard-id: ap-d7f507939e931ae30bce -->
> [!qard]- What design principles complement the Player's Bill of Rights?
> Offer meaningful alternative routes/order, maintain consistent world rules, provide useful but economical descriptions and control combinatorial growth; avoid obscure hints, unwarned dead ends and required foreknowledge.

### World Representation And Rules

<!-- qard-id: ap-d680ced80da1640ee7b1 -->
> [!qard]- Why is Inform 7 declarative even though a running story changes state?
> The author states world relationships, properties and rules; the system supplies much of the command interpretation and control machinery. Declarative does not require the simulated world to stay unchanged.

<!-- qard-id: ap-fedd0292ca1142d82145 -->
> [!qard]- What does a directional relationship normally imply about the reverse route?
> Inform normally supplies the reciprocal connection; explicit declarations can override it, so check each outgoing direction when modelling an asymmetric map.

<!-- qard-id: ap-6bec53d20106a3cb77b1 -->
> [!qard]- Why can “inside from” and “outside from” matter separately from compass directions?
> They describe entry/exit relationships whose precise syntax and reciprocal routes must match the intended map, rather than being interchangeable with every directional assertion.

<!-- qard-id: ap-535b86da7d3248c7b2bc -->
> [!qard]- What is the constraint on nested regions?
> One region may contain another, but overlapping membership is disallowed; use the hierarchy to apply shared rules coherently.

<!-- qard-id: ap-cd580f5f074f7b62485f -->
> [!qard]- How can Inform infer an object's kind from its relationships?
> Placement “on” another object can imply a supporter, while containment/room statements supply different contextual information; explicit kind declarations resolve ambiguity.

<!-- qard-id: ap-09d8d1c0146e2e891073 -->
> [!qard]- How do open/closed, openable/not-openable and locked/unlocked describe different properties?
> Current opening state, capability to be opened, and access restriction are separate; something can be closed yet not openable, or lockable but currently unlocked.

<!-- qard-id: ap-db1858b42901e1c10082 -->
> [!qard]- Why does a door declaration need both its spatial role and its object kind?
> Directions establish the connected rooms; the kind supplies door behaviour instead of accidentally treating the named connection as another room.

<!-- qard-id: ap-f39b01c740f1ad322974 -->
> [!qard]- How does matching a key to a lock express a domain relation?
> It states which object authorises the unlock action; the key need not be a conventional-looking key if the game consistently defines another object for that role.

<!-- qard-id: ap-31ad984a974f2507f809 -->
> [!qard]- How do conditional descriptions communicate simulated state?
> Text substitutions choose appropriate output according to properties such as switched-on/off, letting observation expose meaningful changes to the player.

<!-- qard-id: ap-424d111e527991b68d51 -->
> [!qard]- What is the difference between winning through deduction and requiring a previous failed life?
> Fair clues and consistent rules let the current player infer a solution; mandatory foreknowledge from an unwarned failure violates the stated Player's Bill of Rights.

<!-- qard-id: ap-3a08c782a37ac169a31e -->
> [!qard]- Why can branching puzzle dependencies create exponential authoring/testing work?
> Choices combine with object and world states, multiplying possible interactions. Limit unnecessary combinations while retaining meaningful player freedom.
