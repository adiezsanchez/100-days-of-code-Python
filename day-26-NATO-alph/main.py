import pandas as pd

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {}

# Loop through dataframe rows and add a key:value pair per iteration:

for (index, row) in data.iterrows():
    nato_alphabet[row.letter] = row.code

# Create a dict, using dict comprehension iterating through the rows in a dataframe:

nato_alphabet_2 = {(row.letter):(row.code) for (index, row) in data.iterrows()}

#TODO 2. Create a dict and list of the phonetic code words from a word that the user inputs.

word_to_NATO = ""

while word_to_NATO != "EXIT":

    word_to_NATO = input("Which word would you like to spell?: ").upper()
    word_NATO_dict = {letter.upper():nato_alphabet_2[letter] for letter in word_to_NATO}
    word_NATO_list = [nato_alphabet_2[letter] for letter in word_to_NATO]

    print (word_NATO_dict)
    print (word_NATO_list)
