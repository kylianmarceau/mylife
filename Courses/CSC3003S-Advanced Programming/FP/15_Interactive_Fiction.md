---
tags:
  - advanced-programming
---

# Interactive Fiction And Inform 7

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP-15-Interactive Fiction - Copy.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-15-Interactive%20Fiction%20-%20Copy.pdf), James Gain, University of Cape Town, PDF pages 1–23  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes on interactive fiction and Inform 7, a declarative, natural-language domain-specific language.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Interactive Fiction Defined|Interactive Fiction Defined]]
  - [[#Flavours Of IF|Flavours Of IF]]
  - [[#How To Play|How To Play]]
  - [[#Inform 7 And Its Design Philosophy|Inform 7 And Its Design Philosophy]]
  - [[#Case Study: Prison Break|Case Study: Prison Break]]
  - [[#Source Text Structure|Source Text Structure]]
  - [[#Mapping|Mapping]]
  - [[#Regions|Regions]]
  - [[#Kinds And Properties|Kinds And Properties]]
  - [[#Descriptions|Descriptions]]
  - [[#Doors And Locks|Doors And Locks]]
  - [[#Devices, Vehicles And People|Devices, Vehicles And People]]
  - [[#Designing Interactive Fiction|Designing Interactive Fiction]]
  - [[#Exercise: Icarus Dreams|Exercise: Icarus Dreams]]

---

## Core Content

### Interactive Fiction Defined

#### Definitions

> **Interactive fiction (IF)**: A software environment in which players control a character with natural-language text commands. It is characterised by text input and (mostly) text output and focuses on narrative and puzzles.

- **Input**: simple imperative sentences, e.g. "Go West", "Examine Jar".
- **Output**: present tense, second-person viewpoint ("You are…").

### Flavours Of IF

| Flavour | Description |
|---|---|
| **Text adventures** | The purest and earliest form; the name distinguishes them from graphic adventures |
| **MUDs** (Multi-User Dungeons) | Multiplayer internet games mixing RPG elements and instant messaging; collaborative IF |
| **Choose Your Own Adventure** | Book-based; choices decide which section you read next. The *Fighting Fantasy* series adds dice, like tabletop RPGs |

### How To Play

Games usually open with who you are, where you are, and maybe your objective. Type imperative commands at the `>` prompt; articles can be skipped (`TAKE JAR`, `OPEN JAR`).

- **Movement**: `GO SOUTH`, `SOUTH` or `S`, likewise for other directions including `UP` (`U`) and `DOWN` (`D`). Also `ENTER CAR`, `CLIMB ON SHIP`, `EXIT`, `LEAVE`, `DIVE INTO LAKE`.
- If the game keeps refusing your commands, you are probably on the wrong track.

| Command (abbr.) | Example |
|---|---|
| LOOK (L) | `LOOK UNDER BED` |
| EXAMINE (X) | `X KNIFE` |
| INVENTORY (I) | `I` |
| WAIT (Z) | `Z` |
| QUIT (Q) | `Q` |
| TAKE / DROP | `TAKE KNIFE` |
| SEARCH | `SEARCH DESK` |
| OPEN / CLOSE | `OPEN DRAWER` |
| LOCK / UNLOCK | `UNLOCK DOOR WITH RUSTY KEY` |
| ASK / TELL / SAY | `ASK JOHN ABOUT POLICE OFFICER` |

Modern games recognise hundreds of verbs and combinations such as `PUT ALL BUT HAMMER IN SACK`. `HELP` or `ABOUT` gives game information. A sample game is *Lost Pig* by Admiral Jota: you are Grunk the orc hunting a pig smarter than you. It won Best Game at the 2007 Xyzzy Awards and is 8th in the IF Top 50.

### Inform 7 And Its Design Philosophy

#### Definitions

> **Inform 7**: A natural programming language and IDE for interactive fiction. It uses simplified English-like syntax, is **declarative rather than procedural**, and has powerful IF-specific debugging tools.

Earlier versions used C-like, object-oriented syntax. Inform 7 arose in the modern era of community-supported IF.

> "The natural language in which to write interactive fiction is natural language." — Graham Nelson

1. A casual reader should be able to guess correctly what a sentence does.
2. The language should be economical, but not at the expense of intelligibility.
3. If in doubt about syntax, imitate books or newspapers.
4. Contextual knowledge is best supplied by the author rather than built in.

### Case Study: Prison Break

Inspired by the TV series: escape from Fox River Penitentiary. The puzzle:

1. A hole is hidden behind the toilet **cistern** in your cell.
2. The cistern can only be unfastened with a **sharpened bolt** on the Promenade floor.
3. The **Psycho** attacks you if you walk past his cell, so you must send your **Friend** to fetch the bolt.
4. There is a limited number of turns before **lockdown** closes all cell doors.
5. Before unfastening the cistern you must drape a **sheet** so the guards don't see.

```inform7
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

Running `test pb` executes `west`, then `east`, printing each room's description. Inside Inform descriptions, single quotes are printed as double quotes.

### Source Text Structure

A program does two things:

1. **Create things** with present-tense assertions that set starting conditions, using verbs such as *to be, to have, to carry, to wear, to contain, to support*.
2. **Lay down rules**: instructions that modify state and behaviour. Several hundred rules are built in.

| Punctuation | Use |
|---|---|
| Full stop | Terminates a command |
| `[ ]` | Comments or variables |
| `" "` | Descriptions (take care with quotes inside quotes) |

### Mapping

```inform7
Psycho Cell is a room. North of the walkway is west of Psycho Cell.
Empty Cell is a room. Northeast of the walkway is west of Empty Cell.
Friend's Cell is southeast of the Walkway. The Walkway is west of Friend's Cell.
The Promenade is down from the walkway.
```

![Prison Break map](../../../diagrams/CSC3003S-Advanced%20Programming/FP/15_Interactive_Fiction/prison-map.svg)

*Rooms are nodes and exits are edges. Some connections are deliberately asymmetric: going north from the Walkway reaches Psycho Cell, but you return by going west.*

- Maps are **graphs**: rooms are nodes, connections are edges.
- Connections run in the eight compass directions plus up and down. Inside and outside are supported: "Inside from the meadow is the woodcutter's hut" (the word *from* matters).
- Connections are **assumed symmetric**, but this can be overridden:
  - "The Walkway is west of the Empty Cell. Your Cell is east of the Walkway."
  - Asymmetric rewiring: "North of the Walkway is west of Psycho Cell."
  - One-way with *nowhere*: "South of Psycho Cell is nowhere."

### Regions

- Rooms can be grouped into **regions**, which can nest but cannot overlap.
- Rules can apply to a specific region, and regions are colour-coded in the World Index.

```inform7
AllCells is a region. Your cell, empty cell, friend's cell and psycho cell are in allcells.
Allwalkways is a region. Your walkway, friend's walkway, empty walkway and psycho walkway are in allwalkways.
Cell Block A is a region. Allcells, allwalkways and promenade are in Cell Block A.
```

### Kinds And Properties

#### Definitions

> **Kind**: An object type such as room, thing, container, supporter or direction.

> **Either/or property**: A Boolean-style property such as open/closed, openable/not openable, transparent/opaque, fixed in place/portable, edible/inedible.

- Kinds are often **inferred**: in "A book is on the library cart in your walkway.", the book is a thing and the cart a supporter.
- They can also be assigned directly: "In your walkway is a supporter called the library cart."
- Properties apply to objects of a suitable kind: "The Cistern is an openable opaque container. The Cistern is fixed in place."

### Descriptions

| Description | When shown | Example |
|---|---|---|
| Initial appearance | First time the object is seen | The bolt is here. "A long rusted bolt. It might serve as a weapon in an emergency." |
| Description | When examined | The description of the bolt is "On closer examination you see that the point has been filed slightly…" |
| Printed name | In the inventory list | The printed name of the bolt is "carefully-filed bolt". |

### Doors And Locks

```inform7
Your Cell Gate is west of Your Cell and east of Your Walkway. It is a door.
Your Cell Gate is lockable and locked. The Guards Key unlocks Your Cell Gate.
```

- A door sits between two rooms, and both sides are stated.
- The second sentence, "It is a door.", is needed because Inform would otherwise infer from "is west of Your Cell" that Your Cell Gate is a **room**.
- By default, doors are fixed in place, closed and openable.
- Doors can be locked or unlocked, lockable or not, and have a matching key. Containers can also be locked; supporters cannot.

### Devices, Vehicles And People

| Kind | Behaviour | Example |
|---|---|---|
| **Device** | Switched on/off (off by default); descriptions can depend on state | The tape recorder is a device in your cell. "[if switched off] Devices like these are not allowed in prison. [otherwise] a voice on the tape says 'I'm sorry Michael. I dropped your bolt out on the promenade when the guards frisked me'." |
| **Vehicle** | An enterable container; can be made pushable | In the yard is a vehicle called Prison Truck. It is pushable between rooms. |
| **Person** | A person is a thing; men, women and animals are kinds of person | In friend's cell is a man called Fernando Sucre. |

Extensions add vehicles you ride on rather than in, such as horses or tricycles.

### Designing Interactive Fiction

> "An adventure game is a crossword at war with a narrative." — Graham Nelson

The design tips:

- Avoid linearity in narrative and puzzle-solving.
- Keep internal consistency (realism).
- Be descriptive, but not overly so.
- Beware the trap of exponential growth.

The **Player's Bill of Rights** says a player has the right:

1. Not to be killed without warning.
2. Not to be given horribly unclear hints.
3. To be able to win without experience of past lives.
4. To be able to win without knowledge of future events.
5. Not to have the game closed off without warning.

### Exercise: Icarus Dreams

```inform7
"Icarus Dreams" by James Gain

A ledge is a kind of room. The description of a ledge is "This ledge is narrow and
crumbling. You press yourself flat against the cliff face to avoid falling into the
sea below. You could go down or maybe east or west along the ledge."

The Projecting Spur is a room. "A piece of rock projects out over the sea. It glistens in the sunlight."

Down from the spur is a ledge called High-ledge Left. Up from high-ledge left is nowhere.
East from high-ledge left is a ledge called High-ledge Right. The wax wings is here.
The wax wings is wearable. The indefinite article of wax wings is "a pair of".

Down from high-ledge right is a ledge called low-ledge right. Up from low-ledge right is nowhere.
The climbing boots is here. The climbing boots is wearable.
The indefinite article of climbing boots is "a pair of".

Down from high-ledge left is a ledge called Low-ledge Left. Up from low-ledge left is nowhere.
East of low-ledge left is a Low-ledge Right.
Down from low-ledge left is the Drowning Sea. Down from low-ledge right is the Drowning Sea.
Nowhere is up from the drowning sea.

West of low-ledge left is the vertical crack. Up from the vertical crack is west of projecting spur.
Vertical crack is a door. Vertical crack is locked and lockable. The matching key is the climbing boots.

Fly Away is a scene. Fly Away begins when play begins. Fly Away ends when the player
is in the Projecting Spur and the player is wearing the wax wings.

When Fly Away ends:
  say "You run out along the projecting spur and fling yourself out into space. You
  plummet downwards but then an updraft catches your wings and you are borne up and away."
```

![Icarus Dreams map](../../../diagrams/CSC3003S-Advanced%20Programming/FP/15_Interactive_Fiction/icarus-map.svg)

*Downward moves are one-way. The only way back up to the spur is through the locked vertical crack, which the climbing boots unlock.*

One solution route:

1. From the Projecting Spur, go **down** to High-ledge Left.
2. Go **east** to High-ledge Right and take and wear the **wax wings**.
3. Go **down** to Low-ledge Right and take the **climbing boots**.
4. Go **west** to Low-ledge Left.
5. **Unlock** the vertical crack with the boots, go west through it, then **up** to the Projecting Spur.
6. Arriving wearing the wings ends the scene *Fly Away*.

The source also shows **kinds of room** (`A ledge is a kind of room`), shared descriptions, one-way exits with *nowhere*, a door unlocked by a wearable key, and **scenes** with begin/end conditions.
