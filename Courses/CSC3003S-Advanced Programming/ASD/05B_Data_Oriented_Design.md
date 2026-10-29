---
tags:
  - advanced-programming
---

# Data-Oriented Design

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD05 Data oriented design - Copy.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD05%20Data%20oriented%20design%20-%20Copy.pdf), Johan Bontes, University of Cape Town, PDF pages 1–56 (2026 version; `ASD05 Data oriented design.pdf` is the identical 2025 deck)  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: why OOP is slow for bulk data, how CPUs and caches move data and code, the costs of heap objects and virtual calls, the three DOD steps, and CPU code flow (pipelining, prediction, superscalar and out-of-order execution).

> [!note] <span style="color:#b89aff">Not examinable</span>
> The purple-titled slides "Hot data?" (register file and μop cache sizes) and "Eviction schemes" are marked not examinable. They are included briefly for context.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What DOD Is And When To Use It|What DOD Is And When To Use It]]
  - [[#The Problem With Traditional OOP|The Problem With Traditional OOP]]
  - [[#How A CPU Works: Feeding The Beast|How A CPU Works: Feeding The Beast]]
  - [[#The Cache Hierarchy And Hot Data|The Cache Hierarchy And Hot Data]]
  - [[#Cache Movement, Eviction And Load Size|Cache Movement, Eviction And Load Size]]
  - [[#Access Patterns: Sequential Versus Random|Access Patterns: Sequential Versus Random]]
  - [[#Anatomy Of An Object And The Heap|Anatomy Of An Object And The Heap]]
  - [[#Problem 1: Objects Live On The Heap|Problem 1: Objects Live On The Heap]]
  - [[#Problem 2: Virtual Methods And Cache Eviction|Problem 2: Virtual Methods And Cache Eviction]]
  - [[#Stack Versus Heap, And Polymorphism|Stack Versus Heap, And Polymorphism]]
  - [[#DOD Step 1: Find The Hot Code (Measure)|DOD Step 1: Find The Hot Code (Measure)]]
  - [[#DOD Step 2: Analyse The Data Flow|DOD Step 2: Analyse The Data Flow]]
  - [[#DOD Step 3: Data That Flows Together Stays Together|DOD Step 3: Data That Flows Together Stays Together]]
  - [[#DOD Speed-Up And Other Benefits|DOD Speed-Up And Other Benefits]]
  - [[#CPU Code Flow: Pipelining And Prediction|CPU Code Flow: Pipelining And Prediction]]
  - [[#Superscalar And Out-Of-Order Execution|Superscalar And Out-Of-Order Execution]]
  - [[#Stack Engine And What The Compiler Can't Do|Stack Engine And What The Compiler Can't Do]]

---

## Core Content

### What DOD Is And When To Use It

#### Definitions

> **Data-oriented design (DOD)**: A technique to speed up data processing by organising code around how data flows through the CPU, rather than around real-world objects. It requires you to "think like a CPU": what slows it down, what speeds it up?

**Rule 1: if it ain't broke, don't fix it.**

- DOD is all about **lots of data**. No lots of data, no DOD; consider using a database instead.
- It is used for lots of uniform data that must be processed when a database can't be used: inside database engines, games, numerical simulation (number crunching) and solvers.
- Database techniques are moving into game engines, e.g. SpacetimeDB.

### The Problem With Traditional OOP

Traditional OOP courses say to map real-world entities to objects and solve issues with more objects. But:

- The real world is complex, so a 1-to-1 mapping creates **blob objects**.
- A "correct" OOP mapping has lots of **indirection**: extra work for the CPU, so it is slow.
- Objects live on the **heap**.
- Objects mix **hot and cold** data, and **read-only and read-write** data.

![Pacman OOP versus DOD](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05B_Data_Oriented_Design/pacman-oop-vs-dod.svg)

*In the OOP design, the hot drawing path runs through a deep Sprite hierarchy of heap objects. In the DOD design, the sprite data collapses into arrays inside `Board`, leaving the cold timer, input and AI classes untouched.*

### How A CPU Works: Feeding The Beast

The CPU is a **von Neumann machine**: code and data share memory and move through the same system.

| Source | Bandwidth | Relative to the CPU |
|---|---|---|
| 5 GHz core ($5\text{G}\times 32\times 4$) | $\approx 600$ GiB/s per core | — |
| DDR5-5600, sequential | 70 GiB/s | about 10× slower |
| DDR5-5600, random access | $\approx 400$ MiB/s | about 1500× slower |
| 8-core CPU | $600\times 8 = 4.8$ TiB/s | — |

RAM cannot keep up with the cores, especially for random access.

### The Cache Hierarchy And Hot Data

#### Definitions

> **Hot data**: A small amount of data used over and over: lookup tables, database indexes, sprite coordinates, local variables on the stack, scratchpads, data inside loops.

> **Cache**: Small, fast memory close to the CPU that holds the hottest data.

Most time is spent on hot data, so the hottest data is kept closest to the CPU.

![Cache hierarchy](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05B_Data_Oriented_Design/cache-hierarchy.svg)

*Zen 5: register file plus μop cache (~600 GiB/s), L1 (200 GiB/s), L2 (20 GiB/s), shared L3 (2 GiB/s), RAM (0.4 GiB/s best case).*

The CPU has a small notepad for data, the **register file** (about 500 variables), and a small "screen" for code, the **μop cache** (about 6000 micro-ops). This slide is not examinable.

### Cache Movement, Eviction And Load Size

The CPU **cannot use RAM directly**:

- Data is usable only once it is in the register file; code only once it is in the μop cache.
- Data moves RAM → L3 → L2 → L1 → CPU. New data in means old data out.
- The closer to the CPU, and the more recently or frequently used, the hotter the data.

**Eviction schemes** (not examinable):

| Era | Policy |
|---|---|
| 2000s | LRU: evict the least recently used |
| 2010s | LFU: evict the least frequently used (coldest) |
| Modern | A tiny neural network mixing LRU and LFU, plus prediction of the next data and code (speculative prefetching, which has security implications) |

Tip: **make your data use predictable**.

**Why evict so much?** The minimum load size is **32 bytes** on AMD and Intel. Ask for 1 byte and 32 bytes are fetched, evicting 32 other bytes. This lets the hardware fetch 256 bits in parallel, 32× faster than one byte at a time. Every CPU speed hack has a drawback somewhere else.

### Access Patterns: Sequential Versus Random

```java
final int GB = 1024 * 1024 * 1024;
int[] array[1*GB];               // 4 GiB of ints
for (var a: array) {             // A: sequential access
  doStuff(a);
}
r = new Random();
for (var i = 0; i < GB; i++) {   // B: random access
  var i2 = r.nextInt(GB);
  a = array[i2];
  doStuff(a);
}
```

Sequential access (A) streams through memory and the prefetcher predicts it. Random access (B) misses the cache on almost every read and can be over 1000× slower.

```java
Integer[] array2[1*GB];   // ~48 GiB after initialisation: why?
for (var a: array2) {     // effectively random access: why?
  doStuff(a);
}
```

- `Integer` is an object. The array holds 8-byte **links** to separately allocated heap objects, each with its own header and padding. That explains the roughly 48 GiB.
- Iterating the array sequentially still dereferences each link to a scattered heap location, so the access pattern is effectively random.

### Anatomy Of An Object And The Heap

#### Definitions

> **Stack**: Where local variables live. It is effectively always in L1.

> **Heap**: The object store in main memory.

> **Virtual method table (VMT)**: A per-class table of code pointers, used to find the right method at run time.

```java
ObjectX a;          // local variable: on the stack (L1/CPU)
a = new ObjectX();  // ObjectX allocated on the heap
```

- `a` is a link (pointer, 8 bytes) to the heap object.
- An object combines data and code:

```c
ObjectX = struct {
  VMT;      // 'this'-side pointer to the virtual method table (list of code)
  Data;     // data members
  padding;  // fill so the size is a multiple of 8 bytes
}
```

**The heap** keeps 4 free lists (tiny, small, medium and large objects).

- Allocation is first come, first served.
- Destruction happens at random times (garbage collection).
- So objects end up **randomly distributed** through memory, and heap bookkeeping also takes space.

### Problem 1: Objects Live On The Heap

- Object data and code are spread randomly over memory, and related objects are not stored sequentially.
- The longer the program runs, the more random the layout becomes.
- Each object access can add about a **1500-cycle** penalty, time in which the core could have done about 6000 calculations. It is much worse in multi-threaded code.

### Problem 2: Virtual Methods And Cache Eviction

```java
Sprites[5] dolls;
for (var i:1..4) { dolls[i] = new Ghost(); }
dolls[0] = new Pacman();
// ... game loop
  dolls[i].moveto(x,y);
```

1. Look up the right doll on the heap.
2. `moveto = doll.VMT[42]`, a pointer to code.
3. Call `moveto`. The call **cannot be predicted**: the doll might be a ghost, Pacman or a zombie, each moving differently.

With an inheritance chain the cost multiplies:

```java
public void Ghost.draw()        { bitmap = getScaryBitmap(); super.draw(); }
public void MovingSprite.draw() { location = point(x,y);     super.draw(); }
Sprite.draw()                   { display.draw(bitmap, location); }
```

One `dolls[i].draw()` makes 13 steps:

1. Look up the doll on the heap.
2. `draw = doll.VMT[41]`.
3. Call `Ghost.draw()`.
4. `parent = doll.VMT[0]`.
5. `draw = parent.VMT[41]`.
6. Call `MovingSprite.draw()`.
7. `grandparent = parent.VMT[0]`.
8. `draw = grandparent.VMT[41]`.
9. Call `Sprite.draw()`.
10. Look up the display object on the heap.
11. `draw = display.VMT[125]`.
12. Call `Display.draw(bitmap, location)`.
13. Look up the bitmap object on the heap.

![Virtual dispatch chain](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05B_Data_Oriented_Design/virtual-dispatch.svg)

*Each hop is an indirect lookup: heap misses evict the data cache, and unpredictable calls evict the code cache and stall the pipeline.*

- **2a, data cache eviction**: each heap lookup pulls whole objects into L1, evicting other hot data.
- **2b, code cache eviction**: the first call (`Ghost.draw`) cannot be predicted and the later ones only maybe. Code for each class must be fetched into the L1 code cache.

### Stack Versus Heap, And Polymorphism

In Java, everything created with `new` lives on the heap and is reached through up to three levels of indirection:

1. The variable holds a link to the object.
2. Every non-static method is called indirectly through the VMT.
3. Fields of object type, like `Bear bear;`, are themselves links.

| | Stack | Heap |
|---|---|---|
| Access | Direct | Indirect |
| Holds | Local variables and links to objects | Object data |
| Speed | Fast (effectively 0 time) | Slow: up to 1500 cycles |
| Size | Tiny | Huge |
| Typing | Literal | Polymorphic |

#### Definitions

> **Run-time polymorphism (late binding)**: The method is chosen at run time through the VMT. It is very flexible but costs up to 1500 cycles per access, and the CPU cannot predict it. This is the only kind Java has.

> **Compile-time polymorphism (early binding)**: The method is chosen at compile time (C++ templates). It is almost as flexible but up to 1000× faster. It is not easy, though it is better in C++23.

### DOD Step 1: Find The Hot Code (Measure)

1. **Split the program into hot and cold code.**
   - **Hot**: always in a loop, executed many times per second; more code or objects makes it slower.
   - **Cold**: executed rarely; more code or objects has no measurable effect.
2. **Unless you are 100% sure, measure** where the bottlenecks are:
   - an **instrumenting profiler**: Java Flight Recorder, VisualVM or Async Profiler for Java; tools on hackingcpp.com for C++; pyinstrument for Python
   - or a **timer**:

```java
start = hiresTimer.microsecs();
// doStuff()
end = hiresTimer.microsecs();
duration += end - start;   // uint64 accumulator
```

In Pacman the sprite-drawing path is hot ("20 000× slower than needed"). The timer, keyboard, board and AI are not hot, so they are not a problem.

### DOD Step 2: Analyse The Data Flow

What happens in the hot loop? For Pacman, 60 times a second the timer fires and the game:

1. finds where the dolls are (Pacman and ghosts)
2. checks collisions between Pacman and ghosts
3. checks collisions between Pacman and pills or walls
4. tries to move each doll one space
5. animates the dolls and draws the grid

The data involved is positions, bitmaps and the grid. With thousands of ghosts, the AI might be pulled in too.

### DOD Step 3: Data That Flows Together Stays Together

This is a creative process. **Arrays are your friend.**

| Language | Guidance |
|---|---|
| Java | Arrays of simple types (`char`, `int`, `float`); fewer objects (`Integer`, `String`, `ObjectX`). Abusing a `String` as an array is OK. Use only **static** methods, passing data as the first parameter or making the data static arrays. |
| C++ | Use `class`, but avoid `virtual`; templates give compile-time polymorphism |
| Python | Lists of simple types; avoid sets and dictionaries |

```java
public class GameBoard {
  // everything static, few Objects
  public static final int PM_id = 0;
  public static final int GCOUNT = 4;
  private static int  position[GCOUNT+1][2];        // 0 = Pacman, 1..4 = ghosts; x,y
  private static char grid[GRID_SX][GRID_SY];
  private static char bitmaps[GCOUNT+1][BITMAP_SIZE];
  private static char doll_state[GCOUNT+1];
  private static int  pillsLeft;
  private static int  PM_PowerUpTimeLeft;
  private static AI   GameAI;                       // access to normal objects
  public static void moveto(int doll_id, int x, int y);
  public static void draw(int doll_id);
}
```

Put dynamic data in another object, not inside the DOD object.

**What is in a Java object?** Mostly links, not much data.

| Directly included | Indirectly linked |
|---|---|
| Simple types (`int`, `double`, …) | Any `Object` |
| Arrays of simple types | Non-static (virtual) code |
| `enum` | |
| Static code | |

This is not very flexible when dolls differ. Two solutions:

- **Tag bits** in Java: `isGhost = dollIdx & 1; dollId = dollIdx >> 1;`
- **Variant objects** in C++ (`std::variant`), which are fully polymorphic without virtual calls

### DOD Speed-Up And Other Benefits

Static methods avoid indirect code lookups:

$$
20 \times 1500 = 30\text{K cycles} \times 5\text{ dolls} = 150\text{K cycles} \;/\; 5\text{ GHz} \approx 30\,\mu\text{s per frame}
$$

More realistically it saves about 300 μs per frame, because of other slowdowns. That is not worth it for Pacman alone, but with many ghosts the frame rate could drop below playable.

In Conway's Game of Life pattern searching:

| Algorithm | Method | Cells/gen/s | Speed-up |
|---|---|---:|---:|
| Naïve counting | Count neighbours for every pixel | $10^4$ | — |
| JavaLife | Lookup table + linked list | $3\cdot10^7$ | 3000× |
| QLife | Lookup table + quad tree | $10^8$ | 3× |
| LifeCube | Half-adder logic | $2\cdot10^9$ | 20× |
| Optimised LifeCube | Low-level assembly + stagger step + 64-ary tree | $10^{10}$ | 5× |
| GPU LifeCube | CUDA on a GPU | $10^{13}$ | 1000× |

Together that is a DOD speed-up of about $10^6\times$, data parallelism of about $10^3\times$, and a total of about $10^9\times$.

| DOD | Traditional OOP |
|---|---|
| Data flow is easy to follow; code and its data flow are in one place | Pacman and ghost code is spread over many objects |
| Sub-methods are still possible; static calls are effectively free | All member data of accessed objects gets pulled in, even if unused |
| The CPU does not pull in unrelated data | More cache eviction |

### CPU Code Flow: Pipelining And Prediction

#### Definitions

> **Pipelining**: Overlapping the stages (fetch, decode, execute, write) of consecutive instructions, so linear code completes one instruction per cycle.

> **Branch prediction / speculative execution**: The CPU guesses a branch's outcome and executes ahead as if the guess were right. It commits if right, and rolls back and refetches if wrong.

![Pipelining](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05B_Data_Oriented_Design/pipeline.svg)

*Linear code keeps the pipeline full. A jump empties it, stalling for the length of the pipeline.*

- **Linear code**: one instruction every cycle.
- **Jump**: the pipeline empties and stalls for `length(pipeline)` cycles.
- **Speculation on code**: a wrong guess means roll back the work, empty the pipeline and fetch the other code.
- **Speculation on data**: a wrong guess may evict the wrong data, force a re-fetch, and leave the CPU waiting for the correct data.

| OOP problem | Effect on the CPU |
|---|---|
| Virtual methods | Essentially random to the CPU; unpredictable; often not in the L1 code cache; costly waits |
| Heap-based objects | Random locations in a chaotic heap; data flow can't be predicted; very costly L1/L2/L3 misses |

### Superscalar And Out-Of-Order Execution

#### Definitions

> **Superscalar execution**: Running independent instructions at the same time, e.g. `a = b + 10;` and `c = d * 11;`.

> **Out-of-order (OoO) execution**: Using a dependency graph to reorder instructions so independent ones can run together.

```c
1: a = b + 10;   // a depends on b
2: a += d;       // must wait for line 1
3: c = d * 11;   // independent of a and b
4: c += b;       // must wait for line 3
```

The CPU reorders this to 1, 3, 2, 4. A 2-way superscalar CPU then executes 1 and 3 together, then 2 and 4.

![Dependency graph](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05B_Data_Oriented_Design/dependency-graph.svg)

*The source example's dependency graph: nodes without a path between them, such as $c$ and $d$, $e$ and $f$, or $i$ and $j$, can execute in parallel.*

### Stack Engine And What The Compiler Can't Do

#### Definitions

> **Stack engine**: Hardware (since Intel P6b, 2003) that simulates the stack in CPU registers, so local variables take zero time to access.

- On older CPUs stack bookkeeping had overhead; on new CPUs all stack work is effectively free.
- C++ objects live on the stack by default. Small-ish objects (under about 8 KB) get zero access time, even with random access.

**Why doesn't the compiler fix this?**

| CPU | Compiler |
|---|---|
| Sees instructions and the current data | Sees only a static picture of the code, never the data |
| Builds a better local dependency graph | Cannot make assumptions without risking subtle bugs, so many "obvious" optimisations are skipped |
| Uses a neural network trained as the program runs | Global dependency tracking is NP-hard |
