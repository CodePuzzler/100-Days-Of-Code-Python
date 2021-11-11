# Day10 of my 100DaysOfCode Challenge
# Program to use inheritence in python

class Car():
    def __init__(self, modelName, yearM, price):
        self.modelName = modelName
        self.yearM = yearM
        self.price = price

    def price_increase(self):
        self.price = self.price + 50000

class SuperClass(Car):
    pass

honda = SuperClass('Civic', 2019, 100000)
tata = Car('Bolt', 2019, 100000)

honda.cc = 1500
# print(help(honda))
# print(honda.__dict__)

print(honda.price)