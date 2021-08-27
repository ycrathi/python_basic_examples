class Parent1:
    def fun1(self):
        print("Parent1 function")


class Parent2(Parent1):
    def fun2(self):
        print("Parent2 function")


class Child(Parent2):
    def fun3(self):
        print("Child function")


ob = Child()
ob.fun1()
ob.fun2()
