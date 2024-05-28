#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.

# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint

#choose a number to be guessed

number = randint(1, 100)

end_game = False

def game():
    global number
    global end_game
    if level_choice == 'easy':
        attempts = 10
    elif level_choice == 'hard':
        attempts = 5
    while not end_game:
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            end_game = True
        else:
            # Track the number of turns remaining.
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("make a guess: "))
            if guess == number:
                return print(f"You got it! The answer was {number}")
            else:
                attempts -= 1
                if guess > number:
                    print("Too high")
                elif guess < number:
                    print("Too low")
            if attempts > 0:
                print("guess again")



# Allow the player to submit a guess for a number between 1 and 100.
level_choice = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard':\n").lower()
game()



