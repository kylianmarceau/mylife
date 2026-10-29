---
tags:
  - operating-systems
---

# CSC3002F Operating Systems Flashcards

These cards use the Obsidian Spaced Repetition plugin inline flashcard format.

Sources covered: all source-backed lecture notes in `Courses/CSC3002F-Operating Systems/ASLAM/` and `Courses/CSC3002F-Operating Systems/MICHEL/`.

---

## Introduction And Computer System Structure

#flashcards/CSC3002F-Operating-Systems/ASLAM/01-Introduction-And-Computer-System-Structure

What is an operating system?::Software that controls and coordinates the use of hardware among application programs and users.
What are the four conceptual components of a computer system?::Hardware, operating system, application programs, and users.
What is hardware in the OS model?::The basic computing resources, such as CPU, main memory, disks, keyboards, and displays.
What is an application program in the OS model?::A program that uses system resources to solve a user's computing problem.
What does it mean that the OS is a resource allocator?::It allocates CPU time, memory, files, and I/O devices among competing users and programs.
What does it mean that the OS is a control program?::It controls user programs and I/O devices to prevent errors and improper use.
How do laptop, shared-server, mobile, and embedded OS goals differ?::Laptops emphasize convenience/responsiveness; shared systems emphasize resource use and isolation; mobile systems emphasize usability, battery, and sensors; embedded systems often run with little direct UI.
What is a device controller?::Hardware responsible for a particular device type and connected to the system through a bus.
What is a device driver?::OS software that manages a device controller and presents a uniform kernel interface.
What is an interrupt?::A signal that transfers control to an interrupt service routine so the CPU can handle an event.
What is an interrupt vector?::A table containing the addresses of interrupt service routines.
What is a trap or exception?::A software-generated interrupt caused by an error or a user request such as a system call.
What are the main steps of interrupt-driven I/O?::The controller performs I/O, raises an interrupt, the vector selects the handler, the OS saves state, handles the event, restores state, and resumes execution.
Why is an OS described as interrupt driven?::Hardware interrupts report device events, while traps/exceptions report system calls and exceptional conditions.
What is a system call?::A request from a user program for an OS service.
What is a bootstrap program?::Initial startup code that initializes the system and loads the kernel.
What is firmware?::Low-level startup software stored in ROM, EPROM, or nonvolatile memory.
What is main memory?::The large storage area directly accessible by the CPU.
What is secondary storage?::Nonvolatile storage used as an extension of main memory.
What is caching?::Copying information into faster storage so later access is quicker.
What is direct memory access (DMA)?::A device-controller transfer method that moves blocks directly between controller buffer and main memory, causing one interrupt per block rather than one per byte.
How do synchronous and asynchronous I/O differ?::Synchronous I/O returns control only after completion; asynchronous I/O returns immediately and requires the OS to track completion.
What does the OS device-status table track for asynchronous I/O?::Each device's type, address, and state so programs can wait for completion later.
What is the storage hierarchy from fastest/smallest to slowest/largest?::Registers, cache, main memory, nonvolatile memory, hard disks, optical disks, and magnetic tapes.
Why does DMA improve high-speed I/O performance?::It avoids interrupting the CPU for every byte and instead interrupts once per transferred block.
What is the kernel?::The core OS component that runs with privileged access and manages hardware and core resources.
What is a daemon or service?::A background system process that provides services outside the kernel.
What is multiprogramming?::Keeping several jobs in memory so the CPU can run another job when one waits for I/O.
What is multitasking or time sharing?::Rapidly switching the CPU among jobs so users can interact with programs while they run.
What is CPU scheduling?::Choosing which ready process or thread should run next.
What is swapping?::Moving processes between memory and secondary storage so more processes can exist than fit in RAM at once.
What is virtual memory?::A memory abstraction allowing processes to execute without being fully resident in physical memory.
How does multiprogramming improve CPU utilization?::When one job blocks for I/O, the OS switches the CPU to another ready job.
What is user mode?::A restricted CPU mode used for ordinary application code.
What is kernel mode?::A privileged CPU mode used for OS code.
What is a mode bit?::Hardware state indicating whether the CPU is executing user or kernel code.
What is a privileged instruction?::An instruction that may execute only in kernel mode.
Why are timers important for OS control?::A timer interrupt lets the kernel regain control and prevents a user process from monopolizing the CPU.
How does a system call cross from user mode to kernel mode?::It uses a controlled trap/system-call path into the kernel, then returns to user mode after service.
What are the main OS process-management responsibilities?::Create/delete processes, suspend/resume, synchronize, communicate, schedule, and handle deadlocks.
What are the main OS memory-management responsibilities?::Track memory use, decide what moves into and out of memory, and allocate/deallocate memory.
What are the main OS file-system responsibilities?::Create/delete files and directories, manipulate files, map files to storage, and support backup.
What is protection in OS terms?::Mechanisms controlling access of processes or users to OS-defined resources.
What is security in OS terms?::Defense against internal and external attacks.
Why is cache coherency needed in multiprocessor systems?::Multiple processors may cache copies of the same data, so hardware/OS must ensure the newest value is observed.
What is virtualization?::Running applications or guest operating systems inside another OS or virtual machine monitor.
What is a virtual machine manager (VMM)?::Software that provides virtualization services.
What is a distributed system?::A collection of separate networked systems that communicate and may appear as one system.
What is a multiprocessor system?::A tightly coupled system with multiple processors.
How do symmetric and asymmetric multiprocessing differ?::In SMP each processor can perform all tasks; in asymmetric multiprocessing processors are assigned specific tasks.
What is a clustered system?::Multiple systems working together, often sharing storage, for high availability or high performance.
What are the major cloud service models?::SaaS provides applications, PaaS provides a platform/runtime, and IaaS provides infrastructure such as compute and storage.
What is an open-source operating system?::An OS made available in source-code form.
What is copyleft?::A licensing approach, associated with the GNU GPL, that preserves software freedom in derivative works.
What is a bitmap in kernel data structures?::A string of bits representing the status of many items, such as free or used frames.
Which data structures are common in kernels?::Linked lists, balanced trees, hash maps, and bitmaps.
How do you compute CPU utilization for one CPU/I/O cycle?::CPU burst time divided by CPU burst time plus I/O wait time.
Why can multiprogramming occur without true parallelism?::A single CPU can switch among jobs, so only one runs at an instant even though several are active.

## Operating System Services And Structures

#flashcards/CSC3002F-Operating-Systems/ASLAM/02-Operating-System-Services-And-Structures

