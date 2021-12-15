# Day19 of my 100DaysOfCode Challenge

from turtle import Turtle, Screen

groot = Turtle()
screen = Screen()


def move_forward():
    groot.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()


