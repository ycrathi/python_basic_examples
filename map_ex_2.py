def new(a, b):
    return a * b


x = map(new, [1, 2, 3, 4], [2, 3, 4, 5])
print(x)
print(tuple(x))
