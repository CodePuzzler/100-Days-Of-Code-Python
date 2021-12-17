# Day20 of my 100DaysOfCode Challenge
# TODO: Create a snake body
# TODO: Move the snake
# TODO: Control the snake
# TODO: Detect collision with food
# TODO: create a scoreboard
# TODO: detect collision with wall
# TODO: detect collision with tail

from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
# food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()


