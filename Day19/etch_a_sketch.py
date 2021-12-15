# Day19 of my 100DaysOfCode Challenge

from turtle import Turtle, Screen

groot = Turtle()
screen = Screen()


def move_forward():
    groot.forward(10)


def move_backward():
    groot.backward(10)


def move_left():
    groot.left(10)


def move_right():
    groot.right(10)


def clear():
    groot.clear()
    groot.penup()
    groot.home()
    groot.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.exitonclick()
