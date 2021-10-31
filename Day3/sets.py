# Day3 of my 100DaysOfCode Challenge
# Program to use Sets and it's methods

# create an empty  set
set1 = set()
print(type(set1))

# add value to Sets
set1.add("amit")
print(set1)

# prints length of a set
print(len(set1))

set2 = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 }
set3 = { 8, 10, 12, 15, 46 }

# returns union of Sets
unionSet = set2.union(set3)
print(unionSet)

# returns intersection of sets
intersectionSets = set2.intersection(set3)
print(intersectionSets)

# Return True if all items in set3 are present in set2
subsetSet = set3.issubset(set2)
print(subsetSet)