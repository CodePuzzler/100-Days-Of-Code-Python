# Day18 of my 100DaysOfCode Challenge

# Extracted colors from an image
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)
#
# print(rgb_colors)

# Output of above code [Rgb(r=245, g=243, b=238), Rgb(r=246, g=242, b=244), Rgb(r=202, g=164, b=110), Rgb(r=240,
# g=245, b=241), Rgb(r=236, g=239, b=243), Rgb(r=149, g=75, b=50), Rgb(r=222, g=201, b=136), Rgb(r=53, g=93, b=123),
# Rgb(r=170, g=154, b=41), Rgb(r=138, g=31, b=20), Rgb(r=134, g=163, b=184), Rgb(r=197, g=92, b=73), Rgb(r=47, g=121,
# b=86), Rgb(r=73, g=43, b=35), Rgb(r=145, g=178, b=149), Rgb(r=14, g=98, b=70), Rgb(r=232, g=176, b=165), Rgb(r=160,
# g=142, b=158), Rgb(r=54, g=45, b=50), Rgb(r=101, g=75, b=77), Rgb(r=183, g=205, b=171), Rgb(r=36, g=60, b=74),
# Rgb(r=19, g=86, b=89), Rgb(r=82, g=148, b=129), Rgb(r=147, g=17, b=19), Rgb(r=27, g=68, b=102), Rgb(r=12, g=70,
# b=64), Rgb(r=107, g=127, b=153), Rgb(r=176, g=192, b=208), Rgb(r=168, g=99, b=102)]


import turtle as turtle_module
import random

turtle_module.colormode(255)
groot = turtle_module.Turtle()
groot.speed("fastest")
groot.penup()
groot.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

groot.setheading(225)
groot.forward(300)
groot.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    groot.dot(20, random.choice(color_list))
    groot.forward(50)

    if dot_count % 10 == 0:
        groot.setheading(90)
        groot.forward(50)
        groot.setheading(180)
        groot.forward(500)
        groot.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()

