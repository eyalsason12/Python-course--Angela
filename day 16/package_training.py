# import another_module
#
#
# print(another_module.another_veriable)


# from turtle import Turtle, Screen
#
#
# eyal = Turtle()
# eyal.shape("turtle")
# eyal.color("green")
# eyal.forward(100)
# eyal.position()
# print(eyal.showturtle())
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column(
    "pokemon name",
    ["Goldeen", "Seaking", "Pikachu", "Beedrill", "Weedle", "Pansear", "Psyduck"],
    "l",
)
table.add_column(
    "Type",
    ["water", "water", "electric", "poison", "poison", "fire", "water"],
)

print(table)
