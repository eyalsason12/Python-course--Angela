rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


import random

user_choise = int(
    input("what is your choice? 0 for ROCK, 1 for PAPER or 2 for SCISSORS ")
)

computer_choise = random.randint(0, 2)

if user_choise == 0:
    print(rock)
    if computer_choise == 0:
        print(f"computer chose:\n{rock}\nIts a tie, play again")
    elif computer_choise == 1:
        print(f"computer chose\n{paper}\nYou lose!")
    elif computer_choise == 2:
        print(f"computer chose\n{scissors}\nYou win!")
elif user_choise == 1:
    print(paper)
    if computer_choise == 0:
        print(f"computer chose:\n{rock}\nYou win!")
    elif computer_choise == 1:
        print(f"computer chose\n{paper}\nIts a tie, play again")
    elif computer_choise == 2:
        print(f"computer chose\n{scissors}\n You lose!")
elif user_choise == 2:
    print(scissors)
    if computer_choise == 0:
        print(f"computer chose:\n{rock}\nYou lose!")
    elif computer_choise == 1:
        print(f"computer chose\n{paper}\nyou win!")
    elif computer_choise == 2:
        print(f"computer chose\n{scissors}\n Its a tie, play again!")
else:
    print("you chose invalid number, you lose!")
