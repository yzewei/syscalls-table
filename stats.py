#!/usr/bin/python3

from parser import load_syscall_data

[syscalls, present_archs] = load_syscall_data()

popular_syscalls = {}

for syscall in sorted(syscalls.keys()):

    try:
        popular_syscalls[len(syscalls[syscall])].append(syscall)
    except KeyError:
        popular_syscalls[len(syscalls[syscall])] = []
        popular_syscalls[len(syscalls[syscall])].append(syscall)

for amount in range(1, len(present_archs) + 1):
    try:
        tmp = popular_syscalls[amount]
        print(f"System calls supported on {amount} architectures:")
        for syscall in popular_syscalls[amount]:
            print(f"\t{syscall}")
        print("\n")
    except KeyError:
        pass
