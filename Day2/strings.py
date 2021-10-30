# Day2 of my 100DaysOfCode Challenge
# Program to use string function, string.replace

template = '''Hello <|Name|>,
    Welcome to 100 Days of Code challenge.
    We are glad to have you here.'''

name = input("Enter your name: ")
template = template.replace("<|Name|>", name)

print(template)
