def fun1(name):
    return f"Hello{name}"


def fun2(name):
    return f"{name}, How are you doing ?"


def fun3(fun4):
    return fun4('Dear Learner')


print(fun3(fun1))
print(fun3(fun2))
