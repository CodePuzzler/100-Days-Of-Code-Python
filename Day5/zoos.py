# Day5 of my 100DaysOfCode Challenge

# Problem

# You are required to enter a word that consists of x and y that denote the number of Zs and Os respectively. 
# The input word is considered similar to word zoo if 2 * x = y.

# Determine if the entered word is similar to word zoo.

# For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

# Input format

# First line: A word that starts with several Zs and continues by several Os.
# Note: The maximum length of this word must be 20.

word = input("Enter a word that starts with several Zs and continues by several Os: ")

if len(word) <= 20:
    num_of_z = 0
    num_of_o = 0

for i in word :
    if i[0] == 'z':
        num_of_z += 1
    elif i[0] == 'o':
        num_of_o += 1

if num_of_o == num_of_z * 2:
    print("Yes")
else :
    print("No")