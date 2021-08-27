from collections import namedtuple

a = namedtuple('courses', 'name, technology')
s = a('Programming', 'Java')
print(s)
s = a._make(['AI', 'Python'])
print(s)
