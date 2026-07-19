# Processes

**Subject**: CSC3002F Operating Systems  
**Source**: `CSC3002F_MK_1_ProcessConcept.pdf`, Michelle Kuttel, pages 1-67  
**Generated**: 2026-06-03

---

## Core Content

### Programs, Processes, Threads, And The Kernel

#### Definitions

> **Program**: A passive set of instructions stored on disk.

> **Process**: A program in execution, with resources and protection.

> **Thread**: A single path of execution within a process.

> **Kernel**: The core OS component that manages resource access, memory, and process scheduling.

> **System Program**: A program used by the OS but not necessarily part of the kernel.

> **Application Program**: A program not associated with OS operation.

The source's key distinction is:

| Concept | Definition | Own Address Space? | Own Execution State? | Example |
|---|---|---:|---:|---|
| Program | Passive instructions on disk | No | No | `python`, `chrome`, `ls` |
| Process | Program in execution with resources/protection | Yes | Yes | One running Chrome instance |
| Thread | One execution path inside a process | No, shared with same-process threads | Yes | One worker thread inside Chrome |

Threads in the same process share code, heap, global data, and open files. Each thread has its own program counter, registers, and stack.

A modern OS has many processes executing concurrently: kernel/OS processes and user processes. The OS manages process creation, scheduling, termination, and inter-process communication. Web browsers such as Chrome use process-like isolation: one browser process plus many sandboxed content/helper processes, so a tab crash or malicious script is contained better than in a single-process design.



### Process Trees, PIDs, Boot, And Daemons

#### Definitions

> **Process Identifier (PID)**: A unique number used by the OS to identify a process.

> **Parent Process**: A process that creates another process.

> **Child Process**: A process created by a parent.

> **Process Tree**: The parent-child hierarchy of processes.

> **systemd**: The Linux process that is parent/adopter for system processes and usually has PID $1$.

> **launchd**: macOS's PID $1$ style system launcher.

> **Daemon**: A background process that runs without user intervention.

Processes spawn other processes and form a tree. Linux commands for inspecting this include:

| Command | Use |
|---|---|
| `ps -A --forest` | Show processes as a forest/tree |
| `ps -aef` | Show all processes with parent PIDs |
| `pstree` | Show process hierarchy |
| `cat /proc/sys/kernel/pid_max` | Show Linux maximum PID |

During boot:

1. A tiny bootstrap loader starts from firmware/NVM at a fixed location.
2. It initializes basic hardware such as CPU registers, device controllers, and memory.
3. It loads a fuller bootstrap program from boot blocks on a boot/system disk.
4. The full bootstrap program loads the kernel from secondary storage.
5. The kernel mounts the root filesystem and launches the first process, such as `systemd`.
6. That first process launches daemons on behalf of the system or users.

Example daemons:

| Daemon | Purpose |
|---|---|
| `sshd` | Secure remote shell access |
| `httpd` / Apache | Serve web pages and HTTP requests |
| `rsyslogd` | Collect/process/forward system logs |
| `cron` | Run scheduled periodic tasks |

PID allocation is OS-dependent. Linux exposes a maximum through `/proc/sys/kernel/pid_max`; macOS commonly has maximum PID $99998$; Windows has no fixed maximum in the same way and is constrained by word/system limits. PIDs are often allocated sequentially and wrap around, skipping still-used PIDs. Some systems randomize PIDs for security at some performance cost.



### Process Memory Layout And Execution Context

#### Definitions

> **Execution Context**: The state needed to resume a process, including program counter, registers, memory map, and resources.

> **Text Segment**: Compiled program code in memory.

> **Stack**: Memory for function parameters, return addresses, local variables, and temporary data.

> **Heap**: Memory dynamically allocated during runtime.

> **Stack Overflow**: Failure caused when the call stack exceeds its bound.

> **Heap Exhaustion**: Failure caused when dynamic allocation cannot obtain more heap memory.

A process is a program plus execution context. In memory it contains:

| Region / State | Contents |
|---|---|
| Text | Compiled code |
| Current state | Program counter and CPU registers |
| Stack | Function parameters, return addresses, temporary/local data |
| Data | Initialized static and global variables |
| Heap | Dynamically allocated memory |

Stack properties:

- Automatically managed by the system.
- Local variables are deallocated when they go out of scope.
- Usually limited in size and fast to access.
- Lifetime tied to variable scope.
- Deep/infinite recursion can cause stack overflow.

Heap properties:

- Used for dynamic memory allocation.
- Managed manually in C/C++ with `malloc/free` or `new/delete`; garbage collected in Java.
- Usually larger but slower.
- Lifetime independent of variable scope.
- Too many or too-large allocations can cause `OutOfMemoryError` or allocation failure.

Creating many threads can exhaust memory because each thread needs its own execution state and stack.



### Process Control Blocks

#### Definitions

> **Process Table**: OS-maintained list/table of active process records.

> **Process Control Block (PCB)**: Kernel data structure representing one process.

> **Process Group**: A group of related processes that can be signalled together.

Each PCB stores information the kernel needs:

