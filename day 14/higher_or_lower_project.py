import random

import game_data

from game_data import data

from random import randint


def compare_followers(followers_b, followers_a, compare_b):
    global user_score
    global end_game
    print(
        f"Against B: {compare_b["name"]}, a {compare_b['description']}, from {compare_b['country']}. followers number: {followers_b}"
    )
    # compare between score
    user_answer = input("who has more followers? Type 'A' or 'B': \n")
    if user_answer == "A" and followers_a > followers_b:
        user_score += 1
        print(followers_a)
        print(followers_b)
        print(f"you right! current score: {user_score}")

    elif user_answer == "B" and followers_b > followers_a:
        user_score += 1
        print(followers_a)
        print(followers_b)
        print(f"you right! current score: {user_score}")
    else:
        # end of the game
        end_game = True
        print(f"you lose! current score: {user_score}")


end_game = False
# genarate a random number
user_score = 0
number_a = randint(0, len(data) - 1)
compare_a = data[number_a]
followers_a = compare_a["follower_count"]

print(
    f"Compare A: {compare_a["name"]}, a {compare_a['description']}, from {compare_a['country']}.followers number: {followers_a} \n"
)


while not end_game:
    number_b = randint(0, len(data) - 1)
    while number_b == number_a:
        number_b = randint(0, len(data) - 1)
    compare_b = data[number_b]
    followers_b = compare_b["follower_count"]

    compare_followers(followers_b, followers_a, compare_b)
    print(
        f"Compare A: {compare_b["name"]}, a {compare_b['description']}, from {compare_b['country']}.followers number: {followers_b} \n"
    )
