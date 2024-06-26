# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#         else:
#             pass
#     print(temperatures)

import pandas

main_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_data = main_data["Primary Fur Color"].to_list()
gray_num = 0
black_num = 0
red_num = 0
for color in color_data:
    if color == 'Gray':
        gray_num += 1
    elif color == 'Cinnamon':
        red_num += 1
    elif color == 'Black':
        black_num += 1
    else:
        pass


data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_num, red_num, black_num]
}
# data = pandas.DataFrame(data_dict)
# data.to_csv("color_amount_data.csv")
data = pandas.read_csv("weather_data.csv")
#
# #print the average
#
# # temp_list = data["temp"].to_list()
# # amount_of_days = len(temp_list)
# # total = 0
# #
# # for temp in temp_list:
# #     total += temp
# #
# # average_temp = total/amount_of_days
# # print(round(average_temp, 2))
#
# # also we can just
# # print(data["temp"].mean())
# # print(data)
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp[0])
# monday_temp_f = (monday_temp * 1.8) + 32
# print(monday_temp_f)
print(monday_temp)