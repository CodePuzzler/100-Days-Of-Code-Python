# Day18 of my 100DaysOfCode Challenge
# Draw a random walk using Turtle Graphics

from turtle import Turtle, Screen
import random

groot = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
groot.pensize(15)
groot.speed("fastest")

for _ in range(200):
    groot.color(random.choice(colours))
    groot.forward(30)
    groot.setheading(random.choice(directions))


my_screen = Screen()
my_screen.exitonclick()
