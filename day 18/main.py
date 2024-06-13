import turtle as t

import random


eyal = t.Turtle()
t.colormode(255)
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return eyal.pencolor(r, g, b)


def random_walk():
    for _ in range(200):
        eyal.speed("fastest")
        eyal.pensize(10)
        random_color()
        eyal.forward(50)
        eyal.right(random.choice(directions))


def draw_circle():
    random_color()
    eyal.speed("fastest")
    eyal.circle(100, 360)
    eyal.right(4)


for _ in range(90):
    draw_circle()
# random_walk()

screen = t.Screen()
screen.exitonclick()
