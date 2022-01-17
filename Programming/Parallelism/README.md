# Overview

There are several methods for parallelizing code. On this page We will review the high level prerequisite terminology before diving deeper. In this folder we have notebooks that demonstrate specific techniques. 

## Terminology and Definitions

An operating system is in charge of allocating resources for programs. Programs are implimented as processes and threads.

### Processes
Processes are instances of a program. The OS allocates physical resources (memory and CPU)  for the process to use exclusively. Once allocated the process can utilize the resources as it likes. Multiprocessing is when a program asks the OS to spin up multiple "subprocesses" each with their own separate memory and cpu allocations provides by the operating system. We thusly refer to these processes as the parent process and the set of child processes.

We will see that there are some advanced libraries for managing processes as well as sharring information between them and synchronizing them.

### Threads
Threads are instances of a code segment. Threads are created by processes. Threads are managed by the process (and thus the OS). Once allocated the thread is able to consume the resources allotcated to the process. Multithreading is when a single process creates multiple threads to execute work in parrallel instead of multiple processes.

We will see that there are some advanced libraries for managing threads as well as sharring information between them and synchronizing them.

### Pools
In modern implimentations, the developer has access to Pools. These are manager objects which simplify the use of multiple threads. We will see that there is a ThreadPool and ProcessPool object which allow us to spin up multiple instances of parallel compute with a common interface.

### Asynchronous and Synchronous Programming
When processes execute in parallel, the program (or segment of execution) is referred to as being asynchronous. The operations being performed are generally/clasically considered to be independent. As such, there is no synchronization between them. Synchronization refers to some sort of coordination such that the operations occur in a predefined order or relation. For example, we may have 10 processes working in parallel, but only one of them can write data to a file at a given time. Another example would be that we have 100 workers performing three types of work and due to system limitations, only a certain number of workers can perform each type of work at a given time.

In order for processes/threads to be synchronized in this manner we need to be able to send and receive signals between processes and threads. To help with this there are several classical solutions that exist. The simplest is the mutex pattern. Commonly referred to a lock, the mutex acts similar to that of token/ring programming. Then processes/threads need to access a shared resource they must first acquire the mutex. The mutex is such that it only allows a single thread/process to acquire it at a given point in time. Using this pattern, we guarantee that only one process can access the shared resource at a time. 

A semaphore is a more generalized mutex which allows a predefined finite number of processes/threads to acquire the lock at a given time.

Deadlocks are situations where a parallel set of operations cannot complete because of a circular dependency. An error in the lock management may be a cause for such a situation.

### Shared and Non-Shared Memory
In some cases we may want to share information between threads/processes. This is referred to as shared memory. We are using a section of memory allocated to the process to be used by all the parallel entities.

Non-shared memory is that which is only allocated for and accessible by the single thread/process in question.

## Notebooks
To demonstrate these concepts I have prepared the following notebooks:

- [Multithreading]()
- [Multiprocessing]()

We will see that sharring memory and synchronization between threads and processes is slightly different. Converniently, the objects for managing Pools is consistent.