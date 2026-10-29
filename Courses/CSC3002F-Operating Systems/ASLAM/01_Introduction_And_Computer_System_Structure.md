---
tags:
  - operating-systems
---

# Introduction And Computer System Structure

**Subject**: CSC3002F Operating Systems  
**Source**: `Operating Systems 1 Ch1.pdf`, Aslam Safla, pages 1-66  
**Generated**: 2026-06-03

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What An Operating System Does|What An Operating System Does]]
  - [[#Computer-System Organization|Computer-System Organization]]
  - [[#I/O, Bootstrap, Storage, And DMA|I/O, Bootstrap, Storage, And DMA]]
  - [[#Operating-System Operations|Operating-System Operations]]
  - [[#Dual Mode, Privilege, And Timers|Dual Mode, Privilege, And Timers]]
  - [[#OS Management Responsibilities|OS Management Responsibilities]]
  - [[#System Architectures And Computing Environments|System Architectures And Computing Environments]]
  - [[#Free/Open Source OSes And Kernel Data Structures|Free/Open Source OSes And Kernel Data Structures]]

---

## Core Content

### What An Operating System Does

#### Definitions

> **Operating System**: Software that controls and coordinates the use of hardware among application programs and users.

> **Hardware**: The basic computing resources, including CPU, memory, and I/O devices.

> **Application Program**: A program that defines how system resources are used to solve a user's computing problem.

> **Resource Allocator**: The OS role of allocating CPU time, memory, files, and I/O devices among competing users and programs.

> **Control Program**: The OS role of controlling user programs and I/O devices to prevent errors and improper use.

A computer system is divided into four conceptual components:

| Component | Role | Examples |
|---|---|---|
| Hardware | Provides raw computing resources | CPU, main memory, disks, keyboards, displays |
| Operating system | Coordinates and controls hardware use | Kernel, device drivers, schedulers |
| Application programs | Use resources to solve user problems | Browsers, compilers, games, databases |
| Users | Request work from the system | People, machines, other computers |

The OS looks different from different points of view. A user on a laptop values convenience, ease of use, and responsiveness. A shared mainframe or server must also maximize resource use and keep many users from interfering with each other. Mobile devices emphasize usability, battery life, and sensors such as touch, GPS, and voice input. Embedded systems may have little or no direct UI and run mostly without human intervention.



### Computer-System Organization

#### Definitions

> **Device Controller**: Hardware responsible for a particular device type and connected to the rest of the system through a bus.

> **Device Driver**: OS software that manages a device controller and provides a uniform interface to the kernel.

> **Interrupt**: A signal that transfers control to an interrupt service routine. **signal that tells the cpu to stop what its doing and handle something else.**

> **Interrupt Vector**: A table containing addresses of interrupt service routines.

> **Trap / Exception**: A software-generated interrupt caused by an error or a user request.

One or more CPUs and several device controllers connect through a common bus and share memory. The CPU and I/O devices can execute concurrently, so the OS must coordinate competition for memory cycles and device completion events.

Interrupt-driven I/O works like this:

1. A device controller performs I/O into or out of its local buffer.
2. The CPU moves data between main memory and the controller's buffer, unless DMA is used.
3. When the controller finishes, it raises an interrupt.
4. The interrupt vector directs execution to the correct interrupt service routine.
5. The OS saves the interrupted CPU state, handles the event, restores state, and resumes execution.

The OS is therefore **interrupt driven**: hardware interrupts report device events, and software interrupts/traps report system calls or exceptional conditions such as division by zero.




### I/O, Bootstrap, Storage, And DMA

#### Definitions

> **System Call**: A request from a user program for an OS service.

> **Bootstrap Program**: Initial code loaded at power-up or reboot that initializes the system and loads the kernel. Typically stored in ROM/EPROM, known as firmware.

> **Firmware**: Software stored in ROM or EPROM/NVM that provides low-level startup code.

> **Main Memory**: The large storage area the CPU can access directly.

> **Secondary Storage**: Nonvolatile storage used as an extension of main memory.

> **Caching**: Copying information into faster storage so future access is quicker.

> **Direct Memory Access (DMA)**: A method where a device controller transfers blocks directly between its buffer and main memory without CPU intervention for every byte, only one interrupt per block instead of per byte.

The source distinguishes two broad I/O styles:

| I/O Style                    | Control Returns To User Program | Consequence                                                                       |
| ---------------------------- | ------------------------------- | --------------------------------------------------------------------------------- |
| Synchronous/blocking I/O     | Only after I/O completion       | Simpler, but the CPU may idle or only one I/O request may be outstanding          |
| Asynchronous/nonblocking I/O | immediately without waiting     | More concurrency, but the OS must track device status and let programs wait later |

For asynchronous I/O, the OS maintains a **device-status table** with each device's type, address, and state. Programs can use system calls to wait for completion.

Storage is organized as a hierarchy by speed, cost, and volatility. Registers and caches are fastest and most expensive per byte. Main memory is directly accessible but volatile. Secondary storage is slower and nonvolatile. Hard disks organize surfaces into tracks and sectors; NVM/SSDs are faster than HDDs and increasingly common.

DMA matters because high-speed devices would waste CPU time if every byte caused an interrupt. With DMA, one interrupt is generated per block rather than per byte.

**Storage-Decive Hierarchy:**

<svg width="100%" viewBox="0 0 680 520" role="img">
<title>Storage hierarchy diagram</title>
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>
<rect x="285" y="30"  width="110" height="28" rx="3" fill="none" stroke="#4a90d9" stroke-width="1.2"/>
<text x="340" y="49" text-anchor="middle" font-size="12" fill="#888" font-family="sans-serif">registers</text>
<rect x="265" y="75"  width="150" height="28" rx="3" fill="none" stroke="#4a90d9" stroke-width="1.2"/>
<text x="340" y="94" text-anchor="middle" font-size="12" fill="#888" font-family="sans-serif">cache</text>
<rect x="235" y="120" width="210" height="28" rx="3" fill="none" stroke="#4a90d9" stroke-width="1.2"/>
<text x="340" y="139" text-anchor="middle" font-size="12" fill="#888" font-family="sans-serif">main memory</text>
<rect x="195" y="185" width="290" height="28" rx="3" fill="none" stroke="#4a90d9" stroke-width="1.2"/>
<text x="340" y="204" text-anchor="middle" font-size="12" fill="#888" font-family="sans-serif">nonvolatile memory</text>
<rect x="155" y="235" width="370" height="28" rx="3" fill="none" stroke="#4a90d9" stroke-width="1.2"/>
<text x="340" y="254" text-anchor="middle" font-size="12" fill="#888" font-family="sans-serif">hard-disk drives</text>
<rect x="110" y="285" width="460" height="28" rx="3" fill="none" stroke="#4a90d9" stroke-width="1.2"/>
<text x="340" y="304" text-anchor="middle" font-size="12" fill="#888" font-family="sans-serif">optical disk</text>
<rect x="60"  y="335" width="560" height="28" rx="3" fill="none" stroke="#4a90d9" stroke-width="1.2"/>
<text x="340" y="354" text-anchor="middle" font-size="12" fill="#888" font-family="sans-serif">magnetic tapes</text>
<line x1="340" y1="58"  x2="340" y2="73"  stroke="#888" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="340" y1="103" x2="340" y2="118" stroke="#888" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="340" y1="148" x2="340" y2="183" stroke="#888" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="340" y1="213" x2="340" y2="233" stroke="#888" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="340" y1="263" x2="340" y2="283" stroke="#888" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="340" y1="313" x2="340" y2="333" stroke="#888" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="230" y1="163" x2="450" y2="163" stroke="#888" stroke-width="0.8" stroke-dasharray="5,4"/>
<text x="100" y="158" text-anchor="end" font-size="11" fill="#888" font-family="sans-serif">volatile</text>
<text x="100" y="171" text-anchor="end" font-size="11" fill="#888" font-family="sans-serif">storage</text>
<text x="100" y="200" text-anchor="end" font-size="11" fill="#888" font-family="sans-serif">nonvolatile</text>
<text x="100" y="213" text-anchor="end" font-size="11" fill="#888" font-family="sans-serif">storage</text>
<line x1="28" y1="30"  x2="28" y2="363" stroke="#888" stroke-width="1.2" marker-start="url(#arrow)" marker-end="url(#arrow)"/>
<text x="20" y="100" text-anchor="middle" font-size="11" fill="#888" font-family="sans-serif" transform="rotate(-90,20,197)">smaller</text>
<text x="20" y="300" text-anchor="middle" font-size="11" fill="#888" font-family="sans-serif" transform="rotate(-90,20,310)">larger</text>
<text x="340" y="18" text-anchor="middle" font-size="11" fill="#888" font-family="sans-serif">storage capacity</text>
<line x1="652" y1="30"  x2="652" y2="363" stroke="#888" stroke-width="1.2" marker-start="url(#arrow)" marker-end="url(#arrow)"/>
<text x="660" y="100" text-anchor="middle" font-size="11" fill="#888" font-family="sans-serif" transform="rotate(90,660,197)">faster</text>
<text x="660" y="300" text-anchor="middle" font-size="11" fill="#888" font-family="sans-serif" transform="rotate(90,660,310)">slower</text>
<text x="340" y="395" text-anchor="middle" font-size="11" fill="#888" font-family="sans-serif">access time</text>
<line x1="455" y1="30"  x2="620" y2="30"  stroke="#888" stroke-width="0.8"/>
<line x1="455" y1="163" x2="620" y2="163" stroke="#888" stroke-width="0.8"/>
<text x="622" y="103" font-size="11" fill="#888" font-family="sans-serif">primary</text>
<text x="622" y="116" font-size="11" fill="#888" font-family="sans-serif">storage</text>
<line x1="490" y1="163" x2="620" y2="163" stroke="#888" stroke-width="0.8"/>
<line x1="490" y1="265" x2="620" y2="265" stroke="#888" stroke-width="0.8"/>
<text x="622" y="220" font-size="11" fill="#888" font-family="sans-serif">secondary</text>
<text x="622" y="233" font-size="11" fill="#888" font-family="sans-serif">storage</text>
<line x1="530" y1="265" x2="620" y2="265" stroke="#888" stroke-width="0.8"/>
<line x1="530" y1="363" x2="620" y2="363" stroke="#888" stroke-width="0.8"/>
<text x="622" y="320" font-size="11" fill="#888" font-family="sans-serif">tertiary</text>
<text x="622" y="333" font-size="11" fill="#888" font-family="sans-serif">storage</text>
</svg>

### Operating-System Operations

#### Definitions

> **Kernel**: The core OS component that runs with privileged access and manages hardware and core resources.

> **Daemon / Service**: A background system process that provides services outside the kernel.

> **Multiprogramming**: Keeping several jobs in memory so the CPU always has another job to run when one waits.

> **Multitasking / Time Sharing**: Rapidly switching the CPU among jobs so users can interact with programs while they run.

> **CPU Scheduling**: Choosing which ready process/thread should run next.

> **Swapping**: Moving processes between memory and secondary storage to allow more processes than fit in RAM at once.

> **Virtual Memory**: A memory abstraction that allows processes to execute without being completely resident in physical memory.

After bootstrapping, the kernel loads and starts system daemons. The kernel responds to hardware interrupts, traps, exceptions, and system calls. It also deals with process failures such as infinite loops, illegal memory modification, or attempts to modify the OS.

Multiprogramming improves CPU utilization:

1. Keep a subset of jobs in memory.
2. Select one job to run.
3. When that job waits for I/O, switch to another job.
4. Repeat so the CPU has useful work while devices are busy.

Time sharing extends this by switching frequently enough to support interactive users. If several jobs are ready, CPU scheduling chooses among them. If memory pressure is high, swapping and virtual memory support execution even when all process code/data is not simultaneously in RAM.
### Dual Mode, Privilege, And Timers

#### Definitions

> **User Mode**: A restricted CPU mode used for ordinary application code.

> **Kernel Mode**: A privileged CPU mode used for OS code.

> **Mode Bit**: Hardware state indicating whether the CPU is executing user or kernel code.

> **Privileged Instruction**: An instruction that may execute only in kernel mode.

> **Timer**: Hardware that interrupts after a set time interval.

Dual-mode operation protects the OS and other processes. User code cannot simply set the mode bit to kernel mode. Instead, a system call transfers control into the kernel through a controlled path, and return from the system call restores user mode.

The timer prevents a user process from monopolizing the CPU:

1. The OS sets a counter before scheduling a process.
2. A physical clock decrements the counter.
3. When the counter reaches zero, a timer interrupt occurs.
4. The kernel regains control and may reschedule or terminate the program.




### OS Management Responsibilities

#### Definitions

> **Process**: A program in execution.

> **Thread**: A path of execution within a process.

> **File System**: The OS abstraction that provides a logical view of stored information as files and directories.

> **Protection**: Mechanisms controlling access of processes or users to OS-defined resources.

> **Security**: Defense against internal and external attacks.

The OS is responsible for:

| Area | Main Responsibilities |
|---|---|
| Process management | Create/delete processes, suspend/resume, synchronization, communication, deadlock handling |
| Memory management | Track memory use, choose what moves into/out of memory, allocate/deallocate memory |
| File-system management | Create/delete files/directories, manipulate files, map files to storage, backup |
| Mass-storage management | Mount/unmount, free-space management, storage allocation, disk scheduling, partitioning, protection |
| I/O subsystem | Buffering, caching, spooling, uniform device-driver interface, device-specific drivers |
| Protection/security | User IDs, group IDs, access control, privilege escalation control, defense against attacks |

Caching appears across hardware, OS, and applications. In multitasking and multiprocessor environments, the OS/hardware must ensure the most recent value is observed. Multiprocessor systems need cache coherency; distributed systems are even more complex because copies may exist on different machines.
### System Architectures And Computing Environments

#### Definitions

> **Virtualization**: Running applications or guest operating systems inside another OS or virtual machine monitor.

> **Virtual Machine Manager (VMM)**: Software that provides virtualization services.

> **Distributed System**: A collection of separate, networked systems that communicate and may appear as one system.

> **Multiprocessor System**: A system with multiple processors, also called a parallel or tightly coupled system.

> **Symmetric Multiprocessing (SMP)**: A multiprocessor design where each processor can perform all tasks.

> **Asymmetric Multiprocessing**: A design where each processor is assigned a specific task.

> **Clustered System**: Multiple systems working together, often sharing storage, for high availability or high performance.

Virtualization is useful for running multiple OSes on a laptop, compatibility testing, software development across OS targets, QA testing, and data-center compute management. Emulation is needed when the source CPU type differs from the target CPU type, but it is usually slower than native virtualization.

Multiprocessor systems improve throughput, provide economy of scale, and can improve reliability through graceful degradation or fault tolerance. Clustered systems are like multiprocessors at a larger scale: separate machines coordinate, often with shared storage and a storage-area network.

The source lists common computing environments:

| Environment | Core Idea |
|---|---|
| Traditional | Stand-alone general-purpose machines, now usually networked |
| Mobile | Smartphones/tablets with wireless networking, sensors, and battery constraints |
| Client-server | Servers respond to requests from clients, such as compute servers or file servers |
| Peer-to-peer | Nodes act as clients, servers, or both |
| Cloud computing | Compute, storage, and applications delivered as network services |
| Real-time embedded | Special-purpose systems with fixed time constraints |

Cloud types include public, private, and hybrid cloud. Service models include **SaaS**, **PaaS**, and **IaaS**.



### Free/Open Source OSes And Kernel Data Structures

#### Definitions

> **Open-Source Operating System**: An OS made available in source-code form.

> **Copyleft**: A licensing approach associated with the GNU GPL that preserves software freedom in derivative works.

> **Bitmap**: A string of binary digits representing the status of many items.

Open-source OSes such as GNU/Linux, BSD UNIX, Solaris, and parts of macOS make OS internals easier to study. Virtualization also lets students experiment with multiple OSes without dedicated hardware.

Kernel implementations use standard data structures:

| Data Structure | OS Use |
|---|---|
| Singly/doubly/circular linked lists | Ready queues, device lists, kernel object lists |
| Binary search trees / balanced trees | Ordered lookup; balanced search can be $O(\log n)$ |
| Hash maps | Fast average-case lookup by key |
| Bitmaps | Track free/used frames, blocks, or resource slots |
