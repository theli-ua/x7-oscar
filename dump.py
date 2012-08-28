import sys,re

datare = re.compile(' b504 ([0-9a-f]{2})[0-9a-f]{2} ', flags=re.MULTILINE)

data = ''.join([m.group(1) for m in datare.finditer(open(sys.argv[1]).read())])
print data

open(sys.argv[2],'wb').write(data.decode('hex'))