What is an operating-system service?::A function the OS provides to users, programs, or the system itself.
Which OS services are mainly helpful to users and programs?::UI, program execution, I/O operations, file-system manipulation, communication, and error detection.
Which OS services are mainly for efficient system operation?::Resource allocation, accounting, protection, and security.
What is a user interface (UI)?::The way users interact with the OS.
What is a command-line interface (CLI)?::A UI where commands are typed directly to a command interpreter.
What is a shell?::A command interpreter, usually a system program rather than kernel code.
Why does implementing commands as external programs make a shell flexible?::New commands can be added without changing the shell itself.
What is a graphical user interface (GUI)?::A UI based on windows, icons, menus, mouse/keyboard, and visual objects.
What is a touchscreen interface?::A UI based on gestures, touch selection, virtual keyboard, and sometimes voice.
What is a system call?::The programming interface to OS services.
What is an API?::A higher-level interface used by programs that often hides raw system-call details.
What is the system-call interface?::The OS layer that maps system-call numbers to kernel routines.
What is a runtime support library?::Compiler-provided library code that helps implement APIs and system calls.
What are common OS APIs?::Win32 for Windows, POSIX for UNIX/Linux/macOS-like systems, and the Java API for the JVM.
What is the normal path from API call to kernel routine?::Application calls API, wrapper places number/parameters, trap enters kernel, system-call interface dispatches, kernel routine runs, status returns.
What are the three parameter-passing methods for system calls?::Registers, memory block/table with address in a register, and stack.
Why use memory-block parameter passing for system calls?::It handles many or large parameters without being limited by register count.
What are process-control system calls?::Calls that create, terminate, load, execute, wait, signal, allocate/free memory, dump memory, debug, or lock.
What are file-management system calls?::Calls to create, delete, open, close, read, write, reposition, or change file attributes.
What are device-management system calls?::Calls to request, release, read, write, reposition, or configure devices.
What are information-maintenance system calls?::Calls to get/set time, date, system data, and attributes.
What are communication system calls?::Calls to create/delete connections, send/receive data, use shared memory, transfer status, or attach/detach remotely.
What are protection system calls?::Calls that control resource access, permissions, and user allow/deny decisions.
How does `printf()` reach the OS?::The user program calls `printf()`, the C library formats output, and a lower-level call such as `write()` transfers bytes through the system-call interface.
What was MS-DOS's execution model?::Single-tasking: running a program loaded it into memory and overwrote much of the shell until the program exited.
What is FreeBSD's shell execution model?::The shell forks a child, the child execs the requested program, and the parent waits or continues accepting commands.
What does `fork()` do?::It creates a new UNIX-style process.
What does `exec()` do?::It loads a new program into an existing process image.
What is a system program?::A program that provides a convenient environment for program development and execution.
What are examples of system programs?::File utilities, status tools, editors, compilers, loaders, debuggers, communication tools, background services, and application programs.
What is policy in OS design?::The decision about what will be done.
What is mechanism in OS design?::The implementation of how something is done.
Why separate policy from mechanism?::It makes the OS more flexible because one mechanism can support multiple policies.
What is a timer interrupt in policy/mechanism terms?::The timer/context-switch code is mechanism; a scheduling rule such as RR or priority is policy.
What is SYSGEN?::System generation/configuration that builds or tunes an OS for a specific hardware configuration.
What is a monolithic kernel?::A kernel structure where many OS services run in one large kernel address space.
What is a layered OS structure?::A structure where each layer uses only lower-level services.
What is a microkernel?::A small kernel that moves as much functionality as possible into user space and communicates by message passing.
What is a loadable kernel module?::A kernel component loaded as needed through known interfaces.
What is a hybrid OS structure?::A design combining multiple approaches such as monolithic, modular, and microkernel ideas.
What is the main strength of a microkernel?::Extension, portability, reliability, and security improve because many services run outside the kernel.
What is the main weakness of a microkernel?::User/kernel communication overhead.
How do modular kernels differ from microkernels?::Modules stay in kernel space but are dynamically loadable; microkernels move services to user space.
How are Linux and Solaris commonly characterized structurally?::Largely monolithic but modular.
How is macOS characterized structurally?::Hybrid, combining Aqua/Cocoa, Darwin/XNU, Mach components, BSD UNIX parts, I/O Kit, and kernel extensions.
What is iOS?::Apple's mobile OS for iPhone and iPad, adapted from macOS ideas for mobile devices.
What is Android?::An open-source mobile OS based on a modified Linux kernel and Java-oriented application stack.
What does the Android Linux kernel provide?::Process, memory, device-driver, and power management.
What is debugging?::Finding and fixing errors.
What is a core dump?::A file capturing a failed process's memory.
What is a crash dump?::A file capturing kernel memory after an OS failure.
What is tracing?::Recording system activities for later analysis.
What is profiling?::Periodically sampling execution to find performance trends.
What is a bootstrap loader?::Small code that locates the kernel, loads it into memory, and starts it.
What is GRUB's boot role?::It selects and loads a kernel from disks, versions, or boot options.
What is the boot path from firmware to services?::Firmware -> bootstrap loader -> kernel -> system services.
Why are APIs not the same as system calls?::APIs are stable, higher-level wrappers; the OS still uses system-call numbers, traps, and kernel dispatch internally.
What is the gotcha about `exec()` in process creation?::`exec()` replaces the current program image; it does not create a new process by itself.

## Main Memory

#flashcards/CSC3002F-Operating-Systems/ASLAM/03-Main-Memory

What must happen before a program can run?::It must be brought from disk into memory and placed inside a process.
What can the CPU directly access?::Registers and main memory.
Why do caches matter for memory performance?::Main memory is slower than registers, so cache reduces CPU stalls on repeated accesses.
Why is memory protection necessary?::Multiple processes and the OS share physical memory, so user processes must not access others' memory or kernel memory unless allowed.
What is a base register?::A register containing the smallest physical address a process may access.
What is a limit register?::A register containing the size or range of the process's logical address space.
What is address binding?::Mapping addresses from one address space to another.
What is compile-time address binding?::Address binding when the program is compiled; it requires the starting location to be known.
What is load-time address binding?::Address binding when the program is loaded; it uses relocatable code.
What is execution-time address binding?::Dynamic translation while the program runs; it needs hardware support.
What address form appears in source code?::Symbolic names.
<!--SR:!2026-06-08,4,270-->
What address form appears in compiled code?::Relocatable addresses, such as an offset from a module.
What address form appears in a loaded or running image?::Absolute physical addresses or translated addresses.
What is the base/limit legal-access condition?::$0 \le$ logical address $<$ limit.
What is the simple relocation-register physical-address formula?::Physical address = relocation register + logical address.
What is a logical or virtual address?::An address generated by the CPU.
What is a physical address?::The address seen by the memory unit.
When are logical and physical addresses the same?::Under compile-time or load-time binding.
When do logical and physical addresses differ?::Under execution-time binding with hardware translation.
What is the MMU?::Hardware that maps virtual/logical addresses to physical addresses at run time.
<!--SR:!2026-06-08,4,270-->
What is dynamic loading?::Loading a routine only when it is called.
Why does dynamic loading improve memory use?::Rarely used code is not loaded until needed.
What is static linking?::Combining system libraries and program code into one binary image at load time.
What is dynamic linking?::Postponing linking until execution time.
What is a stub in dynamic linking?::Small code that locates a memory-resident library routine and replaces itself with the routine address.
<!--SR:!2026-06-08,4,270-->
Why are shared library versions important?::Programs may depend on specific versions, so patches must not break compatible assumptions.
What is backing store?::Fast disk space large enough to hold process memory images.
What is the swap transfer-time formula?::Swap transfer time = process image size / disk transfer rate.
What is the source-style swap example for 100 MB at 50 MB/s?::Swapping out takes 2 s; swapping out and back in costs about 4 s.
Why does pending I/O complicate swapping?::I/O into process memory could target the wrong process after memory is reused.
What workaround handles pending I/O during swapping, and what is the cost?::Double buffering through kernel space; it adds overhead.
Why do mobile systems often avoid swapping?::Flash storage has limited write cycles and weaker throughput for heavy swap use.
What is contiguous allocation?::A memory method where each process occupies one contiguous physical-memory region.
What is a partition?::A section of memory allocated for OS or process use.
What is a hole in memory allocation?::A contiguous block of available memory.
What is first-fit allocation?::Allocate the first hole large enough.
What is best-fit allocation?::Allocate the smallest hole large enough.
<!--SR:!2026-06-08,4,270-->
What is worst-fit allocation?::Allocate the largest available hole.
What is external fragmentation?::Free memory exists but is split into holes too small or noncontiguous for a request.
What is internal fragmentation?::Allocated memory is larger than requested and the unused space is inside the allocation.
What is the dynamic storage allocation problem?::Given request size $n$, choose a free hole of size at least $n$.
What is the 50-percent rule?::With $N$ allocated blocks, about $0.5N$ blocks can be lost to fragmentation, so roughly one third of memory may be unusable.
What is compaction?::Moving memory contents so scattered free holes become one large block.
When is compaction possible?::Only with dynamic relocation at execution time and careful handling of pending I/O.
What is segmentation?::A memory-management scheme matching the user's view of memory as logical segments.
What is a segment?::A logical unit such as a main program, procedure, method, object, stack, symbol table, or array.
What is a segment table?::A table mapping segment numbers to physical bases and limits.
What do STBR and STLR store?::STBR points to the segment table; STLR stores the number of segments used by the program.
What is the form of a segmented logical address?::$\langle$segment number, offset$\rangle$.
What fields are in a segment-table entry?::Base, limit, and validation/protection bits.
When is segment number $s$ legal?::$s < \text{STLR}$.
<!--SR:!2026-06-08,4,270-->
Why can segmentation suffer external fragmentation?::Segments vary in size, so allocation is a variable-sized hole problem.
What is paging?::A memory-management scheme splitting logical memory into fixed-size pages and physical memory into same-size frames.
What is a frame?::A fixed-size physical-memory block.
<!--SR:!2026-06-08,4,270-->
What is a page?::A fixed-size logical-memory block.
What is a page table?::A per-process table translating page numbers to frame numbers.
What is a page offset?::The displacement inside a page.
<!--SR:!2026-06-08,4,270-->
For logical address space $2^m$ and page size $2^n$, how is an address split?::It is split into page number $p$ and offset $d$, with $n$ offset bits.
How is a paging physical address formed?::The page table maps page $p$ to frame $f$ and combines $f$ with the unchanged offset $d$.
<!--SR:!2026-06-08,4,270-->
Why does paging avoid external fragmentation?::Any free frame can hold any page, so physical pages need not be contiguous.
Why does paging still have internal fragmentation?::The final page of a process may not fill its frame.
What is worst-case internal fragmentation in paging?::Frame size minus 1 byte.
What is average internal fragmentation in paging?::About one half of the frame size.
What internal fragmentation occurs for 72,766 bytes with 2,048-byte pages?::The last page uses 1,086 bytes, so fragmentation is 2,048 - 1,086 = 962 bytes.
What is the PTBR?::The page-table base register, pointing to the page table in memory.
What is the PTLR?::The page-table length register, indicating page-table size.
What is a TLB?::A small fast associative cache for recent page-table translations.
What is associative memory?::Memory searched in parallel by content.
What is TLB hit ratio?::The percentage of memory references found in the TLB.
Why can a page-table access double memory-access cost without a TLB?::One memory access is needed for the page table and another for the actual data/instruction.
What is the EAT formula from the notes when hit cost is 100 ns and miss cost is 200 ns?::$\text{EAT}=\alpha(100)+(1-\alpha)(200)$ ns.
What is EAT with 80 percent TLB hit ratio in that example?::120 ns.
What is EAT with 99 percent TLB hit ratio in that example?::101 ns.
What are ASIDs used for in TLBs?::They tag translations by process/address space and can avoid full TLB flushes on context switch.
What is a valid-invalid bit?::A page-table bit indicating whether a page is part of the process's legal logical address space.
What is shared code?::Read-only reentrant code shared among processes.
What is hierarchical paging?::Breaking a page table into multiple levels to avoid huge contiguous page tables.
What is a hashed page table?::A page-table structure using a hash of virtual page numbers, useful for large sparse spaces.
What is an inverted page table?::A table with one entry per physical frame rather than one page table per process over all logical pages.
How many page-table entries does a 32-bit space with 4 KB pages need in a flat table?::$2^{32}/2^{12}=2^{20}=1,048,576$ entries.
How large is that page table with 4-byte entries?::$2^{20}\times4=4$ MB.
What does IA-32 combine for address translation?::Segmentation to produce linear addresses, then paging to produce physical addresses.
What is PAE?::Page Address Extension, allowing 32-bit systems to address more than 4 GB of physical memory.
<!--SR:!2026-06-08,4,270-->
What physical address size does PAE support in the notes?::$2^{36}$ bytes = 64 GB.
What page sizes are common in practical x86-64 implementations?::4 KB, 2 MB, and 1 GB pages.
What page sizes does ARM support in the notes?::4 KB and 16 KB pages, larger sections, and multi-level TLBs.
What is the key gotcha about a TLB miss?::A TLB miss is not necessarily a page fault; the page may still be resident and valid in the page table.

