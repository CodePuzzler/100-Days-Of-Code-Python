# Day10 of my 100DaysOfCode Challenge
# Program to check if a string is palindromic

# Problem

# You have been given a String S. You need to find and print whether this string is a palindrome or not. If yes, print "YES" (without quotes), else print "NO" (without quotes).

# Input Format
# The first and only line of input contains the String S. The String shall consist of lowercase English alphabets only.

# Output Format
# Print the required answer on a single line.

# Constraints 
# 1 <= |S| <= 100

# Note
# String S consists of lowercase English Alphabets only.

s = input("Enter a string to check if it's palindromic or not: ")
flag = 0
length = len(s)
for i in range(length):
    if (s[i] != s[length-i-1]):
        flag = 1
        break
if flag == 1:
    print("NO - Sring is not palindrome")
else:
    print("YES - String is palindrome")