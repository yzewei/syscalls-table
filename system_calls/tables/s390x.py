# Content autogenerated. Do not edit.

syscalls_s390x = {
    "_sysctl": 149,
    "accept4": 364,
    "access": 33,
    "acct": 51,
    "add_key": 278,
    "adjtimex": 124,
    "alarm": 27,
    "bdflush": 134,
    "bind": 361,
    "bpf": 351,
    "brk": 45,
    "cachestat": 451,
    "capget": 184,
    "capset": 185,
    "chdir": 12,
    "chmod": 15,
    "chown": 212,
    "chroot": 61,
    "clock_adjtime": 337,
    "clock_getres": 261,
    "clock_gettime": 260,
    "clock_nanosleep": 262,
    "clock_settime": 259,
    "clone": 120,
    "clone3": 435,
    "close": 6,
    "close_range": 436,
    "connect": 362,
    "copy_file_range": 375,
    "creat": 8,
    "create_module": 127,
    "delete_module": 129,
    "dup": 41,
    "dup2": 63,
    "dup3": 326,
    "epoll_create": 249,
    "epoll_create1": 327,
    "epoll_ctl": 250,
    "epoll_pwait": 312,
    "epoll_pwait2": 441,
    "epoll_wait": 251,
    "eventfd": 318,
    "eventfd2": 323,
    "execve": 11,
    "execveat": 354,
    "exit": 1,
    "exit_group": 248,
    "faccessat": 300,
    "faccessat2": 439,
    "fadvise64": 253,
    "fallocate": 314,
    "fanotify_init": 332,
    "fanotify_mark": 333,
    "fchdir": 133,
    "fchmod": 94,
    "fchmodat": 299,
    "fchmodat2": 452,
    "fchown": 207,
    "fchownat": 291,
    "fcntl": 55,
    "fdatasync": 148,
    "fgetxattr": 229,
    "finit_module": 344,
    "flistxattr": 232,
    "flock": 143,
    "fork": 2,
    "fremovexattr": 235,
    "fsconfig": 431,
    "fsetxattr": 226,
    "fsmount": 432,
    "fsopen": 430,
    "fspick": 433,
    "fstat": 108,
    "fstatfs": 100,
    "fstatfs64": 266,
    "fsync": 118,
    "ftruncate": 93,
    "futex": 238,
    "futex_waitv": 449,
    "futimesat": 292,
    "get_kernel_syms": 130,
    "get_mempolicy": 269,
    "get_robust_list": 305,
    "getcpu": 311,
    "getcwd": 183,
    "getdents": 141,
    "getdents64": 220,
    "getegid": 202,
    "geteuid": 201,
    "getgid": 200,
    "getgroups": 205,
    "getitimer": 105,
    "getpeername": 368,
    "getpgid": 132,
    "getpgrp": 65,
    "getpid": 20,
    "getpmsg": 188,
    "getppid": 64,
    "getpriority": 96,
    "getrandom": 349,
    "getresgid": 211,
    "getresuid": 209,
    "getrlimit": 191,
    "getrusage": 77,
    "getsid": 147,
    "getsockname": 367,
    "getsockopt": 365,
    "gettid": 236,
    "gettimeofday": 78,
    "getuid": 199,
    "getxattr": 227,
    "idle": 112,
    "init_module": 128,
    "inotify_add_watch": 285,
    "inotify_init": 284,
    "inotify_init1": 324,
    "inotify_rm_watch": 286,
    "io_cancel": 247,
    "io_destroy": 244,
    "io_getevents": 245,
    "io_pgetevents": 382,
    "io_setup": 243,
    "io_submit": 246,
    "io_uring_enter": 426,
    "io_uring_register": 427,
    "io_uring_setup": 425,
    "ioctl": 54,
    "ioprio_get": 283,
    "ioprio_set": 282,
    "ipc": 117,
    "kcmp": 343,
    "kexec_file_load": 381,
    "kexec_load": 277,
    "keyctl": 280,
    "kill": 37,
    "landlock_add_rule": 445,
    "landlock_create_ruleset": 444,
    "landlock_restrict_self": 446,
    "lchown": 198,
    "lgetxattr": 228,
    "link": 9,
    "linkat": 296,
    "listen": 363,
    "listxattr": 230,
    "llistxattr": 231,
    "lookup_dcookie": 110,
    "lremovexattr": 234,
    "lseek": 19,
    "lsetxattr": 225,
    "lstat": 107,
    "madvise": 219,
    "mbind": 268,
    "membarrier": 356,
    "memfd_create": 350,
    "memfd_secret": 447,
    "migrate_pages": 287,
    "mincore": 218,
    "mkdir": 39,
    "mkdirat": 289,
    "mknod": 14,
    "mknodat": 290,
    "mlock": 150,
    "mlock2": 374,
    "mlockall": 152,
    "mmap": 90,
    "mount": 21,
    "mount_setattr": 442,
    "move_mount": 429,
    "move_pages": 310,
    "mprotect": 125,
    "mq_getsetattr": 276,
    "mq_notify": 275,
    "mq_open": 271,
    "mq_timedreceive": 274,
    "mq_timedsend": 273,
    "mq_unlink": 272,
    "mremap": 163,
    "msgctl": 402,
    "msgget": 399,
    "msgrcv": 401,
    "msgsnd": 400,
    "msync": 144,
    "munlock": 151,
    "munlockall": 153,
    "munmap": 91,
    "name_to_handle_at": 335,
    "nanosleep": 162,
    "newfstatat": 293,
    "nfsservctl": 169,
    "nice": 34,
    "open": 5,
    "open_by_handle_at": 336,
    "open_tree": 428,
    "openat": 288,
    "openat2": 437,
    "pause": 29,
    "perf_event_open": 331,
    "personality": 136,
    "pidfd_getfd": 438,
    "pidfd_open": 434,
    "pidfd_send_signal": 424,
    "pipe": 42,
    "pipe2": 325,
    "pivot_root": 217,
    "pkey_alloc": 385,
    "pkey_free": 386,
    "pkey_mprotect": 384,
    "poll": 168,
    "ppoll": 302,
    "prctl": 172,
    "pread64": 180,
    "preadv": 328,
    "preadv2": 376,
    "prlimit64": 334,
    "process_madvise": 440,
    "process_mrelease": 448,
    "process_vm_readv": 340,
    "process_vm_writev": 341,
    "pselect6": 301,
    "ptrace": 26,
    "pwrite64": 181,
    "pwritev": 329,
    "pwritev2": 377,
    "query_module": 167,
    "quotactl": 131,
    "quotactl_fd": 443,
    "read": 3,
    "readahead": 222,
    "readdir": 89,
    "readlink": 85,
    "readlinkat": 298,
    "readv": 145,
    "reboot": 88,
    "recvfrom": 371,
    "recvmmsg": 357,
    "recvmsg": 372,
    "remap_file_pages": 267,
    "removexattr": 233,
    "rename": 38,
    "renameat": 295,
    "renameat2": 347,
    "request_key": 279,
    "restart_syscall": 7,
    "rmdir": 40,
    "rseq": 383,
    "rt_sigaction": 174,
    "rt_sigpending": 176,
    "rt_sigprocmask": 175,
    "rt_sigqueueinfo": 178,
    "rt_sigreturn": 173,
    "rt_sigsuspend": 179,
    "rt_sigtimedwait": 177,
    "rt_tgsigqueueinfo": 330,
    "s390_guarded_storage": 378,
    "s390_pci_mmio_read": 353,
    "s390_pci_mmio_write": 352,
    "s390_runtime_instr": 342,
    "s390_sthyi": 380,
    "sched_get_priority_max": 159,
    "sched_get_priority_min": 160,
    "sched_getaffinity": 240,
    "sched_getattr": 346,
    "sched_getparam": 155,
    "sched_getscheduler": 157,
    "sched_rr_get_interval": 161,
    "sched_setaffinity": 239,
    "sched_setattr": 345,
    "sched_setparam": 154,
    "sched_setscheduler": 156,
    "sched_yield": 158,
    "seccomp": 348,
    "select": 142,
    "semctl": 394,
    "semget": 393,
    "semtimedop": 392,
    "sendfile": 187,
    "sendmmsg": 358,
    "sendmsg": 370,
    "sendto": 369,
    "set_mempolicy": 270,
    "set_mempolicy_home_node": 450,
    "set_robust_list": 304,
    "set_tid_address": 252,
    "setdomainname": 121,
    "setfsgid": 216,
    "setfsuid": 215,
    "setgid": 214,
    "setgroups": 206,
    "sethostname": 74,
    "setitimer": 104,
    "setns": 339,
    "setpgid": 57,
    "setpriority": 97,
    "setregid": 204,
    "setresgid": 210,
    "setresuid": 208,
    "setreuid": 203,
    "setrlimit": 75,
    "setsid": 66,
    "setsockopt": 366,
    "settimeofday": 79,
    "setuid": 213,
    "setxattr": 224,
    "shmat": 397,
    "shmctl": 396,
    "shmdt": 398,
    "shmget": 395,
    "shutdown": 373,
    "sigaction": 67,
    "sigaltstack": 186,
    "signal": 48,
    "signalfd": 316,
    "signalfd4": 322,
    "sigpending": 73,
    "sigprocmask": 126,
    "sigreturn": 119,
    "sigsuspend": 72,
    "socket": 359,
    "socketcall": 102,
    "socketpair": 360,
    "splice": 306,
    "stat": 106,
    "statfs": 99,
    "statfs64": 265,
    "statx": 379,
    "swapoff": 115,
    "swapon": 87,
    "symlink": 83,
    "symlinkat": 297,
    "sync": 36,
    "sync_file_range": 307,
    "syncfs": 338,
    "sysfs": 135,
    "sysinfo": 116,
    "syslog": 103,
    "tee": 308,
    "tgkill": 241,
    "timer_create": 254,
    "timer_delete": 258,
    "timer_getoverrun": 257,
    "timer_gettime": 256,
    "timer_settime": 255,
    "timerfd": 317,
    "timerfd_create": 319,
    "timerfd_gettime": 321,
    "timerfd_settime": 320,
    "times": 43,
    "tkill": 237,
    "truncate": 92,
    "umask": 60,
    "umount": 22,
    "umount2": 52,
    "uname": 122,
    "unlink": 10,
    "unlinkat": 294,
    "unshare": 303,
    "uselib": 86,
    "userfaultfd": 355,
    "ustat": 62,
    "utime": 30,
    "utimensat": 315,
    "utimes": 313,
    "vfork": 190,
    "vhangup": 111,
    "vmsplice": 309,
    "wait4": 114,
    "waitid": 281,
    "write": 4,
    "writev": 146,
}
