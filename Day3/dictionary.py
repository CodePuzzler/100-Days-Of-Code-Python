# Day3 of my 100DaysOfCode Challenge
# Program to use various Dictionary methods

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "numbers": [1, 2, 3, 4],
  "anotherDict": { "name" : "Amit"}
}

# prints the dicitonary
print(thisdict)

# prints a value of a specified key
print(thisdict['numbers'])

# print keys of dictionary
print(thisdict.keys())

# print values of dictionary
print(thisdict.values())

# prints a list containing a tuple for each key value pair
print(thisdict.items())

# updates a dictionary
updateDict = {"phone":"8545xxx"}
thisdict.update(updateDict)
print(thisdict)

# returns the value of the item with the specified key
# return none if key is not found
print(thisdict.get("model"))