| PCB Field | Purpose |
|---|---|
| Process state | Running, waiting, ready, etc. |
| Program counter | Next instruction location |
| CPU registers | Saved register values |
| CPU scheduling information | Priority and queue pointers |
| Memory-management information | Allocated memory/address-space details |
| Accounting information | CPU used, elapsed time, time limits |
| I/O status information | Allocated devices and open files |

In multithreaded OSes, per-process state and per-thread state are separated. Threads share address space/resources, but each thread has its own execution context. Linux implements the PCB as `task_struct`; Darwin/macOS has analogous structures such as `task`.
### Process Creation With `fork()`

#### Definitions

> **fork()**: UNIX system call that creates a new process by duplicating the calling process.

> **Copy-On-Write**: Optimization where parent and child initially share physical memory pages until one writes.

> **Ready Queue**: Queue of processes in memory that are ready to execute.

`fork()` creates a new PCB, initializes kernel resources from the parent, gives the child a new PID, initializes its program counter to the same point, creates a new address space initially copied from the parent, and places the child PCB on the ready queue.

`fork()` "returns twice":

| In Which Process? | Return Value |
|---|---|
| Parent | Child's PID |
| Child | $0$ |
| Error | $-1$ |

After ```fork()```:

- Parent and child have the same code after the fork.
- They have different return values from `fork()`.
- They have different PIDs.
- They usually share open files unless changed.
- Their address spaces are logically separate, often implemented with copy-on-write.
- They run concurrently in unspecified order.

If a program calls `fork()` twice without conditional control, the number of processes can double each time. With $k$ unconditional forks:

$$
\text{number of processes}=2^k
$$
### Program Replacement With `exec()`

#### Definitions

> **exec()**: UNIX system call family that replaces the current process's memory image with a new program.

> **Program Image**: The loaded memory representation of a program.

`exec()` is commonly used after `fork()`:

1. Parent calls `fork()`.
2. Child receives return value $0$.
3. Child calls `exec()` to replace itself with another program.
4. Parent may call `waitpid()` to wait for the child.

Important: `exec()` does not create a process. It wipes the calling process's old program image and loads a new one. The PID stays the same.

UNIX separates creation and program loading (`fork()` then `exec()`). Windows typically combines both in `CreateProcess`.
### Running Processes, States, Context Switches, And Queues

#### Definitions

> **New/Created State**: The process is being created.

> **Running State**: The process's instructions are executing on a processor.

> **Waiting State**: The process waits for an event such as I/O completion.

> **Ready State**: The process is in memory and waiting for a processor.

> **Terminated State**: The process has finished execution.

> **Context Switch**: Saving one process's context and loading another's.

Only one process can run on a given processor at any instant. A process moves among new, ready, running, waiting, and terminated states as it executes.

Context switch steps:

*1*. Save current process state into its PCB.
*2*. Decide which process should run next.
*3*. Load the new process state from its PCB.

Context switching is overhead: the system does no direct user work while switching. Typical speed is several microseconds, depending on hardware support and PCB complexity.

Queues:

| Queue | Contents |
|---|---|
| Job queue | All processes in the system |
| Ready queue | Processes in main memory, ready and waiting to execute |
| Device queue | Processes waiting for a particular I/O device |

Queueing diagrams use circles for resources, arrows for flow, and queues for waiting processes.



### Mobile OS Process Management

#### Definitions

> **Foreground App**: The app directly interacting with the user.

> **Background Service**: Work performed without a user interface, especially on Android.

Mobile systems require sophisticated resource management, multitasking, security, and failure isolation.

| System | Background Policy | Strength |
|---|---|---|
| iOS | Strongly restricts background execution; limited categories such as audio, VoIP, location | Battery life, predictable performance, security |
| Android | More flexible background work through services | Customizability and flexibility |
### Inter-Process Communication

#### Definitions

> **Independent Process**: A process that does not share data with other processes.

> **Cooperating Process**: A process that communicates with other processes.

> **Inter-Process Communication (IPC)**: OS-supported communication between processes.

> **Shared Memory**: IPC where processes read/write a shared memory region.

> **Pipe**: A unidirectional transient data channel between two processes.

> **Message Passing**: IPC where processes explicitly send and receive messages.

> **Socket**: Endpoint for bidirectional communication on the same machine or across a network.

> **Remote Procedure Call (RPC)**: Calling a function in another process/machine as if it were local.

Reasons for cooperation include information sharing, computation speedup through parallelization, and modularity.

| IPC Model | Strength | Caution |
|---|---|---|
| Shared memory | Fast | Requires synchronization |
| Pipes | Simple one-way process connection, common in shell pipelines | Usually transient/unidirectional |
| Message passing | Isolation-friendly and can be sync/async | More OS/channel overhead |
| Sockets | Same-machine or network communication, client-server systems | Requires addressing/port management |
| RPC | Makes remote communication look local | Failures/latency still exist despite local-looking call |

Example shell pipeline:

```sh
cat file1.txt | sort
```

Here `cat` writes to one end of a pipe and `sort` reads from the other.
### Process Termination, Orphans, And Zombies

