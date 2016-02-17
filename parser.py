#!/bin/python3

import collections, csv, pprint, os

syscalls = collections.OrderedDict()

os.chdir('tables')
for filename in os.listdir(os.getcwd()):
    arch=filename.replace('syscalls-', '')

    with open(filename, newline='') as csvh:
        seccompdata = csv.reader(csvh, delimiter="\t")

        for row in seccompdata:
            if not row[0] in syscalls:
                syscalls[row[0]] = collections.OrderedDict()

            syscalls[row[0]][arch] = row[1]

#pprint.pprint(syscalls)

print("""
<html>
<head>
<style>
table, td { padding: 0.25em; margin:1em}
tr:nth-child(odd)		{ background-color:#ddd; }
tr:nth-child(even)		{ background-color:#fff; }
.legacy {background-color: #b00}

</style>
</head>
<body>
<table>
<thead>
<tr>
<th>system call</th>
<th>aarch64</th>
<th>arm</th>
<th>mips</th>
<th>mips64</th>
<th>mips64n32
<th>ppc64</th>
<th>s390</th>
<th>s390x</th>
<th>x32</th>
<th>x86</th>
<th>x86_64</th>
</tr>
</thead>
<tbody>
""")

for syscall in syscalls.keys():
    print("<tr><td>%s</td>" % syscall)

    for arch in sorted(syscalls[syscall]):
        syscallnr = syscalls[syscall][arch]
        css = ''
        if syscallnr == '' or int(syscallnr) < 0:
            syscallnr = 'legacy'
            css = 'class="legacy"'
        print("<td %s >%s</td>" % (css, syscallnr))

    print("</tr>")

print("""
</tbody>
</table>
</body>
</html>
""")
