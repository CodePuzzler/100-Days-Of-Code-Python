# Day9 of my 100DaysOfCode Challenge
# Program to calculate factorial from HackerEarth

# Problem

# You have been given a positive integer N. 
# You need to find and print the Factorial of this number. 
# The Factorial of a positive integer N refers to the product of 
# all number in the range from 1 to N. You can read more about the 
# factorial of a number here.

# Input Format:
# The first and only line of the input contains a single integer N 
# denoting the number whose factorial you need to find.

# Output Format
# Output a single line denoting the factorial of the number N.

# Constraints
# 1 <= N <= 10

class CalculateFactorial:
    def factorial(self):
        factorial = 1
        for i in range(1, self.num + 1):
            factorial = factorial * i
        return factorial

calculateFactorial = CalculateFactorial()
calculateFactorial.num = int(input("Enter Number to calculate factorial: "))

print(f"Factorial of {calculateFactorial.num} is: {calculateFactorial.factorial()}")


