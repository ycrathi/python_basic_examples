from collections import Counter

a = [1, 1, 2, 4, 2, 4, 1, 5, 6, 7, 8, 2]
c = Counter(a)
print(c)
print(c.get(1))
print(c.get(2))
print(c.get(4))
print(list(c.elements()))

print(c.most_common())
sub = {2: 1, 6: 1}
print(c.subtract(sub))
print(c.most_common())
