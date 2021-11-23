# Day5 of my 100DaysOfCode Challenge

# You are going to write a program that calculates the average student height from a List of heights.

student_heights = input("Input a list of student heights ").split()
total_height = 0
total_students = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total_height += student_heights[n]
    total_students += 1

print("total height =", total_height)
print("number of students =", total_students)
average_height = total_height / total_students
print(round(average_height))