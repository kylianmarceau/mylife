---
tags:
  - advanced-programming
---

# Data-Oriented Design

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD05 Data oriented design.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD05%20Data%20oriented%20design.pdf) (identical to [ASD05 Data oriented design - Copy.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD05%20Data%20oriented%20design%20-%20Copy.pdf) apart from slide dates), Johan Bontes, University of Cape Town, pages 1–56
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Why object-oriented code is slow on modern CPUs (memory bandwidth, caches, heap scattering, virtual calls), the three steps of data-oriented design shown on a Pacman example, and how CPU pipelining, prediction, superscalar and out-of-order execution interact with code structure.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Data-Oriented Design Is|What Data-Oriented Design Is]]
  - [[#The Pacman Case Study|The Pacman Case Study]]
  - [[#Why OOP Mapping Is Slow|Why OOP Mapping Is Slow]]
  - [[#Feeding The CPU: Memory Bandwidth|Feeding The CPU: Memory Bandwidth]]
  - [[#The Cache Hierarchy|The Cache Hierarchy]]
  - [[#Cache Rules And Eviction|Cache Rules And Eviction]]
  - [[#Access Patterns: Sequential Versus Random|Access Patterns: Sequential Versus Random]]
  - [[#Anatomy Of An Object And The Heap|Anatomy Of An Object And The Heap]]
  - [[#Object Problem 1: Living On The Heap|Object Problem 1: Living On The Heap]]
  - [[#Object Problem 2: Virtual Methods|Object Problem 2: Virtual Methods]]
  - [[#Why Cache Lines Cause Eviction|Why Cache Lines Cause Eviction]]
  - [[#Stack Versus Heap And Polymorphism|Stack Versus Heap And Polymorphism]]
  - [[#DOD Step 1: Find The Hot Code|DOD Step 1: Find The Hot Code]]
  - [[#DOD Step 2: Analyse The Data Flow|DOD Step 2: Analyse The Data Flow]]
  - [[#DOD Step 3: Data That Flows Together Stays Together|DOD Step 3: Data That Flows Together Stays Together]]
  - [[#DOD Speed-Ups And Benefits|DOD Speed-Ups And Benefits]]
  - [[#CPU Code Flow: Pipelining And Prediction|CPU Code Flow: Pipelining And Prediction]]
  - [[#Superscalar And Out-Of-Order Execution|Superscalar And Out-Of-Order Execution]]
  - [[#The Stack Engine And The Compiler|The Stack Engine And The Compiler]]

---

## Core Content

### What Data-Oriented Design Is

#### Definitions

> **Data-oriented design (DOD)**: A technique for speeding up data processing by organising code around how data flows through the CPU, rather than around real-world objects. It requires thinking like a CPU: what slows it down, and what speeds it up?

**Rule 1: if it ain't broke, don't fix it.**

- DOD is all about data — **lots** of data. No lots of data, no DOD.
- Consider using a database instead.

Where DOD is used — anywhere with lots of uniform data to process, when a database can't be used:

- inside database engines,
- games,
- numerical simulation (number crunching),
- solvers.

Database techniques are moving into game engines (e.g. SpacetimeDB).

### The Pacman Case Study

The lecture compares two Pacman implementations.

![Pacman: OOP versus DOD](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05B_Data_Oriented_Design/pacman-oop-vs-dod.svg)

*The OOP design scatters each doll's data and behaviour across a class hierarchy of heap objects; the DOD design keeps the hot data in a few flat arrays processed by static code.*

- The traditional OOP design is about **20 000× slower than needed** in its hot path.
- Parts of the OOP design that are not "hot" are not a problem.

### Why OOP Mapping Is Slow

Traditional OOP courses say:

- map real-world entities onto objects, and
- solve issues with more objects.

The problems:

| Issue | Consequence |
|---|---|
| The real world is complex, so 1-to-1 mapping creates **blob objects** | Large, unfocused objects |
| "Correct" OOP mapping uses lots of **indirection** | Extra work for the CPU: slow |
| Objects live on the **heap** | Scattered in memory |
| Objects mix **hot and cold** data | Cold data pollutes the cache |
| Objects mix **read-only and read-write** data | Harder to cache and parallelise |

### Feeding The CPU: Memory Bandwidth

A CPU is a **Von Neumann machine**: code and data are fetched from memory into the processor.

A 5 GHz core can process about

$$
5\text{G} \times 32 \times 4 \approx 600\ \text{GiB/s per core}
$$

| Source | Bandwidth | Relative to CPU demand |
|---|---|---|
| CPU core demand | ~600 GiB/s | — |
| DDR5-5600, sequential | ~70 GiB/s | ~10× slower |
| DDR5-5600, random access | ~400 MiB/s | ~1500× slower |
| 8-core CPU demand | $600 \times 8 = 4.8$ TiB/s | — |

Memory cannot keep the CPU fed, especially with random access.

### The Cache Hierarchy

#### Definitions

> **Hot data**: A small amount of data used over and over — lookup tables, a database index, sprite coordinates, local variables on the stack, scratchpads, data inside a loop.

> **Cache**: Small, fast memory close to the CPU that holds the hottest data.

Most time is spent on hot data, so the hottest data is kept closest to the CPU (figures for AMD Zen 5):

| Level | Size | Bandwidth |
|---|---|---|
| "L0": register file + micro-op cache | 16 KiB / ~24 KiB | ~600 GiB/s |
| L1 data / L1 code | 48 KiB / 32 KiB | ~200 GiB/s |
| L2 (per core, data + code) | 1 MiB | ~20 GiB/s |
| L3 (shared) | 32 MiB | ~2 GiB/s |
| RAM (shared) | Big | ~0.4 GiB/s (best case, random) |

![Cache hierarchy](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05B_Data_Oriented_Design/cache-hierarchy.svg)

*Each level is larger and slower than the one above; the CPU only works on what reaches the register file and micro-op cache.*

The CPU has a small "notepad" for data — the register file, about 500 variables — and a small "screen" for code — about 6000 micro-ops.

### Cache Rules And Eviction

**The CPU cannot use RAM directly.**

- Data can be used only once it is in the register file; code only once it is in the micro-op cache.
- New data in means old data out.
- Data moves in and out of the CPU via L1, into L1 via L2, into L2 via L3.
- The closer to the CPU, the hotter the data. More re-used and more recent data is hotter.

#### Definitions

> **Eviction scheme**: The rule for which cached data to discard when new data arrives.

| Era | Scheme |
|---|---|
| 2000s | **LRU** — least recently used (delete the oldest) |
| 2010s | **LFU** — least frequently used (delete the coldest) |
| Modern | A tiny neural network mixing LRU and LFU |

Modern CPUs also **predict** which data and code will be needed next and fetch it speculatively (**speculative prefetching**, which has security implications). Tip: make your data use **predictable**.

### Access Patterns: Sequential Versus Random

```java
final int GB = 1024 * 1024 * 1024;
int[] array = new int[1 * GB];

// A: sequential
for (var a : array) {
    doStuff(a);
}

// B: random
var r = new Random();
for (var i = 0; i < GB; i++) {
    var i2 = r.nextInt(GB);
    var a = array[i2];
    doStuff(a);
}
```

Sequential access lets the prefetcher stream data; random access pays the full RAM latency on almost every read.

Java objects add a twist:

```java
int[]     array  = new int[1 * GB];      // 4 GiB
Integer[] array2 = new Integer[1 * GB];  // ~48 GiB after initialisation
for (var a : array2) {                   // effectively random access!
    doStuff(a);
}
```

- `Integer[]` holds **pointers**; every `Integer` is a separate heap object with a header and padding, which is why it balloons to about 48 GiB.
- Looping over it is effectively random access, because each element must be fetched from wherever its object landed on the heap.

### Anatomy Of An Object And The Heap

```java
ObjectX a;          // local variable: on the stack (always in L1)
a = new ObjectX();  // the ObjectX itself is created on the heap
```

- The local variable `a` is a **link (pointer)** of 8 bytes to the heap object.
- The heap is the object store in main memory.
- An object is data plus code:

```text
ObjectX = struct {
    VMT:     'this' pointer to the virtual method table (list of code)
    Data:    data members
    padding: empty space to make the size a multiple of 8 bytes
}
```

#### Definitions

> **Heap**: The memory area for dynamically allocated objects. It has four lists (tiny, small, medium and large objects); allocation is first come, first served, and destruction happens at random times (garbage collection).

> **Virtual method table (VMT)**: A per-class table of pointers to the class's (overridable) methods, reached through a pointer in each object.

Because objects are allocated in arrival order and freed at random times, they end up **randomly distributed** through memory. Heap bookkeeping also takes space.

### Object Problem 1: Living On The Heap

- An object's data and code are spread randomly over memory.
- Related objects are not stored sequentially, and the longer the program runs, the more randomly spaced they become.
- This adds about a **1500-cycle start-up penalty** to each object access — time in which the core could have performed about 6000 calculations.
- Delays are much worse in multi-threaded code.

### Object Problem 2: Virtual Methods

```java
Sprite[] dolls = new Sprite[5];
for (var i = 1; i <= 4; i++) { dolls[i] = new Ghost(); }
dolls[0] = new Pacman();
// ... game loop
dolls[i].moveto(x, y);
```

1. Look up the correct doll on the heap.
2. `moveto = doll.VMT[42]` — a pointer to code.
3. Call `moveto` — the call **cannot be predicted**: it might be a ghost, Pacman or a zombie, which all move differently.

A deeper chain:

```java
public void Ghost.draw() {
    bitmap = getScaryBitmap();
    super.draw();
}
public void MovingSprite.draw() {
    location = point(x, y);
    super.draw();
}
public void Sprite.draw() {
    display.draw(bitmap, location);
}
```

`dolls[i].draw()` then performs:

1. Look up the doll on the heap.
2. `draw = doll.VMT[41]`; call `Ghost.draw()` (unpredictable).
3. `parent = doll.VMT[0]`; `draw = parent.VMT[41]`; call `MovingSprite.draw()` (maybe predicted).
4. `grandparent = parent.VMT[0]`; `draw = grandparent.VMT[41]`; call `Sprite.draw()` (maybe predicted).
5. Look up the `display` object on the heap; `draw = display.VMT[125]`; call `Display.draw(bitmap, location)` (maybe predicted).
6. Look up the `bitmap` object on the heap.

![Virtual call chain](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05B_Data_Oriented_Design/virtual-dispatch.svg)

*One `draw()` call chases pointers through several objects and VMTs, each a potential cache miss.*

Every lookup can evict useful data from L1 (**data cache eviction**, problem 2a), and every indirect call can evict code from the L1 code / micro-op cache (**code cache eviction**, problem 2b).

### Why Cache Lines Cause Eviction

- The minimum load size for data is 32 bytes on AMD/Intel. Even if you ask for 1 byte, 32 bytes are fetched, so 32 bytes of other data are evicted.
- Why? The hardware can fetch 256 bits in parallel, 32× faster than one byte at a time.
- Every CPU speed hack has a drawback elsewhere.

### Stack Versus Heap And Polymorphism

In Java, everything created with `new` lives on the heap, giving layers of indirection:

1. `ClassX myobject = new ClassX();` — `myobject` is a link to heap data.
2. All non-static methods are accessed indirectly (through the VMT).
3. Object fields such as `Bear bear;` are links to further heap objects.

| | Stack | Heap |
|---|---|---|
| Access | Direct | Indirect |
| Contents | Local variables and links to objects | Object data |
| Speed | Fast (effectively 0 time) | Slow: up to 1500 cycles |
| Size | Tiny | Huge |
| Typing | Literal | Polymorphic |

#### Definitions

> **Run-time polymorphism (late binding)**: The method called is chosen at run time via the VMT. Very flexible, but up to 1500 cycles per access, and the CPU can't predict it.

> **Compile-time polymorphism (early binding)**: The method called is fixed at compile time (e.g. C++ templates). Almost as flexible, but up to 1000× faster; not easy to use (better in C++23).

Java only has run-time polymorphism; C++ has both.

### DOD Step 1: Find The Hot Code

Split the program into hot and cold code:

| | Hot code | Cold code |
|---|---|---|
| Where | Always in a loop | Rarely executed |
| Frequency | Many times per second | Occasionally |
| Effect of more code/objects | Slower program | No measurable effect |

Unless you are 100% sure, **measure** where the bottlenecks are:

- **Instrumenting profilers** — Java: Java Flight Recorder, VisualVM, Async Profiler; C++: various (hackingcpp.com lists them); Python: pyinstrument.
- A simple **timer**:

```text
start = hiresTimer.microsecs();
// dostuff()
end = hiresTimer.microsecs();
duration: uint64 += end - start;
```

### DOD Step 2: Analyse The Data Flow

Pacman's hot loop runs on a timer 60 times per second:

1. Find where the dolls (Pacman and ghosts) are.
2. Check collisions between Pacman and ghosts.
3. Check collisions between Pacman and pills/walls.
4. Try to move the dolls one space.
5. Animate the dolls and draw the grid.

The data involved: positions, bitmaps and the grid. With thousands of ghosts, you might pull the AI into the hot path too.

### DOD Step 3: Data That Flows Together Stays Together

This is a creative process.

- **Arrays are your friend.** In Java use arrays of simple types (`char`, `int`, `float`) and fewer objects (`Integer`, `String`, `ObjectX`). Abusing a `String` as an array (as in the Pacman demo) is fine.
- **Use only static methods**: pass the data as the first parameter, or make the data static (arrays of stuff).
- **C++**: use classes but avoid `virtual`; templates give compile-time polymorphism.
- **Python**: use lists of simple types; avoid sets and dictionaries.

```java
public class GameBoard {
    // everything static, few Objects
    public static final int PM_id = 0;
    public static final int GCOUNT = 4;
    private static int  position[GCOUNT+1][2];       // 0 = Pacman, 1..4 = ghosts; x,y
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

**What's in a Java object?** Mostly links, not much data.

| Directly included | Indirectly linked |
|---|---|
| Simple types (`int`, `double`, …) | Any `Object` |
| Arrays of simple types | Non-static (virtual) code |
| `enum` | |
| Static code | |

This isn't very flexible when different dolls behave differently. Solutions:

| Language | Technique |
|---|---|
| C++ | Variant objects: `class Doll { boolean isGhost; /* data */ }`, or `std::variant` (fully polymorphic) |
| Java | Tag bits in an index: `isGhost = dollIdx & 1; dollId = dollIdx >> 1;` |

### DOD Speed-Ups And Benefits

Static methods avoid indirect code lookup:

$$
20 \times 1500 = 30\text{K cycles} \times 5 \text{ dolls} = 150\text{K cycles}, \qquad \frac{150\text{K}}{5\text{ GHz}} \approx 30\ \mu\text{s per frame}
$$

In practice more like ~300 µs per frame because of other slowdowns. That's not worth it for Pacman as such, but with many ghosts the frame rate could drop below playable.

| Technique | Speed-up |
|---|---|
| DOD | up to 1 000 000× |
| Data parallelism | 1 000× |
| Combined | up to 1 000 000 000× |

Other benefits:

- Data flow is much easier to follow; code and its data flow are in one place.
- You can still use sub-methods; static calls are effectively free.
- The CPU doesn't pull in unrelated data.

With traditional OOP, Pacman/ghost code is spread over many objects, and all member data of every accessed object is pulled in even if never used, causing more cache eviction.

### CPU Code Flow: Pipelining And Prediction

#### Definitions

> **Pipelining**: Overlapping the stages (fetch, decode, execute, …) of successive instructions, so linear code completes one instruction every cycle.

> **Branch prediction**: The CPU guesses which way a branch goes and speculatively fetches and executes code as if the guess were right.

![Pipelining](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05B_Data_Oriented_Design/pipeline.svg)

*Linear code keeps the pipeline full; a jump to unpredicted code empties it and stalls for the pipeline's length.*

| Code shape | Effect |
|---|---|
| Linear | One instruction per cycle |
| Jump (mispredicted) | Pipeline empties; stall for length(pipeline) cycles |

Speculation:

- **Correct guess**: commit the work.
- **Wrong guess**: roll back, empty the pipeline, fetch the other code.
- The CPU also prefetches data speculatively. If wrong, it may evict the wrong data, have to re-fetch evicted data, and wait for the correct data.

OOP is a poor fit:

| OOP feature | CPU effect |
|---|---|
| Virtual methods | Essentially random to the CPU; can't be predicted; often not in L1 code cache; costly waits |
| Heap-based objects | Chaotic random locations; the CPU can't predict data flow; very costly L1/L2/L3 misses |

### Superscalar And Out-Of-Order Execution

#### Definitions

> **Superscalar execution**: The CPU executes independent instructions at the same time.

> **Out-of-order (OoO) execution**: The CPU analyses code with a dependency graph and reorders independent instructions to keep execution units busy.

```c
a = b + 10;   // a depends on b
c = d * 11;   // c depends on d, not on a or b
```

These two lines can run at the same time (superscalar), though both use the same pipeline.

Out-of-order example:

```c
1: a = b + 10;  // depends on b
2: a += d;      // must wait for line 1
3: c = d * 11;  // depends on d only
4: c += b;      // must wait for line 3
```

The CPU reorders this to 1, 3, 2, 4. A 2-way superscalar CPU executes 1+3 together, then 2+4.

![Dependency graph](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05B_Data_Oriented_Design/dependency-graph.svg)

*Lines 1 and 3 are independent and can run together; lines 2 and 4 each wait for their own predecessor.*

### The Stack Engine And The Compiler

**Stack engine** (since Intel P6b, 2003): modern CPUs simulate the stack in CPU registers.

| | Old CPUs | New CPUs |
|---|---|---|
| Stack bookkeeping | Has overhead | Takes zero time |
| Local variables | Some cost | Zero access time |

C++ objects live on the stack by default; for smallish objects (< 8 KB) access takes zero time, even random access.

**What about the compiler?**

| CPU | Compiler |
|---|---|
| Sees instructions **and** current data | Sees only a static picture of the code |
| Builds a better local dependency graph | Can't make assumptions, or subtle bugs would appear |
| Uses a neural network for prediction, trained as the program runs | Skips many seemingly obvious optimisations |
| Knows things the compiler cannot | Can't see data; global dependency tracking is NP-hard |
