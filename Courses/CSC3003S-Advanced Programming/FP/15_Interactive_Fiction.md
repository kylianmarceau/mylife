---
tags:
  - advanced-programming
---

# Interactive Fiction And Inform 7

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP-15-Interactive Fiction - Copy.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-15-Interactive%20Fiction%20-%20Copy.pdf), James Gain, University of Cape Town, pages 1–23
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Interactive fiction as a genre, how to play it, and Inform 7 as a declarative, natural-language domain-specific language: rooms, maps, regions, kinds, descriptions, doors, devices, vehicles, people and scenes.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Interactive Fiction Is|What Interactive Fiction Is]]
  - [[#Flavours Of Interactive Fiction|Flavours Of Interactive Fiction]]
  - [[#How To Play|How To Play]]
  - [[#Inform 7 And Its Design Philosophy|Inform 7 And Its Design Philosophy]]
  - [[#Case Study: Prison Break|Case Study: Prison Break]]
  - [[#Source Text Structure|Source Text Structure]]
  - [[#Mapping|Mapping]]
  - [[#Regions|Regions]]
  - [[#Kinds And Either/Or Properties|Kinds And Either/Or Properties]]
  - [[#Descriptions|Descriptions]]
  - [[#Doors And Locks|Doors And Locks]]
  - [[#Devices, Vehicles And People|Devices, Vehicles And People]]
  - [[#Designing Interactive Fiction|Designing Interactive Fiction]]
  - [[#Example: Icarus Dreams|Example: Icarus Dreams]]

---

## Core Content

### What Interactive Fiction Is

#### Definitions

> **Interactive fiction (IF)**: A software environment in which players control a character using natural-language text commands. It is characterised by text input and (mostly) text output, and focuses on narrative and puzzles.

| Aspect | Form |
|---|---|
| Input | Simple imperative sentences: "Go west", "Examine jar" |
| Output | Present tense, second-person viewpoint ("You are in…") |

### Flavours Of Interactive Fiction

| Flavour | Description |
|---|---|
| **Text adventures** | The purest and earliest form; the name distinguishes them from graphic adventures |
| **MUDs (Multi-User Dungeons)** | Multiplayer internet games mixing RPG elements and instant messaging — a kind of collaborative IF |
| **Choose Your Own Adventure** | Book-based; choices decide which section is read next. The *Fighting Fantasy* series adds dice, like tabletop RPGs |

### How To Play

A game usually starts with an introduction: who you are, where you are and (maybe) your objectives. At the `>` prompt you type imperative commands; articles can be skipped (`TAKE JAR`, `EXAMINE JAR`, `OPEN JAR`).

**Movement**: `GO SOUTH`, `SOUTH` or just `S`; likewise other directions, including `UP` (`U`) and `DOWN` (`D`). Other movement verbs: `ENTER CAR`, `GO CAR`, `CLIMB ON SHIP`, `EXIT`, `LEAVE`, `DIVE INTO LAKE`.

If the game keeps refusing your commands, you're probably on the wrong track.

| Command | Example |
|---|---|
| `LOOK` (`L`) | `LOOK UNDER BED` |
| `TAKE` / `DROP` | `TAKE KNIFE` |
| `LOCK` / `UNLOCK` | `UNLOCK DOOR WITH RUSTY KEY` |
| `EXAMINE` (`X`) | `X KNIFE` |
| `SEARCH` | `SEARCH DESK` |
| `INVENTORY` (`I`) | `I` |
| `OPEN` / `CLOSE` | `OPEN DRAWER` |
| `ASK` / `TELL` / `SAY` | `ASK JOHN ABOUT POLICE OFFICER` |
| `WAIT` (`Z`) | `Z` |
| `QUIT` (`Q`) | `Q` |
| `HELP` / `ABOUT` | General game information |

Modern games recognise hundreds of verbs and combinations, e.g. `PUT ALL BUT HAMMER IN SACK`.

**Sample game: *Lost Pig*** (Admiral Jota). You are Grunk, an orc sent to find the farmer's pig — which is more intelligent than you. Short but rich in responses; fantasy/humour; Best Game at the 2007 Xyzzy Awards and 8th in the IF Top 50 of all time.

### Inform 7 And Its Design Philosophy

#### Definitions

> **Inform 7**: A natural-language programming language and IDE for interactive fiction. It uses simplified English-like syntax, is **declarative** rather than procedural, and has powerful IF-specific debugging tools.

It arose in the modern era of community-supported IF. Earlier Inform versions used C-like syntax and were object-oriented.

> "The natural language in which to write interactive fiction is natural language." — Graham Nelson

Design principles:

1. A casual reader should be able to guess correctly what a sentence does.
2. The language should be economical, but not at the expense of intelligibility.
3. If in doubt about syntax, imitate books or newspapers.
4. Contextual knowledge is best supplied by the author rather than built in.

### Case Study: Prison Break

Inspired by the TV series *Prison Break*: escape from Fox River Penitentiary.

The central puzzle:

1. There is a hole behind the toilet cistern in Your Cell.
2. The cistern can only be unfastened with a sharpened bolt lying on the Promenade floor.
3. The Psycho attacks you if you walk past his cell, so you must send your Friend to fetch the bolt.
4. You have a limited number of turns before lockdown, when all cell doors close.
5. Before unfastening the cistern, you must drape a sheet so the guards don't see you escape.

Building the first two rooms:

```text
"Prison Break" by James Gain

Your Cell is a room. "A steel-framed bunk with regulation sheets and a leaking
toilet are squeezed into a space barely longer than a coffin. Carved into the
wall is the motto: 'Michael was here!' The automatic gate to your cell is open
to the west. Beyond the opening is an industrial steel walkway that overlooks a
'promenade' below."

The Walkway is west of Your Cell. "Narrow. It's easy to slip and 'accidentally'
fall over the railing. There are stairs at the far end, but Bagwell's cell is
between you and them. 'Here fishy fishy fishy', he says."

Test pb with "west / east".
```

Typing `test pb` runs the scripted commands `west` then `east`, printing each room's name and description — a built-in debugging tool.

### Source Text Structure

A program has two parts:

| Part | How |
|---|---|
| **Create things** | Present-tense assertions that set starting conditions, using verbs such as *to be, to have, to carry, to wear, to contain, to support* |
| **Lay down rules** | Instructions that modify state and behaviour; several hundred rules are built in |

Punctuation:

- Normal punctuation generally applies; full stops end statements.
- Square brackets `[ ]` mark comments or variables.
- Quotation marks `" "` enclose descriptions; take care with quotes inside quotes (use single quotes).

### Mapping

The prison map in source:

```text
Your Cell is a room. "..."
The Walkway is west of Your Cell. "..."
Psycho Cell is a room. North of the walkway is west of Psycho Cell.
Empty Cell is a room. Northeast of the walkway is west of Empty Cell.
Friend's Cell is southeast of the Walkway. The Walkway is west of Friend's Cell.
The Promenade is down from the walkway.
```

![Prison Break map](../../../diagrams/CSC3003S-Advanced%20Programming/FP/15_Interactive_Fiction/prison-map.svg)

*Rooms are nodes and exits are edges; several connections are deliberately asymmetric.*

Maps are graphs:

- **Rooms** are nodes; **connections** are edges.
- Connections use the eight compass directions (north, northeast, …) plus up and down.
- Inside/outside is supported: "Inside from the meadow is the woodcutter's hut" (the word *from* matters).

| Connection type | Example |
|---|---|
| Symmetric (default) | "The Walkway is west of Your Cell" also makes Your Cell east of the Walkway |
| Override the symmetric assumption | "The Walkway is west of the Empty Cell. Your Cell is east of the Walkway." |
| Asymmetric | "North of the Walkway is west of Psycho Cell." (go north from the Walkway, but return by going west) |
| One-way | "South of Psycho Cell is nowhere." |

### Regions

#### Definitions

> **Region**: A named group of rooms. Regions can be nested but cannot overlap, and rules can apply to a region specifically. The Inform 7 World Index colour-codes them.

```text
AllCells is a region. Your cell, empty cell, friend's cell and psycho cell are in allcells.
Allwalkways is a region. Your walkway, friend's walkway, empty walkway and psycho walkway
are in allwalkways.
Cell Block A is a region. Allcells, allwalkways and promenade are in Cell Block A.
```

### Kinds And Either/Or Properties

#### Definitions

> **Kind**: An object type, such as room, thing, container, supporter or direction.

> **Either/or property**: A two-valued property such as open/closed, openable/not openable, transparent/opaque, fixed in place/portable, edible/inedible.

Kinds are often **inferred** from the text: "A book is on the library cart in your walkway." makes the book a thing and the cart a supporter (things are *on* supporters). They can also be set directly: "In your walkway is a supporter called the library cart."

Either/or properties can be assigned to objects of a suitable kind: "The Cistern is an openable opaque container. The Cistern is fixed in place."

### Descriptions

Objects can have three descriptions:

| When shown | Example |
|---|---|
| On first appearance | `The bolt is here. "A long rusted bolt. It might serve as a weapon in an emergency."` |
| When examined | `The description of the bolt is "On closer examination you see that the point has been filed slightly, as if somebody started making a shank but gave up."` |
| In the inventory list | `The printed name of the bolt is "carefully-filed bolt".` |

### Doors And Locks

Doors sit between rooms:

```text
Your Cell Gate is west of Your Cell and east of Your Walkway. It is a door.
```

The second sentence is needed because otherwise Inform would infer "Your Cell Gate" is a room. By default doors are fixed in place, closed and openable.

Locks:

- A door can be locked/unlocked, lockable/not lockable, and have a matching key.
- "Your Cell Gate is lockable and locked. The Guards Key unlocks Your Cell Gate."
- Containers can also be locked; supporters cannot.

### Devices, Vehicles And People

| Kind | Behaviour | Example |
|---|---|---|
| **Device** | Can be switched on or off (off by default); descriptions can change accordingly | `The tape recorder is a device in your cell. "[if switched off] Devices like these are not allowed in prison. [otherwise] a voice on the tape says 'I'm sorry Michael. I dropped your bolt out on the promenade when the guards frisked me'."` |
| **Vehicle** | An enterable container; can be made pushable between rooms. Extensions add vehicles ridden *on* (horses, tricycles) | `In the yard is a vehicle called Prison Truck. It is pushable between rooms.` |
| **Person** | A person is a thing; men, women and animals are kinds of person | `In friend's cell is a man called Fernando Sucre.` |

A lecture exercise details your cell with the cistern: an openable, fixed-in-place container that hides the escape route and can only be moved using the bolt.

### Designing Interactive Fiction

> "An adventure game is a crossword at war with a narrative." — Graham Nelson

Tips:

- Avoid linearity in both narrative and puzzle-solving.
- Ensure internal consistency (realism).
- Be descriptive, but not overly so.
- Beware the trap of exponential growth in content.

**The Player's Bill of Rights** — the player has the right:

1. not to be killed without warning;
2. not to be given horribly unclear hints;
3. to be able to win without experience of past lives;
4. to be able to win without knowledge of future events;
5. not to have the game closed off without warning.

### Example: Icarus Dreams

```text
"Icarus Dreams" by James Gain

A ledge is a kind of room. The description of a ledge is "This ledge is narrow and
crumbling. You press yourself flat against the cliff face to avoid falling into the
sea below. You could go down or maybe east or west along the ledge."

The Projecting Spur is a room. "A piece of rock projects out over the sea. It
glistens in the sunlight."

Down from the spur is a ledge called High-ledge Left. Up from high-ledge left is nowhere.
East from high-ledge left is a ledge called High-ledge Right. The wax wings is here.
The wax wings is wearable. The indefinite article of wax wings is "a pair of".

Down from high-ledge right is a ledge called low-ledge right. Up from low-ledge right
is nowhere. The climbing boots is here. The climbing boots is wearable. The indefinite
article of climbing boots is "a pair of".

Down from high-ledge left is a ledge called Low-ledge Left. Up from low-ledge left is
nowhere. East of low-ledge left is a Low-ledge Right.
Down from low-ledge left is the Drowning Sea. Down from low-ledge right is the
Drowning Sea. Nowhere is up from the drowning sea.

West of low-ledge left is the vertical crack. Up from the vertical crack is west of
projecting spur. Vertical crack is a door. Vertical crack is locked and lockable.
The matching key is the climbing boots.

Fly Away is a scene. Fly Away begins when play begins. Fly Away ends when the player
is in the Projecting Spur and the player is wearing the wax wings.
When Fly Away ends:
    say "You run out along the projecting spur and fling yourself out into space.
    You plummet downwards but then an updraft catches your wings and you are borne
    up and away."
```

![Icarus Dreams map](../../../diagrams/CSC3003S-Advanced%20Programming/FP/15_Interactive_Fiction/icarus-map.svg)

*Every way down the cliff is one-way; the only route back to the spur is the locked vertical crack.*

New features here:

- **A kind of room** (`ledge`) shares one description across several rooms.
- `nowhere` makes the descents one-way.
- A **door's key can be any thing** — here the climbing boots.
- A **scene** with a start condition, an end condition and an ending rule, which wins the game.

A winning command sequence (the lecture exercise):

1. `D` — to High-ledge Left (no way back up).
2. `E` — to High-ledge Right; `TAKE WINGS`.
3. `D` — to Low-ledge Right; `TAKE BOOTS`.
4. `W` — to Low-ledge Left (avoid going down into the Drowning Sea).
5. `UNLOCK CRACK WITH BOOTS`, `OPEN CRACK`, `W` — up through the crack to the Projecting Spur.
6. `WEAR WINGS` — the Fly Away scene ends and you escape.
