0. 为什么要重写**equals**方法和**hashCode**方法


1. 为什么重写**equals**方法前必须先重写**hashCode**方法


2. Java线程有几种状态

> A thread state. A thread can be in one of the following states:
> 
> **NEW**
> 
> A thread that has not yet started is in this state.
> 
> **RUNNABLE**
> 
> A thread executing in the Java virtual machine is in this state.
> 
> **BLOCKED**
> 
> A thread that is blocked waiting for a monitor lock is in this state.
> 
> **WAITING**
> 
> A thread that is waiting indefinitely for another thread to perform a particular action is in this state.
> 
> **TIMED_WAITING**
> 
> A thread that is waiting for another thread to perform an action for up to a specified waiting time is in this state.
> 
> **TERMINATED**
> 
> A thread that has exited is in this state.
> 
> A thread can be in only one state at a given point in time. These states are virtual machine states which do not reflect any operating system thread states.