from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.mainloop()

    # canvas = Canvas(height=250, width=300)
    # canvas.create_text(font=("Ariel", 20, "italic"))
    # canvas.grid(row=0, column=0)