## Demand Paging And Page Replacement

#flashcards/CSC3002F-Operating-Systems/ASLAM/04-Demand-Paging-And-Page-Replacement

What is demand paging?::A virtual-memory strategy where a page is brought into main memory only when it is referenced.
Why does demand paging save memory?::Unused pages stay on secondary storage instead of occupying RAM.
How does demand paging improve startup time?::A process can begin before every page is loaded.
How does demand paging support multiprogramming?::More processes can share RAM because each needs only its active pages.
What is a page hit?::A reference to a page that is already resident in physical memory.
What is a page fault?::A trap raised when a process references a page that is missing from physical memory or marked invalid.
What is a PTE?::A page table entry storing translation and status information for a virtual page.
What does the valid bit in a PTE indicate?::Whether the page can currently be translated as a valid resident page.
What is the simplified page-fault condition?::If `PTE.valid = 0`, raise a page fault.
Why is a page fault like a system-call transition but not a voluntary system call?::The MMU trap switches to kernel code, but user code did not explicitly request the fault handler.
What are the main steps in handling a page fault?::Trap, validate the reference, find a free frame or victim, write back dirty victim if needed, read the needed page, update PTE, restart the faulting instruction.
Can the faulting process run while its page is fetched from disk?::No; it waits, though the OS may run another ready process.
What is a victim page?::A resident page selected for eviction so its frame can be reused.
What is a compulsory page fault?::A fault because the page has not yet been brought into physical memory.
What is a capacity page fault?::A fault because physical memory is too small for the active demand.
What is a policy page fault?::A fault because the replacement algorithm evicted a page that is needed again.
What is a page replacement algorithm?::A policy for choosing which resident page to evict when no free frame is available.
What is a reference string?::A sequence of page numbers accessed by a process.
How is page-fault count evaluated for a reference string?::Count each reference whose page is not resident at access time.
What does random replacement do?::It evicts an arbitrary resident page.
What is the main weakness of random replacement?::Its performance is unpredictable.
What does FIFO replacement do?::It evicts the page that has been resident the longest.
How does FIFO manage pages?::Insert loaded pages at the back of a queue and evict from the front on replacement.
Why can FIFO perform poorly?::It ignores actual usage and can evict a heavily used page.
What is OPT replacement?::The algorithm that evicts the page whose next reference is farthest in the future.
What does Belady's theorem say?::Evicting the page used farthest in the future minimizes page-fault rate.
Why is OPT not implementable online?::The OS does not know the future reference string.
Why is OPT still useful?::It gives a theoretical lower-bound benchmark for other algorithms.
For the notes' 3-frame reference string, what are OPT, LRU, and FIFO fault counts?::OPT = 9, LRU = 12, FIFO = 15.
What is LRU replacement?::It evicts the page that has not been used for the longest time.
What locality assumption supports LRU?::Recently used pages are likely to be used again soon.
How can exact LRU be implemented with timestamps?::Record the current time on every reference and evict the page with the oldest timestamp.
Why is exact LRU expensive?::The OS or hardware must record recency and search for the oldest timestamp.
What is MFU replacement?::It evicts the most frequently used page.
Why can MFU be a poor match for locality?::Frequently used pages may still be important.
What is Belady's anomaly?::Increasing the number of frames increases the number of page faults for some algorithms.
What FIFO anomaly example appears in the notes?::On reference string 3,2,1,0,3,2,4,3,2,1,0,4, FIFO has 9 faults with 3 frames and 10 faults with 4 frames.
What is a stack algorithm?::An algorithm where the pages resident with $N$ frames are always a subset of those resident with $N+1$ frames.
Why do stack algorithms avoid Belady's anomaly?::The subset property means adding frames cannot increase faults.
Which algorithms in the notes are stack-style?::LRU and OPT.
What is the stack algorithm subset property?::$S_N(t)\subseteq S_{N+1}(t)$.
What is the Clock algorithm?::An approximate LRU policy using a circular list, clock hand, and reference bits.
What is the Clock replacement rule?::Replace a page with used bit 0; if used bit is 1, set it to 0 and give another chance.
Why is Clock faster than exact LRU?::It uses cheap reference bits instead of exact timestamps for every access.
What is Clock's worst-case scan cost?::$O(N)$ if every page has its used bit set.
What is a dirty bit?::A bit set when a page has been modified after being loaded.
Why are dirty pages expensive to evict?::They must be written back before the frame can be reused.
What is a clean page?::A page whose memory contents match backing storage and can be discarded cheaply.
What is the usual replacement preference for (used bit, dirty bit)?::Best is (0,0), then possible (0,1), avoid/retry (1,0), and avoid most (1,1).
What is second chance?::A clock-style rule that avoids immediately evicting recently referenced pages.
What is N-Chance Clock?::A Clock variant that gives pages $N$ chances or sweeps before replacement.
What is the trade-off in choosing large $N$ for N-Chance Clock?::It better approximates LRU but may spend longer cycling to find a victim.
Why do modern OSes use Clock-like approximations?::They approximate LRU with acceptable overhead using reference/dirty bits and counters.

## Frame Allocation, Thrashing, And Working Sets

