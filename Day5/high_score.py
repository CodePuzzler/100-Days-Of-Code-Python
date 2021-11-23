# Day5 of my 100DaysOfCode Challenge

# You are going to write a program that calculates the highest score from a List of scores.

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
for n in range(0, len(student_scores)):
    if (highest_score < student_scores[n]):
        highest_score = student_scores[n]
    else:
        highest_score = highest_score

print(f"The highest score in the class is: {highest_score}")