#### Definitions

> **Normal Exit**: Process termination after executing its last statement or calling `exit()`.

> **Abnormal Termination**: Process termination due to error, exception, signal, or forced stop.

> **Orphan Process**: A child process whose parent terminates first.

> **Zombie Process**: A child process that has terminated but whose parent has not yet collected its exit status.

> **Reaping**: Collecting a terminated child's exit status and allowing its PCB/PID entry to be removed.

When a process exits, its resources such as memory, open files, and I/O buffers are deallocated and reclaimed. However, a terminated child is not fully removed until its parent or adopting process reaps it with `wait()` or `waitpid()`.

The OS keeps zombies so that:

1. The parent can still obtain the child's exit status.
2. The child's PID is not reused before the parent waits.
3. The parent does not accidentally wait for a different process with a recycled PID.

A parent may terminate a child because the child exceeded resources, the assigned task is no longer needed, or the parent is exiting and the OS does not allow the child to continue.

## Worked Examples

### Example 1: How Many Processes After Two `fork()` Calls?

**Problem**: A program executes two unconditional `fork()` calls. How many total processes exist after them?

**Step 1**: Initially there is $1$ process.  
**Step 2**: After first `fork()`, each existing process creates one child:

$$
1\times2=2
$$

**Step 3**: After second `fork()`, both existing processes fork:

$$
2\times2=4
$$

**Answer**: $4$ processes total.

### Example 2: Interpret `fork()` Return Values

**Problem**: `pid_t pid = fork();` returns `3472` in one execution path and `0` in another. Which is parent and which is child?

**Step 1**: Parent receives the child's PID.  
**Step 2**: Child receives $0$.  
**Answer**: The path where `pid == 3472` is the parent. The path where `pid == 0` is the child.

### Example 3: Why Zombies Exist

**Problem**: A child exits before its parent calls `waitpid(pid, &status, 0)`. Why does the OS keep a zombie entry?

**Step 1**: The parent may later request the child's exit status.  
**Step 2**: If the PID were immediately reused, the parent might wait on the wrong process.  
**Step 3**: The zombie PCB preserves termination information and prevents PID reuse until reaped.  
**Answer**: Zombies preserve correct parent-child termination semantics.

### Example 4: Draw A Process Tree From PPIDs

**Problem**: Given `PID 179773 PPID 1` and `PID 179774 PPID 179773`, what is the relationship?

**Step 1**: A PPID of $1$ means `179773` is a child of PID $1$.  
**Step 2**: `179774` has parent `179773`.  
**Answer**:

```text
1
└── 179773
    └── 179774
```

---

## Common Mistakes / Gotchas

- Saying `exec()` creates a new process. It does not; it replaces the current process image.
- Assuming parent and child run in a predictable order after `fork()`. They run concurrently in unspecified order.
- Forgetting that a thread has its own stack/registers/program counter even though it shares the process address space.
- Thinking a zombie is still running. It has already terminated; only its process-table entry remains.
- Assuming all background work is equally permitted on iOS and Android. iOS is much more restrictive.
- Treating shared memory as automatically safe. It is fast but needs synchronization.

---

## Summary / Cheat Sheet

| Term | Meaning |
|---|---|
| Program | Passive instructions on disk |
| Process | Program in execution with resources/protection |
| Thread | Execution path within process |
| PID | Unique process identifier |
| PCB | Kernel process record |
| `fork()` | Creates a child process; returns twice |
| `exec()` | Replaces current process image |
| Context switch | Save current PCB state, load another |
| IPC | Communication between processes |
| Zombie | Terminated child not yet reaped |
| Orphan | Child whose parent terminated first |

**Key Formulas**:

$$
\text{processes after }k\text{ unconditional forks}=2^k
$$

$$
\text{process memory}=\text{text}+\text{data}+\text{heap}+\text{stack}+\text{execution context}
$$

**Key Takeaways**:

- A process is dynamic: code plus execution context plus protected resources.
- The PCB is central because it stores what the kernel needs to stop and resume execution.
- UNIX process creation separates duplication (`fork`) from program replacement (`exec`).
- Context switching is necessary but pure overhead.
- IPC choices trade speed, isolation, and synchronization complexity.
- Termination is not complete until children are reaped.

---

## Practice Questions

**Q1**: Distinguish a program, process, and thread.  
> Answer: A program is passive code on disk. A process is a running program with its own address space/resources/execution state. A thread is a single execution path inside a process, sharing the process address space but with its own stack/registers/program counter.

**Q2**: What are the three possible outcomes of `fork()`'s return value?  
> Answer: Parent receives the child's PID, child receives $0$, and error returns $-1$.

**Q3**: Why is context switching considered overhead?  
> Answer: During a context switch, the kernel saves/restores state and chooses another process, but no user-level work is being directly completed.

**Q4**: Compare shared memory and message passing.  
> Answer: Shared memory is fast because processes communicate by reading/writing a common region, but it needs synchronization. Message passing keeps processes isolated and communicates through send/receive operations, but has more OS/channel overhead.
