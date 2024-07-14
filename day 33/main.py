import requests
from datetime import datetime

#
#
# iss_position = (longitude, latitude)
# print(iss_position)
# print(data)
# from tkinter import *
#
#
# def get_quote():
#     response = requests.get(url="https://api.kanye.rest")
#     response.raise_for_status()
#     data = response.json()
#     kanye_quote = data["quote"]
#     canvas.itemconfig(quote_text, text=kanye_quote)
#     # Write your code here.
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(
#     150,
#     207,
#     text="Kanye Quote Goes HERE",
#     width=250,
#     font=("Arial", 30, "bold"),
#     fill="white",
# )
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
# #
# #
# window.mainloop()
# MY_LAT = 31.899160  # my latitude
# MY_LNG = 35.007408  # my longitude
#
#
# def is_iss_overhaed():
#     response = requests.get(url="http://api.open-notify.org/iss-now.json")
#     response.raise_for_status()
#
#     data = response.json()
#     iss_longitude = float(data["iss_position"]["longitude"])
#     iss_latitude = float(data["iss_position"]["latitude"])
#
#     if (
#         MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
#         and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5
#     ):
#         return True
#
#
# def is_night():
#     parameters = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}
#     response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
#     response.raise_for_status()
#     data = response.json()
#     sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
#     sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
#
#     time_now = datetime.now().hour
#
#     if time_now >= sunset or time_now <= sunrise:
#         return True
