# Day30 of my 100DaysOfCode Challenge
# program to learn Catching exceptions(try, except, else, finally)

# FileNotFound
try:
    file = open("a_file.txt")
except FileNotFoundError:
    # print("File Not Found")
    file = open("a_file.txt", "w")
    file.write("something")

# KeyError, TypeError with else
try:
    a_dictionary = {"key": "value"}
    print(a_dictionary["asdf"])
except KeyError as error_message:
    print(f"The key {error_message} does not exists")
# if everything works that else will be triggered
else:
    print("everything is working fine")
finally:
    file.close()
    print("Finally block always executes irrespective of an exception being thrown or not.")
    # raise TypeError("raised a type error")

# IndexError
fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)


# KeyError
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass


print(total_likes)

