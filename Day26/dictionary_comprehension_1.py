# Day26 of 100 Days Of Code in Python
# calculate numbers of letters in each word using dictionary comprehension

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
words = sentence.split()

result = {word: len(word) for word in words}

print(result)
