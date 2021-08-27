class Parent:
    def fun1(self):
        print("Parent function")


class Child(Parent):
    def fun2(self):
        print("Child function")


ob = Child()
ob.fun1()
ob.fun2()
