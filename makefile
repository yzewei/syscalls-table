all: tables out/syscalls.html

arch: list-syscalls
	./list-syscalls |LC_ALL=C sort -u >tables/syscalls-$(shell uname -m)

list-syscalls.c:
	./update-list.sh | sed -e "s/'/\"/g">list-syscalls.c

list-syscalls: list-syscalls.c
	$(CC) list-syscalls.c -o list-syscalls

FORCE:

out/syscalls.html: FORCE
	mkdir -p out
	./parser.py >out/syscalls.html

clean:
	rm -rf list-syscalls list-syscalls.c out/syscalls.html headers

tables: list-syscalls.c FORCE
	mkdir -p headers
	./do_all_tables.sh ${KERNELSRC}
