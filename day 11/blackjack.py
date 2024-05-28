############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards: list):
    if sum(cards) == 21 and len(cards) == 2:
        return sum(cards)
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "draw"
    elif computer_score == 21:
        return "you lose opponent has blackjack"
    elif player_score == 21:
        return "you win with a blackjack"
    elif player_score > 21:
        return "you went over, you lose"
    elif computer_score > 21:
        return "opponent went over, you won"
    elif player_score > computer_score:
        return "you win by passing the computer score"
    else:
        return "you lose, computer pass you"

def play_game():
    player_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f" your cards: {player_cards}, current score: {player_score}")
        print(f" computer's first card: {computer_cards[0]}")


        if player_score == 21 or computer_score == 21 or player_score > 21:
            is_game_over = True
        else:
            player_answer = input("would you like do draw another card? type 'y' or 'n' \n")
            if player_answer == 'y':
                player_cards.append(deal_cards())
                calculate_score(player_cards)
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)


    print(f" your final hand: {player_cards}, final score: {player_score}")
    print(f" computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("do you want to play a game of blackjack? type 'y' to start or type 'n' \n") == 'y':
    play_game()









