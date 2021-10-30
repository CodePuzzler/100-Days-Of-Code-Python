# Day2 of my 100DaysOfCode Challenge
# Program to print Fibonacci series
# the sum of two elements defines the next

limit = int(input("Enter a number upto which you want to print the fibonacci series: "))

def printFibonacci(limit):
    a, b = 0, 1
    while a < limit:
        print(a)
        a, b = b, a+b

printFibonacci(limit)