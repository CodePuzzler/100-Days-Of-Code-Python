# Day7 of my 100DaysOfCode Challenge
# Program to print a pyramid of stars

rowsCount = int(input("Enter the number of rows: "))
for i in range(rowsCount):
    print(" " * (rowsCount-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (rowsCount-i-1))
    