#flashcards/CSC3002F-Operating-Systems/ASLAM/05-Frame-Allocation-Thrashing-And-Working-Sets

What question does frame allocation answer?::How many physical frames each process should receive.
How do demand paging, page replacement, and frame allocation differ?::Demand paging decides when to load; replacement decides what to evict; allocation decides how many frames each process may use.
What is physical frame allocation?::The OS decision of how many physical memory frames each process receives.
What is load control?::OS control over how many processes are allowed to compete for memory at one time.
What performance outcomes does frame allocation affect?::Page-fault rate, fairness, throughput, and whether thrashing starts.
What is local replacement?::Page replacement where a process can evict only its own pages.
What is global replacement?::Page replacement where the victim may be selected from all frames in the system.
What is a resident set?::The set of pages from a process currently held in physical memory.
What is the main strength of local replacement?::It gives more predictable per-process behavior and contains damage from a faulting process.
What is the main weakness of local replacement?::A process may be stuck with too few frames even if freeable frames exist elsewhere.
What is the main strength of global replacement?::It can improve overall memory utilization.
What is the main weakness of global replacement?::Other processes can steal frames, making runtime and page-fault rates unstable.
What is fixed allocation?::An allocation policy where each process receives a fixed number of frames.
What is equal allocation?::Every process receives the same number of frames.
What is the equal-allocation formula?::Each process receives $m/n$ frames for $m$ frames and $n$ processes.
What is proportional allocation?::Processes receive frames proportional to their process size.
What is the proportional-allocation formula?::$a_i=(s_i/S)\times m$, where $S=\sum_i s_i$.
What is priority allocation?::Frame assignment depends on OS, user, or process priority.
How can priority allocation choose victims?::A higher-priority faulting process may take a frame from a lower-priority process.
What is a free frame list?::A list of physical frames currently available for allocation.
What is page-out?::Moving pages from memory to backing storage to free frames.
What does a low-free threshold trigger?::Page replacement/page-out to rebuild the free frame list.
What is `lots-free` in the source's Linux example?::A low-free threshold of about 1/64 of main memory.
What may Linux do if page-out cannot keep enough free pages?::Swap out whole processes as a last resort.
How do compulsory, capacity, and policy faults relate to allocation?::Compulsory faults are first-use; capacity faults need more frames or fewer active processes; policy faults may need better replacement or load control.
What is thrashing?::A condition where a process or system spends most time swapping pages instead of doing useful computation.
What is over-commitment?::Active processes collectively demand more memory than physical memory can support.
What is the thrashing feedback loop?::Faults cause disk I/O, CPU utilization drops, the OS may admit more processes, frames per process shrink, and faults get worse.
Why can low CPU utilization be misleading during thrashing?::The CPU is idle because processes wait for paging I/O, not because the system needs more processes.
What causes thrashing?::Bad replacement policy, too many active processes, too few frames per process, or global frame stealing.
How can local or priority replacement help prevent thrashing spread?::It limits which pages a faulting process can steal, containing damage.
What is a working set?::The set of pages a process has used recently and is likely to need again.
What is the working set algorithm's core load-control idea?::Run only processes whose working sets can fit into available frames.
What is locality of reference?::The tendency of memory references to cluster around a small set of pages for a period.
What is temporal locality?::Reuse of the same memory locations over time.
What is spatial locality?::Use of memory locations near other recently used locations.
Why does virtual memory depend on locality?::If the active locality fits in memory, faults mostly happen early and then performance is good.
In the 128 by 128 array example, why is row-wise traversal better?::Each row fits in one page, so row-wise traversal has 128 faults instead of 16,384 column-wise faults.
What is the row-wise page-fault count in the source array example?::128 faults.
What is the column-wise page-fault count in the source array example?::$128\times128=16,384$ faults.
What is a working set window $w$?::The time interval or number of page references used to decide which pages count as recent.
What is $WS(t,w)$?::The set of pages referenced during the last $w$ references or time units at time $t$.
What is working set size?::$|WS(t,w)|$, the number of distinct pages in the working set.
What is total frame demand $D$?::$D=\sum_i |WS_i(t,w)|$ across active processes.
What does $D>m$ mean?::Active working sets do not fit in the available physical frames, so load should be reduced.
What are the main steps of the working set algorithm?::Estimate each working set, continue/start only if it fits, use local replacement, track changes, reallocate dynamically, and suspend/swap processes that do not fit.
What is page-fault frequency (PFF)?::A measure based on how often a process faults.
What is the PFF window rule in the notes?::If references since last fault exceed $w$, remove pages not referenced since the last fault; otherwise add the faulting page.
What happens if working set window $w$ is too small?::It misses part of the current locality and causes excessive page faults.
What happens if working set window $w$ is too large?::It keeps old localities resident, wasting memory and slowing other processes.
What happens as $w\to\infty$?::The working set approaches the entire program.

## Security

#flashcards/CSC3002F-Operating-Systems/ASLAM/06-Security

