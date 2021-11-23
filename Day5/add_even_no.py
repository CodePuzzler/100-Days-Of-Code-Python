# Day5 of my 100DaysOfCode Challenge

# write a program that calculates the sum of all the even numbers from 1 to 100.

#Write your code below this row 👇
sum = 0
for n in range(1, 101):
    if n % 2 == 0:
        sum += n

print(sum)
