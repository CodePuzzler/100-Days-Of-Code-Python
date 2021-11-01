# Day4 of my 100DaysOfCode Challenge
# Program to use while loop
# Program to print sum of natural numbers

limit = int(input("Enter a natural number upto which you want to calculate the sum: "))
i = 1
sum = 0

while (i <= limit):
    sum = sum + i
    i += 1

print("sum of natural nuumbers you want: ", sum)
