# Day27 of 100 Days Of Code in Python
# use *args for any number of arguments
# add any number for arguments using this function
def add(*args):
    total = 0
    for number in args:
        total += number
    return total


result = add(1, 5, 7, 8)
print(result)


# using many keyword arguments using **kwargs
# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)



