from turtle import Turtle, Screen
import random
# import turtle as t

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270, 360]
amzy = Turtle()
# num_of_sides = 3
#
# while num_of_sides < 11:
#     amzy.pencolor(random.choice(colors))
#     for j in range(num_of_sides):
#         right_angle = 360 / num_of_sides
#         amzy.forward(100)
#         amzy.right(right_angle)
#     num_of_sides += 1

coin_flip = ['heads', 'tails']
i = 0
while i < 100:
    amzy.speed(10)
    amzy.pensize(10)
    amzy.hideturtle()
    amzy.pencolor(random.choice(colors))
    amzy.forward(20)
    amzy.setheading(random.choice(directions))
    i += 1















screen = Screen()
screen.exitonclick()