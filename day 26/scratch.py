# numbers = [1, 2, 3]
# new_numbers = [item + 1 for item in numbers]
# print(new_numbers)

# name = "eyal"
# new_list = [letter for letter in name]
# print(new_list)

# new_range = [n * 2 for n in range(1, 5)]
# print(new_range)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# challenge 1
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n * n for n in numbers]
# print(squared_numbers)

# challenge 2
# list_of_strings = input().split(",")
# list_of_integers = [int(x) for x in list_of_strings]
# result = [num for num in list_of_integers if (num % 2) == 0]
# print(result)

# challenge 3

# import pandas

# with open("./file1.txt") as data_file_1:
#     data = data_file_1.readlines()
#     list1 = [int(num.strip()) for num in data]
# with open("./file2.txt") as data_file_2:
#     data = data_file_2.readlines()
#     list2 = [int(num.strip()) for num in data]
#
# result = [num for num in list1 if num in list2]
#
# print(result)

# import random
#
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student: random.randint(1, 100) for student in names}
# passed_students = {
#     student: score for (student, score) in students_scores.items() if score >= 60
# }
# print(passed_students)

# sentence = input()
# sentence_list = sentence.split()
# result = {word: len(word) for word in sentence_list}
# print(result)

# weather_c = eval(input())
# weather_f = {day: int((temp * 9 / 5) + 32) for (day, temp) in weather_c.items()}
# print(weather_f)

# input = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