What is security in OS terms?::Ensuring resources are used and accessed as intended under all circumstances.
What is a threat?::A potential security violation.
What is an attack?::An attempt to breach security.
Why is perfect security unachievable?::Practical systems must balance protection, cost, usability, and evolving attacker behavior.
What is a breach of confidentiality?::Unauthorized reading of data.
What is a breach of integrity?::Unauthorized modification of data.
What is a breach of availability?::Unauthorized destruction or blocking of data or service.
What is theft of service?::Unauthorized use of resources.
What is denial of service?::Preventing legitimate use of a resource or service.
What is masquerading?::Pretending to be an authorized user.
What is a replay attack?::Reusing captured communication, possibly with modification.
What is a man-in-the-middle attack?::An intruder sits between sender and receiver and impersonates each side to the other.
What is session hijacking?::Intercepting an already established session to bypass authentication.
What is privilege escalation?::Gaining access beyond the rights a user or resource should have.
What are the main security levels in the notes?::Physical, application, operating system, and network.
Why are humans often the weakest security link?::Phishing and social engineering can bypass technical controls.
What usability problem can excessive security cause?::Users may create workarounds that weaken practical protection.
What is malware?::Software designed to exploit, disable, or damage a computer.
What is a Trojan horse?::A legitimate-looking program or code segment that misuses its environment.
What is spyware?::Software that captures user data or displays unwanted ads, often installed with legitimate software.
What is ransomware?::Malware that encrypts or locks data and demands payment.
What is a trap door or backdoor?::A hidden identifier, password, or path that bypasses normal security.
What is a remote access tool (RAT) in the security notes?::A tool left behind to allow repeated remote control.
What is code injection?::Adding or modifying executable code through a bug in otherwise non-malicious code.
What is a buffer overflow?::Writing beyond a buffer's bounds, often overwriting adjacent memory or control data.
How can a buffer overflow lead to privilege misuse?::Injected or redirected code runs with the vulnerable process's privileges.
What defenses help against buffer overflows?::Code review, bounds checking, non-executable stacks/pages, and disabling stack execution.
What is a virus?::A self-replicating code fragment embedded in a legitimate program.
What is a virus dropper?::Software that inserts a virus onto a system.
What is a polymorphic virus?::A virus that changes representation to avoid signature detection.
What is a worm?::A standalone program that spreads using network mechanisms.
How do viruses and worms differ?::Viruses attach to host programs; worms are standalone and spread through networks.
What is port scanning?::Automated attempts to connect to many ports/IPs to identify services and vulnerabilities.
What is a DDoS attack?::A denial-of-service attack launched from many sites at once.
What is a SYN flood?::A DoS attack exploiting TCP connection setup by consuming resources for half-open connections.
Why are network threats hard to contain?::Internet connectivity removes physical boundaries and IP addresses alone are weak identity.
What is cryptography?::Use of mathematical techniques and secrets to constrain message senders/receivers and create trust.
What is encryption?::Transforming plaintext into ciphertext so only key holders can recover the message.
What are plaintext and ciphertext?::Plaintext is the original readable message; ciphertext is the encrypted message.
What is a cryptographic key?::A secret or public/private value used by a cryptographic algorithm.
What are the encryption and decryption function types in the notes?::$E:K\rightarrow(M\rightarrow C)$ and $D:K\rightarrow(C\rightarrow M)$.
What is the essential encryption property?::Recovering plaintext from ciphertext should require the relevant key.
What is symmetric encryption?::The same secret key encrypts and decrypts.
What are examples of symmetric encryption algorithms in the notes?::DES, Triple-DES, AES, and RC4.
What is asymmetric encryption?::A public key encrypts and a private key decrypts.
Why is asymmetric encryption usually not used for bulk data?::It is computationally heavier than symmetric encryption.
What key sizes and block size does AES use in the notes?::AES uses 128-, 192-, or 256-bit keys and 128-bit blocks.
What is the RSA modulus formula?::$N=pq$ for large primes $p$ and $q$.
What RSA relationship must public and private exponents satisfy?::$k_ek_d \bmod ((p-1)(q-1))=1$.
What is RSA encryption in the notes?::$E_{k_e,N}(m)=m^{k_e}\bmod N$.
What is RSA decryption in the notes?::$D_{k_d,N}(c)=c^{k_d}\bmod N$.
For the toy RSA example $p=7$, $q=13$, what are $N$, public key, and private key?::$N=91$, public key $(5,91)$, private key $(29,91)$.
What is authentication?::Constraining and verifying the potential senders of a message.
What is an authenticator?::A value attached to a message to prove authenticity.
What is a hash function?::A function producing a small fixed-size message digest from a message.
What is collision resistance?::It is infeasible to find distinct messages with the same hash.
Why is a plain hash not enough for authentication?::An attacker can modify the message and recompute the public hash.
What is a MAC?::A cryptographic checksum generated from a message using a secret key.
What is a digital signature?::An authenticator produced with a private key and verifiable with a public key.
How do RSA-style signatures use keys?::The private key signs a hash; the public key verifies it.
What is non-repudiation?::Evidence that a sender cannot plausibly deny having produced a signed message.
What is a certificate authority (CA)?::A trusted party that signs public keys after verifying identity.
What is a digital certificate?::Proof that a public key belongs to an entity, signed by a trusted party.
Why are certificates needed for public-key systems?::They prevent man-in-the-middle substitution of unauthenticated public keys.
What is TLS/SSL used for?::Secure communication such as HTTPS.
Why does TLS use both asymmetric and symmetric cryptography?::Asymmetric crypto authenticates/establishes a session key; symmetric crypto handles bulk traffic efficiently.
What is a session key?::A temporary symmetric key used for one communication session.
How should passwords be stored?::With one-way hashing plus salt, not plaintext or reversibly encrypted passwords.
Why are salted hashes better than unsalted hashes?::They prevent identical passwords from producing identical stored values and weaken precomputed attacks.
What is multi-factor authentication?::Authentication requiring two or more independent factors.
What is defense in depth?::Using multiple security layers rather than relying on one control.
What is a security policy?::A statement of what is being secured and what rules apply.
What is vulnerability assessment?::Comparing real system state to the desired security policy.
What is intrusion detection?::Detecting attempted or successful intrusions.
How do signature-based and anomaly-based detection differ?::Signature-based detects known bad patterns; anomaly detection detects behavior different from normal.
What is a firewall?::A network or host control limiting access between security domains.
What are the firewall types in the notes?::Network firewall, personal firewall, application proxy firewall, and system-call firewall.
Why are firewalls not complete protection?::Allowed services, tunneling, spoofing, and compromised insiders can still bypass or abuse them.
What are the DoD security classification divisions in the notes?::D minimal, C discretionary/auditing, B sensitivity labels, and A formal design/verification.
What is a Windows SID?::A unique identifier for a Windows user or group.
What is a Windows access token?::An object containing a user's SID, group SIDs, and privileges for a process.
What is a Windows security descriptor?::Object metadata describing permissions.
How does Windows check object access?::It compares the process access token against the object's security descriptor.

## Protection

#flashcards/CSC3002F-Operating-Systems/ASLAM/07-Protection

What is protection?::Mechanisms ensuring each object is accessed correctly and only by processes allowed to do so.
How does protection differ from security?::Protection is access-control machinery; security is the broader defense goal.
What is an object in the protection model?::A hardware or software resource with a unique name and well-defined operations.
What is the principle of least privilege?::Programs, users, and systems should receive only the privileges required for their tasks.
What is compartmentalization?::Protecting individual system components with specific permissions and access restrictions.
What is an audit trail?::A record of protection-oriented activities.
How can least privilege be static or dynamic?::Static privileges stay fixed; dynamic privileges change through domain switching or privilege escalation.
What is the trade-off between fine-grained and coarse-grained privilege?::Fine-grained is more protective but complex; coarse-grained is simpler but grants more power.
What is a protection ring?::A hierarchical privilege level separating system components.
What is a gate in protection rings?::A controlled transfer path between protection levels.
What is a domain of protection?::A set of access rights defining resources a process may access.
What is an access right?::Permission to perform operations on an object.
What is domain switching?::Changing a process from one protection domain to another.
What is the access-right notation?::$\langle \text{object-name},\text{rights-set}\rangle$.
What is a domain in formal notation?::$\{\langle O_i,R_i\rangle\}$, a set of object/right pairs.
What can domains be associated with?::Users, processes, or procedures.
What is a UID?::A UNIX identifier representing a user or app domain.
What is the setuid bit?::A UNIX file bit that causes execution under the file owner's user ID.
What does `su` do?::It switches to another user's domain after password authentication.
What does `sudo` do?::It executes a command in another domain if policy permits.
How does Android isolate apps?::It assigns distinct UIDs/GIDs and private data directories to apps.
What is an access matrix?::A protection model with domains as rows and objects as columns.
What does `Access(i,j)` contain?::The operations a process in domain $D_i$ may invoke on object $O_j$.
What is the access-matrix allow rule?::Operation `op` is allowed iff $op\in Access(i,j)$.
How does the access matrix separate policy from mechanism?::The OS enforces matrix rules; users/admins decide who gets which rights.
What is an owner right?::A special right allowing a domain to define access rights for an object.
What is a copy right?::A right allowing a domain to copy an operation right to another entry.
What is a control right?::A right allowing a domain to modify another domain's access rights.
What is a transfer right?::A right allowing switching from one domain to another.
What is a global table implementation of the access matrix?::A table of triples $\langle$domain, object, rights-set$\rangle$.
What is an ACL?::A per-object list of domains and rights.
What is a capability list?::A per-domain list of objects and allowed operations.
What is a capability?::A protected object reference representing permission.
What is a lock-key scheme?::Objects have locks and domains have keys; access succeeds when a key matches a lock.
What is the main strength of ACLs?::They match user/object administration needs.
What is the main weakness of ACLs?::Per-access checks can be slow and domain rights are non-local.
What is the main strength of capability lists?::They localize rights for a process or domain.
What is the main weakness of capability lists?::Revocation can be inefficient if capabilities are widely distributed.
How can systems combine ACLs and capabilities?::Check an object's ACL on first access, attach a capability if allowed, then use the capability for repeated access.
What is revocation?::Removing a domain's access right to an object.
What are the four revocation design choices?::Immediate/delayed, selective/general, partial/total, and temporary/permanent.
Why is ACL revocation straightforward?::Remove the rights from the object's access list.
Why is capability revocation harder?::The system must find or invalidate all outstanding capabilities.
What methods can revoke capabilities?::Reacquisition, back-pointers, indirection through a global table, or keys/master keys.
What is RBAC?::Role-based access control, where permissions come through roles assigned to users.
What is DAC?::Discretionary access control, where users/admins set object permissions.
What is MAC?::Mandatory access control, where system policy and labels enforce access even against privileged users.
What is a label in MAC?::Metadata assigned to a subject or object for policy decisions.
What are examples of MAC systems in the notes?::Trusted Solaris, TrustedBSD/macOS, SELinux, and Windows integrity controls.
What are POSIX-style capabilities?::Separate bits that slice root powers into permitted, effective, and inheritable sets.
Why do POSIX capabilities implement least privilege better than all-or-nothing root?::A process can receive only the specific root-like powers it needs.
What is macOS System Integrity Protection (SIP)?::Protection restricting access to system files/resources even by root.
What is system-call filtering?::Restricting which system calls a process may execute, possibly with argument inspection.
What is sandboxing?::Running a process in a limited environment with irremovable restrictions.
What is code signing?::Signing executable code with a cryptographic hash so modification invalidates trust.
What does code signing prove and not prove?::It proves origin/integrity, not that code is safe or correct.
What is language-based protection?::Enforcing protection policies through programming-language or runtime checks.
How does Java provide language-based protection?::The JVM assigns protection domains, checks type safety, and uses stack inspection for privileged operations.
What does Java stack inspection check?::Whether the call chain is allowed to perform a privileged operation.

