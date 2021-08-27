def fun1(function):
    def wrapper():
        print("Hello")
        function()
        print("Welcome to python tutorial")

    return wrapper


def fun2():
    print("Yogesh")


test = fun1(fun2)
test()
