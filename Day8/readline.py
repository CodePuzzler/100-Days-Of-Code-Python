# Day8 of my 100DaysOfCode Challenge
# Program to open a file to read it's contents line by line

file = open('Day8/sample.txt', 'r')

# Read first line
data = file.readline()
print(data)

# Read second line
data = file.readline()
print(data)

# Read third line
data = file.readline()
print(data)


file.close()
