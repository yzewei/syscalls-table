#!/bin/bash

KERNELSRC=$1

TMP=`mktemp`

export_headers()
{
	make -s -C ${KERNELSRC} ARCH=${arch} O=${PWD}/headers headers_install

	egrep -h "^#define __NR_" ${PWD}/headers/usr/include/asm/unistd*.h ${PWD}/headers/usr/include/asm-generic/unistd.h |
		egrep -v "(unistd.h|NR3264|__NR_syscall|__SC_COMP|__NR_.*Linux|__NR_FAST)" |
		egrep -vi "(not implemented|available|unused|reserved|xtensa|spill)" |
		egrep -v "(__SYSCALL|SYSCALL_BASE)" |
		sed -e "s/#define\s*__NR_//g" -e "s/\s.*//g" |
		sort -u >${TMP}
	cat syscall-names.text >>${TMP}
	sed -i '/arch_specific_syscall/d' ${TMP}
	LC_ALL=C sort -u ${TMP} >syscall-names.text
}

generate_table() 
{
	echo $arch

	gcc list-syscalls.c -U__LP64__ -U__ILP32__ -U__i386__ -D${arch^^} \
		-D__${arch}__ ${extraflags} -I headers/usr/include/ -o list-syscalls
	./list-syscalls > "tables/syscalls-$arch"
}


for archdir in $KERNELSRC/arch/*
do 
	arch=`basename $archdir`

	case ${arch} in
	Kconfig)
		continue;
		;;
	um)
		continue;
		;;
	esac

	export_headers

	case ${arch} in
	arm)
		arch=armoabi	extraflags=				generate_table
		arch=arm	extraflags=-D__ARM_EABI__		generate_table
		;;
	mips)
		arch=mipso32	extraflags=-D_MIPS_SIM=_MIPS_SIM_ABI32	generate_table
		arch=mips64n32	extraflags=-D_MIPS_SIM=_MIPS_SIM_NABI32	generate_table
		arch=mips64	extraflags=-D_MIPS_SIM=_MIPS_SIM_ABI64	generate_table
		;;
	tile)
									generate_table
		arch=tile64	extraflags="-D__LP64__ -D__tilegx__"	generate_table
		;;
	x86)
		arch=i386	                        		generate_table
		arch=x32 	extraflags=-D__ILP32__			generate_table
		arch=x86_64	extraflags=-D__LP64__			generate_table
		;;
	riscv)
		arch=riscv32	                        		generate_table
		arch=riscv64	extraflags=-D__LP64__			generate_table
		;;
	powerpc)
									generate_table
		arch=powerpc64						generate_table
		;;
	s390)
									generate_table
		arch=s390x						generate_table
		;;
	sparc)
				extraflags=-D__32bit_syscall_numbers__	generate_table
		arch=sparc64	extraflags=-D__arch64__			generate_table
		;;
	sh)
									generate_table
		arch=sh64	extraflags=-D__SH5__			generate_table
		;;
	*)
		generate_table
		;;
	esac
done
