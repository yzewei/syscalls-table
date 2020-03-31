KVER := $(shell make -C ${KERNELSRC} kernelversion -s)

all: tables out/syscalls.html

list-syscalls.c: update
	@./generate-list-syscalls.sh | sed -e "s/'/\"/g">list-syscalls.c

FORCE:

out/syscalls.html: FORCE
	@mkdir -p out
	@./parser.py >out/syscalls.html ${KVER}

clean:
	@rm -rf list-syscalls list-syscalls.c out/syscalls.html headers

tables: list-syscalls.c FORCE
	@mkdir -p headers
	@./do_all_tables.sh ${KERNELSRC}

update: FORCE
	@./grab_syscall_names_from_tables.sh ${KERNELSRC}
