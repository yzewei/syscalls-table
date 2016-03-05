# System calls table on different architectures

## What and why?

Linux kernel has set of system calls (called syscalls in short) offerred for userspace. 
Each architecture can support them but the numbers they use for their identification can
vary between archs.

And those numbers can be important for some projects (like Valgrind for example).

## How to help?

Clone repo, run "make" to generate C source, compile it and run. You can substitute 
C compiler with "CC" variable. Result will be "tables/syscalls-ARCHNAME" which you
need to send back to me (preferred way is by pull request). ARCHNAME == "uname -m"

## Where to see?

I keep copy at https://fedora.juszkiewicz.com.pl/syscalls.html page.
