# Day5 of my 100DaysOfCode Challenge
# Program to check whether a number is prime or not

num = int(input("Enter a number to check if it's a prime number or not: "))
prime = True
if (num == 1) or (num == 0):
     prime = False
for i in range(2, num):
    if (num % i) == 0:
        prime = False
if (prime == False):
    print("Entered Number is not a prime number")
else:
    print("Entered Number is a prime number")
