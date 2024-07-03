
import hangman_art

import random

import hangman_wordlist

from hangman_wordlist import word_list

from hangman_art import stages

from hangman_art import logo

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6
end_of_game = False
word_lenght = len(chosen_word)
display = []
for _ in range(word_lenght):
    display += "_"

while not end_of_game:

    guess = input('guess a letter: ').lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 1:
            print(f"You have {lives} last life left ")
        elif lives == 0:
            print(f"YOU have left {lives} lives")
            print("you loss the game")
            end_of_game = True
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if display.count("_") == 0:
        print(f"you won! the word is {chosen_word} ")
        end_of_game = True

    print(display)
    print(stages[lives])




