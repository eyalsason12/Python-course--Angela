
import turtle as t
from turtle import Turtle, Screen
import random


color_list = [(16, 11, 93), (127, 251, 206), (36, 182, 159), (235, 40, 3), (155, 11, 28), (211, 178, 208), (238, 67, 165), (247, 218, 23), (188, 6, 0), (38, 133, 244), (247, 217, 0), (211, 217, 231), (40, 109, 196), (130, 157, 207), (222, 122, 166), (222, 128, 117), (106, 192, 178), (228, 70, 49), (159, 60, 71), (51, 46, 107), (244, 162, 150), (137, 188, 253)]
t.colormode(255)
eyal = Turtle()

x = -460
y = -380

# set turtle in start position
def start_position_in_line():
    eyal.speed("fastest")
    eyal.penup()
    eyal.setpos(x, y)
    eyal.pendown()


# function that draw one line
def draw_line_of_dot():
    eyal.speed("slowest")
    for _ in range(9):
        random_color = random.choice(color_list)
        eyal.dot(20, random_color)
        eyal.penup()
        eyal.forward(50)
        eyal.pendown()
    eyal.dot(20, random_color)


#code: drawing 10 rows of dots in diffrent colors

for _ in range(10):
    start_position_in_line()
    draw_line_of_dot()
    y += 50


#show the screen

screen = Screen()
screen.exitonclick()
