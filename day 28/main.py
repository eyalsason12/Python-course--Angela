from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 2 == 0:
        title_label.config(
            text="Break", font=(FONT_NAME, 50, "bold"), fg=PINK, background=YELLOW
        )
        short_break_sec = SHORT_BREAK_MIN * 60
        count_down(short_break_sec)
    elif reps % 8 == 0:
        title_label.config(
            text="Break", font=(FONT_NAME, 50, "bold"), fg=RED, background=YELLOW
        )
        long_break_sec = LONG_BREAK_MIN * 60
        count_down(long_break_sec)
    else:
        title_label.config(
            text="Work", font=(FONT_NAME, 50, "bold"), fg=GREEN, background=YELLOW
        )
        work_sec = WORK_MIN * 60
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    global mark
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark = ""
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodro")
window.config(padx=100, pady=50, background=YELLOW)


# label
title_label = Label(
    text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, background=YELLOW
)
title_label.grid(column=1, row=0)

check_mark = Label(fg=GREEN, font=(FONT_NAME, 15, "bold"), background=YELLOW)
check_mark.grid(column=1, row=3)

# button

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    103, 130, text=str("00:00"), fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)


window.mainloop()
