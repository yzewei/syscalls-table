#/bin/bash

TMP=`mktemp`

grep "#define __NR_" /usr/include/asm-generic/unistd.h |grep -v NR3264|cut -d" " -f2|sed -e "s/__NR_//g" >$TMP
cat tables/syscall-names.text >>$TMP
sort -u $TMP >tables/syscall-names.text

echo "
#include <stdio.h>

#include <asm/unistd.h>

int main(void)
{
"

for syscall in `cat tables/syscall-names.text`
do

	echo "
#ifdef __NR_$syscall
	printf('$syscall\t%d\n', __NR_$syscall);
#else
	printf('$syscall\n');
#endif
"
done

echo "
	return 0;
}
"
