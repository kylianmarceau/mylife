# Operating System Services And Structures

**Subject**: CSC3002F Operating Systems  
**Source**: `Operating Systems 1 Ch2.pdf`, Aslam Safla, pages 1-52  
**Generated**: 2026-06-03

---

## Core Content

### Operating-System Services

#### Definitions

> **Operating-System Service**: A function the OS provides to users, programs, or the system itself.

> **User Interface (UI)**: The way users interact with the OS.

> **Resource Allocation**: Assigning CPU cycles, memory, storage, and I/O devices among competing jobs/users.

> **Accounting**: Tracking resource use by users and jobs.

OS services fall into two broad groups:

| Service Group | Services | Purpose |
|---|---|---|
| Helpful to users/programs | UI, program execution, I/O operations, file-system manipulation, communications, error detection | Make programs usable and reliable |
| Efficient system operation | Resource allocation, accounting, protection and security | Make sharing safe, fair, and efficient |

Programs need OS services to load into memory, start execution, end normally or abnormally, perform I/O, manipulate files/directories, communicate with other processes, and receive error handling. The OS also detects CPU, memory, I/O-device, and program errors and takes appropriate action.




### User Interfaces

#### Definitions

> **Command-Line Interface (CLI)**: A UI where commands are typed directly to a command interpreter.

> **Shell**: A command interpreter, sometimes built into the kernel but usually a system program.

> **Graphical User Interface (GUI)**: A UI based on windows, icons, menus, mouse/keyboard, and visual objects.

> **Touchscreen Interface**: A UI based on gestures, touch selection, virtual keyboard, and sometimes voice.

A CLI fetches commands from the user and executes them. Some commands are built into the shell; others are simply names of programs. If commands are external programs, adding features does not require changing the shell itself.

GUIs use a desktop metaphor where icons represent files, programs, and actions. Many systems provide both CLI and GUI: Windows has a GUI with command shells; macOS has the Aqua GUI over a UNIX-like kernel and shells; UNIX/Linux systems often use CLI plus optional GUIs.
### System Calls, APIs, And Parameter Passing

#### Definitions

> **System Call**: The programming interface to OS services.

> **Application Programming Interface (API)**: A higher-level interface used by programs, often hiding direct system-call details.

> **System-Call Interface**: The OS layer that maps system-call numbers to kernel routines.

> **Runtime Support Library**: Compiler-provided library code that helps implement APIs and system calls.

Programs usually call APIs rather than raw system calls. Common APIs include Win32 for Windows, POSIX for UNIX/Linux/macOS-like systems, and the Java API for the JVM.

System-call implementation normally works as follows:

1. Each system call has an associated number.
2. The system-call interface stores a table indexed by these numbers.
3. A program calls an API/library wrapper.
4. The wrapper places the system-call number and parameters where the OS expects them.
5. A trap/system-call instruction enters the kernel.
6. The system-call interface invokes the intended kernel routine.
7. The kernel returns status and values to the caller.

Parameter-passing methods:

| Method | How It Works | Strength |
|---|---|---|
| Registers | Parameters placed directly in CPU registers | Fast and simple for small fixed parameter sets |
| Memory block/table | Parameters stored in memory; address passed in a register | Handles many/large parameters; used by Linux/Solaris style systems |
| Stack | Parameters pushed by program and popped by OS | Not limited by register count |



### Types Of System Calls

#### Definitions

> **Process Control Call**: A system call that creates, terminates, loads, executes, waits, signals, or changes process attributes.

> **File Management Call**: A system call for creating, deleting, opening, closing, reading, writing, repositioning, or changing file attributes.

> **Device Management Call**: A system call that requests, releases, reads, writes, or configures devices.

> **Message Passing**: A communication model where processes send and receive messages through the OS.

> **Shared Memory**: A communication model where processes access a common memory region.

| Category | Examples |
|---|---|
| Process control | create/terminate, load/execute, wait event, signal event, allocate/free memory, dump memory, debugger support, locks |
| File management | create/delete, open/close, read/write/reposition, get/set attributes |
| Device management | request/release device, read/write/reposition, get/set attributes, attach/detach |
| Information maintenance | get/set time/date, get/set system data, get/set attributes |
| Communications | create/delete connection, send/receive, shared-memory access, transfer status, remote attach/detach |
| Protection | control resource access, get/set permissions, allow/deny user access |

The standard C `printf()` example illustrates layering: a user program calls `printf()`, the C library formats output, and eventually a `write()` system call transfers bytes to the OS.
### Examples: MS-DOS And FreeBSD

#### Definitions

> **Single-Tasking System**: A system that runs one main user program at a time.

> **Multitasking System**: A system that can run multiple processes concurrently.

> **Fork**: A UNIX-style system call that creates a new process.

