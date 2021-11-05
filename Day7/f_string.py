# Day7 of my 100DaysOfCode Challenge
# Revision Exercises
# Program to print table of any number using f string

num = int(input("Enter any number you want to print the table for: "))
for i in range(1, 11):
    # print(str(num) + " X " + str(i) + " = " + str(num*i))

    # using f string
    print(f"{num} X {i} = {num*i}")