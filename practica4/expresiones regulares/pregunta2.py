import re
str = "Working 6 hours a day. Studying 4 hours a day."
pat = r'[0-9]'
for mobj in re.finditer(pat, str):
    s = mobj.start()
    e = mobj.end()
    g = mobj.group()
    print('{} found at location [{},{}]'.format(g, s, e))