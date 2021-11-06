# Day8 of my 100DaysOfCode Challenge
# Problem

# You are provided an array A of N size  that contains non-negative integers. 
# Your task is to determine whether the number that is formed by selecting the last digit of all the N numbers is divisible by 10.

# Note: View the sample explanation section for more clarification.


# Input format

# First line: A single integer N denoting the size of array A
# Second line: N space-separated integers.


# Output format

# If the number is divisible by 10, then print 'Yes'. Otherwise, print 'No'.

# Constraints
# 1 <= N <= 10^5
# 0 <= A[i] <= 10^5

size = int(input("Enter the size of array: "))
array = list(map(int,input().split()))
element = array[size-1]
print(element)
if element % 10 == 0:
    print("Yes")
else:
    print("No")
