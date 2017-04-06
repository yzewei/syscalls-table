# System calls table on different architectures

## What and why?

Linux kernel has set of system calls (called syscalls in short) offerred for userspace. 
Each architecture can support them but the numbers they use for their identification can
vary between archs.

And those numbers can be important for some projects (like Valgrind for example).

## How to help?

Check issues list and work on any of them.

## Where to see?

I keep copy at https://fedora.juszkiewicz.com.pl/syscalls.html page.

## How to run

"make KERNELSRC=<path to Linux kernel tree>"

It will run through all supported architectures. Any new system call will be added to the
list. You can check that with "git diff syscall-names.text" - if there are any new ones
then you have to run "make" for second time to make sure that all architectures are
checked for new syscall.
