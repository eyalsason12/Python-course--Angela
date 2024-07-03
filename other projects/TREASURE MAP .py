line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
column = position[0]
row = int(position[1])
if column == 'A':
    column = 0
elif column == 'B':
    column = 1
elif column == 'C':
    column = 2
if row == 0:
    row = 0
elif row == 1:
    row = 1
elif row == 2:
    row = 2

map[row -1][column] = 'x'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")