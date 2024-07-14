from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


def find_password():
    website = website_input.get()
    password = password_input.get()
    email = user_name_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="no Data File found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website,
                message=f"Email:{email}\nPassword:{password}",
            )
        else:
            messagebox.showinfo(
                title="Oops",
                message="no details for the website exists",
            )


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    password = password_input.get()
    email = user_name_input.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
logo = canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# lable

website_lable = Label(text="Website:")
website_lable.grid(column=0, row=1)
username_lable = Label(text="Email/Username:")
username_lable.grid(column=0, row=2)
password_lable = Label(text="Password:")
password_lable.grid(column=0, row=3)

# entry

website_input = Entry(width=42)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

user_name_input = Entry(width=42)
user_name_input.grid(column=1, row=2, columnspan=2, sticky="")
user_name_input.insert(0, "eyal@gmail.com")

password_input = Entry(width=24)
password_input.grid(column=1, row=3)

# buttons

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="")


window.mainloop()
