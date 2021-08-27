def fun1(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        print("It worked")

    return wrapper


@fun1
def fun2(name):
    print(f"{name}")


fun2("Yogesh")