> **Exec**: A UNIX-style system call that loads a new program into a process.

MS-DOS was single-tasking. At startup, the shell was loaded. Running a program loaded it into memory, overwriting much of the shell except the kernel. When the program exited, the shell reloaded.

FreeBSD is multitasking. A user logs in and chooses a shell. The shell uses `fork()` to create a child process, `exec()` to load the requested program into that child, and then either waits for termination or continues accepting commands. Exit code `0` indicates no error; positive codes indicate errors.
### System Programs

#### Definitions

> **System Program**: A program that provides a convenient environment for program development and execution.

> **Background Service / Daemon**: A long-running user-context process started at boot to provide system facilities.

Most users experience the OS through system programs, not raw system calls.

| System Program Type | Examples |
|---|---|
| File management | Create, delete, copy, rename, print, list files/directories |
| Status information | Date, time, free memory, disk space, users, performance/logging/debugging |
| File modification | Text editors, search commands, text transformation tools |
| Programming support | Compilers, assemblers, debuggers, interpreters |
| Program loading/execution | Loaders, linkage editors, overlay loaders, debugging systems |
| Communications | Remote login, file transfer, email, web browsing, messaging |
| Background services | Disk checking, scheduling, error logging, printing |
| Application programs | User-run programs not considered part of the OS |
### OS Design, Implementation, And Policy/Mechanism

#### Definitions

> **Policy**: The decision about what will be done.

> **Mechanism**: The implementation of how something is done.

> **SYSGEN**: System generation/configuration that builds or tunes an OS for a particular hardware configuration.

OS design starts by defining goals and specifications. User goals emphasize convenience, ease of learning, reliability, safety, and speed. System goals emphasize ease of design, implementation, maintenance, flexibility, reliability, correctness, and efficiency.

Separating policy from mechanism increases flexibility. Example: a timer interrupt mechanism can support many scheduling policies. If the scheduling policy changes, the low-level timer mechanism does not have to change.

OS implementation has evolved from assembly language to C/C++ and mixed-language systems. Low-level parts may still use assembly, the main kernel often uses C, and system programs use C, C++, shell scripts, Perl, Python, and similar languages. Higher-level languages improve portability but can cost performance.
### Operating-System Structures

#### Definitions

> **Monolithic Kernel**: A kernel structure where many OS services run in one large kernel address space.

> **Layered Structure**: An OS structure where each layer uses only lower-level services.

> **Microkernel**: A kernel structure that moves as much functionality as possible into user space and keeps the kernel small.

> **Loadable Kernel Module**: A kernel component that can be loaded as needed through known interfaces.

> **Hybrid System**: An OS structure combining multiple design approaches.

| Structure | Main Idea | Strength | Weakness |
|---|---|---|---|
| Simple/MS-DOS | Minimal separation between modules | Small and direct | Weak interfaces and protection boundaries |
| Traditional UNIX | System programs plus a large kernel below system-call interface | Powerful and practical | Many functions in one kernel level |
| Layered | Each layer uses lower layers | Modularity and abstraction | Hard to define efficient layers |
| Microkernel | Move services to user space; communicate by message passing | Easier extension, portability, reliability, security | User/kernel communication overhead |
| Modules | Core components separate and dynamically loadable | Flexible, modern, efficient | Still requires careful kernel interfaces |
| Hybrid | Combine approaches | Matches real performance/security/usability needs | Harder to classify and reason about |

Linux and Solaris are largely monolithic but modular. Windows is mostly monolithic with microkernel-like subsystem ideas. macOS is hybrid: Aqua UI, Cocoa environment, Darwin/XNU kernel, Mach microkernel components, BSD UNIX parts, I/O Kit, and loadable kernel extensions.



### Mobile OS Structures: iOS And Android

#### Definitions

> **iOS**: Apple's mobile OS for iPhone and iPad, structured from macOS ideas but adapted for mobile.

> **Android**: An open-source mobile OS based on a modified Linux kernel and Java-oriented application stack.

iOS is structured on macOS but does not run macOS applications natively and runs on different CPU architectures. It includes Cocoa Touch for app development, media services for graphics/audio/video, core services such as cloud and databases, and a core OS based on the macOS kernel.

Android is based on a modified Linux kernel that provides process, memory, device-driver, and power management. It adds libraries such as WebKit, SQLite, multimedia support, and a smaller libc. Apps are developed with Java and Android APIs; Java class files are compiled to bytecode and run in the Android runtime environment.



### Debugging, Performance Tuning, And Boot

#### Definitions

> **Debugging**: Finding and fixing errors.

> **Core Dump**: A file capturing a failed process's memory.

> **Crash Dump**: A file capturing kernel memory after an OS failure.

> **Tracing**: Recording system activities for later analysis.

