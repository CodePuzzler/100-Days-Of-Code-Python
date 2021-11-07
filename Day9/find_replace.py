# Day9 of my 100DaysOfCode Challenge
# Program to find and replace a word from a file

with open('Day9/sample.txt') as file:
    data = file.read()
    # print(data)

data = data.replace('dolar', '#######')

with open('Day9/sample.txt', 'w') as file:
    data = file.write(data)

with open('Day9/sample.txt', 'r') as file:
    newFile = file.read()
    print(newFile)