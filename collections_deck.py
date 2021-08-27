from collections import deque

a = ['y', 'o', 'g', 'e', 's', 'h']
d = deque(a)
print(d)

d.append('r')
print(d)

d.appendleft('mr:')
print(d)

d.pop()
print(d)

d.popleft()
print(d)