## Processes

#flashcards/CSC3002F-Operating-Systems/MICHEL/01-Processes

What is a program?::A passive set of instructions stored on disk.
What is a process?::A program in execution, with resources and protection.
What is a thread?::A single path of execution within a process.
How do program, process, and thread differ?::A program is passive code; a process is running code with its own address space/resources; a thread is one execution path sharing its process address space.
What do threads in the same process share?::Code, heap, global data, and open files.
What does each thread have for itself?::Program counter, registers, and stack.
Why does Chrome use multiple processes?::Process isolation contains crashes and malicious scripts better than a single-process browser design.
What is a PID?::A unique number used by the OS to identify a process.
What is a parent process?::A process that creates another process.
What is a child process?::A process created by a parent.
What is a process tree?::The parent-child hierarchy of processes.
What is `systemd`?::The Linux PID 1 style process that starts/adopts system processes.
What is `launchd`?::The macOS PID 1 style system launcher.
What is a daemon?::A background process that runs without user intervention.
What commands inspect Linux process trees?::`ps -A --forest`, `ps -aef`, and `pstree`.
What are common daemons and their purposes?::`sshd` remote shell, `httpd` web serving, `rsyslogd` logs, and `cron` scheduled tasks.
How are PIDs commonly allocated?::Sequentially with wraparound while skipping still-used PIDs, though some systems randomize.
What are the main boot steps into process creation?::Firmware starts bootstrap, hardware initializes, kernel loads, root filesystem mounts, PID 1 starts, daemons launch.
What is execution context?::The state needed to resume a process, including PC, registers, memory map, and resources.
What is the text segment?::Compiled program code in memory.
What is the stack used for?::Function parameters, return addresses, local variables, and temporary data.
What is the heap used for?::Dynamically allocated runtime memory.
How do stack and heap lifetimes differ?::Stack variables are tied to scope and automatic; heap allocations can outlive scope and need explicit/free or garbage-collected management.
What is stack overflow?::Failure when the call stack exceeds its bound.
What is heap exhaustion?::Failure when dynamic allocation cannot obtain more heap memory.
Why can creating many threads exhaust memory?::Each thread needs execution state and its own stack.
What is a process table?::An OS-maintained list or table of active process records.
What is a PCB?::The kernel data structure representing one process.
What fields are commonly stored in a PCB?::Process state, program counter, registers, scheduling info, memory info, accounting info, I/O status, devices, and open files.
How do multithreaded OSes split state?::Per-process resources are separated from per-thread execution state.
What is Linux's PCB-like structure called?::`task_struct`.
What is `fork()`?::A UNIX system call that creates a new process by duplicating the caller.
What is copy-on-write?::Parent and child initially share physical pages until one writes.
What does `fork()` return in the parent?::The child's PID.
What does `fork()` return in the child?::0.
What does `fork()` return on error?::-1.
What is true about parent and child after `fork()`?::They have the same code after the fork, different PIDs, different return values, logically separate address spaces, and unspecified run order.
How many processes exist after $k$ unconditional forks?::$2^k$ total processes.
What does `exec()` do?::It replaces the current process memory image with a new program.
Does `exec()` create a new process?::No; it replaces the current process image and keeps the same PID.
What is the usual UNIX `fork()`/`exec()` pattern?::Parent forks; child gets 0 and execs a new program; parent may wait.
How does Windows typically differ from UNIX creation/loading?::Windows `CreateProcess` combines process creation and program loading.
What are the five classic process states?::New, ready, running, waiting, and terminated.
What is the ready state?::The process is in memory and waiting for a processor.
What is the waiting state?::The process waits for an event such as I/O completion.
What is a context switch?::Saving one process's context and loading another's.
Why is context switching overhead?::The kernel saves/restores state and chooses another process, but no user work completes during the switch.
What is a job queue?::All processes in the system.
What is a ready queue?::Processes in main memory ready and waiting to execute.
What is a device queue?::Processes waiting for a particular I/O device.
How do iOS and Android differ in background execution?::iOS strongly restricts background work; Android permits more flexible background services.
What is an independent process?::A process that does not share data with other processes.
What is a cooperating process?::A process that communicates with other processes.
What is IPC?::OS-supported communication between processes.
What is shared-memory IPC?::Processes read/write a shared memory region.
What is a pipe?::A unidirectional transient data channel between two processes.
What is message passing?::Processes explicitly send and receive messages through the OS.
What is a socket?::A bidirectional endpoint for same-machine or network communication.
What is RPC?::Calling a function in another process or machine as if it were local.
What is the main advantage and caution of shared memory?::It is fast but requires synchronization.
What does `cat file1.txt | sort` illustrate?::A shell pipeline using a pipe from `cat` to `sort`.
What is normal process exit?::Termination after the last statement or `exit()`.
What is abnormal termination?::Termination due to error, exception, signal, or forced stop.
What is an orphan process?::A child whose parent terminates first.
What is a zombie process?::A terminated child whose parent has not yet collected its exit status.
What is reaping?::Collecting a terminated child's exit status and allowing its PCB/PID entry to be removed.
Why does the OS keep zombie entries temporarily?::So the parent can get exit status, PID is not reused too early, and `wait()` targets the correct child.

## Process Scheduling

#flashcards/CSC3002F-Operating-Systems/MICHEL/02-Process-Scheduling

