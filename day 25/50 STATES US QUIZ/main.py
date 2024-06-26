import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title =f"{len(guessed_states)}/50", prompt = "What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        all_states.remove(answer_state)
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

data = pandas.DataFrame(all_states)
data.to_csv("states_to_learn.csv")



















# def get_mouse_click_coor(x,y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# #keeping screen open
# turtle.mainloop()
