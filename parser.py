#!/bin/python3

import collections
import csv
import datetime
import os

syscalls = collections.OrderedDict()

archs = []
os.chdir('tables')
for filename in os.listdir(os.getcwd()):

    try:
        arch=filename.replace('syscalls-', '')

        with open(filename, newline='') as csvh:
            seccompdata = csv.reader(csvh, delimiter="\t")
            archs.append(arch)

            for row in seccompdata:
                try:
                    syscalls[row[0]][arch] = row[1]
                except KeyError:
                    syscalls[row[0]] = collections.OrderedDict()
                    syscalls[row[0]][arch] = row[1]
                except IndexError:
                    pass

    except IndexError:
        pass

print("""
<html>
<head>
    <title>System calls table for several architectures</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <script src="https://fedora.juszkiewicz.com.pl/.js/jquery.tablesorter.js"></script>
    <script src="https://fedora.juszkiewicz.com.pl/.js/jquery.stickytableheaders.min.js"></script>
    <script type="text/javascript" id="js">
            $(document).ready(function() {
            // call the tablesorter plugin
            $("table").tablesorter({textExtraction: "complex", widgets: ['zebra']});
	    $('table').stickyTableHeaders();
    }); 
    </script>
    <style type="text/css">

table.tablesorter {
	border: 1px solid #000;
}

table.tablesorter th {
	text-align: center;
	padding: 0.5em;
	line-height: 2em;
	color: white;
}

table.tablesorter thead {
	border: 1px solid black;
	background-color: grey;
}

table.tablesorter td {
	padding: 0.5em;
}

table.tablesorter tbody tr.odd td {
	background-color: lightgrey;
}

.legacy {
        background-color: #b00
}
    </style>
</head>
<body>
    <p>
    This table shows system call numbers from several architectures.
    </p>
    <p>
    Value "-1" has few meanings:
    <ul>
        <li>legacy syscall which is not supported on this architecture</li>
        <li>syscall added in newer kernel version than was present on testing machine</li>
    </ul>
    </p>
    <p>
    System call names link to their man pages.
    </p>
    <p>
    Sources used to generate table are available in <a
    href="https://github.com/hrw/syscalls-table">git repository at github</a>.
    Pull request is preferred way to update data.
    </p>
""")

print("<p>Table generated on %s</p>" % datetime.datetime.strftime(datetime.datetime.utcnow(), "%Y.%m.%d %H:%M"))

print("""
    <p>
    Headers are clickable.
    </p>
    <table class="tablesorter">
        <thead>
            <tr>
                <th>system call</th>
""")

for arch in sorted(archs):
    print("<th>%s</th>" % arch)


print("""
            </tr>
        </thead>
        <tbody>
""")

oddeven = 0

for syscall in sorted(syscalls.keys()):

    if (oddeven % 2 == 0):
        trclass = "even"
    else:
        trclass = "odd"

    oddeven += 1

    print("<tr class='%s'><td><a href='http://www.man7.org/linux/man-pages/man2/%s.2.html'>%s</a></td>" % (trclass, syscall,syscall))

    for arch in sorted(archs):

        try:
            syscallnr = syscalls[syscall][arch]
            css = ''
        except KeyError:
            syscallnr = -1
            css = ' class="legacy" '

        if not syscallnr:
            syscallnr = -1
            css = ' class="legacy" '

        print("<td%s>%s</td>" % (css, syscallnr))

    print("</tr>")

print("""
        </tbody>
    </table>
</body>
</html>
""")
