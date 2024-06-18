from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Ariel", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(
            arg=f"score:{self.score} highest score:{self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(
            arg=f"score:{self.score} highest score:{self.high_score}",
            move=False,
            align="center",
            font=("Ariel", 24, "normal"),
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{int(self.high_score)}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