What is a processor scheduling policy?::The rule deciding which runnable process or thread runs next.
What is a CPU burst?::A period where a process/thread uses the CPU before blocking or yielding.
What is an I/O-bound process?::A process with many short CPU bursts and frequent I/O waits.
What is a CPU-bound process?::A process with few long CPU bursts.
What is preemptive scheduling?::Scheduling where the OS can take the CPU away from a running process.
What is non-preemptive or cooperative scheduling?::Scheduling where a process keeps the CPU until it blocks, yields, or terminates.
What ready-queue structures are used by different schedulers?::FIFO queues, priority queues, trees, or unordered linked lists.
When can scheduling occur?::Running to waiting, running to ready, waiting to ready, or running to terminated.
Which scheduling transition cases define non-preemptive scheduling?::Scheduling only on running-to-waiting and running-to-terminated.
Why does preemptive scheduling introduce concurrency hazards?::Shared data can be interrupted mid-update.
What is a voluntary context switch?::A switch where a process gives up the CPU because it needs an unavailable resource.
What is a nonvoluntary context switch?::A switch where the CPU is taken away, such as timer expiry or higher-priority preemption.
What is CPU utilization?::The fraction of time the CPU is busy.
What is throughput?::The number of processes completed per unit time.
What is turnaround time?::Time from process submission/arrival to completion.
What is waiting time?::Total time a process spends waiting in the ready queue.
What is response time?::Time from request submission until the first response.
What is starvation?::Indefinite waiting because a process is continually denied CPU/resource access.
What scheduling criteria are usually maximized?::CPU utilization and throughput.
What scheduling criteria are usually minimized?::Turnaround time, waiting time, response time, jitter, and scheduler overhead.
What does Little's Law state?::$L=\lambda W$.
In Little's Law, what do $L$, $\lambda$, and $W$ mean?::$L$ is average queue length, $\lambda$ is average arrival rate, and $W$ is average waiting time.
What is FCFS scheduling?::Non-preemptive scheduling where the head of the FIFO ready queue runs next.
What is the convoy effect?::Short processes wait behind a long process, hurting response time and utilization.
What is FCFS's main strength and weakness?::It is simple and fair by arrival order, but can have poor response time and convoy effects.
For FCFS bursts 24,3,3 in order P1,P2,P3, what is average waiting time?::$(0+24+27)/3=17$.
For FCFS bursts 24,3,3 in order P2,P3,P1, what is average waiting time?::$(0+3+6)/3=3$.
What is SJF scheduling?::Scheduling that chooses the process with the shortest next CPU burst.
What is SRTF scheduling?::Preemptive SJF where a newly arrived shorter remaining burst can preempt the current process.
Why is ideal SJF not directly implementable?::The OS cannot know exact future CPU burst lengths.
What is exponential averaging for burst prediction?::$\tau_{n+1}=\alpha t_n+(1-\alpha)\tau_n$.
What happens when $\alpha=0$ in burst prediction?::Recent actual bursts are ignored.
What happens when $\alpha=1$ in burst prediction?::Only the most recent actual burst counts.
What is the SJF order for bursts P1=6, P2=8, P3=7, P4=3?::P4, P1, P3, P2.
What is the average waiting time for that SJF example?::$(0+3+9+16)/4=7$.
What average waiting times are compared in the SRTF arrival example?::Preemptive SJF 6.5, non-preemptive SJF 7.75, and FCFS 8.75.
What is Round Robin scheduling?::Preemptive scheduling where each process receives up to one time quantum, then returns to the ready queue if unfinished.
What is a time quantum?::The maximum CPU time slice before preemption.
What happens as the RR quantum becomes very large?::RR approaches FCFS.
What happens if the RR quantum is too small?::Too many context switches create high overhead.
What is the source rule of thumb for RR quantum choice?::About 80 percent of CPU bursts should be shorter than the quantum.
For RR with q=4 and bursts 24,3,3, what are source waiting times?::P1=6, P2=4, P3=7, average 17/3 = 5.66.
What is priority scheduling?::Scheduling where the highest-priority process runs next.
What is aging in scheduling?::Gradually increasing a waiting process's priority to prevent starvation.
How is SJF a form of priority scheduling?::Priority is the inverse of predicted next CPU burst length.
What is multilevel queue scheduling?::Scheduling with separate queues for classes/priorities where a process stays in its assigned queue.
What is multilevel feedback queue scheduling?::Scheduling where processes can move between queues based on behavior.
What are key parameters of a multilevel feedback queue?::Number of queues, algorithm per queue, upgrade rule, demotion rule, and entry rule.
What is Linux CFS?::The Completely Fair Scheduler, which allocates CPU proportionally using virtual runtime.
What is a scheduling class in Linux?::A category of tasks with a priority ordering.
What is a nice value?::Linux user-visible priority adjustment from -20 to +19, where lower is higher priority.
What is targeted latency in CFS?::The time interval in which every runnable task should run at least once.
What is `vruntime`?::Runtime scaled by task weight/nice value.
Which task does CFS pick next?::The runnable task with the smallest `vruntime`, the leftmost node in the red-black tree.
How does priority affect `vruntime` accumulation?::Higher-priority tasks accumulate `vruntime` more slowly; lower-priority tasks accumulate it faster.
What is SMT?::Simultaneous multithreading, where one core can run multiple hardware threads at once.
What is memory stall?::Time a processor waits for memory data.
Why can CMT/SMT improve utilization?::Another hardware thread can run while one waits for memory.
What is load balancing?::Moving work so processors have approximately equal load.
What is processor affinity?::Keeping a thread on the same processor/core to preserve cache locality.
What is NUMA?::Non-uniform memory access, where memory access time depends on processor/socket location.
How do push and pull migration differ?::Push migration moves tasks from overloaded CPUs; pull migration lets idle CPUs take work.
What is the main multicore scheduling trade-off?::Balancing load while preserving cache affinity and NUMA locality.
What is the turnaround-time formula?::$T_i=C_i-A_i$.
What is the average waiting-time formula?::$\bar W=\sum_i W_i/n$.

## Process Synchronization

#flashcards/CSC3002F-Operating-Systems/MICHEL/03-Process-Synchronization

What are concurrent events?::Events where we cannot tell which will happen first.
What is a race condition?::Correctness depends on timing or interleaving.
What is a data race?::Unsynchronized concurrent access to the same memory location, with at least one write.
What is a synchronization constraint?::A requirement about event order or access to shared state.
What is mutual exclusion?::Only one thread/process may execute a critical section at a time.
What is an atomic operation?::An operation that executes indivisibly with no visible intermediate state.
Why are race conditions hard to reproduce?::They depend on unpredictable interleavings, cache misses, page faults, and scheduler preemption.
What is signaling as a synchronization constraint?::Event $a_1$ must happen before event $b_1$.
What is rendezvous as a synchronization constraint?::$a_1$ before $b_2$ and $b_1$ before $a_2$.
What is a barrier?::All threads wait until all have arrived.
What is a reusable barrier?::A barrier that can be used more than once.
What is a multiplex?::A critical section that permits at most $n$ threads.
What is liveness?::The requirement that processes or threads eventually make progress.
What is deadlock in synchronization?::Two or more threads permanently wait for each other, so none progresses.
What is starvation?::A thread waits indefinitely because others keep getting the resource.
What is livelock?::Threads keep changing state in response to each other but make no useful progress.
How do deadlock, starvation, and livelock differ?::Deadlock has stuck threads; starvation lets others progress while one waits; livelock has activity without useful progress.
What is the bounded-buffer problem?::Producers add items and consumers remove items while respecting empty/full and mutual exclusion.
What are the producer-consumer constraints?::Protect the buffer, do not consume empty, and do not produce into full.
What is the readers-writers problem?::Many readers may read concurrently, but writers require exclusive access.
What is the dining philosophers problem?::Philosophers need two neighboring chopsticks, illustrating deadlock and starvation risks.
What is `test-and-set()`?::An atomic instruction that reads a Boolean and sets it to true in one indivisible action.
What is compare-and-swap (CAS)?::An atomic instruction that changes a value only if it still equals an expected value.
What is an atomic variable?::A variable whose updates are guaranteed atomic.
Why do atomic variables not solve every concurrency problem?::They protect single-variable updates, not compound invariants across multiple variables.
What is a mutex lock?::A lock enforcing mutual exclusion with `acquire()` and `release()`.
What is a spinlock?::A lock where waiting threads busy-wait until it becomes available.
What is busy waiting?::Repeatedly checking a condition until it changes.
When are spinlocks useful?::On multiprocessors when the lock is held for less than about two context switches.
Why are spinlocks bad for long critical sections?::They waste CPU cycles while waiting.
What is a semaphore?::An integer synchronization variable accessed only through atomic `wait()` and `signal()`.
What does `wait()`/P()/acquire() do to a semaphore?::It decrements a permit or waits until one is available.
What does `signal()`/V()/release() do to a semaphore?::It increments a permit and may wake a waiter.
What is a binary semaphore?::A semaphore restricted to values 0 and 1.
What is a counting semaphore?::A semaphore with an unrestricted integer value.
What does a positive semaphore value mean?::The number of permits available.
What does a zero semaphore value mean?::No permits are available; callers wait.
For a multiplex allowing at most $n$ threads, what is the initial semaphore value?::$n$.
How do practical semaphores avoid busy waiting?::They block waiting threads and later wake them into the ready queue.
How do you use a semaphore for signaling?::Initialize it to 0; A signals after event $a_1$, B waits before event $b_1$.
What are the standard producer-consumer semaphores and initial values?::`mutex=1`, `full=0`, and `empty=n`.
What does `mutex` protect in producer-consumer?::The buffer structure and pointer updates.
What does `full` count in producer-consumer?::Occupied buffer slots.
What does `empty` count in producer-consumer?::Free buffer slots.
What is the producer semaphore order?::Produce item, wait(empty), wait(mutex), add item, signal(mutex), signal(full).
What is the consumer semaphore order?::Wait(full), wait(mutex), remove item, signal(mutex), signal(empty), consume item.
Why is one mutex alone not enough for a bounded buffer?::It protects structure but does not express empty/full availability constraints.
What is reader preference?::Readers are not kept waiting unless a writer already has permission to write.
What is writer preference?::Once a writer is ready, it writes as soon as possible.
What is the lightswitch pattern?::The first entrant locks a shared resource and the last leaver unlocks it.
In reader-preference readers-writers, why does only the first reader lock `rw_mutex`?::The first reader blocks writers; later readers can join while that protection is active.
In reader-preference readers-writers, why does only the last reader signal `rw_mutex`?::Only when read_count reaches 0 can writers safely enter.
What is the starvation risk in reader-preference readers-writers?::Writers may starve if readers keep arriving.
What is deadlock freedom?::A guarantee that the relevant threads cannot all become permanently stuck.
What is starvation freedom?::A guarantee that every waiting/hungry thread eventually gets a turn.
Why can naive dining philosophers deadlock?::Each philosopher can hold one chopstick while waiting for the next, forming a circular wait.
Name three deadlock-avoidance strategies for dining philosophers.::Allow at most four at the table, pick up both chopsticks only if both are available, or use asymmetric acquisition order.
Why does deadlock freedom not imply starvation freedom?::A solution may avoid total cycles while still denying one participant indefinitely.
What happens if `wait(mutex)` and `signal(mutex)` are inverted?::Critical-section violation.
What happens if `signal(mutex)` is replaced with `wait(mutex)`?::Deadlock.
What happens if `wait(mutex)` is omitted?::Mutual exclusion may be violated.
What happens if `signal(mutex)` is omitted?::Deadlock or permanent blocking can occur.
What is a monitor?::A high-level abstraction where internal variables are accessed only through monitor procedures and one process is active at a time.
What is a condition variable?::A synchronization variable supporting `wait()` and `signal()`/notification for condition-based waiting.
What is Java's entry set?::Threads waiting to acquire an object's lock.
What is Java's wait set?::Threads that called `wait()` on the object.
What does a Java `synchronized` method require?::The caller must own the object's intrinsic lock.
What happens when a Java thread calls `wait()`?::It releases the lock, blocks in the wait set, and must reacquire the lock after notification.
What does Java `notify()` do?::Moves an arbitrary waiting thread from the wait set to the entry set and marks it runnable.
Why should Java `wait()` be inside a `while` loop?::Because of spurious wakeups and because state may change before the awakened thread reacquires the lock.
What synchronization tools does Linux provide?::Semaphores, atomic integers, mutexes, spinlocks, and reader-writer locks.
Why does the Linux kernel need synchronization internally?::It is fully preemptive, so kernel code can have race conditions.
What is the lost-update race example result?::Two increments from 0 can end at 1 if both read 0 before either write is observed.
What is the circular-buffer full condition from the notes?::`(in + 1) mod BUFFER_SIZE = out`.

