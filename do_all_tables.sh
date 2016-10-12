#!/bin/bash

KERNELSRC=$1

generate_table() 
{
	echo $arch
	gcc -D${arch^^} list-syscalls.c -I $archdir/include/uapi -I $archdir/include -o list-syscalls
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
	mips)
				generate_table
		arch=mips64n32	generate_table
		arch=mips64	generate_table
		;;
	x86)
				generate_table
		#arch=x32 	generate_table
		arch=x86_64	generate_table
		;;
	powerpc)
				generate_table
		arch=powerpc64	generate_table
		;;
	s390)
				generate_table
		arch=s390x	generate_table
		;;
	sparc)
				generate_table
		arch=sparc64	generate_table
		;;
	sh)
				generate_table
		arch=sh64	generate_table
		;;
	*)
		generate_table
		;;
	esac
done
