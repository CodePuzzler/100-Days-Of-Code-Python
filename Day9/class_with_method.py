# Day9 of my 100DaysOfCode Challenge
# Program to calculate sum of two numbers using c;ass and method

# class definition
class CalculateSum:
    def sum(self):
        return self.num1 + self.num2

calculateSum = CalculateSum()
calculateSum.num1 = int(input("Enter First number: "))
calculateSum.num2 = int(input("Enter Second number: "))

print("Sum of entered numbers is: ", calculateSum.sum())