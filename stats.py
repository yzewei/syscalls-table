#!/usr/bin/python3

import json

from parser import load_syscall_data

[syscalls, present_archs] = load_syscall_data()

popular_syscalls = {}

for syscall in sorted(syscalls.keys()):

    try:
        popular_syscalls[len(syscalls[syscall])] += f" {syscall}"
    except KeyError:
        popular_syscalls[len(syscalls[syscall])] = syscall

print(json.dumps(popular_syscalls, sort_keys=True, indent=4))
