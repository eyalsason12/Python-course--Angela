from game_data import data
from random import randint


def compare_followers(followers_b, followers_a, person_b):
    global end_game

    print(
        f"A: {person_a["name"]}, a {person_a['description']}, from {person_a['country']}. followers number: {followers_a}"
    )
    print(
        f"B: {person_b["name"]}, a {person_b['description']}, from {person_b['country']}. followers number: {followers_b}"
    )
    # compare between score
    user_answer = input("who has more followers? Type 'A' or 'B': \n")
    if user_answer == "A" and followers_a > followers_b:
        pass
    elif user_answer == "B" and followers_b > followers_a:
        pass
    else:
        end_game = True
        print(f"you lose! current score: {user_score}")
        return 0
    print(f"you right! current score: {user_score+1}")
    return 1


end_game = False
# genarate a random number
user_score = 0
number_a = randint(0, len(data) - 1)
person_a = data[number_a]
followers_a = person_a["follower_count"]

while not end_game:
    number_b = randint(0, len(data) - 1)
    print(f"{data[number_b]["name"]=} {data[number_a]["name"]=}")
    while data[number_b] == data[number_a]:
        print(f"{number_b=} {number_a=}")
        number_b = randint(0, len(data) - 1)
    if user_score:
        followers_a = followers_b
        person_a = person_b
    person_b = data[number_b]
    followers_b = person_b["follower_count"]

    user_score += compare_followers(followers_b, followers_a, person_b)
