# Day2 of my 100DaysOfCode Challenge
# Program to print remainder of two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def remainder(num1, num2):
    result = (num1 % num2)
    print("The remainder is: ", result)

remainder(num1, num2)
