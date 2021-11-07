# Day9 of my 100DaysOfCode Challenge
# Program to rename a file
import os

oldname = "Day9/new.txt"
newname = "Day9/new1.txt"

with open(oldname) as file:
    data = file.read()

with open(newname, "w") as file:
    file.write(data)

os.remove(oldname)