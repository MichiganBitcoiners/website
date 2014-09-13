"""
productionize_html.py

Reads an HTML file from standard input and writes to standard output.
Removes sections deliniated by comments containing "begin development section"
and "end development section". Removes comments that contain
"begin production section" and "end production section".
"""

import sys
import re

# Regular expressions for the comments that deliniate the sections.
re_dev_begin = re.compile(r'^ *<!-- begin development section.*-->$')
re_dev_end = re.compile(r'^ *<!-- end development section -->.*$')
re_prod_begin = re.compile(r'^ *<!-- begin production section.*$')
re_prod_end = re.compile(r'^ *end production section -->.*$')

in_dev = False
for line in sys.stdin:
    if in_dev:
        if re_dev_end.match(line):
            in_dev = False
        continue
    if re_dev_begin.match(line):
        in_dev = True
        continue
    if re_prod_begin.match(line):
        continue
    if re_prod_end.match(line):
        continue
    sys.stdout.write(line)
