## First Exercise
# fruits = eval(input())
# # 🚨 Do not change the code above
#
#
# # TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print(f"Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# # 🚨 Do not change the code below
# make_pie(4)

## Second Exercise
# # eval() function will create a list of dictionaries using the input
# facebook_posts = eval(input())
#
# total_likes = 0
# # TODO: Catch the KeyError exception
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post["Likes"]
#     except KeyError:
#         pass
#         # post["Likes"] = 0
#
#
# print(total_likes)
