# Day5 of my 100DaysOfCode Challenge
# Program to print factorial of any number

num = int(input("Enter any number: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("Factorial of entered number is: ", factorial)