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

	if [ "$arch" == 'mips' ]; then
		generate_table
		arch=mips64n32
		generate_table
		arch=mips64
		generate_table
	elif [ "$arch" == 'x86' ]; then
		generate_table
#		arch=x32
#		generate_table
		arch=x86_64
		generate_table
	elif [ "$arch" == 'powerpc' ]; then
		generate_table
		arch=powerpc64
		generate_table
	elif [ "$arch" == 's390' ]; then
		generate_table
		arch=s390x
		generate_table
	elif [ "$arch" == 'sparc' ]; then
		generate_table
		arch=sparc64
		generate_table
	elif [ "$arch" == 'sh' ]; then
		generate_table
		arch=sh64
		generate_table
	elif [ "$arch" == 'Kconfig' ]; then
		echo ""
	else
		generate_table
	fi
done
