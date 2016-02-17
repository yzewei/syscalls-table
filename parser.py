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
    <title>System calls table for several architectures</title>
    <link rel="stylesheet" href="css/style.css" type="text/css" media="print, projection, screen" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <script src="https://raw.githubusercontent.com/christianbach/tablesorter/master/jquery.tablesorter.js"></script>
    <script type="text/javascript" id="js">
            $(document).ready(function() {
            // call the tablesorter plugin
            $("table").tablesorter({textExtraction: "complex"});
    }); 
    </script>
    <style type="text/css">
table.tablesorter {
	border: 1px solid #000;
}
table.tablesorter th {
	text-align: center;
	padding: 0.5em;
}
table.tablesorter td {
	padding: 0.5em;
}
.legacy {background-color: #b00}
    </style>
</head>
<body>
    <p>
    This table shows system call numbers from several architectures.
    Value "-1" means legacy syscall which is not supported on this
    architecture.
    </p>
    <p>
    To add new column please contact me.
    </p>
    <p>
    Headers are clickable.
    </p>
    <table class="tablesorter">
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
            syscallnr = '-1'
            css = ' class="legacy" '
        print("<td%s>%s</td>" % (css, syscallnr))

    print("</tr>")

print("""
        </tbody>
    </table>
</body>
</html>
""")
