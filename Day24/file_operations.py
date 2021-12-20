# Day24 of my 100DaysOfCode Challenge
# Program to read the contents of a file

# Read a file
# file = open("abc.txt")
# contents = file.read()
# print(contents)
# file.close()

# Another way to open a file, default mode is read only
with open("abc.txt") as file:
    contents = file.read()
    print(contents)

# Write to file, change mode to "w"
# create a file if it doesn't exist
with open("abc.txt", mode="w") as file:
    file.write("New Text")

# Append to file, change mode to "a"
with open("abc.txt", mode="a") as file:
    file.write("\nMy name is Amit.")
