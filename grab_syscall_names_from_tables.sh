#!/bin/bash

TMP=`mktemp`

for tbl_file in $(find $KERNELSRC -name syscall*.tbl)
do
	egrep -v "(^#|^$|sys_ni_syscall|unused)" $tbl_file |
		awk '{ print $3 }' > ${TMP}
	cat syscall-names.text >>${TMP}
	LC_ALL=C sort -u ${TMP} >syscall-names.text
done
