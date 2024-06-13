from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Ariel", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(arg=f"score={self.score}",  align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f"score={self.score}", move=False, align="center", font=("Ariel", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!", move=False, align="center", font=("Ariel", 24, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()






