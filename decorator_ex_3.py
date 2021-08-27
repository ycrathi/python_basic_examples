def fun1(function):
    def wrapper():
        print("Hello")
        function()
        print("Welcome to python tutorial")

    return wrapper


@fun1
def fun2():
    print("Yogesh")


fun2()
