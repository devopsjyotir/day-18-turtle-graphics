from turtle import Turtle, Screen

import heroes

print(heroes.gen())
# import turtle as t
amzy = Turtle()

# for i in range(4):
#     amzy.forward(100)
#     amzy.right(90)
# for i in range(20):
#     amzy.forward(10)
#     amzy.penup()
#     amzy.forward(10)
#     amzy.pendown()

num_of_sides = 3

while num_of_sides < 11:
    for j in range(num_of_sides):
        right_angle = 360 / num_of_sides
        amzy.forward(100)
        amzy.right(right_angle)
    num_of_sides += 1

screen = Screen()
screen.exitonclick()
