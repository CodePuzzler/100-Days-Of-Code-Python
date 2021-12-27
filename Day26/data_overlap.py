# Day26 of 100 Days Of Code in Python
# get common numbers from two files using list comprehension

with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

result = [int(item) for item in file1_data if item in file2_data]

print(result)