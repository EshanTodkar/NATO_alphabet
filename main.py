import pandas as pd

# Reads the csv file for NATO alphabet

data = pd.read_csv("./nato_phonetic_alphabet.csv")

# Create a dictionary in format {"A" : "Alfa"}

dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

# Take user input for word and convert it to upper to match format

user_input = input("Enter a word: ").upper()

# Create a new list that cross-references user input with dictionary

list1 = [dictionary[letter] for letter in user_input]

print(list1)
