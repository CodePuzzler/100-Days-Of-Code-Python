# Day7 of my 100DaysOfCode Challenge
# Program to calculate factorial using recursive function

def factorial_iter(n):
    factorial = 1
    for i in range(n):
        factorial = factorial * (i+1)
    return factorial

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)

num = int(input("Enter a number to calculate factorial: "))
# f = factorial_iter(num)
f = factorial_recursive(num)
print(f"Factorial of {num} is: {f}")