class Car():
    def __init__(self, modelname, yearm, price):
        self.modename = modelname
        self.yearm = yearm
        self.price = price

    def price_inc(self):
        self.price = int(self.price * 1.15)


class SuperCar(Car):
    pass


honda = SuperCar('City', 2021, 200)
honda.cc = 1200

tata = Car('Tigor', 2021, 100)

tata.price_inc()

print(honda.__dict__)
print(tata.__dict__)

print(help(honda))