> **Profiling**: Periodically sampling execution to find performance trends.

> **Bootstrap Loader**: Small code that locates the kernel, loads it into memory, and starts it.

OS debugging uses log files, core dumps, crash dumps, traces, and profiling. Performance tuning removes bottlenecks and requires tools that display system behavior, such as `top` or Windows Task Manager. DTrace is an example of live instrumentation, where probes fire when code executes and state data is sent to consumers.

System boot begins at a fixed memory location when power is initialized. Firmware ROM holds initial boot code. A bootstrap loader in ROM/EEPROM or a boot block locates the kernel, loads it, and starts it. GRUB is a common bootstrap loader that can select among kernels, disks, versions, and boot options.

## Worked Examples

### Example 1: Copying One File To Another With System Calls

**Problem**: What system-call sequence is needed to copy `in.txt` to `out.txt`?

**Step 1**: Open `in.txt` for reading.  
**Step 2**: Create/open `out.txt` for writing.  
**Step 3**: Repeatedly call `read()` on the input file.  
**Step 4**: For each block read, call `write()` on the output file.  
**Step 5**: Close both files.  
**Step 6**: If any call returns an error status, report or handle it.  
**Answer**: File copying is mostly file-management system calls wrapped by a user program or library.

### Example 2: `printf()` To `write()`

**Problem**: How does a C program printing text reach the OS?

**Step 1**: The program calls `printf("Hi\n")`.  
**Step 2**: The C library formats the string and chooses the output stream.  
**Step 3**: The library invokes a lower-level write operation.  
**Step 4**: The system-call interface enters the kernel and dispatches to the kernel's write implementation.  
**Answer**: `printf()` is not itself the kernel call; it is a library interface that eventually uses a system call such as `write()`.

### Example 3: Policy Versus Mechanism In Scheduling

**Problem**: Identify mechanism and policy for CPU time slicing.

**Step 1**: The timer interrupt and context-switch code provide a way to regain the CPU and switch processes. This is mechanism.  
**Step 2**: A rule such as round-robin, priority scheduling, or shortest job first decides which process runs next. This is policy.  
**Answer**: Mechanism answers "how can the OS switch?"; policy answers "which process should be chosen?"

---

## Common Mistakes / Gotchas

- Confusing APIs with system calls. APIs are usually higher-level wrappers.
- Assuming every shell command is built into the shell; many commands are separate programs.
- Thinking system programs are kernel code. Many daemons/services run in user context.
- Treating policy and mechanism as the same thing; separating them is a key OS design principle.
- Calling every modern OS purely monolithic or purely microkernel. Most are hybrids.
- Forgetting that `exec()` replaces a program image; it does not create a new process by itself.

---

## Summary / Cheat Sheet

| Term | Meaning |
|---|---|
| OS service | Function provided to programs/users or for efficient sharing |
| CLI/shell | Command interpreter for direct command entry |
| System call | Controlled programming interface to kernel services |
| API | Higher-level interface that may hide raw system calls |
| System program | Utility around OS services, often user-context |
| Policy | What should happen |
| Mechanism | How it is made to happen |
| Microkernel | Minimal kernel with user-space services and message passing |
| Loadable module | Kernel component loaded when needed |
| Bootstrap loader | Code that locates and starts the kernel |

**Key Formulas**:

$$
\text{Design flexibility increases when policy is separated from mechanism.}
$$

$$
\text{Boot path}:\ \text{firmware}\rightarrow\text{bootstrap loader}\rightarrow\text{kernel}\rightarrow\text{system services}
$$

**Key Takeaways**:

- OS services support both user convenience and safe resource sharing.
- Most user programs reach the OS through APIs, libraries, and the system-call interface.
- System programs define much of the user's practical experience of an OS.
- OS structures are trade-offs between simplicity, performance, reliability, portability, security, and maintainability.
- Booting moves from fixed firmware code to a full kernel and running system services.

---

## Practice Questions

**Q1**: List three services helpful to users and three services used for efficient system operation.  
> Answer: Helpful services include UI, program execution, I/O, file manipulation, communication, and error detection. Efficient operation services include resource allocation, accounting, protection, and security.

**Q2**: Why do APIs hide system-call details?  
> Answer: APIs give programmers a stable, higher-level interface while the runtime library and OS handle system-call numbers, parameter placement, traps, and return values.

**Q3**: Compare microkernel and modular-kernel designs.  
> Answer: A microkernel moves services into user space and communicates by message passing, improving reliability/security/portability but adding communication overhead. A modular kernel keeps components in kernel space but loads them dynamically through known interfaces, improving flexibility while preserving performance.

**Q4**: What is the role of GRUB in booting?  
> Answer: GRUB is a bootstrap loader that can locate and load the selected kernel, including choosing among disks, kernel versions, and boot options.
