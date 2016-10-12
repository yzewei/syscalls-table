#!/bin/bash

KERNELSRC=$1

export_headers()
{
	make -s -C ${KERNELSRC} ARCH=${arch} O=${PWD}/headers headers_install
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
