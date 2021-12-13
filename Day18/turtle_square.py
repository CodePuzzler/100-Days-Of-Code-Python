# Day18 of my 100DaysOfCode Challenge
# Draw a square using Turtle Graphics

from turtle import Turtle, Screen

groot = Turtle()

for _ in range(4):
    groot.forward(100)
    groot.left(90)


my_screen = Screen()
my_screen.exitonclick()
