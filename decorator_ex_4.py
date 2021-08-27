def fun1(function):
    def wrapper(*args, **kwargs):
        print("Hello")
        function(*args, **kwargs)
        print("Welcome to python tutorial")

    return wrapper


@fun1
def fun2(name):
    print(f"{name}")


fun2("Yogesh")
