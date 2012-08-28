#!/bin/env python
import sys,re

colors = {
'b500' : 'yellow',
'b501' : 'lightgreen',
'b502' : 'lightblue' ,
'b504' : 'cyan' ,
'b600' : 'orange',
'b601' : 'magenta',
'b60e' : 'hotpink',
'b60f' : 'hotpink',
'b613' : 'hotpink',
'bf01' : 'hotpink '
}

coloring = re.compile(r'80 06 ([0-9a-f]{4}) ([a-f0-9]{2})([a-f0-9]{2})',flags = re.IGNORECASE | re.MULTILINE)

data = open(sys.argv[1]).read()

data_colored = re.sub(coloring, lambda m: '80 06 <FONT style="BACKGROUND-COLOR: %s">%s</FONT> <FONT style="BACKGROUND-COLOR: gainsboro">%s</FONT><FONT style="BACKGROUND-COLOR: lightgreen">%s</FONT>'
        % ( colors[m.group(1)], m.group(1), m.group(2), m.group(3)), data)
print '<pre>',data_colored,'</pre>'

