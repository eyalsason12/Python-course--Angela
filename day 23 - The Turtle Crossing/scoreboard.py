from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-140, 260)
        self.write(f"LEVEL: {self.level}", align="right", font=FONT)
        self.point_increase()

    def point_increase(self):
        self.level += 1

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
