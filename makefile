arch: list-syscalls
	./list-syscalls >tables/syscalls-$(shell uname -m)
list-syscalls.c:
	./update-list.sh | sed -e "s/'/\"/g">list-syscalls.c

list-syscalls: list-syscalls.c
	$(CC) list-syscalls.c -o list-syscalls

out/syscalls.html: 
	./parser.py >out/syscalls.html
