# Day18 of my 100DaysOfCode Challenge
# Draw a dashed line using Turtle Graphics

from turtle import Turtle, Screen

groot = Turtle()

for _ in range(15):
    groot.forward(10)
    groot.penup()
    groot.forward(10)
    groot.pendown()


my_screen = Screen()
my_screen.exitonclick()

