# Content autogenerated. Do not edit.

syscalls_xtensa = {
    "_llseek": 17,
    "_sysctl": 206,
    "accept": 103,
    "accept4": 333,
    "access": 57,
    "acct": 155,
    "add_key": 256,
    "adjtimex": 194,
    "bdflush": 207,
    "bind": 100,
    "bpf": 340,
    "brk": 83,
    "cachestat": 451,
    "capget": 158,
    "capset": 159,
    "chdir": 41,
    "chmod": 44,
    "chown": 45,
    "chroot": 174,
    "clock_adjtime": 329,
    "clock_adjtime64": 405,
    "clock_getres": 246,
    "clock_getres_time64": 406,
    "clock_gettime": 245,
    "clock_gettime64": 403,
    "clock_nanosleep": 247,
    "clock_nanosleep_time64": 407,
    "clock_settime": 244,
    "clock_settime64": 404,
    "clone": 116,
    "clone3": 435,
    "close": 9,
    "close_range": 436,
    "connect": 101,
    "copy_file_range": 345,
    "creat": 21,
    "delete_module": 211,
    "dup": 10,
    "dup2": 11,
    "dup3": 310,
    "epoll_create": 20,
    "epoll_create1": 275,
    "epoll_ctl": 19,
    "epoll_pwait": 274,
    "epoll_pwait2": 441,
    "epoll_wait": 18,
    "eventfd": 306,
    "eventfd2": 316,
    "execve": 117,
    "execveat": 341,
    "exit": 118,
    "exit_group": 119,
    "faccessat": 301,
    "faccessat2": 439,
    "fadvise64_64": 63,
    "fallocate": 62,
    "fanotify_init": 320,
    "fanotify_mark": 321,
    "fchdir": 42,
    "fchmod": 52,
    "fchmodat": 300,
    "fchmodat2": 452,
    "fchown": 53,
    "fchownat": 297,
    "fcntl": 67,
    "fcntl64": 61,
    "fdatasync": 27,
    "fgetxattr": 77,
    "finit_module": 332,
    "flistxattr": 78,
    "flock": 56,
    "fremovexattr": 79,
    "fsconfig": 431,
    "fsetxattr": 76,
    "fsmount": 432,
    "fsopen": 430,
    "fspick": 433,
    "fstat": 54,
    "fstat64": 55,
    "fstatat64": 299,
    "fstatfs": 185,
    "fstatfs64": 187,
    "fsync": 26,
    "ftruncate": 23,
    "ftruncate64": 29,
    "futex": 191,
    "futex_time64": 422,
    "futex_waitv": 449,
    "futimesat": 298,
    "get_mempolicy": 264,
    "get_robust_list": 285,
    "getcpu": 280,
    "getcwd": 43,
    "getdents": 59,
    "getdents64": 60,
    "getegid": 141,
    "geteuid": 140,
    "getgid": 139,
    "getgroups": 196,
    "getitimer": 135,
    "getpeername": 105,
    "getpgid": 149,
    "getpgrp": 151,
    "getpid": 120,
    "getppid": 150,
    "getpriority": 132,
    "getrandom": 338,
    "getresgid": 147,
    "getresuid": 145,
    "getrlimit": 189,
    "getrusage": 190,
    "getsid": 129,
    "getsockname": 104,
    "getsockopt": 98,
    "gettid": 127,
    "gettimeofday": 192,
    "getuid": 137,
    "getxattr": 69,
    "init_module": 210,
    "inotify_add_watch": 277,
    "inotify_init": 276,
    "inotify_init1": 279,
    "inotify_rm_watch": 278,
    "io_cancel": 243,
    "io_destroy": 240,
    "io_getevents": 242,
    "io_pgetevents_time64": 416,
    "io_setup": 239,
    "io_submit": 241,
    "io_uring_enter": 426,
    "io_uring_register": 427,
    "io_uring_setup": 425,
    "ioctl": 66,
    "ioprio_get": 283,
    "ioprio_set": 282,
    "kcmp": 331,
    "kexec_load": 281,
    "keyctl": 258,
    "kill": 123,
    "landlock_add_rule": 445,
    "landlock_create_ruleset": 444,
    "landlock_restrict_self": 446,
    "lchown": 48,
    "lgetxattr": 73,
    "link": 32,
    "linkat": 293,
    "listen": 102,
    "listxattr": 70,
    "llistxattr": 74,
    "lookup_dcookie": 254,
    "lremovexattr": 75,
    "lseek": 15,
    "lsetxattr": 72,
    "lstat": 49,
    "lstat64": 50,
    "madvise": 91,
    "mbind": 263,
    "membarrier": 343,
    "memfd_create": 339,
    "migrate_pages": 262,
    "mincore": 90,
    "mkdir": 40,
    "mkdirat": 289,
    "mknod": 36,
    "mknodat": 290,
    "mlock": 84,
    "mlock2": 344,
    "mlockall": 86,
    "mmap2": 80,
    "mount": 172,
    "mount_setattr": 442,
    "move_mount": 429,
    "move_pages": 267,
    "mprotect": 82,
    "mq_getsetattr": 237,
    "mq_notify": 236,
    "mq_open": 232,
    "mq_timedreceive": 235,
    "mq_timedreceive_time64": 419,
    "mq_timedsend": 234,
    "mq_timedsend_time64": 418,
    "mq_unlink": 233,
    "mremap": 88,
    "msgctl": 169,
    "msgget": 166,
    "msgrcv": 168,
    "msgsnd": 167,
    "msync": 89,
    "munlock": 85,
    "munlockall": 87,
    "munmap": 81,
    "name_to_handle_at": 324,
    "nanosleep": 195,
    "nfsservctl": 205,
    "open": 8,
    "open_by_handle_at": 325,
    "open_tree": 428,
    "openat": 288,
    "openat2": 437,
    "perf_event_open": 327,
    "personality": 131,
    "pidfd_getfd": 438,
    "pidfd_open": 434,
    "pidfd_send_signal": 424,
    "pipe": 37,
    "pipe2": 311,
    "pivot_root": 175,
    "pkey_alloc": 349,
    "pkey_free": 350,
    "pkey_mprotect": 348,
    "poll": 16,
    "ppoll": 273,
    "ppoll_time64": 414,
    "prctl": 130,
    "pread64": 30,
    "preadv": 317,
    "preadv2": 346,
    "prlimit64": 330,
    "process_madvise": 440,
    "process_mrelease": 448,
    "process_vm_readv": 322,
    "process_vm_writev": 323,
    "pselect6": 272,
    "pselect6_time64": 413,
    "ptrace": 160,
    "pwrite64": 31,
    "pwritev": 318,
    "pwritev2": 347,
    "quotactl": 204,
    "quotactl_fd": 443,
    "read": 12,
    "readahead": 260,
    "readlink": 35,
    "readlinkat": 295,
    "readv": 24,
    "reboot": 203,
    "recv": 109,
    "recvfrom": 111,
    "recvmmsg": 307,
    "recvmmsg_time64": 417,
    "recvmsg": 107,
    "remap_file_pages": 261,
    "removexattr": 71,
    "rename": 33,
    "renameat": 292,
    "renameat2": 336,
    "request_key": 257,
    "restart_syscall": 223,
    "rmdir": 39,
    "rseq": 352,
    "rt_sigaction": 226,
    "rt_sigpending": 228,
    "rt_sigprocmask": 227,
    "rt_sigqueueinfo": 230,
    "rt_sigreturn": 225,
    "rt_sigsuspend": 231,
    "rt_sigtimedwait": 229,
    "rt_sigtimedwait_time64": 421,
    "rt_tgsigqueueinfo": 328,
    "sched_get_priority_max": 216,
    "sched_get_priority_min": 217,
    "sched_getaffinity": 157,
    "sched_getattr": 335,
    "sched_getparam": 213,
    "sched_getscheduler": 215,
    "sched_rr_get_interval": 218,
    "sched_rr_get_interval_time64": 423,
    "sched_setaffinity": 156,
    "sched_setattr": 334,
    "sched_setparam": 212,
    "sched_setscheduler": 214,
    "sched_yield": 219,
    "seccomp": 337,
    "select": 14,
    "semctl": 164,
    "semget": 162,
    "semop": 163,
    "semtimedop": 161,
    "semtimedop_time64": 420,
    "send": 108,
    "sendfile": 113,
    "sendfile64": 114,
    "sendmmsg": 115,
    "sendmsg": 106,
    "sendto": 110,
    "set_mempolicy": 265,
    "set_mempolicy_home_node": 450,
    "set_robust_list": 284,
    "set_tid_address": 126,
    "setdomainname": 199,
    "setfsgid": 181,
    "setfsuid": 180,
    "setgid": 138,
    "setgroups": 197,
    "sethostname": 198,
    "setitimer": 134,
    "setns": 308,
    "setpgid": 148,
    "setpriority": 133,
    "setregid": 143,
    "setresgid": 146,
    "setresuid": 144,
    "setreuid": 142,
    "setrlimit": 188,
    "setsid": 128,
    "setsockopt": 97,
    "settimeofday": 193,
    "setuid": 136,
    "setxattr": 68,
    "shmat": 93,
    "shmctl": 94,
    "shmdt": 95,
    "shmget": 92,
    "shutdown": 99,
    "sigaltstack": 224,
    "signalfd": 304,
    "signalfd4": 309,
    "socket": 96,
    "socketpair": 112,
    "splice": 268,
    "stat": 46,
    "stat64": 47,
    "statfs": 184,
    "statfs64": 186,
    "statx": 351,
    "swapoff": 177,
    "swapon": 173,
    "symlink": 34,
    "symlinkat": 294,
    "sync": 178,
    "sync_file_range2": 326,
    "syncfs": 179,
    "sysfs": 182,
    "sysinfo": 209,
    "syslog": 200,
    "tee": 269,
    "tgkill": 125,
    "timer_create": 248,
    "timer_delete": 249,
    "timer_getoverrun": 252,
    "timer_gettime": 251,
    "timer_gettime64": 408,
    "timer_settime": 250,
    "timer_settime64": 409,
    "timerfd_create": 312,
    "timerfd_gettime": 314,
    "timerfd_gettime64": 410,
    "timerfd_settime": 313,
    "timerfd_settime64": 411,
    "times": 154,
    "tkill": 124,
    "truncate": 22,
    "truncate64": 28,
    "umask": 58,
    "umount": 176,
    "umount2": 171,
    "uname": 208,
    "unlink": 38,
    "unlinkat": 291,
    "unshare": 266,
    "uselib": 202,
    "userfaultfd": 342,
    "ustat": 183,
    "utime": 64,
    "utimensat": 296,
    "utimensat_time64": 412,
    "utimes": 65,
    "vhangup": 201,
    "vmsplice": 270,
    "wait4": 121,
    "waitid": 122,
    "write": 13,
    "writev": 25,
}
