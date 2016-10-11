arch: list-syscalls
	./list-syscalls |LC_ALL=C sort -u >tables/syscalls-$(shell uname -m)

list-syscalls.c:
	./update-list.sh | sed -e "s/'/\"/g">list-syscalls.c

list-syscalls: list-syscalls.c
	$(CC) list-syscalls.c -o list-syscalls

out/syscalls.html: 
	./parser.py >out/syscalls.html

clean:
	rm list-syscalls list-syscalls.c out/syscalls.html


tables:
	do_all_tables.sh
