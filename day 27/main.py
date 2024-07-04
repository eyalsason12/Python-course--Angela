from tkinter import *

window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=500, height=300)

# Label

is_equal_label = Label(text="is equal to", font=("Ariel", 10, "bold"))
is_equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles", font=("Ariel", 10, "bold"))
miles_label.grid(column=2, row=0)

kilometers_label = Label(text="Km", font=("Ariel", 10, "bold"))
kilometers_label.grid(column=2, row=1)

# Entry

input = Entry(width=10)
input.grid(column=1, row=0)


km = Label(text=0, font=("Ariel", 15, "bold"))
km.grid(column=1, row=1)


def calculate():
    result = int(input.get()) * 1.609
    km.config(text=round(result))


# button

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
