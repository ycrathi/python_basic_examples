from collections import ChainMap

a = {1: "Java", 2: "Selenium", 3: "Python"}
b = {4: "AI", 5: "ML"}

a1 = ChainMap(a, b)

print(a1)

print(type(a1))
print(type(a))
