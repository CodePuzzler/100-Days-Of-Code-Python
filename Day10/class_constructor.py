# Day10 of my 100DaysOfCode Challenge
# program with a class, a function and constructor

class Car():
    def __init__(self, modelName, yearM, price):
        self.modelName = modelName
        self.yearM = yearM
        self.price = price

    def price_increase(self):
        self.price = self.price + 50000

honda = Car('City', 2017, 800000)
tata = Car('Nano', 2016, 100000)

honda.cc = 1500

# print(honda.__dict__)
# print(tata.__dict__)
print(honda.price)
honda.price_increase()
print(honda.price)
