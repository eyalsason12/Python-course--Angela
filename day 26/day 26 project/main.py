import pandas


# TODO 1. Creat a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Creat a list of the phonetic code words from the word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
