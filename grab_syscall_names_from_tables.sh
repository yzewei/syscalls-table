#!/bin/bash

TMP=`mktemp`

# arm_sync_file_range is sync_file_range2() since 2.6.22
# utimesat is PowerPC/SPU only
# rest are not implemented
#
DEAD_SYSCALLS="afs_syscall|break|ftime|gtty|lock|mpx|oldwait4|prof|profil|putpmsg|security|stty|tuxcall|ulimit|vserver|arm_sync_file_range|utimesat"

for tbl_file in $(find $KERNELSRC -name syscall*.tbl)
do
	egrep -v "(^#|^$|sys_ni_syscall|unused|${DEAD_SYSCALLS})" $tbl_file |
		awk '{ print $3 }' > ${TMP}
	cat syscall-names.text >>${TMP}
	LC_ALL=C sort -u ${TMP} >syscall-names.text
done
