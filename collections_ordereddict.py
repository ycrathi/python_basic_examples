from collections import OrderedDict

d = OrderedDict()
d[1] = 'y'
d[2] = 'o'
d[3] = 'g'
d[4] = 'e'
d[5] = 's'
d[6] = 'h'

print(d)

print(d.keys())
print(d.items())
print(d.values())

d[1] = 'Y'
print(d)
