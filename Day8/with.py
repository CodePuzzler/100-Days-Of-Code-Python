# Day8 of my 100DaysOfCode Challenge
# Program to use with statement

with open('Day8/new.txt', 'w') as file:
    newFile = file.write("Hello, welcome to Earth")
    
with open('Day8/new.txt', 'r') as file:
    newFile = file.read()
# print(newFile)

print(newFile)