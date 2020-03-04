#!/usr/bin/python3

import collections
import csv
from datetime import datetime
import io
import os
import sys

from string import Template

kernel_version = ''

if len(sys.argv) > 1:
    kernel_version = sys.argv[1]

syscalls = collections.OrderedDict()

# use current system call names - tables/* can contain archive data
with io.open('syscall-names.text', newline='') as csvh:
    syscalldata = csv.reader(csvh, delimiter="\t")

    for row in syscalldata:
        syscalls[row[0]] = collections.OrderedDict()

present_archs = []
os.chdir('tables')
for filename in os.listdir(os.getcwd()):

    try:
        arch = filename.replace('syscalls-', '')

        with io.open(filename, newline='') as csvh:
            syscalldata = csv.reader(csvh, delimiter="\t")
            present_archs.append(arch)

            for row in syscalldata:
                try:
                    syscalls[row[0]][arch] = row[1]
                except KeyError:
                    # old kernel table data - we ignore this syscall
                    pass
                except IndexError:
                    pass

    except IndexError:
        pass

archs = ['arm64', 'arm', 'armoabi', 'x86_64', 'x32', 'i386', 'mips64',
         'mips64n32', 'mipso32', 'powerpc64', 'powerpc', 's390x', 's390']

removed_archs = ['avr32', 'blackfin', 'cris', 'frv', 'm32r', 'metag',
                 'mn10300', 'score', 'sh64', 'tile', 'tile64']

for arch in sorted(present_archs):

    if (arch not in removed_archs and arch not in archs):
        archs.append(arch)

for arch in removed_archs:
    archs.append(arch)

archs_header = ''

for arch in archs:
    archs_header += f'<th>{arch}</th>'

syscall_table = ''
oddeven = 0

for syscall in sorted(syscalls.keys()):

    if (oddeven % 2 == 0):
        trclass = "even"
    else:
        trclass = "odd"

    oddeven += 1

    syscall_table += f"""
<tr class='{trclass}'>
<td><a href='http://www.man7.org/linux/man-pages/man2/{syscall}.2.html'>
{syscall}</a></td>"""

    for arch in archs:

        try:
            syscallnr = syscalls[syscall][arch]
            css = ''
        except KeyError:
            syscallnr = -1
            css = ' class="legacy" '

        if not syscallnr:
            syscallnr = -1
            css = ' class="legacy" '

        syscall_table += f"<td {css}>{syscallnr}</td>"

    syscall_table += "</tr>"

with open("../template.html") as html_file:
    html = Template(html_file.read())

    print(html.substitute(generate_time=datetime.strftime(datetime.utcnow(),
                                                          "%Y.%m.%d %H:%M"),
                          kernel_version=kernel_version,
                          archs_header=archs_header,
                          syscall_table=syscall_table))
