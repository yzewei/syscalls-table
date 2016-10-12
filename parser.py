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
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>

    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.12/css/jquery.dataTables.min.css"/>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/buttons/1.2.2/css/buttons.dataTables.min.css"/>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/colreorder/1.3.2/css/colReorder.dataTables.min.css"/>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/fixedheader/3.1.2/css/fixedHeader.dataTables.min.css"/>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/select/1.2.0/css/select.dataTables.min.css"/>

    <script type="text/javascript" src="https://cdn.datatables.net/1.10.12/js/jquery.dataTables.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/buttons/1.2.2/js/dataTables.buttons.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/buttons/1.2.2/js/buttons.colVis.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/buttons/1.2.2/js/buttons.print.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/colreorder/1.3.2/js/dataTables.colReorder.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/fixedheader/3.1.2/js/dataTables.fixedHeader.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/select/1.2.0/js/dataTables.select.min.js"></script>
    <script type="text/javascript" id="js">
            $(document).ready(function() {
                    $("table").DataTable( {
                            pageLength  : -1,
                            fixedHeader : true,
                            dom         : 'Bft',
                            buttons     : [
                            {
                                    extend : 'colvis',
                                    text: 'disable architectures',
                                    columns: ':gt(0)'
                            }
                            ]
                    });
    }); 
    </script>
    <style type="text/css">

table.syscalls {
        border: 1px solid #000;
}

table.syscalls th {
        text-align: center;
        padding: 0.5em;
        line-height: 2em;
        color: white;
}

table.syscalls thead {
        border: 1px solid black;
        background-color: grey;
}

table.syscalls td {
        padding: 0.5em;
}

table.syscalls tbody tr.odd td {
        background-color: lightgrey;
}

.legacy, table.syscalls tbody tr.odd td.legacy {
        background-color: lightpink;
}
    </style>
</head>
<body>

<h1>Introduction</h1>
    <p>
    Linux provides many system calls for userspace. But numbers used for them
    differ between architectures. This page was created to help developers find
    those values.
    </p>
    <p>
    But there is another issue. Some of system calls got dropped during Linux
    development, some got replaced by newer ones. Several architectures got
    added into kernel later and their maintainers decided to not bother with
    supporting obsoleted system calls. They are marked with "-1" value in table
    below.
    </p>
<h1>How to use</h1>
    <p>
    There are few features you can use:
    
    <ul>
    <li>search field allows to filter table by syscall name or number</li>
    <li>system call names link to their man pages</li>
    <li>'disable architectures' button allows to disable not needed columns</li>
    <li>clicking on header entries sorts table</li>
    </ul>
    </p>


<h1>How to help</h1>
    <p>
    Sources used to generate table are available in <a
    href="https://github.com/hrw/syscalls-table">git repository at github</a>.
    Patches are always welcomed.
    </p>
""")


print("""
    <table class="syscalls">
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
    <p>Table generated on %s</p>
</body>
</html>
""" % datetime.datetime.strftime(datetime.datetime.utcnow(), "%Y.%m.%d %H:%M"))