## Deadlock

#flashcards/CSC3002F-Operating-Systems/MICHEL/04-Deadlock

What is a safety property?::A property that must always be true.
What is a liveness property?::A property that must eventually become true.
What is deadlock?::A set of threads/processes where every member waits for an event that can be caused only by another member of the set.
What is a resource in deadlock analysis?::A finite system item used by processes/threads, such as CPU cycles, files, I/O devices, locks, semaphores, memory, disk blocks, or buffers.
What is the normal resource-use sequence?::Request, use, release.
Why may testing fail to discover deadlock?::Deadlock can depend on rare interleavings or workloads.
What are the four necessary conditions for deadlock?::Mutual exclusion, hold and wait, no preemption, and circular wait.
What is mutual exclusion in deadlock?::At least one resource can be used by only one process at a time.
What is hold and wait?::A process holds at least one resource while waiting for additional resources held by others.
What is no preemption?::A resource can be released only voluntarily by the process holding it.
What is circular wait?::A cycle of processes where each waits for a resource held by the next process.
What is the formal circular-wait shape?::$P_0\rightarrow P_1\rightarrow \cdots \rightarrow P_n\rightarrow P_0$.
What is a resource-allocation graph (RAG)?::A directed graph with process nodes, resource-type nodes, request edges, and assignment edges.
What is a request edge in a RAG?::$P_i\rightarrow R_j$, meaning process $P_i$ waits for resource $R_j$.
What is an assignment edge in a RAG?::$R_j\rightarrow P_i$, meaning an instance of $R_j$ is allocated to $P_i$.
What are the RAG vertex sets?::$V=P\cup R$, where $P$ is processes and $R$ is resource types.
What happens to a RAG edge when a request is fulfilled?::The request edge is transformed into an assignment edge.
What can you conclude from no cycle in a RAG?::No deadlock.
What can you conclude from a cycle when each resource type has one instance?::Deadlock exists.
What can you conclude from a cycle when resource types may have multiple instances?::Deadlock is possible but not guaranteed.
Why is a RAG cycle not always deadlock with multiple instances?::Another instance may become available from outside the cycle.
What are the four broad deadlock-handling strategies?::Ignore, prevent, avoid, or detect and recover.
Why do many general-purpose OSes not solve all deadlocks globally?::Prevention/avoidance can reduce utilization, require advance information, and add overhead.
What is deadlock prevention?::Structuring the system so at least one necessary deadlock condition cannot hold.
What is deadlock avoidance?::Dynamically deciding whether resource requests are safe before granting them.
What is deadlock detection?::Allowing deadlock to occur, then finding it.
What is deadlock recovery?::Breaking a detected deadlock.
Which necessary condition is most practical to break for prevention?::Circular wait, usually through global resource ordering.
What is resource ordering?::Assigning a global order to resources and requiring processes to acquire resources in increasing order.
How does ordered locking prevent deadlock?::All waits move in one global direction, so circular wait cannot form.
Why is breaking mutual exclusion usually impractical?::Many resources require exclusive use for correctness.
Why is breaking hold-and-wait often impractical?::It can lower utilization and cause starvation.
Why is breaking no-preemption often impractical?::Many resources cannot be safely taken away.
What is a safe state?::A state where there exists an order in which all processes can finish.
What is an unsafe state?::A state where no safe sequence is guaranteed; deadlock is possible.
What is a safe sequence?::An ordering where each process can obtain remaining resources from current availability plus resources released by earlier processes.
What is the avoidance grant rule?::Pretend to grant the request, check whether the resulting state is safe, and grant only if safe.
Why can avoidance reduce utilization?::An available resource may be withheld because granting it would make the state unsafe.
What is a claim edge?::A dashed edge showing that a process may request a resource in the future.
For single-instance RAG avoidance, when is a request granted?::Only if converting the request edge to an assignment edge creates no cycle.
What is the cycle-detection cost for RAG avoidance in the notes?::About $O(n^2)$.
What is Banker's Algorithm?::A deadlock-avoidance algorithm for multiple resource instances using declared maximum demands.
What is the Available vector?::For each resource type, the number of currently free instances.
What is the Max matrix?::Each process's declared maximum demand for each resource type.
What is the Allocation matrix?::The current allocation of each resource type to each process.
What is the Need matrix?::The remaining possible need of each process.
What is the Banker's Algorithm Need formula?::$Need[i,j]=Max[i,j]-Allocation[i,j]$.
What assumptions does Banker's Algorithm make?::Processes declare maximum needs in advance and return resources in finite time after receiving what they need.
How does the Banker's safety check initialize?::Set `Work = Available` and `Finish[i] = false` for every process.
What condition lets process $P_i$ finish in the safety check?::$Finish[i]=false$ and $Need_i \le Work$ componentwise.
What happens when a process can finish in the safety check?::Set `Work = Work + Allocation_i` and `Finish[i] = true`.
When is the system safe in the Banker's safety check?::All `Finish[i]` values become true.
What is the safety-check time complexity in the notes?::On the order of $O(mn^2)$.
What is a request vector?::`Request_i[j]=k` means process $P_i$ asks for $k$ instances of resource $R_j$.
What are the three checks before granting a Banker's request?::$Request_i\le Need_i$, $Request_i\le Available$, and the state remains safe after pretend allocation.
What happens if $Request_i\nleq Need_i$?::Raise an error because the process exceeded its declared maximum.
What happens if $Request_i\nleq Available$?::The process must wait because resources are not currently available.
What pretend-allocation updates are made in Banker's request check?::Available -= Request, Allocation_i += Request, Need_i -= Request.
What is a wait-for graph?::A process-only graph with $P_i\rightarrow P_j$ when $P_i$ waits for $P_j$.
For single-instance resources, what does a cycle in the wait-for graph mean?::Deadlock.
What is a victim in deadlock recovery?::A process selected to abort or roll back.
What is rollback?::Returning a process or system to a previous safe state.
What is a transaction?::An operation sequence that commits completely or aborts as if it did not happen.
What are recovery options after detection?::Abort all deadlocked processes, abort one at a time, roll back, or restart victims.
What should victim selection minimize?::Cost, considering priority, work done, resources held, remaining needs, and previous rollbacks.
How can deadlock recovery cause starvation?::If the same process is repeatedly chosen as victim.
What command can help inspect Java deadlocks?::`jstack -l <pid>`.
What is the gotcha about unsafe states?::Unsafe does not mean deadlocked; it means deadlock is possible.
What is the gotcha about available resources in avoidance?::Availability alone is not enough; the resulting state must be safe.
