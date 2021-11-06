# Day8 of my 100DaysOfCode Challenge
# Program to open a file to read it's contents

# open a file with read mode
# by default the mode is r i.e. read
file = open('Day8/sample.txt', 'r')
# data = file.read()

# specify no of characters to read in files
data = file.read(20)
print(data)
file.close()

